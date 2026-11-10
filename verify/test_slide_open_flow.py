import sys
sys.stdout.reconfigure(encoding="utf-8")
from playwright.sync_api import sync_playwright
import urllib.request

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)
        page = browser.new_page()

        # 1. Test XSTK
        print("Testing XSTK...")
        page.goto("http://localhost:3000/xstk/hoc", wait_until="networkidle")
        slide_btn = page.locator("a:has-text('Mở Slide')").first
        href = slide_btn.get_attribute("href")
        print("XSTK Lesson A1 Slide Href:", href)
        
        # Test fetching the URL
        clean_url = href.split("#")[0]
        full_url = f"http://localhost:3000{clean_url}"
        res = urllib.request.urlopen(full_url)
        print(f"Fetch {full_url} -> Status: {res.status}, Type: {res.headers.get_content_type()}, Size: {len(res.read())}")
        assert res.status == 200
        assert res.headers.get_content_type() == "application/pdf"

        # 2. Test CSDL
        print("\nTesting CSDL...")
        page.goto("http://localhost:3000/csdl/hoc", wait_until="networkidle")
        csdl_slide_btn = page.locator("a:has-text('Mở Slide')").first
        csdl_href = csdl_slide_btn.get_attribute("href")
        print("CSDL Lesson CSDL_01 Slide Href:", csdl_href)
        
        # Test fetching the URL
        clean_csdl_url = csdl_href.split("#")[0]
        full_csdl_url = f"http://localhost:3000{clean_csdl_url}"
        csdl_res = urllib.request.urlopen(full_csdl_url)
        print(f"Fetch {full_csdl_url} -> Status: {csdl_res.status}, Type: {csdl_res.headers.get_content_type()}, Size: {len(csdl_res.read())}")
        assert csdl_res.status == 200
        assert csdl_res.headers.get_content_type() == "application/pdf"

        # Screenshot of CSDL ref box
        ref_box = page.locator("div:has-text('Dấu Ref Tra cứu Slide')").first
        ref_box.screenshot(path=r"C:\Users\DAT\.gemini\antigravity\brain\1d24eb92-d946-44ab-8525-14088dab9c53\csdl_ref_box_proof.png")
        print("Saved csdl_ref_box_proof.png")

        browser.close()
        print("\nALL SLIDE LINK TESTS PASSED WITH 100% SUCCESS!")

if __name__ == "__main__":
    main()
