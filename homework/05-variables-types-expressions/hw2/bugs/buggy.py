# 影片長度換算：分鐘數換成「幾小時幾分」
minutes = int(input())
hours = round(minutes / 60)
rest = minutes % 60
print(f"{hours} 小時 {rest} 分")
