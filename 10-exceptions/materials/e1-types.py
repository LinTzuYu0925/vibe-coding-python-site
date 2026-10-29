# E1：常見例外各印一次
tests = [
    ("int('abc')", lambda: int("abc")),
    ("10 / 0", lambda: 10 / 0),
    ("[1, 2][5]", lambda: [1, 2][5]),
    ("{'a': 1}['b']", lambda: {"a": 1}["b"]),
    ("'a' + 1", lambda: "a" + 1),
    ("open('不存在.txt')", lambda: open("不存在.txt")),
]
for name, f in tests:
    try:
        f()
    except Exception as e:
        print(f"{name:20} -> {type(e).__name__}: {e}")
