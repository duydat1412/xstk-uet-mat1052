# HƯỚNG DẪN & QUY TẮC PHÁT TRIỂN DÀNH CHO AI AGENT (AGENT GUIDELINES)

> **Dành cho mọi AI Coding Agent (Antigravity, Cursor, Claude Code, Copilot, v.v.) khi làm việc trong repository `XSTK / UET Study Hub`**.  
> **Mục tiêu**: Tối ưu tốc độ thực thi, triệt tiêu lãng phí tokens, ngăn ngừa lỗi vỡ giao diện, và bảo đảm 100% quy chuẩn kỹ thuật & sư phạm của dự án.

---

## 1. Quy Tắc Tìm Kiếm File & Định Vị Mã Nguồn (File Discovery Protocol)

### ⚠️ Điều cấm kỵ:
- **Tuyệt đối không chạy các lệnh quét đệ quy toàn bộ thư mục** như:
  - `findstr /S *.*`
  - `Get-ChildItem -Recurse`
  - `grep -r` từ thư mục gốc
  *(Lý do: Lệnh sẽ quét vào `node_modules/`, `.next/`, `.git/` với hàng trăm nghìn file, gây treo task, timeout và tràn bộ nhớ).*

### ✅ Quy trình chuẩn:
1. **Luôn mở và đọc [`DIR_TREE.md`](file:///d:/Projects/XSTK/DIR_TREE.md) trước**:
   - Tra bảng *Quick File Lookup* để lấy ngay đường dẫn file cần sửa.
2. **Đi thẳng tới file bằng công cụ chuyên dụng**:
   - Đọc file: `read_file(Path: "...")`
   - Sửa file: `edit_file(Path: "...")` hoặc `write_file(Path: "...")`
3. Nếu bắt buộc phải tìm kiếm theo từ khóa trong code:
   - Luôn giới hạn phạm vi thư mục cụ thể, ví dụ:
     `Get-ChildItem -Path components/ -Filter "*.tsx"` hoặc `Get-ChildItem -Path data/ -Filter "*.json"`.

---

## 2. Quy Chuẩn Phát Triển Giao Diện (Frontend Engineering & Design Workflow)

Mọi tác vụ can thiệp UI/UX, Component, Layout đều phải tuân thủ nghiêm ngặt quy trình 5 bước trong `.agents/skills/frontend-design-workflow`:

### 🔹 2.1. Bộ Kỹ năng (Specialist Skills) cần kích hoạt khi làm UI:
- **`frontend-design-workflow`**: Kỹ năng điều phối tổng thể quy trình phát triển frontend của dự án.
- **`ui-ux-pro-max`**: Tra cứu quy chuẩn UX, tỷ lệ khoảng cách (spacing scale), typography hierarchy, phối màu chuẩn.
- **`impeccable`**: Đánh giá và phê bình giao diện; loại bỏ triệt để các thiết kế "AI-template" rẻ tiền, bo góc lộn xộn hoặc gradient nham nhở.
- **`ui-styling`**: Hướng dẫn xây dựng và tùy biến component bằng **shadcn/ui** và **Tailwind CSS**.

### 🔹 2.2. Token hóa Biến Màu & Hỗ trợ Dark / Light Mode:
- **Tuyệt đối không dùng mã màu tĩnh đơn lập** như `#ffffff`, `bg-white` đơn thuần (gây chói lóa và hỏng chế độ Dark Mode).
- **Luôn sử dụng Semantic Design Tokens**:
  - Nền khối card: `bg-card` (đi kèm `border border-border`)
  - Nền trang / sub-card: `bg-background` hoặc `bg-muted/50`
  - Chữ chính: `text-foreground`
  - Chữ phụ / mô tả / chú thích: `text-muted-foreground`
  - Điểm nhấn / Primary: `text-blue-600 dark:text-blue-400`, `bg-blue-600`
- Khi cần màu cảnh báo / thành công:
  - Wrong: `bg-rose-50/50 dark:bg-rose-950/20 text-rose-600 dark:text-rose-400 border-rose-200/80`
  - Correct: `bg-emerald-50/50 dark:bg-emerald-950/20 text-emerald-600 dark:text-emerald-400 border-emerald-200/80`

### 🔹 2.3. Quy tắc Hiển thị Công thức Toán & Ký hiệu (KaTeX):
- **Không bao giờ render chuỗi thô chứa dấu `$` trực tiếp ra JSX**:
  - Dùng hàm [`renderMathInText(text)`](file:///d:/Projects/XSTK/components/course-study-view.tsx) để phân tích ký hiệu inline `$formula$` và khối `$$formula$$`.
- **Chống tràn màn hình**: Các khối công thức dài phải nằm trong container có class `overflow-x-auto`.
- **Chống lỗi font tiếng Việt**: Đảm bảo thẻ cha kế thừa `font-sans` để dấu tiếng Việt không bị tách rời khỏi ký tự.

### 🔹 2.4. Trải nghiệm Mobile-First & Responsive:
- Mọi bố cục phải được tối ưu cho màn hình điện thoại (375px $\to$ 430px):
  - Sidebar danh sách bài học trên mobile bắt buộc dùng component **`Sheet` (Drawer trượt)**.
  - Không bao giờ để xuất hiện thanh cuộn ngang trang (**Zero Horizontal Overflow**).
  - Khoảng cách lề và padding trên mobile: ưu tiên `px-3 sm:px-6`, `py-3 sm:py-6`.

### 🔹 2.5. Hình ảnh Minh họa Sơ đồ & Lightbox Modal:
- Khi đưa hình ảnh sơ đồ vào Ví dụ mẫu hoặc Câu hỏi trắc nghiệm:
  - Khai báo trường `image` (đường dẫn `/illustrations/...`) và `caption`.
  - Bắt buộc gắn sự kiện `onClick` gọi `setZoomedImage` để mở **Lightbox Modal phóng to**, cho phép học viên xem rõ từng chi tiết trên màn hình nhỏ.

---

## 3. Tích Hợp Các MCP Servers & Công Cụ Mở Rộng Để Tăng Hiệu Quả

Để giải quyết công việc nhanh và chính xác nhất, Agent nên chủ động tận dụng các MCP servers và CLI đã được tích hợp sẵn trong môi trường:

| Công cụ / MCP Server | Mục đích sử dụng | Cách tận dụng hiệu quả |
| :--- | :--- | :--- |
| **`context7` / `context7_context7`** | Tra cứu Docs thư viện & Framework | Khi gặp cú pháp mới của Next.js 16 App Router, React 19, Tailwind CSS v4 hay Radix UI, dùng tool `resolve-library-id` và `query-docs` để đọc API docs chuẩn thay vì đoán mò. |
| **`twg` (Atlassian TWG CLI)** | Quản lý Công việc & Issue trên Jira | Tài khoản `duygk45@gmail.com` tại site `duygk45.atlassian.net` đã được xác thực sẵn. Dùng lệnh `twg jira workitem create`, `query`, `update` để tạo hoặc đồng bộ các task, user story, bug cho đồ án môn học (ví dụ: dự án `DLKB`, `KAN`). |
| **`github-mcp-server`** | Tương tác với GitHub Repository | Dùng để tra cứu commit history, kiểm tra pull requests, issues, và rà soát kết quả chạy của GitHub Actions CI/CD mà không cần mở trình duyệt. |
| **`canva_canva`** | Thiết kế Đồ họa & Banner minh họa | Khi cần tạo banner, visual assets học tập hoặc xuất file thiết kế cho môn học, gọi các API Canva để sinh mẫu và tải asset về `public/`. |
| **`robloxstudio` / `Roblox_Studio`** | Phát triển 3D & Mô phỏng Không gian | Sẵn sàng phục vụ khi dự án mở rộng các mô-đun thực hành tương tác không gian 3D. |

---

## 4. Quy Chuẩn Sư Phạm Khóa Học UET (UET Pedagogy Standard)

Mọi bài học trong cả hai môn `XSTK MAT1052` và `CSDL INT2207` bắt buộc tuân theo 5 quy chuẩn:
1. **Sequential Section Stepper**: Không nhảy cóc; luồng học phải đi từ Lý thuyết $\to$ 3 Ví dụ $\to$ Cạm bẫy $\to$ Bài kiểm tra.
2. **3 Ví dụ mẫu bám 100% Slide Giảng viên**: Phân cấp rõ 3 mức (Cơ bản, Trung bình, Vận dụng) với số liệu thật từ slide UET.
3. **Tối thiểu 2 Cạm bẫy thi cử**: Trình bày dưới dạng đối chiếu song song: *Cách nghĩ sai phổ biến ❌* vs *Quy tắc chuẩn thi UET ✅*.
4. **Bài kiểm tra Gatekeeper 3 cấp độ**:
   - Cấp 1 (Nhận biết): Ký hiệu, định nghĩa, hình vẽ cơ bản.
   - Cấp 2 (Thông hiểu): Tính toán trực tiếp 1 công thức, đọc lược đồ.
   - Cấp 3 (Vận dụng & Cạm bẫy): Bài toán nhiều bước, phát hiện bẫy ngộ nhận.
   - *Quy tắc khóa*: Bắt buộc đúng 3/3 câu mới mở khóa bài tiếp theo.
5. **Dấu Ref Tra cứu Slide**: Cuối mỗi bài phải có khung tra cứu với `slide_file`, `pages`, `section`, `remind` và nút bấm mở slide trực tiếp.

---

## 5. Quy Trình Kiểm Thử & Nghiệm Thu Bắt Buộc (Quality Gate Checklist)

Trước khi commit bất kỳ thay đổi nào hoặc báo hoàn thành với người dùng:

- [ ] **Kiểm tra Kiểu dữ liệu**:
  ```powershell
  npm run typecheck
  ```
  *(Phải đạt 0 lỗi)*
- [ ] **Chạy Bộ QA Audit Toàn diện (2.733 assertions)**:
  ```powershell
  npm run test:qa
  ```
  *(Phải đạt 100% Pass, không có warning hoặc fail)*
- [ ] **Kiểm tra Production Build**:
  ```powershell
  npm run build
  ```
  *(Next.js phải build thành công và xuất đủ các static pages)*
- [ ] **Kiểm thử Trực quan Giao diện (Playwright Browser Test)**:
  - Nếu có thay đổi UI hoặc CSS, chạy script Playwright trong `verify/` để kiểm tra render và chụp ảnh bằng chứng nghiệm thu (Evidence-based reporting).
