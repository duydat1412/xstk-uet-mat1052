import os
from playwright.sync_api import sync_playwright

ARTIFACT_DIR = r"C:\Users\DAT\.gemini\antigravity\brain\1d24eb92-d946-44ab-8525-14088dab9c53"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 950}, device_scale_factor=2)
        page = context.new_page()

        print("Navigating to http://localhost:3000/xstk/hoc ...")
        page.goto("http://localhost:3000/xstk/hoc", wait_until="networkidle")

        # Click on Lesson A4 in sidebar
        print("Clicking Lesson A4...")
        page.locator("button:has-text('A4')").first.click()
        page.wait_for_timeout(600)

        # Click on Quiz Tab (Tab 4)
        print("Clicking Quiz Tab...")
        page.locator("button[role='tab']", has_text="Kiểm tra").first.click()
        page.wait_for_timeout(600)

        # Scroll to Question 2 & Question 3
        page.evaluate("window.scrollBy(0, 480)")
        page.wait_for_timeout(400)

        # Light mode screenshot (Question 2 & 3)
        light_file = os.path.join(ARTIFACT_DIR, "math_quiz_light_cau2_cau3.png")
        page.screenshot(path=light_file)
        print(f"Saved light mode screenshot: {light_file}")

        # Toggle Theme to Dark Mode
        print("Toggling to Dark Mode...")
        page.locator("button[aria-label='Toggle Theme']").first.click()
        page.wait_for_timeout(600)

        # Dark mode screenshot (Question 2 & 3)
        dark_file = os.path.join(ARTIFACT_DIR, "math_quiz_dark_cau2_cau3.png")
        page.screenshot(path=dark_file)
        print(f"Saved dark mode screenshot: {dark_file}")

        # Switch to Examples tab (Tab 2) in dark mode
        print("Clicking Examples Tab...")
        page.locator("button[role='tab']", has_text="Ba Ví dụ").first.click()
        page.wait_for_timeout(600)

        examples_file = os.path.join(ARTIFACT_DIR, "math_examples_dark.png")
        page.screenshot(path=examples_file)
        print(f"Saved examples screenshot: {examples_file}")

        # Switch to Theory tab (Tab 1) in dark mode
        print("Clicking Theory Tab...")
        page.locator("button[role='tab']", has_text="Lý thuyết").first.click()
        page.wait_for_timeout(600)

        theory_file = os.path.join(ARTIFACT_DIR, "math_theory_dark.png")
        page.screenshot(path=theory_file)
        print(f"Saved theory screenshot: {theory_file}")

        browser.close()
        print("Playwright full verification completed successfully!")

if __name__ == "__main__":
    main()
