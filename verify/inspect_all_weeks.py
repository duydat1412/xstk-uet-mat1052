import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

files = [f"week0{i}.pdf" for i in range(1, 8)]
files.insert(2, "week03_plotnine.pdf")

for f in files:
    try:
        doc = fitz.open(f)
        p1 = doc[0].get_text().split('\n')
        p1_title = " | ".join([x.strip() for x in p1 if x.strip()][:3])
        p2_title = ""
        if len(doc) > 1:
            p2 = doc[1].get_text().split('\n')
            p2_title = " | ".join([x.strip() for x in p2 if x.strip()][:3])
        print(f"=== {f} ({len(doc)} pages) ===")
        print(f"  P1: {p1_title}")
        print(f"  P2: {p2_title}")
    except Exception as e:
        print(f"Error {f}: {e}")
