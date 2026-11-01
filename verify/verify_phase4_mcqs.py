import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

print("=== VERIFYING PHASE 4 MULTIPLE CHOICE BANK (161 MCQs) ===")

with open('content/tracnghiem_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total MCQs loaded: {len(data)}")

letters = ['A', 'B', 'C', 'D']
errors = []
ids = set()

for i, q in enumerate(data):
    qid = q.get('id')
    if not qid:
        errors.append(f"Item #{i} missing id")
        continue
    if qid in ids:
        errors.append(f"Duplicate id {qid}")
    ids.add(qid)
    
    # Check required fields
    for field in ['topicId', 'topicName', 'level', 'question', 'options', 'correctIndex', 'explanation', 'source']:
        if field not in q or q[field] is None or q[field] == "":
            errors.append(f"{qid}: Missing or empty field '{field}'")
            
    # Check options
    opts = q.get('options', [])
    if len(opts) != 4:
        errors.append(f"{qid}: options length is {len(opts)} != 4")
    for opt_idx, opt in enumerate(opts):
        if not opt or not isinstance(opt, str) or len(opt.strip()) == 0:
            errors.append(f"{qid}: Empty option at index {opt_idx}")
            
    # Check correctIndex
    c_idx = q.get('correctIndex')
    if c_idx not in [0, 1, 2, 3]:
        errors.append(f"{qid}: Invalid correctIndex {c_idx}")
    else:
        expected_letter = letters[c_idx]
        exp = q.get('explanation', '')
        if f"Đáp án đúng là {expected_letter}" not in exp and f"Đáp án đúng là: {expected_letter}" not in exp:
            errors.append(f"{qid}: Explanation mismatch! Expected 'Đáp án đúng là {expected_letter}' but explanation starts with: {exp[:50]}")
            
    # Check for unclosed $ in question and options
    def check_dollars(text, label):
        # Count non-escaped dollars
        # simple check: count of $ should be even
        # replace \$ with empty string
        t = text.replace(r'\$', '')
        count = t.count('$')
        if count % 2 != 0:
            errors.append(f"{qid}: Odd number of $ ({count}) in {label}: {text[:60]}")
            
    check_dollars(q.get('question', ''), 'question')
    for o_idx, o in enumerate(opts):
        check_dollars(o, f"option[{o_idx}]")

if errors:
    print(f"\n❌ FOUND {len(errors)} ERRORS:")
    for e in errors[:20]:
        print("  -", e)
    if len(errors) > 20:
        print(f"  ... and {len(errors) - 20} more errors")
    sys.exit(1)
else:
    print("\n✅ ALL 161 MCQs PASSED INTEGRITY & EXPLANATION ALIGNMENT CHECKS!")
    print(f"  - 100% unique IDs ({len(ids)} questions)")
    print(f"  - 100% 4 non-empty options per question")
    print(f"  - 100% explanations aligned with correctIndex [A, B, C, D]")
    print(f"  - 100% math LaTeX delimiters closed properly")
