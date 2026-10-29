# 寫 CSV：有 newline="" 與沒有 newline="" 的差別
import csv
import ml_stats

rows = []
with open("students.csv", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        rows.append(row)

with open("report.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score", "passed"])
    for row in rows:
        score = int(row["score"])
        ok = len(ml_stats.passed([score])) == 1
        writer.writerow([row["name"], score, ok])

print("--- report.csv 內容 ---")
with open("report.csv", encoding="utf-8") as f:
    print(f.read())

# 沒有 newline=""
with open("report-nonl.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerow(["小明", 80])

with open("report.csv", "rb") as f:
    print("有 newline=\"\" 的位元組：", f.read()[:30])
with open("report-nonl.csv", "rb") as f:
    data = f.read()
    print("沒有 newline=\"\" 的位元組：", data)
    print("出現 \\r\\r\\n 嗎？", b"\r\r\n" in data)
with open("report-nonl.csv", encoding="utf-8") as f:
    print("用文字模式讀回來：", repr(f.read()))
