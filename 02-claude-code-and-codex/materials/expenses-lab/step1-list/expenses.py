# 記帳小工具 v1：讀取 expenses.csv，列出每一筆並算出總金額
import csv

CSV_FILE = "expenses.csv"


def load_expenses():
    """讀取 CSV，回傳一個清單，每一筆是一個字典。"""
    with open(CSV_FILE, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def show_list(rows):
    """列出每一筆記帳，最後印出總金額。"""
    total = 0
    for number, row in enumerate(rows, start=1):
        print(f"{number}. {row['日期']}  {row['項目']}  {row['金額']}")
        total += int(row["金額"])
    print(f"總金額：{total}")


def main():
    rows = load_expenses()
    if not rows:
        print("目前沒有任何記帳資料。")
        return
    show_list(rows)


if __name__ == "__main__":
    main()
