# 依月份篩選：日期屬於查詢的月份就印「是」
date, query = input().split()
if date.startswith(query):
    print("是")
else:
    print("否")
