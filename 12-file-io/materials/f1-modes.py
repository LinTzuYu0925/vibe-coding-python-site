# 'w' 寫入、'a' 附加、再用 'w' 開一次會清空舊內容
with open("out-demo.txt", "w", encoding="utf-8") as f:
    f.write("hello\n")
with open("out-demo.txt", "a", encoding="utf-8") as f:
    f.write("world\n")
with open("out-demo.txt", encoding="utf-8") as f:
    print("w 再 a 之後：", repr(f.read()))

with open("out-demo.txt", "w", encoding="utf-8") as f:
    f.write("new\n")
with open("out-demo.txt", encoding="utf-8") as f:
    print("再用 w 開啟之後：", repr(f.read()))
