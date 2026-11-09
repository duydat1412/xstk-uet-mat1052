import os
import sys
from playwright.sync_api import sync_playwright

# Set up screenshots directory
if "ARTIFACT_DIR" in os.environ:
    ARTIFACT_DIR = os.environ["ARTIFACT_DIR"]
elif os.path.exists(r"C:\Users\DAT\.gemini\antigravity\brain\1d24eb92-d946-44ab-8525-14088dab9c53"):
    ARTIFACT_DIR = r"C:\Users\DAT\.gemini\antigravity\brain\1d24eb92-d946-44ab-8525-14088dab9c53"
else:
    ARTIFACT_DIR = os.path.join(os.path.dirname(__file__), "screenshots")

os.makedirs(ARTIFACT_DIR, exist_ok=True)

def main():
    print(f"Artifact directory: {ARTIFACT_DIR}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 950}, device_scale_factor=2)
        page = context.new_page()

        print("Navigating to http://localhost:3000/xstk/hoc ...")
        page.goto("http://localhost:3000/xstk/hoc", wait_until="networkidle")

        # Click on Lesson A4 in sidebar
        print("Selecting Lesson A4...")
        page.locator("button:has-text('A4')").first.click()
        page.wait_for_timeout(500)

        # Tab 4 is Quiz
        print("Switching to Quiz Tab...")
        page.locator("button[role='tab']").nth(3).click()
        page.wait_for_timeout(500)

        # Check KaTeX elements
        katex_count = page.locator(".katex").count()
        print(f"KaTeX elements found: {katex_count}")
        assert katex_count >= 10, f"Expected at least 10 KaTeX elements, got {katex_count}"

        # Scroll to Question 2 & Question 3
        page.evaluate("window.scrollBy(0, 480)")
        page.wait_for_timeout(300)

        # Light mode screenshot
        light_file = os.path.join(ARTIFACT_DIR, "math_quiz_light_cau2_cau3.png")
        page.screenshot(path=light_file)
        print(f"Saved: {light_file}")

        # Toggle Theme to Dark Mode
        print("Toggling to Dark Mode...")
        page.locator("button[aria-label='Toggle Theme']").first.click()
        page.wait_for_timeout(500)

        # Dark mode screenshot
        dark_file = os.path.join(ARTIFACT_DIR, "math_quiz_dark_cau2_cau3.png")
        page.screenshot(path=dark_file)
        print(f"Saved: {dark_file}")

        # Switch to Examples tab (Tab index 1)
        print("Switching to Examples Tab...")
        page.locator("button[role='tab']").nth(1).click()
        page.wait_for_timeout(500)

        examples_file = os.path.join(ARTIFACT_DIR, "math_examples_dark.png")
        page.screenshot(path=examples_file)
        print(f"Saved: {examples_file}")

        # Switch to Theory tab (Tab index 0)
        print("Switching to Theory Tab...")
        page.locator("button[role='tab']").nth(0).click()
        page.wait_for_timeout(500)

        theory_file = os.path.join(ARTIFACT_DIR, "math_theory_dark.png")
        page.screenshot(path=theory_file)
        print(f"Saved: {theory_file}")

        browser.close()
        print("✅ Playwright E2E verification completed with 100% success!")

if __name__ == "__main__":
    main()
