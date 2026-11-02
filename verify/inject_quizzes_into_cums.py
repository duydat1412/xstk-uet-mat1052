import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

quizzes_data = json.load(open('content/quizzes_3levels.json', encoding='utf-8'))

for cluster in ['a', 'b', 'c', 'd', 'e']:
    fname = f'content/cum_{cluster}.js'
    text = open(fname, 'r', encoding='utf-8').read()
    
    # Check if quizzes already injected
    if 'quizzes:' in text:
        # Strip existing quizzes: [ ... ], if re-running
        text = re.sub(r'quizzes:\s*\[[\s\S]*?\]\s*,\s*(?=final_quiz:)', '', text)
        print(f"Stripped existing quizzes from {fname}")

    matches = list(re.finditer(r'\{\s*id:\s*"([A-E]\d)"', text))
    
    # Process from last to first so string indices don't shift
    for i in range(len(matches) - 1, -1, -1):
        m = matches[i]
        lid = m.group(1)
        lesson_start = m.start()
        lesson_end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        
        lesson_text = text[lesson_start:lesson_end]
        
        fq_match = re.search(r'final_quiz:\s*\{', lesson_text)
        assert fq_match is not None, f"Could not find final_quiz in lesson {lid}"
        
        fq_pos = lesson_start + fq_match.start()
        
        # Format quizzes json
        quizzes_json = json.dumps(quizzes_data[lid], ensure_ascii=False, indent=6)
        inject_str = f"quizzes: {quizzes_json},\n    "
        
        text = text[:fq_pos] + inject_str + text[fq_pos:]
        print(f"Injected 3-level quizzes for {lid}")

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(text)

print("All clusters updated with quizzes!")
