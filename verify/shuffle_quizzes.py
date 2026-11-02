import json
import random
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Load raw 3-level quizzes
with open('content/quizzes_3levels.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Use fixed seed for reproducible deterministic shuffle
rng = random.Random(42)

ans_counts = {0: 0, 1: 0, 2: 0, 3: 0}

for lesson_id, questions in data.items():
    for q in questions:
        correct_opt = q['opts'][0]
        other_opts = q['opts'][1:]
        
        # Target position with balanced selection
        target_pos = min(ans_counts, key=lambda k: ans_counts[k] + rng.uniform(0, 0.5))
        ans_counts[target_pos] += 1
        
        # Shuffle other options
        rng.shuffle(other_opts)
        
        # Place correct option at target_pos
        new_opts = other_opts[:]
        new_opts.insert(target_pos, correct_opt)
        
        q['opts'] = new_opts
        q['ans'] = target_pos

# Save back
with open('content/quizzes_3levels.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Shuffle completed successfully!")
print("Answer distribution across all 78 questions:", ans_counts)
