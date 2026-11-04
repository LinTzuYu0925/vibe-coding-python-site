from dataset import Dataset
def test_average():
    d = Dataset(["小明", "技安"], [80, 59])
    assert d.average() == 69.5
def test_passed_names():
    d = Dataset(["阿美", "技安"], [60, 59])
    assert d.passed_names() == ["阿美"]
def test_empty():
    d = Dataset([], [])
    assert d.average() is None
if __name__ == "__main__":   # 沒有 pytest 時的備案：python test_dataset.py
    test_average()
    test_passed_names()
    test_empty()
    print("三個測試都通過")
