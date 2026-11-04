import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Microsoft JhengHei"   # 中文字型（Windows 內建）
df = pd.read_csv("class-scores.csv")
df.plot(x="name", y="chinese", kind="bar", rot=0, fontsize=14,
        title="國文分數")
plt.tight_layout()
plt.savefig("chinese.png")
