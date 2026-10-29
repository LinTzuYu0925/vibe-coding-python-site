# Agent 風格的壞版本（4 個問題），只在複本 students-copy.csv 上執行
# 問題 1：沒有 with、沒有 close
# 問題 2：寫死的絕對路徑
# 問題 3：沒有指定 encoding
# 問題 4：誤用 "w" 開啟輸入檔
import shutil

shutil.copy("students.csv", "students-copy.csv")

try:
    f = open(r"C:\Users\student\scores.txt")
    print(f.read())
except Exception as e:
    print("問題 2 的結果：", type(e).__name__, e)

f = open("students-copy.csv")
print("問題 3 的結果（沒寫 encoding）：", repr(f.readline()))

f = open("students-copy.csv", "w")
import os
print("問題 4：用 w 開啟後，複本大小 =", os.path.getsize("students-copy.csv"), "位元組")
# 問題 1：忘了 f.close()，程式結束前內容可能還沒寫出
