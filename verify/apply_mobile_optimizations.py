"""
apply_mobile_optimizations.py
Tối ưu hóa toàn diện giao diện và kích thước cho Mobile across all 5 existing HTML files + index.html
Bao gồm:
- Đồng bộ thanh điều hướng 6 trang (thêm dethi.html)
- Tối ưu header: Logo + Theme ở hàng 1, thanh điều hướng cuộn ngang mượt mà (smooth swipe) ở hàng 2 trên mobile
- Ngăn chặn triệt để hiện tượng vỡ layout do công thức toán học KaTeX dài (.katex-display overflow-x: auto)
- Tối ưu bảng biểu (.table-responsive / table overflow-x: auto)
- Tối ưu kích thước nút bấm và lựa chọn trắc nghiệm chuẩn chạm tay Mobile (min-height >= 44px)
- Co giãn font chữ thông minh clamp(...) cho tiêu đề và nội dung trên màn hình nhỏ (< 768px, < 480px)
- Thêm Card Đề thi thử (Phase 5) vào site/index.html
"""

import os
import re
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE_DIR = os.path.join(ROOT_DIR, "site")

# 1. CẬP NHẬT SITE/INDEX.HTML
print("--- [1] Tối ưu hóa site/index.html ---")
index_path = os.path.join(SITE_DIR, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

# Thêm link dethi.html vào navbar nếu chưa có
if 'href="dethi.html"' not in index_html:
    nav_old = '<a href="congthuc.html" class="nav-btn">📐 Công thức</a>'
    nav_new = '<a href="congthuc.html" class="nav-btn">📐 Công thức</a>\n      <a href="dethi.html" class="nav-btn">📝 Đề thi thử</a>'
    index_html = index_html.replace(nav_old, nav_new)
    print("  + Đã thêm dethi.html vào navbar của index.html")

# Thêm Card Đề Thi Thử vào module-grid nếu chưa có
if 'dethi.html' not in index_html.split('<section class="modules">')[1].split('</section>')[0]:
    dethi_card = """
    <!-- Module 5: Đề Thi Thử -->
    <a href="dethi.html" class="module-card" style="border-top: 4px solid var(--purple);">
      <div class="module-icon" style="background: var(--purple-soft); color: var(--purple);">📝</div>
      <div class="module-title">4 Đề Thi Thử Giữa Kỳ Chuẩn UET</div>
      <div class="module-desc">Mô phỏng 100% đề thi thật 90 phút: 50% trắc nghiệm (20 câu) + 50% tự luận (2-3 bài lớn). Đồng hồ đếm giờ, tự động chấm điểm trắc nghiệm & barem tự luận phân rã từng 0,25đ.</div>
      <div class="module-footer">
        <span class="badge-mini" style="background: var(--purple-soft); color: var(--purple);">90 Phút • 4 Đề Thi</span>
        <span class="module-action">Vào thi thử →</span>
      </div>
    </a>
"""
    # Chèn trước thẻ đóng của module-grid
    idx_mg = index_html.find('</div>\n  </section>')
    if idx_mg != -1:
        index_html = index_html[:idx_mg] + dethi_card + index_html[idx_mg:]
        print("  + Đã thêm Module Card Đề Thi Thử vào index.html")

# Thêm stat 4 Đề thi vào hero-stats
if '4 Đề thi 90p' not in index_html:
    stat_pill = """
      <div class="stat-pill">
        <div class="stat-num">4</div>
        <div class="stat-label">Đề thi 90p</div>
      </div>"""
    idx_stats = index_html.find('</div>\n    </div>\n  </section>')
    if idx_stats != -1:
        index_html = index_html[:idx_stats] + stat_pill + index_html[idx_stats:]
        print("  + Đã thêm Stat Pill 4 Đề thi 90p vào index.html")

# Thêm Mobile Responsive CSS vào index.html
mobile_index_css = """
/* ========================================================
   RESPONSIVE CSS TỐI ƯU TOÀN DIỆN CHO MOBILE & TABLET
   ======================================================== */
.katex-display {
  overflow-x: auto;
  overflow-y: hidden;
  padding: 6px 0;
  -webkit-overflow-scrolling: touch;
}

@media (max-width: 900px) {
  .hero {
    padding: 30px 20px;
  }
  .module-grid {
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  }
}

@media (max-width: 768px) {
  .header-top {
    flex-direction: column !important;
    align-items: stretch !important;
    padding: 8px 12px !important;
    gap: 8px !important;
  }
  
  .logo-group {
    justify-content: space-between;
    width: 100%;
  }

  .nav-links {
    display: flex !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    white-space: nowrap !important;
    padding: 4px 0 !important;
    gap: 6px !important;
    scrollbar-width: none !important;
  }
  .nav-links::-webkit-scrollbar {
    display: none !important;
  }

  .nav-btn {
    font-size: 0.82rem !important;
    padding: 6px 10px !important;
    min-height: 36px !important;
    flex-shrink: 0 !important;
  }

  .container {
    padding: 12px 10px 40px !important;
  }

  .hero {
    padding: 24px 16px !important;
    margin-bottom: 24px !important;
  }

  .hero h1 {
    font-size: clamp(1.3rem, 5vw, 1.8rem) !important;
  }

  .hero-stats {
    display: grid !important;
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 8px !important;
  }

  .stat-pill {
    padding: 8px !important;
  }

  .stat-num {
    font-size: 1.3rem !important;
  }

  .module-grid {
    grid-template-columns: 1fr !important;
    gap: 14px !important;
  }

  .roadmap-nav {
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    white-space: nowrap !important;
    padding-bottom: 6px !important;
    scrollbar-width: none !important;
  }
  .roadmap-nav::-webkit-scrollbar {
    display: none !important;
  }

  .roadmap-tab {
    flex-shrink: 0 !important;
    padding: 8px 14px !important;
    font-size: 0.85rem !important;
  }

  .roadmap-box {
    padding: 16px 14px !important;
  }

  table {
    display: block !important;
    width: 100% !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
  }

  .pitfall-grid {
    grid-template-columns: 1fr !important;
    gap: 12px !important;
  }
}
"""

if 'RESPONSIVE CSS TỐI ƯU TOÀN DIỆN' not in index_html:
    index_html = index_html.replace('</style>', mobile_index_css + '\n</style>')
    print("  + Đã tích hợp Mobile Responsive CSS vào index.html")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)
