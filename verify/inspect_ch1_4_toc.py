import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("docs/stat20_detailed_toc.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

in_scope = False
for line in lines:
    line = line.strip()
    if any(line.startswith(f"<h1> {i} Chương {i}") for i in range(1, 6)):
        in_scope = True
    elif "<h1> 5 Chương 5" in line:
        in_scope = False
        print(line)
        break
    
    if in_scope:
        if line.startswith("<h1>") or line.startswith("<h2>") or line.startswith("<h3>"):
            print(line)
