# Q7：班級資料表 students.py（不用迴圈與函式）
students = [
    {"name": "王小明", "student_id": "S1001", "chinese": 80, "english": 72, "math": 65},
    {"name": "林小華", "student_id": "S1002", "chinese": 92, "english": 88, "math": 95},
    {"name": "陳小美", "student_id": "S1003", "chinese": 65, "english": 70, "math": 58},
    {"name": "張小強", "student_id": "S1004", "chinese": 55, "english": 60, "math": 72},
    {"name": "李小雅", "student_id": "S1005", "chinese": 78, "english": 85, "math": 90},
]

print(f"人數：{len(students)}")
first = students[0]
print(f"第一位：{first['name']}（{first['student_id']}）")
last = students[-1]
print(f"最後一位：{last['name']}，數學 {last['math']}")
print(f"{first['name']} 的三科平均：{(first['chinese'] + first['english'] + first['math']) / 3}")

students.append({"name": "周小傑", "student_id": "S1006", "chinese": 88, "english": 90, "math": 76})
print(f"新增後人數：{len(students)}")
print(students[5]["name"])

clubs = ["羽球", "籃球", "羽球", "桌球", "籃球", "羽球"]
print(f"社團報名 {len(clubs)} 筆，共 {len(set(clubs))} 種社團")
