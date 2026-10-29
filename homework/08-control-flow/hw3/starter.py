# 電梯載重：讀入乘客體重，判斷誰能上電梯
LIMIT = 500          # 電梯載重上限（公斤）

count = 0            # 已經上電梯的人數
total = 0            # 電梯裡的總重

while True:
    line = input()
    if line == "結束":
        break
    weight = int(line)
    # TODO：在這裡判斷這位乘客能不能上電梯
    #       能上：人數加 1、總重加上體重
    #       不能上：這位和後面的人都不能上，停止讀入

print(f"上了 {count} 人，總重 {total} 公斤")
