import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # 減少 TensorFlow 啟動訊息
import tensorflow as tf

# t4：逐元素運算、統計、遮罩、廣播
scores = tf.constant([80, 72, 65, 92, 88, 59], dtype=tf.float32)

print("scores / 100：", scores / 100)
print("scores + 5：", scores + 5)
print("scores * 2：", scores * 2)
mask = scores >= 60
print("scores >= 60：", mask)
print("mean：", tf.reduce_mean(scores))
print("max：", tf.reduce_max(scores))
print("sum：", tf.reduce_sum(scores))
print("boolean_mask：", tf.boolean_mask(scores, mask))
print("where：", tf.where(mask, scores, 0.0))

# 廣播：(3,2) 減去每欄的平均 shape (2,)
m = tf.constant([[80.0, 72.0], [65.0, 92.0], [88.0, 59.0]])
col = tf.constant([70.0, 80.0])
print("矩陣 - 向量：", m - col)

# dtype 不同不能相加
try:
    print(tf.constant([1, 2]) + tf.constant([0.5, 1.5]))
except Exception as e:
    print("dtype 混用錯誤：", type(e).__name__, e)

r = tf.constant([1, 2]) / 100
print("int32 / 100：", r, r.dtype)
