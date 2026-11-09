import sys
sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        page.goto("http://localhost:3000/xstk/hoc", wait_until="networkidle")

        # Click Lesson A3 (where Tukey question is)
        page.locator("button:has-text('A3')").first.click()
        page.wait_for_timeout(500)

        # Click Quiz tab (Tab 4)
        page.locator("button[role='tab']").nth(3).click()
        page.wait_for_timeout(500)

        # Find question element with Tukey
        q3_elem = page.locator("div.font-bold:has-text('Tukey')").first
        styles = q3_elem.evaluate("el => { const s = window.getComputedStyle(el); return { fontFamily: s.fontFamily, fontWeight: s.fontWeight, fontSize: s.fontSize }; }")
        print("Computed styles of Question 3:", styles)

        # Screenshot of question element
        q3_elem.screenshot(path=r"C:\Users\DAT\.gemini\antigravity\brain\1d24eb92-d946-44ab-8525-14088dab9c53\local_q3_render.png")
        print("Saved local_q3_render.png")
        browser.close()

if __name__ == "__main__":
    main()
