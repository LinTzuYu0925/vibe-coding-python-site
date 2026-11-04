"""ML 資料小幫手的統計工具（單元 11：自己的模組）。"""


def average(scores):
    """回傳平均；空 list 回傳 None。"""
    if len(scores) == 0:
        return None
    return sum(scores) / len(scores)


def passed(scores, line=60):
    """回傳及格（>= line）的分數。"""
    result = []
    for s in scores:
        if s >= line:
            result.append(s)
    return result


if __name__ == "__main__":
    # 自我測試：assert 後面的條件不成立，就停下來並出現 AssertionError
    assert average([80, 90]) == 85
    assert average([]) is None
    assert passed([80, 59, 60]) == [80, 60]
    print("自我測試通過")
