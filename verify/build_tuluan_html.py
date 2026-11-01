import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read tuluan data
with open("content/tuluan_data.json", "r", encoding="utf-8") as f:
    tuluan_data = json.load(f)

html_template = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>56 Bài tập Tự luận Chuẩn Barem – XSTK UET.MAT1052</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&family=Fira+Code:wght@400;600&display=swap">
<!-- KaTeX for formula rendering -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" crossorigin="anonymous">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" crossorigin="anonymous"></script>

<style>
:root {
  --bg: #f8fafc;
  --card: #ffffff;
  --card-sub: #f1f5f9;
  --ink: #0f172a;
  --mute: #64748b;
  --line: #e2e8f0;
  --acc: #2563eb;
  --acc-hover: #1d4ed8;
  --acc-soft: #eff6ff;
  --ok: #16a34a;
  --ok-soft: #dcfce7;
  --bad: #dc2626;
  --bad-soft: #fee2e2;
  --warn: #d97706;
  --warn-soft: #fef3c7;
  --radius: 14px;
}

:root[data-theme="dark"] {
  --bg: #0b0f17;
  --card: #151c28;
  --card-sub: #1e2738;
  --ink: #f1f5f9;
  --mute: #94a3b8;
  --line: #263348;
  --acc: #3b82f6;
  --acc-hover: #60a5fa;
  --acc-soft: #1a2744;
  --ok: #22c55e;
  --ok-soft: #143522;
  --bad: #ef4444;
  --bad-soft: #381a1d;
  --warn: #f59e0b;
  --warn-soft: #3a2a11;
}

* { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font: 16px/1.6 "Be Vietnam Pro", system-ui, -apple-system, sans-serif;
  transition: background .25s ease, color .25s ease;
  padding-bottom: 80px;
}

/* HEADER */
header {
  position: sticky;
  top: 0;
  z-index: 50;
  background: var(--card);
  border-bottom: 1px solid var(--line);
  backdrop-filter: blur(8px);
  padding: 10px 16px;
}
.header-wrap {
  max-width: 960px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}
.brand {
  font-size: 1.05rem;
  font-weight: 800;
  display: flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  color: var(--ink);
}
.brand span { color: var(--acc); }
.nav-links {
  display: flex;
  align-items: center;
  gap: 6px;
}
.nav-link {
  padding: 6px 12px;
  border-radius: 8px;
  text-decoration: none;
  font-size: .86rem;
  font-weight: 600;
  color: var(--mute);
  transition: .15s;
}
.nav-link:hover { color: var(--ink); background: var(--card-sub); }
.nav-link.active {
  color: var(--acc);
  background: var(--acc-soft);
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}
.btn-icon {
  background: var(--card-sub);
  border: 1px solid var(--line);
  color: var(--ink);
  width: 36px;
  height: 36px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 1rem;
  transition: .15s;
}
.btn-icon:hover { border-color: var(--acc); color: var(--acc); }

/* PROGRESS BAR */
.progress-bar-wrap {
  width: 100%;
  height: 4px;
  background: var(--line);
  position: absolute;
  bottom: 0;
  left: 0;
}
.progress-bar-fill {
  height: 100%;
  width: 0%;
  background: var(--ok);
  transition: width .3s ease;
}

/* MAIN CONTAINER */
main {
  max-width: 960px;
  margin: 0 auto;
  padding: 16px;
}

/* HERO STATS BAR */
.stats-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 16px 20px;
  margin-bottom: 16px;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}
.stats-left h1 {
  font-size: 1.25rem;
  font-weight: 800;
  margin: 0 0 4px 0;
}
.stats-left p {
  margin: 0;
  color: var(--mute);
  font-size: .88rem;
}
.stats-pills {
  display: flex;
  gap: 12px;
  align-items: center;
}
.stat-pill {
  background: var(--card-sub);
  border: 1px solid var(--line);
  padding: 8px 14px;
  border-radius: 10px;
  text-align: center;
}
.stat-pill .num {
  font-size: 1.2rem;
  font-weight: 800;
  line-height: 1.2;
}
.stat-pill .lbl {
  font-size: .75rem;
  color: var(--mute);
  font-weight: 600;
}

