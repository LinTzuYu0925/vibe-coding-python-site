# Q7 稽核：Agent 把欄位寫成 "Chinese"（大寫），KeyError 版的 students.py 片段
students = [
    {"name": "王小明", "student_id": "S1001", "chinese": 80, "english": 72, "math": 65},
]
first = students[0]
print(first["Chinese"])
