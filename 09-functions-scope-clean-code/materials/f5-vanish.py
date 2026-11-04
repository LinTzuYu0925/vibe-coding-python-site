# F5：區域變數在函式結束後消失；每次呼叫都重新開始
def visit():
    count = 0
    count = count + 1
    return count

print(visit())
print(visit())
print(visit())
print(count)
