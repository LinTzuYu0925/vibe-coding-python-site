# Q0：承接單元 05 的 grades.py，一位學生改放進一個 dict
student = {
    "name": "王小明",
    "student_id": "S1001",
    "chinese": 80,
    "english": 72,
    "math": 65,
    "attendance": 0.85,
}

print(student["name"])
print(student["chinese"])
average = (student["chinese"] + student["english"] + student["math"]) / 3
print(f"{student['name']} 的平均：{average}")
print(len(student))
