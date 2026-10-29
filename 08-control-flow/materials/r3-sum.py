# R3：累加與計數
scores = [78, 85.5, 62, 91, 55]
total = 0
count = 0
for s in scores:
    total = total + s
    count = count + 1
print(total)
print(count)
print(total / count)
print(sum(scores) == total)
