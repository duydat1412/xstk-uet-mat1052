import re
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("site/hoc.html", "r", encoding="utf-8") as f:
    html = f.read()

# Extract script blocks
# Specifically find the inline scripts that don't have src
script_pattern = re.compile(r'<script(?![^>]*src=)[^>]*>([\s\S]*?)<\/script>', re.IGNORECASE)
scripts = script_pattern.findall(html)

print(f"Found {len(scripts)} inline script blocks.")

for i, s in enumerate(scripts):
    fname = f"verify/temp_hoc_script_{i}.js"
    with open(fname, "w", encoding="utf-8") as tmp:
        tmp.write(s)
    res = subprocess.run(["node", "--check", fname], capture_output=True, text=True)
    if res.returncode == 0:
        print(f"  Script block {i+1}: Node.js syntax OK!")
    else:
        print(f"  Script block {i+1}: Node.js syntax ERROR:\n{res.stderr}")
        sys.exit(1)

print("All inline scripts in site/hoc.html validated successfully!")
