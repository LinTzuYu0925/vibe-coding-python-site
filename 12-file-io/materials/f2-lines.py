# 一行一行讀，轉成整數
import ml_stats

scores = []
with open("scores.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        scores.append(int(line))

print(scores)
print("平均：", ml_stats.average(scores))
print("及格：", ml_stats.passed(scores))
