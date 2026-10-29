# 主線：讀 students.csv，算平均與及格名單，存成 report.json
import csv
import json
import ml_stats

names = []
scores = []
with open("students.csv", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        names.append(row["name"])
        scores.append(int(row["score"]))

passed_names = []
for i in range(len(names)):
    if scores[i] >= 60:
        passed_names.append(names[i])

result = {
    "average": ml_stats.average(scores),
    "passed": passed_names,
    "count": len(scores),
}
with open("report.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print(result)
