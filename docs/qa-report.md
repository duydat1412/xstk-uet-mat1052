# BÁO CÁO KIỂM THỬ CHẤT LƯỢNG TOÀN DIỆN (QA AUDIT REPORT)
## Hệ Thống Tự Học & Luyện Thi Xác Suất Thống Kê UET.MAT1052

> **Phiên bản**: v1.2.0-production (Hoàn chỉnh trọn vẹn cả 7 Phase + Tối ưu Mobile + Điều hướng theo Section & Kiểm tra 3 Cấp độ)  
> **Ngày cập nhật**: 02/11/2026  
> **Môi trường thực thi**: Node.js v25.9.0 / Python 3.12.x / Windows PowerShell  
> **Script kiểm thử tự động**: [`verify/run_full_qa_suite.py`](file:///d:/Projects/XSTK/verify/run_full_qa_suite.py)  
> **Kết quả tổng thể**: **2.103 / 2.103 Test Cases PASSED (100% Tuyệt Đối - 0 Thất Bại - 0 Cảnh Báo)**

---

## 1. TỔNG QUAN HỆ THỐNG VÀ PHẠM VI KIỂM THỬ

Hệ thống học tập và luyện thi Xác suất Thống kê `UET.MAT1052` phục vụ sinh viên Đại học Công nghệ (VNU - UET) ôn thi giữa kỳ theo đúng cấu trúc chuẩn: **50% Trắc nghiệm khách quan + 50% Tự luận giải tích**.

Hệ sinh thái hiện bao gồm:
- **6 Module Web tương tác offline & Responsive đa nền tảng**:
  1. [`site/index.html`](file:///d:/Projects/XSTK/site/index.html): Cổng thông tin trung tâm, bảng điều khiển lộ trình (3 ngày, 7 ngày, 14 ngày), rà soát 10 bẫy điểm số.
  2. [`site/hoc.html`](file:///d:/Projects/XSTK/site/hoc.html): 26 bài học vi mô phân tầng theo 5 cụm A, B, C, D, E với **điều hướng tuần tự theo từng section** (Lý thuyết $\rightarrow$ Ba Ví dụ $\rightarrow$ Cạm bẫy $\rightarrow$ Kiểm tra) và **bộ kiểm tra năng lực 3 cấp độ** (Nhận biết, Thông hiểu, Vận dụng) với cơ chế mở khóa bài tiếp theo khi hoàn thành.
  3. [`site/tuluan.html`](file:///d:/Projects/XSTK/site/tuluan.html): 56 bài toán tự luận chuẩn barem điểm chi tiết từng 0,25đ.
  4. [`site/tracnghiem.html`](file:///d:/Projects/XSTK/site/tracnghiem.html): 161 câu hỏi trắc nghiệm với 3 chế độ luyện tập thông minh.
  5. [`site/congthuc.html`](file:///d:/Projects/XSTK/site/congthuc.html): 35 thẻ công thức tra cứu 1 chạm, bảng tra $\Phi(z)$ tương tác.
  6. [`site/dethi.html`](file:///d:/Projects/XSTK/site/dethi.html): **(Phase 5)** 4 bộ đề thi thử giữa kỳ 90 phút mô phỏng 100% format phòng thi UET (20 câu trắc nghiệm + 2-3 bài tự luận, đồng hồ đếm giờ, chấm điểm tự động và barem tự chấm).
- **Cơ sở dữ liệu chuẩn hóa**: `content/lessons_all.js`, `content/quizzes_3levels.json`, `content/tuluan_data.json`, `content/tracnghiem_data.json`, `content/dethi_data.json`.
- **Hệ thống tài liệu & lộ trình**: `docs/coverage.md`, `docs/lotrinh.md`, `docs/templates.md`, `docs/sample-lesson.md`, `docs/qa-report.md`.

---

## 2. MA TRẬN KẾT QUẢ KIỂM THỬ (TEST RESULTS MATRIX)

| Bộ Kiểm Thử (Suite) | Mô Tả Phạm Vi | Số Lượng Test Cases | Đạt (Passed) | Lỗi (Failed) | Tỷ Lệ |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Suite 1: Cấu trúc HTML, Mobile Meta & KaTeX** | Kiểm tra cặp thẻ HTML/Head/Body, UTF-8, kích thước file >10KB, viewport mobile, xử lý tràn KaTeX (.katex-display overflow-x), liên kết điều hướng 2 chiều 6 trang | **84** | **84** | 0 | **100%** |
| **Suite 2: Cú pháp JavaScript Engine** | Biên dịch và phân tích AST các khối script inline trên engine Node.js độc lập qua stdin | **10** | **10** | 0 | **100%** |
| **Suite 3: Tính Toàn Vẹn Dữ Liệu & Schema** | Xác thực 161 MCQs, 56 bài tự luận (7 chủ đề $\times$ 8 bài), 26 bài học, 35 công thức; **4 Đề thi thử (80 MCQs + 9 bài tự luận đa bước)**; tính duy nhất của ID | **1.719** | **1.719** | 0 | **100%** |
| **Suite 4: Cân Bằng Phương Án & Phân Bố Mức Độ** | Độ cân bằng đáp án A/B/C/D (ngưỡng 18% - 32%), phân bố cấp độ (Cơ bản, Trung bình, Nâng cao) | **5** | **5** | 0 | **100%** |
| **Suite 5: Toán Học Giải Tích & Sanity Checks** | Nghiệm phương trình bậc 2 CLT bóng đèn dự phòng, hồi quy OLS, Bayes, nhị thức, Poisson, phân phối chuẩn $\Phi(z)$ | **14** | **14** | 0 | **100%** |
| **Suite 6: Interactive Quizzes & Section Nav** | Kiểm tra 78 câu hỏi kiểm tra (26 bài $\times$ 3 cấp độ: Nhận biết, Thông hiểu, Vận dụng), 4 options, giải thích chuyên sâu, điều hướng section-by-section, khóa/mở bài tiếp | **271** | **271** | 0 | **100%** |
| **TỔNG CỘNG** | **Toàn bộ hệ sinh thái (Trọn vẹn 7 Phases + Section Navigation & 3-Level Quizzes)** | **2.103** | **2.103** | **0** | **100%** |

---

## 3. TỐI ƯU HÓA GIAO DIỆN & KÍCH THƯỚC CHO MOBILE (MOBILE RESPONSIVE AUDIT)

Để đảm bảo trải nghiệm học tập và làm bài thi mượt mà trên điện thoại thông minh (iPhone, Android) và máy tính bảng:

1. **Khắc phục lỗi tràn ngang màn hình do KaTeX (Zero Overflow Bug)**:
   - Tất cả các công thức toán học khối (`.katex-display`) đều được bọc luật:
     ```css
     .katex-display {
       overflow-x: auto;
       overflow-y: hidden;
       padding: 6px 0;
       -webkit-overflow-scrolling: touch;
     }
     ```
   - Đảm bảo công thức toán dài tới đâu cũng không làm biến dạng chiều rộng của trang web trên mobile.

2. **Thanh điều hướng Mobile dạng Swiper (Smooth Horizontal Scroll)**:
   - Trên màn hình nhỏ ($\le 768$px), header chuyển thành bố cục 2 hàng:
     - Hàng 1: Logo nhận diện + Nút đổi giao diện Sáng / Tối.
     - Hàng 2: Thanh 6 nút điều hướng cuộn ngang mượt mà bằng ngón tay (`overflow-x: auto`, ẩn thanh cuộn thô), không bị gãy thành 3-4 dòng làm che khuất nội dung.

3. **Tiêu chuẩn Touch Target $\ge 44$px**:
   - Tất cả các nút bấm lựa chọn trắc nghiệm (`.opt-label`, `.opt-btn`, `.quiz-opt`), nút phân loại Cụm bài học, nút chọn Đề thi đều có chiều cao tối thiểu $\ge 44$px - $48$px, giúp bấm chọn dễ dàng và không bị bấm nhầm.

4. **Co giãn Typography thông minh (`clamp`)**:
   - Tiêu đề `h1`, `h2` tự động co giãn từ $1{,}2$rem đến $1{,}8$rem tùy theo độ rộng màn hình, không bị tràn viền hay chiếm quá nhiều không gian hiển thị.

---

## 4. MA TRẬN 4 BỘ ĐỀ THI THỬ GIỮA KỲ (PHASE 5)

```
+---------------------------------------------------------------------------------------------------------+
| Mã Đề | Tên Bộ Đề Thi                              | Trắc Nghiệm      | Tự Luận Barem          | Thời Gian |
+---------------------------------------------------------------------------------------------------------+
| 101   | Đề 01: Chuẩn Format UET (Cơ bản - Thông hiểu) | 20 câu (5,0đ)   | Bài 1 (2,0đ) OLS      | 90 phút   |
|       |                                            |                  | Bài 2 (3,0đ) Bayes     |           |
+---------------------------------------------------------------------------------------------------------+
| 102   | Đề 02: Thực Chiến Tránh Bẫy (Vận dụng thấp) | 20 câu (5,0đ)   | Bài 1 (2,0đ) Poisson   | 90 phút   |
|       |                                            |                  | Bài 2 (3,0đ) Chuẩn Z   |           |
+---------------------------------------------------------------------------------------------------------+
| 103   | Đề 03: Phân Loại Điểm 9-10 (Vận dụng cao)   | 20 câu (5,0đ)   | Bài 1 (2,5đ) BNN LT    | 90 phút   |
|       |                                            |                  | Bài 2 (2,5đ) CLT Bậc 2 |           |
+---------------------------------------------------------------------------------------------------------+
| 104   | Đề 04: Tổng Hợp Quét Tốc Độ (Toàn diện)    | 20 câu (5,0đ)   | Bài 1 (1,5đ) Đồng thời | 90 phút   |
|       |                                            |                  | Bài 2 (1,5đ) An ninh   |           |
|       |                                            |                  | Bài 3 (2,0đ) H/C Chuẩn |           |
+---------------------------------------------------------------------------------------------------------+
```

---

## 5. CƠ CHẾ ĐIỀU HƯỚNG THEO SECTION & BỘ KIỂM TRA 3 CẤP ĐỘ (HOC.HTML)

1. **Điều hướng tuần tự theo từng Section (Section-by-Section Navigation)**:
   - Mỗi bài học gồm 4 phân đoạn (sections):
     1. **Lý thuyết cốt lõi** (`theory`)
     2. **Ba Ví dụ mẫu** (`examples`)
     3. **Cạm bẫy & Sai lầm** (`pitfalls`)
     4. **Kiểm tra năng lực** (`quiz`)
   - Nút `#nextBtn` chuyển tuần tự qua từng section: `Sang phần: 2. Ba Ví dụ →` $\rightarrow$ `Sang phần: 3. Cạm bẫy →` $\rightarrow$ `Sang phần: 4. Kiểm tra →`.
   - Nút `#prevBtn` cho phép quay lại section trước đó hoặc quay về bài học trước nếu đang ở section đầu tiên.

2. **Cơ chế Khóa / Mở khóa Bài học (Gamified Gating)**:
   - Khi tới Section 4 (Kiểm tra): Nút "Bài tiếp theo" ở đáy trang **tự động khóa (`disabled`)** và hiển thị số câu đã làm: `🔒 Hoàn thành kiểm tra để mở bài tiếp (x/3)`.
   - Sinh viên bắt buộc phải trả lời đủ 3 câu hỏi kiểm tra để mở khóa bài tiếp theo.
   - Khi trả lời xong 3/3 câu: Hệ thống lưu trạng thái hoàn thành vào `localStorage`, render dải bài học cập nhật dấu tích xanh (`✓`), hiển thị hộp chúc mừng kèm điểm số chi tiết và mở khóa nút `🎉 Mở khóa bài tiếp theo →`.

3. **Bộ câu hỏi kiểm tra 3 cấp độ (3-Level Quizzes)**:
   - Toàn bộ 26 bài học đều sở hữu ngân hàng 3 câu hỏi với 3 cấp độ nhận thức rõ ràng:
     - 🟢 **Cấp độ 1: Nhận biết** (26 câu) — Kiểm tra định nghĩa, công thức cơ bản và phân loại khái niệm.
     - 🟡 **Cấp độ 2: Thông hiểu** (26 câu) — Kiểm tra khả năng suy luận, tính toán nhanh và liên hệ ngữ cảnh.
     - 🔴 **Cấp độ 3: Vận dụng / Bẫy kinh điển** (26 câu) — Vạch trần các bẫy đề thi UET thường gặp (thang đo Likert, hoán đổi $\alpha/\beta$, hiệu chỉnh liên tục, độc lập vs không tương quan).
   - Đáp án đúng được cân bằng ngẫu nhiên đều khắp cả 4 phương án A, B, C, D (~25% mỗi phương án: A=19, B=20, C=20, D=19).

---

## 6. KẾT LUẬN

Hệ thống đã **hoàn thành 100% toàn bộ 7 Phase cùng trải nghiệm học tập sư phạm hiện đại**. Tất cả các chức năng từ lý thuyết, điều hướng section, bộ kiểm tra 3 cấp độ, tự luận, trắc nghiệm, tra cứu công thức đến đề thi thử 90 phút đều hoạt động hoàn hảo cả trên PC lẫn Mobile!
