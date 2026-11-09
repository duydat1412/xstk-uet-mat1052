import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('site/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add Be Vietnam Pro font link if not present
font_link = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&family=Fira+Code:wght@400;600&display=swap">'
if 'family=Be+Vietnam+Pro' not in text:
    text = text.replace('<!-- KaTeX CSS & JS -->', font_link + '\n  <!-- KaTeX CSS & JS -->', 1)
    print("Added Be Vietnam Pro font to index.html")

# 2. Update font-family in body
old_font = 'font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;'
new_font = 'font-family: "Be Vietnam Pro", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;\n  letter-spacing: -0.011em;'
if old_font in text:
    text = text.replace(old_font, new_font, 1)
    print("Updated font-family in index.html")

# 3. Add browser surfaces styling (selection, focus, scrollbars)
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
  border-radius: 999px;
}
::-webkit-scrollbar-thumb:hover {
  background: var(--mute);
}
:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}
.stat-num, .stat-pill, .badge-course {
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

if 'Impeccable Craft Floor' not in text:
    text = text.replace('* { box-sizing: border-box; margin: 0; padding: 0; }', '* { box-sizing: border-box; margin: 0; padding: 0; }\n' + browser_surfaces, 1)
    print("Added browser surfaces CSS to index.html")

# Save to site/index.html and index.html
with open('site/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved site/index.html and index.html")
