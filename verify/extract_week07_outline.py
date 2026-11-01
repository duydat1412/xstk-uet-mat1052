import fitz
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('week07.pdf')

pages_data = []
for idx, page in enumerate(doc):
    text = page.get_text()
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    pages_data.append({
        'page': idx + 1,
        'title': lines[0] if lines else '',
        'subtitle': lines[1] if len(lines) > 1 else '',
        'lines': lines[:8]
    })

with open('docs/week07_outline.json', 'w', encoding='utf-8') as f:
    json.dump(pages_data, f, ensure_ascii=False, indent=2)

print(f"Extracted outline for {len(pages_data)} pages of week07.pdf")