/* SEARCH & CONTROLS */
.controls-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 16px;
}
.search-box {
  flex: 1 1 240px;
  position: relative;
}
.search-input {
  width: 100%;
  padding: 10px 14px 10px 38px;
  border-radius: 10px;
  border: 1px solid var(--line);
  background: var(--card);
  color: var(--ink);
  font-size: .92rem;
  font-family: inherit;
  outline: none;
  transition: .15s;
}
.search-input:focus { border-color: var(--acc); box-shadow: 0 0 0 3px var(--acc-soft); }
.search-icon {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--mute);
  font-size: .95rem;
  pointer-events: none;
}

/* TOPIC PILLS (HORIZONTAL SCROLL) */
.topic-nav {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding: 4px 0 12px;
  scrollbar-width: none;
}
.topic-nav::-webkit-scrollbar { display: none; }
.topic-btn {
  white-space: nowrap;
  padding: 8px 14px;
  border-radius: 20px;
  border: 1px solid var(--line);
  background: var(--card);
  color: var(--mute);
  font-weight: 600;
  font-size: .86rem;
  cursor: pointer;
  transition: .15s;
}
.topic-btn:hover { color: var(--ink); border-color: var(--mute); }
.topic-btn.active {
  background: var(--acc);
  border-color: var(--acc);
  color: #fff;
}

/* SECONDARY FILTERS ROW */
.filter-row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  margin-bottom: 16px;
}
.sub-filters {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}
.sub-filter-btn {
  padding: 5px 10px;
  border-radius: 8px;
  border: 1px solid var(--line);
  background: var(--card);
  color: var(--mute);
  font-size: .8rem;
  font-weight: 600;
  cursor: pointer;
  transition: .15s;
}
.sub-filter-btn:hover { color: var(--ink); }
.sub-filter-btn.active {
  background: var(--ink);
  color: var(--bg);
  border-color: var(--ink);
}

/* EXERCISE CARD */
.ex-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 20px;
  margin-bottom: 20px;
  transition: border-color .2s, box-shadow .2s;
  position: relative;
}
.ex-card.is-done {
  border-color: #86efac;
}
:root[data-theme="dark"] .ex-card.is-done {
  border-color: #14532d;
}
.ex-card.is-flagged {
  border-color: #fde047;
}
:root[data-theme="dark"] .ex-card.is-flagged {
  border-color: #713f12;
}

.ex-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 12px;
}
.ex-tags {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 6px;
}
.tag-id {
  font-family: "Fira Code", monospace;
  font-weight: 700;
  font-size: .8rem;
  background: var(--card-sub);
  border: 1px solid var(--line);
  padding: 2px 8px;
  border-radius: 6px;
  color: var(--mute);
}
.tag-level {
  font-size: .78rem;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 6px;
}
.tag-level.cb { background: var(--ok-soft); color: var(--ok); }
.tag-level.tb { background: var(--warn-soft); color: var(--warn); }
.tag-level.nc { background: var(--bad-soft); color: var(--bad); }

.tag-topic {
  font-size: .78rem;
  background: var(--acc-soft);
  color: var(--acc);
  padding: 2px 8px;
  border-radius: 6px;
  font-weight: 600;
}

.ex-actions {
  display: flex;
  gap: 6px;
}
.btn-action {
  border: 1px solid var(--line);
  background: var(--card-sub);
  color: var(--mute);
  padding: 4px 8px;
  border-radius: 6px;
  font-size: .78rem;
  font-weight: 600;
  cursor: pointer;
  transition: .15s;
  display: flex;
  align-items: center;
  gap: 4px;
}
.btn-action:hover { border-color: var(--mute); color: var(--ink); }
.btn-action.active-done { background: var(--ok-soft); color: var(--ok); border-color: var(--ok); }
.btn-action.active-flag { background: var(--warn-soft); color: var(--warn); border-color: var(--warn); }

.ex-title {
  font-size: 1.15rem;
  font-weight: 800;
  margin: 0 0 10px 0;
  color: var(--ink);
}

.ex-problem {
  font-size: .98rem;
  line-height: 1.7;
  padding: 14px 16px;
  background: var(--card-sub);
  border-left: 4px solid var(--acc);
  border-radius: 8px;
  margin-bottom: 14px;
}

