# 📚 Hệ Thống Tự Học & Luyện Thi Xác Suất Thống Kê (UET.MAT1052)

> Bộ tài nguyên và ứng dụng tự học tương tác, chuẩn bị toàn diện cho kỳ thi Giữa kỳ Xác suất Thống kê Đại học Công nghệ (VNU - UET). 100% tiếng Việt, có đáp án giải thích chi tiết, barem điểm từng bước, mẹo Casio và kiểm toán toán học chính xác.

[![QA Tests](https://img.shields.io/badge/QA%20Tests-1832%2F1832%20Passed-brightgreen)](docs/qa-report.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Deployed on Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-black?logo=vercel)](https://vercel.com)

---

## 🚀 Các Tính Năng Nổi Bật

1. **26 Bài Học Vi Mô Phân Tầng (`site/hoc.html`)**:
   - Bao quát toàn bộ 7 tuần học (Slide UET + Stat20 UC Berkeley).
   - Chia thành 5 cụm A, B, C, D, E từ trực giác thực tế đến công thức toán học chặt chẽ.
2. **56 Bài Tự Luận Chuẩn Barem (`site/tuluan.html`)**:
   - 7 chủ đề $\times$ 8 bài toán đa bước.
   - Barem điểm chi tiết đến từng 0,25đ, cẩm nang phím bấm Casio fx-580VNX / 880BTG, mẹo giải nhanh và cảnh báo bẫy điểm số.
3. **161 Câu Hỏi Trắc Nghiệm Thông Minh (`site/tracnghiem.html`)**:
   - 3 chế độ: **Luyện tập tự do** (xem giải thích tức thì), **Thi thử tính giờ** (30 phút / 25 câu ngẫu nhiên), và **Sổ tay lỗi sai** (tự động lưu câu sai vào LocalStorage để rà soát).
   - Tỷ lệ đáp án A/B/C/D cân bằng lý tưởng (25% mỗi lựa chọn).
4. **Sổ Tay Công Thức & Bảng Tra $\Phi(z)$ (`site/congthuc.html`)**:
   - 35 thẻ công thức tra cứu 1 chạm, sao chép mã KaTeX, giải thích ký hiệu và điều kiện áp dụng.
   - Bảng tra tương tác cho phân phối chuẩn tắc $\Phi(z)$ từ $0{,}00$ đến $3{,}09$.
5. **4 Bộ Đề Thi Thử Giữa Kỳ Chuẩn UET (`site/dethi.html`)**:
   - 90 phút mô phỏng đề thi thật: 50% trắc nghiệm (20 câu) + 50% tự luận (2-3 bài lớn).
   - Tự động đếm ngược thời gian, chấm điểm trắc nghiệm tức thì và barem tự chấm chi tiết từng 0,25đ.
6. **Cổng Thông Tin & Lộ Trình Ôn Thi (`site/index.html`)**:
   - Lộ trình cấp tốc 72h (3 ngày), lộ trình chuẩn 7 ngày, và lộ trình nâng cao 14 ngày.
   - Bảng kiểm 10 bẫy điểm số chết người.

---

## 🛠️ Công Nghệ & Khởi Chạy

- **Frontend thuần túy**: HTML5, CSS3 hiện đại, Vanilla JavaScript (Zero external runtime dependencies).
- **Toán học & Ký hiệu**: KaTeX hỗ trợ render công thức cực nhanh và sắc nét.
- **Offline Ready**: Hoạt động hoàn toàn cục bộ chỉ bằng cách mở file HTML trên bất kỳ trình duyệt nào.
- **Kiểm thử tự động**: Bộ test suite Python độc lập kiểm chứng 1.365 tiêu chí.

### Chạy Kiểm Thử:
```bash
python verify/run_full_qa_suite.py
```

---

## 📖 Cấu Trúc Thư Mục

```
XSTK/
├── site/                     # Ứng dụng Web tương tác
│   ├── index.html            # Hub trung tâm & bảng điều khiển
│   ├── hoc.html              # 26 bài học vi mô
│   ├── tuluan.html           # 56 bài tự luận phân bước
│   ├── tracnghiem.html       # 161 câu trắc nghiệm 3 chế độ
│   └── congthuc.html         # Sổ tay công thức & bảng tra Phi(z)
├── content/                  # Cơ sở dữ liệu nội dung
│   ├── lessons_all.js        # Dữ liệu bài học
│   ├── tuluan_data.json      # Dữ liệu bài tập tự luận
│   ├── tracnghiem_data.json  # Dữ liệu câu hỏi trắc nghiệm
│   └── ...
├── docs/                     # Tài liệu & Lộ trình
│   ├── lotrinh.md            # Chiến thuật phòng thi & phím bấm Casio
│   ├── qa-report.md          # Báo cáo kiểm thử 1.365 tests
│   └── coverage.md           # Ma trận độ phủ chương trình
├── verify/                   # Test suite tự động
│   └── run_full_qa_suite.py  # Script kiểm thử toàn diện
├── index.html                # Cổng chuyển hướng gốc
└── vercel.json               # Cấu hình định tuyến Vercel
```

---
*Phát triển cho sinh viên Đại học Công nghệ (VNU - UET).*
