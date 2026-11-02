# 每隔幾號點名
a, b, step = [int(x) for x in input().split()]
print(f"座號 {list(range(a, b, step))}")
