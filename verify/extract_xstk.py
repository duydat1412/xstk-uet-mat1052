import os, json, subprocess

with open('site/hoc.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = '<script id="lessons-data">'
start = text.find(start_marker)
if start != -1:
    end = text.find('</script>', start)
    js_code = text[start + len(start_marker):end]
    
    # Write to temporary file
    with open('data/courses/xstk_raw.js', 'w', encoding='utf-8') as f_out:
        f_out.write(js_code)
    
    res = subprocess.run(
        ['node', '-e', 'console.log(JSON.stringify(require("./data/courses/xstk_raw.js").ALL_LESSONS))'],
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    if res.returncode == 0:
        data = json.loads(res.stdout)
        with open('data/courses/xstk.json', 'w', encoding='utf-8') as f_json:
            json.dump(data, f_json, ensure_ascii=False, indent=2)
        print(f"Successfully extracted {len(data)} XSTK lessons to data/courses/xstk.json")
        os.remove('data/courses/xstk_raw.js')
    else:
        print("Error executing node for XSTK:", res.stderr)
else:
    print("Could not find start marker for lessons-data")
