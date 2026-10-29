# 稽核實測：兩個實例獨立嗎？只有標題的 CSV 會怎樣？
import csv
import json
import ml_stats


class Dataset:
    def __init__(self, names=None, scores=None):
        # 不能寫成 names=[]：預設值只會建立一次，
        # 所有實例會共用同一個 list（見 k5-mutable-default.py）
        if names is None:
            names = []
        if scores is None:
            scores = []
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

    def load(self, path):
        with open(path, encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                self.names.append(row["name"])
                self.scores.append(int(row["score"]))

    def save_report(self, path):
        report = {
            "average": self.average(),
            "passed": self.passed_names(),
            "count": self.count(),
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)



a = Dataset()
b = Dataset()
a.load("students.csv")
print("a 人數：", a.count(), "；b 人數：", b.count())

with open("header-only.csv", "w", encoding="utf-8", newline="") as f:
    f.write("name,score" + chr(10))
e = Dataset()
e.load("header-only.csv")
print("只有標題：人數", e.count(), "，平均", e.average(), "，及格", e.passed_names())
