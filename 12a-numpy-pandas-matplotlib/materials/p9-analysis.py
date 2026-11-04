# 實作的講師版（沒有 Agent 額度時的備案）
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Microsoft JhengHei"

# ① 讀檔
df = pd.read_csv("class-scores.csv")

# ② 統計與篩選
print(df.groupby("class")["math"].mean())
low = df[df["math"] < 60]
print(list(low["name"]))

# ③ 畫圖存檔
df.plot(x="name", y="math", kind="bar", rot=0, fontsize=14,
        title="數學分數")
plt.tight_layout()
plt.savefig("math.png")

# ④ 轉陣列
arr = df[["chinese", "english", "math"]].to_numpy()
print(arr.shape)
