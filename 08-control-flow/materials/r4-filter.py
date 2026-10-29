# R4：篩選與計數，for 裡面放 if
scores = [78, 85.5, 62, 91, 55, 73, 88, 67.5, 94, 49]
passed = 0
failed = []
for s in scores:
    if s >= 60:
        passed = passed + 1
    else:
        failed.append(s)
print(f"及格 {passed} 人")
print(f"不及格 {len(failed)} 人：{failed}")
