# UET Interactive Course Pedagogy Standard (Quy chuẩn Sư phạm & Thiết kế Khóa học Tương tác UET)

Tài liệu này là quy chuẩn bắt buộc áp dụng cho mọi môn học trong hệ thống **UET Study Hub** (`Xác suất Thống kê MAT1052`, `Cơ sở dữ liệu INT2207`, và các môn học mở rộng tiếp theo).

---

## 1. Triết lý Sư phạm & Trải nghiệm Người học (Core UX Flow)

Mọi bài học trong hệ sinh thái đều phải tuân thủ nghiêm ngặt luồng học tập tương tác phân đoạn (Section Stepper), tuyệt đối không để người học đọc lướt thụ động hoặc bị choáng ngợp bởi một văn bản dài:

### 🔹 Quy tắc 1: Điều hướng Section tuần tự (Sequential Section Stepper)
- Không bao giờ cho phép nút điều hướng ("Trang trước / Tiếp theo") nhảy cóc nguyên cả bài học.
- Luồng duyệt bài bắt buộc phải đi qua từng section nhỏ:
  $$\text{Bước 1 (Lý thuyết)} \longrightarrow \text{Bước 2 (Lý thuyết)} \longrightarrow \dots \longrightarrow \text{3 Ví dụ mẫu} \longrightarrow \text{Cạm bẫy} \longrightarrow \text{Bài kiểm tra}$$
- Chỉ khi đã duyệt tới section cuối cùng (Bài kiểm tra) và hoàn thành đạt yêu cầu thì nút "Chuyển sang bài tiếp theo" mới được kích hoạt.

### 🔹 Quy tắc 2: Bài kiểm tra 3 cấp độ chặn chuyển bài (3-Level Gatekeeper Quiz)
- Mỗi bài học bắt buộc kết thúc bằng một bài kiểm tra trắc nghiệm gồm đúng **3 câu hỏi** với 3 cấp độ nhận thức phân định rõ rệt:
  1. 🟢 **Cấp độ 1 — Nhận biết (Recall & Definitions)**: Kiểm tra định nghĩa, ký hiệu, phân loại biến/khái niệm cơ bản.
  2. 🟡 **Cấp độ 2 — Thông hiểu (Comprehension & Formula/Syntax)**: Áp dụng trực tiếp 1 công thức, quy tắc cốt lõi hoặc câu lệnh để tính toán ra đáp số.
  3. 🔴 **Cấp độ 3 — Vận dụng & Cạm bẫy (Application & Trap Detection)**: Tình huống thực tế nhiều bước, phát hiện bẫy ngộ nhận, phân tích sai lầm kinh điển trong đề thi.
- **Cơ chế khóa (Gatekeeper)**: Người học bắt buộc phải làm đúng cả 3 câu thì mới hoàn thành bài học và mở khóa bài tiếp theo.

### 🔹 Quy tắc 3: 100% Ví dụ mẫu bám sát Slide Giảng viên (Lecture-Aligned Examples)
- Tuyệt đối không tự sáng tác các ví dụ ngẫu nhiên, xa lạ hoặc không liên quan tới phong cách ra đề của trường.
- Mỗi bài học có đúng **3 ví dụ giải mẫu phân cấp** (Cơ bản, Trung bình, Vận dụng) trích xuất trực tiếp hoặc bám khít 100% ngữ cảnh, số liệu, bài toán xuất hiện trong slide bài giảng (PDF/PPTX) của giảng viên UET.

### 🔹 Quy tắc 4: Cạm bẫy thi cử thực chiến (Exam Pitfalls & Anti-Patterns)
- Mỗi bài học bắt buộc có tối thiểu **2 cạm bẫy đề thi** thường gặp nhất, được trình bày dưới dạng đối chiếu song song:
  - ❌ **Cách nghĩ sai phổ biến**: Chỉ rõ sai lầm sinh viên hay mắc phải khi làm bài thi.
  - ✅ **Cách nghĩ chuẩn**: Quy tắc tư duy chính xác để không bao giờ mất điểm oan.

### 🔹 Quy tắc 5: Dấu Ref tra cứu Slide bài giảng (Lecture Reference Metadata)
- Cuối mỗi bài học bắt buộc có khung tra cứu với đầy đủ các trường:
  - `slide_file`: Tên file slide PDF/PPTX tương ứng.
  - `pages` / `page_start` - `page_end`: Số trang chính xác trong slide.
  - `section`: Đề mục tương ứng trong bài giảng của thầy cô.
  - `remind`: Lời nhắc định hướng sinh viên mở lại trang nào khi gặp khó khăn.
  - Nút bấm trực tiếp mở file tài liệu nhảy tới đúng trang.

### 🔹 Quy tắc 6: Kiến trúc Cổng học tập tích hợp (Multi-Subject Study Hub Architecture)
- Mọi môn học mới đều được tích hợp chung trong domain hiện tại theo mô hình Portal Hub:
  - Đường dẫn gốc `/` là trang chọn môn (UET Study Hub).
  - Mỗi môn có một phân hệ chuyên biệt (`/xstk/...`, `/csdl/...`) gồm đầy đủ 5 công cụ: Học tương tác (`hoc`), Trắc nghiệm (`tracnghiem`), Tự luận chuẩn barem (`tuluan`), Sổ tay tra cứu (`congthuc`/`cheatsheet`), Thi thử bấm giờ (`dethi`).
  - Thanh Navbar toàn hệ thống luôn có **Course Switcher** để chuyển môn nhanh trong 1 cú click.
  - Luôn đảm bảo tính tương thích ngược cho các URL cũ.

---

## 2. Quy chuẩn Workflow Thiết kế & Phát triển Giao diện (Frontend Design & Implementation Workflow Standard)

Mọi tác vụ can thiệp hoặc phát triển giao diện (UI/UX, HTML/CSS/JS, Component, Layout) trong toàn bộ dự án bắt buộc phải tuân thủ quy trình hợp nhất 5 giai đoạn được định nghĩa chi tiết trong skill `.agents/skills/frontend-design-workflow`:

1. **Spec trước, Code sau**: Sử dụng `ui-ux-pro-max` để thiết lập định hướng thiết kế, bảng màu, typography và UX pattern trước khi viết code.
2. **Mài giũa chuẩn cao cấp**: Dùng `impeccable` phê bình phân cấp thị giác, khoảng trắng, độ tương phản và triệt tiêu các mẫu thiết kế "AI-template". Tuyệt đối không tùy ý phá vỡ bản sắc nhận diện sẵn có của dự án.
3. **Thành phần chuẩn mực**: Ưu tiên tái sử dụng hệ thống component chuẩn `shadcn/ui`, bao quát trọn vẹn các trạng thái tương tác (`hover`, `focus`, `loading`, `error`, `empty`).
4. **Token hóa với Tailwind CSS**: Tạo kiểu nhất quán thông qua các design tokens và utility classes, đảm bảo layout responsive mượt mà trên Mobile, Tablet, Desktop.
5. **Nghiệm thu trực quan bắt buộc**: Mọi thay đổi UI đáng kể đều phải được kiểm tra thực tế trên trình duyệt (browser-based verification), đảm bảo không lỗi hiển thị, không tràn ngang và đạt chuẩn tiếp cận WCAG.

