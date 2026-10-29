# F4：key= 與 lambda
students = [
    {"name": "王小明", "math": 65},
    {"name": "林小華", "math": 95},
    {"name": "陳小美", "math": 58},
]
by_math = sorted(students, key=lambda s: s["math"])
print(by_math[0]["name"], by_math[-1]["name"])
best = max(students, key=lambda s: s["math"])
print(best["name"])

def get_math(s):
    return s["math"]

print(max(students, key=get_math)["name"])
f = lambda x: x * 2
print(f(5))
