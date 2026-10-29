# F2：位置、名稱與預設值
def is_passed(average, line=60):
    return average >= line

print(is_passed(72.3))
print(is_passed(59.9))
print(is_passed(72.3, 80))
print(is_passed(average=72.3, line=70))
print(is_passed(60))
print(is_passed(60, line=61))
