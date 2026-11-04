from pathlib import Path
p = Path("data") / "scores.txt"
print(p)
print(p.exists())
print(Path("scores.txt").exists())
for p in Path(".").glob("*.csv"):
    print(p.name)
with open(Path("scores.txt"), encoding="utf-8") as f:
    print(f.readline().strip())
