// Runs student Python in Pyodide, off the page's main thread so an endless loop cannot
// freeze the page: oj.js terminates this worker on timeout and starts a new one.
// Message in: {id, code, stdin}. Message out: {type: 'ready'} once, then {id, stdout, error}.
importScripts('https://cdn.jsdelivr.net/pyodide/v0.29.5/full/pyodide.js')

const HARNESS = `
import sys, io, builtins, traceback, json

def __oj_run(code, stdin):
    inp, out, err = io.StringIO(stdin), io.StringIO(), io.StringIO()

    # input("提示") must not print its prompt: AI-written code often adds one,
    # and beginners cannot tell why the output then differs.
    def quiet_input(prompt=''):
        line = inp.readline()
        if line == '':
            raise EOFError('EOF when reading a line')
        return line[:-1] if line.endswith('\\n') else line

    saved = sys.stdin, sys.stdout, sys.stderr, builtins.input
    sys.stdin, sys.stdout, sys.stderr, builtins.input = inp, out, err, quiet_input
    error = None
    try:
        exec(compile(code, 'solution.py', 'exec'), {'__name__': '__main__'})
    except SystemExit:
        pass
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
  const { id, code, stdin } = e.data
  postMessage({ id, ...JSON.parse(run(code, stdin)) })
}
