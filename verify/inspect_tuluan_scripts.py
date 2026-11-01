import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for fname in ['verify/generate_tuluan_full.py', 'verify/append_topics_3_4.py']:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
            ids = re.findall(r'\"id\":\s*\"(TL\d+_\d+)\"', content)
            print(f"{fname}: {len(ids)} exercises found -> {ids}")
    except Exception as e:
        print(f"Error reading {fname}: {e}")
