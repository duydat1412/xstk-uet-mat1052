import re
import sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

with open("STAT20_in_Vietnamese_stripped.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# Find table of contents or headers
headings = soup.find_all(['h1', 'h2', 'h3'])
print(f"Total headings found: {len(headings)}")

with open("docs/stat20_headings.txt", "w", encoding="utf-8") as out:
    for h in headings:
        level = h.name
        text = " ".join(h.get_text().split())
        out.write(f"{level.upper()}: {text}\n")

print("Saved headings to docs/stat20_headings.txt")

# Print top-level H1 and major H2
print("\n--- Summary of H1 / Major Sections ---")
for h in soup.find_all('h1'):
    print("H1:", " ".join(h.get_text().split()))
