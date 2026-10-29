# E6：students.py 加上防禦（承接單元 08、09）
students = [
    {"name": "王小明", "chinese": 80, "english": 72, "math": 65},
    {"name": "林小華", "chinese": 92, "english": "八十八", "math": 95},
    {"name": "陳小美", "chinese": 65, "math": 58},
    {"name": "張小強", "chinese": 45, "english": 50, "math": 52},
]


def read_score(student, subject):
    """回傳分數（數字）；缺欄位或不是數字就回傳 None。"""
    value = student.get(subject)
    if value is None:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def subject_average(students, subject):
    """回傳某科平均與略過的人名；沒有有效資料時平均為 None。"""
    total = 0
    count = 0
    skipped = []
    for s in students:
        score = read_score(s, subject)
        if score is None:
            skipped.append(s["name"])
        else:
            total = total + score
            count = count + 1
    if count == 0:
        return None, skipped
    return total / count, skipped


for subject in ["chinese", "english", "math"]:
    avg, skipped = subject_average(students, subject)
    print(f"{subject}: 平均 {avg}，略過 {skipped}")
print(subject_average([], "math"))
