import sys, re
sys.stdout.reconfigure(encoding='utf-8')

files = ['site/index.html', 'site/hoc.html', 'site/tuluan.html', 'site/tracnghiem.html', 'site/congthuc.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    m = re.search(r'(<nav[^>]*>[\s\S]*?</nav>|<div class="nav-links"[\s\S]*?</div>)', txt)
    print(f"=== {f} ===")
    if m:
        print(m.group(0))
    else:
        print("Not found")
