"""示範：ml_stats.py 的 average 被改壞（漏了除以個數），自我測試就會停下來。"""


def average(scores):
    if len(scores) == 0:
        return None
    return sum(scores)          # 壞掉：忘了 / len(scores)


if __name__ == "__main__":
    assert average([80, 90]) == 85
    assert average([]) is None
    print("自我測試通過")
