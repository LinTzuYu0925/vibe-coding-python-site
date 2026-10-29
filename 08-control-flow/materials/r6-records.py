# R6：students.py 升級，用迴圈算全班（承接單元 07）
students = [
    {"name": "王小明", "student_id": "S1001", "chinese": 80, "english": 72, "math": 65},
    {"name": "林小華", "student_id": "S1002", "chinese": 92, "english": 88, "math": 95},
    {"name": "陳小美", "student_id": "S1003", "chinese": 65, "english": 70, "math": 58},
    {"name": "張小強", "student_id": "S1004", "chinese": 45, "english": 50, "math": 52},
    {"name": "李小雅", "student_id": "S1005", "chinese": 78, "english": 85, "math": 90},
]

total_math = 0
passed_names = []
for s in students:
    total_math = total_math + s["math"]
    average = (s["chinese"] + s["english"] + s["math"]) / 3
    if average >= 60:
        passed_names.append(s["name"])
    print(f"{s['name']} 平均 {average:.1f}")

print(f"全班數學平均：{total_math / len(students)}")
print(f"及格：{passed_names}")
print(f"及格人數：{len(passed_names)} / {len(students)}")
