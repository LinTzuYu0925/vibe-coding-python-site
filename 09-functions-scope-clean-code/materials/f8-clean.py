# F8：同樣的功能，名稱不同
def f(a, b, c):
    x = a + b + c
    y = x / 3
    return y

def average_of_three(chinese, english, math):
    total = chinese + english + math
    return total / 3

print(f(80, 72, 65))
print(average_of_three(80, 72, 65))
