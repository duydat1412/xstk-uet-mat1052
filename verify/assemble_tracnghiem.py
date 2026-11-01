import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

def rotate_mcq(q, target_idx):
    old_opts = q['options']
    old_exp = q['explanation']
    
    if target_idx == 0:
        perm = [0, 1, 2, 3]
    elif target_idx == 1:
        perm = [1, 0, 2, 3]
    elif target_idx == 2:
        perm = [1, 2, 0, 3]
    elif target_idx == 3:
        perm = [1, 2, 3, 0]
    else:
        raise ValueError("target_idx must be 0, 1, 2, or 3")
        
    new_opts = [old_opts[i] for i in perm]
    new_correct_idx = target_idx
    
    letters = ['A', 'B', 'C', 'D']
    mapping = {
        'A': letters[perm.index(0)],
        'B': letters[perm.index(1)],
        'C': letters[perm.index(2)],
        'D': letters[perm.index(3)],
    }
    
    exp = old_exp
    exp = exp.replace('Đáp án đúng là A', '__LET_A__')
    exp = exp.replace('Phương án B, C, D:', '__PA_BCD__')
    exp = exp.replace('Phương án B, C:', '__PA_BC__')
    exp = exp.replace('Phương án C, D:', '__PA_CD__')
    exp = exp.replace('Phương án B:', '__PA_B__')
    exp = exp.replace('Phương án C:', '__PA_C__')
    exp = exp.replace('Phương án D:', '__PA_D__')
    
    exp = exp.replace('__LET_A__', f"Đáp án đúng là {mapping['A']}")
    exp = exp.replace('__PA_B__', f"Phương án {mapping['B']}:")
    exp = exp.replace('__PA_C__', f"Phương án {mapping['C']}:")
    exp = exp.replace('__PA_D__', f"Phương án {mapping['D']}:")
    
    pair_bc = sorted([mapping['B'], mapping['C']])
    exp = exp.replace('__PA_BC__', f"Phương án {pair_bc[0]}, {pair_bc[1]}:")
    
    pair_cd = sorted([mapping['C'], mapping['D']])
    exp = exp.replace('__PA_CD__', f"Phương án {pair_cd[0]}, {pair_cd[1]}:")
    
    triple = sorted([mapping['B'], mapping['C'], mapping['D']])
    exp = exp.replace('__PA_BCD__', f"Phương án {triple[0]}, {triple[1]}, {triple[2]}:")
    
    q_copy = dict(q)
    q_copy['options'] = new_opts
    q_copy['correctIndex'] = new_correct_idx
    q_copy['explanation'] = exp
    return q_copy

all_mcqs = []
counter = 0

for t in range(1, 8):
    path = f"content/mcq_topic_{t}.json"
    with open(path, 'r', encoding='utf-8') as f:
        topic_mcqs = json.load(f)
    print(f"Loaded Topic {t}: {len(topic_mcqs)} questions")
    for q in topic_mcqs:
        target_idx = counter % 4
        balanced_q = rotate_mcq(q, target_idx)
        all_mcqs.append(balanced_q)
        counter += 1

print(f"\nTotal assembled MCQs: {len(all_mcqs)}")

# Verification statistics
counts_by_topic = {}
counts_by_level = {}
counts_by_answer = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
letters = ['A', 'B', 'C', 'D']

for q in all_mcqs:
    # Check keys
    for k in ['id', 'topicId', 'topicName', 'level', 'question', 'options', 'correctIndex', 'explanation', 'source']:
        if k not in q:
            raise ValueError(f"Missing key {k} in {q['id']}")
    if len(q['options']) != 4:
        raise ValueError(f"Options count != 4 in {q['id']}")
    if q['correctIndex'] not in [0, 1, 2, 3]:
        raise ValueError(f"Invalid correctIndex in {q['id']}")
        
    counts_by_topic[q['topicId']] = counts_by_topic.get(q['topicId'], 0) + 1
    counts_by_level[q['level']] = counts_by_level.get(q['level'], 0) + 1
    counts_by_answer[letters[q['correctIndex']]] += 1

print("\n--- Summary by Topic ---")
for tid in sorted(counts_by_topic.keys()):
    print(f"Topic {tid}: {counts_by_topic[tid]} questions")

print("\n--- Summary by Level ---")
for lvl, count in counts_by_level.items():
    pct = count / len(all_mcqs) * 100
    print(f"{lvl}: {count} ({pct:.1f}%)")

print("\n--- Correct Answer Distribution ---")
for let, count in counts_by_answer.items():
    pct = count / len(all_mcqs) * 100
    print(f"Option {let}: {count} ({pct:.1f}%)")

# Save JSON
with open('content/tracnghiem_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_mcqs, f, ensure_ascii=False, indent=2)
print("\nSaved content/tracnghiem_data.json")

# Save JS bundle
with open('content/tracnghiem_data.js', 'w', encoding='utf-8') as f:
    f.write("/* Ngân hàng câu hỏi trắc nghiệm XSTK UET MAT1052 - Phase 4 */\n")
    f.write("window.TRAC_NGHIEM_DATA = ")
    json.dump(all_mcqs, f, ensure_ascii=False, indent=2)
    f.write(";\n")
print("Saved content/tracnghiem_data.js")
