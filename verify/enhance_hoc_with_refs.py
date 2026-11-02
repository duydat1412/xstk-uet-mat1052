import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("site/hoc.html", "r", encoding="utf-8") as f:
    hoc = f.read()

# 1. ADD CSS STYLES FOR REFERENCE BOX
ref_css = """
/* Reference Box at Bottom of Lessons */
.lesson-ref-box {
  margin-top: 26px;
  background: var(--card);
  border: 1px solid var(--line);
  border-left: 4px solid var(--acc);
  border-radius: 12px;
  padding: 18px 20px;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.04);
  transition: all .2s ease;
}
.ref-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 12px;
  padding-bottom: 10px;
  border-bottom: 1px solid var(--line);
}
.ref-title {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: .92rem;
  font-weight: 800;
  color: var(--acc);
  text-transform: uppercase;
  letter-spacing: .5px;
}
.ref-pdf-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: var(--acc-soft);
  color: var(--acc);
  border: 1px solid rgba(37, 99, 235, 0.25);
  font-size: .82rem;
  font-weight: 700;
  padding: 6px 14px;
  border-radius: 8px;
  text-decoration: none;
  transition: all .15s ease;
}
.ref-pdf-btn:hover {
  background: var(--acc);
  color: #fff;
  transform: translateY(-1px);
}
.ref-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 10px;
  margin-bottom: 14px;
  font-size: .9rem;
}
.ref-item {
  display: flex;
  align-items: baseline;
  gap: 10px;
  flex-wrap: wrap;
  line-height: 1.5;
}
.ref-label {
  font-weight: 700;
  color: var(--mute);
  min-width: 155px;
  font-size: .85rem;
}
.ref-val {
  color: var(--text);
  flex: 1;
}
.ref-key-points {
  margin: 6px 0 0 18px;
  padding: 0;
  color: var(--text);
}
.ref-key-points li {
  margin-bottom: 4px;
  line-height: 1.45;
}
.ref-remind {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  background: rgba(245, 158, 11, 0.08);
  border: 1px solid rgba(245, 158, 11, 0.25);
  border-radius: 8px;
  padding: 11px 15px;
  font-size: .88rem;
  line-height: 1.55;
  color: var(--text);
}
.ref-remind-icon {
  font-size: 1.2rem;
  line-height: 1;
  flex-shrink: 0;
}
.theory-ref-pill {
  margin-top: 22px;
  padding: 12px 16px;
  background: var(--card);
  border: 1px dashed var(--line);
  border-left: 3px solid var(--acc);
  border-radius: 8px;
  font-size: .86rem;
  color: var(--mute);
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 10px;
}
.theory-ref-pill b {
  color: var(--text);
}
.mini-pdf-link {
  color: var(--acc);
  text-decoration: none;
  font-weight: 700;
  font-size: .82rem;
  padding: 3px 10px;
  border-radius: 6px;
  background: var(--acc-soft);
  border: 1px solid rgba(37, 99, 235, 0.2);
  white-space: nowrap;
}
.mini-pdf-link:hover {
  background: var(--acc);
  color: #fff;
}
"""

if ".lesson-ref-box" not in hoc:
    hoc = hoc.replace("</style>", ref_css + "\n</style>")
    print("Added Reference CSS styles!")
else:
    print("Reference CSS styles already present.")

# 2. ADD HTML CONTAINER <div id="lessonRefBox"></div>
ref_html = """    <!-- SUB TAB CONTENT CONTAINER -->
    <div id="tabContent"></div>

    <!-- DẤU REF TRA CỨU SLIDE BÀI GIẢNG -->
    <div id="lessonRefBox"></div>"""

if '<div id="lessonRefBox">' not in hoc:
    hoc = hoc.replace('<!-- SUB TAB CONTENT CONTAINER -->\n    <div id="tabContent"></div>', ref_html)
    print("Added #lessonRefBox HTML container!")
else:
    print("#lessonRefBox HTML container already present.")

# 3. UPDATE renderTheory to include theory-ref-pill
old_render_theory_end = """  if (l.widget === 'outlier_widget') {
    html += `<div class="widget-container" id="outlierWidget">"""

