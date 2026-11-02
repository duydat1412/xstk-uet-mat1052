import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("content/lesson_references.json", "r", encoding="utf-8") as f:
    refs = json.load(f)

cums = {
    "A": ["A1", "A2", "A3", "A4", "A5"],
    "B": ["B1", "B2", "B3", "B4", "B5"],
    "C": ["C1", "C2", "C3", "C4", "C5", "C6"],
    "D": ["D1", "D2", "D3", "D4"],
    "E": ["E1", "E2", "E3", "E4", "E5", "E6"]
}

for cluster, lids in cums.items():
    fname = f"content/cum_{cluster.lower()}.js"
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()

    for lid in lids:
        ref_obj = refs.get(lid)
        if not ref_obj:
            print(f"Warning: No ref for {lid}")
            continue

        ref_json_str = json.dumps(ref_obj, ensure_ascii=False, indent=6)
        # Format properly indented
        ref_field = f'ref: {ref_json_str},'

        # Match lesson block by id: "LID"
        # We can find `sources: "...",` inside this lesson
        # Search for: (id:\s*["\']{lid}["\'][\s\S]*?sources:\s*["\'].*?["\'],)
        pattern = re.compile(rf'(id:\s*["\']{lid}["\'][\s\S]*?sources:\s*["\'][^"\']+["\'],)')
        m = pattern.search(content)
        if m:
            matched_str = m.group(1)
            # Check if ref is already present in this block
            if "ref:" in matched_str:
                print(f"ref already exists in {lid}")
                continue
            replacement = matched_str + "\n    " + ref_field
            content = content[:m.start()] + replacement + content[m.end():]
            print(f"Injected ref into {lid} ({fname})")
        else:
            print(f"Could not find match for {lid} in {fname}")

    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)

print("Finished injecting references into cum files.")
