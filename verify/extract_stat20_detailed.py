import sys, re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

with open("STAT20_in_Vietnamese_stripped.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

headings = soup.find_all(['h1', 'h2', 'h3', 'h4'])
print(f"Total headings: {len(headings)}")

with open("docs/stat20_detailed_toc.txt", "w", encoding="utf-8") as out:
    for h in headings:
        lvl = h.name
        txt = " ".join(h.get_text().split())
        # Filter relevant chapters: 1, 2, 3, 4, 7
        out.write(f"<{lvl}> {txt}\n")

print("Saved docs/stat20_detailed_toc.txt")
