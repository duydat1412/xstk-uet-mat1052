import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("verify"))

from gen_topic_1 import get_topic_1
from gen_topic_2 import get_topic_2
from gen_topic_3 import get_topic_3
from gen_topic_4 import get_topic_4
from gen_topic_5 import get_topic_5
from gen_topic_6 import get_topic_6
from gen_topic_7 import get_topic_7

topics = [
    {"id": 1, "name": "Thống kê mô tả, Bảng liên hợp & Hồi quy tuyến tính", "short": "Mô tả & Hồi quy"},
    {"id": 2, "name": "Lý thuyết xác suất, Xác suất có điều kiện & Bayes", "short": "Xác suất & Bayes"},
    {"id": 3, "name": "Biến ngẫu nhiên rời rạc, Bảng pmf, Hàm cdf & Kỳ vọng, Phương sai", "short": "pmf, cdf & E/Var"},
    {"id": 4, "name": "Các phân phối rời rạc: Nhị thức, Siêu bội & Poisson", "short": "Nhị thức, Siêu bội, Poisson"},
    {"id": 5, "name": "Tổng, Trung bình mẫu i.i.d. & Bất đẳng thức Chebyshev", "short": "Tổng, TB & Chebyshev"},
    {"id": 6, "name": "Biến liên tục, Phân phối Đều, Mũ & Phân phối Chuẩn N(μ, σ²)", "short": "Liên tục, Đều & Chuẩn"},
    {"id": 7, "name": "Định lý giới hạn trung tâm (CLT) & Bài toán kích thước mẫu", "short": "Định lý CLT"}
]

print("Assembling all 56 exercises...")
all_exercises = []
all_exercises.extend(get_topic_1())
all_exercises.extend(get_topic_2())
all_exercises.extend(get_topic_3())
all_exercises.extend(get_topic_4())
all_exercises.extend(get_topic_5())
all_exercises.extend(get_topic_6())
all_exercises.extend(get_topic_7())

print(f"Total exercises assembled: {len(all_exercises)}")

# Validation checks
required_keys = ["id", "topicId", "level", "title", "problem", "analysis", "hints", "steps", "pro_tips", "pitfalls"]
id_set = set()

topic_counts = {t["id"]: 0 for t in topics}

for ex in all_exercises:
    for k in required_keys:
        if k not in ex:
            raise ValueError(f"Exercise {ex.get('id', 'UNKNOWN')} is missing required key '{k}'")
    if ex["id"] in id_set:
        raise ValueError(f"Duplicate exercise ID: {ex['id']}")
    id_set.add(ex["id"])
    topic_counts[ex["topicId"]] += 1
    if not isinstance(ex["hints"], list) or len(ex["hints"]) < 2:
        raise ValueError(f"Exercise {ex['id']} needs at least 2 hints")
    if not isinstance(ex["steps"], list) or len(ex["steps"]) < 2:
        raise ValueError(f"Exercise {ex['id']} needs at least 2 steps")

print("Validation passed successfully!")
for tid, count in topic_counts.items():
    print(f"  Topic {tid} ({topics[tid-1]['short']}): {count} exercises")

# Write to content/tuluan_data.json
bundle = {
    "topics": topics,
    "exercises": all_exercises
}

with open("content/tuluan_data.json", "w", encoding="utf-8") as f:
    json.dump(bundle, f, ensure_ascii=False, indent=2)
print("Saved content/tuluan_data.json")

# Write to content/tuluan_data.js
js_code = f"""// NGÂN HÀNG 56 BÀI TẬP TỰ LUẬN CHUẨN BAREM ĐIỂM THI (PHASE 3)
// Môn: Xác suất và Thống kê (UET.MAT1052 / Stat20)
// Bao gồm 7 dạng bài x 8 bài/dạng = 56 bài tập đầy đủ 3 mức độ (Cơ bản, Trung bình, Nâng cao)

const TULUAN_DATA = {json.dumps(bundle, ensure_ascii=False, indent=2)};

if (typeof module !== 'undefined' && module.exports) {{
  module.exports = TULUAN_DATA;
}}
"""

with open("content/tuluan_data.js", "w", encoding="utf-8") as f:
    f.write(js_code)
print("Saved content/tuluan_data.js")
