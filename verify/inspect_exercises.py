import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('week07.pdf')
for p in range(77, 92):
    print(f"*** SLIDE {p+1} ***")
    print(doc[p].get_text().strip())
    print("-" * 50)
