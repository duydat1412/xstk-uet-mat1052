import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

doc7 = fitz.open("week07.pdf")

def print_range(start, end, desc):
    print(f"\n=================== {desc} (Slide {start}-{end}) ===================")
    for p in range(start-1, end):
        txt = doc7[p].get_text().strip()
        lines = [l.strip() for l in txt.split('\n') if l.strip()]
        header = " | ".join(lines[:3]) if lines else "EMPTY"
        print(f"Slide {p+1}: {header}")

print_range(4, 20, "Phần 1: Kỳ vọng và phương sai")
print_range(21, 32, "Phần 2: BNN độc lập cùng phân phối, mô hình chiếc hộp, tổng và trung bình")
print_range(33, 40, "Phần 3: Bất đẳng thức Chebyshev và luật số lớn yếu")
print_range(41, 49, "Phần 4: Biến ngẫu nhiên liên tục")
print_range(50, 67, "Phần 5: Các phân phối liên tục đặc biệt")
print_range(68, 77, "Phần 6: Định lý giới hạn trung tâm")
