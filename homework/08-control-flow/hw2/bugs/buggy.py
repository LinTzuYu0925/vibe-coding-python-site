# 最長連續打卡
record = input().strip()
best = 0      # 目前最長的連續天數
streak = 0    # 現在連續了幾天
for day in record:
    if day == "O":
        streak = streak + 1
    else:
        if streak > best:
            best = streak
        streak = 0
print(best)
