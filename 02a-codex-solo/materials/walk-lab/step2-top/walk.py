import csv

GOAL = 8000  # 8000 步以上算達標，剛好 8000 也算

with open("walk.csv", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

if not rows:
    print("walk.csv 裡沒有資料。")
else:
    steps = [int(row["步數"]) for row in rows]
    for row in rows:
        print(row["日期"], row["步數"])
    print("平均步數：", round(sum(steps) / len(steps)))
    print("達標天數：", sum(1 for s in steps if s >= GOAL))
    best = max(rows, key=lambda row: int(row["步數"]))
    print("最高紀錄：", best["日期"], best["步數"])
