# Q5 稽核：dict 也有別名陷阱
a = {"name": "王小明", "chinese": 80}
b = a
b["chinese"] = 0
print(a)
c = a.copy()
c["chinese"] = 100
print(a)
print(c)
