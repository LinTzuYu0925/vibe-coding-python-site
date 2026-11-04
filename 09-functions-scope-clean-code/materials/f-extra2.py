# 練習新題與驗證
def is_passed(average, line=60):
    return average >= line
print(is_passed(90, 90), is_passed(line=50, average=50.5), is_passed(80, 90), is_passed(59, line=59))
students = [
    {"name": "王小明", "math": 65, "english": 88},
    {"name": "林小華", "math": 95, "english": 70},
    {"name": "陳小美", "math": 58, "english": 92},
]
print(max(students, key=lambda s: s["english"])["name"])
print(min(students, key=lambda s: s["english"])["name"])
print(sorted(students, key=lambda s: s["english"])[0]["name"])
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
