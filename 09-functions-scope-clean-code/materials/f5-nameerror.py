# F5 陷阱：在函式外面用函式裡面的變數
def with_bonus(score):
    bonus = score * 0.1
    return score + bonus

with_bonus(80)
print(bonus)
