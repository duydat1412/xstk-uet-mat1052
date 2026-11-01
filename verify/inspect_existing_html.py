import sys, re
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')

with open('hoc-week07.html', 'r', encoding='utf-8') as f:
    text = f.read()

titles = re.findall(r't:\s*"([^"]+)"', text)
print(f"Titles in hoc-week07: {len(titles)}")
for i, t in enumerate(titles, 1):
    print(f"  {i}. {t}")

with open('on-tap-week07.html', 'r', encoding='utf-8') as f:
    ot = f.read()

cats = re.findall(r'c:\s*"([^"]+)"', ot)
print(f"\nCategories in on-tap-week07: {len(cats)}")
for c, cnt in Counter(cats).items():
    print(f"  {c}: {cnt}")

qs = re.findall(r'q:\s*"([^"]+)"', ot)
print(f"Total questions in on-tap: {len(qs)}")
