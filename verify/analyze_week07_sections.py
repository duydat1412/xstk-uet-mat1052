import fitz, re, sys

sys.stdout.reconfigure(encoding='utf-8')

doc7 = fitz.open("week07.pdf")
full_text = ""
for page in doc7:
    full_text += page.get_text() + "\n"

# Normalize spaces around Vietnamese accents
import unicodedata
text_norm = unicodedata.normalize('NFC', full_text)

# Let's search sections
for i, page in enumerate(doc7):
    txt = page.get_text()
    if "Phần" in txt:
        first_few = [l.strip() for l in txt.split('\n') if l.strip()][:5]
        print(f"Slide {i+1}:", " | ".join(first_few))
