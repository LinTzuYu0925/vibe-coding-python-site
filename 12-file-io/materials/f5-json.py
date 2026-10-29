# JSON 存取與常見陷阱
import json

data = [
    {"name": "小明", "score": 80},
    {"name": "小華", "score": 72},
    {"name": "阿美", "score": 65},
]

with open("report.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
with open("report.json", encoding="utf-8") as f:
    back = json.load(f)
print(type(back), back == data)
with open("report.json", encoding="utf-8") as f:
    print(f.read())

print("--- 沒有 ensure_ascii=False ---")
print(json.dumps(data[:1], indent=2))

print("--- tuple 變 list ---")
t = {"point": (1, 2)}
print(json.loads(json.dumps(t)))

print("--- int 的 key 變 str ---")
d = {1: "一", 2: "二"}
print(json.loads(json.dumps(d, ensure_ascii=False)))

print("--- set 不能存 ---")
try:
    json.dumps({"tags": {1, 2}})
except TypeError as e:
    print("TypeError:", e)
