// Student self-check page. problems.json is written by scripts/publish-site.mjs.
// Routes: #            all problems
//         #u08         all problems, scrolled to unit 08
//         #08-hw1      one problem
const TYPE_NAME = { oracle: '黑箱題', tests: '抓錯題', classic: '傳統題' }
const $ = (sel, el = document) => el.querySelector(sel)
const h = (tag, attrs = {}, ...kids) => {
  const el = document.createElement(tag)
  for (const [k, v] of Object.entries(attrs)) {
    if (k.startsWith('on')) el.addEventListener(k.slice(2), v)
    else if (v !== false && v != null) el.setAttribute(k, v === true ? '' : v)
  }
  for (const k of kids.flat()) if (k != null) el.append(k)
  return el
}
// replaceChildren would print a skipped (null) branch as the text "null".
const fill = (el, ...kids) => el.replaceChildren(...kids.flat().filter(k => k != null))
const decode = b64 => new TextDecoder().decode(Uint8Array.from(atob(b64), c => c.charCodeAt(0)))
const normalize = s => s.replace(/\r\n/g, '\n').split('\n').map(l => l.trimEnd()).join('\n').replace(/\n+$/, '')
const store = {
  get(k) { try { return localStorage.getItem(`oj:${k}`) } catch { return null } },
  set(k, v) { try { localStorage.setItem(`oj:${k}`, v) } catch {} },
}

// ---------------------------------------------------------------------------
// Python runner: one worker at a time; on timeout the worker is killed and replaced.
const statusEl = $('#status')
let worker, ready, queue = Promise.resolve(), seq = 0
function spawn() {
  worker = new Worker('worker.js')
  ready = new Promise((resolve, reject) => {
    worker.onmessage = e => {
      if (e.data.type === 'ready') { statusEl.className = 'status ready'; statusEl.textContent = 'Python 已就緒。'; resolve() }
      if (e.data.type === 'failed') reject(e.data.message)
    }
    worker.onerror = e => reject(e.message)
  }).catch(msg => {
    statusEl.className = 'status failed'
    statusEl.textContent = `Python 載入失敗，請確認網路連線後重新整理頁面。（${msg}）`
    throw msg
  })
}
spawn()

function runPython(code, stdin, timeoutSec = 3) {
  const job = queue.then(() => ready).then(() => new Promise(resolve => {
    const id = ++seq
    const timer = setTimeout(() => {
      worker.terminate()
      statusEl.className = 'status'
      statusEl.textContent = '程式執行太久，已停止；Python 重新載入中…'
      spawn()
      resolve({ timeout: true, stdout: '', error: null })
    }, timeoutSec * 1000)
    worker.onmessage = e => { if (e.data.id === id) { clearTimeout(timer); resolve(e.data) } }
    worker.postMessage({ id, code, stdin })
  }))
  queue = job.catch(() => {})
  return job
}
const withNewline = s => (s.endsWith('\n') ? s : s + '\n')

// ---------------------------------------------------------------------------
let data
fetch('problems.json').then(r => r.json()).then(d => { data = d; route() })
addEventListener('hashchange', route)

function route() {
  const id = decodeURIComponent(location.hash.slice(1))
  const app = $('#app')
  app.replaceChildren()
  const problem = data.units.flatMap(u => u.problems.map(p => ({ ...p, unit: u }))).find(p => p.id === id)
  if (problem) { document.title = `${problem.title} · 線上練習`; app.append(...problemView(problem)); scrollTo(0, 0); return }
  document.title = '線上練習'
  app.append(...listView())
  if (id.startsWith('u')) $(`#${CSS.escape(id)}`)?.scrollIntoView()
}

function listView() {
  return [
    h('div', { class: 'eyebrow' }, 'VIBE CODING WITH PYTHON'),
    h('h1', {}, '線上練習'),
    h('p', { class: 'lead' }, '在瀏覽器裡執行 Python，自己檢查作業。這裡的結果不算成績。 ', h('a', { href: '../' }, '← 回課程首頁')),
    ...data.units.map(u => h('section', { class: 'unit', id: `u${u.num}` },
      h('h2', {}, `單元 ${u.num}　${u.title}`),
      h('div', { class: 'list' }, u.problems.map(p => h('a', { class: 'item', href: `#${p.id}` },
        h('span', { class: 'tag' }, TYPE_NAME[p.type]), h('strong', {}, p.title)))))),
  ]
}

