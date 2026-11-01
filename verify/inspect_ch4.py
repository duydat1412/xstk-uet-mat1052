import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("docs/stat20_detailed_toc.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

in_ch4 = False
for line in lines:
    line = line.strip()
    if "<h1> 4 Chương 4" in line:
        in_ch4 = True
    elif "<h1> 5 Chương 5" in line:
        in_ch4 = False
        break
    if in_ch4:
        print(line)
