# 常見錯誤的真實訊息
import ml_stats


class Dataset:
    def __init__(self, names, scores):
        self.names = names
        self.scores = scores

    def average(self):
        return ml_stats.average(self.scores)

    def bad_average():          # 忘了寫 self
        return 0

    def bad_count(self):
        return len(names)       # 忘了寫 self.


d = Dataset(["小明"], [80])

def try_it(label, func):
    try:
        func()
    except Exception as e:
        print(label)
        print("  ", type(e).__name__ + ":", e)

try_it("1. 定義時忘了 self，卻用 d.bad_average() 呼叫", lambda: d.bad_average())
try_it("2. 沒有實例，直接 Dataset.average()", lambda: Dataset.average())
try_it("3. 拼錯屬性 d.score", lambda: d.score)
try_it("4. 方法裡忘了 self.（用 names）", lambda: d.bad_count())
try_it("5. Dataset(...) 參數數量錯誤", lambda: Dataset(["小明"]))
