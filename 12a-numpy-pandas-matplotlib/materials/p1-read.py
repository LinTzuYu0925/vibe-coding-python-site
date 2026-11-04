import pandas as pd

df = pd.read_csv("students.csv")
print(df)
print(df["score"].mean())
print(len(df))
