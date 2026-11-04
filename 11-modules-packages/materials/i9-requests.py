# 頁「第一個套件：requests 向網站要資料」
import requests
url = "https://jsonplaceholder.typicode.com/todos/1"
r = requests.get(url, timeout=10)
print(r.status_code)
data = r.json()
print(type(data))
print(data["title"])

# 頁「網路會失敗：先看狀態碼，再用 try 接住」
url = "https://jsonplaceholder.typicode.com/todos/99999"
r = requests.get(url, timeout=10)
print(r.status_code)
print(r.json())

bad = "https://no-such-host.invalid"
try:
    requests.get(bad, timeout=5)
except requests.exceptions.ConnectionError:
    print("連不上：檢查網路或網址")
