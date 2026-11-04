import pandas as pd

df = pd.read_csv("class-scores.csv")
print(df[["name", "chinese"]])
print(df["chinese"] >= 80)
print(df[df["chinese"] >= 80])
