import subprocess
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

scripts = [
    "verify/verify_sample_lesson.py",
    "verify/verify_cum_a.py",
    "verify/verify_cum_b.py",
    "verify/verify_cum_c.py",
    "verify/verify_cum_d.py",
    "verify/verify_cum_e.py"
]

all_passed = True
print("==================================================")
print("  CHẠY TỔNG KIỂM TRA SỐ HỌC TOÀN BỘ CỤM A, B, C, D, E")
print("==================================================")

for s in scripts:
    print(f"\n--- Đang chạy: {s} ---")
    res = subprocess.run([sys.executable, s], capture_output=True, text=True, encoding='utf-8')
    if res.returncode == 0:
        print(f"[OK] {s} HOÀN THÀNH XUẤT SẮC:")
        # print last line
        lines = res.stdout.strip().split('\n')
        print("     " + lines[-1] if lines else "Done")
    else:
        print(f"[ERROR] {s} THẤT BẠI:")
        print(res.stderr)
        all_passed = False

print("\n" + "="*50)
if all_passed:
    print("TẤT CẢ 6 BỘ SỐ LIỆU KIỂM CHỨNG ĐÃ ĐẠT 100% ĐỘ CHÍNH XÁC TOÁN HỌC!")
else:
    print("CÓ LỖI XẢY RA TRONG QUÁ TRÌNH KIỂM CHỨNG!")
print("="*50)
