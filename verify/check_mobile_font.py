import sys
sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 390, "height": 844},
            user_agent="Mozilla/5.0 (Linux; Android 13; Mi 11) AppleWebKit/537.36"
        )
        page = context.new_page()
        page.goto("http://localhost:3000/xstk/hoc", wait_until="networkidle")
        
        # On mobile, open drawer first to select A3
        page.locator("button:has-text('Mục lục')").first.click()
        page.wait_for_timeout(400)
        page.locator("[role='dialog'] button:has-text('A3')").click()
        page.wait_for_timeout(600)
        
        # Click Quiz tab
        page.locator("button[role='tab']").nth(3).click()
        page.wait_for_timeout(500)
        
        # Scroll to question 3
        q3 = page.locator("div.font-bold:has-text('Tukey')").first
        q3.scroll_into_view_if_needed()
        page.wait_for_timeout(300)
        
        # Toggle dark mode
        page.locator("button:has([class*='lucide-moon']), button:has([class*='lucide-sun'])").click()
        page.wait_for_timeout(300)
        page.screenshot(
            path=r"C:\Users\DAT\.gemini\antigravity\brain\1d24eb92-d946-44ab-8525-14088dab9c53\mobile_font_proof_dark_actual.png"
        )
        print("Captured mobile dark screenshot!")
        browser.close()

if __name__ == "__main__":
    main()
