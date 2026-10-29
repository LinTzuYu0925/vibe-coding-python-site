# E6 起始檔：只有資料與沒有防禦的平均，給 Agent 修改（承接單元 09）
students = [
    {"name": "王小明", "chinese": 80, "english": 72, "math": 65},
    {"name": "林小華", "chinese": 92, "english": "八十八", "math": 95},
    {"name": "陳小美", "chinese": 65, "math": 58},
    {"name": "張小強", "chinese": 45, "english": 50, "math": 52},
]


def subject_average(students, subject):
    """回傳某科平均。"""
    total = 0
    for s in students:
        total = total + s[subject]
    return total / len(students)


print(subject_average(students, "chinese"))
print(subject_average(students, "english"))
