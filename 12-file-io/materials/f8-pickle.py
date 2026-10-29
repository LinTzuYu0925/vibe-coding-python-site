# pickle：Python 專用的二進位格式
import pickle

data = {"name": "小明", "score": 80}
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)
with open("data.pkl", "rb") as f:
    print(pickle.load(f))
with open("data.pkl", "rb") as f:
    print(f.read(20))
# 官方文件警告：絕對不要載入不信任來源的 pickle 資料。
