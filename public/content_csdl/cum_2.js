// ==========================================================================
// CỤM 2 (CSDL): MÔ HÌNH QUAN HỆ & THUẬT TOÁN ÁNH XẠ ER/EER SANG BẢNG
// Bao gồm: Bài CSDL_05, CSDL_06
// Nguồn: Slide UET.IS2099 C3_1.pptx
// ==========================================================================

const CUM_2_CSDL = [
  {
    id: "CSDL_05",
    cluster: "2",
    title: "Mô hình Dữ liệu Quan hệ: Khóa chính, Khóa ngoại & Toàn vẹn",
    sources: "Slide UET.IS2099 Chương 3 Phần 1 (Slide 1–27)",
    ref: {
      slide_file: "C3_1.pptx",
      slide_name: "Chương 3 (Phần 1) — Mô hình Dữ liệu Quan hệ",
      pages: "Slide 1 – 27",
      page_start: 1,
      page_end: 27,
      section: "Mục 1.1: Khái niệm Quan hệ, Thuộc tính, Bộ, Miền; Mục 1.3: Khóa & Siêu khóa; Mục 1.4: Ràng buộc toàn vẹn",
      key_points: [
        "Khái niệm Quan hệ (Relation / Bảng), Thuộc tính (Attribute / Cột), Bộ (Tuple / Hàng), Miền giá trị (Domain)",
        "Các khái niệm về Khóa: Siêu khóa (Superkey), Khóa ứng viên / Khóa dự tuyển (Candidate Key), Khóa chính (Primary Key)",
        "Thuộc tính khóa (Prime Attribute) vs Thuộc tính không khóa (Non-prime Attribute)",
        "Ràng buộc toàn vẹn thực thể (Entity Integrity): Khóa chính không bao giờ được chứa giá trị NULL",
        "Khóa ngoại (Foreign Key) và Ràng buộc toàn vẹn tham chiếu (Referential Integrity): Giá trị khóa ngoại phải bằng một khóa chính hiện có hoặc bằng NULL"
      ],
      remind: "Ràng buộc toàn vẹn tham chiếu là trọng tâm câu hỏi trắc nghiệm và tự luận. Hãy mở Slide C3_1 trang 23–27 để xem các ví dụ vi phạm khóa ngoại."
    },
    desc: "Nắm vững bản chất toán học của mô hình quan hệ, phân biệt siêu khóa, khóa ứng viên, khóa chính và 2 ràng buộc toàn vẹn cốt tử.",
    steps: [
      {
        t: "Cấu trúc toán học của Mô hình Quan hệ",
        c: `<p>Mô hình dữ liệu quan hệ do <b>Edgar F. Codd (IBM, 1970)</b> đề xuất, dựa trên lý thuyết tập hợp toán học:</p>
            <ul>
              <li><b>Lược đồ quan hệ (Relation Schema)</b>: Ký hiệu là $R(A_1: D_1, A_2: D_2, \dots, A_n: D_n)$, trong đó $R$ là tên quan hệ, $A_i$ là các thuộc tính, $D_i = \text{dom}(A_i)$ là miền giá trị tương ứng. Bậc của quan hệ (Degree) là số lượng thuộc tính $n$.</li>
              <li><b>Quan hệ (Relation / Thể hiện của quan hệ)</b>: Ký hiệu là $r(R)$, là một tập con của tích Đề-các của các miền giá trị:
                $$r(R) \subseteq D_1 \times D_2 \times \dots \times D_n$$
              </li>
              <li><b>Bộ (Tuple / Hàng)</b>: Mỗi phần tử $t \in r(R)$ là một bộ dữ liệu có thứ tự gồm $n$ giá trị $\langle v_1, v_2, \dots, v_n \rangle$, với $v_i \in D_i$. Lực lượng của quan hệ (Cardinality) là số lượng bộ $|r|$.</li>
            </ul>
            <div class="tip-box">
              <b>3 Đặc trưng cơ bản của Quan hệ:</b><br>
              1. <b>Không có thứ tự giữa các bộ</b>: Hoán đổi thứ tự các hàng trong bảng không làm thay đổi bản chất của quan hệ.<br>
              2. <b>Không có hai bộ trùng lặp hoàn toàn</b>: Quan hệ là một tập hợp toán học, do đó mọi bộ trong bảng đều phải phân biệt được.<br>
              3. <b>Giá trị thuộc tính là nguyên tử (Atomic)</b>: Mỗi ô trong bảng chỉ chứa đúng một giá trị duy nhất (không được là tập hợp, danh sách hay mảng).
            </div>`
      },
      {
        t: "Phân biệt Siêu khóa, Khóa ứng viên & Khóa chính",
        c: `<p>Trong lược đồ quan hệ $R(A_1, A_2, \dots, A_n)$, một tập thuộc tính $K \subseteq R$ có các cấp độ định danh sau:</p>
            <ol>
              <li><b>Siêu khóa (Superkey - SK)</b>: Là một tập thuộc tính mà giá trị của nó nhận diện <i>duy nhất</i> mỗi bộ trong quan hệ. Nghĩa là không thể có hai bộ khác nhau $t_1, t_2 \in r(R)$ mà $t_1[SK] = t_2[SK]$. (Một siêu khóa có thể chứa các thuộc tính thừa thãi).</li>
              <li><b>Khóa ứng viên / Khóa dự tuyển (Candidate Key - CK)</b>: Là một <b>Siêu khóa tối thiểu (Minimal Superkey)</b> — nghĩa là nếu bỏ bất kỳ thuộc tính nào khỏi $K$ thì $K$ không còn là siêu khóa nữa.</li>
              <li><b>Khóa chính (Primary Key - PK)</b>: Là một trong các khóa ứng viên được người thiết kế CSDL <i>chọn làm định danh chính thức</i> cho các bộ trong bảng. Trên lược đồ quan hệ, các thuộc tính của khóa chính được <b>gạch chân nét liền</b>: $R(\\underline{A}, B, C)$.</li>
            </ol>
            <div class="warn-box">
              <b>Phân loại thuộc tính:</b><br>
              • <b>Thuộc tính khóa (Prime Attribute)</b>: Thuộc tính tham gia vào <i>ít nhất một khóa ứng viên</i> nào đó của quan hệ.<br>
              • <b>Thuộc tính không khóa (Non-prime Attribute)</b>: Thuộc tính không tham gia vào bất kỳ khóa ứng viên nào.
            </div>`
      },
      {
        t: "Hai Ràng buộc Toàn vẹn Cốt tử",
        c: `<p>Mọi thể hiện hợp lệ của CSDL quan hệ bắt buộc phải thỏa mãn 2 ràng buộc toàn vẹn:</p>
            <table class="data-table">
              <thead><tr><th>Tên ràng buộc</th><th>Nội dung ràng buộc</th><th>Mục đích bảo vệ</th><th>Hậu quả nếu vi phạm</th></tr></thead>
              <tbody>
                <tr>
                  <td><b>Toàn vẹn Thực thể (Entity Integrity)</b></td>
                  <td>Không có bất kỳ thuộc tính nào thuộc <b>Khóa chính</b> được phép nhận giá trị <b>NULL</b> (rỗng).</td>
                  <td>Đảm bảo mọi cá thể trong bảng luôn được nhận diện duy nhất và phân biệt rõ ràng.</td>
                  <td>Hệ thống từ chối lệnh INSERT / UPDATE nếu khóa chính là NULL.</td>
                </tr>
                <tr>
                  <td><b>Toàn vẹn Tham chiếu (Referential Integrity)</b></td>
                  <td>Nếu tập thuộc tính $FK$ của bảng $R_1$ là <b>Khóa ngoại</b> tham chiếu đến khóa chính $PK$ của bảng $R_2$, thì với mọi bộ $t_1 \in R_1$: Giá trị $t_1[FK]$ hoặc phải <b>bằng giá trị $PK$ của một bộ nào đó trong $R_2$</b>, hoặc phải <b>bằng NULL</b>.</td>
                  <td>Ngăn chặn tình trạng 'tham chiếu mồ côi' (dữ liệu chỉ tới một đối tượng không tồn tại).</td>
                  <td>Từ chối xóa bản ghi cha nếu còn bản ghi con tham chiếu đến (RESTRICT), hoặc xóa dây chuyền (CASCADE).</td>
                </tr>
              </tbody>
            </table>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide C3_1 — Slide 23] Xác định Khóa chính và Khóa dự tuyển",
        q: "Xét lược đồ quan hệ `NHANVIEN(MaNV, SoCMND, HoDem, Ten, NgaySinh, DiaChi)`. Giả sử trong thực tế, `MaNV` không bao giờ trùng và `SoCMND` của mỗi công dân cũng là duy nhất. Hãy chỉ ra: (1) Các khóa ứng viên (Candidate Keys); (2) Các siêu khóa; (3) Thuộc tính khóa và thuộc tính không khóa.",
        sol: "<b>Phân tích bản chất:</b><br>" +
             "1. Các <b>Khóa ứng viên (Candidate Keys)</b> là các siêu khóa tối thiểu:<br>" +
             "   $$CK_1 = \\{MaNV\\}, \\quad CK_2 = \\{SoCMND\\}$$<br>" +
             "2. Các <b>Siêu khóa (Superkeys)</b>: Bất kỳ tập thuộc tính nào chứa $CK_1$ hoặc $CK_2$ đều là siêu khóa (ví dụ: $\\{MaNV\\}$, $\\{MaNV, HoDem\\}$, $\\{SoCMND, DiaChi\\}$, $\\{MaNV, SoCMND\\}$...).<br>" +
             "3. <b>Thuộc tính khóa (Prime attributes)</b>: Là thuộc tính xuất hiện trong ít nhất 1 khóa ứng viên $\\rightarrow \\{MaNV, SoCMND\\}$.<br>" +
             "4. <b>Thuộc tính không khóa (Non-prime attributes)</b>: $\\{HoDem, Ten, NgaySinh, DiaChi\\}$."
      },
      {
        level: "Trung bình",
        t: "[Slide C3_1 — Slide 25–26] Kiểm tra Vi phạm Ràng buộc Toàn vẹn Tham chiếu",
        q: "Cho hai bảng trong CSDL Công ty:<br>" +
           "- `PHONGBAN(`<u>`MaPB`</u>`, TenPB)` có các bộ: `(1, 'Kế toán'), (2, 'Kỹ thuật'), (3, 'Nhân sự')`.<br>" +
           "- `NHANVIEN(`<u>`MaNV`</u>`, HoTen, MaPB)` có `MaPB` là khóa ngoại tham chiếu `PHONGBAN(MaPB)`.<br>" +
           "Xét 3 thao tác sau: (1) Thêm nhân viên có `MaPB = 5`; (2) Thêm nhân viên có `MaPB = NULL`; (3) Xóa phòng ban có `MaPB = 2` khi đang có 5 nhân viên làm việc tại phòng này. Thao tác nào vi phạm toàn vẹn?",
        sol: "<b>Phân tích từng thao tác theo Slide C3_1 trang 25–27:</b><br>" +
             "1. <b>Thao tác 1 (Thêm nhân viên MaPB = 5)</b>: <b>VI PHẠM toàn vẹn tham chiếu!</b> Vì giá trị `5` không tồn tại trong tập khóa chính của bảng `PHONGBAN`. Hệ thống sẽ báo lỗi Foreign Key Constraint Violation.<br>" +
             "2. <b>Thao tác 2 (Thêm nhân viên MaPB = NULL)</b>: <b>HỢP LỆ!</b> (nếu cột `MaPB` không có ràng buộc NOT NULL). Một nhân viên mới vào có thể chưa được phân công phòng ban chính thức.<br>" +
             "3. <b>Thao tác 3 (Xóa phòng ban MaPB = 2)</b>: <b>VI PHẠM toàn vẹn tham chiếu!</b> Nếu xóa, 5 nhân viên của phòng ban này sẽ trỏ tới một `MaPB` không tồn tại (tham chiếu mồ côi). Muốn xóa, DBMS phải có chính sách xử lý: ON DELETE CASCADE (xóa luôn cả 5 nhân viên) hoặc ON DELETE SET NULL."
      },
      {
        level: "Vận dụng",
        t: "[Slide C3_1 — Slide 24] Bài toán Khóa chính Phức hợp và Vi phạm Toàn vẹn Thực thể",
        q: "Xét bảng kết quả học tập `KETQUA(`<u>`MaSV`</u>`, `<u>`MaMH`</u>`, DiemSo)` có khóa chính gồm 2 thuộc tính gộp lại là `(MaSV, MaMH)`. Một nhân viên phòng đào tạo thực hiện lệnh INSERT: `INSERT INTO KETQUA VALUES ('23020001', NULL, 8.5)`. Lệnh này có thực hiện thành công không? Tại sao?",
        sol: "<b>Phân tích:</b><br>" +
             "<b>Lệnh này THẤT BẠI HOÀN TOÀN!</b><br>" +
             "- Theo nguyên lý <b>Ràng buộc toàn vẹn thực thể (Entity Integrity Constraint)</b>: Mọi thành phần cấu thành nên Khóa chính (kể cả khóa chính phức hợp gồm nhiều thuộc tính) đều <b>tuyệt đối KHÔNG ĐƯỢC chứa giá trị NULL</b>.<br>" +
             "- Ở đây thuộc tính `MaMH` là một phần của khóa chính bị gán giá trị NULL $\\rightarrow$ Vi phạm toàn vẹn thực thể, DBMS sẽ chặn đứng giao dịch và ném ngoại lệ lỗi."
      }
    ],
    pitfalls: [
      {
        bad: "Nghĩ rằng Khóa ngoại (Foreign Key) bắt buộc phải có tên giống hệt tên của Khóa chính (Primary Key) mà nó tham chiếu tới.",
        good: "Khóa ngoại có thể đặt tên hoàn toàn khác với khóa chính (ví dụ: MaTruongPhong trong PHONGBAN tham chiếu đến MaNV trong NHANVIEN), chỉ cần chúng có cùng kiểu dữ liệu và cùng miền giá trị."
      },
      {
        bad: "Cho rằng giá trị của Khóa ngoại không bao giờ được phép mang giá trị NULL.",
        good: "Khóa ngoại hoàn toàn có thể nhận giá trị NULL (trừ khi có thêm ràng buộc NOT NULL tường minh), thể hiện đối tượng con hiện thời chưa liên kết với đối tượng cha nào."
      }
    ],
    quizzes: [
      {
        level: "Nhận biết",
        badge: "🟢 Cấp độ 1: Nhận biết",
        q: "Nguyên lý 'Toàn vẹn thực thể' (Entity Integrity) trong mô hình dữ liệu quan hệ yêu cầu điều gì?",
        opts: [
          "Mọi bảng phải có ít nhất 1 khóa ngoại",
          "Không có bất kỳ thuộc tính nào thuộc Khóa chính được phép nhận giá trị NULL",
          "Giá trị khóa ngoại phải luôn luôn khác NULL",
          "Không được phép đổi tên bảng khi đang truy vấn"
        ],
        ans: 1,
        fb: "Chính xác! Toàn vẹn thực thể bắt buộc mọi thành phần của khóa chính không được phép là NULL để bảo đảm tính định danh duy nhất."
      },
      {
        level: "Thông hiểu",
        badge: "🟡 Cấp độ 2: Thông hiểu",
        q: "Một quan hệ có 3 khóa ứng viên là $K_1 = \{A\}$, $K_2 = \{B, C\}$, $K_3 = \{D\}$. Tập các thuộc tính khóa (Prime attributes) của quan hệ này là:",
        opts: [
          "$\{A\}$",
          "$\{A, D\}$",
          "$\{A, B, C, D\}$",
          "Chỉ có thuộc tính được chọn làm khóa chính"
        ],
        ans: 2,
        fb: "Đúng! Thuộc tính khóa (Prime attribute) là bất kỳ thuộc tính nào xuất hiện trong ít nhất một khóa ứng viên, do đó tập thuộc tính khóa là {A, B, C, D}."
      },
      {
        level: "Vận dụng",
        badge: "🔴 Cấp độ 3: Vận dụng & Bẫy",
        q: "Xét quan hệ `DEAN(`<u>`MaDA`</u>`, TenDA, MaPhongQuanLy)` với `MaPhongQuanLy` là khóa ngoại tham chiếu đến `PHONGBAN(MaPB)`. Thao tác nào sau đây trên CSDL CHẮC CHẮN KHÔNG BAO GIỜ gây vi phạm ràng buộc toàn vẹn tham chiếu?",
        opts: [
          "Thêm một bộ mới vào bảng `DEAN`",
          "Xóa một bộ khỏi bảng `PHONGBAN`",
          "Sửa giá trị `MaPB` trong bảng `PHONGBAN`",
          "Xóa một bộ bất kỳ khỏi bảng `DEAN`"
        ],
        ans: 3,
        fb: "Rất xuất sắc! Xóa một bản ghi ở bảng con (`DEAN`) không bao giờ làm ảnh hưởng đến bảng cha (`PHONGBAN`), nên chắc chắn không thể vi phạm ràng buộc tham chiếu."
      }
    ]
  },

  {
    id: "CSDL_06",
    cluster: "2",
    title: "Thuật toán chuyển đổi Lược đồ ER/EER sang Lược đồ Quan hệ",
    sources: "Slide UET.IS2099 Chương 3 Phần 1 (Slide 28–43)",
    ref: {
      slide_file: "C3_1.pptx",
      slide_name: "Chương 3 (Phần 1) — Mô hình Dữ liệu Quan hệ",
      pages: "Slide 28 – 43",
      page_start: 28,
      page_end: 43,
      section: "Mục 2: Chuyển lược đồ ER sang lược đồ Quan hệ; 7 bước quy tắc ánh xạ chuẩn mực",
      key_points: [
        "Bước 1: Ánh xạ kiểu thực thể thông thường (Regular Entity)",
        "Bước 2: Ánh xạ kiểu thực thể yếu (Weak Entity - lấy khóa chủ làm khóa ngoại ghép với khóa bộ phận)",
        "Bước 3: Ánh xạ kiểu liên kết 1 : 1 (Đưa khóa bên tham gia toàn phần sang làm khóa ngoại bên kia)",
        "Bước 4: Ánh xạ kiểu liên kết 1 : N (Đưa khóa chính của bên 1 sang làm khóa ngoại ở bảng bên N)",
        "Bước 5: Ánh xạ kiểu liên kết M : N (Tạo bảng liên kết riêng, khóa chính là hợp của 2 khóa ngoại)",
        "Bước 6: Ánh xạ thuộc tính đa trị (Tạo bảng riêng gồm khóa chính của thực thể + thuộc tính đa trị)",
        "Bước 7: Ánh xạ kiểu liên kết n-phân (n > 2) và Ánh xạ chuyên biệt hóa EER"
      ],
      remind: "Đây là dạng bài TỰ LUẬN BẮT BUỘC (Câu 2, 2.5 - 3 điểm) trong đề thi giữa kỳ và cuối kỳ UET. Hãy xem kỹ ví dụ chuyển đổi lược đồ Quản lý Công ty ở Slide C3_1 trang 42."
    },
    desc: "Nắm vững trọn vẹn 7 bước thuật toán ánh xạ chuyển đổi lược đồ ER/EER sang các bảng quan hệ, không bao giờ nhầm lẫn vị trí đặt khóa ngoại.",
    steps: [
      {
        t: "Thuật toán Ánh xạ 7 bước từ ER sang Lược đồ Quan hệ",
        c: `<p>Thuật toán ánh xạ chuẩn hóa biến đổi các thành phần đồ họa của sơ đồ ER thành các bảng quan hệ có cấu trúc chặt chẽ:</p>
            <ol>
              <li><b>Bước 1 — Kiểu thực thể thông thường (Regular Entity)</b>: Mỗi kiểu thực thể $E$ tạo thành một bảng quan hệ $R$. Giữ lại các thuộc tính đơn. Với thuộc tính tổng hợp, chỉ đưa các thuộc tính thành phần con vào. Khóa chính $PK(R) = PK(E)$.</li>
              <li><b>Bước 2 — Kiểu thực thể yếu (Weak Entity)</b>: Mỗi thực thể yếu $W$ phụ thuộc thực thể chủ $E$ tạo thành một bảng $R_W$. Khóa chính của $R_W$ là <b>tổ hợp gồm Khóa chính của $E$ (làm khóa ngoại) + Khóa bộ phận của $W$</b>:
                $$PK(R_W) = \{ PK(E), \text{PartialKey}(W) \}$$
              </li>
              <li><b>Bước 3 — Kiểu liên kết 1 : 1</b>: Có 3 cách tiếp cận, trong đó chuẩn nhất là <b>Cách tiếp cận Khóa ngoại</b>: Chọn bên tham gia toàn phần (Total participation) để đưa Khóa chính của bên kia vào làm Khóa ngoại (kèm các thuộc tính của liên kết).</li>
              <li><b>Bước 4 — Kiểu liên kết 1 : N</b>: <b>Nguyên tắc vàng: Đưa khóa của bên 1 sang bên N!</b> Thêm Khóa chính của bảng phía 1 vào làm Khóa ngoại ($FK$) của bảng phía $N$, cùng với các thuộc tính của mối liên kết.</li>
              <li><b>Bước 5 — Kiểu liên kết M : N</b>: Bắt buộc <b>tạo một bảng quan hệ mới</b> đại diện cho liên kết. Bảng này chứa: Khóa chính của 2 thực thể tham gia (đóng vai trò là 2 khóa ngoại), và các thuộc tính của mối liên kết. Khóa chính của bảng mới là <b>tổ hợp của cả 2 khóa ngoại</b>.</li>
              <li><b>Bước 6 — Thuộc tính Đa trị (Multivalued Attribute)</b>: Mỗi thuộc tính đa trị $A$ của thực thể $E$ được tách thành một bảng mới gồm: Khóa chính của $E$ (làm khóa ngoại) và thuộc tính $A$. Khóa chính của bảng mới là tổ hợp $\{ PK(E), A \}$.</li>
              <li><b>Bước 7 — Kiểu liên kết $n$-phân ($n > 2$)</b>: Tạo bảng mới chứa Khóa chính của tất cả $n$ thực thể tham gia làm khóa ngoại.</li>
            </ol>`
      },
      {
        t: "Ánh xạ Chuyên biệt hóa / Khái quát hóa (EER)",
        c: `<p>Đối với cấu trúc lớp cha $C$ và các lớp con $S_1, S_2, \dots, S_m$, có 4 phương án ánh xạ:</p>
            <ul>
              <li><b>Phương án A (Tạo bảng cho Lớp cha và tất cả Lớp con - Khuyên dùng)</b>: Tạo 1 bảng cho lớp cha $C$ và $m$ bảng cho các lớp con. Khóa chính của các bảng con chính là Khóa chính của lớp cha (vừa là $PK$, vừa là $FK$ tham chiếu về lớp cha). Phù hợp cho mọi ràng buộc.</li>
              <li><b>Phương án B (Chỉ tạo bảng cho các Lớp con)</b>: Không tạo bảng cho lớp cha. Mỗi lớp con có 1 bảng chứa đầy đủ cả thuộc tính cha lẫn thuộc tính con. <i>Chỉ áp dụng khi ràng buộc là {d, total}</i>.</li>
              <li><b>Phương án C (Gộp tất cả vào 1 bảng duy nhất với Biến chỉ báo loại)</b>: Tạo 1 bảng duy nhất chứa tất cả thuộc tính của cha và con, cộng thêm một cột <code>Loai</code> (Type flag) để phân biệt. Các thuộc tính không dùng sẽ bị NULL. <i>Áp dụng tốt khi các lớp con có ít thuộc tính riêng</i>.</li>
            </ul>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide C3_1 — Slide 30–33] Ánh xạ Liên kết 1:N và Thực thể Yếu trong QL Công ty",
        q: "Xét lược đồ ER gồm:<br>" +
           "- `PHONGBAN(`<u>`MaPB`</u>`, TenPB)` và `NHANVIEN(`<u>`MaNV`</u>`, HoTen)` có mối liên kết 1:N `LamViecCho` (1 phòng ban có nhiều nhân viên, 1 nhân viên thuộc 1 phòng ban).<br>" +
           "- `THANNHAN(`<u>`TenTN`</u>`, QuanHe)` là thực thể yếu liên kết với thực thể chủ `NHANVIEN`.<br>" +
           "Hãy chuyển đổi sơ đồ trên thành các lược đồ quan hệ chuẩn (chỉ rõ khóa chính và khóa ngoại).",
        sol: "<b>Áp dụng thuật toán chuyển đổi:</b><br>" +
             "1. <b>Bảng PHONGBAN</b>: <code>PHONGBAN(<u>MaPB</u>, TenPB)</code>.<br>" +
             "2. <b>Bảng NHANVIEN (Áp dụng Bước 4 cho liên kết 1:N)</b>: Đưa khóa bên 1 (<code>MaPB</code>) sang làm khóa ngoại ở bên N (<code>NHANVIEN</code>):<br>" +
             "   $$\\text{NHANVIEN}(\\underline{MaNV}, HoTen, MaPB)$$ (với $MaPB$ là $FK$ tham chiếu <code>PHONGBAN(MaPB)</code>).<br>" +
             "3. <b>Bảng THANNHAN (Áp dụng Bước 2 cho thực thể yếu)</b>:<br>" +
             "   $$\\text{THANNHAN}(\\underline{MaNV, TenTN}, QuanHe)$$<br>" +
             "   - Khóa chính phức hợp: <code>(MaNV, TenTN)</code>.<br>" +
             "   - Khóa ngoại: <code>MaNV</code> tham chiếu <code>NHANVIEN(MaNV)</code>."
      },
      {
        level: "Trung bình",
        t: "[Slide C3_1 — Slide 34–36] Ánh xạ Liên kết M:N Đăng ký Đề án",
        q: "Trong CSDL Công ty: Nhân viên tham gia vào các Đề án. Biết rằng một nhân viên có thể tham gia nhiều đề án, và một đề án có nhiều nhân viên tham gia. Khi tham gia, hệ thống ghi nhận `SoGio` làm việc trong tuần của nhân viên đó cho đề án. `NHANVIEN` có khóa `MaNV`, `DEAN` có khóa `MaDA`. Hãy chuyển đổi mối liên kết này sang mô hình quan hệ.",
        sol: "<b>Phân tích áp dụng Bước 5 (Liên kết M:N):</b><br>" +
             "- Vì đây là liên kết M:N có thuộc tính <code>SoGio</code>, ta bắt buộc phải tạo một bảng quan hệ mới, đặt tên là <code>PHANCONG</code> (hoặc <code>THAMGIA</code>).<br>" +
             "- Bảng này nhận khóa chính của <code>NHANVIEN</code> và <code>DEAN</code> làm 2 khóa ngoại:<br>" +
             "  $$\\text{PHANCONG}(\\underline{MaNV, MaDA}, SoGio)$$<br>" +
             "- <b>Khóa chính (PK):</b> Tổ hợp hai thuộc tính <code>(MaNV, MaDA)</code>.<br>" +
             "- <b>Khóa ngoại (FK):</b><br>" +
             "  + <code>MaNV</code> là $FK$ tham chiếu <code>NHANVIEN(MaNV)</code>.<br>" +
             "  + <code>MaDA</code> là $FK$ tham chiếu <code>DEAN(MaDA)</code>."
      },
      {
        level: "Vận dụng",
        t: "[Slide C3_1 — Slide 42–43] Chuyển đổi Lược đồ ER Hoàn chỉnh Công ty UET sang Quan hệ",
        q: "Bài tập lớn Slide C3_1 trang 42: Chuyển đổi lược đồ ER quản lý công ty hoàn chỉnh gồm: `NHANVIEN`, `PHONGBAN`, `DEAN`, `THANNHAN` với các mối liên kết:<br>" +
           "- `QuanLy` (1:1 giữa NHANVIEN và PHONGBAN, có thuộc tính `NgayNhanChuc`).<br>" +
           "- `LamViecCho` (1:N giữa PHONGBAN và NHANVIEN).<br>" +
           "- `ThamGia` (M:N giữa NHANVIEN và DEAN, có `SoGio`).<br>" +
           "- `DiaDiem_Phong` là thuộc tính đa trị của PHONGBAN.<br>" +
           "Viết danh sách các lược đồ quan hệ thu được kèm khóa chính và khóa ngoại.",
        sol: "<b>Kết quả chuyển đổi chuẩn xác 100% theo barem UET:</b><br>" +
             "1. <code>NHANVIEN(<u>MaNV</u>, HoDem, Ten, NgaySinh, DiaChi, Luong, MaPB, MaNguoiGiamSat)</code><br>" +
             "   - PK: <code>MaNV</code>; FK1: <code>MaPB</code> $\\to$ <code>PHONGBAN(MaPB)</code>; FK2: <code>MaNguoiGiamSat</code> $\\to$ <code>NHANVIEN(MaNV)</code> (Liên kết đệ quy).<br>" +
             "2. <code>PHONGBAN(<u>MaPB</u>, TenPB, TruongPhong_MaNV, NgayNhanChuc)</code><br>" +
             "   - PK: <code>MaPB</code>; FK: <code>TruongPhong_MaNV</code> $\\to$ <code>NHANVIEN(MaNV)</code> (Ánh xạ liên kết 1:1 QuanLy vào bảng tham gia toàn phần).<br>" +
             "3. <code>DIADIEM_PHONG(<u>MaPB, DiaDiem</u>)</code><br>" +
             "   - PK: <code>(MaPB, DiaDiem)</code>; FK: <code>MaPB</code> $\\to$ <code>PHONGBAN(MaPB)</code> (Ánh xạ thuộc tính đa trị).<br>" +
             "4. <code>DEAN(<u>MaDA</u>, TenDA, DiaDiemDA, MaPB_QuanLy)</code><br>" +
             "   - PK: <code>MaDA</code>; FK: <code>MaPB_QuanLy</code> $\\to$ <code>PHONGBAN(MaPB)</code>.<br>" +
             "5. <code>PHANCONG(<u>MaNV, MaDA</u>, SoGio)</code><br>" +
             "   - PK: <code>(MaNV, MaDA)</code>; FK1: <code>MaNV</code> $\\to$ <code>NHANVIEN(MaNV)</code>; FK2: <code>MaDA</code> $\\to$ <code>DEAN(MaDA)</code>.<br>" +
             "6. <code>THANNHAN(<u>MaNV, TenTN</u>, GioiTinh, NgaySinh, QuanHe)</code><br>" +
             "   - PK: <code>(MaNV, TenTN)</code>; FK: <code>MaNV</code> $\\to$ <code>NHANVIEN(MaNV)</code>."
      }
    ],
    pitfalls: [
      {
        bad: "Trong liên kết 1:N, đưa khóa chính của bên N sang làm khóa ngoại ở bên 1.",
        good: "Sai lầm nghiêm trọng! Phải luôn đưa khóa của bên 1 sang làm khóa ngoại của bên N. Nếu làm ngược lại, bảng bên 1 sẽ bị đa trị hoặc vi phạm tính nguyên tử của thuộc tính."
      },
      {
        bad: "Quên không đưa khóa chính của thực thể cha vào bảng chứa thuộc tính đa trị.",
        good: "Khi tách thuộc tính đa trị thành bảng mới, bắt buộc phải lấy khóa chính của thực thể cha kết hợp với thuộc tính đa trị đó để tạo thành khóa chính phức hợp."
      }
    ],
    quizzes: [
      {
        level: "Nhận biết",
        badge: "🟢 Cấp độ 1: Nhận biết",
        q: "Khi chuyển đổi một mối liên kết nhiều - nhiều (M:N) từ sơ đồ ER sang mô hình quan hệ, quy tắc chuẩn là:",
        opts: [
          "Thêm khóa của thực thể thứ nhất làm khóa ngoại ở thực thể thứ hai",
          "Tạo một bảng quan hệ mới, nhận khóa chính của cả hai thực thể làm khóa ngoại và tổ hợp của chúng làm khóa chính",
          "Gộp hai thực thể thành một bảng duy nhất",
          "Xóa bỏ thuộc tính của liên kết để đơn giản hóa"
        ],
        ans: 1,
        fb: "Chính xác! Mối liên kết M:N bắt buộc phải được chuyển đổi thành một bảng liên kết riêng, khóa chính là tổ hợp của 2 khóa ngoại tham chiếu đến 2 thực thể ban đầu."
      },
      {
        level: "Thông hiểu",
        badge: "🟡 Cấp độ 2: Thông hiểu",
        q: "Kiểu thực thể `KHACHHANG` có thuộc tính đa trị `SoDienThoai` (một khách hàng có thể có nhiều số). Khi chuyển sang mô hình quan hệ, bảng mới `KH_SDT` sẽ có khóa chính là:",
        opts: [
          "Chỉ có thuộc tính `SoDienThoai`",
          "Chỉ có thuộc tính `MaKH`",
          "Tổ hợp cả hai thuộc tính `(MaKH, SoDienThoai)`",
          "Tự sinh thêm một mã ID mới làm khóa chính"
        ],
        ans: 2,
        fb: "Đúng! Cần tổ hợp cả (MaKH, SoDienThoai) để phân biệt các số điện thoại khác nhau của cùng một khách hàng và các số trùng nhau giữa các khách hàng khác nhau."
      },
      {
        level: "Vận dụng",
        badge: "🔴 Cấp độ 3: Vận dụng & Bẫy",
        q: "Trong mối liên kết 1:1 giữa `PHONGBAN` và `NHANVIEN` (Trưởng phòng quản lý phòng ban): Biết rằng mỗi phòng ban BẮT BUỘC phải có 1 trưởng phòng (tham gia toàn phần), nhưng chỉ một số ít nhân viên được làm trưởng phòng (tham gia một phần). Vị trí đặt khóa ngoại tối ưu nhất để tránh giá trị NULL là:",
        opts: [
          "Đặt `MaPB` làm khóa ngoại trong bảng `NHANVIEN`",
          "Đặt `TruongPhong_MaNV` làm khóa ngoại trong bảng `PHONGBAN`",
          "Tạo một bảng liên kết trung gian riêng `QUANLY`",
          "Đặt ở bảng nào cũng có số lượng giá trị NULL như nhau"
        ],
        ans: 1,
        fb: "Rất xuất sắc! Vì mọi phòng ban đều có trưởng phòng (toàn phần), nên đặt `TruongPhong_MaNV` vào bảng `PHONGBAN` sẽ không bao giờ bị giá trị NULL. Nếu đặt ngược lại vào `NHANVIEN`, hàng trăm nhân viên không làm trưởng phòng sẽ bị gán NULL ở cột chức vụ này!"
      }
    ]
  }
];

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { CUM_2_CSDL };
}
