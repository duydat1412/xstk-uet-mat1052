import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('site/hoc.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update brand in header
old_brand = '<a href="hoc.html" class="brand" style="text-decoration:none; color:inherit;">\n      <span>⚡</span> XSTK UET\n    </a>'
new_brand = '<a href="/hoc" class="brand" style="text-decoration:none; color:inherit; display:flex; align-items:center; gap:8px;">\n      <span style="font-size:1.3rem;">🎲</span>\n      <div style="display:flex; flex-direction:column; line-height:1.2;">\n        <span style="font-weight:800; font-size:1.05rem;">XSTK UET</span>\n        <span style="font-size:0.75rem; color:var(--mute); font-weight:600;">MAT1052 • Xác suất Thống kê</span>\n      </div>\n    </a>'

if old_brand in text:
    text = text.replace(old_brand, new_brand, 1)
    print("Replaced brand in hoc.html")
else:
    print("Brand not found in hoc.html")

# 2. Update course switcher in hoc.html
old_switcher = '''      <div class="course-switcher" style="display:inline-flex;align-items:center;background:var(--card-subtle);border:1px solid var(--line);border-radius:var(--radius-sm);padding:2px;margin-right:12px;">
        <a href="/hoc" style="display:inline-flex;align-items:center;gap:4px;padding:4px 10px;font-size:0.8rem;font-weight:700;color:var(--acc);background:var(--card);text-decoration:none;border-radius:6px;box-shadow:var(--shadow-sm);">
          🎲 XSTK
        </a>
        <a href="/csdl/hoc" style="display:inline-flex;align-items:center;gap:4px;padding:4px 10px;font-size:0.8rem;font-weight:600;color:var(--mute);text-decoration:none;border-radius:6px;transition:all 0.15s ease;">
          🗄️ CSDL
        </a>
      </div>'''

new_switcher = '''      <div class="course-switcher" style="display:inline-flex;align-items:center;background:var(--card-sub);border:1px solid var(--line);border-radius:8px;padding:3px;margin-right:12px;">
        <a href="/hoc" style="display:inline-flex;align-items:center;gap:5px;padding:5px 12px;font-size:0.82rem;font-weight:700;color:var(--acc);background:var(--card);text-decoration:none;border-radius:6px;box-shadow:0 1px 2px rgba(0,0,0,0.06);">
          🎲 XSTK
        </a>
        <a href="/csdl/hoc" style="display:inline-flex;align-items:center;gap:5px;padding:5px 12px;font-size:0.82rem;font-weight:600;color:var(--mute);text-decoration:none;border-radius:6px;transition:all 0.15s ease;">
          🗄️ CSDL
        </a>
      </div>'''

if old_switcher in text:
    text = text.replace(old_switcher, new_switcher, 1)
    print("Replaced switcher in hoc.html")
else:
    print("Switcher not found in hoc.html")

with open('site/hoc.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Saved site/hoc.html")
