import pandas as pd

df = pd.read_csv("class-scores.csv")
arr = df[["chinese", "english"]].to_numpy()
print(type(arr))
print(arr.shape)
print(arr.dtype)
print(arr[0])
print(arr[:, 0])
print(arr + 5)
