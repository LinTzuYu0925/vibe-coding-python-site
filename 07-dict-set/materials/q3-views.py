# Q3：keys、values、items 與整體運算
scores = {"國文": 80, "英文": 72, "數學": 65}
print(scores.keys())
print(scores.values())
print(scores.items())
print(list(scores.keys()))
print(sum(scores.values()))
print(max(scores.values()))
print(sum(scores.values()) / len(scores))
