# TỔNG QUAN VÀ HIỆN TRẠNG DỰ ÁN (PROJECT CONTEXT)

> **Cập nhật gần nhất**: Tháng 11/2026  
> **Tên hệ thống**: **UET Study Hub** (Cổng học tập & ôn thi tương tác đa môn UET)  
> **Repository GitHub**: [`duydat1412/xstk-uet-mat1052`](https://github.com/duydat1412/xstk-uet-mat1052)  
> **Môi trường Production (Vercel)**: [`xstk-uet-mat1052.vercel.app`](https://xstk-uet-mat1052.vercel.app)  
> **Chủ sở hữu & Quản trị**: Trần Duy ([@duydat1412](https://github.com/duydat1412) - `duygk45@gmail.com`)  

---

## 1. Mục tiêu & Triết lý Dự án

**UET Study Hub** là nền tảng học tập trực tuyến tương tác cao, được thiết kế chuyên biệt cho sinh viên **Trường Đại học Công nghệ – Đại học Quốc gia Hà Nội (VNU-UET)**.

Dự án giải quyết triệt để các nhược điểm truyền thống của việc ôn thi:
1. **Chống đọc lướt thụ động**: Áp dụng luồng học tập phân đoạn tuần tự (**Section Stepper**), chia nhỏ kiến thức thành từng bước súc tích, đi kèm câu hỏi tương tác ngay tại chỗ.
2. **Bám sát 100% đề cương & slide giảng viên UET**: Không tự sáng tác lý thuyết hay ví dụ xa lạ; toàn bộ dữ liệu, ví dụ mẫu, số liệu và bài tập đều trích xuất trực tiếp từ bài giảng chính quy của các thầy cô UET.
3. **Phòng ngừa cạm bẫy thi cử thực chiến**: Mỗi bài học trang bị các khối đối chiếu **Cách nghĩ sai phổ biến ❌** và **Quy tắc chuẩn thi UET ✅** để triệt tiêu các lỗi mất điểm kinh điển.
4. **Cơ chế chốt chặn kiến thức (Gatekeeper Quiz)**: Bắt buộc sinh viên phải vượt qua bài kiểm tra 3 cấp độ nhận thức (Nhận biết $\to$ Thông hiểu $\to$ Vận dụng) mới được mở khóa bài học kế tiếp.

---

## 2. Các Môn Học & Cụm Kiến Thức Hiện Có

Hệ thống hoạt động theo kiến trúc **Portal Hub Đa môn (Multi-Subject Study Hub)**:
- Trang chủ `/` là Cổng chọn môn học (UET Study Hub Portal).
- Mỗi môn có phân hệ URL riêng biệt và thanh chuyển môn nhanh (**Course Switcher**) trong thanh điều hướng trên cùng.

### 2.1. Phân hệ Xác suất Thống kê (`MAT1052` - `/xstk/hoc`)
- **Số lượng bài học**: **26 bài học** hoàn chỉnh, chia thành **5 Cụm kiến thức**:
  - **Cụm A: Dữ liệu & Thống kê Mô tả** (A1 $\to$ A5): Khung dữ liệu, bảng tần số, liên hợp, tâm, phân tán, hình dạng phân phối, hồi quy OLS đơn giản, biến chỉ báo.
  - **Cụm B: Xác suất & Biến ngẫu nhiên** (B1 $\to$ B5): Không gian mẫu, biến cố, xác suất cổ điển, công thức xác suất đầy đủ & định lý Bayes.
  - **Cụm C: Phân phối Xác suất Rời rạc** (C1 $\to$ C6): Phân phối Đều rời rạc, Bernoulli, Nhị thức (Binomial), Poisson, Siêu bội (Hypergeometric), Hình học (Geometric).
  - **Cụm D: Tổng biến & Biến Liên tục** (D1 $\to$ D4): Phân phối Chuẩn (Normal distribution), Chuẩn hóa $Z$, Xấp xỉ Nhị thức sang Chuẩn, Định lý Giới hạn Trung tâm (CLT).
  - **Cụm E: Thống kê Suy luận & Hồi quy** (E1 $\to$ E6): Ước lượng điểm, khoảng tin cậy (CI), kiểm định giả thuyết ($Z$-test, $t$-test), hồi quy tuyến tính OLS mẫu.
- **Công cụ mở rộng đi kèm**:
  - Học tương tác phân đoạn (`/xstk/hoc`)
  - Luyện thi trắc nghiệm theo chủ đề (`site/tracnghiem.html`)
  - Luyện giải tự luận có barem chấm điểm chi tiết (`site/tuluan.html`)
  - Sổ tay tra cứu công thức nhanh (`site/congthuc.html`)
  - Thi thử bấm giờ bám sát cấu trúc đề thi UET (`site/dethi.html`)

### 2.2. Phân hệ Cơ sở Dữ liệu (`INT2207` - `/csdl/hoc`)
- **Số lượng bài học**: **14 bài học** hoàn chỉnh, chia thành **4 Cụm kiến thức**:
  - **Chương 1: Tổng quan về Hệ CSDL & Kiến trúc 3 mức** (CSDL_01): Khái niệm, ưu điểm DBMS, kiến trúc ANSI/SPARC 3 mức và tính độc lập dữ liệu.
  - **Chương 2: Mô hình Thực thể - Liên kết (ER/EER)** (CSDL_02 $\to$ CSDL_04): Thực thể, thuộc tính, liên kết, tỉ số lực lượng ($1:1, 1:N, M:N$), thực thể yếu, mở rộng EER (Disjoint / Overlap).
  - **Chương 3: Mô hình Quan hệ & Đại số Quan hệ** (CSDL_05 $\to$ CSDL_09): Lược đồ quan hệ, khóa chính, khóa ngoại, ràng buộc toàn vẹn tham chiếu, thuật toán ánh xạ 7 bước từ ER sang quan hệ, phép chọn $\sigma$, chiếu $\pi$, kết nối $\bowtie$, cây biểu thức truy vấn (Query Tree).
  - **Chương 4: Lý thuyết Thiết kế & Chuẩn hóa CSDL** (CSDL_10 $\to$ CSDL_14): Phụ thuộc hàm, hệ tiên đề Armstrong, thuật toán tìm bao đóng $X^+$, thuật toán tìm khóa tối thiểu, các dạng chuẩn 1NF, 2NF, 3NF, BCNF, thuật toán phân rã bảo toàn thông tin và phụ thuộc hàm.
- **Tính năng đặc biệt**: 100% bài học đều được tích hợp **Sơ đồ minh họa slide độ phân giải cao** (ERD symbols, Công ty ERD hoàn chỉnh, Foreign Key arrows, Query Tree, Cây phân rã chuẩn hóa, v.v.) kèm tính năng Lightbox phóng to.

---

## 3. Tech Stack & Kiến trúc Kỹ thuật

| Thành phần | Công nghệ / Thư viện | Vai trò |
| :--- | :--- | :--- |
| **Framework** | **Next.js 16.4.5 (App Router)** | Render ứng dụng phía server/static (SSG & ISR), định tuyến URL, bundling với Turbopack. |
| **Ngôn ngữ** | **TypeScript 5.x** | Kiểm soát chặt chẽ kiểu dữ liệu, bắt lỗi lúc compile (`npm run typecheck`). |
| **UI Library** | **React 19** | Quản lý state component, tương tác tabs, drawer, modal, quiz state. |
| **Styling** | **Tailwind CSS v4** | Hệ thống utility-first styling nhất quán, token hóa biến màu (Design Tokens). |
| **Component Kit** | **shadcn/ui** | Thư viện UI headless dựa trên Radix UI (`Card`, `Badge`, `Button`, `Sheet`, `Tabs`, `Dialog`, `DropdownMenu`, `Progress`, `RadioGroup`). |
| **Toán học** | **KaTeX (auto-render)** | Render công thức toán và ký hiệu đại số quan hệ tốc độ cực nhanh, bọc qua hàm `renderMathInText`. |
| **Icons** | **Lucide React** | Hệ thống icon vector đồng bộ, không dùng emoji thô trong giao diện. |
| **E2E Testing** | **Playwright** | Tự động hóa kiểm thử trình duyệt Chrome thực tế, chụp ảnh màn hình nghiệm thu giao diện (Desktop & Mobile). |
| **QA Audit** | **Python 3 Script Suite** | Bộ kiểm thử cấu trúc dữ liệu, slide references, công thức toán và route Vercel (2.733 assertions). |
| **CI/CD** | **GitHub Actions** (`ci.yml`) | Tự động chạy Typecheck, Lint, QA Audit và Next.js build trên mỗi lần Push / Pull Request lên `main`. |
| **Hosting** | **Vercel** | Nền tảng triển khai đám mây với CDN toàn cầu, tự động preview và deploy production. |

---

## 4. Các Tính Năng Đã Hoàn Thiện Gần Đây

1. **Minh họa Trực quan (Diagram Illustrations & Zoom Lightbox)**:
   - Toàn bộ các bài học, ví dụ mẫu và câu hỏi trắc nghiệm 3 cấp độ (đặc biệt là dạng Nhận biết / Thông hiểu / Vận dụng mô hình ER, ERD, Lược đồ CSDL, Boxplot, Phân phối chuẩn) đều có sơ đồ trực quan.
   - Hỗ trợ click phóng to sơ đồ (Lightbox Modal) độ phân giải cao, hỗ trợ phím `Esc` và chạm mở trên mobile.
2. **Slide Reference & Tra cứu Trực tiếp**:
   - Dấu Ref cuối mỗi bài học hiển thị chính xác tên file slide PDF, số trang, đề mục bài giảng và lời nhắc học tập.
   - Nút bấm trực tiếp mở tài liệu PDF nhảy tới đúng trang bài giảng.
3. **Đồng bộ Theme Dark / Light Mode**:
   - Hệ thống chuyển đổi theme hoạt động chuẩn xác qua class `dark` của `next-themes`, token hóa toàn bộ màu nền và viền (`bg-card`, `border-border`, `text-foreground`).
4. **Tối ưu Mobile First & Khắc phục lỗi Font**:
   - Menu bài học trên mobile chuyển đổi sang ngăn kéo trượt (**Sheet / Drawer**) chống tràn viền.
   - Sửa lỗi tách dấu tiếng Việt trong KaTeX bằng font chuẩn hệ thống (`font-sans`), căn chỉnh padding không bị thanh điều hướng điện thoại che khuất.
5. **Tích hợp Quản lý Công việc Jira (Atlassian TWG)**:
   - CLI `twg` đã được xác thực với tài khoản `duygk45@gmail.com` tại site `duygk45.atlassian.net`, kết nối trực tiếp với dự án `DLKB` và `KAN`, sẵn sàng tạo và quản lý work item tự động.

---

## 5. Tiêu Chuẩn Chất Lượng (Quality Gates)

Trước khi bất kỳ thay đổi nào được chấp thuận và đưa lên nhánh `main`:
- `npm run typecheck` $\to$ **0 lỗi TypeScript**.
- `npm run test:qa` $\to$ **100% (2.733+) tests QA passed**.
- `npm run build` $\to$ **Build Next.js thành công 100% static prerender**.
- GitHub Actions CI báo **Xanh (Pass)** toàn bộ các bước.
