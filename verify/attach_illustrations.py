import json

# Load CSDL
with open("data/courses/csdl.json", "r", encoding="utf-8") as f:
    csdl = json.load(f)

# Load XSTK
with open("data/courses/xstk.json", "r", encoding="utf-8") as f:
    xstk = json.load(f)

csdl_illustrations = {
    "CSDL_01": [
        {
            "title": "Sơ đồ Kiến trúc 3 mức ANSI/SPARC",
            "src": "/illustrations/csdl/csdl01_ansi_sparc_architecture.png",
            "slide_ref": "Slide C1.pdf trang 40",
            "caption": "Mô hình kiến trúc 3 mức chuẩn của Hệ CSDL theo ANSI/SPARC, phân chia ranh giới giữa Mức ngoài, Mức quan niệm, Mức trong và cơ chế độc lập dữ liệu.",
            "drawing_guide": [
                "1. Vẽ 3 khối chữ nhật nằm ngang từ trên xuống: Mức ngoài (External/View), Mức quan niệm (Conceptual), Mức trong (Internal).",
                "2. Dưới đáy cùng, vẽ 3 hình trụ đại diện cho Cơ sở dữ liệu vật lý (Physical DB).",
                "3. Vẽ mũi tên 2 chiều giữa Mức ngoài và Mức quan niệm: ghi chú 'Ánh xạ ngoài/quan niệm' (bảo đảm Độc lập logic).",
                "4. Vẽ mũi tên 2 chiều giữa Mức quan niệm và Mức trong: ghi chú 'Ánh xạ quan niệm/trong' (bảo đảm Độc lập vật lý).",
                "5. Trên cùng, vẽ các hình người biểu diễn Người dùng/Chương trình ứng dụng kết nối tới từng Lược đồ ngoài."
            ]
        }
    ],
    "CSDL_02": [
        {
            "title": "Bảng tra cứu Ký hiệu chuẩn Lược đồ ER (Chen Notation)",
            "src": "/illustrations/csdl/csdl02_erd_symbols_table.png",
            "slide_ref": "Slide C2_1.pdf trang 36",
            "caption": "Toàn bộ quy ước hình học chuẩn khi vẽ Lược đồ ER: Thực thể, Thực thể yếu, Thuộc tính khóa, Đa trị, Phức hợp, Suy diễn, Mối liên kết và Ràng buộc tham gia.",
            "drawing_guide": [
                "1. Kiểu thực thể: Vẽ hình chữ nhật nét đơn, tên viết HOA (ví dụ NHANVIEN).",
                "2. Thuộc tính khóa chính (PK): Vẽ hình elip nét đơn, tên thuộc tính được GẠCH CHÂN LIỀN (ví dụ MaNV).",
                "3. Thuộc tính thường: Vẽ hình elip nét đơn, nối với thực thể bằng đường thẳng.",
                "4. Thuộc tính đa trị: Vẽ hình elip VIỀN ĐÔI (ví dụ DiaDiem).",
                "5. Thuộc tính phức hợp: Vẽ 1 elip gốc nối chùm ra các elip con (ví dụ HoTen -> HoDem, Ten).",
                "6. Thuộc tính suy diễn: Vẽ hình elip NÉT ĐỨT (ví dụ Tuoi suy ra từ NgaySinh)."
            ]
        },
        {
            "title": "Tập thực thể và Các loại Thuộc tính NHANVIEN",
            "src": "/illustrations/csdl/csdl02_entity_attributes.png",
            "slide_ref": "Slide C2_1.pdf trang 15",
            "caption": "Ví dụ cụ thể cách gắn các thuộc tính đơn, thuộc tính khóa và thuộc tính phức hợp vào tập thực thể NHANVIEN."
        }
    ],
    "CSDL_03": [
        {
            "title": "Toàn cảnh Lược đồ ERD Quản lý Dự án Công ty UET",
            "src": "/illustrations/csdl/csdl03_full_company_erd.png",
            "slide_ref": "Slide C2_1.pdf trang 45",
            "caption": "Lược đồ ERD hoàn chỉnh kinh điển trong giáo trình UET với đầy đủ các mối liên kết 1:1, 1:N, M:N, liên kết đệ quy, thực thể yếu CON và thuộc tính trên liên kết.",
            "drawing_guide": [
                "1. Vẽ 4 hình chữ nhật thực thể chính: NHÂNVIÊN, ĐƠNVỊ, DỰÁN và CON (Con vẽ viền đôi vì là thực thể yếu).",
                "2. Vẽ các hình thoi liên kết: Quảnlý (1:1 giữa NHANVIEN và DONVI), Làmviệccho (1:N), Kiểm soát (1:N giữa DONVI và DUAN), Làm việc trên (M:N giữa NHANVIEN và DUAN).",
                "3. Thực thể yếu & Liên kết xác định: Vẽ hình thoi viền đôi 'Có' nối giữa NHANVIEN và CON, nối bằng nét đôi (toàn phần). Tên con gạch chân nét đứt (khóa bộ phận).",
                "4. Thuộc tính trên liên kết: Nối hình elip 'Sốgiờ' vào hình thoi 'Làm việc trên'; nối 'Ngày bắt đầu' vào 'Quảnlý'.",
                "5. Liên kết đệ quy: Vẽ hình thoi 'Giám sát' nối từ NHANVIEN vòng lại chính NHANVIEN, gán vai trò: Người giám sát (0,N) và Bị giám sát (0,1)."
            ]
        },
        {
            "title": "Ràng buộc tỉ số lực lượng (Cardinality Ratios)",
            "src": "/illustrations/csdl/csdl03_cardinality_ratios.png",
            "slide_ref": "Slide C2_1.pdf trang 25",
            "caption": "Cách biểu diễn và xác định tỉ số lực lượng 1:1, 1:N và M:N trên các nhánh liên kết ER."
        }
    ],
    "CSDL_04": [
        {
            "title": "Mô hình EER: Chuyên biệt hóa & Ràng buộc rời rạc (Disjoint)",
            "src": "/illustrations/csdl/csdl04_eer_disjoint_constraint.png",
            "slide_ref": "Slide C2_2.pdf trang 13",
            "caption": "Mô hình Lớp cha - Lớp con với hình tròn 'd' (Disjoint) và ký hiệu tập con (⊂).",
            "drawing_guide": [
                "1. Vẽ hình chữ nhật Lớp cha (Superclass) ở trên cùng: ví dụ NHANVIEN.",
                "2. Vẽ một đường thẳng nối từ đáy Lớp cha xuống một hình tròn nhỏ.",
                "3. Trong hình tròn, ghi chữ 'd' (nếu là rời rạc - disjoint) hoặc chữ 'o' (nếu là chồng chéo - overlapping).",
                "4. Từ hình tròn, vẽ các nhánh rẽ xuống từng hình chữ nhật Lớp con: NV_BIENCHE, NV_HOPDONG.",
                "5. Trên mỗi nhánh rẽ, vẽ ký hiệu chữ U nằm ngang (⊂) quay miệng về phía lớp cha để chỉ quan hệ thừa kế."
            ]
        }
    ],
    "CSDL_05": [
        {
            "title": "Lược đồ CSDL Quan hệ & Mũi tên Ràng buộc Khóa ngoại",
            "src": "/illustrations/csdl/csdl05_foreign_key_schema.png",
            "slide_ref": "Slide C3_1.pdf trang 27",
            "caption": "Lược đồ quan hệ hoàn chỉnh của CSDL Đề án công ty với các mũi tên tham chiếu khóa ngoại trỏ từ bảng con tới khóa chính của bảng cha.",
            "drawing_guide": [
                "1. Với mỗi bảng, vẽ một khung chữ nhật phân chia thành từng ô thuộc tính.",
                "2. Khóa chính (Primary Key): Gạch chân liền bên dưới tên thuộc tính (ví dụ MANV, MAPHG, MADA).",
                "3. Khóa ngoại (Foreign Key): Vẽ mũi tên cong xuất phát từ ô thuộc tính khóa ngoại (ở bảng con) trỏ thẳng vào thuộc tính khóa chính (ở bảng cha tham chiếu).",
                "4. Khóa ngoại đệ quy: Thuộc tính MA_NQL trong bảng NHANVIEN có mũi tên cong vòng lại trỏ vào MANV của chính bảng đó."
            ]
        }
    ],
    "CSDL_06": [
        {
            "title": "Bảng quy tắc ánh xạ từ ER sang Mô hình Quan hệ",
            "src": "/illustrations/csdl/csdl06_mapping_summary.png",
            "slide_ref": "Slide C3_1.pdf trang 37",
            "caption": "Bảng tóm tắt quy tắc 7 bước chuyển đổi từ thực thể, liên kết 1:1, 1:N, M:N sang bảng và khóa ngoại.",
            "drawing_guide": [
                "1. Bước 1: Thực thể thường -> Chuyển thành 1 bảng quan hệ, giữ nguyên PK.",
                "2. Bước 2: Thực thể yếu -> Tạo bảng gồm các thuộc tính của nó + PK của bảng cha làm FK, khóa chính là (PK cha + Khóa bộ phận).",
                "3. Bước 3: Liên kết 1:1 -> Đưa PK của một bên sang làm FK bên kia (ưu tiên bên tham gia toàn phần).",
                "4. Bước 4: Liên kết 1:N -> Đưa PK của bên 1 sang làm FK của bên N.",
                "5. Bước 5: Liên kết M:N -> Tạo một BẢNG QUAN HỆ MỚI, có PK là cặp (PK1, PK2), kèm các thuộc tính của liên kết.",
                "6. Bước 6: Thuộc tính đa trị -> Tạo bảng mới gồm (PK thực thể + giá trị đa trị)."
            ]
        }
    ],
    "CSDL_07": [
        {
            "title": "Các phép toán Đại số Quan hệ: Phép Chọn (σ) & Phép Chiếu (π)",
            "src": "/illustrations/csdl/csdl07_relational_algebra_select_project.png",
            "slide_ref": "Slide C3_2.pdf trang 12",
            "caption": "Minh họa trực quan hoạt động lọc hàng ngang (Select) và cắt dọc cột thuộc tính (Project) trên bảng dữ liệu."
        }
    ],
    "CSDL_08": [
        {
            "title": "Phép Kết nối Quan hệ (Join - ⨝)",
            "src": "/illustrations/csdl/csdl08_relational_algebra_join.png",
            "slide_ref": "Slide C3_2.pdf trang 37",
            "caption": "Minh họa cách ghép nối 2 bảng theo điều kiện bằng (Equi-Join) và Kết nối tự nhiên (Natural Join)."
        }
    ],
    "CSDL_09": [
        {
            "title": "Cây biểu thức Đại số Quan hệ (Query Tree)",
            "src": "/illustrations/csdl/csdl09_relational_query_tree.png",
            "slide_ref": "Slide C3_2.pdf trang 80",
            "caption": "Sơ đồ cây cú pháp tối ưu hóa truy vấn đại số quan hệ: các quan hệ gốc ở lá, các phép toán ở nút và kết quả ở đỉnh gốc."
        }
    ],
    "CSDL_10": [
        {
            "title": "Biểu diễn Phụ thuộc hàm (Functional Dependency)",
            "src": "/illustrations/csdl/csdl10_functional_dependency.png",
            "slide_ref": "Slide C4_1.pdf trang 20",
            "caption": "Quy tắc biểu diễn đồ thị phụ thuộc hàm X -> Y và các dị thường dữ liệu khi chưa chuẩn hóa."
        }
    ],
    "CSDL_11": [
        {
            "title": "Sơ đồ Thuật toán tìm Bao đóng thuộc tính X+",
            "src": "/illustrations/csdl/csdl11_attribute_closure_algorithm.png",
            "slide_ref": "Slide C4_1.pdf trang 28",
            "caption": "Lưu đồ thuật toán từng bước để tính bao đóng X+ dưới tập phụ thuộc hàm F."
        }
    ],
    "CSDL_12": [
        {
            "title": "Thuật toán Xác định tất cả Khóa tối thiểu của Lược đồ",
            "src": "/illustrations/csdl/csdl12_minimal_keys_algorithm.png",
            "slide_ref": "Slide C4_1.pdf trang 50",
            "caption": "Sơ đồ phân loại tập thuộc tính: Tập nguồn L, Tập trung gian M, Tập đích R và cách tìm tổ hợp khóa."
        }
    ],
    "CSDL_13": [
        {
            "title": "Bảng Tổng hợp và Đối chiếu các Dạng chuẩn: 1NF, 2NF, 3NF, BCNF",
            "src": "/illustrations/csdl/csdl13_normal_forms_summary.png",
            "slide_ref": "Slide C4_1.pdf trang 62",
            "caption": "Tiêu chuẩn phân cấp dạng chuẩn và điều kiện vi phạm tương ứng trong đề thi."
        }
    ],
    "CSDL_14": [
        {
            "title": "Cây Phân rã Chuẩn hóa Bảo toàn Thông tin & Phụ thuộc hàm",
            "src": "/illustrations/csdl/csdl14_decomposition_tree.png",
            "slide_ref": "Slide C4_1.pdf trang 81",
            "caption": "Cây phân rã lược đồ quan hệ từng bước đạt 3NF hoặc BCNF mà không làm mất thông tin."
        }
    ]
}

