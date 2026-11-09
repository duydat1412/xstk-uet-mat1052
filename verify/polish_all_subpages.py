import sys
sys.stdout.reconfigure(encoding='utf-8')

pages = [
    'site/tracnghiem.html',
    'site/tuluan.html',
    'site/congthuc.html',
    'site/dethi.html'
]

font_link = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&family=Fira+Code:wght@400;600&display=swap">'

browser_surfaces = '''
/* Impeccable Craft Floor: Browser Surfaces & Design Tokens */
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
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
'''

for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()

    # Font
    if 'family=Be+Vietnam+Pro' not in content:
        content = content.replace('<head>', '<head>\n  ' + font_link, 1)

    # Browser surfaces
    if 'Impeccable Craft Floor' not in content:
        if '* { box-sizing: border-box;' in content:
            content = content.replace('* { box-sizing: border-box;', '* { box-sizing: border-box;\n' + browser_surfaces, 1)
        elif '* {' in content:
            content = content.replace('* {', '* {\n' + browser_surfaces, 1)

    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Polished {p}")
