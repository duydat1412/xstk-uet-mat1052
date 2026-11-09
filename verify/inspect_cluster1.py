import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('docs/csdl_slides_raw.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print('=== C1 KEY SLIDES ===')
for s in d['C1 .pptx']['slides']:
    txt = s['text']
    if any(k in txt.lower() for k in ['kiến trúc 3', 'độc lập dữ liệu', 'dbms', 'người dùng', 'mô hình']):
        print(f"Slide {s['slide_num']}: {txt[:160]}\n")

print('=== C2_1 KEY SLIDES ===')
for s in d['C2_1.pptx']['slides']:
    txt = s['text']
    if any(k in txt.lower() for k in ['thực thể yếu', 'tỉ số', 'bán_hàng', 'thư viện', 'đa trị', 'tổng hợp']):
        print(f"Slide {s['slide_num']}: {txt[:160]}\n")

print('=== C2_2 KEY SLIDES ===')
for s in d['C2_2.pptx']['slides']:
    txt = s['text']
    if any(k in txt.lower() for k in ['chuyên biệt', 'khái quát', 'rời rạc', 'đầy đủ', 'lớp cha']):
        print(f"Slide {s['slide_num']}: {txt[:160]}\n")
