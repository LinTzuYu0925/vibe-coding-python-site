import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # 減少 TensorFlow 啟動訊息
import tensorflow as tf

# t0：Python list 與 tensor 的差別
scores_list = [80, 72, 65, 92, 88, 59]
scores = tf.constant(scores_list)

print("list 的型別：", type(scores_list))
print("tensor 的型別：", type(scores))
print("tensor：", scores)
print("shape：", scores.shape)
print("dtype：", scores.dtype)

# list 不能直接除以數字
try:
    print(scores_list / 100)
except TypeError as e:
    print("list / 100 失敗：", type(e).__name__, e)

# tensor 會每個元素都除
result = scores / 100
print("tensor / 100：", result)
print("結果 dtype：", result.dtype)
