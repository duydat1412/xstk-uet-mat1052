import re
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

# Search for STAT20 html file
candidate_paths = [
    r"C:\Users\DAT\Downloads\STAT20_in_Vietnamese_2026.10.05.html",
    r"C:\Users\DAT\Downloads\STAT20_in_Vietnamese.html",
    r"d:\Projects\XSTK\STAT20_in_Vietnamese_2026_10_05.html"
]

src_path = None
for p in candidate_paths:
    if os.path.exists(p):
        src_path = p
        break

if not src_path:
    print("Error: STAT20 file not found!")
    sys.exit(1)

print(f"Reading from {src_path} ...")
with open(src_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

print(f"Original file length: {len(content)} characters (~{len(content.encode('utf-8')) / (1024*1024):.2f} MB)")

# Strip base64 data
stripped = re.sub(r'data:image\/[a-zA-Z0-9\+\-\.]+;base64,[^"\'\s\)]+', 'data:image/...[STRIPPED]', content)
print(f"Stripped file length: {len(stripped)} characters (~{len(stripped.encode('utf-8')) / (1024*1024):.2f} MB)")

out_path = r"d:\Projects\XSTK\STAT20_in_Vietnamese_stripped.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(stripped)

print(f"Successfully saved stripped HTML to: {out_path}")
