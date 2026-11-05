# 頁「繼承」：LabeledDataset 以 Dataset 為藍本
# 需要 dataset.py、ml_stats.py 在同一個資料夾
from dataset import Dataset


class LabeledDataset(Dataset):
    def __init__(self, names, scores, labels):
        super().__init__(names, scores)     # 先請 Dataset 設好 names、scores
        self.labels = labels                # 再加上自己的新資料

    def label_of(self, name):               # 新增：Dataset 沒有的方法
        for i in range(len(self.names)):
            if self.names[i] == name:
                return self.labels[i]

    def passed_names(self):                 # 覆寫：同名，改成看標籤
        result = []
        for i in range(len(self.names)):
            if self.labels[i] == "pass":
                result.append(self.names[i])
        return result


ld = LabeledDataset(["小明", "阿美", "技安"], [80, 65, 59],
                    ["pass", "fail", "fail"])
print(ld.count())           # 繼承來的：LabeledDataset 裡沒有寫 count
print(ld.average())         # 繼承來的
print(ld.label_of("阿美"))  # 新增的
print(ld.passed_names())    # 覆寫的：用自己的版本，看標籤

d = Dataset(["小明", "阿美", "技安"], [80, 65, 59])
print(d.passed_names())     # 父類別自己的版本：看分數 >= 60