/* COLLAPSIBLE ANALYSIS */
.accordion {
  border: 1px solid var(--line);
  border-radius: 8px;
  margin-bottom: 12px;
  overflow: hidden;
}
.acc-header {
  padding: 10px 14px;
  background: var(--card);
  font-size: .88rem;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  user-select: none;
}
.acc-header:hover { background: var(--card-sub); }
.acc-body {
  padding: 12px 14px;
  background: var(--bg);
  font-size: .9rem;
  line-height: 1.6;
  border-top: 1px solid var(--line);
  display: none;
}
.acc-body.open { display: block; }

/* HINTS DISCLOSURE */
.hints-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 14px;
}
.btn-hint {
  padding: 7px 12px;
  border-radius: 8px;
  border: 1px dashed var(--acc);
  background: var(--acc-soft);
  color: var(--acc);
  font-size: .84rem;
  font-weight: 700;
  cursor: pointer;
  transition: .15s;
}
.btn-hint:hover { background: var(--acc); color: #fff; }
.hint-content {
  width: 100%;
  padding: 10px 14px;
  border-radius: 8px;
  background: var(--acc-soft);
  color: var(--ink);
  font-size: .88rem;
  border-left: 3px solid var(--acc);
  display: none;
  margin-top: 6px;
}

/* SOLUTION TOGGLE BUTTON */
.btn-sol-toggle {
  width: 100%;
  padding: 10px;
  border-radius: 10px;
  border: 1px solid var(--line);
  background: var(--card-sub);
  color: var(--ink);
  font-weight: 700;
  font-size: .92rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: .15s;
}
.btn-sol-toggle:hover { background: var(--acc-soft); border-color: var(--acc); color: var(--acc); }

/* SOLUTION BODY */
.sol-body {
  margin-top: 14px;
  padding: 16px;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 10px;
  display: none;
}
.sol-body.open { display: block; }

.sol-step {
  padding: 12px 0;
  border-bottom: 1px dashed var(--line);
  font-size: .95rem;
  line-height: 1.7;
}
.sol-step:last-child { border-bottom: none; }

/* PRO TIPS & PITFALLS */
.box-pro-tips {
  margin-top: 14px;
  padding: 12px 14px;
  border-radius: 8px;
  background: var(--ok-soft);
  border-left: 4px solid var(--ok);
  font-size: .88rem;
  color: var(--ink);
}
.box-pro-tips strong { color: var(--ok); }

.box-pitfalls {
  margin-top: 10px;
  padding: 12px 14px;
  border-radius: 8px;
  background: var(--bad-soft);
  border-left: 4px solid var(--bad);
  font-size: .88rem;
  color: var(--ink);
}
.box-pitfalls strong { color: var(--bad); }

/* DATA TABLES */
.data-table {
  width: 100%;
  max-width: 500px;
  margin: 10px 0;
  border-collapse: collapse;
  font-size: .88rem;
}
.data-table th, .data-table td {
  border: 1px solid var(--line);
  padding: 6px 10px;
  text-align: center;
}
.data-table th { background: var(--card-sub); font-weight: 700; }

/* PERSONAL NOTES */
.notes-sec {
  margin-top: 12px;
}
.notes-btn {
  font-size: .8rem;
  color: var(--mute);
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px 0;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 4px;
}
.notes-btn:hover { color: var(--acc); }
.notes-drawer {
  display: none;
  margin-top: 6px;
}
.notes-area {
  width: 100%;
  padding: 8px 12px;
  border-radius: 8px;
  border: 1px solid var(--line);
  background: var(--card-sub);
  color: var(--ink);
  font-family: inherit;
  font-size: .85rem;
  outline: none;
  resize: vertical;
  min-height: 60px;
}
.notes-area:focus { border-color: var(--acc); background: var(--card); }

/* FLOATING QUICK JUMP BUTTON */
.fab-jump {
  position: fixed;
  bottom: 24px;
  right: 24px;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: var(--acc);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  box-shadow: 0 4px 14px rgba(37, 99, 235, .4);
  cursor: pointer;
  z-index: 40;
  border: none;
  transition: transform .15s;
}
.fab-jump:hover { transform: scale(1.08); }

/* QUICK JUMP MODAL */
.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.5);
  backdrop-filter: blur(4px);
  z-index: 100;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 16px;
}
.modal-overlay.open { display: flex; }
.modal-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  width: 100%;
  max-width: 600px;
  max-height: 85vh;
  display: flex;
  flex-direction: column;
  box-shadow: 0 20px 25px -5px rgba(0,0,0,0.2);
}
.modal-head {
  padding: 16px 20px;
  border-bottom: 1px solid var(--line);
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.modal-head h3 { margin: 0; font-size: 1.1rem; }
.modal-body {
  padding: 16px 20px;
  overflow-y: auto;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(60px, 1fr));
  gap: 8px;
}
.jump-pill {
  padding: 8px;
  text-align: center;
  border-radius: 8px;
  border: 1px solid var(--line);
  background: var(--card-sub);
  color: var(--ink);
  font-family: "Fira Code", monospace;
  font-size: .8rem;
  font-weight: 700;
  cursor: pointer;
  transition: .15s;
}
.jump-pill:hover { border-color: var(--acc); color: var(--acc); }
.jump-pill.is-done { background: var(--ok-soft); border-color: var(--ok); color: var(--ok); }
.jump-pill.is-flagged { background: var(--warn-soft); border-color: var(--warn); color: var(--warn); }

