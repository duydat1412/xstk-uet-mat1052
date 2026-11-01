import sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

with open('site/hoc.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print(f"site/hoc.html size: {len(html)} chars (~{len(html.encode('utf-8'))/1024:.2f} KB)")
print(f"Title: {soup.title.string}")
print(f"Scripts count: {len(soup.find_all('script'))}")

# Check if ALL_LESSONS is present in script
assert "ALL_LESSONS" in html, "ALL_LESSONS must be present in hoc.html"
assert "CUM_A" in html, "CUM_A must be present"
assert "CUM_E" in html, "CUM_E must be present"

print("HTML structure and inline data verified successfully!")
