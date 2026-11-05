# 頁「@ 是什麼」：寫 @dataclass，和寫 Dataset = dataclass(Dataset)，結果一樣
from dataclasses import dataclass


@dataclass                      # 寫法一：用 @
class Dataset:
    names: list
    scores: list

print(Dataset(["小明"], [80]))


class Dataset:                  # 寫法二：不用 @，自己交給 dataclass 加工
    names: list
    scores: list

Dataset = dataclass(Dataset)

print(Dataset(["小明"], [80]))
