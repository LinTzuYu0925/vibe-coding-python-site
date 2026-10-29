import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # 減少 TensorFlow 啟動訊息
import tensorflow as tf

# t7：ML 資料小幫手 — 用 tensor 處理 students.csv
import csv

names = []
scores_list = []
with open("students.csv", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        names.append(row["name"])
        scores_list.append(float(row["score"]))

scores = tf.constant(scores_list, dtype=tf.float32)
print("shape：", scores.shape)
print("dtype：", scores.dtype)
print("平均：", tf.reduce_mean(scores).numpy())
print("正規化（/100）：", (scores / 100).numpy())

mask = scores >= 60
print("遮罩：", mask.numpy())
count = tf.reduce_sum(tf.cast(mask, tf.int32))
print("及格人數：", count.numpy())

mask_list = mask.numpy()
for i in range(len(names)):
    if mask_list[i]:
        print("及格：", names[i])
