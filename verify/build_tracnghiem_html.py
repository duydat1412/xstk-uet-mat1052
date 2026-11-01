import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

print("=== BUILDING SITE/TRACNGHIEM.HTML ===")

with open('content/tracnghiem_data.json', 'r', encoding='utf-8') as f:
    mcqs = json.load(f)

print(f"Loaded {len(mcqs)} MCQs from content/tracnghiem_data.json")

# Prepare serialized JSON string safe for inlining
json_data_str = json.dumps(mcqs, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="vi" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Ngân hàng Trắc nghiệm XSTK - 161 câu UET MAT1052</title>

<!-- Fonts & KaTeX -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>

<style>
:root {
  --bg: #f8fafc;
  --card: #ffffff;
  --card-subtle: #f1f5f9;
  --ink: #0f172a;
  --mute: #64748b;
  --line: #e2e8f0;
  --acc: #3b82f6;
  --acc-hover: #2563eb;
  --acc-soft: #eff6ff;
  --ok: #10b981;
  --ok-soft: #ecfdf5;
  --bad: #ef4444;
  --bad-soft: #fef2f2;
  --warn: #f59e0b;
  --warn-soft: #fffbeb;
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
}

[data-theme="dark"] {
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
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.3);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.4);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.5);
}

* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: 'Be Vietnam Pro', system-ui, -apple-system, sans-serif;
  background: var(--bg);
  color: var(--ink);
  line-height: 1.6;
  padding-bottom: 60px;
  -webkit-font-smoothing: antialiased;
}

/* Header */
header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: var(--card);
  border-bottom: 1px solid var(--line);
  backdrop-filter: blur(12px);
  box-shadow: var(--shadow-sm);
}
.header-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: 1200px;
  margin: 0 auto;
  padding: 12px 20px;
}
.logo-group {
  display: flex;
  align-items: center;
  gap: 12px;
}
.badge-course {
  background: var(--acc-soft);
  color: var(--acc);
  padding: 4px 10px;
  border-radius: 99px;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}
.title-main {
  font-size: 1.15rem;
  font-weight: 800;
  letter-spacing: -0.01em;
}
.nav-links {
  display: flex;
  align-items: center;
  gap: 6px;
}
.nav-link {
  color: var(--mute);
  text-decoration: none;
  font-size: 0.85rem;
  font-weight: 600;
  padding: 6px 12px;
  border-radius: var(--radius-sm);
  transition: all 0.2s;
}
.nav-link:hover { color: var(--ink); background: var(--card-subtle); }
.nav-link.active {
  color: var(--acc);
  background: var(--acc-soft);
  font-weight: 700;
}
.btn-icon {
  background: var(--card-subtle);
  border: 1px solid var(--line);
  color: var(--ink);
  padding: 8px 12px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  font-size: 0.85rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s;
}
.btn-icon:hover { border-color: var(--acc); }

/* Main Container */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 24px 20px;
}

/* Mode Switcher Tabs */
.mode-tabs {
  display: flex;
  background: var(--card-subtle);
  padding: 6px;
  border-radius: var(--radius-md);
  gap: 6px;
  margin-bottom: 20px;
  border: 1px solid var(--line);
}
.mode-tab {
  flex: 1;
  text-align: center;
  padding: 10px 14px;
  border-radius: var(--radius-sm);
  border: 0;
  background: transparent;
  color: var(--mute);
  font-weight: 600;
  font-size: 0.92rem;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}
.mode-tab:hover { color: var(--ink); }
.mode-tab.active {
  background: var(--card);
  color: var(--acc);
  font-weight: 700;
  box-shadow: var(--shadow-sm);
}

/* Stats Ribbon */
.stats-ribbon {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 12px;
  margin-bottom: 20px;
}
.stat-box {
  background: var(--card);
  border: 1px solid var(--line);
  padding: 14px 18px;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-sm);
}
.stat-box small {
  display: block;
  font-size: 0.78rem;
  color: var(--mute);
  font-weight: 600;
  text-transform: uppercase;
  margin-bottom: 4px;
}
.stat-box .val {
  font-size: 1.45rem;
  font-weight: 800;
  color: var(--ink);
}

