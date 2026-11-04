# 稽核用的壞版本：我們依常見疏漏自己寫的，不是某個 Agent 的真實輸出
import pandas as pd

df = pd.read_csv("class-scores.csv")
low = df[df["math"] <= 60]          # 疏漏 1：題目是「低於 60」，寫成 <=
print(list(low["name"]))
try:
    print(df["Math"].mean())        # 疏漏 2：欄名大小寫拼錯
except KeyError as e:
    print("KeyError:", e)
