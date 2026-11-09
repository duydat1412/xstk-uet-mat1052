---
name: frontend-design-workflow
description: Persistent frontend design and implementation workflow coordinating UI UX Pro Max, Impeccable, shadcn/ui, and Tailwind CSS with browser verification.
metadata:
  version: "1.0.0"
---

# Frontend Design & Implementation Workflow

Quy trình chuẩn hóa 5 giai đoạn thiết kế và triển khai giao diện người dùng cho toàn bộ hệ thống UET Study Hub:

## 🔹 Phase 1: Phân tích & Lập Đặc tả Thiết kế (Design Specification)
- **Công cụ chủ lực**: Skill `ui-ux-pro-max`
- **Nhiệm vụ**:
  - Phân tích ngữ cảnh sản phẩm, chân dung người dùng (sinh viên UET).
  - Xác lập hướng thiết kế (Design Direction), hệ màu (Color Palette), tỷ lệ phân cấp Typography, và các UX Pattern cốt lõi (layouts, navigation, card nesting).
  - Tuyệt đối tuân thủ Design Tokens hiện có của dự án trước khi bổ sung tokens mới.

## 🔹 Phase 2: Phê bình & Tinh chỉnh Thẩm mỹ (Design Critique & Refinement)
- **Công cụ chủ lực**: Skill `impeccable`
- **Nhiệm vụ**:
  - Soi xét phân cấp thị giác (visual hierarchy), nhịp điệu khoảng trắng (spacing/rhythm), độ tương phản (contrast WCAG AA/AAA).
  - Loại bỏ hoàn toàn các visual pattern generic, rẻ tiền kiểu "AI-generated UI" (muddy gradients, bóng mờ lộn xộn, icon vô nghĩa).
  - **Quy tắc bảo tồn**: Tinh chỉnh và mài giũa dựa trên Design Spec đã duyệt; không tùy tiện thay đổi bản sắc nhận diện thương hiệu của sản phẩm.

## 🔹 Phase 3: Hiện thực hóa Component (Component Implementation)
- **Hệ thống thành phần**: `shadcn/ui` (thông qua skill `ui-styling` & Radix primitives)
- **Nhiệm vụ**:
  - Ưu tiên tái sử dụng các component có sẵn, cấu trúc modular, phân tách rõ presentation và logic.
  - Xử lý đầy đủ mọi trạng thái tương tác: `idle`, `hover`, `focus-visible`, `active`, `disabled`, `loading`, `empty`, `error`.

## 🔹 Phase 4: Token hóa Phong cách & Responsive (Styling & Layout)
- **Hệ thống tạo kiểu**: `Tailwind CSS`
- **Nhiệm vụ**:
  - Sử dụng Tailwind classes gắn chặt với Design Tokens (variables, themes).
  - Xây dựng bố cục thích ứng (responsive layout) thông suốt trên cả Mobile (<640px), Tablet (768px), và Desktop (>=1024px).
  - Không để xảy ra lỗi tràn ngang (horizontal overflow).

## 🔹 Phase 5: Thẩm định Trực quan & Nghiệm thu (Visual Verification)
- **Nhiệm vụ bắt buộc**:
  - Phải kiểm tra trực quan giao diện thực tế (Browser-based verification) cho mọi thay đổi UI đáng kể.
  - Kiểm tra 3 tiêu chí:
    1. **Responsive**: Kiểm tra co giãn trên các breakpoint thực tế.
    2. **Accessibility**: Kiểm tra độ tương phản, trạng thái focus bàn phím, nhãn aria.
    3. **Functional**: Đảm bảo các tương tác (click, stepper, search, toggle) hoạt động trơn tru.