/* Filters & Search */
.controls-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  padding: 18px 20px;
  margin-bottom: 24px;
  box-shadow: var(--shadow-sm);
}
.topic-scroll {
  display: flex;
  overflow-x: auto;
  gap: 8px;
  padding-bottom: 12px;
  margin-bottom: 14px;
  border-bottom: 1px solid var(--line);
  scrollbar-width: thin;
}
.topic-btn {
  white-space: nowrap;
  padding: 8px 16px;
  border-radius: 99px;
  border: 1px solid var(--line);
  background: var(--card-subtle);
  color: var(--mute);
  font-size: 0.84rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}
.topic-btn:hover { color: var(--ink); border-color: var(--acc); }
.topic-btn.active {
  background: var(--acc);
  border-color: var(--acc);
  color: #fff;
  font-weight: 700;
}
.filter-row {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  align-items: center;
  justify-content: space-between;
}
.filter-group {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
}
.filter-label {
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--mute);
  margin-right: 4px;
}
.chip-btn {
  padding: 6px 12px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--line);
  background: var(--card);
  color: var(--ink);
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s;
}
.chip-btn:hover { border-color: var(--acc); }
.chip-btn.active {
  background: var(--acc-soft);
  border-color: var(--acc);
  color: var(--acc);
  font-weight: 700;
}
.search-input {
  flex: 1;
  min-width: 220px;
  max-width: 320px;
  padding: 8px 14px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--line);
  background: var(--bg);
  color: var(--ink);
  font-family: inherit;
  font-size: 0.85rem;
}
.search-input:focus {
  outline: 2px solid var(--acc);
  border-color: transparent;
}

/* Layout for Quiz View: List + Quick Jump Matrix */
.quiz-layout {
  display: grid;
  grid-template-columns: 1fr 300px;
  gap: 24px;
  align-items: start;
}
@media (max-width: 900px) {
  .quiz-layout { grid-template-columns: 1fr; }
}

/* MCQ Card */
.mcq-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  padding: 24px;
  margin-bottom: 20px;
  box-shadow: var(--shadow-sm);
  transition: transform 0.15s, box-shadow 0.15s;
  position: relative;
}
.mcq-card:hover {
  box-shadow: var(--shadow-md);
}
.mcq-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}
.mcq-tags {
  display: flex;
  align-items: center;
  gap: 8px;
}
.tag-id {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--acc);
  background: var(--acc-soft);
  padding: 2px 8px;
  border-radius: 6px;
}
.tag-topic {
  font-size: 0.78rem;
  color: var(--mute);
  font-weight: 600;
}
.tag-level {
  font-size: 0.72rem;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 99px;
}
.tag-level.cb { background: var(--ok-soft); color: var(--ok); }
.tag-level.tb { background: var(--warn-soft); color: var(--warn); }
.tag-level.nc { background: var(--bad-soft); color: var(--bad); }

.bookmark-btn {
  background: transparent;
  border: 0;
  cursor: pointer;
  color: var(--mute);
  font-size: 1.15rem;
  transition: color 0.15s;
}
.bookmark-btn.active { color: var(--warn); }

.mcq-question {
  font-size: 1.05rem;
  font-weight: 600;
  color: var(--ink);
  margin-bottom: 20px;
  line-height: 1.6;
}

/* Options */
.options-grid {
  display: grid;
  gap: 10px;
  margin-bottom: 18px;
}
.option-btn {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  width: 100%;
  text-align: left;
  padding: 14px 16px;
  border-radius: var(--radius-md);
  border: 2px solid var(--line);
  background: var(--card);
  color: var(--ink);
  font-family: inherit;
  font-size: 0.95rem;
  cursor: pointer;
  transition: all 0.15s;
}
.option-btn:hover:not(:disabled) {
  border-color: var(--acc);
  background: var(--card-subtle);
}
.option-letter {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: var(--card-subtle);
  border: 1px solid var(--line);
  font-weight: 800;
  font-size: 0.85rem;
  color: var(--mute);
  flex-shrink: 0;
  margin-top: 1px;
}
.option-text {
  flex: 1;
}

/* Option states */
.option-btn.selected-correct {
  border-color: var(--ok);
  background: var(--ok-soft);
  color: var(--ink);
}
.option-btn.selected-correct .option-letter {
  background: var(--ok);
  border-color: var(--ok);
  color: #fff;
}
.option-btn.selected-wrong {
  border-color: var(--bad);
  background: var(--bad-soft);
  color: var(--ink);
}
.option-btn.selected-wrong .option-letter {
  background: var(--bad);
  border-color: var(--bad);
  color: #fff;
}
.option-btn.reveal-correct {
  border-color: var(--ok);
  background: var(--ok-soft);
  border-style: dashed;
}
.option-btn.reveal-correct .option-letter {
  background: var(--ok);
  border-color: var(--ok);
  color: #fff;
}

