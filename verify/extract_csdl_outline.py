import os
import sys
import json
import pptx
import fitz

sys.stdout.reconfigure(encoding='utf-8')

folder = 'tailieu_csdl'

def analyze_pptx(fpath):
    prs = pptx.Presentation(fpath)
    slides_info = []
    for idx, slide in enumerate(prs.slides):
        texts = []
        for shape in slide.shapes:
            if shape.has_text_frame:
                t = shape.text.strip()
                if t:
                    texts.append(t)
        full_text = "\n".join(texts)
        first_line = full_text.split('\n')[0] if full_text else ""
        slides_info.append({
            "slide_num": idx + 1,
            "title": first_line[:120],
            "text": full_text
        })
    return slides_info

def analyze_pdf(fpath):
    doc = fitz.open(fpath)
    pages_info = []
    for idx in range(len(doc)):
        page = doc[idx]
        full_text = page.get_text().strip()
        first_line = full_text.split('\n')[0] if full_text else ""
        pages_info.append({
            "page_num": idx + 1,
            "title": first_line[:120],
            "text": full_text
        })
    return pages_info

summary = {}
for fname in sorted(os.listdir(folder)):
    fpath = os.path.join(folder, fname)
    print(f"Analyzing {fname}...")
    if fname.endswith('.pptx'):
        info = analyze_pptx(fpath)
        summary[fname] = {
            "type": "pptx",
            "total": len(info),
            "slides": info
        }
    elif fname.endswith('.pdf'):
        info = analyze_pdf(fpath)
        summary[fname] = {
            "type": "pdf",
            "total": len(info),
            "slides": info
        }

with open('docs/csdl_slides_raw.json', 'w', encoding='utf-8') as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)

print("\nSaved docs/csdl_slides_raw.json successfully!")
for fname, data in summary.items():
    print(f"- {fname}: {data['total']} slides/pages")
