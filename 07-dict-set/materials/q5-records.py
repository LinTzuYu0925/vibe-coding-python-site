# Q5：多筆紀錄，list 裡放 dict
students = [
    {"name": "王小明", "student_id": "S1001", "chinese": 80},
    {"name": "林小華", "student_id": "S1002", "chinese": 92},
    {"name": "陳小美", "student_id": "S1003", "chinese": 65},
]
print(len(students))
print(students[0])
print(students[0]["name"])
print(students[-1]["chinese"])
students[1]["chinese"] = 95
print(students[1])
students.append({"name": "張小強", "student_id": "S1004", "chinese": 70})
print(len(students))
print(students[3]["name"])