function problemView(p) {
  const head = [
    h('a', { href: `#u${p.unit.num}` }, '← 所有練習'),
    h('div', { class: 'eyebrow', style: 'margin-top:12px' }, `單元 ${p.unit.num} · ${TYPE_NAME[p.type]}`),
    h('h1', {}, p.title),
  ]
  const readme = h('div', { class: 'readme' })
  readme.innerHTML = marked.parse(p.readme)
  const body = p.type === 'tests' ? testsPanels(p) : [
    p.type === 'oracle' ? blackBoxPanel(p) : null,
    p.aiFormat ? aiFormatPanel(p) : null,
    examplesPanel(p),
    codePanel(p),
  ]
  return [...head, readme, ...body]
}

// ---------------------------------------------------------------------------
function blackBoxPanel(p) {
  const oracle = decode(p.oracle)
  const lines = (p.tryPlaceholder ?? '').split('\n').length
  const input = h('textarea', { rows: Math.max(lines, 2), class: 'mono', placeholder: p.tryPlaceholder ?? '' })
  const out = h('div')
  const shown = r => r.timeout ? '（執行太久，已停止）' : r.stdout || '（什麼都沒印）'
  const busy = on => { btn.disabled = on; cmp.disabled = on }
  const btn = h('button', { class: 'primary', type: 'button', onclick: async () => {
    busy(true)
    const r = await runPython(oracle, withNewline(input.value), p.timeout)
    busy(false)
    fill(out, h('div', { class: 'label muted' }, '黑箱的回答：'), h('pre', {}, shown(r)))
  } }, '執行黑箱')
  // Same input through the black box and the student's program: the self-check that
  // matters once the public examples pass.
  const cmp = h('button', { type: 'button', onclick: async () => {
    const code = $('#code')?.value ?? ''
    if (!code.trim()) { fill(out, h('div', { class: 'result note' }, '下方的程式框還是空的，先貼上你的程式。')); return }
    busy(true)
    const stdin = withNewline(input.value)
    const a = await runPython(oracle, stdin, p.timeout)
    const b = await runPython(code, stdin, p.timeout)
    busy(false)
    const same = !b.timeout && !b.error && normalize(a.stdout) === normalize(b.stdout)
    fill(out,
      h('div', { class: `result ${same ? 'ok' : 'bad'}` }, same ? '✓ 一模一樣' : '✗ 不一樣：你的規格（或 AI 的程式）漏掉了這裡的規則'),
      h('div', { class: 'label muted' }, '黑箱的回答：'), h('pre', {}, shown(a)),
      h('div', { class: 'label muted' }, '你的程式印出：'), h('pre', {}, shown(b)),
      b.error ? [h('div', { class: 'label muted' }, '錯誤訊息：'), h('pre', {}, b.error)] : null)
  } }, '也跑我的程式，比對')
  return h('section', { class: 'panel black' },
    h('h2', {}, '試試黑箱'),
    h('p', { class: 'muted' }, '在框裡輸入資料，按「執行黑箱」，看它怎麼回答。貼上你的程式以後，可以按「也跑我的程式，比對」，用同一個輸入比較兩邊。'),
    input, h('div', { class: 'row' }, btn, cmp), out)
}

function copyButton(text) {
  const b = h('button', { type: 'button', onclick: async () => {
    try { await navigator.clipboard.writeText(text); b.textContent = '已複製' } catch { b.textContent = '請手動選取' }
    setTimeout(() => { b.textContent = '複製' }, 1500)
  } }, '複製')
  return b
}

function aiFormatPanel(p) {
  return h('section', { class: 'panel' },
    h('h2', {}, '給 AI 的格式說明'),
    h('p', { class: 'muted' }, '這段只說明輸入和輸出的格式，沒有規則。規則要你自己從黑箱找出來，再寫進 Prompt。'),
    h('pre', {}, p.aiFormat), h('div', { class: 'row' }, copyButton(p.aiFormat)))
}

function examplesPanel(p) {
  return h('section', { class: 'panel' },
    h('h2', {}, '範例'),
    h('table', { class: 'examples' },
      h('thead', {}, h('tr', {}, h('th', {}, '#'), h('th', {}, '輸入'), h('th', {}, '應該印出'))),
      h('tbody', {}, p.examples.map((ex, i) => h('tr', {},
        h('td', {}, String(i + 1)),
        h('td', {}, h('pre', {}, ex.in), copyButton(ex.in)),
        h('td', {}, h('pre', {}, ex.out)))))))
}