/* Explanation Box */
.explanation-card {
  background: var(--card-subtle);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  padding: 18px 20px;
  margin-top: 16px;
  animation: fadeIn 0.25s ease-out;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-6px); }
  to { opacity: 1; transform: translateY(0); }
}
.exp-title {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 800;
  font-size: 0.95rem;
  margin-bottom: 12px;
}
.exp-title.ok { color: var(--ok); }
.exp-title.bad { color: var(--bad); }
.exp-body {
  font-size: 0.92rem;
  color: var(--ink);
  line-height: 1.7;
  white-space: pre-wrap;
}
.exp-source {
  margin-top: 14px;
  font-size: 0.78rem;
  color: var(--mute);
  font-style: italic;
  border-top: 1px solid var(--line);
  padding-top: 8px;
}

/* Quick Jump Matrix Sidebar */
.matrix-sidebar {
  position: sticky;
  top: 80px;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  padding: 20px;
  box-shadow: var(--shadow-sm);
  max-height: calc(100vh - 110px);
  overflow-y: auto;
}
.sidebar-title {
  font-size: 0.95rem;
  font-weight: 800;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.matrix-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 6px;
  margin-bottom: 16px;
}
.matrix-item {
  aspect-ratio: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  font-weight: 700;
  border-radius: 6px;
  border: 1px solid var(--line);
  background: var(--card-subtle);
  color: var(--mute);
  cursor: pointer;
  transition: all 0.15s;
  text-decoration: none;
}
.matrix-item:hover { border-color: var(--acc); color: var(--acc); }
.matrix-item.correct { background: var(--ok); border-color: var(--ok); color: #fff; }
.matrix-item.wrong { background: var(--bad); border-color: var(--bad); color: #fff; }
.matrix-item.flagged { box-shadow: 0 0 0 2px var(--warn); }

/* Exam Mode Container */
.exam-banner {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  padding: 16px 20px;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: var(--shadow-sm);
}
.timer-val {
  font-family: 'JetBrains Mono', monospace;
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--acc);
}
.timer-val.urgent { color: var(--bad); animation: pulse 1s infinite; }
@keyframes pulse { 50% { opacity: 0.5; } }

.btn-primary {
  background: var(--acc);
  color: #fff;
  border: 0;
  padding: 10px 20px;
  border-radius: var(--radius-sm);
  font-size: 0.92rem;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.15s;
}
.btn-primary:hover { background: var(--acc-hover); }

/* Modal */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(4px);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}
.modal-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  max-width: 500px;
  width: 100%;
  padding: 28px;
  box-shadow: var(--shadow-lg);
}
.modal-title { font-size: 1.3rem; font-weight: 800; margin-bottom: 12px; }
.modal-body { font-size: 0.95rem; color: var(--mute); margin-bottom: 20px; line-height: 1.6; }
.modal-actions { display: flex; gap: 10px; justify-content: flex-end; }

/* Empty state */
.empty-state {
  text-align: center;
  padding: 60px 20px;
  background: var(--card);
  border: 1px dashed var(--line);
  border-radius: var(--radius-lg);
  color: var(--mute);
}
.empty-state h3 { font-size: 1.15rem; color: var(--ink); margin-bottom: 6px; }

/* Score Report */
.score-card {
  text-align: center;
  padding: 24px;
  background: var(--card-subtle);
  border-radius: var(--radius-md);
  margin-bottom: 20px;
}
.big-score {
  font-size: 3rem;
  font-weight: 800;
  color: var(--acc);
  line-height: 1;
  margin: 10px 0;
}
.topic-breakdown {
  margin: 16px 0;
  text-align: left;
}
.topic-breakdown-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 0;
  border-bottom: 1px solid var(--line);
  font-size: 0.88rem;
}

</style>
</head>
<body>

<header>
  <div class="header-top">
    <div class="logo-group">
      <span class="badge-course">UET MAT1052</span>
      <h1 class="title-main">Ngân hàng Trắc nghiệm XSTK</h1>
    </div>
    <nav class="nav-links">
      <a href="hoc.html" class="nav-link">Lý thuyết</a>
      <a href="tuluan.html" class="nav-link">Tự luận (56 bài)</a>
      <a href="tracnghiem.html" class="nav-link active">Trắc nghiệm (161 câu)</a>
      <a href="dethi.html" class="nav-link">Đề thi mẫu</a>
      <a href="congthuc.html" class="nav-link">Công thức</a>
    </nav>
    <button id="themeToggle" class="btn-icon" title="Chuyển chế độ Sáng / Tối">
      <span id="themeIcon">🌓</span>
    </button>
  </div>
