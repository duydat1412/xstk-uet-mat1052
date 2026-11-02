import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

clusters = ['a', 'b', 'c', 'd', 'e']
for c in clusters:
    fname = f"content/cum_{c}.js"
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Find all lessons
    matches = re.finditer(r'id:\s*["\']([A-E]\d+)["\'][\s\S]*?title:\s*["\'](.*?)["\'][\s\S]*?examples:\s*\[([\s\S]*?)\]\s*,\s*pitfalls', text)
    for m in matches:
        lid = m.group(1)
        ltitle = m.group(2)
        ex_block = m.group(3)
        # extract each example q
        q_matches = re.findall(r'q:\s*["\'](.*?)["\']', ex_block)
        print(f"=== {lid}: {ltitle} ===")
        for i, q in enumerate(q_matches):
            print(f"  Ex {i+1}: {q[:100]}...")
