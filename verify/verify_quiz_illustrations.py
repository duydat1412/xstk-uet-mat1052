import os
import sys
from playwright.sync_api import sync_playwright

artifact_dir = r"C:\Users\DAT\.gemini\antigravity\brain\1d24eb92-d946-44ab-8525-14088dab9c53"

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        
        print("1. Testing CSDL_01 Quiz & Example Illustrations...")
        page.goto("http://localhost:3000/csdl/hoc", wait_until="networkidle")
        
        # Switch to 'Bài kiểm tra' tab
        page.click("button[role='tab']:has-text('Bài kiểm tra')")
        page.wait_for_selector("img[src*='csdl01_ansi_sparc_architecture.png']", timeout=5000)
        page.screenshot(path=os.path.join(artifact_dir, "proof_csdl01_quiz_diagram.png"))
        print(" -> CSDL_01 Quiz Diagram verified & captured!")
        
        # Switch to 'Ví dụ mẫu' tab
        page.click("button[role='tab']:has-text('Ví dụ mẫu')")
        page.wait_for_selector("img[src*='csdl01_ansi_sparc_architecture.png']", timeout=5000)
        page.screenshot(path=os.path.join(artifact_dir, "proof_csdl01_example_diagram.png"))
        print(" -> CSDL_01 Example Diagram verified & captured!")
        
        # Select CSDL_02
        print("2. Testing CSDL_02 Quiz & Lightbox...")
        page.click("button:has-text('CSDL_02')")
        page.wait_for_timeout(500)
        page.click("button[role='tab']:has-text('Bài kiểm tra')")
        page.wait_for_selector("img[src*='csdl02_erd_symbols_table.png']", timeout=5000)
        page.screenshot(path=os.path.join(artifact_dir, "proof_csdl02_quiz_diagram.png"))
        print(" -> CSDL_02 Quiz Diagram verified!")
        
        # Click the image to trigger Lightbox
        page.click("img[src*='csdl02_erd_symbols_table.png']")
        page.wait_for_selector("div.fixed.inset-0.z-50", timeout=5000)
        page.screenshot(path=os.path.join(artifact_dir, "proof_csdl02_quiz_lightbox.png"))
        print(" -> CSDL_02 Lightbox Modal verified & captured!")
        
        # Close lightbox
        page.keyboard.press("Escape")
        page.wait_for_timeout(500)
        
        # Select CSDL_03 Examples
        print("3. Testing CSDL_03 Company ERD Example...")
        page.click("button:has-text('CSDL_03')")
        page.wait_for_timeout(500)
        page.click("button[role='tab']:has-text('Ví dụ mẫu')")
        page.wait_for_selector("img[src*='csdl03_full_company_erd.png']", timeout=5000)
        page.screenshot(path=os.path.join(artifact_dir, "proof_csdl03_example3_company_erd.png"))
        print(" -> CSDL_03 Example 3 Company ERD verified!")
        
        # Navigate to XSTK A3 Boxplot
        print("4. Testing XSTK A3 Boxplot Quiz...")
        page.goto("http://localhost:3000/xstk/hoc", wait_until="networkidle")
        # Click A3
        page.click("button:has-text('A3')")
        page.wait_for_timeout(500)
        page.click("button[role='tab']:has-text('Bài kiểm tra')")
        # Question 3 in A3
        page.wait_for_selector("img[src*='xstk_a3_boxplot_tukey.png']", timeout=5000)
        page.screenshot(path=os.path.join(artifact_dir, "proof_xstk_a3_quiz_boxplot.png"))
        print(" -> XSTK A3 Quiz Boxplot verified & captured!")
        
        browser.close()
        print("All tests passed successfully!")

if __name__ == "__main__":
    run()