@media (max-width: 640px) {
  .header-wrap { flex-wrap: wrap; }
  .stats-card { flex-direction: column; align-items: stretch; }
  .stats-pills { justify-content: space-between; }
}
</style>
</head>
<body>

<header>
  <div class="header-wrap">
    <a href="#" class="brand">
      <span>📐</span> XSTK • Tự luận
    </a>
    <nav class="nav-links">
      <a href="hoc.html" class="nav-link">📚 Lý thuyết</a>
      <a href="tuluan.html" class="nav-link active">✍️ Tự luận</a>
      <a href="tracnghiem.html" class="nav-link">📝 Trắc nghiệm</a>
      <a href="congthuc.html" class="nav-link">📖 Công thức</a>
    </nav>
    <div class="header-actions">
      <button class="btn-icon" id="theme-btn" title="Đổi giao diện sáng/tối">🌓</button>
    </div>
  </div>
  <div class="progress-bar-wrap">
    <div class="progress-bar-fill" id="global-progress"></div>
  </div>
</header>

<main>
  <!-- STATS BAR -->
  <div class="stats-card">
    <div class="stats-left">
      <h1>Bộ 56 Bài tập Tự luận Chuẩn Barem</h1>
      <p>Bao quát trọn vẹn 7 dạng bài giữa kỳ • Lời giải từng bước chi tiết kèm barem điểm</p>
    </div>
    <div class="stats-pills">
      <div class="stat-pill">
        <div class="num" id="stat-done" style="color:var(--ok);">0 / 56</div>
        <div class="lbl">ĐÃ HOÀN THÀNH</div>
      </div>
      <div class="stat-pill">
        <div class="num" id="stat-flag" style="color:var(--warn);">0</div>
        <div class="lbl">CẦN ÔN LẠI</div>
      </div>
      <div class="stat-pill">
        <div class="num" id="stat-pct" style="color:var(--acc);">0%</div>
        <div class="lbl">TIẾN ĐỘ</div>
      </div>
    </div>
  </div>

  <!-- SEARCH & CONTROLS -->
  <div class="controls-bar">
    <div class="search-box">
      <span class="search-icon">🔍</span>
      <input type="text" id="search-input" class="search-input" placeholder="Tìm theo tên bài, số hiệu (TL7_7), từ khóa (CLT, Chebyshev, Poisson, Bayes)...">
    </div>
  </div>

  <!-- TOPIC PILLS -->
  <div class="topic-nav" id="topic-tabs">
    <button class="topic-btn active" data-tid="0">Tất cả (56 bài)</button>
    <!-- Topics rendered by JS -->
  </div>

  <!-- SECONDARY FILTERS -->
  <div class="filter-row">
    <div class="sub-filters" id="level-filters">
      <button class="sub-filter-btn active" data-lvl="all">Mọi mức độ</button>
      <button class="sub-filter-btn" data-lvl="Cơ bản">🟢 Cơ bản</button>
      <button class="sub-filter-btn" data-lvl="Trung bình">🟡 Trung bình</button>
      <button class="sub-filter-btn" data-lvl="Nâng cao">🔴 Nâng cao</button>
    </div>
    <div class="sub-filters" id="status-filters">
      <button class="sub-filter-btn active" data-status="all">Tất cả trạng thái</button>
      <button class="sub-filter-btn" data-status="done">✓ Đã làm</button>
      <button class="sub-filter-btn" data-status="todo">⏳ Chưa làm</button>
      <button class="sub-filter-btn" data-status="flag">🚩 Cần ôn lại</button>
    </div>
  </div>

  <!-- EXERCISES CONTAINER -->
  <div id="exercises-container">
    <!-- Rendered via JS -->
  </div>
