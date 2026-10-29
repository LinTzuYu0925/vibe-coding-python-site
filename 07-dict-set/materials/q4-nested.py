# Q4：巢狀 dict，用學號當 key
students = {
    "S1001": {"name": "王小明", "chinese": 80},
    "S1002": {"name": "林小華", "chinese": 92},
}
print(students["S1001"])
print(students["S1002"]["name"])
students["S1001"]["chinese"] = 85
print(students["S1001"]["chinese"])
print("S1003" in students)
