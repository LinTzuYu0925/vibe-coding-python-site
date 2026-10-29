# 電梯載重：讀入乘客體重，判斷誰能上電梯
LIMIT = 500          # 電梯載重上限（公斤）

count = 0            # 已經上電梯的人數
total = 0            # 電梯裡的總重

while True:
    line = input()
    if line == "結束":
        break
    weight = int(line)

print(f"上了 {count} 人，總重 {total} 公斤")