</main>

<!-- FLOATING QUICK JUMP BUTTON -->
<button class="fab-jump" id="fab-jump" title="Mục lục 56 bài tập">📑</button>

<!-- QUICK JUMP MODAL -->
<div class="modal-overlay" id="jump-modal">
  <div class="modal-card">
    <div class="modal-head">
      <h3>Mục lục 56 Bài tập Tự luận</h3>
      <button class="btn-icon" id="close-modal-btn">✕</button>
    </div>
    <div class="modal-body" id="modal-jump-list">
      <!-- Injected by JS -->
    </div>
  </div>
</div>

<script>
// RAW TULUAN DATA EMBEDDED
const TULUAN_DATA = __TULUAN_DATA_PLACEHOLDER__;

// STATE MANAGEMENT WITH LOCALSTORAGE
const STORAGE_KEY = "xstk_tuluan_state_v1";
let userState = {
  done: {},      // { "TL1_1": true, ... }
  flagged: {},   // { "TL1_1": true, ... }
  notes: {},     // { "TL1_1": "text", ... }
  theme: "light"
};

function loadState() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) userState = Object.assign(userState, JSON.parse(raw));
  } catch(e) {}
}

function saveState() {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(userState));
  } catch(e) {}
}

// FILTER STATE
let currentTopicId = 0;
let currentLevel = "all";
let currentStatus = "all";
let searchQuery = "";

// INITIALIZATION
window.addEventListener("DOMContentLoaded", () => {
  loadState();
  initTheme();
  initTopicTabs();
  initEventListeners();
  renderExercises();
  updateStats();
  initMathRendering();
});

// THEME
function initTheme() {
  if (userState.theme === "dark" || (!userState.theme && window.matchMedia("(prefers-color-scheme: dark)").matches)) {
    document.documentElement.setAttribute("data-theme", "dark");
  } else {
    document.documentElement.removeAttribute("data-theme");
  }
  document.getElementById("theme-btn").addEventListener("click", () => {
    const isDark = document.documentElement.getAttribute("data-theme") === "dark";
    if (isDark) {
      document.documentElement.removeAttribute("data-theme");
      userState.theme = "light";
    } else {
      document.documentElement.setAttribute("data-theme", "dark");
      userState.theme = "dark";
    }
    saveState();
  });
}

// TOPIC TABS
function initTopicTabs() {
  const container = document.getElementById("topic-tabs");
  TULUAN_DATA.topics.forEach(t => {
    const btn = document.createElement("button");
    btn.className = "topic-btn";
    btn.dataset.tid = t.id;
    btn.textContent = `Dạng ${t.id}: ${t.short}`;
    container.appendChild(btn);
  });
}