</header>

<main class="container">

  <!-- Study Mode Selector -->
  <div class="mode-tabs">
    <button class="mode-tab active" data-mode="practice" onclick="setMode('practice')">
      <span>🎯 Luyện tập tức thì</span>
    </button>
    <button class="mode-tab" data-mode="exam" onclick="setMode('exam')">
      <span>⏱️ Thi thử tính giờ</span>
    </button>
    <button class="mode-tab" data-mode="notebook" onclick="setMode('notebook')">
      <span>📖 Sổ tay câu sai (<span id="wrongCountBadge">0</span>)</span>
    </button>
  </div>

  <!-- Stats Ribbon -->
  <div class="stats-ribbon" id="statsRibbon">
    <div class="stat-box">
      <small>Tổng câu hỏi</small>
      <div class="val" id="statTotal">161</div>
    </div>
    <div class="stat-box">
      <small>Đã hoàn thành</small>
      <div class="val" id="statDone">0</div>
    </div>
    <div class="stat-box">
      <small>Tỷ lệ đúng</small>
      <div class="val" id="statAccuracy">0%</div>
    </div>
    <div class="stat-box">
      <small>Điểm kinh nghiệm (XP)</small>
      <div class="val" id="statXP">0 XP</div>
    </div>
  </div>

  <!-- Exam Mode Top Banner (hidden by default) -->
  <div id="examBanner" class="exam-banner" style="display: none;">
    <div>
      <div style="font-size: 0.82rem; color: var(--mute); font-weight: 700; text-transform: uppercase;">Thời gian làm bài còn lại</div>
      <div id="timerDisplay" class="timer-val">45:00</div>
    </div>
    <div style="display: flex; gap: 10px; align-items: center;">
      <span id="examProgressTxt" style="font-size: 0.9rem; font-weight: 600; color: var(--mute);">Đã làm: 0/30 câu</span>
      <button class="btn-primary" onclick="confirmSubmitExam()">Nộp bài</button>
    </div>
  </div>

  <!-- Controls Card: Filters & Search (Only shown in Practice & Notebook modes) -->
  <div class="controls-card" id="controlsCard">
    <div class="topic-scroll">
      <button class="topic-btn active" data-topic="0" onclick="filterTopic(0)">Tất cả 7 chủ đề</button>
      <button class="topic-btn" data-topic="1" onclick="filterTopic(1)">1. Dữ liệu & Thống kê mô tả (23)</button>
      <button class="topic-btn" data-topic="2" onclick="filterTopic(2)">2. Xác suất & Bayes (23)</button>
      <button class="topic-btn" data-topic="3" onclick="filterTopic(3)">3. Biến rời rạc & Kỳ vọng (22)</button>
      <button class="topic-btn" data-topic="4" onclick="filterTopic(4)">4. Mô hình rời rạc (23)</button>
      <button class="topic-btn" data-topic="5" onclick="filterTopic(5)">5. Hộp, Chebyshev & WLLN (22)</button>
      <button class="topic-btn" data-topic="6" onclick="filterTopic(6)">6. Biến liên tục & Chuẩn (25)</button>
      <button class="topic-btn" data-topic="7" onclick="filterTopic(7)">7. CLT & Ứng dụng (23)</button>
    </div>

    <div class="filter-row">
      <div class="filter-group">
        <span class="filter-label">Mức độ:</span>
        <button class="chip-btn active" data-level="all" onclick="filterLevel('all')">Tất cả</button>
        <button class="chip-btn" data-level="cb" onclick="filterLevel('cb')">Cơ bản</button>
        <button class="chip-btn" data-level="tb" onclick="filterLevel('tb')">Trung bình</button>
        <button class="chip-btn" data-level="nc" onclick="filterLevel('nc')">Nâng cao</button>
      </div>

      <div class="filter-group">
        <span class="filter-label">Trạng thái:</span>
        <button class="chip-btn active" data-status="all" onclick="filterStatus('all')">Tất cả</button>
        <button class="chip-btn" data-status="todo" onclick="filterStatus('todo')">Chưa làm</button>
        <button class="chip-btn" data-status="ok" onclick="filterStatus('ok')">Đã đúng</button>
        <button class="chip-btn" data-status="wrong" onclick="filterStatus('wrong')">Từng sai</button>
      </div>

      <input type="text" id="searchInput" class="search-input" placeholder="🔍 Tìm kiếm bài tập, từ khóa..." oninput="handleSearch()">
    </div>
  </div>

  <!-- Quiz View Layout: Questions List + Matrix Sidebar -->
  <div class="quiz-layout">
    <div id="mcqList">
      <!-- MCQs injected by JS -->
    </div>

    <!-- Quick Jump Sidebar -->
    <aside class="matrix-sidebar" id="matrixSidebar">
      <div class="sidebar-title">
        <span>Ma trận câu hỏi (<span id="matrixCount">161</span>)</span>
        <button onclick="resetAllProgress()" style="font-size: 0.72rem; color: var(--mute); background: transparent; border: 0; cursor: pointer; text-decoration: underline;">Đặt lại</button>
      </div>
      <div class="matrix-grid" id="matrixGrid">
        <!-- Matrix items injected by JS -->
      </div>
    </aside>
  </div>

