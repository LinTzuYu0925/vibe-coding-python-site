# E2 陷阱：except 全抓，把錯默默吞掉
def average(scores):
    try:
        return sum(scores) / len(scores)
    except:
        return 0

print(average([80, 70]))
print(average([]))
print(average(["a", "b"]))
print(average(None))
