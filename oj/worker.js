// Runs student Python in Pyodide, off the page's main thread so an endless loop cannot
// freeze the page: oj.js terminates this worker on timeout and starts a new one.
// Message in: {id, code, stdin, file, after}. With file, stdin is written to that file instead
// (an empty or blank text gives an empty file), and the program reads no keyboard input.
// With after (a task's tests/harness.py), the student's code runs with no keyboard input, then
// the harness runs in the same namespace, reads stdin and calls the student's class or functions.
// Message out: {type: 'ready'} once, then {id, stdout, error}.
importScripts('https://cdn.jsdelivr.net/pyodide/v0.29.5/full/pyodide.js')

const HARNESS = `
import sys, io, os, shutil, builtins, traceback, json

def __oj_run(code, stdin, file, after):
    # A fresh folder for every run, so files a program wrote never reach the next run.
    # Leave the folder first: the file system cannot delete the current folder.
    os.chdir('/')
    shutil.rmtree('/home/pyodide/oj', ignore_errors=True)
    os.makedirs('/home/pyodide/oj', exist_ok=True)
    os.chdir('/home/pyodide/oj')
    if file:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(stdin if stdin.strip() else '')
        stdin = ''
    # With a harness, the input belongs to the harness, not the student's code.
    inp, out, err = io.StringIO('' if after else stdin), io.StringIO(), io.StringIO()

    # input("提示") must not print its prompt: AI-written code often adds one,
    # and beginners cannot tell why the output then differs.
    def quiet_input(prompt=''):
        line = sys.stdin.readline()
        if line == '':
            raise EOFError('EOF when reading a line')
        return line[:-1] if line.endswith('\\n') else line

    saved = sys.stdin, sys.stdout, sys.stderr, builtins.input
    sys.stdin, sys.stdout, sys.stderr, builtins.input = inp, out, err, quiet_input
    error = None
    in_harness = False
    try:
        namespace = {'__name__': '__main__'}
        exec(compile(code, 'solution.py', 'exec'), namespace)
        if after:
            in_harness = True
            sys.stdin = io.StringIO(stdin)
            exec(compile(after, 'test.py', 'exec'), namespace)
    except SystemExit:
        pass
    except EOFError if after and not in_harness else () as e:
        error = ('EOFError: 這題只要寫類別或函式，不用 input()：'
                 '網頁的測試程式會自己呼叫你的函式或方法。把讀輸入、印結果的主程式拿掉。')
    except BaseException as e:
        # Skip this harness frame so the traceback starts in the student's file.
        error = ''.join(traceback.format_exception(type(e), e, e.__traceback__.tb_next))
    finally:
        sys.stdin, sys.stdout, sys.stderr, builtins.input = saved
    return json.dumps({'stdout': out.getvalue(), 'error': error})
`

let run
loadPyodide().then(py => {
  py.runPython(HARNESS)
  run = py.globals.get('__oj_run')
  postMessage({ type: 'ready' })
}).catch(e => postMessage({ type: 'failed', message: String(e) }))

onmessage = e => {
  const { id, code, stdin, file, after } = e.data
  postMessage({ id, ...JSON.parse(run(code, stdin, file || '', after || '')) })
}
