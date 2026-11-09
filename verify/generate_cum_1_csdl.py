import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

cum_1_code = """// ==========================================================================
// CỤM 1 (CSDL): TỔNG QUAN HỆ CƠ SỞ DỮ LIỆU & MÔ HÌNH THỰC THỂ - LIÊN KẾT (ER/EER)
// Bao gồm: Bài CSDL_01, CSDL_02, CSDL_03, CSDL_04
// Nguồn: Slide UET.IS2099 C1 .pptx, C2_1.pptx, C2_2.pptx
// ==========================================================================

const CUM_1_CSDL = [
  {
    id: "CSDL_01",
    cluster: "1",
    title: "Tổng quan về Hệ Cơ sở Dữ liệu & Kiến trúc 3 mức",
    sources: "Slide UET.IS2099 Chương 1 (Slide 1–52)",
    ref: {
      slide_file: "C1 .pptx",
      slide_name: "Chương 1 — Tổng quan về Hệ CSDL",
      pages: "Slide 1 – 52",
      page_start: 1,
      page_end: 52,
      section: "Mục 1.1: Mở đầu & Khái niệm; Mục 1.4: Người sử dụng; Mục 1.6: Kiến trúc 3 mức ANSI/SPARC",
      key_points: [
        "Khái niệm CSDL, Hệ QTCSDL (DBMS) và sự khác biệt giữa tệp truyền thống vs CSDL",
        "Kiến trúc 3 mức ANSI/SPARC: Mức trong (vật lý), Mức quan niệm (logic toàn cục), Mức ngoài (khung nhìn view)",
        "Tính độc lập dữ liệu: Độc lập logic (thay đổi mức quan niệm không ảnh hưởng mức ngoài) và Độc lập vật lý (thay đổi lưu trữ không ảnh hưởng mức quan niệm)",
        "Các nhóm người dùng: Quản trị viên CSDL (DBA), Người thiết kế CSDL, Lập trình viên ứng dụng, Người dùng cuối"
      ],
      remind: "Nếu bạn hay nhầm lẫn giữa Độc lập logic và Độc lập vật lý, hãy mở lại Slide C1 từ trang 40 đến trang 43 để xem sơ đồ kiến trúc 3 mức ANSI/SPARC."
    },
    desc: "Nắm vững bản chất của Hệ CSDL, ưu thế vượt trội so với quản lý tệp, kiến trúc 3 mức ANSI/SPARC và tính độc lập dữ liệu cốt lõi.",
    steps: [
      {
        t: "Tại sao cần Hệ Cơ sở Dữ liệu (DBMS)?",
        c: `<p>Trước khi có Hệ CSDL, dữ liệu được quản lý bằng các <b>hệ thống tệp truyền thống (File-processing systems)</b> dẫn tới nhiều nhược điểm nghiêm trọng:</p>
            <ul>
              <li><b>Dư thừa dữ liệu (Data Redundancy)</b>: Cùng một thông tin sinh viên được lưu rải rác ở nhiều phòng ban (Đào tạo, Tài vụ, Thư viện) gây lãng phí bộ nhớ.</li>
              <li><b>Không nhất quán (Inconsistency)</b>: Khi sinh viên đổi số điện thoại, một phòng ban cập nhật nhưng phòng ban khác giữ nguyên thông tin cũ.</li>
              <li><b>Khó chia sẻ & phụ thuộc chương trình - dữ liệu</b>: Cấu trúc file thay đổi thì toàn bộ mã nguồn chương trình ứng dụng phải viết lại.</li>
              <li><b>Kém an toàn và vi phạm tính toàn vẹn</b>: Thiếu cơ chế kiểm soát truy cập đồng thời và không bảo đảm tính nguyên tố (Atomicity) của giao dịch.</li>
            </ul>
            <div class="tip-box"><b>Định nghĩa CSDL (Database):</b> Là một tập hợp dữ liệu tác nghiệp được lưu trữ có cấu trúc, có mối liên hệ logic với nhau, được dùng chung cho nhiều ứng dụng và người dùng khác nhau.</div>`
      },
      {
        t: "Kiến trúc 3 mức ANSI/SPARC & Tính độc lập dữ liệu",
        c: `<p>Để giải quyết sự phụ thuộc giữa chương trình và dữ liệu, kiến trúc chuẩn ANSI/SPARC chia Hệ CSDL thành <b>3 mức trừu tượng</b>:</p>
            <ol>
              <li><b>Mức ngoài (External Level / View Level)</b>: Mô tả phần dữ liệu mà từng nhóm người dùng cụ thể được phép nhìn thấy (các Khung nhìn - View). Mỗi nhóm người dùng có một View riêng, che giấu các thông tin không liên quan hoặc nhạy cảm.</li>
              <li><b>Mức quan niệm (Conceptual Level / Logical Level)</b>: Mô tả cấu trúc <b>toàn bộ CSDL</b> dưới dạng các thực thể, mối liên kết, kiểu dữ liệu và ràng buộc toàn vẹn. Đây là góc nhìn toàn cục độc lập với công nghệ lưu trữ.</li>
              <li><b>Mức trong (Internal Level / Physical Level)</b>: Mô tả chi tiết cấu trúc lưu trữ vật lý của CSDL trên đĩa cứng (cách tổ chức file, chỉ mục B-tree, cấp phát khối đĩa, mã hóa, nén dữ liệu).</li>
            </ol>
            <div class="tip-box">
              <b>Hai mức Độc lập dữ liệu (Data Independence):</b><br>
              • <b>Độc lập vật lý (Physical Data Independence)</b>: Khả năng thay đổi lược đồ mức trong (ví dụ: tạo thêm chỉ mục Index, đổi thuật toán băm, chuyển sang ổ đĩa SSD) mà <i>hoàn toàn không cần sửa đổi lược đồ mức quan niệm</i>.<br>
              • <b>Độc lập logic (Logical Data Independence)</b>: Khả năng thay đổi lược đồ mức quan niệm (ví dụ: thêm một bảng mới, thêm một thuộc tính vào bảng) mà <i>không cần sửa đổi các lược đồ mức ngoài (View)</i> hoặc các chương trình ứng dụng đang chạy. Độc lập logic khó đạt được hơn độc lập vật lý!
            </div>`
      },
      {
        t: "Các nhóm người dùng và vai trò của DBA",
        c: `<p>Hệ CSDL phục vụ 4 nhóm người dùng chính:</p>
            <table class="data-table">
              <thead><tr><th>Nhóm người dùng</th><th>Vai trò & Trách nhiệm chính</th><th>Công cụ / Giao diện sử dụng</th></tr></thead>
              <tbody>
                <tr><td><b>Quản trị viên CSDL (DBA)</b></td><td>Chịu trách nhiệm cao nhất: Cấp quyền truy cập, giám sát hiệu năng, sao lưu (backup), phục hồi sau sự cố, điều chỉnh mức vật lý.</td><td>Lệnh đặc quyền hệ thống, DCL, hệ thống quản trị DBMS.</td></tr>
                <tr><td><b>Người thiết kế CSDL</b></td><td>Khảo sát nghiệp vụ, xác định dữ liệu, xây dựng lược đồ quan niệm (ERD) và lược đồ quan hệ chuẩn hóa.</td><td>Mô hình dữ liệu quan niệm và logic.</td></tr>
                <tr><td><b>Lập trình viên ứng dụng</b></td><td>Viết các phần mềm tương tác với CSDL qua các câu lệnh thao tác dữ liệu (DML, SQL nhúng).</td><td>Ngôn ngữ lập trình (Java, Python, C#) + SQL API.</td></tr>
                <tr><td><b>Người dùng cuối (End-users)</b></td><td>Người sử dụng phần mềm để truy vấn hoặc cập nhật dữ liệu hàng ngày (sinh viên xem điểm, nhân viên bán hàng).</td><td>Giao diện đồ họa (GUI, Web form).</td></tr>
              </tbody>
            </table>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide C1 — Slide 12–14] CSDL Quản lý Đào tạo Đại học",
        q: "Trong bài giảng Slide C1 (trang 12–14), xét CSDL Quản lý Đào tạo gồm các đối tượng: Sinh viên, Môn học, Học phần, Điểm số. Hãy phân biệt rõ: Thao tác nào thuộc Ngôn ngữ Định nghĩa Dữ liệu (DDL) và thao tác nào thuộc Ngôn ngữ Thao tác Dữ liệu (DML)?",
        sol: "<b>Phân tích đối chiếu theo Slide Chương 1:</b><br>" +
             "1. <b>DDL (Data Definition Language)</b>: Dùng để định nghĩa và thay đổi cấu trúc bảng, kiểu dữ liệu và ràng buộc toàn vẹn:<br>" +
             "   - Tạo bảng <code>SINHVIEN</code> với các cột <code>MaSV</code> (chuỗi 8 ký tự), <code>HoTen</code>, <code>NgaySinh</code>.<br>" +
             "   - Thiết lập ràng buộc <code>MaSV</code> làm khóa chính, điểm số phải nằm trong đoạn $[0, 10]$.<br>" +
             "2. <b>DML (Data Manipulation Language)</b>: Dùng để truy vấn, thêm, sửa, xóa dữ liệu tác nghiệp bên trong bảng:<br>" +
             "   - Thêm sinh viên mới Nguyễn Văn A vào bảng <code>SINHVIEN</code>.<br>" +
             "   - Cập nhật điểm thi môn CSDL của sinh viên có mã 23020001 thành 8.5.<br>" +
             "   - Truy vấn danh sách tất cả sinh viên có điểm trung bình tích lũy $\\\\ge 3.2$."
      },
      {
        level: "Trung bình",
        t: "[Slide C1 — Slide 40–43] Phân biệt Độc lập dữ liệu Vật lý vs Độc lập dữ liệu Logic",
        q: "Quản trị viên CSDL (DBA) thực hiện hai hành động sau:<br>" +
           "a) Tạo thêm một chỉ mục B-tree (Index) trên cột `NgaySinh` của bảng `NHANVIEN` để tăng tốc độ tìm kiếm nhân viên theo độ tuổi.<br>" +
           "b) Bổ sung thêm một cột `SoDienThoai` vào bảng `NHANVIEN`.<br>" +
           "Hai hành động trên minh họa cho mức độ độc lập dữ liệu nào? Các chương trình ứng dụng cũ có cần phải viết lại không?",
        sol: "<b>Phân tích theo Slide C1 (trang 42–43):</b><br>" +
             "a) Hành động tạo thêm Index trên đĩa cứng là thay đổi ở <b>mức trong (Lược đồ vật lý)</b>. Nhờ có <b>Độc lập dữ liệu vật lý (Physical Data Independence)</b>, lược đồ mức quan niệm và các chương trình ứng dụng hoàn toàn không bị ảnh hưởng, không cần sửa đổi bất kỳ dòng code nào.<br>" +
             "b) Hành động thêm cột <code>SoDienThoai</code> là thay đổi ở <b>mức quan niệm (Lược đồ logic)</b>. Nhờ có <b>Độc lập dữ liệu logic (Logical Data Independence)</b>, các khung nhìn (View) mức ngoài và các chương trình chỉ truy vấn các cột cũ (như MaNV, HoTen) vẫn hoạt động bình thường mà không cần viết lại."
      },
      {
        level: "Vận dụng",
        t: "[Slide C1 — Slide 28–29] Thiết kế Phân quyền Mức ngoài (Views) cho CSDL Bệnh viện",
        q: "Một bệnh viện triển khai CSDL tập trung lưu trữ hồ sơ bệnh án gồm: `MaBN`, `HoTen`, `NgaySinh`, `DiaChi`, `TienSuBenh`, `ChanDoanHienTai`, `ChiPhiDieuTri`, `BaoHiemChiTra`. Dựa trên kiến trúc mức ngoài (View Level), hãy thiết kế 2 khung nhìn (View) độc lập cho hai nhóm người dùng: (1) Bác sĩ điều trị và (2) Kế toán viện phí, giải thích lý do bảo mật.",
        sol: "<b>Phân tích thiết kế mức ngoài:</b><br>" +
             "1. <b>Khung nhìn dành cho Bác sĩ (View_BacSi)</b>:<br>" +
             "   - Thuộc tính được hiển thị: <code>MaBN</code>, <code>HoTen</code>, <code>NgaySinh</code>, <code>TienSuBenh</code>, <code>ChanDoanHienTai</code>.<br>" +
             "   - Lý do: Bác sĩ cần toàn bộ thông tin lâm sàng để ra quyết định điều trị, nhưng không cần và không được can thiệp vào viện phí.<br>" +
             "2. <b>Khung nhìn dành cho Kế toán (View_KeToan)</b>:<br>" +
             "   - Thuộc tính được hiển thị: <code>MaBN</code>, <code>HoTen</code>, <code>ChiPhiDieuTri</code>, <code>BaoHiemChiTra</code>.<br>" +
             "   - Lý do: Kế toán chỉ cần tính toán thanh toán viện phí, che giấu thông tin bệnh án nhạy cảm (<code>TienSuBenh</code>, <code>ChanDoanHienTai</code>) để bảo vệ quyền riêng tư người bệnh."
      }
    ],
    pitfalls: [
      {
        bad: "Nghĩ rằng Độc lập dữ liệu vật lý và Độc lập dữ liệu logic có độ phức tạp và khả năng đạt được như nhau.",
        good: "Độc lập dữ liệu logic khó đạt được hơn rất nhiều so với độc lập vật lý, vì việc thay đổi cấu trúc bảng/mối liên kết logic thường dễ ảnh hưởng đến các câu truy vấn phức tạp của ứng dụng."
      },
      {
        bad: "Nhầm lẫn DBA (Quản trị viên CSDL) là người chịu trách nhiệm viết mã nguồn các phần mềm ứng dụng.",
        good: "DBA chịu trách nhiệm quản lý hệ thống, phân quyền, sao lưu, phục hồi và tối ưu hiệu năng lưu trữ; người viết mã nguồn phần mềm là Lập trình viên ứng dụng (Application Programmer)."
      }
    ],
    quizzes: [
      {
        level: "Nhận biết",
        badge: "🟢 Cấp độ 1: Nhận biết",
        q: "Trong kiến trúc 3 mức ANSI/SPARC, mức nào mô tả cấu trúc lưu trữ vật lý thực tế của dữ liệu trên đĩa cứng?",
        opts: [
          "Mức ngoài (External level)",
          "Mức quan niệm (Conceptual level)",
          "Mức trong (Internal level)",
          "Mức logic người dùng"
        ],
        ans: 2,
        fb: "Chính xác! Mức trong (Internal level hay Physical level) mô tả chi tiết cách thức dữ liệu được lưu trữ vật lý trên thiết bị nhớ thứ cấp (cấu trúc tệp, chỉ mục, khối dữ liệu)."
      },
      {
        level: "Thông hiểu",
        badge: "🟡 Cấp độ 2: Thông hiểu",
        q: "Khả năng thay đổi cấu trúc lưu trữ vật lý (như tạo thêm chỉ mục B-tree để tăng tốc độ truy vấn) mà không làm ảnh hưởng đến lược đồ quan niệm được gọi là:",
        opts: [
          "Độc lập dữ liệu logic (Logical Data Independence)",
          "Độc lập dữ liệu vật lý (Physical Data Independence)",
          "Tính toàn vẹn thực thể (Entity Integrity)",
          "Tính nguyên tố của giao dịch (Atomicity)"
        ],
        ans: 1,
        fb: "Đúng! Độc lập dữ liệu vật lý đảm bảo mọi thay đổi về phương pháp lưu trữ, chỉ mục hoặc thiết bị phần cứng ở mức trong đều không ảnh hưởng tới lược đồ mức quan niệm."
      },
      {
        level: "Vận dụng",
        badge: "🔴 Cấp độ 3: Vận dụng & Bẫy",
        q: "Một ngân hàng muốn nâng cấp hệ thống: tách bảng `KHACHHANG(MaKH, HoTen, DiaChi, SoCMND)` thành hai bảng riêng biệt nhưng không muốn viết lại hàng trăm ứng dụng web/mobile hiện tại đang truy vấn từ bảng này. Ngân hàng cần áp dụng cơ chế nào của Hệ CSDL?",
        opts: [
          "Thay đổi mức trong và áp dụng độc lập dữ liệu vật lý",
          "Tạo một Khung nhìn (View) ở mức ngoài có tên `KHACHHANG` kết hợp dữ liệu hai bảng để bảo đảm Độc lập dữ liệu logic",
          "Xóa bỏ hoàn toàn ràng buộc khóa chính để tăng tính linh hoạt",
          "Bắt buộc phải dừng toàn bộ hệ thống và viết lại mã nguồn của tất cả ứng dụng"
        ],
        ans: 1,
        fb: "Rất xuất sắc! Nhờ cơ chế Khung nhìn (View) ở mức ngoài và tính Độc lập dữ liệu logic, ta có thể tái tạo lại giao diện bảng `KHACHHANG` cũ thông qua một câu lệnh JOIN giữa hai bảng mới, giúp tất cả các chương trình ứng dụng cũ chạy mượt mà mà không cần sửa code."
      }
    ]
  },

  {
    id: "CSDL_02",
    cluster: "1",
    title: "Mô hình Thực thể - Liên kết (ER): Thực thể & Thuộc tính",
    sources: "Slide UET.IS2099 Chương 2 (Slide 1–25)",
    ref: {
      slide_file: "C2_1.pptx",
      slide_name: "Chương 2 (Phần 1) — Mô hình Thực thể - Liên kết",
      pages: "Slide 1 – 25",
      page_start: 1,
      page_end: 25,
      section: "Mục 2.1: Quá trình thiết kế CSDL; Mục 2.2: Các khái niệm cơ bản (Thực thể, Thuộc tính, Khóa)",
      key_points: [
        "4 bước thiết kế CSDL: Phân tích yêu cầu -> Thiết kế quan niệm (ERD) -> Thiết kế logic (Mô hình quan hệ) -> Thiết kế vật lý",
        "Khái niệm Thực thể (Entity), Kiểu thực thể (Entity Type) và Tập thực thể (Entity Set)",
        "Phân loại thuộc tính: Đơn vs Tổng hợp (Composite), Đơn trị vs Đa trị (Multivalued), Lưu trữ vs Phái sinh (Derived)",
        "Thuộc tính khóa (Key Attribute): Nhận diện duy nhất mỗi thực thể, ký hiệu gạch chân trên sơ đồ ER"
      ],
      remind: "Khi làm bài tập vẽ lược đồ ER, nếu phân vân giữa thuộc tính đơn và thuộc tính tổng hợp (như Họ tên, Địa chỉ), hãy mở Slide C2_1 trang 12–16 để xem quy ước vẽ hình elip."
    },
    desc: "Làm chủ các khái niệm nền tảng của mô hình ER: thực thể, kiểu thực thể, các loại thuộc tính và cách biểu diễn chuẩn trên lược đồ.",
    steps: [
      {
        t: "Quy trình 4 giai đoạn thiết kế CSDL",
        c: `<p>Quá trình xây dựng một hệ CSDL chuyên nghiệp luôn trải qua 4 giai đoạn nối tiếp nhau:</p>
            <ol>
              <li><b>Thu thập & Phân tích yêu cầu</b>: Phỏng vấn người dùng, khảo sát tài liệu nghiệp vụ để nắm rõ nhu cầu dữ liệu và các luồng xử lý.</li>
              <li><b>Thiết kế mức quan niệm (Conceptual Design)</b>: Xây dựng <b>Lược đồ Thực thể - Liên kết (ERD)</b> ở mức trừu tượng cao, độc lập với bất kỳ phần mềm DBMS cụ thể nào.</li>
              <li><b>Thiết kế mức logic (Logical Design)</b>: Ánh xạ lược đồ ER sang mô hình dữ liệu cụ thể (chủ yếu là <b>Mô hình Quan hệ - Relational Model</b> gồm các bảng, khóa chính, khóa ngoại) và chuẩn hóa (Normalize) để loại trừ dư thừa.</li>
              <li><b>Thiết kế mức vật lý (Physical Design)</b>: Cài đặt các bảng trên một DBMS cụ thể (MySQL, PostgreSQL, Oracle), chỉ định kiểu dữ liệu bộ nhớ, tạo Index và thiết lập bảo mật.</li>
            </ol>`
      },
      {
        t: "Thực thể, Kiểu thực thể & Tập thực thể",
        c: `<p>Trong mô hình ER của Peter Chen:</p>
            <ul>
              <li><b>Thực thể (Entity)</b>: Là một đối tượng cụ thể trong thế giới thực có sự tồn tại độc lập (ví dụ: sinh viên Nguyễn Văn An có mã 23020001, đề án 'Chính phủ điện tử').</li>
              <li><b>Kiểu thực thể (Entity Type)</b>: Là tập hợp các thực thể có cùng tập thuộc tính đặc trưng (ví dụ: kiểu thực thể <code>SINHVIEN</code>, <code>DEAN</code>). Trên lược đồ ER, kiểu thực thể được vẽ bằng <b>Hình chữ nhật</b>.</li>
              <li><b>Tập thực thể (Entity Set)</b>: Tập hợp tất cả các thực thể của một kiểu thực thể tại một thời điểm cụ thể trong CSDL.</li>
            </ul>`
      },
      {
        t: "Phân loại 4 nhóm thuộc tính trong mô hình ER",
        c: `<p>Thuộc tính (Attribute) là các đặc trưng dùng để mô tả thực thể. Trên lược đồ ER, thuộc tính được vẽ bằng <b>Hình Elip</b> gắn với hình chữ nhật thực thể:</p>
            <table class="data-table">
              <thead><tr><th>Loại thuộc tính</th><th>Định nghĩa & Bản chất</th><th>Ký hiệu trên ERD</th><th>Ví dụ thực tế</th></tr></thead>
              <tbody>
                <tr><td><b>Thuộc tính Đơn (Simple)</b></td><td>Giá trị nguyên tử, không thể chia nhỏ hơn nữa.</td><td>Elip nét đơn bình thường.</td><td><code>GioiTinh</code>, <code>Luong</code>.</td></tr>
                <tr><td><b>Thuộc tính Tổng hợp (Composite)</b></td><td>Có thể chia nhỏ thành nhiều thành phần độc lập.</td><td>Elip phân nhánh thành các elip con.</td><td><code>HoTen</code> (Ho, Dem, Ten); <code>DiaChi</code> (SoNha, Duong, Quan, TP).</td></tr>
                <tr><td><b>Thuộc tính Đa trị (Multivalued)</b></td><td>Một thực thể có thể nhận nhiều giá trị cùng lúc.</td><td><b>Elip viền đôi (Double ellipse)</b>.</td><td><code>SoDienThoai</code> (1 người có nhiều số), <code>BangCap</code>.</td></tr>
                <tr><td><b>Thuộc tính Phái sinh (Derived)</b></td><td>Giá trị được tính toán từ các thuộc tính khác, không cần lưu trữ trực tiếp.</td><td><b>Elip nét đứt (Dashed ellipse)</b>.</td><td><code>Tuoi</code> (tính từ <code>NgaySinh</code>); <code>SoLuongNhanVien</code> (tính bằng COUNT).</td></tr>
                <tr><td><b>Thuộc tính Khóa (Key)</b></td><td>Giá trị phân biệt duy nhất từng thực thể trong tập thực thể.</td><td><b>Tên thuộc tính gạch chân</b> bên trong elip.</td><td><code><u>MaSV</u></code>, <code><u>SoCMND</u></code>.</td></tr>
              </tbody>
            </table>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide C2_1 — Slide 13–15] Phân loại Thuộc tính cho Thực thể Thí sinh Tuyển sinh",
        q: "Trong bài toán Quản lý Tuyển sinh (Slide C2_1 trang 13), kiểu thực thể `THISINH` gồm các thuộc tính: `SBD`, `HoTen` (Họ, Tên đệm, Tên), `NgaySinh`, `Tuoi`, `DienThoaiLienLac`. Hãy phân loại chính xác từng thuộc tính trên theo đúng chuẩn mô hình ER.",
        sol: "<b>Phân tích đối chiếu theo Slide C2_1:</b><br>" +
             "1. <code>SBD</code>: Giá trị phân biệt duy nhất mỗi thí sinh $\\rightarrow$ <b>Thuộc tính Khóa (Key Attribute)</b> (vẽ elip nét đơn, gạch chân chữ <u>SBD</u>).<br>" +
             "2. <code>HoTen</code>: Gồm 3 thành phần con (Họ, Đệm, Tên) $\\rightarrow$ <b>Thuộc tính Tổng hợp (Composite Attribute)</b>.<br>" +
             "3. <code>NgaySinh</code>: Giá trị nguyên tử lưu trữ trực tiếp $\\rightarrow$ <b>Thuộc tính Đơn lưu trữ (Simple Stored Attribute)</b>.<br>" +
             "4. <code>Tuoi</code>: Được tính toán trực tiếp từ $2026 - \\text{Năm sinh}$ $\\rightarrow$ <b>Thuộc tính Phái sinh (Derived Attribute)</b> (vẽ elip nét đứt).<br>" +
             "5. <code>DienThoaiLienLac</code>: Một thí sinh có thể đăng ký nhiều số liên lạc $\\rightarrow$ <b>Thuộc tính Đa trị (Multivalued Attribute)</b> (vẽ elip nét đôi)."
      },
      {
        level: "Trung bình",
        t: "[Slide C2_1 — Slide 10, 51] Mô hình hóa Thực thể Thư viện UET",
        q: "Khảo sát thư viện trường Đại học: 'Mỗi cuốn sách có một Mã sách duy nhất, Tên sách, Năm xuất bản, Danh sách các Tác giả và Số lượng bản sao hiện có trong kho'. Hãy thiết kế kiểu thực thể `SACH` và chỉ rõ ký hiệu hình vẽ ERD cho từng thuộc tính.",
        sol: "<b>Thiết kế kiểu thực thể SACH trên ERD:</b><br>" +
             "- Kiểu thực thể: <code>SACH</code> $\\rightarrow$ Vẽ hình chữ nhật ghi chữ SACH.<br>" +
             "- <code><u>MaSach</u></code> $\\rightarrow$ Hình elip nét đơn gạch chân (Thuộc tính khóa).<br>" +
             "- <code>TenSach</code>, <code>NamXuatBan</code> $\\rightarrow$ Hình elip nét đơn (Thuộc tính đơn).<br>" +
             "- <code>TacGia</code> $\\rightarrow$ <b>Hình elip nét đôi (Double ellipse)</b> vì một cuốn sách có thể do nhiều đồng tác giả cùng viết (Thuộc tính đa trị).<br>" +
             "- <code>SoLuongBanSao</code> $\\rightarrow$ Hình elip nét đứt (Thuộc tính phái sinh) nếu được tính bằng cách COUNT các bản sách vật lý hiện có trong kho."
      },
      {
        level: "Vận dụng",
        t: "[Slide C2_1 — Slide 52] Thiết kế Kiểu thực thể Bán hàng & Xử lý Thuộc tính phức hợp",
        q: "Trong CSDL Bán hàng của một công ty (Slide C2_1 trang 52): Khách hàng có `MaKH`, `TenCongTy`, `DiaChiGiaoHang` (gồm Số nhà, Tên đường, Quận, Thành phố), và có thể có nhiều `DiaChiEmail` để nhận hóa đơn điện tử. Hãy trình bày cách vẽ lược đồ ER chuẩn mực để không bị mất thông tin địa lý khi phân tích doanh số theo Quận/Thành phố.",
        sol: "<b>Phân tích thiết kế:</b><br>" +
             "- Nếu để <code>DiaChiGiaoHang</code> là một chuỗi văn bản đơn lẻ, sau này khi viết câu lệnh SQL để thống kê doanh số bán theo từng 'Quận' hoặc 'Thành phố' sẽ cực kỳ khó khăn và chạy rất chậm (phải dùng LIKE '%Quận Cầu Giấy%').<br>" +
             "- <b>Giải pháp chuẩn ER:</b> Mô hình hóa <code>DiaChiGiaoHang</code> thành <b>Thuộc tính Tổng hợp (Composite)</b>, phân nhánh ra 4 elip con: <code>SoNha</code>, <code>Duong</code>, <code>Quan</code>, <code>ThanhPho</code>.<br>" +
             "- Thuộc tính <code>DiaChiEmail</code> là <b>Thuộc tính Đa trị</b>, vẽ bằng elip viền đôi.<br>" +
             "- Thuộc tính <code><u>MaKH</u></code> là <b>Thuộc tính Khóa</b> gạch chân."
      }
    ],
    pitfalls: [
      {
        bad: "Lưu trữ thuộc tính Tuổi trực tiếp vào CSDL như một thuộc tính đơn thông thường.",
        good: "Tuổi thay đổi theo thời gian thực mỗi năm; lưu trực tiếp sẽ khiến dữ liệu nhanh chóng bị sai lệch. Chuẩn thiết kế là lưu NgaySinh (Stored) và tính Tuoi khi cần qua thuộc tính phái sinh (Derived)."
      },
      {
        bad: "Xem thuộc tính đa trị (như SoDienThoai, BangCap) như một thuộc tính đơn và lưu tất cả vào 1 ô ngăn cách bằng dấu phẩy.",
        good: "Điều này vi phạm dạng chuẩn 1 (1NF) sau này. Trên ERD bắt buộc phải đánh dấu bằng hình elip nét đôi để giai đoạn sau tách thành bảng quan hệ riêng."
      }
    ],
    quizzes: [
      {
        level: "Nhận biết",
        badge: "🟢 Cấp độ 1: Nhận biết",
        q: "Trên lược đồ Thực thể - Liên kết (ERD), kiểu thuộc tính Đa trị (Multivalued Attribute) được quy ước vẽ bằng hình gì?",
        opts: [
          "Hình thoi nét đơn",
          "Hình chữ nhật nét đôi",
          "Hình elip viền đôi (Double ellipse)",
          "Hình elip nét đứt"
        ],
        ans: 2,
        fb: "Chính xác! Thuộc tính đa trị (có thể nhận nhiều giá trị cho một thực thể) được ký hiệu bằng hình elip nét đôi."
      },
      {
        level: "Thông hiểu",
        badge: "🟡 Cấp độ 2: Thông hiểu",
        q: "Thuộc tính 'Thâm niên công tác' (số năm làm việc) của nhân viên được tính toán từ công thức `Năm hiện tại - NamVaoLam`. Thuộc tính này thuộc loại nào?",
        opts: [
          "Thuộc tính tổng hợp (Composite attribute)",
          "Thuộc tính phái sinh (Derived attribute), vẽ bằng elip nét đứt",
          "Thuộc tính đa trị (Multivalued attribute), vẽ bằng elip nét đôi",
          "Thuộc tính khóa (Key attribute), gạch chân"
        ],
        ans: 1,
        fb: "Đúng! Thuộc tính phái sinh không cần lưu trữ cứng trong bộ nhớ mà được suy diễn/tính toán từ các thuộc tính lưu trữ khác, vẽ bằng hình elip nét đứt."
      },
      {
        level: "Vận dụng",
        badge: "🔴 Cấp độ 3: Vận dụng & Bẫy",
        q: "Trong một dự án thiết kế CSDL Bệnh viện, một thực tập sinh đưa ra nhận định: 'Vì mỗi bệnh nhân có thể có nhiều người thân liên hệ khi cấp cứu, ta nên gộp Tên, Số điện thoại và Mối quan hệ của tất cả người thân vào một chuỗi văn bản dài trong thuộc tính NguoiThan'. Thiết kế này vi phạm nguyên tắc nào?",
        opts: [
          "Vi phạm tính độc lập vật lý của DBMS",
          "Vi phạm tính nguyên tử của thuộc tính (Atomic) và nhầm lẫn giữa thuộc tính đa trị/tổng hợp với thực thể yếu",
          "Vi phạm tiên đề Armstrong",
          "Vi phạm quy tắc đặt tên bảng"
        ],
        ans: 1,
        fb: "Chính xác! Gộp chuỗi làm mất cấu trúc dữ liệu, không thể tìm kiếm hay ràng buộc số điện thoại của người thân. Giải pháp chuẩn là tách 'Người thân' thành kiểu thực thể yếu (Weak entity) hoặc bảng liên kết riêng."
      }
    ]
  },

  {
    id: "CSDL_03",
    cluster: "1",
    title: "Mối liên kết, Ràng buộc tỉ số & Thực thể yếu",
    sources: "Slide UET.IS2099 Chương 2 (Slide 26–52)",
    ref: {
      slide_file: "C2_1.pptx",
      slide_name: "Chương 2 (Phần 1) — Mô hình Thực thể - Liên kết",
      pages: "Slide 26 – 52",
      page_start: 26,
      page_end: 52,
      section: "Mục 2.2.d: Kiểu liên kết; Mục 2.2.e: Ràng buộc tỉ số; Mục 2.2.h: Thực thể yếu",
      key_points: [
        "Khái niệm Kiểu liên kết (Relationship Type), vẽ bằng Hình thoi (Diamond)",
        "Bậc của liên kết: Nhị phân (Binary - phổ biến nhất), Tam phân (Ternary), Đệ quy (Recursive / Unary)",
        "Ràng buộc tỉ số lực lượng (Cardinality Ratio): 1:1, 1:N, M:N",
        "Ràng buộc tham gia (Participation Constraint): Toàn phần (Total - nét đôi) vs Một phần (Partial - nét đơn)",
        "Thực thể yếu (Weak Entity): Không có khóa riêng, phụ thuộc thực thể chủ, vẽ bằng Hình chữ nhật nét đôi, liên kết xác định nét đôi, khóa bộ phận gạch chân nét đứt"
      ],
      remind: "Thực thể yếu là một trong những câu hỏi tự luận kinh điển của UET. Hãy xem kỹ Slide C2_1 trang 33–35 về ví dụ NHANVIEN có THANNAN."
    },
    desc: "Nắm trọn các loại mối liên kết, phân biệt chính xác tỉ số lực lượng (1:1, 1:N, M:N), ràng buộc toàn phần và kỹ thuật mô hình hóa thực thể yếu.",
    steps: [
      {
        t: "Kiểu liên kết & Bậc của liên kết",
        c: `<p>Mối liên kết (Relationship) biểu diễn sự kết nối hoặc quan hệ ngữ nghĩa giữa hai hay nhiều thực thể:</p>
            <ul>
              <li>Trên sơ đồ ER, kiểu liên kết được vẽ bằng <b>Hình thoi (Diamond)</b>.</li>
              <li><b>Bậc của liên kết (Degree)</b>: Số lượng kiểu thực thể tham gia vào mối liên kết:
                <ul>
                  <li><b>Liên kết nhị phân (Binary - bậc 2)</b>: Phổ biến nhất (ví dụ: <code>NHANVIEN</code> <i>LàmViệcCho</i> <code>PHONGBAN</code>).</li>
                  <li><b>Liên kết đệ quy (Recursive / Unary - bậc 1)</b>: Một kiểu thực thể tự liên kết với chính nó (ví dụ: <code>NHANVIEN</code> <i>GiámSát</i> <code>NHANVIEN</code> khác).</li>
                  <li><b>Liên kết tam phân (Ternary - bậc 3)</b>: 3 kiểu thực thể cùng tham gia (ví dụ: <code>NHACUNGCAP</code> <i>CungCấp</i> <code>PHUTUNG</code> cho <code>DUAN</code>).</li>
                </ul>
              </li>
            </ul>`
      },
      {
        t: "Ràng buộc cấu trúc: Tỉ số lực lượng & Ràng buộc tham gia",
        c: `<p>Để xác định chính xác cấu trúc dữ liệu, mối liên kết nhị phân được khống chế bởi 2 ràng buộc:</p>
            <ol>
              <li><b>Tỉ số lực lượng (Cardinality Ratio)</b>: Số lượng tối đa thực thể bên này có thể liên kết với thực thể bên kia:
                <ul>
                  <li><b>1 : 1 (Một - Một)</b>: Ví dụ mỗi Trưởng phòng quản lý tối đa 1 Phòng ban, và mỗi Phòng ban chỉ có tối đa 1 Trưởng phòng.</li>
                  <li><b>1 : N (Một - Nhiều)</b>: Ví dụ một Phòng ban có nhiều Nhân viên, nhưng mỗi Nhân viên chỉ thuộc về 1 Phòng ban duy nhất.</li>
                  <li><b>M : N (Nhiều - Nhiều)</b>: Ví dụ một Sinh viên đăng ký nhiều Môn học, và một Môn học có nhiều Sinh viên theo học.</li>
                </ul>
              </li>
              <li><b>Ràng buộc tham gia (Participation Constraint)</b>:
                <ul>
                  <li><b>Tham gia Toàn phần (Total Participation / Khắc khe)</b>: Mọi thực thể trong tập đều <i>bắt buộc</i> phải tham gia vào liên kết. Vẽ bằng <b>Đường nối nét đôi (Double line)</b>. (Ví dụ: Mọi Nhân viên bắt buộc phải thuộc một Phòng ban).</li>
                  <li><b>Tham gia Một phần (Partial Participation / Tùy chọn)</b>: Có thể có thực thể không tham gia. Vẽ bằng <b>Đường nối nét đơn (Single line)</b>. (Ví dụ: Không phải Nhân viên nào cũng là Trưởng phòng).</li>
                </ul>
              </li>
            </ol>`
      },
      {
        t: "Thực thể yếu (Weak Entity) & Liên kết xác định",
        c: `<p><b>Thực thể yếu</b> là kiểu thực thể không có đủ thuộc tính để tạo thành một khóa chính riêng biệt:</p>
            <ul>
              <li>Thực thể yếu <b>bắt buộc phải phụ thuộc sự tồn tại</b> vào một kiểu thực thể khác gọi là <b>Thực thể chủ (Owner / Identifying Entity)</b>.</li>
              <li>Mối liên kết giữa thực thể yếu và thực thể chủ gọi là <b>Liên kết xác định (Identifying Relationship)</b>, vẽ bằng <b>Hình thoi viền đôi</b>.</li>
              <li>Bản thân thực thể yếu được vẽ bằng <b>Hình chữ nhật viền đôi</b>.</li>
              <li>Thực thể yếu chỉ có một <b>Khóa bộ phận (Partial Key / Discriminator)</b> dùng để phân biệt các thực thể yếu thuộc cùng một thực thể chủ. Khóa bộ phận được vẽ bằng <b>Gạch chân nét đứt (Dashed underline)</b> bên trong elip.</li>
            </ul>
            <div class="tip-box">
              <b>Ví dụ kinh điển UET (Slide C2_1 tr. 34–35):</b><br>
              <code>NHANVIEN</code> (Thực thể chủ, khóa <code><u>MaNV</u></code>) có mối liên kết xác định <i>Có_ThânNhân</i> (Hình thoi đôi) với <code>THANNHAN</code> (Thực thể yếu, chữ nhật đôi).<br>
              <code>THANNHAN</code> chỉ có thuộc tính <code><u>TenThanNhan</u></code> (gạch chân nét đứt) và <code>MoiQuanHe</code>. Nếu không biết <code>MaNV</code>, ta không thể phân biệt người thân tên 'An' là của nhân viên nào!
            </div>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide C2_1 — Slide 26] Ràng buộc Tỉ số trong CSDL Thư viện",
        q: "Trong bài toán CSDL Thư viện (Slide C2_1 trang 26), xét mối liên kết `Muon` giữa hai kiểu thực thể `BANDOC` (Bạn đọc) và `CUONSACH` (Cuốn sách vật lý có Mã vạch duy nhất). Hãy xác định tỉ số lực lượng (1:1, 1:N hay M:N) nếu: (1) Xét giữa Bạn đọc và Đầu sách; (2) Xét giữa Bạn đọc và Cuốn sách cụ thể tại một thời điểm.",
        sol: "<b>Phân tích bản chất theo bài giảng UET:</b><br>" +
             "1. Xét giữa <code>BANDOC</code> và <code>DAUSACH</code> (Tác phẩm): Một bạn đọc có thể mượn nhiều đầu sách khác nhau theo thời gian, và một đầu sách được nhiều bạn đọc mượn $\\rightarrow$ Tỉ số là <b>M : N (Nhiều - Nhiều)</b>.<br>" +
             "2. Xét giữa <code>BANDOC</code> và <code>CUONSACH</code> (Bản sao vật lý cụ thể) tại một thời điểm: Một bạn đọc có thể mượn cùng lúc nhiều cuốn sách, nhưng một cuốn sách cụ thể (có mã vạch xác định) tại một thời điểm chỉ có thể do <b>tối đa một bạn đọc</b> cầm giữ $\\rightarrow$ Tỉ số là <b>1 : N (Một - Nhiều)</b> phía Bạn đọc là 1, Cuốn sách là N."
      },
      {
        level: "Trung bình",
        t: "[Slide C2_1 — Slide 34–35] Mô hình hóa Thực thể yếu Thân nhân của Nhân viên",
        q: "Một công ty cần quản lý thông tin thân nhân của nhân viên để chi trả bảo hiểm: Mỗi nhân viên có `MaNV` (duy nhất), `HoTen`. Thân nhân có `TenThanNhan`, `NgaySinh`, `QuanHe`. Hai nhân viên khác nhau có thể có thân nhân trùng tên (ví dụ đều có con tên 'Bình'). Hãy vẽ và mô tả chi tiết các thành phần ERD để biểu diễn mối quan hệ này.",
        sol: "<b>Mô hình hóa chi tiết theo chuẩn UET:</b><br>" +
             "1. Kiểu thực thể chủ: <code>NHANVIEN</code> (vẽ hình chữ nhật nét đơn, khóa chính <code><u>MaNV</u></code> gạch chân nét liền).<br>" +
             "2. Kiểu thực thể yếu: <code>THANNHAN</code> (vẽ <b>hình chữ nhật viền đôi</b>).<br>" +
             "3. Khóa bộ phận của thân nhân: <code><u>TenThanNhan</u></code> (vẽ hình elip, chữ được <b>gạch chân bằng nét đứt</b>).<br>" +
             "4. Mối liên kết xác định: <code>Co_ThanNhan</code> (vẽ <b>hình thoi viền đôi</b>).<br>" +
             "5. Ràng buộc tham gia: Phía <code>THANNHAN</code> bắt buộc phải nối bằng <b>đường nét đôi (Total participation)</b> vì không thể tồn tại một thân nhân trong CSDL mà không gắn với nhân viên nào."
      },
      {
        level: "Vận dụng",
        t: "[Slide C2_1 — Slide 52] Thiết kế Lược đồ ER Hoàn chỉnh cho CSDL Bán hàng",
        q: "Bài tập 4 (Slide C2_1 trang 52): Thiết kế lược đồ ER cho CSDL Bán hàng của một công ty gồm: Khách hàng, Đơn đặt hàng, Hàng hóa. Biết rằng:<br>" +
           "- Mỗi Đơn đặt hàng do đúng một Khách hàng đặt, một Khách hàng có thể đặt nhiều đơn.<br>" +
           "- Mỗi Đơn đặt hàng có thể gồm nhiều Mặt hàng với số lượng và đơn giá bán tương ứng; mỗi Mặt hàng có thể xuất hiện trong nhiều đơn hàng.<br>" +
           "Hãy xác định các kiểu thực thể, mối liên kết, tỉ số lực lượng và vị trí đặt thuộc tính `SoLuong`, `DonGiaBan`.",
        sol: "<b>Phân tích thiết kế chuẩn xác:</b><br>" +
             "1. Các kiểu thực thể: <code>KHACHHANG</code> (<u>MaKH</u>, TenKH, DiaChi), <code>DONDATHANG</code> (<u>SoDH</u>, NgayDat), <code>HANGHOA</code> (<u>MaHang</u>, TenHang, DonViTinh).<br>" +
             "2. Liên kết <code>DatHang</code> giữa <code>KHACHHANG</code> và <code>DONDATHANG</code>:<br>" +
             "   - Tỉ số: <b>1 : N</b> (1 Khách hàng đặt N Đơn hàng). Phía <code>DONDATHANG</code> tham gia toàn phần (đường nét đôi) vì đơn hàng bắt buộc phải có người đặt.<br>" +
             "3. Liên kết <code>ChiTietDonHang</code> giữa <code>DONDATHANG</code> và <code>HANGHOA</code>:<br>" +
             "   - Tỉ số: <b>M : N</b> (1 Đơn hàng có nhiều Hàng hóa, 1 Hàng hóa nằm trong nhiều Đơn hàng).<br>" +
             "   - <b>Cạm bẫy vị trí thuộc tính:</b> Thuộc tính <code>SoLuong</code> và <code>DonGiaBan</code> <b>KHÔNG THỂ</b> đặt ở thực thể Hàng hóa (vì mỗi đơn hàng mua số lượng khác nhau) cũng không thể đặt ở Đơn đặt hàng (vì mỗi món trong đơn có số lượng khác nhau). Chúng bắt buộc phải là <b>Thuộc tính của mối liên kết M:N ChiTietDonHang</b>!"
      }
    ],
    pitfalls: [
      {
        bad: "Đặt thuộc tính số lượng mua (SoLuong) vào kiểu thực thể Hàng hóa hoặc Khách hàng trong mối liên kết M:N.",
        good: "Trong mối liên kết nhiều - nhiều (M:N), các thuộc tính phát sinh từ sự tương tác giữa hai thực thể (như Số lượng mua, Điểm thi của sinh viên học môn học) bắt buộc phải gắn trực tiếp vào Hình thoi liên kết M:N."
      },
      {
        bad: "Quên vẽ viền đôi cho kiểu thực thể yếu và liên kết xác định, hoặc gạch chân nét liền cho khóa bộ phận.",
        good: "Thực thể yếu phải có 3 đặc điểm nhận diện bắt buộc trên ERD: Hình chữ nhật đôi, Hình thoi đôi và Khóa bộ phận gạch chân nét đứt."
      }
    ],
    quizzes: [
      {
        level: "Nhận biết",
        badge: "🟢 Cấp độ 1: Nhận biết",
        q: "Trên sơ đồ ER, một đường nối nét đôi (Double line) giữa một kiểu thực thể và một kiểu liên kết thể hiện điều gì?",
        opts: [
          "Ràng buộc tỉ số là 1 : 1",
          "Ràng buộc tham gia toàn phần (Total participation - mọi thực thể bắt buộc phải tham gia liên kết)",
          "Thực thể đó là thực thể yếu",
          "Thuộc tính của liên kết là đa trị"
        ],
        ans: 1,
        fb: "Chính xác! Đường nối đôi biểu diễn sự tham gia toàn phần (Total / Mandatory participation), nghĩa là mọi cá thể thực thể đều bắt buộc phải tồn tại trong mối liên kết đó."
      },
      {
        level: "Thông hiểu",
        badge: "🟡 Cấp độ 2: Thông hiểu",
        q: "Trong mối quan hệ giữa `LOPHOC` và `PHONGHOC` tại một tiết học: 'Mỗi lớp học tại một tiết học chỉ được xếp vào tối đa 1 phòng học, và mỗi phòng học tại tiết đó chỉ chứa tối đa 1 lớp học'. Tỉ số lực lượng của liên kết này là:",
        opts: [
          "1 : 1",
          "1 : N",
          "M : N",
          "Không xác định được"
        ],
        ans: 0,
        fb: "Đúng! Tại một thời điểm cố định, 1 phòng học phục vụ 1 lớp học và 1 lớp học chỉ ở trong 1 phòng học, đây là quan hệ 1 : 1."
      },
      {
        level: "Vận dụng",
        badge: "🔴 Cấp độ 3: Vận dụng & Bẫy",
        q: "Xét bài toán Quản lý Đào tạo: Sinh viên đăng ký học các môn học. Thuộc tính `DiemThi` (Điểm tổng kết môn) phải được đặt ở vị trí nào trên sơ đồ ER?",
        opts: [
          "Đặt trong kiểu thực thể `SINHVIEN`",
          "Đặt trong kiểu thực thể `MONHOC`",
          "Đặt gắn trực tiếp vào mối liên kết M:N `DangKyHoc` giữa `SINHVIEN` và `MONHOC`",
          "Tạo thành một thực thể độc lập tên là `DIEMTHI`"
        ],
        ans: 2,
        fb: "Rất chuẩn! Một sinh viên có nhiều điểm thi (cho các môn khác nhau), và một môn học có nhiều điểm thi (của các sinh viên khác nhau). Do đó `DiemThi` là thuộc tính của mối liên kết M:N giữa Sinh viên và Môn học."
      }
    ]
  },

  {
    id: "CSDL_04",
    cluster: "1",
    title: "Mô hình ER mở rộng (EER): Chuyên biệt hóa & Khái quát hóa",
    sources: "Slide UET.IS2099 Chương 2 Phần 2 (Slide 1–26)",
    ref: {
      slide_file: "C2_2.pptx",
      slide_name: "Chương 2 (Phần 2) — Mô hình Thực thể - Liên kết Mở rộng (EER)",
      pages: "Slide 1 – 26",
      page_start: 1,
      page_end: 26,
      section: "Mục 2.3: Lớp cha / Lớp con; Chuyên biệt hóa & Khái quát hóa; Ràng buộc rời rạc & Ràng buộc đầy đủ",
      key_points: [
        "Khái niệm Lớp cha (Superclass) và Lớp con (Subclass), quan hệ IS-A (Là-Một)",
        "Tính kế thừa kiểu (Type Inheritance): Lớp con thừa kế tất cả thuộc tính và mối liên kết của lớp cha",
        "Chuyên biệt hóa (Specialization - top-down) vs Khái quát hóa (Generalization - bottom-up)",
        "Ràng buộc Rời rạc (Disjointness constraint): Rời rạc (d) vs Chồng chéo (o)",
        "Ràng buộc Đầy đủ (Completeness constraint): Toàn bộ (Total - nét đôi) vs Một phần (Partial - nét đơn)",
        "4 tổ hợp kinh điển: {d, total}, {d, partial}, {o, total}, {o, partial}"
      ],
      remind: "Ràng buộc {d/o} và {total/partial} trong EER luôn xuất hiện trong câu hỏi trắc nghiệm lý thuyết UET. Mở Slide C2_2 trang 12–18 để xem sơ đồ phân biệt."
    },
    desc: "Làm chủ mô hình EER: kế thừa thuộc tính, chuyên biệt hóa, khái quát hóa và 4 tổ hợp ràng buộc cấu trúc phân cấp lớp cha/lớp con.",
    steps: [
      {
        t: "Tại sao cần Mô hình ER Mở rộng (EER)?",
        c: `<p>Mô hình ER truyền thống gặp hạn chế khi cần mô hình hóa các hệ thống có tính kế thừa phức tạp:</p>
            <ul>
              <li>Ví dụ thực tế trong trường đại học: Ta có kiểu thực thể <code>NGUOI</code>, nhưng trong trường có các nhóm đối tượng riêng: <code>GIANGVIEN</code> (có học hàm, học vị, lương), <code>SINHVIEN</code> (có điểm trung bình GPA, lớp niên chế).</li>
              <li>Nếu gộp chung vào 1 thực thể, các thuộc tính riêng sẽ bị NULL rất nhiều (sinh viên không có học hàm). Nếu tách rời thành 2 thực thể độc lập, ta bị lặp lại các thuộc tính chung (Họ tên, Ngày sinh, CCCD).</li>
              <li><b>Mô hình EER (Enhanced ER)</b> bổ sung các khái niệm hướng đối tượng: <b>Lớp cha (Superclass)</b>, <b>Lớp con (Subclass)</b> và <b>Tính kế thừa (Inheritance)</b> để giải quyết triệt để vấn đề này.</li>
            </ul>`
      },
      {
        t: "Chuyên biệt hóa vs Khái quát hóa & Tính kế thừa",
        c: `<p>Hai quá trình thiết kế đối ngẫu nhau:</p>
            <ul>
              <li><b>Chuyên biệt hóa (Specialization - Tiếp cận Top-down)</b>: Quá trình phân rã một lớp cha thành các lớp con cụ thể dựa trên các đặc trưng riêng biệt (ví dụ: từ <code>NHANVIEN</code> phân rã thành <code>NhanVienCoHuu</code> hưởng lương tháng và <code>NhanVienHopDong</code> hưởng lương theo giờ).</li>
              <li><b>Khái quát hóa (Generalization - Tiếp cận Bottom-up)</b>: Quá trình tổng hợp nhiều lớp thực thể có chung thuộc tính để tạo thành một lớp cha tổng quát (ví dụ: từ <code>XE_HOI</code> và <code>XE_TAI</code> tổng quát hóa thành <code>PHUONGTIEN</code>).</li>
              <li><b>Quy tắc kế thừa (Inheritance)</b>: Một thực thể là thành viên của lớp con sẽ <i>tự động thừa kế toàn bộ thuộc tính và tất cả các mối liên kết</i> của lớp cha, đồng thời sở hữu thêm các thuộc tính và liên kết chuyên biệt của riêng nó.</li>
            </ul>`
      },
      {
        t: "Các ràng buộc trên Chuyên biệt hóa / Khái quát hóa",
        c: `<p>Một cấu trúc phân cấp lớp cha / lớp con trong EER được khống chế bởi 2 cặp ràng buộc độc lập:</p>
            <table class="data-table">
              <thead><tr><th>Loại ràng buộc</th><th>Hai trạng thái lựa chọn</th><th>Ý nghĩa & Biểu diễn trên EERD</th></tr></thead>
              <tbody>
                <tr><td rowspan="2"><b>Ràng buộc Rời rạc (Disjointness)</b></td><td><b>Rời rạc (Disjoint - ký hiệu chữ d)</b></td><td>Một thực thể ở lớp cha chỉ được phép là thành viên của <b>tối đa một</b> lớp con (các lớp con không giao nhau).</td></tr>
                <tr><td><b>Chồng chéo (Overlap - ký hiệu chữ o)</b></td><td>Một thực thể ở lớp cha có thể đồng thời là thành viên của <b>nhiều</b> lớp con khác nhau.</td></tr>
                <tr><td rowspan="2"><b>Ràng buộc Đầy đủ (Completeness)</b></td><td><b>Toàn bộ (Total Specialization)</b></td><td>Mọi thực thể ở lớp cha <b>bắt buộc phải thuộc về ít nhất một</b> lớp con. Vẽ bằng <b>đường nét đôi (Double line)</b> nối lớp cha với hình tròn.</td></tr>
                <tr><td><b>Một phần (Partial Specialization)</b></td><td>Có thể có thực thể ở lớp cha <b>không thuộc về bất kỳ lớp con nào</b>. Vẽ bằng <b>đường nét đơn (Single line)</b>.</td></tr>
              </tbody>
            </table>
            <div class="tip-box">
              <b>4 Tổ hợp ràng buộc:</b><br>
              1. <code>{d, total}</code>: Thuộc đúng 1 lớp con duy nhất.<br>
              2. <code>{d, partial}</code>: Thuộc tối đa 1 lớp con, hoặc không thuộc lớp con nào.<br>
              3. <code>{o, total}</code>: Thuộc ít nhất 1 lớp con (có thể thuộc nhiều lớp con).<br>
              4. <code>{o, partial}</code>: Có thể thuộc 0, 1 hoặc nhiều lớp con tùy ý.
            </div>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide C2_2 — Slide 4–6] Tính Kế thừa trong Thực thể Sinh viên và Nhân viên",
        q: "Xét lược đồ EER (Slide C2_2 trang 4–6): Lớp cha `NGUOI` có các thuộc tính `CCCD`, `HoTen`, `NgaySinh`. Hai lớp con là `SINHVIEN` (có thuộc tính riêng `GPA`) và `GIANGVIEN` (có thuộc tính riêng `HocHam`). Hãy liệt kê đầy đủ các thuộc tính của một giảng viên trong hệ thống.",
        sol: "<b>Phân tích tính kế thừa kiểu (Type Inheritance):</b><br>" +
             "Theo quy tắc kế thừa trong EER, một thực thể thuộc lớp con <code>GIANGVIEN</code> kế thừa toàn bộ thuộc tính của lớp cha <code>NGUOI</code> cộng với thuộc tính riêng của nó:<br>" +
             "$$\\\\text{Thuộc tính của GIANGVIEN} = \\\\{ \\\\underline{CCCD}, HoTen, NgaySinh, HocHam \\\\}$$"
      },
      {
        level: "Trung bình",
        t: "[Slide C2_2 — Slide 12–17] Xác định Ràng buộc {d, total} cho Phương tiện Giao thông",
        q: "Trong bài toán Quản lý Đăng kiểm Xe (Slide C2_2 trang 17): Lớp cha `XE` chuyên biệt hóa thành hai lớp con: `XE_XANG` (chạy động cơ xăng) và `XE_DIEN` (chạy động cơ điện thuần túy). Giả sử hệ thống quy định mỗi chiếc xe bắt buộc phải thuộc một trong hai loại trên và không có xe lai (hybrid). Hãy xác định cặp ràng buộc (Disjointness và Completeness) và cách vẽ trên EERD.",
        sol: "<b>Phân tích xác định ràng buộc:</b><br>" +
             "1. Một chiếc xe không thể vừa là xe xăng vừa là xe điện thuần túy $\\rightarrow$ Rời rạc hoàn toàn $\\rightarrow$ Ký hiệu chữ <b>d (Disjoint)</b> trong hình tròn.<br>" +
             "2. Mọi chiếc xe trong hệ thống bắt buộc phải thuộc một trong hai loại trên (không có ngoại lệ) $\\rightarrow$ Chuyên biệt hóa toàn bộ $\\rightarrow$ <b>Total completeness</b>.<br>" +
             "3. Cách vẽ trên EERD: Nối lớp cha <code>XE</code> tới hình tròn chứa chữ <b>d</b> bằng <b>đường nét đôi (Double line)</b>."
      },
      {
        level: "Vận dụng",
        t: "[Slide C2_2 — Slide 21–22] Mô hình hóa Trường Đại học với Ràng buộc Chồng chéo {o, partial}",
        q: "Tại trường Đại học UET: Mỗi người có thông tin chung trong `NGUOI`. Một người có thể là `SINHVIEN`, có thể là `NHANVIEN` của trường (ví dụ sinh viên vừa học vừa làm trợ giảng/nhân viên lab), hoặc có thể chỉ là khách vãng lai đến thư viện đọc sách mà không phải sinh viên hay nhân viên trường. Hãy xác định tổ hợp ràng buộc chính xác cho mô hình này.",
        sol: "<b>Phân tích thiết kế:</b><br>" +
             "1. Một người có thể đồng thời vừa là <code>SINHVIEN</code> vừa là <code>NHANVIEN</code> $\\rightarrow$ Các lớp con không loại trừ nhau $\\rightarrow$ Ràng buộc <b>Chồng chéo (Overlap - ký hiệu chữ o)</b>.<br>" +
             "2. Tồn tại khách vãng lai chỉ thuộc lớp cha <code>NGUOI</code> mà không thuộc lớp con nào $\\rightarrow$ Chuyên biệt hóa một phần $\\rightarrow$ <b>Partial completeness</b> (vẽ đường nét đơn từ <code>NGUOI</code> tới hình tròn).<br>" +
             "3. Tổ hợp chuẩn xác: <b>{o, partial}</b> (Chồng chéo - Một phần)."
      }
    ],
    pitfalls: [
      {
        bad: "Nhầm lẫn giữa Disjoint (d) và Total: Cho rằng hễ đã rời rạc thì bắt buộc phải là toàn phần.",
        good: "Disjoint (d) và Total là 2 trục ràng buộc hoàn toàn độc lập: Disjoint quy định số lớp con tối đa một thực thể có thể tham gia (<= 1), còn Total quy định số lớp con tối thiểu (>= 1)."
      },
      {
        bad: "Quên không gán khóa chính của lớp cha cho các lớp con khi chuyển đổi sang mô hình quan hệ.",
        good: "Lớp con trong EER không cần khai báo lại thuộc tính khóa riêng trên sơ đồ; nó tự động thừa kế khóa chính từ lớp cha."
      }
    ],
    quizzes: [
      {
        level: "Nhận biết",
        badge: "🟢 Cấp độ 1: Nhận biết",
        q: "Trong mô hình EER, ký hiệu chữ 'd' bên trong hình tròn biểu diễn cho ràng buộc nào?",
        opts: [
          "Ràng buộc dẫn xuất (Derived)",
          "Ràng buộc rời rạc (Disjoint - các lớp con tách biệt hoàn toàn, không giao nhau)",
          "Ràng buộc miền giá trị (Domain)",
          "Ràng buộc phụ thuộc dữ liệu"
        ],
        ans: 1,
        fb: "Chính xác! Chữ 'd' là viết tắt của Disjoint (Rời rạc), quy định một thực thể ở lớp cha chỉ được phép là thành viên của tối đa 1 lớp con."
      },
      {
        level: "Thông hiểu",
        badge: "🟡 Cấp độ 2: Thông hiểu",
        q: "Một nhân viên trong công ty có thể đồng thời là 'Kỹ sư phần mềm' và 'Trưởng nhóm dự án'. Chuyên biệt hóa này có đặc tính gì?",
        opts: [
          "Ràng buộc rời rạc (Disjoint - d)",
          "Ràng buộc chồng chéo (Overlap - o)",
          "Ràng buộc đơn trị",
          "Ràng buộc phân cấp nghiêm ngặt"
        ],
        ans: 1,
        fb: "Đúng! Khi một thực thể có thể đồng thời thuộc về nhiều lớp con khác nhau thì đó là ràng buộc Chồng chéo (Overlap - ký hiệu chữ o)."
      },
      {
        level: "Vận dụng",
        badge: "🔴 Cấp độ 3: Vận dụng & Bẫy",
        q: "Lược đồ EER có lớp cha `TAIKHOAN` và hai lớp con `TIETKIEM`, `THANHTOAN`. Biết rằng: Mỗi tài khoản trong ngân hàng bắt buộc phải là tài khoản tiết kiệm hoặc tài khoản thanh toán, và không có tài khoản nào thuộc cả hai loại. Tổ hợp ràng buộc chuẩn mực là:",
        opts: [
          "{o, partial}",
          "{o, total}",
          "{d, partial}",
          "{d, total}"
        ],
        ans: 3,
        fb: "Xuất sắc! Bắt buộc phải thuộc một loại => Total (nét đôi); Không thể thuộc cả hai loại => Disjoint (chữ d). Do đó tổ hợp là {d, total}."
      }
    ]
  }
];

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { CUM_1_CSDL };
}
"""

with open('content_csdl/cum_1.js', 'w', encoding='utf-8') as f:
    f.write(cum_1_code)

print("Created content_csdl/cum_1.js successfully! Length:", len(cum_1_code))
