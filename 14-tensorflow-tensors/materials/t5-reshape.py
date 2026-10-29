import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # 減少 TensorFlow 啟動訊息
import tensorflow as tf

# t5：reshape
t = tf.constant([80, 72, 65, 92, 88, 59])
print("原本：", t.numpy(), t.shape)
print("(3,2)：", tf.reshape(t, (3, 2)).numpy())
print("(6,1)：", tf.reshape(t, (6, 1)).numpy())
r = tf.reshape(t, (2, -1))
print("(2,-1)：", r.numpy(), r.shape)

try:
    tf.reshape(t, (4, 2))
except Exception as e:
    print("reshape 錯誤：", type(e).__name__, e)

# 值的順序不變：攤平回來和原本一樣
flat = tf.reshape(tf.reshape(t, (3, 2)), (6,))
print("攤平回來：", flat.numpy())
