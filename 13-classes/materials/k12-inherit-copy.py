# 頁「兩個很像的類別」：不用繼承，從頭再寫一個 LabeledDataset
# average、count 和 dataset.py 的 Dataset 一模一樣：複製了兩份
import ml_stats


class LabeledDataset:
    def __init__(self, names, scores, labels):
        self.names = names
        self.scores = scores
        self.labels = labels

    def average(self):                      # 複製自 Dataset
        return ml_stats.average(self.scores)

    def count(self):                        # 複製自 Dataset
        return len(self.names)

    def label_of(self, name):
        for i in range(len(self.names)):
            if self.names[i] == name:
                return self.labels[i]


ld = LabeledDataset(["小明", "阿美", "技安"], [80, 65, 59],
                    ["pass", "fail", "fail"])
print(ld.count())
print(ld.average())
print(ld.label_of("阿美"))
