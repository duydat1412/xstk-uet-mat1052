import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read site/index.html
with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Title and Header Brand
html = html.replace(
    '<title>Cổng Tự Học & Luyện Thi Xác Suất Thống Kê UET.MAT1052</title>',
    '<title>UET Study Hub — Nền tảng Tự học & Luyện thi Tương tác UET</title>'
)
html = html.replace(
    '<span class="badge-course">UET.MAT1052</span>',
    '<span class="badge-course" style="background:#dbeafe;color:#1e40af;font-weight:800;">UET STUDY HUB</span>'
)
html = html.replace(
    '<span class="site-title">Xác Suất Thống Kê</span>',
    '<span class="site-title">Cổng Ôn Thi Sinh Viên UET</span>'
)

# 2. Add Course Switcher into Header
switcher_hub = """
      <div class="course-switcher" style="display:inline-flex;align-items:center;background:var(--card-subtle);border:1px solid var(--line);border-radius:var(--radius-sm);padding:2px;margin-right:12px;">
        <a href="#mon-xstk" onclick="switchSubject('xstk')" id="tab-btn-xstk" style="display:inline-flex;align-items:center;gap:4px;padding:4px 10px;font-size:0.8rem;font-weight:700;color:var(--acc);background:var(--card);text-decoration:none;border-radius:6px;box-shadow:var(--shadow-sm);cursor:pointer;">
          🎲 XSTK
        </a>
        <a href="#mon-csdl" onclick="switchSubject('csdl')" id="tab-btn-csdl" style="display:inline-flex;align-items:center;gap:4px;padding:4px 10px;font-size:0.8rem;font-weight:600;color:var(--mute);text-decoration:none;border-radius:6px;transition:all 0.15s ease;cursor:pointer;">
          🗄️ CSDL
        </a>
      </div>
"""
if 'course-switcher' not in html:
    html = html.replace('<nav class="nav-links">', switcher_hub + '\n      <nav class="nav-links">')

# 3. Add Subject Selector Cards Section right before the modules
subject_selector_section = """
    <!-- Subject Selection Cards (UET Study Hub Core) -->
    <div style="margin-bottom: 36px;">
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
        <h2 style="font-size: 1.35rem; font-weight: 800; color: var(--ink);">📚 Chọn Môn Học Cần Ôn Tập</h2>
        <span style="font-size: 0.85rem; color: var(--mute);">Chuẩn format đề thi & bài giảng UET</span>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
        <!-- Card Môn 1: Xác suất Thống kê -->
        <div id="card-sub-xstk" onclick="switchSubject('xstk')" style="background: var(--card); border: 2px solid var(--acc); border-radius: var(--radius-lg); padding: 24px; cursor: pointer; transition: all 0.2s ease; box-shadow: var(--shadow-md); position: relative; overflow: hidden;">
          <div style="position: absolute; top: 14px; right: 16px;">
            <span style="background: var(--acc-soft); color: var(--acc); font-size: 0.75rem; font-weight: 800; padding: 4px 10px; border-radius: 20px;">MAT1052</span>
          </div>
          <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
            <div style="font-size: 2.2rem;">🎲</div>
            <div>
              <h3 style="font-size: 1.25rem; font-weight: 800; color: var(--ink);">Xác Suất Thống Kê</h3>
              <p style="font-size: 0.85rem; color: var(--mute);">Khoa Toán - Cơ - Tin học</p>
            </div>
          </div>
          <p style="font-size: 0.9rem; color: var(--mute); line-height: 1.5; margin-bottom: 16px;">
            Hệ thống 26 bài học chia nhỏ theo Section Stepper, 78 ví dụ slide UET, 161 câu trắc nghiệm thực chiến, 56 bài tự luận chuẩn barem và 4 đề thi thử giữa kỳ bấm giờ.
          </p>
          <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 18px;">
            <span style="background: var(--card-subtle); color: var(--ink); font-size: 0.78rem; font-weight: 600; padding: 4px 8px; border-radius: 6px;">26 Bài học</span>
            <span style="background: var(--card-subtle); color: var(--ink); font-size: 0.78rem; font-weight: 600; padding: 4px 8px; border-radius: 6px;">161 Trắc nghiệm</span>
            <span style="background: var(--card-subtle); color: var(--ink); font-size: 0.78rem; font-weight: 600; padding: 4px 8px; border-radius: 6px;">56 Tự luận</span>
            <span style="background: var(--card-subtle); color: var(--ink); font-size: 0.78rem; font-weight: 600; padding: 4px 8px; border-radius: 6px;">4 Đề thi thử</span>
          </div>
          <div style="display: flex; gap: 10px;">
            <a href="/hoc" style="flex: 1; text-align: center; background: var(--acc); color: white; padding: 8px 14px; border-radius: var(--radius-sm); font-size: 0.88rem; font-weight: 700; text-decoration: none; box-shadow: var(--shadow-sm);">Vào Học Ngay</a>
            <a href="/dethi" style="background: var(--card-subtle); color: var(--ink); padding: 8px 14px; border-radius: var(--radius-sm); font-size: 0.88rem; font-weight: 600; text-decoration: none; border: 1px solid var(--line);">Thi thử</a>
          </div>
        </div>

        <!-- Card Môn 2: Cơ sở Dữ liệu -->
        <div id="card-sub-csdl" onclick="switchSubject('csdl')" style="background: var(--card); border: 1px solid var(--line); border-radius: var(--radius-lg); padding: 24px; cursor: pointer; transition: all 0.2s ease; box-shadow: var(--shadow-sm); position: relative; overflow: hidden;">
          <div style="position: absolute; top: 14px; right: 16px;">
            <span style="background: #fef3c7; color: #b45309; font-size: 0.75rem; font-weight: 800; padding: 4px 10px; border-radius: 20px;">IS2099 / INT2207</span>
          </div>
          <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
            <div style="font-size: 2.2rem;">🗄️</div>
            <div>
              <h3 style="font-size: 1.25rem; font-weight: 800; color: var(--ink);">Cơ Sở Dữ Liệu</h3>
              <p style="font-size: 0.85rem; color: var(--mute);">Khoa Công nghệ Thông tin</p>
            </div>
          </div>
          <p style="font-size: 0.9rem; color: var(--mute); line-height: 1.5; margin-bottom: 16px;">
            Bám sát 380 slide bài giảng UET: Mô hình ER/EER, Ánh xạ sang Bảng, Đại số quan hệ (σ, π, ⨝, ÷, γ), Bao đóng X+, Tìm khóa tối thiểu và Chuẩn hóa 3NF/BCNF.
          </p>
          <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 18px;">
            <span style="background: var(--card-subtle); color: var(--ink); font-size: 0.78rem; font-weight: 600; padding: 4px 8px; border-radius: 6px;">14 Bài học</span>
            <span style="background: var(--card-subtle); color: var(--ink); font-size: 0.78rem; font-weight: 600; padding: 4px 8px; border-radius: 6px;">42 Ví dụ Slide</span>
            <span style="background: var(--card-subtle); color: var(--ink); font-size: 0.78rem; font-weight: 600; padding: 4px 8px; border-radius: 6px;">28 Bẫy đề thi</span>
            <span style="background: var(--card-subtle); color: var(--ink); font-size: 0.78rem; font-weight: 600; padding: 4px 8px; border-radius: 6px;">Quiz chặn 3 cấp</span>
          </div>
          <div style="display: flex; gap: 10px;">
            <a href="/csdl/hoc" style="flex: 1; text-align: center; background: #d97706; color: white; padding: 8px 14px; border-radius: var(--radius-sm); font-size: 0.88rem; font-weight: 700; text-decoration: none; box-shadow: var(--shadow-sm);">Vào Học CSDL</a>
            <a href="/csdl/hoc" style="background: var(--card-subtle); color: var(--ink); padding: 8px 14px; border-radius: var(--radius-sm); font-size: 0.88rem; font-weight: 600; text-decoration: none; border: 1px solid var(--line);">Đại số QH</a>
          </div>
        </div>
      </div>
    </div>
"""