// EVENT LISTENERS
function initEventListeners() {
  // Topic click
  document.getElementById("topic-tabs").addEventListener("click", (e) => {
    if (!e.target.classList.contains("topic-btn")) return;
    document.querySelectorAll(".topic-btn").forEach(b => b.classList.remove("active"));
    e.target.classList.add("active");
    currentTopicId = parseInt(e.target.dataset.tid, 10);
    renderExercises();
  });

  // Level click
  document.getElementById("level-filters").addEventListener("click", (e) => {
    if (!e.target.classList.contains("sub-filter-btn")) return;
    document.querySelectorAll("#level-filters .sub-filter-btn").forEach(b => b.classList.remove("active"));
    e.target.classList.add("active");
    currentLevel = e.target.dataset.lvl;
    renderExercises();
  });

  // Status click
  document.getElementById("status-filters").addEventListener("click", (e) => {
    if (!e.target.classList.contains("sub-filter-btn")) return;
    document.querySelectorAll("#status-filters .sub-filter-btn").forEach(b => b.classList.remove("active"));
    e.target.classList.add("active");
    currentStatus = e.target.dataset.status;
    renderExercises();
  });

  // Search input
  const sInput = document.getElementById("search-input");
  sInput.addEventListener("input", () => {
    searchQuery = sInput.value.trim().toLowerCase();
    renderExercises();
  });

  // Quick Jump Modal
  const modal = document.getElementById("jump-modal");
  document.getElementById("fab-jump").addEventListener("click", () => {
    openJumpModal();
  });
  document.getElementById("close-modal-btn").addEventListener("click", () => {
    modal.classList.remove("open");
  });
  modal.addEventListener("click", (e) => {
    if (e.target === modal) modal.classList.remove("open");
  });
}

// RENDER EXERCISES
function renderExercises() {
  const container = document.getElementById("exercises-container");
  container.innerHTML = "";

  const filtered = TULUAN_DATA.exercises.filter(ex => {
    // Topic filter
    if (currentTopicId !== 0 && ex.topicId !== currentTopicId) return false;
    // Level filter
    if (currentLevel !== "all" && ex.level !== currentLevel) return false;
    // Status filter
    const isDone = !!userState.done[ex.id];
    const isFlag = !!userState.flagged[ex.id];
    if (currentStatus === "done" && !isDone) return false;
    if (currentStatus === "todo" && isDone) return false;
    if (currentStatus === "flag" && !isFlag) return false;
    // Search query
    if (searchQuery) {
      const hay = (ex.id + " " + ex.title + " " + ex.problem + " " + (ex.analysis || "")).toLowerCase();
      if (!hay.includes(searchQuery)) return false;
    }
    return true;
  });

  if (filtered.length === 0) {
    container.innerHTML = `
      <div style="text-align:center; padding: 40px 20px; color: var(--mute); background: var(--card); border-radius: var(--radius); border: 1px solid var(--line);">
        <p style="font-size: 2rem; margin: 0 0 10px;">🔍</p>
        <p style="font-weight: 700; margin: 0 0 6px;">Không tìm thấy bài tập nào phù hợp</p>
        <p style="font-size: .88rem; margin: 0;">Hãy thử điều chỉnh bộ lọc hoặc xóa bớt từ khóa tìm kiếm</p>
      </div>
    `;
    return;
  }

  filtered.forEach(ex => {
    const card = document.createElement("div");
    card.className = "ex-card";
    card.id = "card-" + ex.id;
    if (userState.done[ex.id]) card.classList.add("is-done");
    if (userState.flagged[ex.id]) card.classList.add("is-flagged");

    const lvlClass = ex.level === "Cơ bản" ? "cb" : (ex.level === "Trung bình" ? "tb" : "nc");
    const topicObj = TULUAN_DATA.topics.find(t => t.id === ex.topicId);
    const topicShort = topicObj ? topicObj.short : `Dạng ${ex.topicId}`;

    // Render hints
    const hintsHtml = ex.hints.map((h, i) => `
      <div style="width:100%;">
        <button class="btn-hint" onclick="toggleHint('${ex.id}', ${i})">💡 Gợi ý ${i+1}</button>
        <div class="hint-content" id="hint-${ex.id}-${i}">${h}</div>
      </div>
    `).join("");

    // Render steps
    const stepsHtml = ex.steps.map(s => `
      <div class="sol-step">${s}</div>
    `).join("");

    // User note
    const currentNote = userState.notes[ex.id] || "";

    card.innerHTML = `
      <div class="ex-header">
        <div class="ex-tags">
          <span class="tag-id">${ex.id}</span>
          <span class="tag-level ${lvlClass}">${ex.level}</span>
          <span class="tag-topic">${topicShort}</span>
        </div>
        <div class="ex-actions">
          <button class="btn-action ${userState.done[ex.id] ? 'active-done' : ''}" id="btn-done-${ex.id}" onclick="toggleDone('${ex.id}')">
            ${userState.done[ex.id] ? '✓ Đã xong' : '✓ Hoàn thành'}
          </button>
          <button class="btn-action ${userState.flagged[ex.id] ? 'active-flag' : ''}" id="btn-flag-${ex.id}" onclick="toggleFlag('${ex.id}')">
            ${userState.flagged[ex.id] ? '🚩 Đã lưu' : '🚩 Ôn lại'}
          </button>
        </div>
      </div>

      <h2 class="ex-title">${ex.title}</h2>
      <div class="ex-problem">${ex.problem}</div>

      <!-- ACCORDION ANALYSIS -->
      <div class="accordion">
        <div class="acc-header" onclick="toggleAcc('${ex.id}')">
          <span>💡 Phân tích đề bài & Hướng tư duy</span>
          <span id="acc-icon-${ex.id}">▼</span>
        </div>
        <div class="acc-body" id="acc-body-${ex.id}">${ex.analysis}</div>
      </div>

      <!-- HINTS ROW -->
      <div class="hints-row">
        ${hintsHtml}
      </div>

      <!-- SOLUTION ACCORDION -->
      <button class="btn-sol-toggle" id="btn-sol-${ex.id}" onclick="toggleSolution('${ex.id}')">
        <span>📝 Xem Lời giải chi tiết chuẩn Barem điểm thi</span>
        <span id="sol-icon-${ex.id}">▼</span>
      </button>

      <div class="sol-body" id="sol-body-${ex.id}">
        <div style="font-weight: 800; color: var(--acc); margin-bottom: 12px; font-size: 1rem; border-bottom: 2px solid var(--acc-soft); padding-bottom: 6px;">
          LỜI GIẢI CHI TIẾT TỪNG BƯỚC (BẢO ĐẢM TỐI ĐA ĐIỂM)
        </div>
        ${stepsHtml}

        ${ex.pro_tips ? `
          <div class="box-pro-tips">
            <strong>🎯 MẸO GHI ĐIỂM TUYỆT ĐỐI:</strong><br>${ex.pro_tips}
          </div>
        ` : ''}

        ${ex.pitfalls ? `
          <div class="box-pitfalls">
            <strong>⚠️ BẪY & LỖI HAY BỊ TRỪ ĐIỂM:</strong><br>${ex.pitfalls}
          </div>
        ` : ''}
      </div>

      <!-- PERSONAL NOTES -->
      <div class="notes-sec">
        <button class="notes-btn" onclick="toggleNotes('${ex.id}')">
          <span>✍️ Ghi chú cá nhân</span>
          <span id="note-indicator-${ex.id}">${currentNote ? '(Có ghi chú)' : ''}</span>
        </button>
        <div class="notes-drawer" id="note-drawer-${ex.id}">
          <textarea class="notes-area" id="note-input-${ex.id}" placeholder="Viết lại điểm cần nhớ, công thức riêng hoặc lưu ý cho bài này..." oninput="saveNote('${ex.id}', this.value)">${currentNote}</textarea>
        </div>
      </div>
    `;

    container.appendChild(card);
  });

  // Re-run KaTeX math rendering on freshly inserted cards
  initMathRendering();
}

