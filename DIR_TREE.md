# CẤU TRÚC THƯ MỤC DỰ ÁN (DIRECTORY TREE & QUICK LOOKUP)

> **MỤC ĐÍCH**: Tài liệu này giúp AI Agent và lập trình viên tra cứu nhanh cấu trúc dự án, **đi thẳng tới đúng file cần thao tác trong 1 bước**, tuyệt đối tránh việc chạy các lệnh tìm kiếm quét đệ quy (`findstr /S *.*`, `grep -r`, `Get-ChildItem -Recurse`) làm nghẽn tiến trình và lãng phí tài nguyên.

---

## 1. Bảng Tra Cứu Nhanh (Quick File Lookup)

| Bạn cần làm gì? | File hoặc Thư mục cần đến | Mô tả chi tiết |
| :--- | :--- | :--- |
| **Sửa giao diện chính trang học** | [`components/course-study-view.tsx`](file:///d:/Projects/XSTK/components/course-study-view.tsx) | Component React cốt lõi: stepper lý thuyết, ví dụ mẫu, cạm bẫy, trắc nghiệm 3 cấp độ, modal lightbox, ref slide, sidebar & mobile sheet. |
| **Sửa dữ liệu bài học XSTK** | [`data/courses/xstk.json`](file:///d:/Projects/XSTK/data/courses/xstk.json) | Toàn bộ 26 bài học XSTK (lý thuyết, ví dụ, cạm bẫy, trắc nghiệm, hình ảnh, slide ref). |
| **Sửa dữ liệu bài học CSDL** | [`data/courses/csdl.json`](file:///d:/Projects/XSTK/data/courses/csdl.json) | Toàn bộ 14 bài học CSDL (lý thuyết, ví dụ, cạm bẫy, trắc nghiệm, hình ảnh, slide ref). |
| **Sửa / Khai báo Schema Types** | [`types/course.ts`](file:///d:/Projects/XSTK/types/course.ts) | Định nghĩa TypeScript: `Course`, `Lesson`, `Example`, `GatekeeperQuiz`, `Pitfall`, `SlideRef`. |
| **Chuẩn hóa dữ liệu nạp khóa học** | [`data/courses/index.ts`](file:///d:/Projects/XSTK/data/courses/index.ts) | File nạp `csdl.json` và `xstk.json`, chuẩn hóa fallback data trước khi đưa lên UI. |
| **Chỉnh sửa Trang chủ (Portal Hub)** | [`app/page.tsx`](file:///d:/Projects/XSTK/app/page.tsx) | Trang chủ chuyển hướng chọn môn học (UET Study Hub). |
| **Chỉnh sửa Trang học CSDL** | [`app/csdl/hoc/page.tsx`](file:///d:/Projects/XSTK/app/csdl/hoc/page.tsx) | Route Next.js `/csdl/hoc`. |
| **Chỉnh sửa Trang học XSTK** | [`app/xstk/hoc/page.tsx`](file:///d:/Projects/XSTK/app/xstk/hoc/page.tsx) | Route Next.js `/xstk/hoc`. |
| **Cấu hình Layout chung & Metadata** | [`app/layout.tsx`](file:///d:/Projects/XSTK/app/layout.tsx) | Root layout, font Inter, provider Theme, thẻ `<head>`. |
| **Cấu hình CSS biến màu & Dark Mode** | [`app/globals.css`](file:///d:/Projects/XSTK/app/globals.css) | Tokens CSS variables cho Light/Dark mode, class KaTeX overflow, scrollbar. |
| **Component hiển thị Công thức Toán** | [`components/math-block.tsx`](file:///d:/Projects/XSTK/components/math-block.tsx) | Wrapper render KaTeX inline và KaTeX block. |
| **Component Chuyển đổi Dark/Light** | [`components/theme-toggle.tsx`](file:///d:/Projects/XSTK/components/theme-toggle.tsx) | Nút bấm chuyển giao diện sáng / tối / theo hệ thống. |
| **Các UI Components chuẩn shadcn** | [`components/ui/`](file:///d:/Projects/XSTK/components/ui/) | `button.tsx`, `card.tsx`, `sheet.tsx`, `tabs.tsx`, `dialog.tsx`, `badge.tsx`, `progress.tsx`, v.v. |
| **Thêm / xem Ảnh sơ đồ minh họa CSDL** | [`public/illustrations/csdl/`](file:///d:/Projects/XSTK/public/illustrations/csdl/) | Toàn bộ ảnh sơ đồ ER, ERD, lược đồ quan hệ, cây truy vấn, dạng chuẩn, phân rã. |
| **Thêm / xem Ảnh sơ đồ minh họa XSTK** | [`public/illustrations/xstk/`](file:///d:/Projects/XSTK/public/illustrations/xstk/) | Ảnh Boxplot, đồ thị OLS, sơ đồ Venn, cây xác suất Bayes, phân phối chuẩn Gauss. |
| **Tra cứu File Slide PDF bài giảng** | [`public/`](file:///d:/Projects/XSTK/public/) | Các file slide PDF của giảng viên UET (`C1.pdf` $\to$ `C4_1.pdf`, `week01.pdf` $\to$ `week07.pdf`). |
| **File cấu hình CI/CD GitHub Actions** | [`.github/workflows/ci.yml`](file:///d:/Projects/XSTK/.github/workflows/ci.yml) | Workflow tự động chạy Typecheck, Lint, QA Audit và Next.js build. |
| **Bộ mã kiểm thử & QA tự động** | [`verify/`](file:///d:/Projects/XSTK/verify/) | Các script Python chạy 2.733+ test cases và kiểm thử Playwright browser. |
| **Cấu hình build Next.js** | [`next.config.mjs`](file:///d:/Projects/XSTK/next.config.mjs) | Cấu hình Turbopack, headers, redirects và static export. |
| **Cấu hình routing Vercel** | [`vercel.json`](file:///d:/Projects/XSTK/vercel.json) | Khai báo rewrite và cache control trên Vercel. |

---

## 2. Toàn Cảnh Cây Thư Mục (Full Directory Tree)

```text
D:\Projects\XSTK\
│
├── .agents/                               # Định nghĩa kỹ năng cho AI Coding Agents
│   └── skills/
│       └── frontend-design-workflow/
│           └── SKILL.md                   # Quy trình 5 bước phát triển UI tiêu chuẩn cao
│
├── .github/
│   └── workflows/
│       └── ci.yml                         # GitHub Actions CI/CD Pipeline
│
├── app/                                   # Next.js 16 App Router
│   ├── globals.css                        # Design tokens, CSS variables, Dark/Light rules
│   ├── layout.tsx                         # Root Layout bọc ThemeProvider
│   ├── page.tsx                           # Trang chủ Portal Hub chọn môn học
│   ├── csdl/
│   │   └── hoc/
│   │       └── page.tsx                   # Trang học môn Cơ sở dữ liệu (INT2207)
│   └── xstk/
│       └── hoc/
│           └── page.tsx                   # Trang học môn Xác suất Thống kê (MAT1052)
│
├── components/                            # React Components
│   ├── course-study-view.tsx              # Component học tập chính (Section stepper, Quiz, Lightbox)
│   ├── icons.tsx                          # Icon tùy biến (Subject icons, Github, v.v.)
│   ├── math-block.tsx                     # KaTeX Math block & inline wrapper
│   ├── theme-toggle.tsx                   # Nút chuyển Dark/Light theme
│   └── ui/                                # Bộ thành phần shadcn/ui (Radix UI primitives)
│       ├── accordion.tsx
│       ├── badge.tsx
│       ├── button.tsx
│       ├── card.tsx
│       ├── dialog.tsx
│       ├── dropdown-menu.tsx
│       ├── input.tsx
│       ├── progress.tsx
│       ├── radio-group.tsx
│       ├── scroll-area.tsx
│       ├── separator.tsx
│       ├── sheet.tsx                      # Drawer menu danh sách bài học trên mobile
│       ├── tabs.tsx
│       └── tooltip.tsx
│
├── data/                                  # Dữ liệu Khóa học (Single Source of Truth)
│   └── courses/
│       ├── csdl.json                      # Dữ liệu 14 bài học CSDL
│       ├── xstk.json                      # Dữ liệu 26 bài học XSTK
│       └── index.ts                       # Adapter nạp & chuẩn hóa dữ liệu
│
├── docs/                                  # Tài liệu phân tích, đề cương, đặc tả kỹ thuật
│   ├── all_slide_exercises.json           # Trích xuất toàn bộ bài tập từ slide
│   ├── csdl_lessons_map.json              # Bản đồ bài học CSDL
│   ├── lotrinh.md                         # Lộ trình phát triển dự án
│   └── qa-report.md                       # Báo cáo kết quả kiểm thử
│
├── lib/
│   └── utils.ts                           # Hàm tiện ích (cn = clsx + tailwind-merge)
│
├── public/                                # Static Assets phục vụ web & client
│   ├── illustrations/                     # Thư viện ảnh sơ đồ minh họa bài giảng
│   │   ├── csdl/                          # Sơ đồ CSDL: ERD, Schema, Query Tree, 1NF-BCNF,...
│   │   └── xstk/                          # Sơ đồ XSTK: Boxplot, OLS, Venn, Bayes, Normal,...
│   ├── site/                              # Static HTML fallback cho các công cụ mở rộng
│   │   ├── congthuc.html                  # Sổ tay công thức
│   │   ├── dethi.html                     # Đề thi thử bấm giờ
│   │   ├── tracnghiem.html                # Luyện trắc nghiệm theo chuyên đề
│   │   └── tuluan.html                    # Luyện tự luận có barem điểm
│   ├── C1.pdf ... C4_1.pdf                # Các file slide PDF bài giảng CSDL
│   └── week01.pdf ... week07.pdf          # Các file slide PDF bài giảng XSTK
│
├── types/
│   └── course.ts                          # Định nghĩa TypeScript Types toàn dự án
│
├── verify/                                # Bộ kiểm thử & QA tự động
│   ├── run_full_qa_suite.py               # Chạy toàn bộ 7 phases QA cho XSTK
│   ├── run_csdl_qa_suite.py               # Chạy toàn bộ QA cho CSDL
│   ├── test_public_pdfs.py                # Kiểm tra tính toàn vẹn và trang của các file PDF
│   ├── verify_quiz_illustrations.py       # Playwright E2E test cho Quiz & Lightbox
│   └── ... (các script hỗ trợ trích xuất & kiểm tra khác)
│
├── AGENTS.md                              # Quy chuẩn Sư phạm UET & Workflow phát triển UI
├── AGENT_GUIDELINES.md                    # Cẩm nang luật & lưu ý cho AI Coding Agent
├── PROJECT_CONTEXT.md                     # Tổng quan hiện trạng kỹ thuật & tính năng dự án
├── DIR_TREE.md                            # Bản đồ thư mục & bảng tra cứu nhanh này
├── components.json                        # Cấu hình cài đặt shadcn/ui
├── next.config.mjs                        # Cấu hình Next.js 16
├── package.json                           # Dependencies và scripts chạy dự án
├── tsconfig.json                          # Cấu hình TypeScript compiler
└── vercel.json                            # Cấu hình router & cache cho Vercel
```

---

## 3. Lưu Ý Về Các Thư Mục Cấm Quét Đệ Quy

Khi sử dụng các công cụ tìm kiếm dòng lệnh (`run_command`, PowerShell, bash):
- ⚠️ **TUYỆT ĐỐI KHÔNG quét đệ quy vào**:
  - `node_modules/` (Hàng trăm nghìn file thư viện)
  - `.next/` (Build artifacts của Next.js)
  - `.git/` (Dữ liệu lịch sử git)
- Hãy dùng bảng tra cứu nhanh ở Mục 1 để mở trực tiếp file bằng `read_file` hoặc `edit_file`.
