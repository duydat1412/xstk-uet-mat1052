"""
build_dethi_html.py - Xây dựng trang site/dethi.html hoàn chỉnh, offline standalone,
tối ưu chuẩn Mobile & Desktop, tích hợp KaTeX và 4 bộ đề thi giữa kỳ UET.MAT1052.
"""

import os
import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE_DIR = os.path.join(ROOT_DIR, "site")
CONTENT_DIR = os.path.join(ROOT_DIR, "content")

# Đọc dữ liệu đề thi
with open(os.path.join(CONTENT_DIR, "dethi_data.json"), "r", encoding="utf-8") as f:
    dethi_data = json.load(f)

dethi_json_str = json.dumps(dethi_data, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="vi" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>Đề Thi Thử Giữa Kỳ Chuẩn UET.MAT1052 | Xác Suất Thống Kê</title>
  
  <!-- KaTeX CSS & JS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>

  <style>
    :root {{
      --bg: #f8fafc;
      --card: #ffffff;
      --card-subtle: #f1f5f9;
      --ink: #0f172a;
      --mute: #64748b;
      --line: #e2e8f0;
      --acc: #2563eb;
      --acc-hover: #1d4ed8;
      --acc-soft: #eff6ff;
      --ok: #10b981;
      --ok-soft: #ecfdf5;
      --bad: #ef4444;
      --bad-soft: #fef2f2;
      --warn: #f59e0b;
      --warn-soft: #fffbeb;
      --purple: #8b5cf6;
      --purple-soft: #f5f3ff;
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
      --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
    }}

    [data-theme="dark"] {{
      --bg: #0b0f19;
      --card: #151d30;
      --card-subtle: #1c2640;
      --ink: #f1f5f9;
      --mute: #94a3b8;
      --line: #263352;
      --acc: #60a5fa;
      --acc-hover: #3b82f6;
      --acc-soft: #172554;
      --ok: #34d399;
      --ok-soft: #064e3b;
      --bad: #f87171;
      --bad-soft: #450a0a;
      --warn: #fbbf24;
      --warn-soft: #451a03;
      --purple: #a78bfa;
      --purple-soft: #2e1065;
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.3);
      --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.4);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.5);
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background-color: var(--bg);
      color: var(--ink);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }}

    /* Global KaTeX Overflow Fix for Mobile */
    .katex-display {{
      overflow-x: auto;
      overflow-y: hidden;
      padding: 6px 0;
      -webkit-overflow-scrolling: touch;
      margin: 0.6em 0;
    }}

    /* Header & Navigation */
    header {{
      background: var(--card);
      border-bottom: 1px solid var(--line);
      position: sticky;
      top: 0;
      z-index: 50;
      box-shadow: var(--shadow-sm);
    }}

    .header-top {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 10px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .logo-group {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .badge-course {{
      background: var(--acc-soft);
      color: var(--acc);
      font-size: 0.8rem;
      font-weight: 700;
      padding: 4px 8px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--acc);
      letter-spacing: 0.5px;
    }}

    .site-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--ink);
    }}

    .nav-links {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .nav-btn {{
      padding: 7px 12px;
      border-radius: var(--radius-sm);
      color: var(--mute);
      text-decoration: none;
      font-size: 0.88rem;
      font-weight: 500;
      transition: all 0.15s ease;
      white-space: nowrap;
      min-height: 38px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
    }}

    .nav-btn:hover {{
      background: var(--card-subtle);
      color: var(--ink);
    }}

    .nav-btn.active {{
      background: var(--acc-soft);
      color: var(--acc);
      font-weight: 600;
    }}

    .btn-theme {{
      background: transparent;
      border: 1px solid var(--line);
      color: var(--ink);
      padding: 6px 10px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      font-size: 1rem;
      min-height: 38px;
      min-width: 38px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
    }}

    /* Main Container */
    .container {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 20px 16px 60px;
    }}

    /* Hero Banner */
    .hero-banner {{
      background: linear-gradient(135deg, var(--card) 0%, var(--card-subtle) 100%);
      border: 1px solid var(--line);
      border-radius: var(--radius-lg);
      padding: 20px 24px;
      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      box-shadow: var(--shadow-sm);
    }}

    .hero-text h1 {{
      font-size: clamp(1.3rem, 2.8vw, 1.8rem);
      font-weight: 800;
      color: var(--ink);
      margin-bottom: 4px;
    }}

    .hero-text p {{
      color: var(--mute);
      font-size: 0.95rem;
    }}

    .exam-tabs {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .exam-tab {{
      padding: 9px 16px;
      border-radius: var(--radius-md);
      border: 1px solid var(--line);
      background: var(--card);
      color: var(--mute);
      font-weight: 600;
      font-size: 0.9rem;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .exam-tab:hover {{
      border-color: var(--acc);
      color: var(--ink);
    }}

    .exam-tab.active {{
      background: var(--acc);
      color: #ffffff;
      border-color: var(--acc);
      box-shadow: 0 2px 8px rgba(37, 99, 235, 0.3);
    }}

    /* Two-column exam grid */
    .exam-layout {{
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 20px;
      align-items: start;
    }}

    /* Left Content (Questions) */
    .exam-main {{
      display: flex;
      flex-direction: column;
      gap: 24px;
    }}

    .section-header {{
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: var(--radius-md);
      padding: 16px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }}

    .section-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--ink);
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .section-badge {{
      background: var(--acc-soft);
      color: var(--acc);
      font-size: 0.8rem;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 20px;
    }}

    /* Question Cards */
    .q-card {{
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: var(--radius-lg);
      padding: 20px;
      box-shadow: var(--shadow-sm);
      transition: border-color 0.2s;
    }}

    .q-card:hover {{
      border-color: #cbd5e1;
    }}

    .q-meta {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      gap: 10px;
    }}

    .q-num {{
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--acc);
    }}

    .btn-flag {{
      background: transparent;
      border: 1px solid var(--line);
      color: var(--mute);
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      font-size: 0.8rem;
      font-weight: 500;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: all 0.15s;
    }}

    .btn-flag.flagged {{
      background: var(--warn-soft);
      border-color: var(--warn);
      color: #b45309;
      font-weight: 600;
    }}

    .q-text {{
      font-size: 1rem;
      font-weight: 500;
      margin-bottom: 16px;
      color: var(--ink);
    }}

    .options-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 10px;
    }}

    .opt-label {{
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 12px 16px;
      border: 1.5px solid var(--line);
      border-radius: var(--radius-md);
      cursor: pointer;
      transition: all 0.15s ease;
      background: var(--card);
      user-select: none;
      min-height: 48px;
    }}

    .opt-label:hover {{
      border-color: var(--acc);
      background: var(--card-subtle);
    }}

    .opt-label.selected {{
      border-color: var(--acc);
      background: var(--acc-soft);
      color: var(--acc);
      font-weight: 600;
    }}

    .opt-label.correct {{
      border-color: var(--ok) !important;
      background: var(--ok-soft) !important;
      color: #065f46 !important;
      font-weight: 600;
    }}

    .opt-label.wrong {{
      border-color: var(--bad) !important;
      background: var(--bad-soft) !important;
      color: #991b1b !important;
    }}

    .opt-letter {{
      width: 28px;
      height: 28px;
      border-radius: 50%;
      border: 1.5px solid currentColor;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 0.85rem;
      font-weight: 700;
      flex-shrink: 0;
    }}

    .opt-text {{
      flex: 1;
    }}

    /* Explanation box */
    .explain-box {{
      margin-top: 14px;
      padding: 14px 16px;
      border-radius: var(--radius-md);
      background: var(--card-subtle);
      border-left: 4px solid var(--acc);
      font-size: 0.92rem;
      display: none;
    }}

    .explain-box.show {{
      display: block;
    }}

    /* Free-response Problem Card */
    .essay-card {{
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: var(--radius-lg);
      padding: 24px;
      box-shadow: var(--shadow-sm);
    }}

    .essay-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--ink);
      margin-bottom: 12px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--line);
    }}

    .essay-problem {{
      font-size: 0.98rem;
      margin-bottom: 20px;
      background: var(--card-subtle);
      padding: 16px;
      border-radius: var(--radius-md);
      border-left: 4px solid var(--purple);
    }}

    .part-box {{
      margin-top: 18px;
      padding: 16px;
      border: 1px solid var(--line);
      border-radius: var(--radius-md);
      background: var(--card);
    }}

    .part-head {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 10px;
    }}

    .part-name {{
      font-weight: 700;
      color: var(--ink);
      font-size: 0.95rem;
    }}

    .part-score-badge {{
      background: var(--purple-soft);
      color: var(--purple);
      font-weight: 700;
      font-size: 0.8rem;
      padding: 3px 8px;
      border-radius: var(--radius-sm);
    }}

    .barem-toggle {{
      background: transparent;
      border: 1px solid var(--line);
      color: var(--acc);
      padding: 5px 12px;
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      margin-top: 8px;
      transition: all 0.15s;
    }}

    .barem-toggle:hover {{
      background: var(--acc-soft);
    }}

    .barem-content {{
      margin-top: 12px;
      padding: 14px;
      background: var(--card-subtle);
      border-radius: var(--radius-md);
      font-size: 0.92rem;
      display: none;
    }}

    .barem-content.show {{
      display: block;
    }}

    .self-grading-group {{
      margin-top: 12px;
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
      background: var(--card);
      padding: 10px 14px;
      border-radius: var(--radius-sm);
      border: 1px dashed var(--line);
    }}

    .self-grading-group span {{
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--mute);
    }}

    .score-btn {{
      padding: 4px 10px;
      border: 1px solid var(--line);
      border-radius: var(--radius-sm);
      background: var(--card);
      color: var(--ink);
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s;
    }}

    .score-btn:hover {{
      border-color: var(--acc);
    }}

    .score-btn.active {{
      background: var(--acc);
      color: #fff;
      border-color: var(--acc);
    }}

    /* Right Sticky Sidebar (Timer & Palette) */
    .exam-sidebar {{
      position: sticky;
      top: 75px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .timer-card {{
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: var(--radius-lg);
      padding: 20px;
      text-align: center;
      box-shadow: var(--shadow-sm);
    }}

    .timer-title {{
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--mute);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 6px;
    }}

    .timer-display {{
      font-size: 2.2rem;
      font-weight: 800;
      font-variant-numeric: tabular-nums;
      color: var(--ink);
      margin-bottom: 12px;
    }}

    .timer-display.warning {{
      color: var(--warn);
      animation: pulse 1s infinite alternate;
    }}

    .timer-display.danger {{
      color: var(--bad);
      animation: pulse 0.5s infinite alternate;
    }}

    @keyframes pulse {{
      from {{ transform: scale(1); }}
      to {{ transform: scale(1.05); }}
    }}

    .timer-controls {{
      display: flex;
      gap: 8px;
    }}

    .btn-action {{
      flex: 1;
      padding: 10px 14px;
      border-radius: var(--radius-md);
      font-weight: 600;
      font-size: 0.9rem;
      cursor: pointer;
      border: none;
      transition: all 0.2s;
      min-height: 42px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }}

    .btn-pause {{
      background: var(--card-subtle);
      border: 1px solid var(--line);
      color: var(--ink);
    }}

    .btn-pause:hover {{
      background: var(--line);
    }}

    .btn-submit {{
      background: var(--ok);
      color: #ffffff;
    }}

    .btn-submit:hover {{
      background: #059669;
      box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
    }}

    /* Question Palette */
    .palette-card {{
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: var(--radius-lg);
      padding: 18px;
      box-shadow: var(--shadow-sm);
    }}

    .palette-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      font-size: 0.9rem;
      font-weight: 700;
    }}

    .palette-grid {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 6px;
    }}

    .palette-btn {{
      aspect-ratio: 1;
      border: 1.5px solid var(--line);
      border-radius: var(--radius-sm);
      background: var(--card);
      color: var(--mute);
      font-weight: 700;
      font-size: 0.85rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      transition: all 0.15s;
    }}

    .palette-btn:hover {{
      border-color: var(--acc);
      color: var(--ink);
    }}

    .palette-btn.answered {{
      background: var(--acc-soft);
      border-color: var(--acc);
      color: var(--acc);
    }}

    .palette-btn.flagged::after {{
      content: "🚩";
      position: absolute;
      top: -4px;
      right: -4px;
      font-size: 0.65rem;
    }}

    .palette-btn.correct {{
      background: var(--ok-soft) !important;
      border-color: var(--ok) !important;
      color: var(--ok) !important;
    }}

    .palette-btn.wrong {{
      background: var(--bad-soft) !important;
      border-color: var(--bad) !important;
      color: var(--bad) !important;
    }}

    /* Score Report Modal */
    .modal-backdrop {{
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.7);
      backdrop-filter: blur(4px);
      z-index: 100;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 16px;
    }}

    .modal-backdrop.show {{
      display: flex;
    }}

    .modal-card {{
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: var(--radius-lg);
      max-width: 650px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      padding: 28px;
      box-shadow: var(--shadow-lg);
      position: relative;
    }}

    .modal-title {{
      font-size: 1.4rem;
      font-weight: 800;
      text-align: center;
      margin-bottom: 16px;
    }}

    .score-breakdown {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      margin: 20px 0;
      text-align: center;
    }}

    .score-box {{
      padding: 16px 10px;
      border-radius: var(--radius-md);
      background: var(--card-subtle);
      border: 1px solid var(--line);
    }}

    .score-box.total {{
      background: var(--acc-soft);
      border-color: var(--acc);
    }}

    .score-label {{
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--mute);
      margin-bottom: 4px;
    }}

    .score-val {{
      font-size: 1.6rem;
      font-weight: 800;
      color: var(--ink);
    }}

    .score-box.total .score-val {{
      color: var(--acc);
    }}

    .review-advice {{
      background: var(--card-subtle);
      padding: 16px;
      border-radius: var(--radius-md);
      margin-bottom: 20px;
      font-size: 0.95rem;
      border-left: 4px solid var(--warn);
    }}

    .modal-actions {{
      display: flex;
      gap: 12px;
      justify-content: center;
    }}

    /* =======================================================
       RESPONSIVE CSS TỐI ƯU TOÀN DIỆN CHO MOBILE & TABLET
       ======================================================= */
    @media (max-width: 900px) {{
      .exam-layout {{
        grid-template-columns: 1fr;
      }}

      .exam-sidebar {{
        position: static;
        order: -1;
        margin-bottom: 10px;
      }}

      .timer-card {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 16px;
      }}

      .timer-display {{
        font-size: 1.6rem;
        margin-bottom: 0;
      }}

      .timer-controls {{
        flex: 0 0 auto;
      }}

      .palette-card {{
        display: none; /* Mặc định ẩn palette trên mobile để tiết kiệm diện tích */
      }}

      .palette-card.mobile-show {{
        display: block;
      }}
    }}

    @media (max-width: 768px) {{
      .header-top {{
        flex-direction: column;
        align-items: stretch;
        padding: 8px 12px;
        gap: 8px;
      }}

      .header-row-1 {{
        display: flex;
        justify-content: space-between;
        align-items: center;
      }}

      .nav-links {{
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        white-space: nowrap;
        padding: 4px 0;
        scrollbar-width: none;
      }}

      .nav-links::-webkit-scrollbar {{
        display: none;
      }}

      .nav-btn {{
        font-size: 0.82rem;
        padding: 6px 10px;
        min-height: 36px;
      }}

      .container {{
        padding: 12px 10px 40px;
      }}

      .hero-banner {{
        padding: 14px 16px;
        margin-bottom: 14px;
      }}

      .hero-text h1 {{
        font-size: 1.25rem;
      }}

      .exam-tab {{
        font-size: 0.82rem;
        padding: 7px 12px;
      }}

      .q-card, .essay-card {{
        padding: 16px 14px;
        border-radius: var(--radius-md);
      }}

      .opt-label {{
        padding: 10px 12px;
        min-height: 44px;
        font-size: 0.92rem;
      }}

      .score-breakdown {{
        grid-template-columns: 1fr;
        gap: 8px;
      }}
    }}
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <div class="header-top">
      <div class="header-row-1">
        <div class="logo-group">
          <span class="badge-course">UET.MAT1052</span>
          <span class="site-title">Xác suất Thống kê Giữa kỳ</span>
        </div>
        <button class="btn-theme" id="themeBtn" title="Chuyển chế độ sáng/tối">
          <span id="themeIcon">🌙</span>
        </button>
      </div>
      <nav class="nav-links">
        <a href="index.html" class="nav-btn">🏠 Tổng quan</a>
        <a href="hoc.html" class="nav-btn">📘 Lý thuyết</a>
        <a href="tuluan.html" class="nav-btn">✍️ Tự luận</a>
        <a href="tracnghiem.html" class="nav-btn">⚡ Trắc nghiệm</a>
        <a href="congthuc.html" class="nav-btn">📐 Công thức</a>
        <a href="dethi.html" class="nav-btn active">📝 Đề thi thử</a>
      </nav>
    </div>
  </header>

  <div class="container">
    
    <!-- Hero Banner with Exam Selector Tabs -->
    <section class="hero-banner">
      <div class="hero-text">
        <h1 id="examTitle">Đề Thi Thử Giữa Kỳ</h1>
        <p id="examDesc">Cấu trúc 50% trắc nghiệm (20 câu) + 50% tự luận (2-3 bài lớn). Thời gian: 90 phút.</p>
      </div>
      <div class="exam-tabs" id="examTabsContainer">
        <!-- Rendered by JS -->
      </div>
    </section>

    <!-- Exam Layout -->
    <div class="exam-layout">
      
      <!-- Main Content (Questions) -->
      <main class="exam-main">
        
        <!-- Section 1: Multiple Choice (5.0đ) -->
        <div class="section-header">
          <div class="section-title">
            <span>🎯 PHẦN I: TRẮC NGHIỆM KHÁCH QUAN</span>
            <span class="section-badge">5,0 Điểm (20 câu)</span>
          </div>
          <span style="font-size: 0.85rem; color: var(--mute);">Mỗi câu đúng đạt +0,25đ</span>
        </div>

        <div id="mcqContainer" style="display: flex; flex-direction: column; gap: 16px;">
          <!-- MCQs rendered here -->
        </div>

        <!-- Section 2: Free Response (5.0đ) -->
        <div class="section-header" style="margin-top: 10px;">
          <div class="section-title">
            <span>✍️ PHẦN II: TỰ LUẬN GIẢI TÍCH</span>
            <span class="section-badge" style="background: var(--purple-soft); color: var(--purple);">5,0 Điểm</span>
          </div>
          <span style="font-size: 0.85rem; color: var(--mute);">Barem điểm chi tiết từng 0,25đ</span>
        </div>

        <div id="essayContainer" style="display: flex; flex-direction: column; gap: 20px;">
          <!-- Essay problems rendered here -->
        </div>

      </main>

      <!-- Sticky Sidebar (Timer & Palette) -->
      <aside class="exam-sidebar">
        
        <!-- Timer Card -->
        <div class="timer-card">
          <div class="timer-title">⏱️ Thời gian còn lại</div>
          <div class="timer-display" id="timerDisplay">90:00</div>
          <div class="timer-controls">
            <button class="btn-action btn-pause" id="btnPause">⏸️ Tạm dừng</button>
            <button class="btn-action btn-submit" id="btnSubmit">📤 Nộp bài</button>
          </div>
        </div>

        <!-- Palette Card -->
        <div class="palette-card">
          <div class="palette-header">
            <span>Danh sách câu hỏi</span>
            <span id="answeredCountBadge" style="color: var(--acc);">0/20</span>
          </div>
          <div class="palette-grid" id="paletteGrid">
            <!-- 20 question buttons -->
          </div>
        </div>

      </aside>

    </div>

  </div>

  <!-- Score Breakdown Modal -->
  <div class="modal-backdrop" id="scoreModal">
    <div class="modal-card">
      <div class="modal-title">🎉 KẾT QUẢ BÀI THI GIỮA KỲ</div>
      
      <div class="score-breakdown">
        <div class="score-box">
          <div class="score-label">Trắc nghiệm (/5.0đ)</div>
          <div class="score-val" id="resMcqScore">0.0</div>
        </div>
        <div class="score-box">
          <div class="score-label">Tự luận (/5.0đ)</div>
          <div class="score-val" id="resEssayScore">0.0</div>
        </div>
        <div class="score-box total">
          <div class="score-label">TỔNG ĐIỂM (/10.0đ)</div>
          <div class="score-val" id="resTotalScore">0.0</div>
        </div>
      </div>

      <div class="review-advice" id="resAdvice">
        Đang phân tích kết quả bài làm...
      </div>

      <div class="modal-actions">
        <button class="btn-action btn-pause" id="btnCloseModal">Xem lại bài & Lời giải</button>
        <button class="btn-action btn-submit" id="btnRetryExam">Làm lại đề này</button>
      </div>
    </div>
  </div>

  <!-- Embedded Data & Interactive Logic -->
  <script>
    const DETHI_DATA = {dethi_json_str};

    // State
    let currentExamIndex = 0;
    let userAnswers = {{}}; // {{ qId: selectedOptionIndex }}
    let flaggedQuestions = new Set();
    let essayScores = {{}}; // {{ partKey: scoreVal }}
    let timeRemaining = 90 * 60; // 90 mins in seconds
    let timerInterval = null;
    let isPaused = false;
    let isSubmitted = false;

    // DOM Elements
    const examTabsContainer = document.getElementById("examTabsContainer");
    const examTitle = document.getElementById("examTitle");
    const examDesc = document.getElementById("examDesc");
    const mcqContainer = document.getElementById("mcqContainer");
    const essayContainer = document.getElementById("essayContainer");
    const paletteGrid = document.getElementById("paletteGrid");
    const answeredCountBadge = document.getElementById("answeredCountBadge");
    const timerDisplay = document.getElementById("timerDisplay");
    const btnPause = document.getElementById("btnPause");
    const btnSubmit = document.getElementById("btnSubmit");
    const scoreModal = document.getElementById("scoreModal");
    const btnCloseModal = document.getElementById("btnCloseModal");
    const btnRetryExam = document.getElementById("btnRetryExam");

    // Theme Management
    const themeBtn = document.getElementById("themeBtn");
    const themeIcon = document.getElementById("themeIcon");

    function initTheme() {{
      const saved = localStorage.getItem("xstk_theme") || "light";
      document.documentElement.setAttribute("data-theme", saved);
      themeIcon.textContent = saved === "dark" ? "☀️" : "🌙";
    }}

    themeBtn.addEventListener("click", () => {{
      const current = document.documentElement.getAttribute("data-theme");
      const next = current === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      localStorage.setItem("xstk_theme", next);
      themeIcon.textContent = next === "dark" ? "☀️" : "🌙";
    }});

    // Render Exam Tabs
    function renderTabs() {{
      examTabsContainer.innerHTML = "";
      DETHI_DATA.forEach((exam, idx) => {{
        const btn = document.createElement("button");
        btn.className = `exam-tab ${{idx === currentExamIndex ? "active" : ""}}`;
        btn.textContent = `Đề ${{exam.code}}`;
        btn.onclick = () => switchExam(idx);
        examTabsContainer.appendChild(btn);
      }});
    }}

    function switchExam(idx) {{
      if (isSubmitted || confirm("Chuyển đề thi sẽ thiết lập lại tiến độ của đề hiện tại. Bạn có chắc chắn muốn chuyển?")) {{
        currentExamIndex = idx;
        resetExam();
        renderTabs();
        loadExam();
      }}
    }}

    function resetExam() {{
      userAnswers = {{}};
      flaggedQuestions.clear();
      essayScores = {{}};
      timeRemaining = 90 * 60;
      isPaused = false;
      isSubmitted = false;
      btnPause.textContent = "⏸️ Tạm dừng";
      clearInterval(timerInterval);
      startTimer();
    }}

    // Load & Render Current Exam
    function loadExam() {{
      const exam = DETHI_DATA[currentExamIndex];
      examTitle.textContent = exam.title;
      examDesc.innerHTML = `${{exam.description}} (Mã đề: <b>${{exam.code}}</b>)`;

      // 1. Render MCQs
      mcqContainer.innerHTML = "";
      exam.mcqs.forEach((q, idx) => {{
        const card = document.createElement("div");
        card.className = "q-card";
        card.id = `q_card_${{idx}}`;

        const isFlagged = flaggedQuestions.has(q.id);
        const selectedOpt = userAnswers[q.id];

        let optionsHtml = q.options.map((opt, optIdx) => {{
          const letters = ["A", "B", "C", "D"];
          let optClass = "opt-label";
          if (selectedOpt === optIdx) optClass += " selected";
          if (isSubmitted) {{
            if (optIdx === q.correctIndex) optClass += " correct";
            else if (selectedOpt === optIdx) optClass += " wrong";
          }}
          return `
            <div class="${{optClass}}" onclick="selectOption('${{q.id}}', ${{optIdx}}, ${{idx}})">
              <span class="opt-letter">${{letters[optIdx]}}</span>
              <span class="opt-text">${{opt}}</span>
            </div>
          `;
        }}).join("");

        card.innerHTML = `
          <div class="q-meta">
            <span class="q-num">Câu ${{idx + 1}} (0,25đ)</span>
            <button class="btn-flag ${{isFlagged ? "flagged" : ""}}" onclick="toggleFlag('${{q.id}}', ${{idx}})">
              ${{isFlagged ? "🚩 Đã cắm cờ" : "🏳️ Cắm cờ"}}
            </button>
          </div>
          <div class="q-text">${{q.question}}</div>
          <div class="options-grid">
            ${{optionsHtml}}
          </div>
          <div class="explain-box ${{isSubmitted ? "show" : ""}}" id="explain_${{idx}}">
            <b>💡 Giải thích chi tiết:</b><br>${{q.explanation}}
          </div>
        `;
        mcqContainer.appendChild(card);
      }});

      // 2. Render Free-Response
      essayContainer.innerHTML = "";
      exam.essays.forEach((essay, eIdx) => {{
        const card = document.createElement("div");
        card.className = "essay-card";
        
        let partsHtml = essay.parts.map((p, pIdx) => {{
          const partKey = `${{essay.id}}_p${{pIdx}}`;
          const currentScore = essayScores[partKey] || 0;
          return `
            <div class="part-box">
              <div class="part-head">
                <span class="part-name">${{p.part}}</span>
                <span class="part-score-badge">+${{p.score}} điểm</span>
              </div>
              
              <button class="barem-toggle" onclick="toggleBarem('${{partKey}}')">
                📋 Xem Barem Điểm & Lời Giải Chi Tiết
              </button>

              <div class="barem-content" id="barem_${{partKey}}">
                <div style="color: var(--acc); font-weight: 600; margin-bottom: 6px;">📐 Barem chấm điểm:</div>
                <div style="margin-bottom: 10px;">${{p.barem}}</div>
                <div style="color: var(--ok); font-weight: 600; margin-bottom: 6px;">✍️ Lời giải chi tiết:</div>
                <div>${{p.solution}}</div>
              </div>

              <div class="self-grading-group">
                <span>Tự chấm điểm cho ý này:</span>
                <button class="score-btn ${{currentScore === 0 ? "active" : ""}}" onclick="setSelfScore('${{partKey}}', 0)">0đ</button>
                <button class="score-btn ${{currentScore === p.score * 0.5 ? "active" : ""}}" onclick="setSelfScore('${{partKey}}', ${{p.score * 0.5}})">${{p.score * 0.5}}đ (50%)</button>
                <button class="score-btn ${{currentScore === p.score ? "active" : ""}}" onclick="setSelfScore('${{partKey}}', ${{p.score}})">${{p.score}}đ (Đúng hết)</button>
              </div>
            </div>
          `;
        }}).join("");

        card.innerHTML = `
          <div class="essay-title">${{essay.title}}</div>
          <div class="essay-problem">${{essay.problem}}</div>
          ${{partsHtml}}
        `;
        essayContainer.appendChild(card);
      }});

      // 3. Render Question Palette
      renderPalette();
      
      // Render Math
      if (window.renderMathInElement) {{
        renderMathInElement(document.body, {{
          delimiters: [
            {{ left: "$$", right: "$$", display: true }},
            {{ left: "$", right: "$", display: false }}
          ],
          throwOnError: false
        }});
      }}
    }}

    // Palette & Navigation
    function renderPalette() {{
      const exam = DETHI_DATA[currentExamIndex];
      paletteGrid.innerHTML = "";
      let answeredCount = 0;

      exam.mcqs.forEach((q, idx) => {{
        const btn = document.createElement("button");
        btn.className = "palette-btn";
        btn.textContent = idx + 1;
        
        const isAns = userAnswers[q.id] !== undefined;
        if (isAns) {{
          btn.classList.add("answered");
          answeredCount++;
        }}
        if (flaggedQuestions.has(q.id)) {{
          btn.classList.add("flagged");
        }}

        if (isSubmitted) {{
          if (userAnswers[q.id] === q.correctIndex) {{
            btn.classList.add("correct");
          }} else {{
            btn.classList.add("wrong");
          }}
        }}

        btn.onclick = () => {{
          const target = document.getElementById(`q_card_${{idx}}`);
          if (target) {{
            target.scrollIntoView({{ behavior: "smooth", block: "center" }});
          }}
        }};

        paletteGrid.appendChild(btn);
      }});

      answeredCountBadge.textContent = `${{answeredCount}}/${{exam.mcqs.length}}`;
    }}

    function selectOption(qId, optIdx, qIdx) {{
      if (isSubmitted) return;
      userAnswers[qId] = optIdx;
      
      // Update UI of this card
      const card = document.getElementById(`q_card_${{qIdx}}`);
      const labels = card.querySelectorAll(".opt-label");
      labels.forEach((l, idx) => {{
        if (idx === optIdx) l.classList.add("selected");
        else l.classList.remove("selected");
      }});

      renderPalette();
    }}

    function toggleFlag(qId, qIdx) {{
      if (flaggedQuestions.has(qId)) {{
        flaggedQuestions.delete(qId);
      }} else {{
        flaggedQuestions.add(qId);
      }}
      
      const card = document.getElementById(`q_card_${{qIdx}}`);
      const flagBtn = card.querySelector(".btn-flag");
      if (flaggedQuestions.has(qId)) {{
        flagBtn.classList.add("flagged");
        flagBtn.innerHTML = "🚩 Đã cắm cờ";
      }} else {{
        flagBtn.classList.remove("flagged");
        flagBtn.innerHTML = "🏳️ Cắm cờ";
      }}

      renderPalette();
    }}

    function toggleBarem(partKey) {{
      const el = document.getElementById(`barem_${{partKey}}`);
      el.classList.toggle("show");
    }}

    function setSelfScore(partKey, val) {{
      essayScores[partKey] = val;
      loadExam(); // Re-render to update active buttons and math
    }}

    // Timer Logic
    function startTimer() {{
      updateTimerDisplay();
      timerInterval = setInterval(() => {{
        if (!isPaused && !isSubmitted) {{
          timeRemaining--;
          updateTimerDisplay();
          if (timeRemaining <= 0) {{
            clearInterval(timerInterval);
            alert("⏰ Đã hết 90 phút làm bài! Hệ thống sẽ tự động nộp bài.");
            submitExam();
          }}
        }}
      }}, 1000);
    }}

    function updateTimerDisplay() {{
      const mins = Math.floor(timeRemaining / 60);
      const secs = timeRemaining % 60;
      timerDisplay.textContent = `${{String(mins).padStart(2, '0')}}:${{String(secs).padStart(2, '0')}}`;

      if (timeRemaining <= 300) {{ // 5 mins
        timerDisplay.className = "timer-display danger";
      }} else if (timeRemaining <= 900) {{ // 15 mins
        timerDisplay.className = "timer-display warning";
      }} else {{
        timerDisplay.className = "timer-display";
      }}
    }}

    btnPause.addEventListener("click", () => {{
      if (isSubmitted) return;
      isPaused = !isPaused;
      btnPause.textContent = isPaused ? "▶️ Tiếp tục" : "⏸️ Tạm dừng";
    }});

    // Submit & Grading
    btnSubmit.addEventListener("click", () => {{
      if (isSubmitted) {{
        showResultsModal();
        return;
      }}
      const exam = DETHI_DATA[currentExamIndex];
      const answered = Object.keys(userAnswers).length;
      if (answered < exam.mcqs.length) {{
        if (!confirm(`Bạn mới làm ${{answered}}/${{exam.mcqs.length}} câu trắc nghiệm. Bạn có chắc chắn muốn nộp bài sớm?`)) {{
          return;
        }}
      }}
      submitExam();
    }});

    function submitExam() {{
      isSubmitted = true;
      clearInterval(timerInterval);
      btnSubmit.textContent = "📊 Xem điểm";
      btnPause.style.display = "none";

      loadExam();
      showResultsModal();
    }}

    function showResultsModal() {{
      const exam = DETHI_DATA[currentExamIndex];
      
      // Calculate MCQ score
      let correctCount = 0;
      exam.mcqs.forEach(q => {{
        if (userAnswers[q.id] === q.correctIndex) {{
          correctCount++;
        }}
      }});
      const mcqScore = correctCount * 0.25;

      // Calculate Essay score
      let totalEssay = 0;
      for (const key in essayScores) {{
        totalEssay += essayScores[key];
      }}
      if (totalEssay > 5.0) totalEssay = 5.0;

      const totalScore = mcqScore + totalEssay;

      document.getElementById("resMcqScore").textContent = `${{mcqScore.toFixed(2)}}/5.0`;
      document.getElementById("resEssayScore").textContent = `${{totalEssay.toFixed(2)}}/5.0`;
      document.getElementById("resTotalScore").textContent = `${{totalScore.toFixed(2)}}/10.0`;

      // Advice
      let grade = "";
      let advice = "";
      if (totalScore >= 8.5) {{
        grade = "🏆 Xuất sắc (Điểm A/A+)";
        advice = "Bạn nắm rất vững toàn bộ chương trình và có phản xạ tính toán tốt. Hãy giữ phong độ và rà soát kỹ các bẫy nhỏ trong phòng thi!";
      }} else if (totalScore >= 7.0) {{
        grade = "🎖️ Giỏi (Điểm B/B+)";
        advice = "Kiến thức nền tảng của bạn rất tốt. Hãy rà soát lại các câu sai ở phần trắc nghiệm và đối chiếu barem tự luận để tối ưu hóa từng 0,25 điểm.";
      }} else if (totalScore >= 5.0) {{
        grade = "📘 Khá (Điểm C/C+)";
        advice = "Bạn đã qua môn an toàn nhưng cần củng cố thêm về Định lý CLT, phân phối chuẩn và công thức Bayes để nâng điểm lên mức Giỏi.";
      }} else {{
        grade = "⚠️ Cần Cải Thiện (D/F)";
        advice = "Bạn bị hổng một số kiến thức trọng tâm. Hãy quay lại xem 26 Bài học vi mô tại tab 'Lý thuyết' và làm lại 56 bài tự luận chuẩn barem!";
      }}

      document.getElementById("resAdvice").innerHTML = `
        <div style="font-weight: 700; font-size: 1.05rem; margin-bottom: 6px; color: var(--ink);">Xếp loại: ${{grade}}</div>
        <div>${{advice}}</div>
      `;

      scoreModal.classList.add("show");
    }}

    btnCloseModal.addEventListener("click", () => {{
      scoreModal.classList.remove("show");
    }});

    btnRetryExam.addEventListener("click", () => {{
      scoreModal.classList.remove("show");
      resetExam();
      loadExam();
    }});

    // Initialize
    document.addEventListener("DOMContentLoaded", () => {{
      initTheme();
      renderTabs();
      loadExam();
      startTimer();
    }});
  </script>
</body>
</html>
"""

# Ghi ra file site/dethi.html
output_file = os.path.join(SITE_DIR, "dethi.html")
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[OK] Successfully built {output_file} ({len(html_content)} bytes)")
