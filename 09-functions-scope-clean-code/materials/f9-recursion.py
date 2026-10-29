# F9：遞迴（選修）
def countdown(n):
    if n == 0:
        print("發射")
        return
    print(n)
    countdown(n - 1)

countdown(3)

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
