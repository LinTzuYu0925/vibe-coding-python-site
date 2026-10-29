# R5 稽核：range(len(...)) 的差一
scores = [80, 72, 65]
for i in range(len(scores)):
    print(i, scores[i])
print("---")
for i in range(1, len(scores)):
    print(i, scores[i])
print("---")
for i in range(len(scores) + 1):
    print(i, scores[i])
