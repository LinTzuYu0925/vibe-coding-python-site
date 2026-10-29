# t8：不用 TensorFlow，只用 Python list 和迴圈（備案）
import csv

names = []
scores = []
with open("students.csv", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        names.append(row["name"])
        scores.append(float(row["score"]))

print("筆數：", len(scores))

# 平均
total = 0.0
for s in scores:
    total = total + s
print("平均：", total / len(scores))

# 正規化
normalized = []
for s in scores:
    normalized.append(s / 100)
print("正規化（/100）：", normalized)

# 遮罩
mask = []
for s in scores:
    mask.append(s >= 60)
print("遮罩：", mask)

count = 0
for flag in mask:
    if flag:
        count = count + 1
print("及格人數：", count)

for i in range(len(names)):
    if mask[i]:
        print("及格：", names[i])

# list 不能直接除
try:
    print(scores / 100)
except TypeError as e:
    print("list / 100 失敗：", type(e).__name__, e)
