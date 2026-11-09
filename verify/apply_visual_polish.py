import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def polish_course_file(filepath, course_code, course_name, course_id, badge_icon):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Ensure Be Vietnam Pro & Fira Code font link is present
    font_link = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&family=Fira+Code:wght@400;600&display=swap">'
    if 'family=Be+Vietnam+Pro' not in content:
        content = content.replace('<head>', '<head>\n' + font_link, 1)

    # 2. Refined Global CSS & Tokens (Impeccable craft floor)
    craft_floor_css = '''
/* ==========================================================================
   IMPECCABLE CRAFT FLOOR: DESIGN TOKENS & BROWSER SURFACES
   ========================================================================== */
::selection {
  background: var(--acc-soft);
  color: var(--acc);
}
* {
  scrollbar-width: thin;
  scrollbar-color: var(--line) transparent;
}
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}
::-webkit-scrollbar-track {
  background: transparent;
}
::-webkit-scrollbar-thumb {
  background: var(--line);
  border-radius: 9999px;
}
::-webkit-scrollbar-thumb:hover {
  background: var(--mute);
}
:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}
.tree-badge-total, .tree-folder-badge, .stat-num, .step-pill, .badge-course {
  font-variant-numeric: tabular-nums;
}
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
'''
    if 'IMPECCABLE CRAFT FLOOR' not in content:
        content = content.replace('* { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }',
                                '* { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }\n' + craft_floor_css, 1)

    # 3. Polish Sub-Tabs Stepper into modern segmented control
    old_sub_tabs = '''.sub-tabs {
  display: flex;
  gap: 8px;
  border-bottom: 2px solid var(--line);
  margin-bottom: 20px;
}
.sub-tab-btn {
  padding: 10px 14px;
  background: none;
  border: none;
  border-bottom: 2px solid transparent;
  margin-bottom: -2px;
  color: var(--mute);
  font-weight: 700;
  font-size: .92rem;
  cursor: pointer;
  transition: .15s;
}
.sub-tab-btn:hover { color: var(--ink); }
.sub-tab-btn.active {
  color: var(--acc);
  border-bottom-color: var(--acc);
}'''

    new_sub_tabs = '''.sub-tabs {
  display: inline-flex;
  gap: 4px;
  background: var(--card-sub);
  border: 1px solid var(--line);
  padding: 4px;
  border-radius: 12px;
  margin-bottom: 24px;
  max-width: 100%;
  overflow-x: auto;
  scrollbar-width: none;
}
.sub-tabs::-webkit-scrollbar { display: none; }
.sub-tab-btn {
  padding: 8px 16px;
  background: transparent;
  border: 1px solid transparent;
  border-radius: 8px;
  color: var(--mute);
  font-weight: 600;
  font-size: 0.88rem;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1);
}
.sub-tab-btn:hover {
  color: var(--ink);
  background: rgba(0, 0, 0, 0.03);
}
:root[data-theme="dark"] .sub-tab-btn:hover {
  background: rgba(255, 255, 255, 0.04);
}
.sub-tab-btn.active {
  color: var(--acc);
  background: var(--card);
  border-color: var(--line);
  font-weight: 700;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
}'''

    if old_sub_tabs in content:
        content = content.replace(old_sub_tabs, new_sub_tabs, 1)

    # 4. Polish Pitfall colors (softer, refined borders)
    old_pitfall = '''.pitfall-bad {
  background: var(--bad-soft);
  border: 1px solid var(--bad);
  color: var(--ink);
}
.pitfall-good {
  background: var(--ok-soft);
  border: 1px solid var(--ok);
  color: var(--ink);
}'''

    new_pitfall = '''.pitfall-bad {
  background: var(--bad-soft);
  border: 1px solid rgba(239, 68, 68, 0.25);
  border-radius: 12px;
  padding: 16px 18px;
  color: var(--ink);
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.02);
}
.pitfall-good {
  background: var(--ok-soft);
  border: 1px solid rgba(22, 163, 74, 0.25);
  border-radius: 12px;
  padding: 16px 18px;
  color: var(--ink);
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.02);
}'''

    if old_pitfall in content:
        content = content.replace(old_pitfall, new_pitfall, 1)

    # 5. Polish Quiz Option Cards
    old_quiz_opt = '''.quiz-opt {
  display: block;
  width: 100%;
  text-align: left;
  padding: 14px 16px;
  margin-bottom: 10px;
  border-radius: 12px;
  border: 2px solid var(--line);
  background: var(--card);
  color: var(--ink);
  font: inherit;
  font-size: .95rem;
  font-weight: 500;
  cursor: pointer;
  transition: .15s;
}
.quiz-opt:hover:not(:disabled) {
  border-color: var(--acc);
  background: var(--acc-soft);
}
.quiz-opt.ok {
  border-color: var(--ok);
  background: var(--ok-soft);
  font-weight: 700;
}
.quiz-opt.no {
  border-color: var(--bad);
  background: var(--bad-soft);
}'''

    new_quiz_opt = '''.quiz-opt {
  display: flex;
  align-items: flex-start;
  width: 100%;
  text-align: left;
  padding: 12px 16px;
  margin-bottom: 10px;
  border-radius: 10px;
  border: 1px solid var(--line);
  background: var(--card);
  color: var(--ink);
  font: inherit;
  font-size: 0.94rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.15s cubic-bezier(0.16, 1, 0.3, 1);
  box-sizing: border-box;
}
.quiz-opt:hover:not(:disabled) {
  border-color: var(--acc);
  background: var(--card-sub);
  transform: translateY(-1px);
}
.quiz-opt.ok {
  border-color: var(--ok);
  background: var(--ok-soft);
  font-weight: 700;
  transform: none;
}
.quiz-opt.no {
  border-color: var(--bad);
  background: var(--bad-soft);
  transform: none;
}'''

    if old_quiz_opt in content:
        content = content.replace(old_quiz_opt, new_quiz_opt, 1)

    # 6. Polish Buttons (Primary & Secondary)
    old_btn = '''.btn {
  padding: 12px 20px;
  border-radius: 12px;
  font-size: .95rem;
  font-weight: 700;
  border: none;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: .15s;
}
.btn-primary { background: var(--acc); color: #fff; }
.btn-primary:hover { background: var(--acc-hover); }
.btn-secondary { background: var(--card-sub); border: 1px solid var(--line); color: var(--ink); }
.btn-secondary:hover { border-color: var(--mute); }
.btn:disabled { opacity: .4; cursor: not-allowed; }'''

    new_btn = '''.btn {
  padding: 11px 20px;
  border-radius: 10px;
  font-size: 0.92rem;
  font-weight: 700;
  border: 1px solid transparent;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  transition: all 0.16s cubic-bezier(0.16, 1, 0.3, 1);
  letter-spacing: -0.01em;
}
.btn-primary {
  background: var(--acc);
  color: #fff;
  box-shadow: 0 2px 6px rgba(37, 99, 235, 0.2);
}
.btn-primary:hover:not(:disabled) {
  background: var(--acc-hover);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.28);
}
.btn-primary:active:not(:disabled) {
  transform: translateY(0);
}
.btn-secondary {
  background: var(--card);
  border: 1px solid var(--line);
  color: var(--ink);
}
.btn-secondary:hover:not(:disabled) {
  border-color: var(--mute);
  background: var(--card-sub);
}
.btn:disabled {
  opacity: 0.55;
  cursor: not-allowed;
  transform: none !important;
  box-shadow: none !important;
}'''

    if old_btn in content:
        content = content.replace(old_btn, new_btn, 1)

    # 7. Polish Reference Box
    old_ref = '''.lesson-ref-box {
  margin-top: 26px;
  background: var(--card);
  border: 1px solid var(--line);
  border-left: 4px solid var(--acc);
  border-radius: 12px;
  padding: 18px 20px;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.04);
  transition: all .2s ease;
}'''

    new_ref = '''.lesson-ref-box {
  margin-top: 32px;
  background: var(--card);
  border: 1px solid var(--line);
  border-left: 4px solid var(--acc);
  border-radius: 12px;
  padding: 20px 24px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  transition: all 0.2s ease;
}'''

    if old_ref in content:
        content = content.replace(old_ref, new_ref, 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Polished {filepath}")

# Polish both hoc.html and csdl/hoc.html
polish_course_file('site/hoc.html', 'MAT1052', 'Xác suất Thống kê', 'XSTK', '🎲')
polish_course_file('site/csdl/hoc.html', 'INT2207', 'Cơ sở dữ liệu', 'CSDL', '🗄️')
