import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open("content/lessons_all.js", "r", encoding="utf-8") as f:
    text = f.read()

pattern = r'id:\s*["\']([A-E]\d+)["\'],\s*cluster:\s*["\']([A-E])["\'],\s*title:\s*["\'](.*?)["\'],\s*sources:\s*["\'](.*?)["\']'
matches = re.findall(pattern, text)
print(f"Found {len(matches)} lessons:")
for m in matches:
    print(f"{m[0]}: {m[2]} | sources: {m[3]}")
