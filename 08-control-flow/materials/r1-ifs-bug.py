# R1 陷阱：用多個 if 而不是 elif
score = 95
if score >= 90:
    print("優")
if score >= 80:
    print("良")
if score >= 60:
    print("及格")
