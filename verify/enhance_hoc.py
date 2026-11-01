import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('site/hoc.html', 'r', encoding='utf-8') as f:
    hoc = f.read()

# Enhance KaTeX auto-render so when KaTeX script loads deferred, it renders math automatically:
old_init = """// INIT APP
renderClusterTabs();
renderLessonsStrip();
renderCurrentLesson();"""

new_init = """// AUTO TRIGGER KATEX ONCE LOADED
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
renderCurrentLesson();"""

hoc = hoc.replace(old_init, new_init)

with open('site/hoc.html', 'w', encoding='utf-8') as f:
    f.write(hoc)

print("Added deferred KaTeX handler to site/hoc.html")
