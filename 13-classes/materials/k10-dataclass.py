from dataclasses import dataclass


@dataclass
class Dataset:
    names: list
    scores: list


d = Dataset(["小明", "技安"], [80, 59])
print(d.names)
print(d)
