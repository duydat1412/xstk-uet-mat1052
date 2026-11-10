import sys
sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 900})

        print("1. Testing CSDL CSDL_02 (ERD symbols)...")
        page.goto("http://localhost:3000/csdl/hoc", wait_until="networkidle")
        
        # Click CSDL_02
        page.locator("button:has-text('CSDL_02')").first.click()
        page.wait_for_timeout(500)
        
        # Verify illustration is present
        img_locator = page.locator("img[alt*='Bảng tra cứu Ký hiệu chuẩn Lược đồ ER']").first
        assert img_locator.is_visible(), "ERD symbol illustration is not visible!"
        print("CSDL_02 illustration is visible!")

        # Scroll to illustration and take screenshot
        card = page.locator("div:has-text('Sơ đồ & Minh họa trực quan')").first
        card.scroll_into_view_if_needed()
        page.wait_for_timeout(300)
        page.screenshot(path=r"C:\Users\DAT\.gemini\antigravity\brain\1d24eb92-d946-44ab-8525-14088dab9c53\csdl02_erd_illustrations_proof.png")
        print("Captured csdl02_erd_illustrations_proof.png")

        # Click image to test zoom lightbox
        img_locator.click()
        page.wait_for_timeout(400)
        modal_img = page.locator("[role='dialog'] img[alt*='Bảng tra cứu Ký hiệu chuẩn Lược đồ ER']").first
        assert modal_img.is_visible(), "Zoom lightbox image is not visible!"
        print("Lightbox modal opened successfully!")
        page.screenshot(path=r"C:\Users\DAT\.gemini\antigravity\brain\1d24eb92-d946-44ab-8525-14088dab9c53\csdl02_erd_lightbox_proof.png")
        print("Captured csdl02_erd_lightbox_proof.png")

        # Close modal with Esc
        page.keyboard.press("Escape")
        page.wait_for_timeout(300)

        # 2. Test CSDL_03 (Company ERD)
        print("\n2. Testing CSDL CSDL_03 (Full Company ERD)...")
        page.locator("button:has-text('CSDL_03')").first.click()
        page.wait_for_timeout(500)
        company_erd = page.locator("img[alt*='Toàn cảnh Lược đồ ERD Quản lý Dự án Công ty']").first
        assert company_erd.is_visible(), "Company ERD is not visible!"
        company_erd.scroll_into_view_if_needed()
        page.wait_for_timeout(300)
        page.screenshot(path=r"C:\Users\DAT\.gemini\antigravity\brain\1d24eb92-d946-44ab-8525-14088dab9c53\csdl03_company_erd_proof.png")
        print("Captured csdl03_company_erd_proof.png")

        # 3. Test CSDL_05 (Relational Schema & FK arrows)
        print("\n3. Testing CSDL CSDL_05 (Relational Schema & FK)...")
        # Click Chương 2 folder
        c2_btn = page.locator("button:has-text('Chương 2')").first
        c2_btn.click()
        page.wait_for_timeout(300)
        page.locator("button:has-text('CSDL_05')").first.click()
        page.wait_for_timeout(500)
        fk_schema = page.locator("img[alt*='Lược đồ CSDL Quan hệ & Mũi tên Ràng buộc Khóa ngoại']").first
        assert fk_schema.is_visible(), "FK schema illustration is not visible!"
        fk_schema.scroll_into_view_if_needed()
        page.wait_for_timeout(300)
        page.screenshot(path=r"C:\Users\DAT\.gemini\antigravity\brain\1d24eb92-d946-44ab-8525-14088dab9c53\csdl05_fk_schema_proof.png")
        print("Captured csdl05_fk_schema_proof.png")

        # 4. Test XSTK A3 (Boxplot Tukey)
        print("\n4. Testing XSTK Lesson A3 (Boxplot)...")
        page.goto("http://localhost:3000/xstk/hoc", wait_until="networkidle")
        page.locator("button:has-text('A3')").first.click()
        page.wait_for_timeout(500)
        boxplot_img = page.locator("img[alt*='Cấu tạo Biểu đồ Hộp']").first
        assert boxplot_img.is_visible(), "Boxplot illustration is not visible!"
        boxplot_img.scroll_into_view_if_needed()
        page.wait_for_timeout(300)
        page.screenshot(path=r"C:\Users\DAT\.gemini\antigravity\brain\1d24eb92-d946-44ab-8525-14088dab9c53\xstk_a3_boxplot_proof.png")
        print("Captured xstk_a3_boxplot_proof.png")

        browser.close()
        print("\nALL ILLUSTRATIONS & BLUEPRINTS VERIFIED WITH 100% SUCCESS!")

if __name__ == "__main__":
    main()
