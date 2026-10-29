# P6：班級成績 scores.py，30 位學生的數學成績（不用迴圈與函式）
scores = [

]

print(f"人數：{len(scores)}")
print(f"最高：{max(scores)}")
print(f"最低：{min(scores)}")
print(f"前三名：{sorted(scores)[-3:]}")
print(f"最低三名：{sorted(scores)[:3]}")
print(f"平均：{sum(scores) / len(scores)}")
print(f"第一位：{scores[0]}，最後一位：{scores[-1]}")
