# 頁「__str__」：讓 print(d) 印出看得懂的內容
import ml_stats


class Dataset:
    def __init__(self, names, scores):
        self.names = names
        self.scores = scores

    def average(self):
        return ml_stats.average(self.scores)

    def count(self):
        return len(self.names)


d = Dataset(["小明", "技安"], [80, 59])
print(d)                        # 沒有 __str__：只看到「哪個類別、在記憶體哪裡」


class Dataset:
    def __init__(self, names, scores):
        self.names = names
        self.scores = scores

    def average(self):
        return ml_stats.average(self.scores)

    def count(self):
        return len(self.names)

    def __str__(self):          # 只多了這 2 行
        return f"Dataset：{self.count()} 筆，平均 {self.average()}"


d = Dataset(["小明", "技安"], [80, 59])
print(d)                        # print 自動呼叫 __str__
print(str(d))                   # str() 也會
