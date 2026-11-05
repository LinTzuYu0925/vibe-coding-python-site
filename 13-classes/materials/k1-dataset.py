# 講師版：從 students.csv 讀出名字和分數，包成一個 Dataset
# 需要 students.csv、ml_stats.py 在同一個資料夾
import csv
import ml_stats


class Dataset:
    def __init__(self, names, scores):
        self.names = names
        self.scores = scores

    def average(self):
        return ml_stats.average(self.scores)

    def passed_names(self, line=60):
        result = []
        for i in range(len(self.names)):
            if self.scores[i] >= line:
                result.append(self.names[i])
        return result

    def count(self):
        return len(self.names)


names = []
scores = []
with open("students.csv", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        names.append(row["name"])
        scores.append(int(row["score"]))

d = Dataset(names, scores)
print("平均：", d.average())
print("及格（60）：", d.passed_names())
print("及格（80）：", d.passed_names(80))
print("人數：", d.count())