print(f"  -> Lưu thành công site/index.html ({len(index_html)} bytes)")


# 2. CẬP NHẬT SITE/HOC.HTML
print("\n--- [2] Tối ưu hóa site/hoc.html ---")
hoc_path = os.path.join(SITE_DIR, "hoc.html")
with open(hoc_path, "r", encoding="utf-8") as f:
    hoc_html = f.read()

# Cập nhật navbar để đồng bộ tên và link dethi.html
hoc_html = re.sub(
    r'<a href="dethi\.html"[^>]*>.*?</a>',
    '<a href="dethi.html" class="nav-link">📝 Đề thi thử</a>',
    hoc_html
)

mobile_hoc_css = """
/* ========================================================
   RESPONSIVE CSS TỐI ƯU TOÀN DIỆN CHO MOBILE & TABLET
   ======================================================== */
.katex-display {
  overflow-x: auto;
  overflow-y: hidden;
  padding: 6px 0;
  -webkit-overflow-scrolling: touch;
}

@media (max-width: 768px) {
  .header-wrap {
    flex-direction: column !important;
    align-items: stretch !important;
    padding: 8px 12px !important;
    gap: 8px !important;
  }

  .brand-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
  }

  .nav-links {
    display: flex !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    white-space: nowrap !important;
    padding: 4px 0 !important;
    gap: 6px !important;
    scrollbar-width: none !important;
  }
  .nav-links::-webkit-scrollbar {
    display: none !important;
  }

  .nav-link {
    font-size: 0.82rem !important;
    padding: 6px 10px !important;
    min-height: 36px !important;
    flex-shrink: 0 !important;
  }

  main {
    padding: 12px 10px 40px !important;
  }

  .clusters-nav {
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    white-space: nowrap !important;
    padding-bottom: 6px !important;
    scrollbar-width: none !important;
    gap: 6px !important;
  }
  .clusters-nav::-webkit-scrollbar {
    display: none !important;
  }

  .cluster-btn {
    flex-shrink: 0 !important;
    padding: 7px 12px !important;
    font-size: 0.82rem !important;
  }

  .lessons-strip {
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    white-space: nowrap !important;
    padding-bottom: 6px !important;
    gap: 6px !important;
    scrollbar-width: none !important;
  }
  .lessons-strip::-webkit-scrollbar {
    display: none !important;
  }

  .lesson-pill {
    flex-shrink: 0 !important;
    padding: 6px 12px !important;
    font-size: 0.82rem !important;
  }

  .lesson-card {
    padding: 16px 14px !important;
    border-radius: 12px !important;
  }

  .lesson-card h1 {
    font-size: 1.3rem !important;
  }

  .pitfall-row {
    grid-template-columns: 1fr !important;
    gap: 10px !important;
  }

  .quiz-opt {
    padding: 12px 14px !important;
    min-height: 44px !important;
    font-size: 0.92rem !important;
  }
}
"""

