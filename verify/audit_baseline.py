import sys
sys.stdout.reconfigure(encoding='utf-8')
from playwright.sync_api import sync_playwright

def audit_page(url):
    errors = []
    logs = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.on('console', lambda msg: logs.append(f"[{msg.type}] {msg.text}"))
        page.on('pageerror', lambda exc: errors.append(str(exc)))
        page.goto(url)
        page.wait_for_timeout(1000)
        
        dom_nodes = page.evaluate("() => document.querySelectorAll('*').length")
        browser.close()
    return logs, errors, dom_nodes

for name, path in [
    ('index.html', 'file:///d:/Projects/XSTK/site/index.html'),
    ('hoc.html', 'file:///d:/Projects/XSTK/site/hoc.html'),
    ('csdl/hoc.html', 'file:///d:/Projects/XSTK/site/csdl/hoc.html')
]:
    logs, errors, dom_nodes = audit_page(path)
    print(f"=== {name} ===")
    print(f"DOM nodes: {dom_nodes}")
    print(f"Errors: {len(errors)}")
    for e in errors:
        print(f"  ERR: {e}")
    warns = [l for l in logs if 'error' in l.lower() or 'warn' in l.lower()]
    print(f"Console warnings/errors: {len(warns)}")
    for w in warns:
        print(f"  LOG: {w}")
