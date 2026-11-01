import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("==================================================")
print("  KIỂM TRA TỔNG THỂ TOÀN BỘ PHASE 3 (TỰ LUẬN)      ")
print("==================================================")

# 1. Check data file presence
for p in ['content/tuluan_data.json', 'content/tuluan_data.js', 'site/tuluan.html']:
    if not os.path.exists(p):
        print(f"[FAIL] Missing {p}")
        sys.exit(1)
    print(f"[OK] File exists: {p} ({os.path.getsize(p):,} bytes)")

# 2. Check JSON data
with open('content/tuluan_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

topics = data['topics']
exercises = data['exercises']

print(f"\n[OK] Loaded {len(topics)} topics, {len(exercises)} exercises.")

if len(exercises) != 56:
    print(f"[FAIL] Expected 56 exercises, got {len(exercises)}")
    sys.exit(1)

# Check topic distribution and levels
by_topic = {}
by_level = {"Cơ bản": 0, "Trung bình": 0, "Nâng cao": 0}

for ex in exercises:
    t = ex['topicId']
    by_topic[t] = by_topic.get(t, 0) + 1
    lvl = ex['level']
    by_level[lvl] = by_level.get(lvl, 0) + 1

    # Check required fields
    for field in ['id', 'topicId', 'level', 'title', 'problem', 'analysis', 'hints', 'steps', 'pro_tips', 'pitfalls']:
        assert field in ex, f"Missing {field} in {ex['id']}"
        assert ex[field], f"Empty {field} in {ex['id']}"

    # Check hints & steps count
    assert len(ex['hints']) >= 2, f"Fewer than 2 hints in {ex['id']}"
    assert len(ex['steps']) >= 2, f"Fewer than 2 steps in {ex['id']}"

    # Check barem points in steps
    has_points = any('[+' in s for s in ex['steps'])
    assert has_points, f"No barem marking [+...đ] in {ex['id']}"

print("\n--- PHÂN PHỐI 7 DẠNG BÀI (MỖI DẠNG ĐÚNG 8 BÀI) ---")
for t in topics:
    cnt = by_topic[t['id']]
    print(f"  Dạng {t['id']}: {t['name']} -> {cnt} bài [OK]")
    assert cnt == 8, f"Topic {t['id']} does not have 8 exercises"

print("\n--- PHÂN PHỐI THEO 3 CẤP ĐỘ ---")
for lvl, cnt in by_level.items():
    print(f"  {lvl}: {cnt} bài")

print("\n==================================================")
print("  PHASE 3 HOÀN TOÀN ĐẠT CHUẨN 100%!               ")
print("==================================================")
