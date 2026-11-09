import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('content/lessons_all.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const ALL_LESSONS = (\[.*?\]);\s*(?:if \(typeof module|\Z)', text, re.DOTALL)
if m:
    data = json.loads(m.group(1))
    print(f"Total lessons: {len(data)}")
    total_steps = 0
    total_exs = 0
    total_traps = 0
    total_quiz = 0
    for l in data:
        steps = len(l.get('theory', {}).get('steps', []))
        exs = len(l.get('examples', []))
        q_len = len(l.get('quiz', {}).get('questions', []))
        traps = len(l.get('theory', {}).get('pitfalls', []))
        total_steps += steps
        total_exs += exs
        total_traps += traps
        total_quiz += q_len
        ref = l.get('ref', {})
        r_str = f"{ref.get('slide_file')} p.{ref.get('page_start')}-{ref.get('page_end')}" if ref else 'No ref'
        print(f"[{l['id']}] {l['title']} | Steps: {steps} | Exs: {exs} | Traps: {traps} | Quiz: {q_len} | Ref: {r_str}")
    print("---")
    print(f"SUMMARY: Steps={total_steps}, Examples={total_exs}, Traps={total_traps}, Quiz Questions={total_quiz}")
