import json

with open("data/courses/csdl.json", "r", encoding="utf-8") as f:
    csdl = json.load(f)

with open("data/courses/xstk.json", "r", encoding="utf-8") as f:
    xstk = json.load(f)

# CSDL Quiz & Example Image Attachments
csdl_quiz_images = {
    "CSDL_01": {
        0: {"image": "/illustrations/csdl/csdl01_ansi_sparc_architecture.png", "caption": "Sơ đồ Kiến trúc 3 mức ANSI/SPARC"}
    },
    "CSDL_02": {
        0: {"image": "/illustrations/csdl/csdl02_erd_symbols_table.png", "caption": "Bảng tra cứu quy ước ký hiệu Lược đồ ER"}
    },
    "CSDL_03": {
        0: {"image": "/illustrations/csdl/csdl03_full_company_erd.png", "caption": "Sơ đồ ERD có các liên kết nét đơn và nét đôi"},
        1: {"image": "/illustrations/csdl/csdl03_cardinality_ratios.png", "caption": "Sơ đồ xác định tỉ số lực lượng 1:1, 1:N, M:N"}
    },
    "CSDL_04": {
        0: {"image": "/illustrations/csdl/csdl04_eer_disjoint_constraint.png", "caption": "Ký hiệu hình tròn 'd' (Disjoint) trong EER"}
    },
    "CSDL_05": {
        2: {"image": "/illustrations/csdl/csdl05_foreign_key_schema.png", "caption": "Mũi tên tham chiếu khóa ngoại giữa các bảng"}
    },
    "CSDL_06": {
        0: {"image": "/illustrations/csdl/csdl06_mapping_summary.png", "caption": "Quy tắc ánh xạ liên kết M:N sang bảng mới"}
    },
    "CSDL_07": {
        0: {"image": "/illustrations/csdl/csdl07_relational_algebra_select_project.png", "caption": "Quy ước ký hiệu phép Chọn (σ) và phép Chiếu (π)"}
    },
    "CSDL_08": {
        0: {"image": "/illustrations/csdl/csdl08_relational_algebra_join.png", "caption": "Ký hiệu phép kết nối tự nhiên và phép nối có điều kiện"}
    },
    "CSDL_09": {
        1: {"image": "/illustrations/csdl/csdl09_relational_query_tree.png", "caption": "Cây biểu thức Đại số Quan hệ (Query Tree)"}
    },
    "CSDL_10": {
        0: {"image": "/illustrations/csdl/csdl10_functional_dependency.png", "caption": "Quy ước mũi tên phụ thuộc hàm X -> Y"}
    },
    "CSDL_11": {
        1: {"image": "/illustrations/csdl/csdl11_attribute_closure_algorithm.png", "caption": "Quy trình tính bao đóng thuộc tính X+"}
    },
    "CSDL_12": {
        0: {"image": "/illustrations/csdl/csdl12_minimal_keys_algorithm.png", "caption": "Thuật toán xác định tập nguồn L và tập đích R"}
    },
    "CSDL_13": {
        0: {"image": "/illustrations/csdl/csdl13_normal_forms_summary.png", "caption": "Điều kiện phân cấp các dạng chuẩn 1NF, 2NF, 3NF, BCNF"}
    },
    "CSDL_14": {
        2: {"image": "/illustrations/csdl/csdl14_decomposition_tree.png", "caption": "Sơ đồ cây phân rã chuẩn hóa bảo toàn thông tin"}
    }
}

csdl_example_images = {
    "CSDL_01": {
        0: {"image": "/illustrations/csdl/csdl01_ansi_sparc_architecture.png", "caption": "Sơ đồ Kiến trúc 3 mức ANSI/SPARC"}
    },
    "CSDL_02": {
        0: {"image": "/illustrations/csdl/csdl02_entity_attributes.png", "caption": "Sơ đồ tập thực thể và phân loại thuộc tính"},
        2: {"image": "/illustrations/csdl/csdl02_erd_symbols_table.png", "caption": "Bảng tra cứu quy ước ký hiệu Lược đồ ER"}
    },
    "CSDL_03": {
        0: {"image": "/illustrations/csdl/csdl03_cardinality_ratios.png", "caption": "Sơ đồ xác định tỉ số lực lượng 1:1, 1:N, M:N"},
        1: {"image": "/illustrations/csdl/csdl03_weak_entity.png", "caption": "Sơ đồ thực thể yếu và liên kết xác định"},
        2: {"image": "/illustrations/csdl/csdl03_full_company_erd.png", "caption": "Toàn cảnh lược đồ ERD Quản lý Dự án Công ty UET"}
    },
    "CSDL_04": {
        0: {"image": "/illustrations/csdl/csdl04_eer_disjoint_constraint.png", "caption": "Mô hình EER phân loại lớp cha - lớp con"}
    },
    "CSDL_05": {
        0: {"image": "/illustrations/csdl/csdl05_relation_table_components.png", "caption": "Cấu trúc bảng quan hệ"},
        2: {"image": "/illustrations/csdl/csdl05_foreign_key_schema.png", "caption": "Lược đồ CSDL Quan hệ có mũi tên Khóa ngoại"}
    },
    "CSDL_06": {
        0: {"image": "/illustrations/csdl/csdl06_mapping_summary.png", "caption": "Bảng quy tắc ánh xạ 7 bước từ ER sang Quan hệ"},
        2: {"image": "/illustrations/csdl/csdl06_mapped_relational_schema.png", "caption": "Lược đồ quan hệ kết quả sau khi ánh xạ"}
    },
    "CSDL_07": {
        0: {"image": "/illustrations/csdl/csdl07_relational_algebra_select_project.png", "caption": "Minh họa phép Chọn (σ) và phép Chiếu (π)"}
    },
    "CSDL_08": {
        0: {"image": "/illustrations/csdl/csdl08_relational_algebra_join.png", "caption": "Minh họa các loại phép Kết nối (Join)"}
    },
    "CSDL_09": {
        2: {"image": "/illustrations/csdl/csdl09_relational_query_tree.png", "caption": "Cây cú pháp truy vấn đại số quan hệ"}
    },
    "CSDL_10": {
        0: {"image": "/illustrations/csdl/csdl10_functional_dependency.png", "caption": "Đồ thị biểu diễn phụ thuộc hàm"}
    },
    "CSDL_11": {
        0: {"image": "/illustrations/csdl/csdl11_attribute_closure_algorithm.png", "caption": "Lưu đồ thuật toán tìm bao đóng X+"}
    },
    "CSDL_12": {
        0: {"image": "/illustrations/csdl/csdl12_minimal_keys_algorithm.png", "caption": "Phân loại tập thuộc tính L, M, R"}
    },
    "CSDL_13": {
        0: {"image": "/illustrations/csdl/csdl13_normal_forms_summary.png", "caption": "Bảng tổng hợp các Dạng chuẩn 1NF, 2NF, 3NF, BCNF"}
    },
    "CSDL_14": {
        1: {"image": "/illustrations/csdl/csdl14_decomposition_tree.png", "caption": "Cây phân rã chuẩn hóa bảo toàn thông tin"}
    }
}