</main>

<!-- Inlined Data -->
<script>
window.TRAC_NGHIEM_DATA = """ + json_data_str + """;
</script>

<!-- App Logic -->
<script>
let currentMode = 'practice'; // 'practice' | 'exam' | 'notebook'
let currentTopic = 0; // 0 = all
let currentLevel = 'all';
let currentStatus = 'all';
let searchQuery = '';

// LocalStorage user progress: { [id]: { chosenIndex, isCorrect, timestamp, flagged } }
let userProgress = {};
try {
  const saved = localStorage.getItem('xstk_mcq_progress');
  if (saved) userProgress = JSON.parse(saved);
} catch(e) { console.error(e); }

function saveProgress() {
  try {
    localStorage.setItem('xstk_mcq_progress', JSON.stringify(userProgress));
  } catch(e) { console.error(e); }
  updateStats();
}

// Exam State
let examQuestions = [];
let examAnswers = {};
let examTimer = null;
let examSecondsLeft = 45 * 60;

// Theme toggle
function initTheme() {
  const savedTheme = localStorage.getItem('xstk_theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  document.documentElement.setAttribute('data-theme', savedTheme);
  document.getElementById('themeIcon').textContent = savedTheme === 'dark' ? '☀️' : '🌙';
}
document.getElementById('themeToggle').addEventListener('click', () => {
  const current = document.documentElement.getAttribute('data-theme');
  const target = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', target);
  localStorage.setItem('xstk_theme', target);
  document.getElementById('themeIcon').textContent = target === 'dark' ? '☀️' : '🌙';
});

// Render Math via KaTeX
function renderMathInPage() {
  if (window.renderMathInElement) {
    window.renderMathInElement(document.body, {
      delimiters: [
        {left: '$$', right: '$$', display: true},
        {left: '$', right: '$', display: false},
        {left: '\\\\(', right: '\\\\)', display: false},
        {left: '\\\\[', right: '\\\\]', display: true}
      ],
      throwOnError: false
    });
  }
}

// Mode Management
function setMode(mode) {
  currentMode = mode;
  document.querySelectorAll('.mode-tab').forEach(t => t.classList.toggle('active', t.dataset.mode === mode));
  
  const examBanner = document.getElementById('examBanner');
  const controlsCard = document.getElementById('controlsCard');
  const statsRibbon = document.getElementById('statsRibbon');

  if (mode === 'exam') {
    startExamSetup();
  } else {
    if (examTimer) { clearInterval(examTimer); examTimer = null; }
    examBanner.style.display = 'none';
    controlsCard.style.display = 'block';
    statsRibbon.style.display = 'grid';
    if (mode === 'notebook') {
      currentStatus = 'wrong';
      document.querySelectorAll('[data-status]').forEach(b => b.classList.toggle('active', b.dataset.status === 'wrong'));
    } else {
      currentStatus = 'all';
      document.querySelectorAll('[data-status]').forEach(b => b.classList.toggle('active', b.dataset.status === 'all'));
    }
    renderMCQs();
  }
}

function filterTopic(tid) {
  currentTopic = tid;
  document.querySelectorAll('.topic-btn').forEach(b => b.classList.toggle('active', parseInt(b.dataset.topic) === tid));
  renderMCQs();
}

function filterLevel(lvl) {
  currentLevel = lvl;
  document.querySelectorAll('[data-level]').forEach(b => b.classList.toggle('active', b.dataset.level === lvl));
  renderMCQs();
}

function filterStatus(st) {
  currentStatus = st;
  document.querySelectorAll('[data-status]').forEach(b => b.classList.toggle('active', b.dataset.status === st));
  renderMCQs();
}

function handleSearch() {
  searchQuery = document.getElementById('searchInput').value.trim().toLowerCase();
  renderMCQs();
}

function toggleBookmark(qid, e) {
  e.stopPropagation();
  if (!userProgress[qid]) userProgress[qid] = {};
  userProgress[qid].flagged = !userProgress[qid].flagged;
  saveProgress();
  renderMCQs();
}

function resetAllProgress() {
  if (confirm("Bạn có chắc chắn muốn đặt lại toàn bộ lịch sử làm bài trắc nghiệm?")) {
    userProgress = {};
    saveProgress();
    renderMCQs();
  }
}

function updateStats() {
  const total = window.TRAC_NGHIEM_DATA.length;
  let done = 0;
  let correct = 0;
  let wrong = 0;

  for (let q of window.TRAC_NGHIEM_DATA) {
    const p = userProgress[q.id];
    if (p && p.chosenIndex !== undefined) {
      done++;
      if (p.isCorrect) correct++;
      else wrong++;
    }
  }

  document.getElementById('statTotal').textContent = total;
  document.getElementById('statDone').textContent = `${done}/${total}`;
  const acc = done > 0 ? Math.round((correct / done) * 100) : 0;
  document.getElementById('statAccuracy').textContent = `${acc}%`;
  document.getElementById('statXP').textContent = `${correct * 10} XP`;
  document.getElementById('wrongCountBadge').textContent = wrong;
}

// Main Render Function
function renderMCQs() {
  const listEl = document.getElementById('mcqList');
  const matrixEl = document.getElementById('matrixGrid');
  listEl.innerHTML = '';
  matrixEl.innerHTML = '';

  let filtered = window.TRAC_NGHIEM_DATA.filter(q => {
    if (currentTopic !== 0 && q.topicId !== currentTopic) return false;
    if (currentLevel === 'cb' && q.level !== 'Cơ bản') return false;
    if (currentLevel === 'tb' && q.level !== 'Trung bình') return false;
    if (currentLevel === 'nc' && q.level !== 'Nâng cao') return false;

    const prog = userProgress[q.id];
    if (currentStatus === 'todo' && prog && prog.chosenIndex !== undefined) return false;
    if (currentStatus === 'ok' && (!prog || !prog.isCorrect)) return false;
    if (currentStatus === 'wrong' && (!prog || prog.isCorrect)) return false;

    if (searchQuery) {
      const text = (q.id + ' ' + q.question + ' ' + q.explanation + ' ' + q.topicName).toLowerCase();
      if (!text.includes(searchQuery)) return false;
    }
    return true;
  });

  document.getElementById('matrixCount').textContent = filtered.length;

  if (filtered.length === 0) {
    listEl.innerHTML = `
      <div class="empty-state">
        <h3>Không tìm thấy câu hỏi phù hợp</h3>
        <p>Vui lòng thử chọn bộ lọc khác hoặc xoá bớt từ khoá tìm kiếm.</p>
      </div>
    `;
    return;
  }

  const letters = ['A', 'B', 'C', 'D'];

  filtered.forEach((q, idx) => {
    const prog = userProgress[q.id] || {};
    const isAnswered = prog.chosenIndex !== undefined;
    const isCorrect = prog.isCorrect;
    const isFlagged = prog.flagged;

    // Build MCQ card
    const card = document.createElement('div');
    card.className = 'mcq-card';
    card.id = 'card_' + q.id;

    let levelClass = 'cb';
    if (q.level === 'Trung bình') levelClass = 'tb';
    if (q.level === 'Nâng cao') levelClass = 'nc';

    card.innerHTML = `
      <div class="mcq-card-header">
        <div class="mcq-tags">
          <span class="tag-id">${q.id}</span>
          <span class="tag-topic">Chủ đề ${q.topicId}: ${q.topicName}</span>
          <span class="tag-level ${levelClass}">${q.level}</span>
        </div>
        <button class="bookmark-btn ${isFlagged ? 'active' : ''}" onclick="toggleBookmark('${q.id}', event)" title="Đánh dấu câu hỏi này">
          ${isFlagged ? '★' : '☆'}
        </button>
      </div>

      <div class="mcq-question">${idx + 1}. ${q.question}</div>

      <div class="options-grid" id="opts_${q.id}">
        ${q.options.map((opt, oIdx) => {
          let btnClass = 'option-btn';
          if (isAnswered) {
            if (oIdx === q.correctIndex) {
              btnClass += (prog.chosenIndex === oIdx) ? ' selected-correct' : ' reveal-correct';
            } else if (prog.chosenIndex === oIdx) {
              btnClass += ' selected-wrong';
            }
          }
          const disabledAttr = (currentMode === 'practice' && isAnswered) ? 'disabled' : '';
          return `
            <button class="${btnClass}" ${disabledAttr} onclick="selectOption('${q.id}', ${oIdx})">
              <span class="option-letter">${letters[oIdx]}</span>
              <span class="option-text">${opt}</span>
            </button>
          `;
        }).join('')}
      </div>

      ${isAnswered ? `
        <div class="explanation-card">
          <div class="exp-title ${isCorrect ? 'ok' : 'bad'}">
            <span>${isCorrect ? '✅ Chính xác! (+10 XP)' : '❌ Chưa chính xác!'}</span>
          </div>
          <div class="exp-body">${q.explanation}</div>
          <div class="exp-source">Nguồn: ${q.source}</div>
        </div>
      ` : ''}
    `;
    listEl.appendChild(card);

    // Build matrix button
    const mBtn = document.createElement('a');
    mBtn.className = 'matrix-item';
    mBtn.href = '#card_' + q.id;
    mBtn.textContent = idx + 1;
    if (isAnswered) {
      if (isCorrect) mBtn.classList.add('correct');
      else mBtn.classList.add('wrong');
    }
    if (isFlagged) mBtn.classList.add('flagged');
    matrixEl.appendChild(mBtn);
  });

  renderMathInPage();
}

function selectOption(qid, chosenIdx) {
  const q = window.TRAC_NGHIEM_DATA.find(x => x.id === qid);
  if (!q) return;

  const isCorrect = (chosenIdx === q.correctIndex);
  userProgress[qid] = {
    chosenIndex: chosenIdx,
    isCorrect: isCorrect,
    timestamp: Date.now(),
    flagged: (userProgress[qid] && userProgress[qid].flagged) || false
  };

  saveProgress();
  renderMCQs();
}

// Exam Mode Implementation
function startExamSetup() {
  const count = prompt(`Chọn số lượng câu hỏi thi thử:\n1. 20 câu (30 phút)\n2. 30 câu (45 phút)\n3. 40 câu (60 phút)`, "30");
  let numQ = parseInt(count) || 30;
  if (![20, 30, 40].includes(numQ)) numQ = 30;

  // Shuffle and pick
  const shuffled = [...window.TRAC_NGHIEM_DATA].sort(() => 0.5 - Math.random());
  examQuestions = shuffled.slice(0, numQ);
  examAnswers = {};
  examSecondsLeft = numQ * 90; // 1.5 min per question

  document.getElementById('examBanner').style.display = 'flex';
  document.getElementById('controlsCard').style.display = 'none';
  document.getElementById('statsRibbon').style.display = 'none';

  startExamTimer();
  renderExamView();
}

function startExamTimer() {
  if (examTimer) clearInterval(examTimer);
  updateTimerDisplay();
  examTimer = setInterval(() => {
    examSecondsLeft--;
    updateTimerDisplay();
    if (examSecondsLeft <= 0) {
      clearInterval(examTimer);
      alert("Hết giờ làm bài! Hệ thống sẽ tự động nộp bài của bạn.");
      submitExam();
    }
  }, 1000);
}

function updateTimerDisplay() {
  const mins = Math.floor(examSecondsLeft / 60);
  const secs = examSecondsLeft % 60;
  const disp = document.getElementById('timerDisplay');
  disp.textContent = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  if (examSecondsLeft < 300) disp.classList.add('urgent');
  else disp.classList.remove('urgent');

  const answeredCount = Object.keys(examAnswers).length;
  document.getElementById('examProgressTxt').textContent = `Đã làm: ${answeredCount}/${examQuestions.length} câu`;
}

function renderExamView() {
  const listEl = document.getElementById('mcqList');
  const matrixEl = document.getElementById('matrixGrid');
  listEl.innerHTML = '';
  matrixEl.innerHTML = '';

  const letters = ['A', 'B', 'C', 'D'];

  examQuestions.forEach((q, idx) => {
    const card = document.createElement('div');
    card.className = 'mcq-card';
    card.id = 'exam_card_' + q.id;

    const chosenIdx = examAnswers[q.id];

    card.innerHTML = `
      <div class="mcq-card-header">
        <div class="mcq-tags">
          <span class="tag-id">Câu ${idx + 1}</span>
          <span class="tag-topic">Chủ đề ${q.topicId}: ${q.topicName}</span>
        </div>
      </div>
      <div class="mcq-question">${q.question}</div>
      <div class="options-grid">
        ${q.options.map((opt, oIdx) => {
          const isSelected = (chosenIdx === oIdx);
          return `
            <button class="option-btn ${isSelected ? 'selected-correct' : ''}" onclick="selectExamOption('${q.id}', ${oIdx})">
              <span class="option-letter">${letters[oIdx]}</span>
              <span class="option-text">${opt}</span>
            </button>
          `;
        }).join('')}
      </div>
    `;
    listEl.appendChild(card);

    const mBtn = document.createElement('a');
    mBtn.className = 'matrix-item' + (chosenIdx !== undefined ? ' correct' : '');
    mBtn.href = '#exam_card_' + q.id;
    mBtn.textContent = idx + 1;
    matrixEl.appendChild(mBtn);
  });

  renderMathInPage();
}

function selectExamOption(qid, optIdx) {
  examAnswers[qid] = optIdx;
  updateTimerDisplay();
  renderExamView();
}

function confirmSubmitExam() {
  const answeredCount = Object.keys(examAnswers).length;
  const total = examQuestions.length;
  if (answeredCount < total) {
    if (!confirm(`Bạn mới chỉ làm ${answeredCount}/${total} câu hỏi. Bạn có chắc chắn muốn nộp bài sớm không?`)) {
      return;
    }
  } else {
    if (!confirm("Bạn có chắc chắn muốn nộp bài để xem kết quả?")) return;
  }
  submitExam();
}

function submitExam() {
  if (examTimer) clearInterval(examTimer);
  
  let score = 0;
  let topicStats = {};

  examQuestions.forEach(q => {
    if (!topicStats[q.topicId]) topicStats[q.topicId] = { name: q.topicName, total: 0, correct: 0 };
    topicStats[q.topicId].total++;

    const chosen = examAnswers[q.id];
    const isCorrect = (chosen === q.correctIndex);
    if (isCorrect) {
      score++;
      topicStats[q.topicId].correct++;
    }

    // Save into global progress as well
    userProgress[q.id] = {
      chosenIndex: chosen,
      isCorrect: isCorrect,
      timestamp: Date.now()
    };
  });
  saveProgress();

  const finalScore10 = ((score / examQuestions.length) * 10).toFixed(2).replace('.', ',');

  let breakdownHtml = Object.keys(topicStats).map(tid => {
    const st = topicStats[tid];
    const pct = Math.round((st.correct / st.total) * 100);
    return `
      <div class="topic-breakdown-row">
        <span>Chủ đề ${tid}: ${st.name}</span>
        <b>${st.correct}/${st.total} (${pct}%)</b>
      </div>
    `;
  }).join('');

  const modal = document.createElement('div');
  modal.className = 'modal-overlay';
  modal.innerHTML = `
    <div class="modal-card">
      <h2 class="modal-title">🎉 Kết quả Thi thử</h2>
      <div class="score-card">
        <div>Điểm số quy đổi (thang 10)</div>
        <div class="big-score">${finalScore10}</div>
        <div style="font-weight: 600; color: var(--mute);">Đúng ${score}/${examQuestions.length} câu (${Math.round(score/examQuestions.length*100)}%)</div>
      </div>
      <div class="topic-breakdown">
        <div style="font-size: 0.8rem; font-weight: 700; color: var(--mute); text-transform: uppercase; margin-bottom: 6px;">Phân tích kết quả theo chủ đề:</div>
        ${breakdownHtml}
      </div>
      <div class="modal-actions">
        <button class="btn-primary" onclick="closeExamModalAndReview()">Xem lại bài giải chi tiết</button>
      </div>
    </div>
  `;
  document.body.appendChild(modal);
}

function closeExamModalAndReview() {
  document.querySelector('.modal-overlay').remove();
  setMode('practice');
}

// Initial Boot
window.addEventListener('DOMContentLoaded', () => {
  initTheme();
  updateStats();
  renderMCQs();
});
</script>

</body>
</html>
"""

with open('site/tracnghiem.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Saved site/tracnghiem.html successfully!")
