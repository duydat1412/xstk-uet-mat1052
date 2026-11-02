import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('site/hoc.html', 'r', encoding='utf-8') as f:
    hoc = f.read()

# 1. Update CSS for quiz level badges and cards if not present
new_css = """
/* 3-Level Quiz Badges & Cards */
.quiz-level-badge {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: .8rem;
  font-weight: 700;
  padding: 3px 10px;
  border-radius: 999px;
  margin-bottom: 10px;
}
.level-nhan-biet {
  background: rgba(16, 185, 129, 0.15);
  color: #059669;
  border: 1px solid rgba(16, 185, 129, 0.3);
}
.level-thong-hieu {
  background: rgba(245, 158, 11, 0.15);
  color: #d97706;
  border: 1px solid rgba(245, 158, 11, 0.3);
}
.level-van-dung {
  background: rgba(239, 68, 68, 0.15);
  color: #dc2626;
  border: 1px solid rgba(239, 68, 68, 0.3);
}
.quiz-item-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 18px 20px;
  margin-bottom: 20px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.03);
}
.quiz-congrats-box {
  margin-top: 24px;
  padding: 20px 24px;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(59, 130, 246, 0.1));
  border: 2px solid var(--ok);
  border-radius: 14px;
  text-align: center;
  animation: fadeIn .3s ease;
}
"""

if '.quiz-level-badge' not in hoc:
    hoc = hoc.replace('</style>', new_css + '\n</style>', 1)
    print("Added new CSS for 3-level quiz badges!")

# 2. Update bottom nav button click handlers
hoc = re.sub(r'<button class="btn btn-secondary" id="prevBtn"[^>]*>.*?</button>',
             '<button class="btn btn-secondary" id="prevBtn" onclick="prevSection()">← Phần trước</button>', hoc)
hoc = re.sub(r'<button class="btn btn-primary" id="nextBtn"[^>]*>.*?</button>',
             '<button class="btn btn-primary" id="nextBtn" onclick="nextSection()">Phần tiếp theo →</button>', hoc)
print("Updated bottom nav buttons HTML!")

# 3. Replace the logic script (from <script> after lessons-data to </script>)
pos = hoc.find('id="lessons-data"')
end_data = hoc.find('</script>', pos) + len('</script>')
script_start = hoc.find('<script>', end_data)
script_end = hoc.rfind('</script>')

