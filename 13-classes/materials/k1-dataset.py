# 老師版：把名字和分數包成一個 Dataset
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


d = Dataset(["小明", "小華", "阿美", "大雄", "靜香", "技安"],
            [80, 72, 65, 92, 88, 59])
print("平均：", d.average())
print("及格（60）：", d.passed_names())
print("及格（80）：", d.passed_names(80))
print("人數：", d.count())
