# 兩天活動總人數
saturday, sunday = input().split("/")
sat = saturday.split()
sun = sunday.split()
both = set(sat) & set(sun)
total = len(sat) + len(sun) - len(both)
print(f"兩天都來 {len(both)} 人，總共 {total} 人")