new_script_logic = """<script>
// ==========================================================================
// TRÌNH ĐIỀU KHIỂN HỌC TẬP TƯƠNG TÁC (SECTION-BY-SECTION & 3-LEVEL QUIZ)
// ==========================================================================

const SUB_TABS = ['theory', 'examples', 'pitfalls', 'quiz'];
const SUB_TAB_NAMES = {
  theory: '1. Lý thuyết',
  examples: '2. Ba Ví dụ',
  pitfalls: '3. Cạm bẫy',
  quiz: '4. Kiểm tra'
};

// STATE
let curLessonIdx = 0;
let curSubTab = 'theory';
let selectedCluster = 'ALL';
let completedLessons = {};
// Store session quiz progress per lesson: { lessonId: { qIdx: chosenOptIdx } }
const lessonQuizAnswers = {};

// Load saved state
try {
  const saved = JSON.parse(localStorage.getItem('xstk_progress') || '{}');
  completedLessons = saved.done || {};
  curLessonIdx = saved.curIdx || 0;
  if (curLessonIdx >= ALL_LESSONS.length || curLessonIdx < 0) curLessonIdx = 0;
} catch(e) {}

function saveProgress() {
  try {
    localStorage.setItem('xstk_progress', JSON.stringify({
      done: completedLessons,
      curIdx: curLessonIdx
    }));
  } catch(e) {}
}

// THEME TOGGLE
const themeBtn = document.getElementById('themeBtn');
function initTheme() {
  const savedTheme = localStorage.getItem('xstk_theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  document.documentElement.setAttribute('data-theme', savedTheme);
}
if (themeBtn) {
  themeBtn.onclick = () => {
    const cur = document.documentElement.getAttribute('data-theme');
    const next = cur === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('xstk_theme', next);
  };
}
initTheme();

// RENDER CLUSTER & LESSON STRIP
function renderClusterTabs() {
  document.querySelectorAll('.cluster-btn').forEach(btn => {
    btn.onclick = () => {
      document.querySelectorAll('.cluster-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      selectedCluster = btn.dataset.c;
      if (selectedCluster !== 'ALL') {
        const firstIdx = ALL_LESSONS.findIndex(l => l.cluster === selectedCluster);
        if (firstIdx !== -1) {
          curLessonIdx = firstIdx;
          curSubTab = 'theory';
        }
      }
      renderLessonsStrip();
      renderCurrentLesson();
    };
  });
}

function renderLessonsStrip() {
  const strip = document.getElementById('lessonsStrip');
  if (!strip) return;
  let html = '';
  ALL_LESSONS.forEach((l, i) => {
    if (selectedCluster === 'ALL' || l.cluster === selectedCluster) {
      const isDone = !!completedLessons[l.id];
      const isActive = i === curLessonIdx;
      html += `<button class="lesson-pill ${isActive ? 'active' : ''} ${isDone ? 'done' : ''}" onclick="goToLesson(${i})">
        ${isDone ? '✓ ' : ''}${l.id}: ${l.title.split(':')[0]}
      </button>`;
    }
  });
  strip.innerHTML = html;
}

// NAVIGATION FUNCTIONS (SECTION BY SECTION)
function goToLesson(idx) {
  if (idx < 0 || idx >= ALL_LESSONS.length) return;
  curLessonIdx = idx;
  curSubTab = 'theory';
  saveProgress();
  renderLessonsStrip();
  renderCurrentLesson();
  window.scrollTo({ top: 120, behavior: 'smooth' });
}

function switchSubTab(tab) {
  if (!SUB_TABS.includes(tab)) return;
  curSubTab = tab;
  renderCurrentLesson();
  // Smooth scroll to lesson content
  const tabContent = document.getElementById('tabContent');
  if (tabContent) {
    const yOffset = -140;
    const y = tabContent.getBoundingClientRect().top + window.pageYOffset + yOffset;
    window.scrollTo({ top: Math.max(0, y), behavior: 'smooth' });
  }
}

function prevSection() {
  const tabIdx = SUB_TABS.indexOf(curSubTab);
  if (tabIdx > 0) {
    // Chuyển về sub-tab trước trong bài hiện tại
    switchSubTab(SUB_TABS[tabIdx - 1]);
  } else {
    // Đang ở tab đầu (theory): chuyển về bài học trước đó nếu có
    if (curLessonIdx > 0) {
      goToLesson(curLessonIdx - 1);
    }
  }
}

function nextSection() {
  const tabIdx = SUB_TABS.indexOf(curSubTab);
  if (tabIdx < SUB_TABS.length - 1) {
    // Chuyển sang sub-tab tiếp theo trong bài hiện tại
    switchSubTab(SUB_TABS[tabIdx + 1]);
  } else {
    // Đang ở tab cuối (quiz): Kiểm tra xem đã hoàn thành kiểm tra chưa
    const l = ALL_LESSONS[curLessonIdx];
    const qList = (l.quizzes && l.quizzes.length) ? l.quizzes : [l.final_quiz];
    const userAnswers = lessonQuizAnswers[l.id] || {};
    const isDone = completedLessons[l.id] || (Object.keys(userAnswers).length >= qList.length);

    if (isDone) {
      if (curLessonIdx < ALL_LESSONS.length - 1) {
        goToLesson(curLessonIdx + 1);
      }
    } else {
      alert(`Vui lòng hoàn thành đủ ${qList.length} câu trắc nghiệm kiểm tra để mở khóa bài học tiếp theo!`);
    }
  }
}

function updateNavButtons() {
  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');
  if (!prevBtn || !nextBtn) return;

  const l = ALL_LESSONS[curLessonIdx];
  const tabIdx = SUB_TABS.indexOf(curSubTab);
  const qList = (l.quizzes && l.quizzes.length) ? l.quizzes : [l.final_quiz];
  const userAnswers = lessonQuizAnswers[l.id] || {};
  const answeredCount = Object.keys(userAnswers).length;
  const isDone = completedLessons[l.id] || (answeredCount >= qList.length);

  // 1. UPDATE PREV BUTTON
  if (tabIdx > 0) {
    prevBtn.disabled = false;
    prevBtn.innerHTML = `← Phần trước: ${SUB_TAB_NAMES[SUB_TABS[tabIdx - 1]]}`;
  } else {
    if (curLessonIdx > 0) {
      prevBtn.disabled = false;
      prevBtn.innerHTML = `← Bài trước (${ALL_LESSONS[curLessonIdx - 1].id})`;
    } else {
      prevBtn.disabled = true;
      prevBtn.innerHTML = `← Bắt đầu khóa học`;
    }
  }

  // 2. UPDATE NEXT BUTTON
  if (tabIdx < SUB_TABS.length - 1) {
    // Vẫn còn các sub-tab tiếp theo trong bài này
    nextBtn.disabled = false;
    nextBtn.className = 'btn btn-primary';
    nextBtn.innerHTML = `Sang phần: ${SUB_TAB_NAMES[SUB_TABS[tabIdx + 1]]} →`;
  } else {
    // Đang ở tab 'quiz' (phần cuối cùng của bài)
    if (!isDone) {
      nextBtn.disabled = true;
      nextBtn.className = 'btn btn-secondary';
      nextBtn.innerHTML = `🔒 Hoàn thành kiểm tra để mở bài tiếp (${answeredCount}/${qList.length})`;
    } else {
      if (curLessonIdx < ALL_LESSONS.length - 1) {
        const nextL = ALL_LESSONS[curLessonIdx + 1];
        nextBtn.disabled = false;
        nextBtn.className = 'btn btn-primary';
        nextBtn.innerHTML = `🎉 Mở khóa bài tiếp theo: ${nextL.id} →`;
      } else {
        nextBtn.disabled = true;
        nextBtn.className = 'btn btn-secondary';
        nextBtn.innerHTML = `🏆 Bạn đã hoàn thành toàn bộ 26 bài học!`;
      }
    }
  }
}

// RENDER CURRENT LESSON
function renderCurrentLesson() {
  const l = ALL_LESSONS[curLessonIdx];
  if (!l) return;

  document.getElementById('clusterBadge').textContent = `Cụm ${l.cluster}`;
  document.getElementById('sourceBadge').textContent = l.sources;
  document.getElementById('lessonTitle').textContent = `${l.id}: ${l.title}`;
  document.getElementById('lessonDesc').textContent = l.desc;

  // Update Progress
  const totalDone = Object.keys(completedLessons).length;
  document.getElementById('statsBadge').textContent = `${totalDone}/${ALL_LESSONS.length} bài`;
  document.getElementById('progressBar').style.width = `${(totalDone / ALL_LESSONS.length) * 100}%`;

  // Update Sub Tabs Active State
  document.querySelectorAll('.sub-tab-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.tab === curSubTab);
  });

  // Render Sub Tab Content
  const container = document.getElementById('tabContent');
  if (curSubTab === 'theory') {
    container.innerHTML = renderTheory(l);
    if (l.widget === 'outlier_widget') initOutlierWidget();
    if (l.widget === 'clt_widget') initCltWidget();
  } else if (curSubTab === 'examples') {
    container.innerHTML = renderExamples(l);
  } else if (curSubTab === 'pitfalls') {
    container.innerHTML = renderPitfalls(l);
  } else if (curSubTab === 'quiz') {
    container.innerHTML = renderQuiz(l);
    attachQuizEvents(l);
  }

  // Update Navigation Buttons dynamically
  updateNavButtons();

  // Render Math with KaTeX
  if (window.renderMathInElement) {
    renderMathInElement(container, {
      delimiters: [
        {left: '$$', right: '$$', display: true},
        {left: '$', right: '$', display: false}
      ],
      throwOnError: false
    });
  }
}

// SUB TAB RENDERERS
function renderTheory(l) {
  let html = '';
  l.steps.forEach((step, idx) => {
    html += `<div class="step-block">
      <h3><span>#${idx + 1}</span> ${step.t}</h3>
      <div>${step.c}</div>
    </div>`;
  });

  // Check for Widget insertion
  if (l.widget === 'outlier_widget') {
    html += `<div class="widget-container" id="outlierWidget">
      <div class="widget-title">🕹️ Widget Tương Tác: Thử Nghiệm Giá Trị Ngoại Lai & Tính Bền Vững</div>
      <p style="font-size: .88rem; color: var(--mute);">Kéo thanh trượt để thay đổi giá trị x (ngoại lai) và quan sát: Trung bình bị kéo lệch vùn vụt, trong khi Trung vị giữ nguyên không đổi!</p>
      <div class="widget-slider-row">
        <span>x = </span>
        <input type="range" id="outlierSlider" min="5" max="100" value="8" step="1">
        <b id="outlierVal" style="font-size: 1.1rem; min-width: 36px;">8</b>
      </div>
      <div class="widget-stat-grid">
        <div class="widget-stat-card">
          <div style="font-size:.8rem;color:var(--mute)">Dãy 5 số liệu</div>
          <div style="font-size:.95rem;font-weight:700;margin-top:4px;">[4, 6, 7, 7, <span id="outlierValCopy">x</span>]</div>
        </div>
        <div class="widget-stat-card">
          <div style="font-size:.8rem;color:var(--mute)">Trung bình (Mean)</div>
          <div id="meanVal" style="font-size:1.25rem;font-weight:800;color:var(--acc);margin-top:4px;">6.4</div>
        </div>
        <div class="widget-stat-card">
          <div style="font-size:.8rem;color:var(--mute)">Trung vị (Median)</div>
          <div id="medianVal" style="font-size:1.25rem;font-weight:800;color:var(--ok);margin-top:4px;">7</div>
        </div>
      </div>
    </div>`;
  } else if (l.widget === 'clt_widget') {
    html += `<div class="widget-container" id="cltWidget">
      <div class="widget-title">🕹️ Widget Mô Phỏng Định Lý Giới Hạn Trung Tâm (CLT)</div>
      <p style="font-size: .88rem; color: var(--mute);">Phân phối gốc là <b>Mũ (Exponential λ=1)</b> cực kỳ lệch phải. Hãy tăng dần cỡ mẫu n từ 1 lên 35 để thấy hình chuông Gauss đối xứng kỳ diệu xuất hiện!</p>
      <div style="display:flex; gap:8px; margin: 12px 0; flex-wrap:wrap;">
        <button class="btn btn-primary" id="cltBtn1" onclick="runClt(1)">Cỡ mẫu n = 1</button>
        <button class="btn btn-secondary" id="cltBtn5" onclick="runClt(5)">Cỡ mẫu n = 5</button>
        <button class="btn btn-secondary" id="cltBtn15" onclick="runClt(15)">Cỡ mẫu n = 15</button>
        <button class="btn btn-secondary" id="cltBtn35" onclick="runClt(35)">Cỡ mẫu n = 35 (CLT)</button>
      </div>
      <div class="clt-hist-wrap">
        <div class="clt-hist-bars" id="cltBars"></div>
      </div>
      <div class="clt-info" id="cltInfo">Đang vẽ phân phối của biến ngẫu nhiên gốc X...</div>
    </div>`;
  }

  return html;
}

function renderExamples(l) {
  let html = '';
  l.examples.forEach((ex, idx) => {
    html += `<div class="ex-card">
      <div class="ex-title">
        <span>Ví dụ ${idx + 1}</span>
        ${ex.t}
      </div>
      <div class="ex-q"><b>Đề bài:</b> ${ex.q}</div>
      <div class="ex-sol"><b>Lời giải chi tiết:</b><br>${ex.sol}</div>
    </div>`;
  });
  return html;
}

function renderPitfalls(l) {
  let html = '';
  l.pitfalls.forEach(p => {
    html += `<div class="pitfall-row">
      <div class="pitfall-col pitfall-bad">
        <b>❌ CÁCH HIỂU SAI / MẤT ĐIỂM:</b><br>${p.bad}
      </div>
      <div class="pitfall-col pitfall-good">
        <b>✔️ CÁCH HIỂU ĐÚNG / ĂN ĐIỂM:</b><br>${p.good}
      </div>
    </div>`;
  });
  return html;
}

// 3-LEVEL QUIZ RENDERER
function renderQuiz(l) {
  const qList = (l.quizzes && l.quizzes.length) ? l.quizzes : [l.final_quiz];
  const userAnswers = lessonQuizAnswers[l.id] || {};
  const answeredCount = Object.keys(userAnswers).length;
  const isAllAnswered = answeredCount >= qList.length;

  let html = `<div class="quiz-container">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;flex-wrap:wrap;gap:8px;">
      <div>
        <h3 style="margin:0;font-size:1.15rem;color:var(--text);font-weight:800;">
          🎯 Bài Kiểm Tra Năng Lực (3 Cấp độ: Nhận biết — Thông hiểu — Vận dụng)
        </h3>
        <p style="margin:4px 0 0;font-size:.88rem;color:var(--mute);">
          Hãy hoàn thành đủ ${qList.length} câu hỏi dưới đây để mở khóa bài học tiếp theo.
        </p>
      </div>
      <span class="badge" id="quizCounterBadge" style="background:var(--acc-soft);color:var(--acc);padding:5px 12px;border-radius:999px;font-weight:700;font-size:.85rem;">
        Tiến độ: ${answeredCount}/${qList.length} câu
      </span>
    </div>`;

  qList.forEach((q, qIdx) => {
    const levelClass = (q.level === 'Nhận biết') ? 'level-nhan-biet' : ((q.level === 'Thông hiểu') ? 'level-thong-hieu' : 'level-van-dung');
    const levelIcon = (q.level === 'Nhận biết') ? '🟢 Cấp độ 1: Nhận biết' : ((q.level === 'Thông hiểu') ? '🟡 Cấp độ 2: Thông hiểu' : '🔴 Cấp độ 3: Vận dụng / Bẫy kinh điển');
    const chosenIdx = userAnswers[qIdx];
    const isAnswered = chosenIdx !== undefined;

    html += `<div class="quiz-item-card" id="quizCard_${qIdx}">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
        <span class="quiz-level-badge ${levelClass}">${levelIcon}</span>
        <span style="font-size:.8rem;color:var(--mute);font-weight:600;">Câu ${qIdx + 1} / ${qList.length}</span>
      </div>
      <div class="quiz-q" style="font-size:1.02rem;margin-bottom:14px;line-height:1.55;">${q.q}</div>
      <div class="quiz-opts" id="quizOpts_${qIdx}">`;

    q.opts.forEach((opt, oIdx) => {
      let optClass = 'quiz-opt';
      let disabledAttr = isAnswered ? 'disabled' : '';
      if (isAnswered) {
        if (oIdx === q.ans) optClass += ' ok';
        else if (oIdx === chosenIdx) optClass += ' no';
      }
      html += `<button class="${optClass}" data-qidx="${qIdx}" data-oidx="${oIdx}" ${disabledAttr}>
        <span style="display:inline-block;width:22px;font-weight:700;">${String.fromCharCode(65 + oIdx)}.</span> ${opt}
      </button>`;
    });

    html += `</div>
      <div id="quizFeedback_${qIdx}">`;
    if (isAnswered) {
      const isCorrect = (chosenIdx === q.ans);
      html += `<div class="feedback-box ${isCorrect ? 'ok' : 'no'}">
        <b>${isCorrect ? '🎉 RẤT XUẤT SẮC! ĐÚNG RỒI!' : '⚠️ CHƯA CHÍNH XÁC!'}</b><br>
        ${!isCorrect ? `Đáp án chính xác: <b>${String.fromCharCode(65 + q.ans)}. ${q.opts[q.ans]}</b><br>` : ''}
        ${typeof q.fb === 'string' ? q.fb : (q.fb[chosenIdx] || '')}
      </div>`;
    }
    html += `</div></div>`;
  });

  // Hộp chúc mừng khi hoàn thành cả 3 câu
  if (isAllAnswered) {
    let correctCount = 0;
    qList.forEach((q, idx) => {
      if (userAnswers[idx] === q.ans) correctCount++;
    });
    html += `<div class="quiz-congrats-box">
      <div style="font-size:1.35rem;font-weight:800;color:var(--ok);margin-bottom:6px;">
        🎉 CHÚC MỪNG BẠN ĐÃ HOÀN THÀNH BÀI KIỂM TRA!
      </div>
      <div style="font-size:.95rem;color:var(--ink);margin-bottom:14px;">
        Bạn đã trả lời đúng <b>${correctCount}/${qList.length}</b> câu hỏi. Bài học <b>${l.id}: ${l.title.split(':')[0]}</b> đã được ghi nhận hoàn thành!
      </div>
      ${curLessonIdx < ALL_LESSONS.length - 1 ? `
        <button class="btn btn-primary" onclick="nextSection()" style="font-size:1rem;padding:10px 22px;">
          Tiếp tục sang bài tiếp theo (${ALL_LESSONS[curLessonIdx + 1].id}) →
        </button>
      ` : `
        <div style="display:inline-block;background:var(--ok);color:#fff;font-weight:700;padding:8px 18px;border-radius:999px;">
          🏆 Bạn đã hoàn thành toàn bộ 26 bài học trong chương trình!
        </div>
      `}
    </div>`;
  }

  html += `</div>`;
  return html;
}

function attachQuizEvents(l) {
  const qList = (l.quizzes && l.quizzes.length) ? l.quizzes : [l.final_quiz];
  if (!lessonQuizAnswers[l.id]) {
    lessonQuizAnswers[l.id] = {};
  }

  document.querySelectorAll('.quiz-opt').forEach(btn => {
    btn.onclick = () => {
      const qIdx = +btn.dataset.qidx;
      const oIdx = +btn.dataset.oidx;
      const q = qList[qIdx];
      if (!q) return;

      // Save answer
      lessonQuizAnswers[l.id][qIdx] = oIdx;
      const isCorrect = (oIdx === q.ans);

      // Disable buttons for this question & highlight
      const card = document.getElementById(`quizCard_${qIdx}`);
      if (card) {
        card.querySelectorAll('.quiz-opt').forEach(b => {
          b.disabled = true;
          const curO = +b.dataset.oidx;
          if (curO === q.ans) b.classList.add('ok');
          else if (curO === oIdx) b.classList.add('no');
        });

        // Show feedback
        const fbEl = document.getElementById(`quizFeedback_${qIdx}`);
        if (fbEl) {
          fbEl.innerHTML = `<div class="feedback-box ${isCorrect ? 'ok' : 'no'}">
            <b>${isCorrect ? '🎉 RẤT XUẤT SẮC! ĐÚNG RỒI!' : '⚠️ CHƯA CHÍNH XÁC!'}</b><br>
            ${!isCorrect ? `Đáp án chính xác: <b>${String.fromCharCode(65 + q.ans)}. ${q.opts[q.ans]}</b><br>` : ''}
            ${typeof q.fb === 'string' ? q.fb : (q.fb[oIdx] || '')}
          </div>`;
          // Render math in feedback if any
          if (window.renderMathInElement) {
            renderMathInElement(fbEl, {
              delimiters: [
                {left: '$$', right: '$$', display: true},
                {left: '$', right: '$', display: false}
              ],
              throwOnError: false
            });
          }
        }
      }

      // Check overall quiz completion
      const answeredCount = Object.keys(lessonQuizAnswers[l.id]).length;
      const counterEl = document.getElementById('quizCounterBadge');
      if (counterEl) {
        counterEl.textContent = `Tiến độ: ${answeredCount}/${qList.length} câu`;
      }

      // If finished all 3 questions
      if (answeredCount >= qList.length) {
        completedLessons[l.id] = true;
        saveProgress();
        renderLessonsStrip();
        const totalDone = Object.keys(completedLessons).length;
        document.getElementById('statsBadge').textContent = `${totalDone}/${ALL_LESSONS.length} bài`;
        document.getElementById('progressBar').style.width = `${(totalDone / ALL_LESSONS.length) * 100}%`;

        // Re-render quiz to show congrats box
        const container = document.getElementById('tabContent');
        if (container) {
          container.innerHTML = renderQuiz(l);
          attachQuizEvents(l);
          if (window.renderMathInElement) {
            renderMathInElement(container, {
              delimiters: [
                {left: '$$', right: '$$', display: true},
                {left: '$', right: '$', display: false}
              ],
              throwOnError: false
            });
          }
        }
      }

      // Update bottom nav buttons immediately
      updateNavButtons();
    };
  });
}

// SETUP SUB TAB CLICK EVENTS
document.querySelectorAll('.sub-tab-btn').forEach(btn => {
  btn.onclick = () => {
    switchSubTab(btn.dataset.tab);
  };
});

// INTERACTIVE WIDGET 1: OUTLIER SLIDER
function initOutlierWidget() {
  const slider = document.getElementById('outlierSlider');
  const valText = document.getElementById('outlierVal');
  const valCopy = document.getElementById('outlierValCopy');
  const meanText = document.getElementById('meanVal');
  const medianText = document.getElementById('medianVal');
  if (!slider) return;

  function update() {
    const x = +slider.value;
    if (valText) valText.textContent = x;
    if (valCopy) valCopy.textContent = x;
    const arr = [4, 6, 7, 7, x];
    const mean = (4 + 6 + 7 + 7 + x) / 5;
    arr.sort((a, b) => a - b);
    const median = arr[2];

    if (meanText) {
      meanText.textContent = mean.toFixed(1);
      if (x > 20) {
        meanText.style.color = 'var(--bad)';
      } else {
        meanText.style.color = 'var(--acc)';
      }
    }
    if (medianText) medianText.textContent = median;
  }
  slider.oninput = update;
  update();
}

// INTERACTIVE WIDGET 2: CLT SIMULATOR
function initCltWidget() {
  window.runClt = function(n) {
    document.querySelectorAll('#cltWidget .btn').forEach(b => {
      b.classList.remove('btn-primary');
      b.classList.add('btn-secondary');
    });
    const activeBtn = document.getElementById(`cltBtn${n}`);
    if (activeBtn) {
      activeBtn.classList.remove('btn-secondary');
      activeBtn.classList.add('btn-primary');
    }

    const reps = 1500;
    const bins = 28;
    const counts = new Array(bins).fill(0);
    let sumMeans = 0;

    for (let i = 0; i < reps; i++) {
      let sampleSum = 0;
      // Exponential distribution samples
      for (let k = 0; k < n; k++) {
        sampleSum -= Math.log(1 - Math.random());
      }
      const sampleMean = sampleSum / n;
      sumMeans += sampleMean;
      const binIdx = Math.min(bins - 1, Math.max(0, Math.floor((sampleMean / 2.5) * bins)));
      counts[binIdx]++;
    }

    const maxCount = Math.max(...counts);
    let barsHtml = '';
    counts.forEach(c => {
      const pct = (c / maxCount) * 100;
      barsHtml += `<i style="height: ${Math.max(3, pct)}%;"></i>`;
    });

    const barsEl = document.getElementById('cltBars');
    if (barsEl) barsEl.innerHTML = barsHtml;
    const avg = (sumMeans / reps).toFixed(2);
    const theorySd = (1 / Math.sqrt(n)).toFixed(2);
    const infoEl = document.getElementById('cltInfo');
    if (infoEl) {
      infoEl.innerHTML = `Trung bình mẫu mô phỏng ≈ <b>${avg}</b>. Sai số lý thuyết σ/√n = 1/√${n} ≈ <b>${theorySd}</b>. ${n >= 15 ? 'Đồ thị đã thành hình chuông Gauss đối xứng!' : 'Đồ thị vẫn còn bị lệch phải do cỡ mẫu nhỏ.'}`;
    }
  };

  runClt(1);
}

// AUTO TRIGGER KATEX ONCE LOADED
window.addEventListener('load', () => {
  if (window.renderMathInElement) {
    const container = document.getElementById('tabContent');
    if (container) {
      renderMathInElement(container, {
        delimiters: [
          {left: '$$', right: '$$', display: true},
          {left: '$', right: '$', display: false}
        ],
        throwOnError: false
      });
    }
  }
});

// INIT APP
renderClusterTabs();
renderLessonsStrip();
renderCurrentLesson();
</script>"""

# Replace the script block cleanly
hoc = hoc[:script_start] + new_script_logic + hoc[script_end + len('</script>'):]

with open('site/hoc.html', 'w', encoding='utf-8') as out:
    out.write(hoc)

print("Updated site/hoc.html successfully with section-by-section navigation and 3-level quiz!")
