# 略過壞資料的加總
total = 0
skipped = 0
try:
    for word in input().split():
        total = total + int(word)
except ValueError:
    skipped = skipped + 1
print(f"總和 {total}，略過 {skipped} 個")
