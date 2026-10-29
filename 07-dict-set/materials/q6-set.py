# Q6：set 去重
ids = [3, 1, 3, 2, 1]
unique = set(ids)
print(unique)
print(len(ids), len(unique))
print(2 in unique)
unique.add(5)
print(unique)
unique.add(3)
print(unique)

clubs = ["羽球", "籃球", "羽球", "桌球", "籃球"]
print(len(clubs))
print(len(set(clubs)))
print(sorted(set(clubs)))
print(type({}), type(set()), type({1, 2}))
