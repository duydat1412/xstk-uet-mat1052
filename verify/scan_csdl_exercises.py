import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('docs/csdl_slides_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for fname, fcontent in data.items():
    print(f"\n=======================================================")
    print(f"FILE: {fname} (Total: {fcontent['total']})")
    print(f"=======================================================")
    exercises = []
    for s in fcontent['slides']:
        num = s.get('slide_num') or s.get('page_num')
        title = s.get('title', '')
        txt = s.get('text', '')
        # Check for exercise keywords
        if any(kw in txt.lower() for kw in ['bài tập', 'ví dụ', 'câu hỏi', 'xét quan hệ', 'cho lược đồ', 'yêu cầu']):
            # Filter meaningful lines
            first_lines = [l for l in txt.split('\n') if l.strip()][:3]
            exercises.append((num, title, " | ".join(first_lines)))
    
    print(f"Found {len(exercises)} potential exercise/example slides:")
    for num, title, snippet in exercises[:8]:
        print(f"  Slide {num}: {snippet[:120]}")
