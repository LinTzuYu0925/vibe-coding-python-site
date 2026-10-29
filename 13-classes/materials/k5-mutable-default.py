# 可變預設值的陷阱
class BadDataset:
    def __init__(self, names=[]):
        self.names = names


a = BadDataset()
b = BadDataset()
a.names.append("小明")
print("a.names =", a.names)
print("b.names =", b.names, "（我們沒動 b！）")
print("同一個 list 嗎？", a.names is b.names)