# Check if theory-ref-pill already added
if "theory-ref-pill" not in hoc:
    # Find return html; at end of renderTheory
    # Let's inspect the exact return html; in renderTheory
    theory_return_match = re.search(r'(function renderTheory\(l\)[\s\S]*?)(return html;\s*\n\})', hoc)
    if theory_return_match:
        pill_code = """  // Inline Reference Pill at the end of Theory
  if (l.ref) {
    html += `<div class="theory-ref-pill">
      <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;">
        <span>📌 <b>Tra cứu Slide bài giảng:</b> ${l.ref.slide_name} (<b>${l.ref.pages}</b>) — <i>${l.ref.section}</i></span>
      </div>
      <a href="/${l.ref.slide_file}#page=${l.ref.page_start}" target="_blank" class="mini-pdf-link" title="Mở trang ${l.ref.page_start} trong file ${l.ref.slide_file}">
        📄 Mở Slide PDF (${l.ref.slide_file}) ↗
      </a>
    </div>`;
  }

  return html;
}"""
        hoc = hoc[:theory_return_match.start(2)] + pill_code + hoc[theory_return_match.end(2):]
        print("Injected inline reference pill into renderTheory!")

# 4. ADD renderRefBox function and hook it into renderCurrentLesson
if "function renderRefBox(l)" not in hoc:
    ref_box_func = """
// RENDER REFERENCE BOX (TRA CỨU SLIDE BÀI GIẢNG)
function renderRefBox(l) {
  const box = document.getElementById('lessonRefBox');
  if (!box) return;
  const ref = l.ref;
  if (!ref) {
    box.innerHTML = '';
    return;
  }

  let keyPointsHtml = '';
  if (ref.key_points && ref.key_points.length) {
    keyPointsHtml = `<ul class="ref-key-points">
      ${ref.key_points.map(pt => `<li>${pt}</li>`).join('')}
    </ul>`;
  }

  box.innerHTML = `
    <div class="lesson-ref-box">
      <div class="ref-header">
        <div class="ref-title">
          <span class="ref-icon">📌</span>
          <span>DẤU REF TRA CỨU SLIDE BÀI GIẢNG & HỌC LIỆU (MAT1052)</span>
        </div>
        <a href="/${ref.slide_file}#page=${ref.page_start}" target="_blank" class="ref-pdf-btn" title="Mở trực tiếp file PDF slide tại trang ${ref.page_start}">
          📄 Mở Slide: ${ref.slide_file} (trang ${ref.page_start}) ↗
        </a>
      </div>
      <div class="ref-grid">
        <div class="ref-item">
          <span class="ref-label">📁 File Slide UET:</span>
          <span class="ref-val"><b>${ref.slide_name}</b> (<code>${ref.slide_file}</code>)</span>
        </div>
        <div class="ref-item">
          <span class="ref-label">📑 Vị trí trang & Mục:</span>
          <span class="ref-val"><b>${ref.pages}</b> — ${ref.section}</span>
        </div>
        <div class="ref-item">
          <span class="ref-label">📖 Giáo trình đối chiếu:</span>
          <span class="ref-val">${ref.stat20}</span>
        </div>
        ${keyPointsHtml ? `
        <div class="ref-item">
          <span class="ref-label">🎯 Trọng tâm kiến thức:</span>
          <span class="ref-val">${keyPointsHtml}</span>
        </div>` : ''}
      </div>
      <div class="ref-remind">
        <span class="ref-remind-icon">💡</span>
        <div><b>Chỉ dẫn tra cứu khi đọc chưa hiểu:</b> ${ref.remind}</div>
      </div>
    </div>
  `;
}
"""
    # Insert renderRefBox before renderCurrentLesson
    hoc = hoc.replace("// RENDER CURRENT LESSON", ref_box_func + "\n// RENDER CURRENT LESSON")
    print("Added renderRefBox function!")

# 5. Call renderRefBox(l) inside renderCurrentLesson()
if "renderRefBox(l);" not in hoc:
    hoc = hoc.replace("updateNavButtons();", "renderRefBox(l);\n  updateNavButtons();")
    print("Called renderRefBox(l) in renderCurrentLesson!")

# 6. Add KaTeX rendering to lessonRefBox if KaTeX present
if "renderMathInElement(container" in hoc and "renderMathInElement(document.getElementById('lessonRefBox')" not in hoc:
    katex_extra = """  const refBoxEl = document.getElementById('lessonRefBox');
  if (window.renderMathInElement && refBoxEl) {
    renderMathInElement(refBoxEl, {
      delimiters: [
        {left: '$$', right: '$$', display: true},
        {left: '$', right: '$', display: false}
      ],
      throwOnError: false
    });
  }"""
    hoc = hoc.replace("renderMathInElement(container, {", katex_extra + "\n    renderMathInElement(container, {")
    print("Added KaTeX render for lessonRefBox!")

with open("site/hoc.html", "w", encoding="utf-8") as f:
    f.write(hoc)

print("Saved site/hoc.html with full reference features!")
