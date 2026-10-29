# 沒寫 encoding 會怎樣
# 注意：輸出刻意只用 ASCII（ascii() 會把中文轉成 \uXXXX），
# 因為沒有 -X utf8 時，終端機輸出編碼也可能無法顯示中文。
import locale

print("default encoding:", locale.getpreferredencoding(False))
try:
    with open("students.csv") as f:
        print("read OK:", ascii(f.read()))
except UnicodeDecodeError as e:
    print("UnicodeDecodeError:", e)
