# 類別（設計圖）與實例（照圖蓋出來的房子）
class Dataset:
    def __init__(self, names, scores):
        self.names = names
        self.scores = scores


d1 = Dataset(["小明", "小華"], [80, 72])
d2 = Dataset(["阿美"], [65])

print(type(d1))
print(d1)   # 預設的 repr：有記憶體位址，每次執行都不同
print(d2)

d1.scores.append(100)
print("d1.scores =", d1.scores)
print("d2.scores =", d2.scores, "（沒有變，兩個實例互相獨立）")
