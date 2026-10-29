# hello.py：確認 Python 環境正常（講師提供的完成版）
import sys
from datetime import date

name = "你的名字"
print(f"你好，我是 {name}")
print(f"Python 版本：{sys.version.split()[0]}")
print(f"今天日期：{date.today()}")
