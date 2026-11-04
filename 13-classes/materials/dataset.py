# 頁「pytest」用：k1-dataset.py 的 Dataset，只留類別（被 import 時不印東西）
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
