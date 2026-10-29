# P3：別名陷阱，b = a 不是複製
playlist = ["晴天", "七里香", "稻香"]
backup = playlist
backup.append("告白氣球")
print(playlist)
print(backup)
print(playlist is backup)

safe = ["晴天", "七里香", "稻香"]
copy = safe.copy()
copy.append("告白氣球")
print(safe)
print(copy)
