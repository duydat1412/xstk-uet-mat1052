import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('content_csdl/cum_1.js', 'r', encoding='utf-8') as f:
    c1 = f.read()
with open('content_csdl/cum_2.js', 'r', encoding='utf-8') as f:
    c2 = f.read()
with open('content_csdl/cum_3.js', 'r', encoding='utf-8') as f:
    c3 = f.read()
with open('content_csdl/cum_4.js', 'r', encoding='utf-8') as f:
    c4 = f.read()

# Combine files
output = f"""// ==========================================================================
// TỔNG HỢP TOÀN BỘ 14 BÀI HỌC CƠ SỞ DỮ LIỆU UET.IS2099
// Được sinh tự động từ content_csdl/cum_1.js -> cum_4.js
// Tuân thủ 100% UET Interactive Course Pedagogy Standard (AGENTS.md)
// ==========================================================================

{c1}

{c2}

{c3}

{c4}

const ALL_CSDL_LESSONS = [
  ...CUM_1_CSDL,
  ...CUM_2_CSDL,
  ...CUM_3_CSDL,
  ...CUM_4_CSDL
];

if (typeof module !== 'undefined' && module.exports) {{
  module.exports = {{ ALL_CSDL_LESSONS }};
}}
"""

with open('content_csdl/lessons_all.js', 'w', encoding='utf-8') as f:
    f.write(output)

print("Created content_csdl/lessons_all.js successfully! Length:", len(output))
