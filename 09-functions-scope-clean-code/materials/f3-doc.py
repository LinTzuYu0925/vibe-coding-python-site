# F3：docstring 與型別提示
def average(chinese: int, english: int, math: int) -> float:
    """回傳三科成績的平均（不四捨五入）。"""
    return (chinese + english + math) / 3

print(average.__doc__)
print(average(80, 72, 65))
