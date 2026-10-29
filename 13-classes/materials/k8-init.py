# 投影片「__init__ 與 self」那頁的範例
class Dataset:
    def __init__(self, names, scores):
        self.names = names
        self.scores = scores

d = Dataset(["小明"], [80])
print(d.names)
