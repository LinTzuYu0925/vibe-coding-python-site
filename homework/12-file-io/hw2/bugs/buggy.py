import json

with open("settings.json", encoding="utf-8") as f:
    settings = json.load(f)
volume = settings.get("volume", 0)
if volume == 0:
    volume = 50
print(f"音量 {volume}")
