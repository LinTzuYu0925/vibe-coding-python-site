# 練習新題與驗證
def is_passed(average, line=60):
    return average >= line
print(is_passed(90, 90), is_passed(line=50, average=50.5), is_passed(80, 90), is_passed(59, line=59))
def add_one(n):
    return n + 1
def say(n):
    print(n + 1)
print(add_one(5))
print(say(5))
print(say(5) is None)
def typed(a: int) -> int:
    return a
print(typed("文字"))
def swap_name(first, second):
    return second, first
a, b = swap_name("A", "B")
print(a, b)
