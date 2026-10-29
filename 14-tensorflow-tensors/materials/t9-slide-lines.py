import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # 減少 TensorFlow 啟動訊息
import tensorflow as tf

# t9：投影片上「改寫列印」的那幾行，這裡照投影片的寫法實際印一次

print("--- 頁 4 ---")
scores = [80, 72, 65, 92, 88, 59]
try:
    print(scores / 100)
except TypeError as e:
    print("TypeError:", e)
t = tf.constant(scores)
print((t / 100).numpy())

print("--- 頁 7 ---")
a = tf.constant(5)
b = tf.constant([80, 72, 65, 92, 88, 59])
c = tf.constant([[80, 72],
                 [65, 92],
                 [88, 59]])
print(a.shape, b.shape, c.shape)

print("--- 頁 9 ---")
t = tf.constant([80, 72, 65, 92, 88, 59])
print(t[0].numpy(), t[-1].numpy())
print(t[1:4].numpy())
m = tf.constant([[80, 72], [65, 92], [88, 59]])
print(m[:, 0].numpy())

print("--- 頁 12 ---")
s = tf.constant([80, 72, 65, 92, 88, 59],
                dtype=tf.float32)
print((s / 100).numpy())
print((s >= 60).numpy())
print(tf.reduce_mean(s).numpy())
print(tf.boolean_mask(s, s >= 60).numpy())

print("--- 頁 21：拿掉 dtype=tf.float32 ---")
float_list = [80.0, 72.0, 65.0, 92.0, 88.0, 59.0]   # 像 float(row["score"])
int_list = [80, 72, 65, 92, 88, 59]                 # 像 int(row["score"])
x = tf.constant(float_list)
y = tf.constant(int_list)
print("小數清單、沒寫 dtype：", x.dtype, tf.reduce_mean(x).numpy())
print("整數清單、沒寫 dtype：", y.dtype, (y / 100).dtype)
