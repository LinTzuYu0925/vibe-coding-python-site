# 有沒有人不及格
def has_fail(scores):
    for s in scores:
        if s < 60:
            return True
        else:
            return False


scores = [int(x) for x in input().split()]
if has_fail(scores):
    print("有人不及格")
else:
    print("全部及格")
