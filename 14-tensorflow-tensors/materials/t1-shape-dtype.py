import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # 減少 TensorFlow 啟動訊息
import tensorflow as tf

# t1：shape、dtype、rank
a = tf.constant(5)
v = tf.constant([80, 72, 65, 92, 88, 59])
m = tf.constant([[80, 72], [65, 92], [88, 59]])

print("純量 shape：", a.shape, "dtype：", a.dtype, "rank：", tf.rank(a).numpy())
print("向量 shape：", v.shape, "dtype：", v.dtype, "rank：", len(v.shape))
print("矩陣 shape：", m.shape, "dtype：", m.dtype, "rank：", len(m.shape))

print("整數 dtype：", tf.constant([80, 72]).dtype)
print("小數 dtype：", tf.constant([80.0, 72.0]).dtype)
print("整數混小數 dtype：", tf.constant([80, 72.5]).dtype)

x = tf.constant([80, 72], dtype=tf.float32)
print("指定 float32：", x, x.dtype)
