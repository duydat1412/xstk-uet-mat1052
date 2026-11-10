import fitz
import os

csdl_renders = [
    # CSDL_01: ANSI/SPARC 3-level architecture
    ("C1.pdf", 40, "public/illustrations/csdl/csdl01_ansi_sparc_architecture.png", "Kiến trúc 3 mức ANSI/SPARC"),
    # CSDL_02: ER Symbols & Entities
    ("C2_1.pdf", 15, "public/illustrations/csdl/csdl02_entity_attributes.png", "Tập thực thể NHANVIEN và các thuộc tính"),
    ("C2_1.pdf", 21, "public/illustrations/csdl/csdl02_erd_overview.png", "Tổng quan ký hiệu Lược đồ ER"),
    ("C2_1.pdf", 36, "public/illustrations/csdl/csdl02_erd_symbols_table.png", "Bảng tra cứu toàn bộ ký hiệu chuẩn ERD"),
    # CSDL_03: Relationships, Cardinality & Weak Entities
    ("C2_1.pdf", 22, "public/illustrations/csdl/csdl03_relationship_types.png", "Mối liên kết giữa các thực thể"),
    ("C2_1.pdf", 25, "public/illustrations/csdl/csdl03_cardinality_ratios.png", "Ràng buộc tỉ số lực lượng 1:1, 1:N, M:N"),
    ("C2_1.pdf", 34, "public/illustrations/csdl/csdl03_weak_entity.png", "Mô hình thực thể yếu THANNHAN và liên kết xác định"),
    ("C2_1.pdf", 43, "public/illustrations/csdl/csdl03_full_company_erd.png", "Toàn cảnh Lược đồ ERD Quản lý Dự án Công ty UET"),
    # CSDL_04: EER Specialization & Generalization
    ("C2_2.pdf", 4, "public/illustrations/csdl/csdl04_eer_superclass_subclass.png", "Mô hình Lớp cha - Lớp con trong EER"),
    ("C2_2.pdf", 13, "public/illustrations/csdl/csdl04_eer_disjoint_constraint.png", "Ràng buộc rời rạc (d) và chồng chéo (o) trong EER"),
    ("C2_2.pdf", 17, "public/illustrations/csdl/csdl04_eer_completeness_constraint.png", "Ràng buộc đầy đủ: Toàn phần (nét đôi) và một phần (nét đơn)"),
    # CSDL_05: Relational Schema & Foreign Keys
    ("C3_1.pdf", 10, "public/illustrations/csdl/csdl05_relation_table_components.png", "Cấu trúc Bảng quan hệ: Bộ, Thuộc tính, Miền giá trị"),
    ("C3_1.pdf", 27, "public/illustrations/csdl/csdl05_foreign_key_schema.png", "Lược đồ CSDL Quan hệ với mũi tên Khóa ngoại"),
    # CSDL_06: ER to Relational Mapping
    ("C3_1.pdf", 37, "public/illustrations/csdl/csdl06_mapping_summary.png", "Bảng quy tắc ánh xạ từ ER sang Mô hình Quan hệ"),
    ("C3_1.pdf", 42, "public/illustrations/csdl/csdl06_mapped_relational_schema.png", "Lược đồ Quan hệ hoàn chỉnh sau khi ánh xạ từ ERD"),
    # CSDL_07-09: Relational Algebra & Query Trees
    ("C3_2.pdf", 12, "public/illustrations/csdl/csdl07_relational_algebra_select_project.png", "Minh họa phép Chọn và phép Chiếu"),
    ("C3_2.pdf", 37, "public/illustrations/csdl/csdl08_relational_algebra_join.png", "Minh họa các phép Kết nối (Join)"),
    ("C3_2.pdf", 80, "public/illustrations/csdl/csdl09_relational_query_tree.png", "Cây biểu thức Đại số Quan hệ (Query Tree)"),
    # CSDL_10-14: Functional Dependencies & Normalization
    ("C4_1.pdf", 20, "public/illustrations/csdl/csdl10_functional_dependency.png", "Biểu diễn Phụ thuộc hàm (Functional Dependency)"),
    ("C4_1.pdf", 28, "public/illustrations/csdl/csdl11_attribute_closure_algorithm.png", "Thuật toán tìm Bao đóng thuộc tính X+"),
    ("C4_1.pdf", 50, "public/illustrations/csdl/csdl12_minimal_keys_algorithm.png", "Thuật toán xác định Khóa tối thiểu"),
    ("C4_1.pdf", 62, "public/illustrations/csdl/csdl13_normal_forms_summary.png", "Bảng tổng hợp các Dạng chuẩn 1NF, 2NF, 3NF, BCNF"),
    ("C4_1.pdf", 81, "public/illustrations/csdl/csdl14_decomposition_tree.png", "Cây phân rã Lược đồ quan hệ bảo toàn thông tin"),
]

print("Rendering CSDL illustrations...")
for fname, pno, out_path, title in csdl_renders:
    pdf_path = os.path.join("public", "tailieu_csdl", fname)
    if not os.path.exists(pdf_path):
        print(f"Missing PDF: {pdf_path}")
        continue
    doc = fitz.open(pdf_path)
    if pno > len(doc):
        print(f"Page {pno} > {len(doc)} in {fname}")
        continue
    page = doc[pno - 1]
    pix = page.get_pixmap(dpi=150)
    pix.save(out_path)
    print(f"Rendered: {out_path} ({pix.width}x{pix.height}) - {title}")

print("\nDone rendering CSDL illustrations!")