if 'RESPONSIVE CSS TỐI ƯU TOÀN DIỆN' not in hoc_html:
    hoc_html = hoc_html.replace('</style>', mobile_hoc_css + '\n</style>')
    print("  + Đã tích hợp Mobile Responsive CSS vào hoc.html")

with open(hoc_path, "w", encoding="utf-8") as f:
    f.write(hoc_html)
print(f"  -> Lưu thành công site/hoc.html ({len(hoc_html)} bytes)")


# 3. CẬP NHẬT SITE/TULUAN.HTML
print("\n--- [3] Tối ưu hóa site/tuluan.html ---")
tuluan_path = os.path.join(SITE_DIR, "tuluan.html")
with open(tuluan_path, "r", encoding="utf-8") as f:
    tuluan_html = f.read()

# Cập nhật navbar
tuluan_html = re.sub(
    r'<a href="dethi\.html"[^>]*>.*?</a>',
    '<a href="dethi.html" class="nav-link">📝 Đề thi thử</a>',
    tuluan_html
)

mobile_tuluan_css = """
/* ========================================================
   RESPONSIVE CSS TỐI ƯU TOÀN DIỆN CHO MOBILE & TABLET
   ======================================================== */
.katex-display {
  overflow-x: auto;
  overflow-y: hidden;
  padding: 6px 0;
  -webkit-overflow-scrolling: touch;
}

@media (max-width: 768px) {
  .header-wrap {
    flex-direction: column !important;
    align-items: stretch !important;
    padding: 8px 12px !important;
    gap: 8px !important;
  }

  .nav-links {
    display: flex !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    white-space: nowrap !important;
    padding: 4px 0 !important;
    gap: 6px !important;
    scrollbar-width: none !important;
  }
  .nav-links::-webkit-scrollbar {
    display: none !important;
  }

  .nav-link {
    font-size: 0.82rem !important;
    padding: 6px 10px !important;
    min-height: 36px !important;
    flex-shrink: 0 !important;
  }

  main {
    padding: 12px 10px 40px !important;
  }

  .topics-nav {
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    white-space: nowrap !important;
    padding-bottom: 6px !important;
    gap: 6px !important;
    scrollbar-width: none !important;
  }
  .topics-nav::-webkit-scrollbar {
    display: none !important;
  }

  .topic-btn {
    flex-shrink: 0 !important;
    padding: 7px 12px !important;
    font-size: 0.82rem !important;
  }

  .exercise-card {
    padding: 16px 14px !important;
    border-radius: 12px !important;
  }

  .exercise-title {
    font-size: 1.1rem !important;
  }

  .step-box {
    padding: 12px 14px !important;
  }

  .casio-shortcut {
    font-size: 0.85rem !important;
    padding: 10px 12px !important;
  }

  table {
    display: block !important;
    width: 100% !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
  }
}
"""

if 'RESPONSIVE CSS TỐI ƯU TOÀN DIỆN' not in tuluan_html:
    tuluan_html = tuluan_html.replace('</style>', mobile_tuluan_css + '\n</style>')
    print("  + Đã tích hợp Mobile Responsive CSS vào tuluan.html")

with open(tuluan_path, "w", encoding="utf-8") as f:
    f.write(tuluan_html)
print(f"  -> Lưu thành công site/tuluan.html ({len(tuluan_html)} bytes)")


# 4. CẬP NHẬT SITE/TRACNGHIEM.HTML
print("\n--- [4] Tối ưu hóa site/tracnghiem.html ---")
tn_path = os.path.join(SITE_DIR, "tracnghiem.html")
with open(tn_path, "r", encoding="utf-8") as f:
    tn_html = f.read()

# Cập nhật navbar
tn_html = re.sub(
    r'<a href="dethi\.html"[^>]*>.*?</a>',
    '<a href="dethi.html" class="nav-link">📝 Đề thi thử</a>',
    tn_html
)

