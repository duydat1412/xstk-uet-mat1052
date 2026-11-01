import fitz, sys
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
    for i in range(min(5, len(doc))):
        text = doc[i].get_text().strip()
        first_line = text.split('\n')[0] if text else ''
        print(f"  Slide {i+1}: {first_line}")
    text_last = doc[len(doc)-1].get_text().strip()
    first_last = text_last.split('\n')[0] if text_last else ''
    print(f"  Last slide ({len(doc)}): {first_last}")
