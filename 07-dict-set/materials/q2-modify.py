# Q2：通訊錄，新增、修改、刪除
phone = {"小明": "0912-345-678", "小華": "0922-111-222"}
phone["小美"] = "0933-555-666"
print(phone)
phone["小明"] = "0900-000-000"
print(phone)
del phone["小華"]
print(phone)
print(len(phone))

dup = {"a": 1, "a": 2}
print(dup)
