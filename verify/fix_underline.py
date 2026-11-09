import glob

files = glob.glob('content_csdl/*.js')
for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Replace \underline with \\underline when preceded by non-backslash
    import re
    # Replace single backslash before u with double backslash
    fixed = re.sub(r'(?<!\\)\\underline', r'\\\\underline', content)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(fixed)
    print(f"Fixed {fpath}")

# Regenerate lessons_all.js
import subprocess
subprocess.run(['python', 'verify/generate_csdl_lessons_all.py'], check=True)
print("Regenerated lessons_all.js")
