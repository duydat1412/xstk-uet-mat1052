import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

switcher_html = """
      <div class="course-switcher" style="display:inline-flex;align-items:center;background:var(--card-subtle);border:1px solid var(--line);border-radius:var(--radius-sm);padding:2px;margin-right:12px;">
        <a href="/hoc" style="display:inline-flex;align-items:center;gap:4px;padding:4px 10px;font-size:0.8rem;font-weight:700;color:var(--acc);background:var(--card);text-decoration:none;border-radius:6px;box-shadow:var(--shadow-sm);">
          🎲 XSTK
        </a>
        <a href="/csdl/hoc" style="display:inline-flex;align-items:center;gap:4px;padding:4px 10px;font-size:0.8rem;font-weight:600;color:var(--mute);text-decoration:none;border-radius:6px;transition:all 0.15s ease;">
          🗄️ CSDL
        </a>
      </div>
"""

xstk_files = [
    'site/hoc.html',
    'site/tracnghiem.html',
    'site/tuluan.html',
    'site/congthuc.html',
    'site/dethi.html'
]

for fpath in xstk_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if switcher already present
    if 'course-switcher' in content:
        print(f"Skipping {fpath} (already has course-switcher)")
        continue
    
    # Insert switcher before <nav class="nav-links">
    if '<nav class="nav-links">' in content:
        content = content.replace('<nav class="nav-links">', switcher_html + '\n      <nav class="nav-links">')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added course switcher to {fpath}")
    else:
        print(f"Warning: Could not find <nav class=\"nav-links\"> in {fpath}")
