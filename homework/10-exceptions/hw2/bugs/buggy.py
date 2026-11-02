# 聚餐分攤
try:
    total, people = input().split()
    total = int(total)
    people = int(people)
    print(f"每人 {total // people} 元，剩 {total % people} 元")
except Exception:
    print("請輸入兩個整數")
