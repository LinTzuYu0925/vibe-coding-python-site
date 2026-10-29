# 學生成績單：單元 05 的完成版範例（備案用）
name = "王小明"
student_id = "S1001"
chinese = 80
english = 72
math = 65
attendance = 0.85

average = (chinese + english + math) / 3
passed = average >= 60 and attendance >= 0.8

print(f"{name}（{student_id}）")
print(f"平均分數：{average}")
print(f"出席率：{attendance}")
print(f"是否及格：{passed}")
