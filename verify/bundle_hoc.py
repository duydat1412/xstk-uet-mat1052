import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Read clean template of hoc.html (without the corrupted script)
with open('site/hoc.html', 'r', encoding='utf-8') as f:
    hoc = f.read()

# 2. Read clean content/lessons_all.js
with open('content/lessons_all.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

new_script = f'<script id="lessons-data">\n{js_content}\n</script>'

# Use lambda in re.sub so backslashes in js_content are NEVER treated as escape codes!
pattern = r'<script id="lessons-data">[\s\S]*?<\/script>'
if re.search(pattern, hoc):
    hoc = re.sub(pattern, lambda m: new_script, hoc)
    print("Cleanly replaced id=lessons-data using lambda replacer!")
elif '<script src="../content/lessons_all.js"></script>' in hoc:
    hoc = hoc.replace('<script src="../content/lessons_all.js"></script>', new_script)
    print("Replaced script src tag!")
else:
    pattern2 = r'<script>[\s\S]*?const ALL_LESSONS[\s\S]*?<\/script>'
    hoc = re.sub(pattern2, lambda m: new_script, hoc)
    print("Replaced ALL_LESSONS script using lambda replacer!")

with open('site/hoc.html', 'w', encoding='utf-8') as out:
    out.write(hoc)

print("Saved site/hoc.html successfully!")
