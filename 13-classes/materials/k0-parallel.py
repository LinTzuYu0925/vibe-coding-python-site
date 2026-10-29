# 兩個「平行 list」：名字和分數靠位置對應
names = ["小明", "小華", "阿美"]
scores = [80, 72, 65]

print("正常配對：")
for i in range(len(names)):
    print(" ", names[i], scores[i])

# 小明的分數被誤刪，names 沒跟著刪
scores.pop(0)

print("刪掉一筆分數後的配對（錯位！）：")
for i in range(len(scores)):
    print(" ", names[i], scores[i])
print("names 有", len(names), "筆，scores 只剩", len(scores), "筆")
