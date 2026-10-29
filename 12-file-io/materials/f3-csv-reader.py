# csv.reader 與 csv.DictReader
import csv

print("--- csv.reader（每列是 list）---")
with open("students.csv", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    next(reader)  # 跳過標題列
    for row in reader:
        print(row, type(row), type(row[1]))

print("--- csv.DictReader（每列是 dict）---")
with open("students.csv", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        score = int(row["score"])  # 讀出來是字串，要自己轉
        print(row["name"], type(row["score"]), score, type(score))
