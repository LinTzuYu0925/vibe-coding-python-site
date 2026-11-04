# F3：docstring（Google 格式）
def subject_average(students, subject):
    """回傳全班某一科的平均。

    Args:
        students (list): 學生資料，每位是一個 dict。
        subject (str): 科目欄位名稱，例如 "math"。

    Returns:
        float: 這一科的平均；沒有資料時回傳 None。
    """
    if len(students) == 0:
        return None
    total = 0
    for s in students:
        total = total + s[subject]
    return total / len(students)


print(subject_average.__doc__.splitlines()[0])
print(subject_average([{"math": 65}, {"math": 95}], "math"))
help(subject_average)