// TOGGLE ACTIONS
function toggleDone(id) {
  userState.done[id] = !userState.done[id];
  if (!userState.done[id]) delete userState.done[id];
  saveState();
  updateStats();

  const card = document.getElementById("card-" + id);
  const btn = document.getElementById("btn-done-" + id);
  if (card) {
    if (userState.done[id]) {
      card.classList.add("is-done");
      btn.classList.add("active-done");
      btn.textContent = "✓ Đã xong";
    } else {
      card.classList.remove("is-done");
      btn.classList.remove("active-done");
      btn.textContent = "✓ Hoàn thành";
    }
  }
}

function toggleFlag(id) {
  userState.flagged[id] = !userState.flagged[id];
  if (!userState.flagged[id]) delete userState.flagged[id];
  saveState();
  updateStats();

  const card = document.getElementById("card-" + id);
  const btn = document.getElementById("btn-flag-" + id);
  if (card) {
    if (userState.flagged[id]) {
      card.classList.add("is-flagged");
      btn.classList.add("active-flag");
      btn.textContent = "🚩 Đã lưu";
    } else {
      card.classList.remove("is-flagged");
      btn.classList.remove("active-flag");
      btn.textContent = "🚩 Ôn lại";
    }
  }
}

function toggleAcc(id) {
  const body = document.getElementById("acc-body-" + id);
  const icon = document.getElementById("acc-icon-" + id);
  const isOpen = body.classList.toggle("open");
  icon.textContent = isOpen ? "▲" : "▼";
  if (isOpen) initMathRendering();
}

