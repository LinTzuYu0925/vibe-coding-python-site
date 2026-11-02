# 遊覽車台數
import math

people = int(input())
buses = math.floor(people / 40) + 1
empty = buses * 40 - people
print(f"需要 {buses} 台車，最後一台空 {empty} 個位子")
