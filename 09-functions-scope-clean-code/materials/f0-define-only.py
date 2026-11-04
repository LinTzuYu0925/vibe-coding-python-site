# F0：只定義、不呼叫：函式裡的 print 不會執行
def greet(name):
    print("進入 greet")
    return "你好，" + name
