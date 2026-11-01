# 最近 n 天的步數合計
numbers = [int(x) for x in input().split()]
n = numbers[0]          # 第一個數字：要看最近幾天
days = numbers[1:]      # 其他數字：每天的步數（千步），最舊的在前面
print(sum(days[-n:]))
