import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # 減少 TensorFlow 啟動訊息
import tensorflow as tf

# t3：索引與切片
t = tf.constant([80, 72, 65, 92, 88, 59])
m = tf.constant([[80, 72], [65, 92], [88, 59]])

print("t[0]：", t[0])
print("t[0].numpy()：", t[0].numpy())
print("t[-1]：", t[-1], t[-1].numpy())
print("t[1:4]：", t[1:4], t[1:4].numpy())
print("t[:3]：", t[:3], t[:3].numpy())

print("m[0]：", m[0], m[0].numpy())
print("m[:,0]：", m[:, 0], m[:, 0].numpy())
print("m[1,1]：", m[1, 1], m[1, 1].numpy())
