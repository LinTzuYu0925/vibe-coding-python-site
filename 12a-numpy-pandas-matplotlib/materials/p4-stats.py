import pandas as pd

df = pd.read_csv("class-scores.csv")
print(df["english"].describe())
print(df.groupby("class")["english"].mean())