xstk_illustrations = {
    "A2": [
        {
            "title": "Các dạng hình dạng phân phối (Distribution Shapes)",
            "src": "/illustrations/xstk/xstk_a2_distribution_shapes.png",
            "slide_ref": "Slide week02.pdf trang 7",
            "caption": "Đối chiếu 3 dạng phân phối kinh điển: Lệch trái (Left-skewed), Đối xứng hình chuông (Symmetric), Lệch phải (Right-skewed)."
        }
    ],
    "A3": [
        {
            "title": "Cấu tạo Biểu đồ Hộp (Boxplot) & Hàng rào 1.5 IQR của Tukey",
            "src": "/illustrations/xstk/xstk_a3_boxplot_tukey.png",
            "slide_ref": "Slide week02.pdf trang 64",
            "caption": "Sơ đồ giải phẫu đầy đủ của biểu đồ hộp: Q1, Median, Q3, Khoảng tứ phân vị IQR, Râu (Whiskers) và Điểm ngoại lai (Outliers).",
            "drawing_guide": [
                "1. Trục số: Vẽ một trục số thẳng đứng hoặc nằm ngang có chia vạch tỉ lệ đều.",
                "2. Thân hộp (Box): Vẽ hình chữ nhật có đáy ở Q1 và đỉnh ở Q3. Chiều rộng hộp chính là IQR = Q3 - Q1.",
                "3. Đường trung vị (Median): Vẽ một đường kẻ ngang đậm bên trong thân hộp tại vị trí Median (Q2).",
                "4. Tính hàng rào Tukey: Hàng rào dưới = Q1 - 1.5*IQR; Hàng rào trên = Q3 + 1.5*IQR.",
                "5. Râu (Whiskers): Kéo đoạn thẳng từ mép hộp tới giá trị nhỏ nhất / lớn nhất KHÔNG phải là ngoại lai.",
                "6. Điểm ngoại lai (Outliers): Vẽ các dấu chấm tròn riêng biệt cho mọi điểm số liệu nằm ngoài hàng rào Tukey."
            ]
        }
    ],
    "A4": [
        {
            "title": "Biểu đồ phân tán (Scatter Plot) & Đường hồi quy tuyến tính OLS",
            "src": "/illustrations/xstk/xstk_a4_scatter_ols_line.png",
            "slide_ref": "Slide week04.pdf trang 12",
            "caption": "Đường xu hướng hồi quy OLS y = b0 + b1*x và phần dư sai số e_i giữa điểm quan sát và đường dự báo."
        }
    ],
    "B1": [
        {
            "title": "Sơ đồ Venn Biến cố Xác suất",
            "src": "/illustrations/xstk/xstk_b1_venn_diagram.png",
            "slide_ref": "Slide week05.pdf trang 12",
            "caption": "Minh họa hình học các biến cố Giao (A ∩ B), Hợp (A ∪ B), Phần bù (A') và Biến cố xung khắc."
        }
    ],
    "B5": [
        {
            "title": "Sơ đồ Cây xác suất (Tree Diagram) & Công thức Bayes",
            "src": "/illustrations/xstk/xstk_b5_bayes_tree_diagram.png",
            "slide_ref": "Slide week05.pdf trang 72",
            "caption": "Cấu trúc phân nhánh tính xác suất toàn phần và cập nhật xác suất hậu nghiệm theo Định lý Bayes."
        }
    ],
    "D1": [
        {
            "title": "Đường cong Phân phối Chuẩn hình chuông & Quy tắc Thực nghiệm 68-95-99.7",
            "src": "/illustrations/xstk/xstk_d1_normal_distribution_curve.png",
            "slide_ref": "Slide week07.pdf trang 22",
            "caption": "Đường cong Gauss đối xứng qua kỳ vọng μ với diện tích xác suất tại 1σ, 2σ và 3σ."
        }
    ]
}

# Attach to CSDL
for l in csdl:
    lid = l["id"]
    if lid in csdl_illustrations:
        l["illustrations"] = csdl_illustrations[lid]

# Attach to XSTK
for l in xstk:
    lid = l["id"]
    if lid in xstk_illustrations:
        l["illustrations"] = xstk_illustrations[lid]

with open("data/courses/csdl.json", "w", encoding="utf-8") as f:
    json.dump(csdl, f, ensure_ascii=False, indent=2)

with open("data/courses/xstk.json", "w", encoding="utf-8") as f:
    json.dump(xstk, f, ensure_ascii=False, indent=2)

print("Enriched csdl.json and xstk.json with illustrations!")
