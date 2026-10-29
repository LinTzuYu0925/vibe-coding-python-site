# E7：finally 一定會執行
def run():
    try:
        return "try 回傳"
    finally:
        print("finally 一定會做")

print(run())
