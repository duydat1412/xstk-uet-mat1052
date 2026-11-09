import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read base hoc.html
with open('site/hoc.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Read csdl lessons_all.js
with open('content_csdl/lessons_all.js', 'r', encoding='utf-8') as f:
    csdl_js = f.read()

# 1. Replace lessons-data script block
# Find <script id="lessons-data"> ... </script>
pattern = r'<script id="lessons-data">.*?</script>'
replacement = f'<script id="lessons-data">\n{csdl_js}\nconst ALL_LESSONS = ALL_CSDL_LESSONS;\n</script>'
html_csdl = re.sub(pattern, lambda m: replacement, html, flags=re.DOTALL)

# 2. Update Titles and Badges
html_csdl = html_csdl.replace(
    'Cổng Tự Học & Luyện Thi Xác Suất Thống Kê UET.MAT1052',
    'Cơ Sở Dữ Liệu Tương Tác UET.IS2099 — UET Study Hub'
)
html_csdl = html_csdl.replace(
    '<span class="badge-course">UET.MAT1052</span>',
    '<span class="badge-course" style="background:#fef3c7;color:#b45309;border-color:#f59e0b;">UET.IS2099</span>'
)
html_csdl = html_csdl.replace(
    '<span class="site-title">Xác Suất Thống Kê</span>',
    '<span class="site-title">Cơ Sở Dữ Liệu</span>'
)

# 3. Add Course Switcher into Header
course_switcher = """
      <div class="course-switcher" style="display:inline-flex;align-items:center;background:var(--card-subtle);border:1px solid var(--line);border-radius:var(--radius-sm);padding:2px;margin-right:12px;">
        <a href="/hoc" style="display:inline-flex;align-items:center;gap:4px;padding:4px 10px;font-size:0.8rem;font-weight:600;color:var(--mute);text-decoration:none;border-radius:6px;transition:all 0.15s ease;">
          🎲 XSTK
        </a>
        <a href="/csdl/hoc" style="display:inline-flex;align-items:center;gap:4px;padding:4px 10px;font-size:0.8rem;font-weight:700;color:#b45309;background:var(--card);text-decoration:none;border-radius:6px;box-shadow:var(--shadow-sm);">
          🗄️ CSDL
        </a>
      </div>
"""

# Insert switcher before .nav-links
html_csdl = html_csdl.replace('<nav class="nav-links">', course_switcher + '\n      <nav class="nav-links">')

# 4. Update Navigation Links in Header for CSDL
html_csdl = html_csdl.replace('href="/index.html"', 'href="/site/index.html"')
html_csdl = html_csdl.replace('href="/hoc"', 'href="/csdl/hoc"')
html_csdl = html_csdl.replace('href="/tracnghiem"', 'href="/tracnghiem?mon=csdl"')
html_csdl = html_csdl.replace('href="/tuluan"', 'href="/tuluan?mon=csdl"')
html_csdl = html_csdl.replace('href="/congthuc"', 'href="/congthuc?mon=csdl"')
html_csdl = html_csdl.replace('href="/dethi"', 'href="/dethi?mon=csdl"')

# 5. Change localStorage keys to isolate CSDL progress from XSTK
html_csdl = html_csdl.replace("'xstk_active_lesson'", "'csdl_active_lesson'")
html_csdl = html_csdl.replace("'xstk_completed_lessons'", "'csdl_completed_lessons'")
html_csdl = html_csdl.replace("'xstk_lesson_section'", "'csdl_lesson_section'")

# 6. Update cluster names for CSDL
# In renderSidebar or cluster mapping
cluster_map_code = """
const CLUSTER_NAMES = {
  "1": "Cụm 1: Tổng quan & Mô hình ER/EER",
  "2": "Cụm 2: Mô hình Quan hệ & Ánh xạ",
  "3": "Cụm 3: Đại số Quan hệ",
  "4": "Cụm 4: Phụ thuộc hàm & Chuẩn hóa"
};
"""
html_csdl = html_csdl.replace(
    'const CLUSTER_NAMES = {',
    cluster_map_code + '\nconst OLD_CLUSTER_NAMES = {'
)

# 7. Update PDF link handling in ref box
# If file is pptx, provide download / view link; if pdf, open directly
ref_link_patch = """
          const isPdf = ref.slide_file && ref.slide_file.endsWith('.pdf');
          const fileUrl = `/tailieu_csdl/${encodeURIComponent(ref.slide_file)}${isPdf ? `#page=${ref.page_start || 1}` : ''}`;
"""
html_csdl = re.sub(
    r'const fileUrl = `/${ref\.slide_file}#page=\$\{ref\.page_start\}`;',
    ref_link_patch,
    html_csdl
)

with open('site/csdl/hoc.html', 'w', encoding='utf-8') as f:
    f.write(html_csdl)

print("Created site/csdl/hoc.html successfully! Length:", len(html_csdl))
