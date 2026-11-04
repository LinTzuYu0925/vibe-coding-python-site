# 沒有設定中文字型：中文變方框
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("class-scores.csv")
df.plot(x="name", y="chinese", kind="bar", rot=0, fontsize=14,
        title="國文分數")
plt.tight_layout()
plt.savefig("chinese-boxes.png")
