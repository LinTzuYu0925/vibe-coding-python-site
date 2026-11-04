# 頁「看到這些先別慌」：每段只求讀懂
import asyncio
import functools
import logging
import re
import argparse

# ① 裝飾器（decorator）
@functools.cache
def square(n):
    return n * n
print(square(9))

# ② 產生器（generator）
def numbers():
    for n in [80, 72, 65]:
        yield n
print(list(numbers()))

# ③ async／await
async def fetch():
    await asyncio.sleep(0.1)
    return "done"
print(asyncio.run(fetch()))

# ④ logging
logging.basicConfig(level=logging.INFO)
logging.info("讀到 6 筆資料")

# 〔選修〕re
print(re.findall(r"\d+", "小明80分、小華72分"))

# 〔選修〕argparse
parser = argparse.ArgumentParser()
parser.add_argument("--file", default="students.csv")
args = parser.parse_args([])
print(args.file)
