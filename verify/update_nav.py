import sys

sys.stdout.reconfigure(encoding='utf-8')

for p in ['site/hoc.html', 'site/tuluan.html']:
    with open(p, 'r', encoding='utf-8') as f:
        text = f.read()
    if 'dethi.html' not in text:
        text = text.replace(
            '<a href="tracnghiem.html" class="nav-link">📝 Trắc nghiệm</a>',
            '<a href="tracnghiem.html" class="nav-link">📝 Trắc nghiệm (161 câu)</a>\n      <a href="dethi.html" class="nav-link">🎯 Đề thi mẫu</a>'
        )
        with open(p, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Updated nav in {p}")
    else:
        print(f"Nav already updated in {p}")
