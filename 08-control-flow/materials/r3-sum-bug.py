# R3 陷阱：total 放進迴圈裡每次歸零
scores = [78, 85.5, 62, 91, 55]
for s in scores:
    total = 0
    total = total + s
print(total)
