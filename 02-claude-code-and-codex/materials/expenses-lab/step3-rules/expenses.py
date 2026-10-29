# 記帳小工具 v2：列出、新增一筆（會檢查輸入）
import csv
from datetime import date

CSV_FILE = "expenses.csv"


def load_expenses():
    """讀取 CSV，回傳一個清單，每一筆是一個字典。"""
    with open(CSV_FILE, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def show_list(rows):
    """列出每一筆記帳，最後印出總金額。"""
    if not rows:
        print("目前沒有任何記帳資料。")
        return
    total = 0
    for number, row in enumerate(rows, start=1):
        print(f"{number}. {row['日期']}  {row['項目']}  {row['金額']}")
        total += int(row["金額"])
    print(f"總金額：{total}")


def ask_date():
    """詢問日期；直接按 Enter 就用今天。格式錯誤時回傳 None。"""
    text = input("日期（YYYY-MM-DD，直接按 Enter 代表今天）：").strip()
    if text == "":
        return date.today().isoformat()
    try:
        return date.fromisoformat(text).isoformat()
    except ValueError:
        print("日期格式不對，請用 2026-10-28 這種寫法。")
        return None


def ask_item():
    """詢問項目；空白時回傳 None。"""
    text = input("項目：").strip()
    if text == "":
        print("項目不能是空白。")
        return None
    return text


def ask_amount():
    """詢問金額；不是正整數時回傳 None。"""
    text = input("金額：").strip()
    if not (text.isascii() and text.isdigit()) or int(text) <= 0:
        print("金額必須是大於 0 的整數。")
        return None
    return int(text)


def add_expense():
    """新增一筆記帳到 CSV 的最後一行。任何一項不對就不新增。"""
    day = ask_date()
    if day is None:
        return
    item = ask_item()
    if item is None:
        return
    amount = ask_amount()
    if amount is None:
        return
    with open(CSV_FILE, "a", encoding="utf-8", newline="") as f:
        csv.writer(f).writerow([day, item, amount])
    print(f"已新增：{day}  {item}  {amount}")


def main():
    while True:
        print("\n1 列出　2 新增　0 離開")
        choice = input("請選擇：").strip()
        if choice == "1":
            show_list(load_expenses())
        elif choice == "2":
            add_expense()
        elif choice == "0":
            print("再見！")
            break
        else:
            print("請輸入 1、2 或 0。")


if __name__ == "__main__":
    main()
