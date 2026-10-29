# R5：while 與 break
n = 1
while n <= 3:
    print("n 是", n)
    n = n + 1
print("結束，n 是", n)

total = 0
for s in [50, 40, 30, 20]:
    total = total + s
    if total > 100:
        print("超過 100 了，停")
        break
print(total)
