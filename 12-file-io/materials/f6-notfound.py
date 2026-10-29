# 找不到檔案
import os

print("目前工作目錄：", os.getcwd())
print("腳本所在資料夾：", os.path.dirname(os.path.abspath(__file__)))

try:
    f = open("nofile.txt")
except FileNotFoundError as e:
    print("錯誤訊息：", str(e))

print("--- try / except / finally ---")
f = None
try:
    f = open("scores.txt", encoding="utf-8")
    print("讀到第一行：", f.readline().strip())
except FileNotFoundError:
    print("找不到 scores.txt（相對路徑是相對於「目前工作目錄」）")
finally:
    if f is not None:
        f.close()
        print("finally：檔案已關閉")
