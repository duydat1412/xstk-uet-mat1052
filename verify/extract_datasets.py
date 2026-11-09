import os, json, re

os.makedirs('data/courses', exist_ok=True)

# 1. Extract CSDL lessons from content_csdl/lessons_all.js
with open('content_csdl/lessons_all.js', 'r', encoding='utf-8') as f:
    csdl_code = f.read()

# We can run node to dump ALL_CSDL_LESSONS as JSON
import subprocess
res_csdl = subprocess.run(
    ['node', '-e', 'console.log(JSON.stringify(require("./content_csdl/lessons_all.js").ALL_CSDL_LESSONS))'],
    capture_output=True,
    text=True,
    encoding='utf-8'
)

if res_csdl.returncode == 0:
    csdl_data = json.loads(res_csdl.stdout)
    with open('data/courses/csdl.json', 'w', encoding='utf-8') as f:
        json.dump(csdl_data, f, ensure_ascii=False, indent=2)
    print(f"Extracted {len(csdl_data)} CSDL lessons to data/courses/csdl.json")
else:
    print("Error extracting CSDL:", res_csdl.stderr)

# 2. Extract XSTK lessons from site/hoc.html
with open('site/hoc.html', 'r', encoding='utf-8') as f:
    hoc_html = f.read()

# Extract the script content from hoc.html (the first script tag containing CUM_A to CUM_E)
script_match = re.search(r'<script>([\s\S]*?module\.exports = \{ ALL_LESSONS[\s\S]*?\};[\s\S]*?)</script>', hoc_html)
if script_match:
    script_js = script_match.group(1)
    with open('data/courses/xstk_raw.js', 'w', encoding='utf-8') as f:
        f.write(script_js)
    
    res_xstk = subprocess.run(
        ['node', '-e', 'console.log(JSON.stringify(require("./data/courses/xstk_raw.js").ALL_LESSONS))'],
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    if res_xstk.returncode == 0:
        xstk_data = json.loads(res_xstk.stdout)
        with open('data/courses/xstk.json', 'w', encoding='utf-8') as f:
            json.dump(xstk_data, f, ensure_ascii=False, indent=2)
        print(f"Extracted {len(xstk_data)} XSTK lessons to data/courses/xstk.json")
        os.remove('data/courses/xstk_raw.js')
    else:
        print("Error running node for XSTK:", res_xstk.stderr)
else:
    print("Could not find XSTK script block in hoc.html")
