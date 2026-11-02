import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("docs/all_slide_exercises.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data.get("week06.pdf", []):
    print(f"Slide {item['page']}: {item['header']}")
