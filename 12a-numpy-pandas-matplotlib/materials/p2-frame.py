import pandas as pd
import numpy as np
df = pd.read_csv("class-scores.csv")
print(df.shape)
print(list(df.columns))
s = df["chinese"]
print(type(df))
print(type(s))
print(s)


data = {
    "name": ["A", "B", "C"],
    "score": [90, 80, 70]}
df2 = pd.DataFrame(data)
print(df2)
print(df2['name'][2])

dn = df2.to_numpy()
print(dn)