# F5 陷阱：函式裡面想改全域的數字
count = 0

def add_one():
    count = count + 1

add_one()
print(count)
