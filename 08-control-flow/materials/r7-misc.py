# 補充：for 搭配 enumerate、字串、dict
for i, name in enumerate(["小明", "小華"]):
    print(i, name)
for ch in "abc":
    print(ch)
d = {"國文": 80, "英文": 72}
for k in d:
    print(k, d[k])
for k, v in d.items():
    print(k, v)
