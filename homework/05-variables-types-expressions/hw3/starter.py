# 找零錢：用最少的硬幣找錢
change = int(input())        # 要找的錢（元）

coin50 = change // 50        # 50 元硬幣幾枚
change = change % 50         # 剩下還要找多少

# 接著算 10 元、5 元、1 元各幾枚

print(f"50 元 {coin50} 枚")
