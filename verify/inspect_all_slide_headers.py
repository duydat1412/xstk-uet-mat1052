import fitz
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

for fname in file_list:
    doc = fitz.open(fname)
    print(f"\n=================== {fname} ({len(doc)} pages) ===================")
    for i in range(len(doc)):
        text = doc[i].get_text().strip()
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        header = " | ".join(lines[:2]) if lines else ""
        # print slides that look like section titles or contain interesting keywords
        if any(kw in header.lower() for kw in ['chương', 'phần', 'mục', 'bài', 'định lý', 'nội dung', 'tóm tắt', '1.', '2.', '3.', '4.', '5.', '6.', '7.']):
            if len(header) < 100:
                print(f"  Slide {i+1}: {header}")
