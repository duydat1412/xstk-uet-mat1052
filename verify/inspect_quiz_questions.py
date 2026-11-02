import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("content/quizzes_3levels.json", "r", encoding="utf-8") as f:
    quizzes = json.load(f)

for lid, q_list in quizzes.items():
    print(f"=== {lid} ===")
    for q in q_list:
        print(f"  [{q['level']}] {q['q'][:90]}...")
