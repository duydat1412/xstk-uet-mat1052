import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('docs/csdl_slides_raw.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print('=== C3_1 KEY SLIDES ===')
for s in d['C3_1.pptx']['slides']:
    txt = s['text']
    if any(k in txt.lower() for k in ['chuyển sang', 'bài tập', 'khóa ngoại', 'toàn vẹn']):
        print(f"Slide {s['slide_num']}: {txt[:160]}\n")

print('=== C3_2 KEY SLIDES ===')
count = 0
for s in d['C3_2.pdf']['slides']:
    txt = s['text']
    if any(k in txt.lower() for k in ['phép chọn', 'phép chiếu', 'phép kết nối', 'phép chia', 'gom nhóm', 'cây truy vấn']):
        count += 1
        if count <= 10:
            print(f"Page {s['page_num']}: {txt[:160]}\n")

print('=== C4_1 KEY SLIDES ===')
for s in d['C4_1.pptx']['slides']:
    txt = s['text']
    if any(k in txt.lower() for k in ['armstrong', 'bao đóng', 'tìm khóa', '3nf', 'bcnf', 'bảo toàn']):
        print(f"Slide {s['slide_num']}: {txt[:160]}\n")
