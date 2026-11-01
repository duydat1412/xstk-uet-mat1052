import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

clusters = ['a', 'b', 'c', 'd', 'e']
content_all = "// ==========================================================================\n"
content_all += "// TOÀN BỘ 26 BÀI HỌC TỰ HỌC TƯƠNG TÁC (CỤM A, B, C, D, E)\n"
content_all += "// UET.MAT1052 — Xác suất Thống kê\n"
content_all += "// ==========================================================================\n\n"

for c in clusters:
    fname = f"content/cum_{c}.js"
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    # Strip the entire Node.js export block clean
    text = re.sub(r'if\s*\(\s*typeof\s+module[\s\S]*?\}\s*$', '', text, flags=re.MULTILINE)
    content_all += text.strip() + "\n\n"

content_all += """// ==========================================================================
// HỢP NHẤT TOÀN BỘ 26 BÀI HỌC
// ==========================================================================
const ALL_LESSONS = [
  ...CUM_A,
  ...CUM_B,
  ...CUM_C,
  ...CUM_D,
  ...CUM_E
];

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { ALL_LESSONS, CUM_A, CUM_B, CUM_C, CUM_D, CUM_E };
}
"""

with open("content/lessons_all.js", "w", encoding="utf-8") as out:
    out.write(content_all)

print(f"Generated clean content/lessons_all.js! Length: {len(content_all)} chars")
