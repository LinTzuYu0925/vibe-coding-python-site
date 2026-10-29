# F6 稽核：函式改到傳進來的 list
def add_bonus(scores):
    scores.append(100)
    return scores

original = [80, 72]
result = add_bonus(original)
print(original)
print(result)
print(original is result)

def add_bonus_safe(scores):
    new = scores.copy()
    new.append(100)
    return new

original2 = [80, 72]
result2 = add_bonus_safe(original2)
print(original2)
print(result2)
