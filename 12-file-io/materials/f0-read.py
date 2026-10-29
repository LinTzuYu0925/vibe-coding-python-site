# 讀取整個文字檔
with open("scores.txt", encoding="utf-8") as f:
    text = f.read()
print(repr(text))
print(type(text))
