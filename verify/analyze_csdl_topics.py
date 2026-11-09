import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('docs/csdl_slides_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Define 14 lessons mapping
lessons_map = [
    # Cụm 1: Tổng quan & Mô hình ER/EER
    {"id": "CSDL_01", "cluster": "1", "title": "Tổng quan về Hệ Cơ sở Dữ liệu & Kiến trúc 3 mức", "file": "C1 .pptx", "slides": [1, 52]},
    {"id": "CSDL_02", "cluster": "1", "title": "Mô hình Thực thể - Liên kết (ER): Thực thể & Thuộc tính", "file": "C2_1.pptx", "slides": [1, 25]},
    {"id": "CSDL_03", "cluster": "1", "title": "Mối liên kết, Ràng buộc tỉ số & Thực thể yếu", "file": "C2_1.pptx", "slides": [26, 52]},
    {"id": "CSDL_04", "cluster": "1", "title": "Mô hình ER mở rộng (EER): Chuyên biệt hóa & Khái quát hóa", "file": "C2_2.pptx", "slides": [1, 26]},
    
    # Cụm 2: Mô hình Quan hệ & Ánh xạ ER
    {"id": "CSDL_05", "cluster": "2", "title": "Mô hình Dữ liệu Quan hệ: Khóa chính, Khóa ngoại & Toàn vẹn", "file": "C3_1.pptx", "slides": [1, 27]},
    {"id": "CSDL_06", "cluster": "2", "title": "Thuật toán chuyển đổi Lược đồ ER/EER sang Lược đồ Quan hệ", "file": "C3_1.pptx", "slides": [28, 43]},
    
    # Cụm 3: Đại số Quan hệ (Relational Algebra)
    {"id": "CSDL_07", "cluster": "3", "title": "Đại số quan hệ: Phép Chọn (σ), Chiếu (π) & Phép toán Tập hợp", "file": "C3_2.pdf", "slides": [1, 35]},
    {"id": "CSDL_08", "cluster": "3", "title": "Các phép Kết nối: Kết nối tự nhiên (⨝), Theta-Join & Outer Join", "file": "C3_2.pdf", "slides": [36, 70]},
    {"id": "CSDL_09", "cluster": "3", "title": "Phép Chia (÷), Gom nhóm (γ) & Tối ưu hóa Cây truy vấn", "file": "C3_2.pdf", "slides": [71, 111]},
    
    # Cụm 4: Phụ thuộc hàm & Chuẩn hóa
    {"id": "CSDL_10", "cluster": "4", "title": "Dư thừa dữ liệu, Dị thường & Định nghĩa Phụ thuộc hàm (FD)", "file": "C4_1.pptx", "slides": [1, 25]},
    {"id": "CSDL_11", "cluster": "4", "title": "Hệ tiên đề Armstrong & Thuật toán tìm Bao đóng thuộc tính X+", "file": "C4_1.pptx", "slides": [26, 45]},
    {"id": "CSDL_12", "cluster": "4", "title": "Thuật toán xác định tất cả Khóa tối thiểu của Lược đồ", "file": "C4_1.pptx", "slides": [46, 60]},
    {"id": "CSDL_13", "cluster": "4", "title": "Các Dạng chuẩn dữ liệu: 1NF, 2NF, 3NF và BCNF", "file": "C4_1.pptx", "slides": [61, 78]},
    {"id": "CSDL_14", "cluster": "4", "title": "Lý thuyết Phân rã: Bảo toàn thông tin, Bảo toàn phụ thuộc hàm", "file": "C4_1.pptx", "slides": [79, 96]}
]

print(f"Total designed CSDL lessons: {len(lessons_map)}")
for l in lessons_map:
    file_slides = data.get(l['file'], {}).get('slides', [])
    start_s = l['slides'][0]
    end_s = l['slides'][1]
    
    # Extract text from this range
    text_snippets = []
    for s in file_slides:
        s_num = s.get('slide_num') or s.get('page_num')
        if start_s <= s_num <= end_s:
            t = s.get('text', '').strip()
            if t:
                text_snippets.append(t)
    print(f"[{l['id']}] {l['title']} | File: {l['file']} (Slide {start_s}-{end_s}) | Text blocks: {len(text_snippets)}")

with open('docs/csdl_lessons_map.json', 'w', encoding='utf-8') as f:
    json.dump(lessons_map, f, ensure_ascii=False, indent=2)
print("Saved docs/csdl_lessons_map.json!")
