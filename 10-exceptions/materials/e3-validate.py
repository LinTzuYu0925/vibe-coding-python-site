# E3：輸入驗證，用 if 檢查，不要等出錯
def parse_score(text):
    text = text.strip()
    if text == "":
        return None
    try:
        score = float(text)
    except ValueError:
        return None
    if score < 0 or score > 100:
        return None
    return score

for t in ["85", " 72.5 ", "", "abc", "-5", "101", "100", "0"]:
    print(repr(t), "->", parse_score(t))
