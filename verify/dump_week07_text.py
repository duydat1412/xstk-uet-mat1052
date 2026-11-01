import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('week07.pdf')
with open('docs/week07_full_text.txt', 'w', encoding='utf-8') as out:
    for idx, page in enumerate(doc):
        out.write(f"\n==================== TRANG {idx+1} / {len(doc)} ====================\n")
        out.write(page.get_text())

print("Saved week07_full_text.txt")