mobile_tn_css = """
/* ========================================================
   RESPONSIVE CSS TỐI ƯU TOÀN DIỆN CHO MOBILE & TABLET
   ======================================================== */
.katex-display {
  overflow-x: auto;
  overflow-y: hidden;
  padding: 6px 0;
  -webkit-overflow-scrolling: touch;
}

@media (max-width: 900px) {
  .quiz-layout {
    grid-template-columns: 1fr !important;
  }

  .sidebar-palette {
    position: static !important;
    order: -1 !important;
    margin-bottom: 12px !important;
  }
}

@media (max-width: 768px) {
  .header-wrap {
    flex-direction: column !important;
    align-items: stretch !important;
    padding: 8px 12px !important;
    gap: 8px !important;
  }

  .nav-links {
    display: flex !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    white-space: nowrap !important;
    padding: 4px 0 !important;
    gap: 6px !important;
    scrollbar-width: none !important;
  }
  .nav-links::-webkit-scrollbar {
    display: none !important;
  }

  .nav-link {
    font-size: 0.82rem !important;
    padding: 6px 10px !important;
    min-height: 36px !important;
    flex-shrink: 0 !important;
  }

  .container {
    padding: 12px 10px 40px !important;
  }

  .mode-tabs {
    overflow-x: auto !important;
    white-space: nowrap !important;
    -webkit-overflow-scrolling: touch !important;
    padding-bottom: 6px !important;
    scrollbar-width: none !important;
  }
  .mode-tabs::-webkit-scrollbar {
    display: none !important;
  }

  .mode-tab {
    flex-shrink: 0 !important;
    padding: 8px 12px !important;
    font-size: 0.85rem !important;
  }

  .q-card {
    padding: 16px 14px !important;
  }

  .q-text {
    font-size: 0.98rem !important;
  }

  .opt-btn {
    padding: 12px 14px !important;
    min-height: 48px !important;
    font-size: 0.92rem !important;
  }
}
"""

if 'RESPONSIVE CSS TỐI ƯU TOÀN DIỆN' not in tn_html:
    tn_html = tn_html.replace('</style>', mobile_tn_css + '\n</style>')
    print("  + Đã tích hợp Mobile Responsive CSS vào tracnghiem.html")

with open(tn_path, "w", encoding="utf-8") as f:
    f.write(tn_html)
print(f"  -> Lưu thành công site/tracnghiem.html ({len(tn_html)} bytes)")


# 5. CẬP NHẬT SITE/CONGTHUC.HTML
print("\n--- [5] Tối ưu hóa site/congthuc.html ---")
ct_path = os.path.join(SITE_DIR, "congthuc.html")
with open(ct_path, "r", encoding="utf-8") as f:
    ct_html = f.read()

# Cập nhật navbar
ct_html = re.sub(
    r'<a href="dethi\.html"[^>]*>.*?</a>',
    '<a href="dethi.html" class="nav-link">📝 Đề thi thử</a>',
    ct_html
)

mobile_ct_css = """
/* ========================================================
   RESPONSIVE CSS TỐI ƯU TOÀN DIỆN CHO MOBILE & TABLET
   ======================================================== */
.katex-display {
  overflow-x: auto;
  overflow-y: hidden;
  padding: 6px 0;
  -webkit-overflow-scrolling: touch;
}

@media (max-width: 900px) {
  .formulas-grid {
    grid-template-columns: repeat(auto-fill, minmax(min(100%, 320px), 1fr)) !important;
  }
}

@media (max-width: 768px) {
  .header-wrap {
    flex-direction: column !important;
    align-items: stretch !important;
    padding: 8px 12px !important;
    gap: 8px !important;
  }

  .nav-links {
    display: flex !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    white-space: nowrap !important;
    padding: 4px 0 !important;
    gap: 6px !important;
    scrollbar-width: none !important;
  }
  .nav-links::-webkit-scrollbar {
    display: none !important;
  }

  .nav-link {
    font-size: 0.82rem !important;
    padding: 6px 10px !important;
    min-height: 36px !important;
    flex-shrink: 0 !important;
  }

  .container {
    padding: 12px 10px 40px !important;
  }

  .filter-tabs {
    overflow-x: auto !important;
    white-space: nowrap !important;
    -webkit-overflow-scrolling: touch !important;
    padding-bottom: 6px !important;
    scrollbar-width: none !important;
  }
  .filter-tabs::-webkit-scrollbar {
    display: none !important;
  }

  .filter-btn {
    flex-shrink: 0 !important;
    padding: 7px 12px !important;
    font-size: 0.82rem !important;
  }

  .formulas-grid {
    grid-template-columns: 1fr !important;
    gap: 14px !important;
  }

  .formula-card {
    padding: 16px 14px !important;
  }

  .formula-math {
    padding: 12px 10px !important;
  }

  .modal-dialog {
    width: 95% !important;
    padding: 16px !important;
    max-height: 85vh !important;
  }

  table {
    display: block !important;
    width: 100% !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
  }
}
"""

if 'RESPONSIVE CSS TỐI ƯU TOÀN DIỆN' not in ct_html:
    ct_html = ct_html.replace('</style>', mobile_ct_css + '\n</style>')
    print("  + Đã tích hợp Mobile Responsive CSS vào congthuc.html")

with open(ct_path, "w", encoding="utf-8") as f:
    f.write(ct_html)
print(f"  -> Lưu thành công site/congthuc.html ({len(ct_html)} bytes)")

print("\n[HOÀN THÀNH] Đã tối ưu hóa giao diện và kích thước Mobile cho toàn bộ hệ thống!")
