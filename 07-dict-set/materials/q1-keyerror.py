# Q1：查不存在的 key，重現 KeyError
words = {"cat": "貓", "dog": "狗", "fish": "魚"}
print(words["bird"])
