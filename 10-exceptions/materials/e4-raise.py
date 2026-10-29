# E4：raise 自己丟出錯誤
def set_score(score):
    if score < 0 or score > 100:
        raise ValueError(f"分數要在 0 到 100 之間，收到 {score}")
    return score

print(set_score(85))
try:
    set_score(120)
except ValueError as e:
    print("接住了：", e)