function codePanel(p) {
  const key = `${p.id}:code`
  const code = h('textarea', { id: 'code', class: 'code', spellcheck: 'false', placeholder: p.type === 'oracle' ? '把你的程式（AI 給你的那一整段）貼在這裡' : '' })
  code.value = store.get(key) ?? p.starter ?? ''
  code.addEventListener('input', () => store.set(key, code.value))
  code.addEventListener('keydown', e => {
    if (e.key !== 'Tab') return
    e.preventDefault()
    code.setRangeText('    ', code.selectionStart, code.selectionEnd, 'end')
    store.set(key, code.value)
  })
  const file = h('input', { type: 'file', accept: '.py,.txt', hidden: true, onchange: async () => {
    if (!file.files[0]) return
    code.value = await file.files[0].text()
    store.set(key, code.value)
  } })
  const results = h('div')
  const btn = h('button', { class: 'primary', type: 'button', onclick: async () => {
    btn.disabled = true
    fill(results, h('div', { class: 'result note' }, '執行中…'))
    const items = []
    let passed = 0
    let stopped = false
    for (const [i, ex] of p.examples.entries()) {
      const r = await runPython(code.value, withNewline(ex.in), p.timeout)
      const ok = !r.timeout && !r.error && normalize(r.stdout) === normalize(ex.out)
      if (ok) passed++
      items.push(exampleResult(i, ex, r, ok))
      // Each timeout reloads Python, so stop here instead of timing out on every example.
      if (r.timeout) { stopped = i < p.examples.length - 1; break }
    }
    btn.disabled = false
    const all = passed === p.examples.length
    fill(results,
      h('div', { class: `result ${all ? 'ok' : 'bad'} big` }, `範例通過 ${passed}／${p.examples.length}`),
      all && p.type === 'oracle' ? h('div', { class: 'result note' }, '範例全過了，但範例只示範最普通的情況。到上方「試試黑箱」輸入你找到的特殊情況，按「也跑我的程式，比對」，每一個都要一模一樣。') : null,
      ...items,
      stopped ? h('div', { class: 'result note' }, '程式執行太久，後面的範例先不執行。修好以後再按一次「檢查範例」。') : null)
  } }, '檢查範例')
  const reset = p.starter ? h('button', { type: 'button', onclick: () => {
    if (confirm('要把程式框還原成一開始的內容嗎？你改過的會不見。')) { code.value = p.starter; store.set(key, code.value) }
  } }, '還原') : null
  return h('section', { class: 'panel' },
    h('h2', {}, p.type === 'oracle' ? '貼上你的程式' : '你的程式'),
    code,
    h('div', { class: 'row' }, btn, h('button', { type: 'button', onclick: () => file.click() }, '從檔案載入…'), reset, file),
    results)
}

function exampleResult(i, ex, r, ok) {
  if (ok) return h('div', { class: 'result ok' }, `✓ 範例 ${i + 1} 通過`)
  const why = r.timeout ? '執行太久（可能是無窮迴圈，或程式在等更多輸入）'
    : r.error ? '程式出現錯誤' : '印出的內容不一樣'
  return h('div', { class: 'result bad' },
    h('div', {}, `✗ 範例 ${i + 1}：${why}`),
    h('div', { class: 'label' }, '輸入'), h('pre', {}, ex.in),
    h('div', { class: 'label' }, '應該印出'), h('pre', {}, ex.out),
    h('div', { class: 'label' }, '你的程式印出'), h('pre', {}, r.stdout || '（什麼都沒印）'),
    r.error ? [h('div', { class: 'label' }, '錯誤訊息'), h('pre', {}, r.error)] : null)
}

// ---------------------------------------------------------------------------
// Bug-hunt task: the page shows a buggy program; the student types inputs (its output appears
// by itself) and the correct answer by the spec. A row whose answer matches the correct version
// while the buggy program prints something else has caught the bug.
function testsPanels(p) {
  const oracle = decode(p.oracle)
  return p.bugs.map((bug, i) => bugPanel(p, oracle, bug, p.bugs.length > 1 ? i + 1 : null))
}

const shownRun = r => r.timeout ? '（執行太久，已停止）'
  : r.error ? `（程式當掉）${r.error.trim().split('\n').pop()}` : r.stdout || '（什麼都沒印）'
const failed = (r, want) => r.timeout || r.error || normalize(r.stdout) !== normalize(want)