# XSTK Quiz & Example Images
xstk_quiz_images = {
    "A2": {
        1: {"image": "/illustrations/xstk/xstk_a2_distribution_shapes.png", "caption": "Các dạng hình dạng phân phối: Đối xứng, Lệch phải, Lệch trái"}
    },
    "A3": {
        2: {"image": "/illustrations/xstk/xstk_a3_boxplot_tukey.png", "caption": "Sơ đồ giải phẫu Boxplot và hàng rào 1.5 IQR của Tukey"}
    },
    "A4": {
        1: {"image": "/illustrations/xstk/xstk_a4_scatter_ols_line.png", "caption": "Đường hồi quy OLS và biểu đồ phân tán"}
    },
    "B1": {
        0: {"image": "/illustrations/xstk/xstk_b1_venn_diagram.png", "caption": "Sơ đồ Venn các biến cố xác suất"}
    },
    "B5": {
        1: {"image": "/illustrations/xstk/xstk_b5_bayes_tree_diagram.png", "caption": "Sơ đồ cây xác suất và Công thức Bayes"}
    },
    "D1": {
        0: {"image": "/illustrations/xstk/xstk_d1_normal_distribution_curve.png", "caption": "Đường cong Phân phối chuẩn và quy tắc 68-95-99.7"}
    }
}

xstk_example_images = {
    "A2": {
        0: {"image": "/illustrations/xstk/xstk_a2_distribution_shapes.png", "caption": "Các dạng hình dạng phân phối"}
    },
    "A3": {
        1: {"image": "/illustrations/xstk/xstk_a3_boxplot_tukey.png", "caption": "Cấu tạo Biểu đồ Hộp (Boxplot) và Hàng rào 1.5 IQR"}
    },
    "A4": {
        0: {"image": "/illustrations/xstk/xstk_a4_scatter_ols_line.png", "caption": "Đường hồi quy OLS"},
        2: {"image": "/illustrations/xstk/xstk_a4_residuals_plot.png", "caption": "Đồ thị Phần dư quan sát"}
    },
    "B1": {
        0: {"image": "/illustrations/xstk/xstk_b1_venn_diagram.png", "caption": "Sơ đồ Venn biến cố xác suất"}
    },
    "B5": {
        1: {"image": "/illustrations/xstk/xstk_b5_bayes_tree_diagram.png", "caption": "Cây xác suất Bayes"}
    },
    "D1": {
        0: {"image": "/illustrations/xstk/xstk_d1_normal_distribution_curve.png", "caption": "Đường cong Gauss chuẩn"}
    }
}

# Apply to CSDL
for l in csdl:
    lid = l["id"]
    if lid in csdl_quiz_images:
        for q_idx, img_info in csdl_quiz_images[lid].items():
            if q_idx < len(l["quizzes"]):
                l["quizzes"][q_idx]["image"] = img_info["image"]
                l["quizzes"][q_idx]["caption"] = img_info["caption"]
    if lid in csdl_example_images:
        for ex_idx, img_info in csdl_example_images[lid].items():
            if ex_idx < len(l["examples"]):
                l["examples"][ex_idx]["image"] = img_info["image"]
                l["examples"][ex_idx]["caption"] = img_info["caption"]

# Apply to XSTK
for l in xstk:
    lid = l["id"]
    if lid in xstk_quiz_images:
        for q_idx, img_info in xstk_quiz_images[lid].items():
            if q_idx < len(l["quizzes"]):
                l["quizzes"][q_idx]["image"] = img_info["image"]
                l["quizzes"][q_idx]["caption"] = img_info["caption"]
    if lid in xstk_example_images:
        for ex_idx, img_info in xstk_example_images[lid].items():
            if ex_idx < len(l["examples"]):
                l["examples"][ex_idx]["image"] = img_info["image"]
                l["examples"][ex_idx]["caption"] = img_info["caption"]

with open("data/courses/csdl.json", "w", encoding="utf-8") as f:
    json.dump(csdl, f, ensure_ascii=False, indent=2)

with open("data/courses/xstk.json", "w", encoding="utf-8") as f:
    json.dump(xstk, f, ensure_ascii=False, indent=2)

print("Successfully enriched Quizzes and Examples with illustrations!")
