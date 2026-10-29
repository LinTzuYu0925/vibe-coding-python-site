# E0：第一個 try / except
text = "85"
try:
    score = int(text)
    print("轉換成功：", score)
except ValueError:
    print("這不是數字")

text = "八十五"
try:
    score = int(text)
    print("轉換成功：", score)
except ValueError:
    print("這不是數字")
print("程式繼續跑")
