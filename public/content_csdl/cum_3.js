// ==========================================================================
// CỤM 3 (CSDL): ĐẠI SỐ QUAN HỆ (RELATIONAL ALGEBRA)
// Bao gồm: Bài CSDL_07, CSDL_08, CSDL_09
// Nguồn: Slide UET.IS2099 C3_2.pdf (111 trang)
// ==========================================================================

const CUM_3_CSDL = [
  {
    id: "CSDL_07",
    cluster: "3",
    title: "Đại số quan hệ: Phép Chọn (σ), Chiếu (π) & Phép toán Tập hợp",
    sources: "Slide UET.IS2099 Chương 3 Phần 2 (Slide 1–35)",
    ref: {
      slide_file: "C3_2.pdf",
      slide_name: "Chương 3 (Phần 2) — Đại số Quan hệ",
      pages: "Slide 1 – 35",
      page_start: 1,
      page_end: 35,
      section: "Mục 2.1: Phép toán tập hợp (Hợp, Giao, Trừ, Tích Descartes); Mục 2.2: Phép chọn σ; Mục 2.3: Phép chiếu π; Mục 2.4: Phép đổi tên ρ",
      key_points: [
        "Định nghĩa Đại số quan hệ: Ngôn ngữ truy vấn hình thức (Procedural Query Language)",
        "Điều kiện khả hợp (Union-compatible): Hai quan hệ phải cùng bậc và các thuộc tính tương ứng cùng miền giá trị",
        "Phép hợp (∪), Giao (∩), Trừ (-), Tích Descartes (×)",
        "Phép chọn (Selection - σ): Lọc các bộ theo biểu thức điều kiện logic, giữ nguyên số cột",
        "Phép chiếu (Projection - π): Lọc danh sách cột và tự động loại bỏ các bộ trùng lặp (Set semantics)",
        "Phép đổi tên (Rename - ρ): Đổi tên quan hệ hoặc tên thuộc tính để tránh nhập nhằng"
      ],
      remind: "Phép chiếu luôn tự động khử trùng lặp; phép chọn chỉ lọc hàng chứ không bao giờ làm giảm số cột. Xem Slide C3_2 trang 25–35 để nắm chắc cú pháp."
    },
    desc: "Làm chủ 4 phép toán tập hợp và 3 phép toán đơn ngôi nền tảng: Chọn, Chiếu, Đổi tên trong đại số quan hệ.",
    steps: [
      {
        t: "Bản chất của Đại số Quan hệ & Điều kiện Khả hợp",
        c: `<p>Đại số quan hệ (Relational Algebra) là một hệ thống toán học gồm các phép toán nhận vào <b>một hoặc hai quan hệ</b> và trả về <b>một quan hệ mới duy nhất</b>. Tính chất này gọi là <b>Tính đóng (Closure property)</b>, cho phép lồng ghép nhiều phép toán vào nhau.</p>
            <div class="tip-box">
              <b>Điều kiện Khả hợp (Union-compatible):</b><br>
              Để thực hiện được các phép toán tập hợp (Hợp $\\cup$, Giao $\\cap$, Trừ $-$), hai quan hệ $R(A_1, \\dots, A_n)$ và $S(B_1, \\dots, B_m)$ bắt buộc phải thỏa mãn:
              <ol>
                <li>Cùng bậc: $n = m$ (cùng số lượng thuộc tính).</li>
                <li>Cùng miền giá trị tương ứng: $\\text{dom}(A_i) = \\text{dom}(B_i)$ với mọi $i = 1, \\dots, n$.</li>
              </ol>
            </div>`
      },
      {
        t: "Các phép toán Tập hợp: Hợp (∪), Giao (∩), Trừ (-) & Tích (×)",
        c: `<table class="data-table">
              <thead><tr><th>Phép toán</th><th>Ký hiệu</th><th>Định nghĩa toán học</th><th>Lưu ý đặc biệt</th></tr></thead>
              <tbody>
                <tr><td><b>Phép Hợp</b></td><td>$R \\cup S$</td><td>$\\{ t \\mid t \\in R \\lor t \\in S \\}$</td><td>Yêu cầu khả hợp; tự động loại bỏ bộ trùng.</td></tr>
                <tr><td><b>Phép Giao</b></td><td>$R \\cap S$</td><td>$\\{ t \\mid t \\in R \\land t \\in S \\}$</td><td>$R \\cap S = R - (R - S)$.</td></tr>
                <tr><td><b>Phép Trừ</b></td><td>$R - S$</td><td>$\\{ t \\mid t \\in R \\land t \\notin S \\}$</td><td>Có thứ tự: $R - S \\neq S - R$. Rất quan trọng để tìm 'không tham gia / chưa nợ'.</td></tr>
                <tr><td><b>Tích Descartes</b></td><td>$R \\times S$</td><td>$\\{ t_R \\circ t_S \\mid t_R \\in R, t_S \\in S \\}$</td><td><b>Không cần khả hợp</b>. Bậc kết quả $= n + m$; Số bộ $= |R| \\times |S|$.</td></tr>
              </tbody>
            </table>`
      },
      {
        t: "Phép Chọn (σ), Phép Chiếu (π) & Phép Đổi tên (ρ)",
        c: `<p>Ba phép toán cốt tử trên cấu trúc bảng:</p>
            <ul>
              <li><b>Phép Chọn (Selection - $\\sigma_{\\text{Điều kiện}}(R)$)</b>: Lấy ra các hàng (bộ) thỏa mãn điều kiện logic. Điều kiện có thể kết hợp các toán tử so sánh ($=, \\neq, <, \\le, >, \\ge$) và toán tử logic ($\\land, \\lor, \\neg$).
                $$\\sigma_{Luong > 15000000 \\land MaPB = 2}(NHANVIEN)$$
              </li>
              <li><b>Phép Chiếu (Projection - $\\pi_{A_1, A_2, \\dots, A_k}(R)$)</b>: Lấy ra danh sách các cột mong muốn và <b>tự động loại bỏ các hàng trùng lặp</b>:
                $$\\pi_{HoDem, Ten, Luong}(NHANVIEN)$$
              </li>
              <li><b>Phép Đổi tên (Rename - $\\rho_{S}(R)$ hoặc $\\rho_{S(B_1, \\dots, B_n)}(R)$)</b>: Dùng để đổi tên quan hệ $R$ thành $S$ hoặc đổi tên thuộc tính để phân biệt khi kết nối bảng với chính nó.</li>
            </ul>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide C3_2 — Slide 22–28] Phép Chọn và Chiếu trên Bảng Sinh viên UET",
        q: "Cho lược đồ `SINHVIEN(`<u>`MaSV`</u>`, HoTen, Khoa, DiemTB)`. Hãy viết biểu thức đại số quan hệ để lấy ra danh sách Họ tên và Điểm trung bình của tất cả các sinh viên thuộc Khoa 'CNTT' có Điểm trung bình từ 8.0 trở lên.",
        sol: "<b>Phân tích từng bước:</b><br>" +
             "1. Bước 1 (Lọc hàng thỏa mãn điều kiện): Áp dụng phép chọn $\\sigma$:<br>" +
             "   $$R_1 = \\sigma_{Khoa = 'CNTT' \\land DiemTB \\ge 8.0}(SINHVIEN)$$<br>" +
             "2. Bước 2 (Lọc cột cần hiển thị): Áp dụng phép chiếu $\\pi$ trên $R_1$:<br>" +
             "   $$\\text{Kết quả} = \\pi_{HoTen, DiemTB}(\\sigma_{Khoa = 'CNTT' \\land DiemTB \\ge 8.0}(SINHVIEN))$$"
      },
      {
        level: "Trung bình",
        t: "[Slide C3_2 — Slide 41] Tìm Danh sách Sinh viên Nợ môn bằng Phép Trừ (-)",
        q: "Ví dụ 7 Slide C3_2 trang 41: Cho hai bảng:<br>" +
           "- `SINHVIEN(`<u>`MaSV`</u>`, HoTen)`<br>" +
           "- `DANGKY(`<u>`MaSV, MaMH`</u>`, DiemSo)`<br>" +
           "Hãy viết biểu thức đại số quan hệ tìm mã và họ tên của những sinh viên <b>chưa từng đăng ký học môn nào</b>.",
        sol: "<b>Phân tích kỹ thuật dùng Phép Trừ:</b><br>" +
             "1. Tìm danh sách tất cả các mã sinh viên trong trường: $A = \\pi_{MaSV}(SINHVIEN)$.<br>" +
             "2. Tìm danh sách các mã sinh viên đã từng đăng ký ít nhất một môn: $B = \\pi_{MaSV}(DANGKY)$.<br>" +
             "3. Lấy tập $A$ trừ tập $B$ để ra mã các sinh viên chưa đăng ký môn nào:<br>" +
             "   $$C = A - B = \\pi_{MaSV}(SINHVIEN) - \\pi_{MaSV}(DANGKY)$$<br>" +
             "4. Kết nối tự nhiên lại với bảng `SINHVIEN` để lấy Họ tên:<br>" +
             "   $$\\text{Kết quả} = \\pi_{MaSV, HoTen}(SINHVIEN \\bowtie C)$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide C3_2 — Slide 52] Kết hợp Tích Descartes (×), Phép Chọn và Đổi tên",
        q: "Cho lược đồ `NHANVIEN(`<u>`MaNV`</u>`, HoTen, Luong, MaNQL)` trong đó `MaNQL` là mã người quản lý (cũng là một nhân viên). Viết biểu thức đại số quan hệ tìm Họ tên của các nhân viên có mức lương cao hơn mức lương của chính người quản lý trực tiếp của họ.",
        sol: "<b>Phân tích tự kết nối (Self-join):</b><br>" +
             "1. Đổi tên quan hệ `NHANVIEN` thành `NQL` để phân biệt nhân viên thường với quản lý:<br>" +
             "   $$\\rho_{NQL}(NHANVIEN)$$<br>" +
             "2. Nhân tích Descartes giữa nhân viên và quản lý, sau đó lọc bộ có mã quản lý khớp nhau và lương nhân viên lớn hơn lương quản lý:<br>" +
             "   $$R_1 = \\sigma_{NHANVIEN.MaNQL = NQL.MaNV \\land NHANVIEN.Luong > NQL.Luong}(NHANVIEN \\times \\rho_{NQL}(NHANVIEN))$$<br>" +
             "3. Chiếu lấy họ tên nhân viên:<br>" +
             "   $$\\text{Kết quả} = \\pi_{NHANVIEN.HoTen}(R_1)$$"
      }
    ],
    pitfalls: [
      {
        bad: "Thực hiện phép Hợp (∪) hoặc Trừ (-) giữa hai bảng không khả hợp (khác số lượng thuộc tính hoặc khác kiểu dữ liệu).",
        good: "Luôn phải dùng phép chiếu $\pi$ để đưa hai bảng về cùng số lượng cột và cùng miền dữ liệu trước khi thực hiện hợp, giao, trừ."
      },
      {
        bad: "Nghĩ rằng phép Chiếu (π) giữ nguyên số lượng hàng của bảng gốc.",
        good: "Phép chiếu tuân thủ lý thuyết tập hợp, tự động loại bỏ mọi bộ trùng lặp. Nếu chiếu trên các thuộc tính không phải là siêu khóa, số hàng kết quả có thể ít hơn bảng ban đầu!"
      }
    ],
    quizzes: [
      {
        level: "Nhận biết",
        badge: "🟢 Cấp độ 1: Nhận biết",
        q: "Ký hiệu nào trong Đại số quan hệ đại diện cho phép Chiếu (Projection - chọn danh sách các cột)?",
        opts: [
          "$\\sigma$ (Sigma)",
          "$\\pi$ (Pi)",
          "$\\rho$ (Rho)",
          "$\\gamma$ (Gamma)"
        ],
        ans: 1,
        fb: "Chính xác! $\\pi$ (Pi) là phép Chiếu danh sách các cột; $\\sigma$ (Sigma) là phép Chọn các hàng theo điều kiện."
      },
      {
        level: "Thông hiểu",
        badge: "🟡 Cấp độ 2: Thông hiểu",
        q: "Quan hệ $R$ có 4 thuộc tính và 10 bộ dữ liệu. Quan hệ $S$ có 3 thuộc tính và 5 bộ dữ liệu. Kết quả của phép tích Descartes $R \\times S$ có bậc (số cột) và lực lượng (số hàng) lần lượt là:",
        opts: [
          "7 cột và 15 hàng",
          "12 cột và 50 hàng",
          "7 cột và 50 hàng",
          "4 cột và 10 hàng"
        ],
        ans: 2,
        fb: "Đúng! Số cột của tích Descartes bằng tổng số cột: $4 + 3 = 7$; Số hàng bằng tích số hàng: $10 \\times 5 = 50$."
      },
      {
        level: "Vận dụng",
        badge: "🔴 Cấp độ 3: Vận dụng & Bẫy",
        q: "Để tìm danh sách các phòng ban CHƯA CÓ bất kỳ nhân viên nào làm việc, kỹ thuật biểu diễn đại số quan hệ chuẩn nhất là:",
        opts: [
          "$\\pi_{MaPB}(PHONGBAN) \\cup \\pi_{MaPB}(NHANVIEN)$",
          "$\\pi_{MaPB}(PHONGBAN) - \\pi_{MaPB}(NHANVIEN)$",
          "$\\sigma_{MaPB = NULL}(PHONGBAN)$",
          "$\\pi_{MaPB}(PHONGBAN) \\cap \\pi_{MaPB}(NHANVIEN)$"
        ],
        ans: 1,
        fb: "Xuất sắc! Lấy toàn bộ mã phòng ban trừ đi các mã phòng ban đang có nhân viên làm việc: $\\pi_{MaPB}(PHONGBAN) - \\pi_{MaPB}(NHANVIEN)$ sẽ cho ra các phòng ban trống."
      }
    ]
  },

  {
    id: "CSDL_08",
    cluster: "3",
    title: "Các phép Kết nối: Kết nối tự nhiên (⨝), Theta-Join & Outer Join",
    sources: "Slide UET.IS2099 Chương 3 Phần 2 (Slide 36–70)",
    ref: {
      slide_file: "C3_2.pdf",
      slide_name: "Chương 3 (Phần 2) — Đại số Quan hệ",
      pages: "Slide 36 – 70",
      page_start: 36,
      page_end: 70,
      section: "Mục 2.5: Phép kết nối có điều kiện (Theta-Join); Kết nối bằng (Equijoin); Kết nối tự nhiên (Natural Join ⨝); Các phép kết nối ngoài (Outer Joins)",
      key_points: [
        "Theta-Join (⨝_θ): Tích Descartes đi kèm điều kiện chọn θ: R ⨝_θ S = σ_θ(R × S)",
        "Equijoin: Điều kiện θ chỉ gồm các dấu bằng (=)",
        "Kết nối tự nhiên (Natural Join - ⨝): Tự động kết nối trên các thuộc tính cùng tên và chỉ giữ lại 1 cột chung",
        "Treo dữ liệu (Dangling Tuples): Các bộ không có đối tác kết nối sẽ bị biến mất khỏi kết quả Inner Join",
        "Kết nối ngoài (Outer Joins): Trái (⟕), Phải (⟖), Toàn phần (⟗) — giữ lại các bộ treo và điền NULL vào các cột thiếu"
      ],
      remind: "Kết nối tự nhiên và Kết nối ngoài luôn xuất hiện trong các bài thi UET. Hãy xem bảng minh họa Dangling Tuples tại Slide C3_2 trang 55–68."
    },
    desc: "Nắm vững cơ chế hoạt động của các phép kết nối: kết nối tự nhiên, theta-join, equijoin và cứu vãn bộ treo bằng các phép kết nối ngoài (Outer Joins).",
    steps: [
      {
        t: "Phép Kết nối có điều kiện (Theta-Join) & Equijoin",
        c: `<p>Trong thực tế, phép tích Descartes $R \\times S$ sinh ra quá nhiều bộ vô nghĩa. Phép kết nối ra đời để ghép các bộ có liên hệ logic:</p>
            <ul>
              <li><b>Theta-Join ($R \\bowtie_{\\theta} S$)</b>: Là sự kết hợp giữa tích Descartes và phép chọn theo điều kiện $\\theta$:
                $$R \\bowtie_{\\theta} S = \\sigma_{\\theta}(R \\times S)$$
              </li>
              <li><b>Kết nối bằng (Equijoin)</b>: Là Theta-join trong đó điều kiện $\\theta$ chỉ chứa toàn các phép so sánh bằng ($=$). Ví dụ: $NHANVIEN \\bowtie_{NHANVIEN.MaPB = PHONGBAN.MaPB} PHONGBAN$. Bậc của kết quả bằng tổng số thuộc tính của cả hai bảng (vẫn giữ nguyên 2 cột MaPB).</li>
            </ul>`
      },
      {
        t: "Kết nối tự nhiên (Natural Join - ⨝)",
        c: `<p><b>Kết nối tự nhiên ($R \\bowtie S$)</b> là phép kết nối bằng đặc biệt và phổ biến nhất:</p>
            <ol>
              <li>Hệ thống <b>tự động tìm tất cả các thuộc tính có cùng tên</b> giữa hai quan hệ $R$ và $S$.</li>
              <li>So sánh bằng trên các thuộc tính cùng tên này.</li>
              <li><b>Tự động loại bỏ các cột trùng lặp</b>, chỉ giữ lại đúng một cột đại diện trong kết quả.</li>
            </ol>
            <div class="tip-box">
              <b>Ví dụ:</b> $R(A, B, C)$ và $S(B, C, D)$ có 2 thuộc tính cùng tên là $B$ và $C$.<br>
              Khi thực hiện $R \\bowtie S$, điều kiện so sánh ngầm là $R.B = S.B \\land R.C = S.C$, và lược đồ kết quả chỉ có 4 cột: $T(A, B, C, D)$.
            </div>`
      },
      {
        t: "Bộ treo (Dangling Tuples) & Các phép Kết nối Ngoài (Outer Joins)",
        c: `<p>Trong phép kết nối thông thường (Inner Join), nếu một bộ trong $R$ không tìm thấy bất kỳ bộ nào trong $S$ thỏa mãn điều kiện kết nối, bộ đó sẽ <b>bị loại bỏ hoàn toàn (gọi là Bộ treo - Dangling tuple)</b>.</p>
            <p>Để giữ lại các thông tin này, ta dùng <b>Phép Kết nối Ngoài (Outer Join)</b>, tự động bù giá trị <code>NULL</code> vào các thuộc tính bị thiếu:</p>
            <table class="data-table">
              <thead><tr><th>Phép toán</th><th>Ký hiệu</th><th>Nguyên tắc giữ lại dữ liệu</th></tr></thead>
              <tbody>
                <tr><td><b>Kết nối ngoài Trái (Left Outer Join)</b></td><td>$R \\mathbin{⟕} S$</td><td>Giữ lại <b>toàn bộ các bộ của bảng bên trái ($R$)</b>. Nếu bộ nào không khớp với $S$, các thuộc tính của $S$ sẽ điền <code>NULL</code>.</td></tr>
                <tr><td><b>Kết nối ngoài Phải (Right Outer Join)</b></td><td>$R \\mathbin{⟖} S$</td><td>Giữ lại <b>toàn bộ các bộ của bảng bên phải ($S$)</b>. Các thuộc tính của $R$ không khớp sẽ điền <code>NULL</code>.</td></tr>
                <tr><td><b>Kết nối ngoài Toàn phần (Full Outer Join)</b></td><td>$R \\mathbin{⟗} S$</td><td>Giữ lại <b>toàn bộ các bộ của cả hai bảng</b> $R$ và $S$.</td></tr>
              </tbody>
            </table>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide C3_2 — Slide 45–48] Kết nối Tự nhiên Nhân viên và Phòng ban",
        q: "Cho `NHANVIEN(`<u>`MaNV`</u>`, HoTen, MaPB)` và `PHONGBAN(`<u>`MaPB`</u>`, TenPB)`. Viết biểu thức đại số quan hệ lấy ra Mã NV, Họ tên và Tên phòng ban của tất cả nhân viên.",
        sol: "<b>Phân tích:</b><br>" +
             "- Hai bảng có chung thuộc tính <code>MaPB</code>.<br>" +
             "- Thực hiện phép kết nối tự nhiên $\\bowtie$ để ghép thông tin, sau đó dùng phép chiếu $\\pi$:<br>" +
             "  $$\\text{Kết quả} = \\pi_{MaNV, HoTen, TenPB}(NHANVIEN \\bowtie PHONGBAN)$$"
      },
      {
        level: "Trung bình",
        t: "[Slide C3_2 — Slide 60–65] Giữ lại Nhân viên chưa có Phòng ban bằng Left Outer Join",
        q: "Công ty có một số nhân viên mới chưa được phân công phòng ban (`MaPB = NULL`). Nếu thực hiện `NHANVIEN ⨝ PHONGBAN` thì các nhân viên này bị biến mất. Hãy viết biểu thức đại số quan hệ để lấy danh sách toàn bộ nhân viên (kể cả người chưa có phòng ban) kèm tên phòng ban của họ.",
        sol: "<b>Áp dụng Phép Kết nối ngoài Trái (Left Outer Join):</b><br>" +
             "- Dùng $NHANVIEN \\mathbin{⟕} PHONGBAN$:<br>" +
             "  $$\\text{Kết quả} = \\pi_{MaNV, HoTen, TenPB}(NHANVIEN \\mathbin{⟕} PHONGBAN)$$<br>" +
             "- Với những nhân viên chưa có phòng ban, cột <code>TenPB</code> sẽ hiển thị giá trị <code>NULL</code> thay vì bị mất dòng."
      },
      {
        level: "Vận dụng",
        t: "[Slide C3_2 — Slide 66–70] Tìm Dự án chưa có Nhân viên tham gia bằng Phép Kết nối Ngoài",
        q: "Cho `DEAN(`<u>`MaDA`</u>`, TenDA)` và `PHANCONG(`<u>`MaNV, MaDA`</u>`, SoGio)`. Hãy viết biểu thức đại số quan hệ sử dụng phép kết nối ngoài để tìm Tên các đề án hiện tại chưa có bất kỳ nhân viên nào được phân công làm việc.",
        sol: "<b>Phân tích kỹ thuật lọc bộ treo qua Left Join:</b><br>" +
             "1. Thực hiện Left Outer Join giữa `DEAN` và `PHANCONG` theo `MaDA`:<br>" +
             "   $$R_1 = DEAN \\mathbin{⟕} PHANCONG$$<br>" +
             "2. Những đề án chưa có ai tham gia sẽ có thuộc tính <code>MaNV</code> mang giá trị <code>NULL</code>:<br>" +
             "   $$R_2 = \\sigma_{MaNV = NULL}(R_1)$$<br>" +
             "3. Chiếu lấy tên đề án:<br>" +
             "   $$\\text{Kết quả} = \\pi_{TenDA}(R_2)$$"
      }
    ],
    pitfalls: [
      {
        bad: "Dùng Kết nối tự nhiên (⨝) khi hai bảng có hai thuộc tính trùng tên nhưng khác bản chất ngữ nghĩa.",
        good: "Ví dụ cả NHANVIEN và PHONGBAN đều có cột 'Ten' (TenNV và TenPB). Kết nối tự nhiên sẽ bắt TenNV = TenPB, dẫn tới kết quả rỗng! Cần dùng Theta-Join chỉ định rõ ràng hoặc đổi tên thuộc tính trước khi kết nối."
      },
      {
        bad: "Nhầm lẫn giữa Left Outer Join và Inner Join trong các bài toán yêu cầu giữ lại toàn bộ đối tượng chính.",
        good: "Hễ đề bài có cụm từ 'kể cả những sinh viên chưa đăng ký', 'kể cả khách hàng chưa mua hàng' thì bắt buộc phải dùng Phép kết nối ngoài (Outer Join)."
      }
    ],
    quizzes: [
      {
        level: "Nhận biết",
        badge: "🟢 Cấp độ 1: Nhận biết",
        q: "Phép toán nào sau đây tự động so sánh bằng trên các thuộc tính có cùng tên giữa hai quan hệ và loại bỏ các cột trùng lặp?",
        opts: [
          "Theta-Join ($\\bowtie_{\\theta}$)",
          "Equijoin",
          "Kết nối tự nhiên (Natural Join - $\\bowtie$)",
          "Tích Descartes ($\\times$)"
        ],
        ans: 2,
        fb: "Chính xác! Kết nối tự nhiên ($\\bowtie$) tự động phát hiện các cột trùng tên, ghép bằng và chỉ giữ lại 1 cột duy nhất trong kết quả."
      },
      {
        level: "Thông hiểu",
        badge: "🟡 Cấp độ 2: Thông hiểu",
        q: "Trong phép kết nối ngoài Trái $R \\mathbin{⟕} S$, một bộ $t \in R$ không có đối tác nào phù hợp trong $S$. Bộ $t$ này sẽ xuất hiện trong kết quả như thế nào?",
        opts: [
          "Bị loại bỏ hoàn toàn",
          "Vẫn xuất hiện trong kết quả, các thuộc tính tương ứng lấy từ $S$ sẽ nhận giá trị NULL",
          "Làm cho toàn bộ câu truy vấn bị lỗi",
          "Tự động điền giá trị 0 vào tất cả các cột"
        ],
        ans: 1,
        fb: "Đúng! Left Outer Join bảo toàn mọi bộ của quan hệ bên trái, nếu không khớp thì điền NULL vào các cột của bảng bên phải."
      },
      {
        level: "Vận dụng",
        badge: "🔴 Cấp độ 3: Vận dụng & Bẫy",
        q: "Cho $R(A, B)$ có 3 bộ: `(1, 10), (2, 20), (3, 30)` và $S(B, C)$ có 2 bộ: `(20, 'X'), (40, 'Y')`. Kết quả của $R \\mathbin{⟕} S$ có bao nhiêu bộ và bao nhiêu cột?",
        opts: [
          "3 bộ và 3 cột",
          "2 bộ và 4 cột",
          "1 bộ và 3 cột",
          "4 bộ và 3 cột"
        ],
        ans: 0,
        fb: "Rất chuẩn! Kết quả gồm 3 cột (A, B, C) và 3 bộ (tương ứng với cả 3 bộ của R): (1, 10, NULL), (2, 20, 'X'), (3, 30, NULL)."
      }
    ]
  },

  {
    id: "CSDL_09",
    cluster: "3",
    title: "Phép Chia (÷), Gom nhóm (γ) & Tối ưu hóa Cây truy vấn",
    sources: "Slide UET.IS2099 Chương 3 Phần 2 (Slide 71–111)",
    ref: {
      slide_file: "C3_2.pdf",
      slide_name: "Chương 3 (Phần 2) — Đại số Quan hệ",
      pages: "Slide 71 – 111",
      page_start: 71,
      page_end: 111,
      section: "Mục 2.6: Phép chia (Division ÷); Mục 2.7: Phép toán Gom nhóm và Hàm gộp (γ); Mục 3: Cây biểu diễn truy vấn & Tối ưu hóa",
      key_points: [
        "Phép chia (Division - ÷): Mô hình hóa câu hỏi phổ quát 'Cho tất cả' (For all)",
        "Công thức giải tích của phép chia: T(Y) = R(Z) ÷ S(X) qua phép chiếu và phép trừ",
        "Phép gom nhóm và Hàm gộp (Aggregation - γ): COUNT, SUM, AVG, MIN, MAX theo nhóm thuộc tính",
        "Biểu diễn Cây truy vấn quan hệ (Query Tree / Relational Algebra Tree)",
        "Các quy tắc tương đương & Tối ưu hóa truy vấn: Đẩy phép chọn σ và phép chiếu π xuống thấp nhất có thể trước phép kết nối"
      ],
      remind: "Phép chia và Cây truy vấn tối ưu là điểm phân loại 9–10 trong bài thi tự luận UET. Xem công thức 4 bước tính phép chia tại Slide C3_2 trang 79."
    },
    desc: "Chinh phục dạng bài khó nhất trong Đại số quan hệ: giải quyết câu hỏi 'cho tất cả' bằng Phép Chia, thống kê với Gom nhóm và tối ưu hóa Cây truy vấn.",
    steps: [
      {
        t: "Phép Chia (Division - ÷) cho bài toán 'Cho tất cả'",
        c: `<p>Phép chia được thiết kế chuyên biệt để trả lời cho các câu hỏi chứa mệnh đề <b>'cho tất cả' (For all)</b>:</p>
            <ul>
              <li>Ví dụ: <i>'Tìm nhân viên tham gia TẤT CẢ các đề án của công ty'</i>, <i>'Tìm sinh viên đã học TẤT CẢ các môn của ngành CNTT'</i>.</li>
              <li>Ký hiệu: $R(Z) \\div S(X)$, trong đó $X \\subset Z$. Đặt $Y = Z - X$. Kết quả trả về quan hệ $T(Y)$ gồm các bộ giá trị $y$ sao cho với mọi bộ $x \\in S$, bộ ghép $\\langle y, x \\rangle$ đều xuất hiện trong $R$.</li>
            </ul>
            <div class="tip-box">
              <b>Thuật toán 4 bước tính $T(Y) = R(Z) \\div S(X)$ qua các phép toán cơ bản (Slide C3_2 tr. 79):</b><br>
              1. Xác định tập thuộc tính kết quả: $Y = Z - X$.<br>
              2. Lấy tất cả các giá trị $Y$ có trong $R$: $T_1 = \\pi_Y(R)$.<br>
              3. Tìm các giá trị $Y$ KHÔNG thỏa mãn tất cả (bằng cách lấy tích Đề-các với $S$ rồi trừ $R$):<br>
                 $$T_2 = \\pi_Y((T_1 \\times S) - R)$$<br>
              4. Kết quả chính thức là lấy toàn bộ trừ đi những trường hợp không thỏa mãn:<br>
                 $$T = T_1 - T_2$$
            </div>`
      },
      {
        t: "Phép Gom nhóm & Hàm gộp (γ)",
        c: `<p>Trong thực tế phân tích dữ liệu, ta cần tính toán các đại lượng thống kê (tổng, trung bình, đếm số lượng):</p>
            <ul>
              <li>Ký hiệu: $_{G_1, G_2, \dots, G_k}\\gamma_{f_1(A_1), f_2(A_2), \dots}(R)$</li>
              <li>Trong đó:
                <ul>
                  <li>$G_1, \dots, G_k$: Danh sách các thuộc tính dùng để phân nhóm (Grouping attributes). (Nếu không có $G_i$, gộp toàn bộ bảng thành 1 nhóm).</li>
                  <li>$f_i$: Hàm gộp tổng hợp, gồm: <code>COUNT</code>, <code>SUM</code>, <code>AVG</code>, <code>MIN</code>, <code>MAX</code>.</li>
                  <li>$A_i$: Thuộc tính được áp dụng hàm gộp.</li>
                </ul>
              </li>
              <li><b>Ví dụ:</b> Tìm mã phòng ban và mức lương trung bình của từng phòng:<br>
                $$_{MaPB}\\gamma_{AVG(Luong)}(NHANVIEN)$$
              </li>
            </ul>`
      },
      {
        t: "Biểu diễn Cây truy vấn & Chiến lược Tối ưu hóa",
        c: `<p>Mỗi câu truy vấn đại số quan hệ có thể được biểu diễn dưới dạng một <b>Cây truy vấn (Query Tree)</b>:</p>
            <ul>
              <li><b>Nút lá (Leaves)</b>: Các quan hệ nguồn trong CSDL.</li>
              <li><b>Nút trong (Internal nodes)</b>: Các phép toán đại số quan hệ ($\\sigma, \\pi, \\bowtie, \\times$).</li>
              <li><b>Nút gốc (Root)</b>: Kết quả cuối cùng của truy vấn.</li>
            </ul>
            <div class="warn-box">
              <b>Nguyên tắc vàng tối ưu hóa cây truy vấn (Slide C3_2 tr. 102–110):</b><br>
              • <b>Đẩy phép chọn ($\\sigma$) xuống sâu nhất có thể</b>: Thực hiện lọc hàng càng sớm càng tốt để giảm kích thước trung gian trước khi thực hiện các phép kết nối hoặc tích Đề-các đắt đỏ.<br>
              • <b>Đẩy phép chiếu ($\\pi$) xuống sớm</b>: Loại bỏ ngay các cột không cần thiết để giảm độ rộng bản ghi.<br>
              • <b>Thay thế $( \\times + \\sigma )$ bằng phép kết nối ($\\bowtie$)</b>.
            </div>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide C3_2 — Slide 93–96] Phép Gom nhóm đếm số Nhân viên mỗi Phòng ban",
        q: "Cho `NHANVIEN(`<u>`MaNV`</u>`, HoTen, MaPB, Luong)`. Viết biểu thức đại số quan hệ tìm Mã phòng ban, số lượng nhân viên và tổng quỹ lương của mỗi phòng ban.",
        sol: "<b>Áp dụng Phép gom nhóm $\\gamma$:</b><br>" +
             "- Thuộc tính gom nhóm: <code>MaPB</code>.<br>" +
             "- Các hàm gộp: <code>COUNT(MaNV)</code> và <code>SUM(Luong)</code>.<br>" +
             "  $$_{MaPB}\\gamma_{\\text{COUNT}(MaNV), \\text{SUM}(Luong)}(NHANVIEN)$$"
      },
      {
        level: "Trung bình",
        t: "[Slide C3_2 — Slide 76–84] Bài toán Phép chia Tìm Nhân viên làm Tất cả Đề án",
        q: "Cho các quan hệ:<br>" +
           "- `DEAN(`<u>`MaDA`</u>`, TenDA)`<br>" +
           "- `PHANCONG(`<u>`MaNV, MaDA`</u>`, SoGio)`<br>" +
           "Viết biểu thức đại số quan hệ tìm Mã của các nhân viên tham gia <b>TẤT CẢ</b> các đề án hiện có của công ty.",
        sol: "<b>Phân tích bản chất Phép Chia:</b><br>" +
             "1. Tập chia (Tất cả các đề án): $S = \\pi_{MaDA}(DEAN)$.<br>" +
             "2. Tập bị chia (Nhân viên và đề án họ làm): $R = \\pi_{MaNV, MaDA}(PHANCONG)$.<br>" +
             "3. Áp dụng phép chia $R \\div S$:<br>" +
             "   $$\\text{Kết quả} = \\pi_{MaNV, MaDA}(PHANCONG) \\div \\pi_{MaDA}(DEAN)$$<br>" +
             "Kết quả trả về chính xác các <code>MaNV</code> mà kết hợp với mọi <code>MaDA</code> trong $S$ đều có mặt trong $PHANCONG$."
      },
      {
        level: "Vận dụng",
        t: "[Slide C3_2 — Slide 104–108] Tối ưu hóa Cây truy vấn bằng cách Đẩy Phép Chọn",
        q: "Xét câu truy vấn chưa tối ưu: $\\pi_{HoTen}(\\sigma_{TenPB = 'Nghiên cứu' \\land Luong > 20000000}(NHANVIEN \\bowtie PHONGBAN))$.<br>" +
           "a) Vẽ cây truy vấn ban đầu.<br>" +
           "b) Áp dụng các quy tắc biến đổi tương đương để tối ưu hóa cây truy vấn.",
        sol: "<b>Phân tích tối ưu hóa theo Slide C3_2:</b><br>" +
             "a) <b>Cây ban đầu:</b> Kết nối toàn bộ <code>NHANVIEN</code> với <code>PHONGBAN</code> trước, sau đó mới lọc $\\sigma$ trên bảng kết quả khổng lồ $\\rightarrow$ Rất lãng phí bộ nhớ và CPU.<br>" +
             "b) <b>Cây tối ưu (Đẩy phép chọn xuống trước phép kết nối):</b><br>" +
             "- Tách điều kiện chọn: $\\sigma_{TenPB = 'Nghiên cứu'}$ chỉ liên quan đến bảng <code>PHONGBAN</code>; $\\sigma_{Luong > 20000000}$ chỉ liên quan đến <code>NHANVIEN</code>.<br>" +
             "- Đẩy chọn xuống từng bảng nguồn trước:<br>" +
             "  + $R_1 = \\sigma_{Luong > 20000000}(NHANVIEN)$<br>" +
             "  + $R_2 = \\sigma_{TenPB = 'Nghiên cứu'}(PHONGBAN)$<br>" +
             "- Chỉ kết nối giữa $R_1$ và $R_2$ (số lượng bản ghi đã giảm đi hàng chục lần):<br>" +
             "  $$\\text{Biểu thức tối ưu} = \\pi_{HoTen}((\\sigma_{Luong > 20000000}(NHANVIEN)) \\bowtie (\\sigma_{TenPB = 'Nghiên cứu'}(PHONGBAN)))$$"
      }
    ],
    pitfalls: [
      {
        bad: "Nghĩ rằng phép chia (÷) có thể thực hiện trên hai bảng bất kỳ mà không cần quan tâm đến tập thuộc tính.",
        good: "Phép chia $R(Z) \div S(X)$ bắt buộc yêu cầu tập thuộc tính $X$ của quan hệ chia phải là tập con thực sự của $Z$ ($X \subset Z$)."
      },
      {
        bad: "Thực hiện phép tích Descartes hoặc kết nối bảng trước, rồi mới áp dụng phép chọn lọc điều kiện.",
        good: "Đây là lỗi tối ưu hóa kinh điển! Trong bài thi tự luận UET, nếu không đẩy phép chọn $\sigma$ xuống trước phép kết nối, bạn sẽ bị trừ điểm tối ưu hóa câu truy vấn."
      }
    ],
    quizzes: [
      {
        level: "Nhận biết",
        badge: "🟢 Cấp độ 1: Nhận biết",
        q: "Phép toán Đại số quan hệ nào phù hợp nhất để trả lời câu hỏi: 'Tìm các khách hàng đã mua TẤT CẢ các sản phẩm do công ty sản xuất'?",
        opts: [
          "Phép kết nối tự nhiên ($\\bowtie$)",
          "Phép chia (Division - $\\div$)",
          "Phép gom nhóm ($\\gamma$)",
          "Phép kết nối ngoài (Outer Join)"
        ],
        ans: 1,
        fb: "Chính xác! Phép chia ($\\div$) được thiết kế riêng để giải quyết các truy vấn mang ngữ nghĩa phổ quát 'cho tất cả' (for all)."
      },
      {
        level: "Thông hiểu",
        badge: "🟡 Cấp độ 2: Thông hiểu",
        q: "Quy tắc cơ bản và quan trọng nhất trong tối ưu hóa cây biểu diễn câu truy vấn đại số quan hệ là:",
        opts: [
          "Đẩy phép chọn ($\\sigma$) và phép chiếu ($\\pi$) xuống sâu nhất có thể trước khi thực hiện phép kết nối",
          "Thực hiện tất cả các phép tích Descartes trước tiên",
          "Đổi tên tất cả các bảng sang tên viết tắt",
          "Không bao giờ sử dụng phép chiếu"
        ],
        ans: 0,
        fb: "Đúng! Đẩy phép chọn và phép chiếu xuống sớm giúp giảm tối đa kích thước dữ liệu trung gian, tăng tốc độ thực thi truy vấn."
      },
      {
        level: "Vận dụng",
        badge: "🔴 Cấp độ 3: Vận dụng & Bẫy",
        q: "Cho $R(A, B)$ có các bộ: `(x, 1), (x, 2), (y, 1), (z, 1), (z, 2), (z, 3)` và $S(B)$ có các bộ: `(1), (2)`. Kết quả của phép chia $R \\div S$ trả về tập thuộc tính nào và gồm những giá trị nào?",
        opts: [
          "Thuộc tính $B$ với giá trị `(1), (2)`",
          "Thuộc tính $A$ với các giá trị `(x), (z)`",
          "Thuộc tính $A$ với duy nhất giá trị `(z)`",
          "Thuộc tính $A$ với tất cả các giá trị `(x), (y), (z)`"
        ],
        ans: 1,
        fb: "Rất xuất sắc! Thuộc tính kết quả là $A = \{A, B\} - \{B\}$. Chỉ có `x` và `z` là kết hợp được với cả hai giá trị `1` và `2` của S (y chỉ kết hợp với 1 nên bị loại). Vậy kết quả là {x, z}."
      }
    ]
  }
];

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { CUM_3_CSDL };
}
