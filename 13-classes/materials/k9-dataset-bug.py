# 示範：把 passed_names 的 >= 改成 >（故意改壞），pytest 會抓到
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
            if self.scores[i] > line:
                result.append(self.names[i])
        return result

    def count(self):
        return len(self.names)
