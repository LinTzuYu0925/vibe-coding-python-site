# 質數判斷
n = int(input())
is_prime = True
for d in range(2, n // 2):
    if n % d == 0:
        is_prime = False
        break
if is_prime:
    print("是質數")
else:
    print("不是質數")
