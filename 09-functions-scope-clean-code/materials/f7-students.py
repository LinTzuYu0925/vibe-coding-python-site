# F7：用函式回答兩個問題：全班數學／國文平均、誰及格（資料照抄自 grades.csv）
students = [
    {"name": "王小明", "student_id": "S1001", "chinese": 80, "english": 72, "math": 65},
    {"name": "林小華", "student_id": "S1002", "chinese": 92, "english": 88, "math": 95},
    {"name": "陳小美", "student_id": "S1003", "chinese": 65, "english": 70, "math": 58},
    {"name": "張小強", "student_id": "S1004", "chinese": 45, "english": 50, "math": 52},
    {"name": "李小雅", "student_id": "S1005", "chinese": 78, "english": 85, "math": 90},
]


def average(student):
    """回傳一位學生的三科平均。

    Args:
        student (dict): 一位學生，有 chinese、english、math。

    Returns:
        float: 三科平均，不四捨五入。
    """
    return (student["chinese"] + student["english"] + student["math"]) / 3


def is_passed(student, line=60):
    """判斷一位學生是否及格。

    Args:
        student (dict): 一位學生。
        line (int): 及格線，預設 60。

    Returns:
        bool: 三科平均大於或等於 line 就是 True。
    """
    return average(student) >= line


def subject_average(students, subject):
    """回傳全班某一科的平均。

    Args:
        students (list): 全班學生的 list。
        subject (str): 科目欄位，例如 "math"。

    Returns:
        float: 這一科的平均；沒有資料時回傳 None。
    """
    if len(students) == 0:
        return None
    total = 0
    for s in students:
        total = total + s[subject]
    return total / len(students)


def passed_names(students):
    """回傳及格者的姓名。

    Args:
        students (list): 全班學生的 list。

    Returns:
        list: 及格者姓名，照原本順序。
    """
    names = []
    for s in students:
        if is_passed(s):
            names.append(s["name"])
    return names


print(f"全班數學平均：{subject_average(students, 'math')}")
print(f"全班國文平均：{subject_average(students, 'chinese')}")
print(f"及格：{passed_names(students)}")
print(f"空資料的平均：{subject_average([], 'math')}")
