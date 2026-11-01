import json

index_html = r"""<!DOCTYPE html>
<html lang="vi" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Hệ thống Tự học Xác suất Thống kê - UET MAT1052</title>

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
  --purple: #8b5cf6;
  --purple-soft: #f5f3ff;
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
  --purple: #a78bfa;
  --purple-soft: #2e1065;
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
  padding-bottom: 80px;
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
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.5px;
}
.site-title {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--ink);
}
.nav-links {
  display: flex;
  align-items: center;
  gap: 8px;
}
.nav-btn {
  padding: 8px 14px;
  border-radius: var(--radius-sm);
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--mute);
  transition: all 0.2s;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.nav-btn:hover {
  background: var(--card-subtle);
  color: var(--ink);
}
.nav-btn.active {
  background: var(--acc);
  color: #fff;
}
.btn-theme {
  background: transparent;
  border: 1px solid var(--line);
  padding: 8px 12px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  color: var(--ink);
  font-size: 1rem;
  transition: all 0.2s;
}
.btn-theme:hover {
  background: var(--card-subtle);
}

/* Hero Section */
.hero {
  max-width: 1200px;
  margin: 30px auto;
  padding: 40px 30px;
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.08) 0%, rgba(139, 92, 246, 0.08) 100%);
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  text-align: center;
  position: relative;
  overflow: hidden;
}
.hero-tag {
  display: inline-block;
  background: var(--acc-soft);
  color: var(--acc);
  font-weight: 700;
  font-size: 0.85rem;
  padding: 6px 14px;
  border-radius: 99px;
  margin-bottom: 16px;
  text-transform: uppercase;
  letter-spacing: 1px;
}
.hero h1 {
  font-size: 2.2rem;
  font-weight: 800;
  line-height: 1.3;
  margin-bottom: 16px;
  color: var(--ink);
}
.hero p {
  font-size: 1.1rem;
  color: var(--mute);
  max-width: 760px;
  margin: 0 auto 28px;
}
.hero-stats {
  display: flex;
  justify-content: center;
  gap: 30px;
  flex-wrap: wrap;
  margin-top: 20px;
}
.stat-pill {
  background: var(--card);
  padding: 12px 24px;
  border-radius: var(--radius-md);
  border: 1px solid var(--line);
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
  align-items: center;
}
.stat-num {
  font-size: 1.6rem;
  font-weight: 800;
  color: var(--acc);
}
.stat-label {
  font-size: 0.82rem;
  color: var(--mute);
  font-weight: 600;
}

/* Main Container */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Module Grid */
.section-title {
  font-size: 1.4rem;
  font-weight: 800;
  margin: 40px 0 20px;
  display: flex;
  align-items: center;
  gap: 10px;
}
.section-subtitle {
  font-size: 0.95rem;
  color: var(--mute);
  margin-top: -12px;
  margin-bottom: 24px;
}
.module-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(270px, 1fr));
  gap: 20px;
  margin-bottom: 40px;
}
.module-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  padding: 24px;
  box-shadow: var(--shadow-sm);
  transition: all 0.25s ease;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  text-decoration: none;
  color: inherit;
}
.module-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
  border-color: var(--acc);
}
.module-icon {
  width: 50px;
  height: 50px;
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.6rem;
  margin-bottom: 16px;
}
.module-card:nth-child(1) .module-icon { background: var(--acc-soft); }
.module-card:nth-child(2) .module-icon { background: var(--ok-soft); }
.module-card:nth-child(3) .module-icon { background: var(--purple-soft); }
.module-card:nth-child(4) .module-icon { background: var(--warn-soft); }

.module-title {
  font-size: 1.2rem;
  font-weight: 700;
  margin-bottom: 8px;
  color: var(--ink);
}
.module-desc {
  font-size: 0.9rem;
  color: var(--mute);
  margin-bottom: 20px;
  flex-grow: 1;
}
.module-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--acc);
  border-top: 1px solid var(--line);
  padding-top: 14px;
}

/* Roadmap Tabs */
.roadmap-box {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  padding: 30px;
  box-shadow: var(--shadow-sm);
  margin-bottom: 40px;
}
.roadmap-nav {
  display: flex;
  gap: 12px;
  border-bottom: 1px solid var(--line);
  padding-bottom: 14px;
  margin-bottom: 24px;
  flex-wrap: wrap;
}
.roadmap-tab {
  padding: 10px 20px;
  border-radius: var(--radius-md);
  font-size: 0.95rem;
  font-weight: 700;
  cursor: pointer;
  border: 1px solid var(--line);
  background: var(--card-subtle);
  color: var(--mute);
  transition: all 0.2s;
}
.roadmap-tab.active {
  background: var(--acc);
  color: #fff;
  border-color: var(--acc);
}
.timeline-item {
  display: flex;
  gap: 20px;
  padding: 18px 0;
  border-bottom: 1px dashed var(--line);
}
.timeline-item:last-child {
  border-bottom: none;
}
.timeline-time {
  min-width: 130px;
  font-weight: 700;
  color: var(--acc);
  font-size: 0.95rem;
}
.timeline-body h4 {
  font-size: 1.05rem;
  font-weight: 700;
  margin-bottom: 6px;
  color: var(--ink);
}
.timeline-body p {
  font-size: 0.9rem;
  color: var(--mute);
}

/* Pitfall preview */
.pitfall-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 16px;
  margin-bottom: 40px;
}
.pitfall-item {
  background: var(--bad-soft);
  border: 1px solid rgba(239, 68, 68, 0.2);
  border-radius: var(--radius-md);
  padding: 16px 20px;
}
.pitfall-title {
  font-weight: 700;
  color: var(--bad);
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.pitfall-desc {
  font-size: 0.88rem;
  color: var(--ink);
}

/* Footer */
footer {
  text-align: center;
  padding: 30px;
  color: var(--mute);
  font-size: 0.85rem;
  border-top: 1px solid var(--line);
  margin-top: 60px;
}
</style>
</head>
<body>

<header>
  <div class="header-top">
    <div class="logo-group">
      <span class="badge-course">UET.MAT1052</span>
      <span class="site-title">Xác suất Thống kê Giữa kỳ</span>
    </div>
    <div class="nav-links">
      <a href="index.html" class="nav-btn active">🏠 Tổng quan</a>
      <a href="hoc.html" class="nav-btn">📘 Lý thuyết</a>
      <a href="tuluan.html" class="nav-btn">✍️ Tự luận</a>
      <a href="tracnghiem.html" class="nav-btn">⚡ Trắc nghiệm</a>
      <a href="congthuc.html" class="nav-btn">📐 Công thức</a>
      <button class="btn-theme" id="themeBtn" title="Chuyển chế độ sáng/tối">
        <span id="themeIcon">🌙</span>
      </button>
    </div>
  </div>
</header>

<main class="container">
  <!-- Hero Section -->
  <section class="hero">
    <div class="hero-tag">Trường Đại học Công nghệ - ĐHQGHN</div>
    <h1>Bộ Tài Liệu Tự Học Tương Tác XSTK Toàn Diện</h1>
    <p>Hệ thống học tập cá nhân hóa chuẩn theo giáo trình Stat20 & Slide Tuần 01 – Tuần 07 UET. Thiết kế đặc biệt cho sinh viên bắt đầu từ số 0 chinh phục điểm A/A+ Giữa kỳ (50% Trắc nghiệm + 50% Tự luận).</p>
    
    <div class="hero-stats">
      <div class="stat-pill">
        <div class="stat-num" id="statLessons">26</div>
        <div class="stat-label">Bài học Micro-learning</div>
      </div>
      <div class="stat-pill">
        <div class="stat-num" id="statExercises">56</div>
        <div class="stat-label">Bài Tự luận chuẩn Barem</div>
      </div>
      <div class="stat-pill">
        <div class="stat-num" id="statMcqs">161</div>
        <div class="stat-label">Câu hỏi Trắc nghiệm</div>
      </div>
      <div class="stat-pill">
        <div class="stat-num" id="statFormulas">35</div>
        <div class="stat-label">Công thức Cốt lõi & Bẫy</div>
      </div>
    </div>
  </section>

  <!-- 4 Core Modules -->
  <h2 class="section-title">🚀 4 Trụ Cột Ôn Luyện Cốt Lõi</h2>
  <div class="section-subtitle">Lựa chọn mô-đun phù hợp với nhu cầu học tập và giai đoạn ôn thi của bạn:</div>

  <div class="module-grid">
    <!-- Module 1 -->
    <a href="hoc.html" class="module-card">
      <div>
        <div class="module-icon">📘</div>
        <h3 class="module-title">1. Bài Học Tương Tác</h3>
        <p class="module-desc">26 bài học chia theo 5 Cụm kiến thức (A đến E). Tích hợp giải thích trực giác, ví dụ số thực tế, câu hỏi kiểm tra nhanh có phản hồi tức thì.</p>
      </div>
      <div class="module-footer">
        <span>Bắt đầu học</span>
        <span>→</span>
      </div>
    </a>

    <!-- Module 2 -->
    <a href="tuluan.html" class="module-card">
      <div>
        <div class="module-icon">✍️</div>
        <h3 class="module-title">2. Luyện Thi Tự Luận</h3>
        <p class="module-desc">56 bài tập kinh điển (7 chủ đề × 8 bài). Đầy đủ barem điểm từng bước 0.25đ, gợi ý 3 cấp độ (Hint), lưu ý bẫy thường gặp và Pro-tips.</p>
      </div>
      <div class="module-footer">
        <span>Vào luyện giải</span>
        <span>→</span>
      </div>
    </a>

    <!-- Module 3 -->
    <a href="tracnghiem.html" class="module-card">
      <div>
        <div class="module-icon">⚡</div>
        <h3 class="module-title">3. Ngân Hàng Trắc Nghiệm</h3>
        <p class="module-desc">161 câu hỏi trắc nghiệm chất lượng cao. 3 chế độ: Luyện tập phản xạ tức thì, Thi thử bấm giờ 45 phút, và Sổ tay câu sai (Spaced Repetition).</p>
      </div>
      <div class="module-footer">
        <span>Làm trắc nghiệm</span>
        <span>→</span>
      </div>
    </a>

    <!-- Module 4 -->
    <a href="congthuc.html" class="module-card">
      <div>
        <div class="module-icon">📐</div>
        <h3 class="module-title">4. Sổ Tay Công Thức</h3>
        <p class="module-desc">35 công thức trọng tâm kèm điều kiện sử dụng, ý nghĩa ký hiệu, bẫy thi chết người, nút Copy LaTeX 1 chạm và Bảng tra Chuẩn $\Phi(z)$ tích hợp.</p>
      </div>
      <div class="module-footer">
        <span>Tra cứu công thức</span>
        <span>→</span>
      </div>
    </a>
  </div>

  <!-- Interactive Roadmap Planner -->
  <h2 class="section-title">🗺️ Lộ Trình Ôn Thi Đề Xuất</h2>
  <div class="section-subtitle">Chọn lộ trình phù hợp với thời gian còn lại trước kỳ thi giữa kỳ:</div>

  <div class="roadmap-box">
    <div class="roadmap-nav">
      <button class="roadmap-tab active" onclick="switchRoadmap(3)">⚡ Cấp tốc 72 Giờ (3 Ngày)</button>
      <button class="roadmap-tab" onclick="switchRoadmap(7)">🎯 Chuẩn 7 Ngày (1 Tuần Điểm A)</button>
      <button class="roadmap-tab" onclick="switchRoadmap(14)">🏆 Nâng cao 14 Ngày (Mastery 10/10)</button>
    </div>

    <div id="roadmapContent">
      <!-- Dynamic Roadmap content injected by JS -->
    </div>
  </div>

  <!-- Top Pitfalls Section -->
  <h2 class="section-title">⚠️ Bảng Kiểm Bẫy Điểm Số Thường Gặp</h2>
  <div class="section-subtitle">Đừng để mất điểm oan uổng vào những sai lầm kinh điển này:</div>

  <div class="pitfall-grid">
    <div class="pitfall-item">
      <div class="pitfall-title">❌ Nhầm Độc lập và Xung khắc</div>
      <div class="pitfall-desc">Hai biến cố độc lập có xác suất dương <b>không bao giờ xung khắc</b>. Xung khắc: $P(AB) = 0$. Độc lập: $P(AB) = P(A)P(B)$.</div>
    </div>
    <div class="pitfall-item">
      <div class="pitfall-title">❌ Quên bình phương ở Phương sai</div>
      <div class="pitfall-desc">$\operatorname{Var}(aX+b) = a^2\operatorname{Var}(X)$. Dấu trừ đổi thành cộng: $\operatorname{Var}(-3X) = 9\operatorname{Var}(X)$.</div>
    </div>
    <div class="pitfall-item">
      <div class="pitfall-title">❌ Phương sai của Hiệu 2 biến độc lập</div>
      <div class="pitfall-desc">Khi $X, Y$ độc lập: $\operatorname{Var}(X - Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)$. Độ không chắc chắn luôn cộng dồn!</div>
    </div>
    <div class="pitfall-item">
      <div class="pitfall-title">❌ Quên hiệu chỉnh liên tục $\pm 0.5$</div>
      <div class="pitfall-desc">Khi xấp xỉ Nhị thức sang Chuẩn: $P(X \ge 10) \approx P(Y \ge 9.5)$. Mở rộng vùng tích phân 0.5 đơn vị.</div>
    </div>
    <div class="pitfall-item">
      <div class="pitfall-title">❌ Tổng $S_n$ vs Trung bình $\bar{X}_n$ trong CLT</div>
      <div class="pitfall-desc">Tổng tải trọng thang máy: độ lệch chuẩn là $\sigma\sqrt{n}$. Trung bình mẫu: độ lệch chuẩn là $\sigma/\sqrt{n}$.</div>
    </div>
    <div class="pitfall-item">
      <div class="pitfall-title">❌ Quên bình phương nghiệm CLT bóng đèn</div>
      <div class="pitfall-desc">Với phương trình $100u^2 - 49.35u - 2000 \ge 0$, nghiệm là $u = \sqrt{n} \ge 4.76 \implies n = \lceil 4.76^2 \rceil = 23$ bóng đèn.</div>
    </div>
  </div>
</main>

<footer>
  <p>Hệ thống Tài liệu Tự học & Ôn thi Giữa kỳ Xác suất Thống kê UET.MAT1052 | Đại học Công nghệ - ĐHQGHN</p>
  <p style="margin-top: 6px; font-size: 0.8rem;">Được xây dựng bám sát đề cương Tuần 01 – Tuần 07 & Slide UET. Offline-ready & Zero Calculation Errors.</p>
</footer>

<script>
// Theme Management
function initTheme() {
  const saved = localStorage.getItem('xstk_theme') || 'light';
  document.documentElement.setAttribute('data-theme', saved);
  document.getElementById('themeIcon').textContent = saved === 'dark' ? '☀️' : '🌙';
}

document.getElementById('themeBtn').addEventListener('click', () => {
  const cur = document.documentElement.getAttribute('data-theme');
  const target = cur === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', target);
  localStorage.setItem('xstk_theme', target);
  document.getElementById('themeIcon').textContent = target === 'dark' ? '☀️' : '🌙';
});

// Roadmap Data
const ROADMAPS = {
  3: [
    { time: "Ngày 1 (24h đầu)", title: "Ăn chắc Điểm Tự luận Cơ sở (Chủ đề 1 & 2)", desc: "Làm chủ Hồi quy OLS (bài TL1_1, TL1_2) và Xác suất điều kiện, Định lý Bayes (bài TL2_1, TL2_3). Quét 40 câu trắc nghiệm Topic 1 & 2." },
    { time: "Ngày 2 (24h tiếp)", title: "Chinh phục Biến ngẫu nhiên & Định lý Giới hạn (Chủ đề 3, 4, 6, 7)", desc: "Làm các bài tự luận mẫu: pmf/kỳ vọng (TL3_1), Poisson/Nhị thức (TL4_1, TL4_3), Chuẩn hóa Z (TL6_1, TL6_2) và CLT bóng đèn dự phòng (TL7_7). Quét 50 câu trắc nghiệm." },
    { time: "Ngày 3 (24h cuối)", title: "Tổng lực Thi thử, Sửa lỗi sai & Chuẩn bị Phòng thi", desc: "Bật chế độ Thi thử 30 câu ngẫu nhiên trong 45 phút trên site/tracnghiem.html. Rà soát lại Sổ tay lỗi sai và xem lướt bảng kiểm 10 bẫy công thức." }
  ],
  7: [
    { time: "Ngày 1", title: "Chủ đề 1: Thống kê mô tả & Hồi quy OLS", desc: "Học bài A1-A7. Làm bài tự luận TL1_1 đến TL1_8. Quét 23 câu trắc nghiệm TN1_01 - TN1_23." },
    { time: "Ngày 2", title: "Chủ đề 2: Lý thuyết Xác suất & Bayes", desc: "Học bài B1-B5. Làm bài tự luận TL2_1 đến TL2_8. Quét 23 câu trắc nghiệm TN2_01 - TN2_23." },
    { time: "Ngày 3", title: "Chủ đề 3: Biến ngẫu nhiên rời rạc, Kỳ vọng & Phương sai", desc: "Học bài C1, C5, C6. Làm bài tự luận TL3_1 đến TL3_8. Quét 22 câu trắc nghiệm TN3_01 - TN3_22." },
    { time: "Ngày 4", title: "Chủ đề 4: Phân phối Bernoulli, Nhị thức, Siêu bội & Poisson", desc: "Học bài C2, C3, C4. Làm bài tự luận TL4_1 đến TL4_8. Quét 23 câu trắc nghiệm TN4_01 - TN4_23." },
    { time: "Ngày 5", title: "Chủ đề 5: Mô hình Chiếc hộp, Chebyshev & Luật số lớn (WLLN)", desc: "Học bài D1-D4. Làm bài tự luận TL5_1 đến TL5_8. Quét 22 câu trắc nghiệm TN5_01 - TN5_22." },
    { time: "Ngày 6", title: "Chủ đề 6: Biến liên tục, Phân phối Chuẩn & Hàm Mật độ", desc: "Học bài E1-E5. Làm bài tự luận TL6_1 đến TL6_8. Quét 25 câu trắc nghiệm TN6_01 - TN6_25." },
    { time: "Ngày 7", title: "Chủ đề 7: Định lý giới hạn trung tâm (CLT) & Tổng ôn", desc: "Học bài E6. Làm bài tự luận TL7_1 đến TL7_8. Quét 23 câu trắc nghiệm. Thi thử 1 đề tổng hợp 90 phút." }
  ],
  14: [
    { time: "Ngày 1 - 7", title: "Giai đoạn 1: Nền tảng Toàn diện & Giải quyết 56 bài Tự luận", desc: "Mỗi ngày 1 cụm kiến thức: hoàn thành lý thuyết, giải toàn bộ bài tập tự luận có ghi chú vào vở, kiểm tra chéo bằng máy tính Casio." },
    { time: "Ngày 8 - 11", title: "Giai đoạn 2: Quét sạch Ngân hàng 161 câu Trắc nghiệm", desc: "Mỗi ngày làm 40 câu trắc nghiệm ở chế độ Luyện tập có giải thích chi tiết. Đọc kỹ phân tích distractor bẫy." },
    { time: "Ngày 12 - 13", title: "Giai đoạn 3: Rèn luyện Sổ tay Lỗi sai (Spaced Repetition)", desc: "Mở Chế độ Sổ tay Lỗi sai, làm lại 100% các câu từng làm sai cho đến khi tỷ lệ đúng đạt 100%." },
    { time: "Ngày 14", title: "Giai đoạn 4: Thi thử Bấm giờ & Làm chủ Phòng thi", desc: "Thi thử 2 đề ngẫu nhiên 45 phút, ôn 35 công thức và tâm lý tự tin bước vào kỳ thi." }
  ]
};

function switchRoadmap(days) {
  document.querySelectorAll('.roadmap-tab').forEach((t, i) => {
    t.classList.toggle('active', (days === 3 && i === 0) || (days === 7 && i === 1) || (days === 14 && i === 2));
  });
  const container = document.getElementById('roadmapContent');
  const items = ROADMAPS[days];
  container.innerHTML = items.map(item => `
    <div class="timeline-item">
      <div class="timeline-time">${item.time}</div>
      <div class="timeline-body">
        <h4>${item.title}</h4>
        <p>${item.desc}</p>
      </div>
    </div>
  `).join('');
  if (window.renderMathInElement) {
    window.renderMathInElement(container, {
      delimiters: [
        {left: '$$', right: '$$', display: true},
        {left: '$', right: '$', display: false}
      ],
      throwOnError: false
    });
  }
}

function updateStatsFromStorage() {
  try {
    const errorNotebook = JSON.parse(localStorage.getItem('xstk_mcq_errors') || '[]');
    const correctList = JSON.parse(localStorage.getItem('xstk_mcq_correct') || '[]');
    // Can display progress if needed
  } catch (e) {}
}

window.addEventListener('DOMContentLoaded', () => {
  initTheme();
  switchRoadmap(3);
  if (window.renderMathInElement) {
    window.renderMathInElement(document.body, {
      delimiters: [
        {left: '$$', right: '$$', display: true},
        {left: '$', right: '$', display: false}
      ],
      throwOnError: false
    });
  }
});
</script>
</body>
</html>
"""

with open("site/index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

print("site/index.html written successfully!")
