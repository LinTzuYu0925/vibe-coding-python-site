import pandas as pd

df = pd.read_csv("class-scores.csv")
print(df.shape)
print(list(df.columns))
s = df["chinese"]
print(type(df))
print(type(s))
print(s)
