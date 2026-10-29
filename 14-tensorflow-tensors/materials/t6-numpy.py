import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # 減少 TensorFlow 啟動訊息
import tensorflow as tf

# t6：與 numpy 互換
import numpy as np

t = tf.constant([80.0, 72.0, 65.0])
arr = t.numpy()
print("numpy 陣列：", arr, type(arr))

np_arr = np.array([1.5, 2.5, 3.5])
print("np float64 -> tensor dtype：", tf.constant(np_arr).dtype)
print("np int 陣列 -> tensor dtype：", tf.constant(np.array([1, 2, 3])).dtype)

c = tf.convert_to_tensor([80, 72, 65])
print("convert_to_tensor(list)：", c, c.dtype)
print("python 小數 list dtype：", tf.convert_to_tensor([1.5, 2.5]).dtype)