function toggleHint(id, index) {
  const h = document.getElementById(`hint-${id}-${index}`);
  const isShown = h.style.display === "block";
  h.style.display = isShown ? "none" : "block";
  if (!isShown) initMathRendering();
}

function toggleSolution(id) {
  const body = document.getElementById("sol-body-" + id);
  const icon = document.getElementById("sol-icon-" + id);
  const isOpen = body.classList.toggle("open");
  icon.textContent = isOpen ? "▲" : "▼";
  if (isOpen) initMathRendering();
}

function toggleNotes(id) {
  const drawer = document.getElementById("note-drawer-" + id);
  const isOpen = drawer.style.display === "block";
  drawer.style.display = isOpen ? "none" : "block";
}

function saveNote(id, text) {
  if (text.trim()) {
    userState.notes[id] = text;
    document.getElementById("note-indicator-" + id).textContent = "(Có ghi chú)";
  } else {
    delete userState.notes[id];
    document.getElementById("note-indicator-" + id).textContent = "";
  }
  saveState();
}

// UPDATE STATS
function updateStats() {
  const total = TULUAN_DATA.exercises.length;
  const doneCount = Object.keys(userState.done).length;
  const flagCount = Object.keys(userState.flagged).length;
  const pct = Math.round((doneCount / total) * 100);

  document.getElementById("stat-done").textContent = `${doneCount} / ${total}`;
  document.getElementById("stat-flag").textContent = flagCount;
  document.getElementById("stat-pct").textContent = `${pct}%`;
  document.getElementById("global-progress").style.width = `${pct}%`;
}

// QUICK JUMP MODAL
function openJumpModal() {
  const modal = document.getElementById("jump-modal");
  const list = document.getElementById("modal-jump-list");
  list.innerHTML = "";

  TULUAN_DATA.exercises.forEach(ex => {
    const pill = document.createElement("div");
    pill.className = "jump-pill";
    if (userState.done[ex.id]) pill.classList.add("is-done");
    if (userState.flagged[ex.id]) pill.classList.add("is-flagged");
    pill.textContent = ex.id;
    pill.onclick = () => {
      modal.classList.remove("open");
      // reset filters to show this exercise
      currentTopicId = 0;
      currentLevel = "all";
      currentStatus = "all";
      searchQuery = "";
      document.querySelectorAll(".topic-btn").forEach((b, i) => b.classList.toggle("active", i === 0));
      document.querySelectorAll(".sub-filter-btn").forEach(b => b.classList.toggle("active", b.dataset.lvl === "all" || b.dataset.status === "all"));
      document.getElementById("search-input").value = "";
      renderExercises();

      setTimeout(() => {
        const target = document.getElementById("card-" + ex.id);
        if (target) {
          target.scrollIntoView({ behavior: "smooth", block: "start" });
          target.style.boxShadow = "0 0 0 4px var(--acc)";
          setTimeout(() => { target.style.boxShadow = ""; }, 1800);
        }
      }, 100);
    };
    list.appendChild(pill);
  });

  modal.classList.add("open");
}

// KATEX MATH RENDERING
function initMathRendering() {
  if (typeof renderMathInElement === "function") {
    try {
      renderMathInElement(document.body, {
        delimiters: [
          {left: '$$', right: '$$', display: true},
          {left: '$', right: '$', display: false}
        ],
        throwOnError: false
      });
    } catch(e) {
      console.warn("KaTeX render error:", e);
    }
  }
}
</script>
</body>
</html>
"""

# Replace __TULUAN_DATA_PLACEHOLDER__ cleanly with lambda
tuluan_json_str = json.dumps(tuluan_data, ensure_ascii=False)
final_html = re.sub(r'__TULUAN_DATA_PLACEHOLDER__', lambda m: tuluan_json_str, html_template)

with open("site/tuluan.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Generated site/tuluan.html ({len(final_html)} bytes)")
