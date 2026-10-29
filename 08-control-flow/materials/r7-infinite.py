# R7：忘了更新變數的 while（只跑 5 圈就強制停，示範用）
n = 1
loops = 0
while n <= 3:
    loops = loops + 1
    if loops >= 5:
        print("已經跑了 5 圈，n 仍是", n, "，真的程式不會自己停")
        break
