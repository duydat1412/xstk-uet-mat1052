import fitz
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

file_list = [
    "week01.pdf",
    "week02.pdf",
    "week03_plotnine.pdf",
    "week04.pdf",
    "week05.pdf",
    "week06.pdf",
    "week07.pdf"
]

all_slide_exercises = {}

for fname in file_list:
    doc = fitz.open(fname)
    all_slide_exercises[fname] = []
    for i, page in enumerate(doc):
        text = page.get_text()
        text_lower = text.lower()
        # Look for indicators of examples / exercises / solutions
        is_ex = bool(re.search(r'(w0[1-7]-(ex|wp|ch|th|case|bt|q)\d+|ví dụ\s*\d*|bài tập\s*\d*|bài mẫu|đáp án|lời giải|tự kiểm tra|openintro\s*4e|ims2e)', text_lower))
        if is_ex:
            lines = [l.strip() for l in text.split('\n') if l.strip()]
            header = " | ".join(lines[:3]) if lines else ""
            all_slide_exercises[fname].append({
                "page": i + 1,
                "header": header,
                "full_text": text.strip()
            })

print(f"Extraction summary:")
for fname, ex_list in all_slide_exercises.items():
    print(f"  {fname}: {len(ex_list)} slides with examples/exercises")

with open("docs/all_slide_exercises.json", "w", encoding="utf-8") as f:
    json.dump(all_slide_exercises, f, ensure_ascii=False, indent=2)

print("Saved to docs/all_slide_exercises.json!")
