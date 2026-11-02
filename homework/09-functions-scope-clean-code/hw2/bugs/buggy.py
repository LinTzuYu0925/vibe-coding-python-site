# 最高分與第一位交卷
def highest(scores):
    scores.sort()
    return scores[-1]


scores = [int(x) for x in input().split()]
top = highest(scores)
print(f"最高分 {top}，第一位交卷 {scores[0]}")
