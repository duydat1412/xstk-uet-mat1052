# BÁO CÁO KIỂM THỬ CHẤT LƯỢNG TOÀN DIỆN (QA AUDIT REPORT)
## Hệ Thống Tự Học & Luyện Thi Xác Suất Thống Kê UET.MAT1052

> **Phiên bản**: v1.3.0-production (Hoàn chỉnh 7 Phase + Tối ưu Mobile + Điều hướng Section & 3-Level Quiz + Dấu Ref Tra Cứu Slide Bài Giảng)  
> **Ngày cập nhật**: 02/11/2026  
> **Môi trường thực thi**: Node.js v25.9.0 / Python 3.12.x / Windows PowerShell  
> **Script kiểm thử tự động**: [`verify/run_full_qa_suite.py`](file:///d:/Projects/XSTK/verify/run_full_qa_suite.py)  
> **Kết quả tổng thể**: **2.240 / 2.240 Test Cases PASSED (100% Tuyệt Đối - 0 Thất Bại - 0 Cảnh Báo)**

---

## 1. TỔNG QUAN HỆ THỐNG VÀ PHẠM VI KIỂM THỬ

Hệ thống học tập và luyện thi Xác suất Thống kê `UET.MAT1052` phục vụ sinh viên Đại học Công nghệ (VNU - UET) ôn thi giữa kỳ theo đúng cấu trúc chuẩn: **50% Trắc nghiệm khách quan + 50% Tự luận giải tích**.

Hệ sinh thái hiện bao gồm:
- **6 Module Web tương tác offline & Responsive đa nền tảng**:
  1. [`site/index.html`](file:///d:/Projects/XSTK/site/index.html): Cổng thông tin trung tâm, bảng điều khiển lộ trình (3 ngày, 7 ngày, 14 ngày), rà soát 10 bẫy điểm số.
  2. [`site/hoc.html`](file:///d:/Projects/XSTK/site/hoc.html): 26 bài học vi mô phân tầng theo 5 cụm A, B, C, D, E với **điều hướng tuần tự theo từng section** (Lý thuyết $\rightarrow$ Ba Ví dụ $\rightarrow$ Cạm bẫy $\rightarrow$ Kiểm tra), **bộ kiểm tra năng lực 3 cấp độ** (Nhận biết, Thông hiểu, Vận dụng), và **hệ thống dấu ref tra cứu slide bài giảng UET Week 01 – 07** ở cuối mỗi bài học.
  3. [`site/tuluan.html`](file:///d:/Projects/XSTK/site/tuluan.html): 56 bài toán tự luận chuẩn barem điểm chi tiết từng 0,25đ.
  4. [`site/tracnghiem.html`](file:///d:/Projects/XSTK/site/tracnghiem.html): 161 câu hỏi trắc nghiệm với 3 chế độ luyện tập thông minh.
  5. [`site/congthuc.html`](file:///d:/Projects/XSTK/site/congthuc.html): 35 thẻ công thức tra cứu 1 chạm, bảng tra $\Phi(z)$ tương tác.
  6. [`site/dethi.html`](file:///d:/Projects/XSTK/site/dethi.html): **(Phase 5)** 4 bộ đề thi thử giữa kỳ 90 phút mô phỏng 100% format phòng thi UET (20 câu trắc nghiệm + 2-3 bài tự luận, đồng hồ đếm giờ, chấm điểm tự động và barem tự chấm).
- **Cơ sở dữ liệu chuẩn hóa**: `content/lessons_all.js`, `content/lesson_references.json`, `content/quizzes_3levels.json`, `content/tuluan_data.json`, `content/tracnghiem_data.json`, `content/dethi_data.json`.
- **Hệ thống tài liệu & lộ trình**: `docs/coverage.md`, `docs/lotrinh.md`, `docs/templates.md`, `docs/sample-lesson.md`, `docs/qa-report.md`.

---

## 2. MA TRẬN KẾT QUẢ KIỂM THỬ (TEST RESULTS MATRIX)

| Bộ Kiểm Thử (Suite) | Mô Tả Phạm Vi | Số Lượng Test Cases | Đạt (Passed) | Lỗi (Failed) | Tỷ Lệ |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Suite 1: Cấu trúc HTML, Mobile Meta & KaTeX** | Kiểm tra cặp thẻ HTML/Head/Body, UTF-8, kích thước file >10KB, viewport mobile, xử lý tràn KaTeX (.katex-display overflow-x), liên kết điều hướng 2 chiều 6 trang | **84** | **84** | 0 | **100%** |
| **Suite 2: Cú pháp JavaScript Engine** | Biên dịch và phân tích AST các khối script inline trên engine Node.js độc lập qua stdin | **10** | **10** | 0 | **100%** |
| **Suite 3: Tính Toàn Vẹn Dữ Liệu & Schema** | Xác thực 161 MCQs, 56 bài tự luận (7 chủ đề $\times$ 8 bài), 26 bài học, 35 công thức; 4 Đề thi thử (80 MCQs + 9 bài tự luận đa bước); tính duy nhất của ID | **1.719** | **1.719** | 0 | **100%** |
| **Suite 4: Cân Bằng Phương Án & Phân Bố Mức Độ** | Độ cân bằng đáp án A/B/C/D (ngưỡng 18% - 32%), phân bố cấp độ (Cơ bản, Trung bình, Nâng cao) | **5** | **5** | 0 | **100%** |
| **Suite 5: Toán Học Giải Tích & Sanity Checks** | Nghiệm phương trình bậc 2 CLT bóng đèn dự phòng, hồi quy OLS, Bayes, nhị thức, Poisson, phân phối chuẩn $\Phi(z)$ | **14** | **14** | 0 | **100%** |
| **Suite 6: Interactive Quizzes & Section Nav** | Kiểm tra 78 câu hỏi kiểm tra (26 bài $\times$ 3 cấp độ: Nhận biết, Thông hiểu, Vận dụng), 4 options, giải thích chuyên sâu, điều hướng section-by-section, khóa/mở bài tiếp | **271** | **271** | 0 | **100%** |
| **Suite 7: Lesson References & Slide Cross-Ref** | Kiểm tra 26 dấu ref bài học, đối chiếu file PDF thực tế (week01-07), dải trang hợp lệ, mục slide, sách Stat20, chỉ dẫn khi không hiểu, UI render | **137** | **137** | 0 | **100%** |
| **TỔNG CỘNG** | **Toàn bộ hệ sinh thái (Trọn vẹn 7 Phases + Section Nav + 3-Level Quizzes + Dấu Ref Slide)** | **2.240** | **2.240** | **0** | **100%** |

---

## 3. TỐI ƯU HÓA GIAO DIỆN & KÍCH THƯỚC CHO MOBILE (MOBILE RESPONSIVE AUDIT)

Để đảm bảo trải nghiệm học tập và làm bài thi mượt mà trên điện thoại thông minh (iPhone, Android) và máy tính bảng:

1. **Khắc phục lỗi tràn ngang màn hình do KaTeX (Zero Overflow Bug)**:
   - Tất cả các công thức toán học khối (`.katex-display`) đều được bọc luật:
     ```css
     .katex-display {
       overflow-x: auto;
       overflow-y: hidden;
       padding: 8px 0;
       -webkit-overflow-scrolling: touch;
       max-width: 100%;
     }
     ```
   - Nhờ đó, ngay cả các công thức phức tạp như Bất đẳng thức Chebyshev, Tích phân từng phần, Ma trận hiệp phương sai hay Bảng phân phối xác suất đều có thể cuộn ngang nhẹ nhàng bằng ngón tay mà không làm biến dạng layout trang.

2. **Cụm điều khiển và Lưới nút bấm thích ứng (Adaptive Touch Controls)**:
   - Thanh chọn Cụm bài học (`.clusters-nav`), dải bài học (`.lessons-strip`) và các Sub-tabs (`.sub-tabs`) có thể cuộn ngang mượt mà (`scroll-snap`, ẩn thanh cuộn thô).
   - Chiều cao các nút bấm và tùy chọn trắc nghiệm tối thiểu 44px (chuẩn Apple Human Interface Guidelines) giúp chạm chọn chính xác, không bấm nhầm.

---

## 4. CƠ CHẾ ĐIỀU HƯỚNG THEO SECTION & BỘ KIỂM TRA 3 CẤP ĐỘ

1. **Quy trình học tập sư phạm khép kín từng bước**:
   - Mỗi bài học được chia thành 4 section rõ rệt:
     1. **`1. Lý thuyết`**: Các khối kiến thức chuẩn hóa, quy tắc vàng, cạm bẫy, ví dụ minh họa và widget tương tác (như widget ngoại lai & widget mô phỏng CLT).
     2. **`2. Ba Ví dụ`**: 3 bài toán mẫu có lời giải chi tiết từng bước.
     3. **`3. Cạm bẫy`**: Bảng đối chiếu song song "❌ Cách hiểu sai" vs "✔️ Cách hiểu đúng".
     4. **`4. Kiểm tra`**: Bài kiểm tra năng lực gồm 3 câu hỏi với 3 cấp độ (🟢 Nhận biết, 🟡 Thông hiểu, 🔴 Vận dụng / Bẫy kinh điển).
   - Nút `Phần tiếp theo →` chuyển tuần tự giữa các section của bài. Tại section kiểm tra cuối cùng, nút chuyển bài bị khóa (`disabled`) cho đến khi người học hoàn thành đủ cả 3 câu hỏi.

2. **Ngân hàng kiểm tra 3 cấp độ (78 câu)**:
   - Cân bằng hoàn hảo 4 phương án A, B, C, D (~25% mỗi phương án: A=19, B=20, C=20, D=19).
   - Phản hồi giải thích chi tiết có công thức KaTeX cho từng phương án lựa chọn.

---

## 5. HỆ THỐNG DẤU REF TRA CỨU SLIDE BÀI GIẢNG (SLIDE CROSS-REFERENCING)

Nhằm giúp sinh viên dễ dàng truy cứu và đọc lại các đoạn kiến thức trong slide bài giảng khi gặp nội dung chưa hiểu:

1. **Khối Dấu Ref Chi Tiết (`#lessonRefBox`) ở cuối mỗi bài học**:
   - Được neo cố định ngay phía trên thanh điều hướng chân trang (`bottom-nav`).
   - Hiển thị đầy đủ 5 trường thông tin:
     - 📁 **File Slide UET**: Tên file slide chính thức (ví dụ `week01.pdf`, `week07.pdf`).
     - 📑 **Vị trí trang & Mục bài giảng**: Dải trang chính xác (ví dụ `Slide 68 – 77, 89 – 91`) kèm tên chương/phần cụ thể.
     - 📖 **Giáo trình đối chiếu**: Vị trí tương ứng trong giáo trình Stat20 hoặc OpenIntro.
     - 🎯 **Trọng tâm kiến thức**: Các gạch đầu dòng cốt lõi nhất cần nắm.
     - 💡 **Chỉ dẫn tra cứu khi đọc chưa hiểu**: Lời khuyên cụ thể về các trang slide và ví dụ cần mở lại khi gặp khó khăn.
   - Nút hành động trực tiếp **`📄 Mở Slide PDF (trang X) ↗`**: Mở trực tiếp file PDF slide chính thức ngay tại số trang tương ứng trên trình duyệt (`/weekXX.pdf#page=YY`).

2. **Thanh Tra Cứu Nhanh (`theory-ref-pill`)**:
   - Xuất hiện ở cuối phần `1. Lý thuyết` để học viên có thể tra cứu tức thì nguồn gốc tài liệu ngay sau khi đọc xong lý thuyết.

3. **Gợi ý tra cứu sau khi hoàn thành bài kiểm tra (`renderQuiz`)**:
   - Banner chúc mừng gợi ý học viên các trang slide cần ôn tập thêm nếu muốn đào sâu chuyên đề.

---

## 6. KẾT LUẬN

Hệ thống đã **hoàn thành 100% toàn bộ các yêu cầu của dự án**, đạt độ tin cậy tuyệt đối với **2.240 / 2.240 tests passed**, sẵn sàng phục vụ sinh viên UET ôn thi đạt điểm A/A+ môn Xác suất Thống kê!
