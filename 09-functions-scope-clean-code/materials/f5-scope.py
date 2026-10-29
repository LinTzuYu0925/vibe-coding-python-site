# F5：區域與全域
rate = 0.1

def with_bonus(score):
    bonus = score * rate
    return score + bonus

print(with_bonus(80))
print(rate)
