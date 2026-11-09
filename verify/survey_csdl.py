import os
import sys
import pptx
import fitz

sys.stdout.reconfigure(encoding='utf-8')

folder = 'tailieu_csdl'
files = sorted(os.listdir(folder))

for fname in files:
    fpath = os.path.join(folder, fname)
    print(f"\n=======================================================")
    print(f"FILE: {fname} (Size: {os.path.getsize(fpath):,} bytes)")
    print(f"=======================================================")
    
    if fname.endswith('.pptx'):
        prs = pptx.Presentation(fpath)
        print(f"Total slides: {len(prs.slides)}")
        # Print first 5 slide titles or text
        for idx, slide in enumerate(prs.slides):
            title = ""
            texts = []
            for shape in slide.shapes:
                if shape.has_text_frame:
                    t = shape.text.strip().replace('\n', ' ')
                    if t:
                        texts.append(t)
            first_txt = texts[0] if texts else "No text"
            if idx < 5 or idx == len(prs.slides) - 1:
                print(f"  Slide {idx+1}: {first_txt[:100]}")
    elif fname.endswith('.pdf'):
        doc = fitz.open(fpath)
        print(f"Total pages: {len(doc)}")
        for idx in range(min(5, len(doc))):
            page = doc[idx]
            txt = page.get_text().strip().replace('\n', ' ')
            print(f"  Page {idx+1}: {txt[:100]}")
