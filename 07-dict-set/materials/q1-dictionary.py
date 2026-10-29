# Q1：英中小字典，查詢、in、get
words = {"cat": "貓", "dog": "狗", "fish": "魚"}

print(words["cat"])
print(len(words))
print("dog" in words)
print("bird" in words)
print(words.get("fish"))
print(words.get("bird"))
print(words.get("bird", "找不到"))
