# 頁「@property」「@staticmethod」「@classmethod」：同一個 Dataset 的三種寫法
# 需要 ml_stats.py、students.csv 在同一個資料夾
import csv
import ml_stats


class Dataset:
    def __init__(self, names, scores):
        self.names = names
        self.scores = scores

    def average(self):                  # 一般方法：要加括號
        return ml_stats.average(self.scores)

    @property
    def count(self):                    # 讀起來像屬性：不加括號
        return len(self.names)

    @staticmethod
    def is_pass(score, line=60):        # 沒有 self：不需要哪一筆資料
        return score >= line

    @classmethod
    def from_csv(cls, path):            # cls 是 Dataset 這個類別本身
        names = []
        scores = []
        with open(path, encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                names.append(row["name"])
                scores.append(int(row["score"]))
        return cls(names, scores)       # 等於 Dataset(names, scores)


# @property
d = Dataset(["小明", "技安"], [80, 59])
print(d.count)
d.names.append("大雄")
d.scores.append(92)
print(d.count)                          # 資料變了，count 跟著變

# @staticmethod
print(Dataset.is_pass(72))
print(Dataset.is_pass(59))

# @classmethod
d2 = Dataset.from_csv("students.csv")
print(d2.count)
print(d2.average())
