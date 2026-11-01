import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('site/hoc.html', 'r', encoding='utf-8') as f:
    text = f.read()

nav_css = """
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
"""

if '.nav-links' not in text:
    text = text.replace('/* PROGRESS BAR */', nav_css + '\n/* PROGRESS BAR */')

target_str = """    <div class="brand" onclick="goToLesson(0)">
      <span>⚡</span> XSTK UET
    </div>"""

replacement_str = """    <a href="hoc.html" class="brand" style="text-decoration:none; color:inherit;">
      <span>⚡</span> XSTK UET
    </a>
    <nav class="nav-links">
      <a href="hoc.html" class="nav-link active">📚 Lý thuyết</a>
      <a href="tuluan.html" class="nav-link">✍️ Tự luận</a>
      <a href="tracnghiem.html" class="nav-link">📝 Trắc nghiệm</a>
      <a href="congthuc.html" class="nav-link">📖 Công thức</a>
    </nav>"""

if target_str in text:
    text = text.replace(target_str, replacement_str)
    with open('site/hoc.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated hoc.html header navigation successfully!")
else:
    print("target_str not found")