function bugPanel(p, oracle, bug, num) {
  const key = `${p.id}:cases:${num ?? 1}`
  const tbody = h('tbody')
  const results = h('div')
  const rowsData = () => [...tbody.rows].map(tr => ({ in: tr._in.value, out: tr._out.value }))
  const save = () => store.set(key, JSON.stringify(rowsData()))
  const active = tr => tr._in.value.trim() !== '' || tr._out.value.trim() !== ''

  // Run the buggy program for one row and show what it prints.
  const runBug = async tr => {
    if (!active(tr)) { tr._got.replaceChildren(); return null }
    const inp = tr._in.value
    const r = await runPython(bug.code, inp + '\n', p.timeout)
    if (tr._in.value === inp) fill(tr._got, h('pre', {}, shownRun(r)))
    return r
  }
  const addRow = (c = { in: '', out: '' }) => {
    const n = tbody.rows.length + 1
    let timer
    const inEl = h('input', { type: 'text', value: c.in, placeholder: n === 1 ? p.inputPlaceholder : '', oninput: () => {
      save(); tr._verdict.replaceChildren()
      clearTimeout(timer); timer = setTimeout(() => runBug(tr), 400)
    } })
    const outEl = h('input', { type: 'text', value: c.out, placeholder: n === 1 ? p.outputPlaceholder : '', oninput: () => { save(); tr._verdict.replaceChildren() } })
    const tr = h('tr', {}, h('td', {}, String(n)), h('td', {}, inEl), h('td', { class: 'got' }), h('td', {}, outEl), h('td', { class: 'verdict' }))
    Object.assign(tr, { _in: inEl, _out: outEl, _got: tr.cells[2], _verdict: tr.cells[4] })
    tbody.append(tr)
    if (c.in.trim() || c.out.trim()) runBug(tr)
  }
  let saved = []
  try { saved = JSON.parse(store.get(key) ?? '[]') } catch {}
  for (let i = 0; i < Math.max(saved.length, 3); i++) addRow(saved[i])

  const btn = h('button', { class: 'primary', type: 'button', onclick: async () => {
    btn.disabled = true
    fill(results, h('div', { class: 'result note' }, '檢查中…'))
    let caught = 0, wrong = 0, checked = 0
    for (const tr of tbody.rows) {
      const cell = tr._verdict
      cell.replaceChildren()
      if (!active(tr)) continue
      checked++
      const inp = tr._in.value
      const want = await runPython(oracle, inp + '\n', p.timeout)
      const got = await runBug(tr)
      let verdict
      if (want.error || want.timeout) verdict = h('span', { class: 'cell-bad' }, '這個輸入不符合規格')
      else if (!tr._out.value.trim()) verdict = h('span', { class: 'muted' }, '填上正確答案')
      else if (normalize(want.stdout) !== normalize(tr._out.value)) { wrong++; verdict = h('span', { class: 'cell-bad' }, '✗ 正確答案不對，照規格再算一次') }
      else if (failed(got, want.stdout)) { caught++; verdict = h('span', { class: 'cell-ok' }, '✓ 抓到錯了！') }
      else verdict = h('span', { class: 'muted' }, '程式這次答對了')
      cell.append(verdict)
    }
    btn.disabled = false
    fill(results,
      !checked ? h('div', { class: 'result note' }, '表格還是空的，先填一組輸入和正確答案。')
        : caught ? [h('div', { class: 'result ok big' }, '抓到了！這個輸入讓 AI 的程式印錯。'),
          h('p', { class: 'muted' }, h('i', {}, '說說看：是程式的哪幾行讓它出錯？要怎麼改？'))]
        : h('div', { class: 'result bad' }, wrong
          ? `有 ${wrong} 列的正確答案不對；答案不對的列不能拿來抓錯。`
          : '還沒抓到。想想：最前面、最後面、什麼都沒有、剛好在分界上的輸入。'))
  } }, '檢查')

  return h('section', { class: 'panel' },
    h('h2', {}, num ? `AI 寫的程式 ${num}` : 'AI 寫的程式'),
    h('pre', { class: 'mono' }, bug.code.replace(/\n+$/, '')),
    h('p', { class: 'muted' }, '在「輸入」欄打一組輸入，旁邊會自動出現這個程式印出什麼；再依照規格填「正確應該印出」，按「檢查」。'),
    h('div', { class: 'scroll' }, h('table', { class: 'cases' },
      h('thead', {}, h('tr', {}, h('th', {}, '#'), h('th', {}, p.inputLabel), h('th', {}, '這個程式印出'), h('th', {}, p.outputLabel), h('th', {}, '結果'))),
      tbody)),
    h('div', { class: 'row' }, btn, h('button', { type: 'button', onclick: () => { addRow(); save() } }, '多加一列')),
    results)
}
