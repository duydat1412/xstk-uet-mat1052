import sys, re
sys.stdout.reconfigure(encoding='utf-8')

# Update site/hoc.html
with open('site/hoc.html', 'r', encoding='utf-8') as f:
    hoc = f.read()
hoc = hoc.replace(
    '<nav class="nav-links">\n      <a href="hoc.html" class="nav-link active">📚 Lý thuyết</a>',
    '<nav class="nav-links">\n      <a href="index.html" class="nav-link">🏠 Tổng quan</a>\n      <a href="hoc.html" class="nav-link active">📚 Lý thuyết</a>'
)
with open('site/hoc.html', 'w', encoding='utf-8') as f:
    f.write(hoc)

# Update site/tuluan.html
with open('site/tuluan.html', 'r', encoding='utf-8') as f:
    tuluan = f.read()
tuluan = tuluan.replace(
    '<nav class="nav-links">\n      <a href="hoc.html" class="nav-link">📚 Lý thuyết</a>',
    '<nav class="nav-links">\n      <a href="index.html" class="nav-link">🏠 Tổng quan</a>\n      <a href="hoc.html" class="nav-link">📚 Lý thuyết</a>'
)
with open('site/tuluan.html', 'w', encoding='utf-8') as f:
    f.write(tuluan)

# Update site/tracnghiem.html
with open('site/tracnghiem.html', 'r', encoding='utf-8') as f:
    tn = f.read()
tn = tn.replace(
    '<nav class="nav-links">\n      <a href="hoc.html" class="nav-link">Lý thuyết</a>',
    '<nav class="nav-links">\n      <a href="index.html" class="nav-link">🏠 Tổng quan</a>\n      <a href="hoc.html" class="nav-link">Lý thuyết</a>'
)
with open('site/tracnghiem.html', 'w', encoding='utf-8') as f:
    f.write(tn)

# Update site/congthuc.html
with open('site/congthuc.html', 'r', encoding='utf-8') as f:
    ct = f.read()
ct = ct.replace(
    '<nav class="nav-links">\n      <a href="hoc.html" class="nav-link">Lý thuyết</a>',
    '<nav class="nav-links">\n      <a href="index.html" class="nav-link">🏠 Tổng quan</a>\n      <a href="hoc.html" class="nav-link">Lý thuyết</a>'
)
with open('site/congthuc.html', 'w', encoding='utf-8') as f:
    f.write(ct)

print("Updated navbars across all pages!")