# Insert Subject Selector right after Hero Section
html = re.sub(
    r'(</section>\s*<!-- 5 Core Modules -->)',
    lambda m: '</section>\n' + subject_selector_section + '\n    <!-- 5 Core Modules -->',
    html
)

# 4. Add JavaScript for Subject Switching
js_switcher = """
<script>
function switchSubject(subject) {
  const cardXstk = document.getElementById('card-sub-xstk');
  const cardCsdl = document.getElementById('card-sub-csdl');
  const btnXstk = document.getElementById('tab-btn-xstk');
  const btnCsdl = document.getElementById('tab-btn-csdl');
  
  if (subject === 'csdl') {
    if (cardCsdl) {
      cardCsdl.style.borderColor = '#d97706';
      cardCsdl.style.boxShadow = 'var(--shadow-md)';
    }
    if (cardXstk) {
      cardXstk.style.borderColor = 'var(--line)';
      cardXstk.style.boxShadow = 'var(--shadow-sm)';
    }
    if (btnCsdl) {
      btnCsdl.style.color = '#b45309';
      btnCsdl.style.background = 'var(--card)';
      btnCsdl.style.boxShadow = 'var(--shadow-sm)';
    }
    if (btnXstk) {
      btnXstk.style.color = 'var(--mute)';
      btnXstk.style.background = 'transparent';
      btnXstk.style.boxShadow = 'none';
    }
  } else {
    if (cardXstk) {
      cardXstk.style.borderColor = 'var(--acc)';
      cardXstk.style.boxShadow = 'var(--shadow-md)';
    }
    if (cardCsdl) {
      cardCsdl.style.borderColor = 'var(--line)';
      cardCsdl.style.boxShadow = 'var(--shadow-sm)';
    }
    if (btnXstk) {
      btnXstk.style.color = 'var(--acc)';
      btnXstk.style.background = 'var(--card)';
      btnXstk.style.boxShadow = 'var(--shadow-sm)';
    }
    if (btnCsdl) {
      btnCsdl.style.color = 'var(--mute)';
      btnCsdl.style.background = 'transparent';
      btnCsdl.style.boxShadow = 'none';
    }
  }
}

// Auto check URL query param or hash
window.addEventListener('DOMContentLoaded', () => {
  const params = new URLSearchParams(window.location.search);
  const mon = params.get('mon');
  if (mon === 'csdl' || window.location.hash === '#mon-csdl') {
    switchSubject('csdl');
  }
});
</script>
"""

html = html.replace('</body>', js_switcher + '\n</body>')

with open('site/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Upgraded site/index.html & index.html to UET Study Hub successfully!")
