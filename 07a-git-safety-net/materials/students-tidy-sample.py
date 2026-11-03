# students.py（講師手寫的「整理過」範例，示意 Agent 對模糊要求常見的大幅改寫；不是 Agent 實際輸出）
"""班級成績資料表。"""


def make_student(name, student_id, chinese, english, math):
    """建立一位學生的紀錄。"""
    return {"name": name, "student_id": student_id, "scores": {"chinese": chinese, "english": english, "math": math}}


STUDENTS = [
    make_student("王小明", "S1001", 80, 72, 65),
    make_student("林小華", "S1002", 92, 88, 95),
    make_student("陳小美", "S1003", 65, 70, 58),
    make_student("張小強", "S1004", 45, 50, 52),
    make_student("李小雅", "S1005", 78, 85, 90),
]


def average(student):
    """回傳三科平均。"""
    return sum(student["scores"].values()) / 3


def main():
    print(f"人數：{len(STUDENTS)}")
    first = STUDENTS[0]
    print(f"第一位：{first['name']}（{first['student_id']}）")
    print(f"最後一位：{STUDENTS[-1]['name']}，數學 {STUDENTS[-1]['scores']['math']}")
    print(f"{first['name']} 的三科平均：{average(first)}")


if __name__ == "__main__":
    main()
