# P6：班級成績 scores.py，30 位學生的數學成績（不用迴圈與函式）
scores = [
    78, 85.5, 62, 91, 55, 73, 88, 67.5, 94, 49,
    81, 70, 59.5, 86, 77, 92.5, 64, 83, 58, 75,
    89, 66, 72.5, 97, 53, 80, 69, 84, 61, 90,
]

print(f"人數：{len(scores)}")
print(f"平均：{sum(scores) / len(scores)}")
print(f"最高：{max(scores)}")
print(f"最低：{min(scores)}")
print(f"前三名：{sorted(scores)[-3:]}")
print(f"最低三名：{sorted(scores)[:3]}")
print(f"第一位：{scores[0]}，最後一位：{scores[-1]}")
