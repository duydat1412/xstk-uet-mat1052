// ==========================================================================
// CỤM A: DỮ LIỆU VÀ THỐNG KÊ MÔ TẢ
// Bao gồm: Bài A1, A2, A3, A4, A5
// Nguồn: Slide UET Week 01 - 04, Stat20 Chương 1, Chương 2, Mục 7.2
// Kiểm chứng số học: verify/verify_cum_a.py
// ==========================================================================

const CUM_A = [
  {
    id: "A1",
    cluster: "A",
    title: "Khung dữ liệu và Các loại biến",
    sources: "Slide Week 01 (tr. 1–75); Stat20 Mục 1.1, 1.2, 1.3",
    ref: {
      "slide_file": "week01.pdf",
      "slide_name": "Tuần 01 — Dữ liệu và Thu thập",
      "pages": "Slide 23 – 50",
      "page_start": 23,
      "section": "Phần 2: Từ đối tượng đến biến (Slide 23–30) & Phần 3: Từ biến đến khung dữ liệu (Slide 31–50)",
      "stat20": "Stat20 Mục 1.1, 1.2, 1.3 (Data Frames & Variable Types)",
      "key_points": [
            "Đơn vị quan sát (Observation) ở mỗi hàng và Biến số (Variable) ở mỗi cột",
            "Phân loại 4 họ biến: Định danh (Nominal), Thứ bậc (Ordinal), Rời rạc (Discrete), Liên tục (Continuous)",
            "Cạm bẫy mã số: MSSV, SĐT, Mã chuyến bay là biến phân loại định danh, không phải biến số"
      ],
      "remind": "Nếu bạn chưa phân biệt được biến định danh vs thứ bậc, hoặc hay nhầm mã số là biến số, hãy mở lại Slide Week 01 từ trang 23 đến 45 để xem các ví dụ trực quan về bảng Palmer Penguins và phim Marvel."
},
    desc: "Nắm vững cách cấu trúc dữ liệu dưới dạng bảng và phân loại chính xác 4 họ biến: Định danh, Thứ bậc, Rời rạc, Liên tục. Không bao giờ mắc bẫy mã số.",
    steps: [
      {
        t: "Cấu trúc dữ liệu: Khung dữ liệu (Data Frame)",
        c: `<p>Trong thống kê và khoa học dữ liệu, dữ liệu luôn được tổ chức dưới dạng một bảng chữ nhật gọi là <b>Khung dữ liệu (Data Frame)</b>:</p>
            <ul>
              <li><b>Mỗi hàng (Row)</b>: Đại diện cho một <b>đơn vị quan sát</b> (Observation) — ví dụ: một sinh viên, một bệnh nhân, một chuyến bay.</li>
              <li><b>Mỗi cột (Column)</b>: Đại diện cho một <b>biến số</b> (Variable) — đặc tính đo lường được của đối tượng (ví dụ: Chiều cao, Điểm GPA, Ngành học).</li>
            </ul>
            <div class="tip-box"><b>Quy tắc vàng:</b> Trước khi tính toán bất kỳ chỉ số nào, bạn phải biết rõ đơn vị quan sát ở mỗi hàng là gì và cột bạn đang xét thuộc loại biến nào!</div>`
      },
      {
        t: "Hai họ biến lớn: Phân loại vs Biến số",
        c: `<p>Mọi biến số trên đời đều thuộc một trong hai họ lớn:</p>
            <ol>
              <li><b>Biến phân loại (Categorical variable)</b>: Giá trị là một từ ngữ, một nhãn hoặc một nhóm phân loại (ví dụ: Giới tính, Quê quán, Nhóm máu).</li>
              <li><b>Biến số (Numerical variable)</b>: Giá trị là một con số đo lường hoặc đếm được, và việc làm các phép tính số học (cộng, trừ, tính trung bình) với nó <b>có ý nghĩa thực tế</b>.</li>
            </ol>
            <div class="warn-box">
              <b>⚠️ CẠM BẪY CHÍ MẠNG: Mã số không phải là biến số!</b><br>
              Mã số sinh viên (23020123), Số điện thoại (0912345678), Mã bưu chính, Mã chuyến bay (VN215) tuy được viết bằng các chữ số, nhưng chúng thực chất chỉ là <b>nhãn định danh</b> dùng để phân biệt các đối tượng. Việc lấy trung bình cộng hai mã số sinh viên là hoàn toàn vô nghĩa! Vì vậy, chúng thuộc họ <b>Biến phân loại</b>.
            </div>`
      },
      {
        t: "Chia nhỏ thành 4 loại biến cụ thể",
        c: `<p>Để quyết định phương pháp tóm tắt dữ liệu phù hợp, ta chia sâu thêm một cấp:</p>
            <table class="data-table">
              <thead><tr><th>Họ lớn</th><th>Loại biến</th><th>Đặc điểm nhận diện</th><th>Ví dụ thực tế</th></tr></thead>
              <tbody>
                <tr><td rowspan="2"><b>Phân loại</b></td><td><b>Định danh (Nominal)</b></td><td>Các nhóm không có thứ tự hơn kém, chỉ dùng để gọi tên.</td><td>Khoa (CNTT, Cơ học), Nhóm máu (A, B, O), Tình trạng hôn nhân.</td></tr>
                <tr><td><b>Thứ bậc (Ordinal)</b></td><td>Các nhóm có quan hệ thứ tự tự nhiên (hơn/kém, cao/thấp).</td><td>Học lực (Kém &lt; Khá &lt; Giỏi), Đánh giá sao (1 sao &lt; 5 sao), Cỡ áo (S, M, L).</td></tr>
                <tr><td rowspan="2"><b>Biến số</b></td><td><b>Rời rạc (Discrete)</b></td><td>Giá trị là các con số tách rời (thường là kết quả của việc <b>đếm</b>: 0, 1, 2, ...).</td><td>Số môn học đã tích lũy, Số con trong gia đình, Số lỗi chính tả.</td></tr>
                <tr><td><b>Liên tục (Continuous)</b></td><td>Giá trị có thể nhận bất kỳ số nào trong một khoảng (kết quả của phép <b>đo</b>).</td><td>Chiều cao (1,725 m), Thời gian chờ xe buýt (12,4 phút), Cân nặng.</td></tr>
              </tbody>
            </table>
            <div class="tip-box"><b>Mẹo thử nhanh:</b> Giữa hai giá trị bất kỳ, nếu luôn có thể tìm thấy một giá trị trung gian hợp lý (như giữa 1,70 m và 1,71 m có 1,705 m) $\rightarrow$ <b>Liên tục</b>. Nếu không thể chia nhỏ (giữa 2 phòng ngủ và 3 phòng ngủ không có 2,5 phòng ngủ) $\rightarrow$ <b>Rời rạc</b>.</div>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 01 — W01-IMS02] Bộ dữ liệu Chim cánh cụt Palmer Penguins",
        q: "Trong bộ dữ liệu nghiên cứu sinh học Palmer Penguins (Slide 40–41), các nhà khoa học thu thập thông tin về 344 cá thể chim cánh cụt gồm các cột: (1) Loài (`species`: Adelie, Chinstrap, Gentoo); (2) Đảo sinh sống (`island`: Biscoe, Dream, Torgersen); (3) Chiều dài mỏ (`bill_length_mm`, mm); (4) Năm thu thập (`year`: 2007, 2008, 2009). Hãy phân loại chính xác 4 biến trên.",
        sol: "<b>Phân tích đối chiếu theo Slide Week 01 (trang 40–41):</b><br>" +
             "1. <code>species</code>: Các nhóm tên loài chim không có thứ bậc hơn kém $\\rightarrow$ <b>Biến phân loại Định danh (Nominal)</b>.<br>" +
             "2. <code>island</code>: Tên các hòn đảo nơi chim sinh sống $\\rightarrow$ <b>Biến phân loại Định danh (Nominal)</b>.<br>" +
             "3. <code>bill_length_mm</code>: Phép đo liên tục chiều dài mỏ bằng thước kẹp (có thể nhận giá trị thập phân như 39,1 mm) $\\rightarrow$ <b>Biến số Liên tục (Continuous Numerical)</b>.<br>" +
             "4. <code>year</code>: Năm khảo sát (2007, 2008, 2009), có quan hệ thứ tự thời gian tự nhiên $\\rightarrow$ <b>Biến phân loại Thứ bậc (Ordinal)</b> (hoặc biến số rời rạc nếu xét hiệu số năm)."
      },
      {
        level: "Trung bình",
        t: "[Slide Week 01 — W01-CH02] Thử thách '1, 2, 3, 4, 5 nói được gì?'",
        q: "Một kỹ sư nhận một tệp dữ liệu chỉ có một cột $x$ chứa các số nguyên: 1, 2, 3, 4, 5 (Slide 28–29). Tài liệu mô tả bị thiếu. Kỹ sư này kết luận ngay: 'Vì $x$ lưu bằng số nguyên nên $x$ chắc chắn là biến số rời rạc'. Kết luận này đúng hay sai? Tại sao?",
        sol: "<b>Phân tích theo Slide Week 01 (trang 28–29):</b><br>" +
             "<b>Kết luận SAI hoàn toàn!</b> Cách biểu diễn số trong máy tính chỉ là kiểu lưu trữ (Storage type), không quyết định bản chất thống kê của biến.<br>" +
             "- Nếu $x$ là mã hóa của khu vực (1=Miền Bắc, 2=Miền Trung, 3=Miền Nam) $\\rightarrow$ $x$ là <b>Biến phân loại Định danh</b>.<br>" +
             "- Nếu $x$ là đánh giá mức độ hài lòng (1 sao đến 5 sao) $\\rightarrow$ $x$ là <b>Biến phân loại Thứ bậc</b>.<br>" +
             "- Chỉ khi $x$ là số người phụ thuộc hoặc số sản phẩm đếm được (phép tính trung bình có ý nghĩa định lượng thực tế) thì $x$ mới là <b>Biến số rời rạc</b>."
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 01 — W01-IMS01 & W01-CH03] Xác định Đơn vị quan sát (Observation Unit)",
        q: "Dựa vào hai bài toán thực tế trong bài giảng Slide Week 01 (trang 38–43), hãy xác định chính xác Đơn vị quan sát (Observation unit) của mỗi hàng trong bảng dữ liệu:<br>" +
           "a) [W01-IMS01] Bảng dữ liệu 23 bộ phim thuộc Vũ trụ Điện ảnh Marvel (MCU) ghi nhận: Tên phim, Năm phát hành, Doanh thu mở màn (triệu USD), Doanh thu toàn cầu.<br>" +
           "b) [W01-CH03] Bảng lịch sử đăng ký học tập do Phòng Đào tạo UET trích xuất gồm các cột: `MSSV`, `MaMon`, `HocKy`, `DiemSo`.",
        sol: "<b>Phân tích bản chất cấu trúc dữ liệu theo Slide Week 01:</b><br>" +
             "a) Trong bảng Marvel (Slide 38–39): Mỗi hàng đại diện cho <b>một bộ phim cụ thể</b> (A movie). Có 23 hàng tức là có 23 bộ phim được quan sát.<br>" +
             "b) Trong bảng Đào tạo UET (Slide 42–43): Một hàng <b>KHÔNG PHẢI</b> là một sinh viên, cũng không phải một môn học (vì một sinh viên học nhiều môn, một môn có nhiều sinh viên). Mỗi hàng là <b>một lượt đăng ký học (Sinh viên × Môn học × Học kỳ)</b>."
      }
    
    ],
    pitfalls: [
      {
        bad: "Nghĩ rằng hễ dữ liệu chứa toàn số (như mã bưu chính, số điện thoại, số áo cầu thủ) thì đều là biến số.",
        good: "Luôn tự hỏi: 'Lấy trung bình cộng các con số này có ý nghĩa thực tế không?'. Nếu vô nghĩa thì đó là biến phân loại định danh!"
      },
      {
        bad: "Nhầm lẫn giữa biến số rời rạc và biến phân loại thứ bậc khi các mức độ được mã hóa bằng số 1, 2, 3, 4, 5.",
        good: "Các số 1, 2, 3, 4, 5 trên thang đo Likert chỉ là nhãn đại diện cho mức độ đồng ý, bản chất vẫn là biến phân loại thứ bậc."
      }
    ],
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Trong một bảng dữ liệu sinh viên, biến 'Mã số sinh viên' (ví dụ: 24020123) thuộc loại biến nào?",
            "opts": [
                  "Biến phân loại thứ bậc (Ordinal)",
                  "Biến phân loại định danh (Nominal)",
                  "Biến số rời rạc (Discrete numerical)",
                  "Biến số liên tục (Continuous numerical)"
            ],
            "ans": 1,
            "fb": "Chính xác! Mã số sinh viên tuy dùng các chữ số để ghi nhưng bản chất là một 'nhãn danh xưng' dùng để định danh, việc tính trung bình cộng mã sinh viên là hoàn toàn vô nghĩa."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Biến số nào sau đây là một biến số liên tục (Continuous)?",
            "opts": [
                  "Số lượt đăng nhập vào cổng đào tạo trong một học kỳ",
                  "Số phòng học trong tòa nhà E3",
                  "Thời gian hoàn thành bài kiểm tra chạy bằng đồng hồ bấm giờ (phút)",
                  "Số lượng bài tập sinh viên đã nộp trên hệ thống LMS"
            ],
            "ans": 2,
            "fb": "Đúng! Thời gian là đại lượng đo lường trên trục số thực, có thể nhận bất kỳ giá trị thập phân nào tùy thuộc vào độ chính xác của đồng hồ đo (ví dụ: 45,32 phút)."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Một phiếu khảo sát môn học đánh giá mức độ hài lòng với thang điểm 1 (Rất tệ), 2 (Tệ), 3 (Bình thường), 4 (Tốt), 5 (Rất tốt). Một bạn sinh viên khẳng định: 'Vì các giá trị là 1, 2, 3, 4, 5 nên đây là biến số rời rạc và lấy hiệu 5 - 4 bằng 4 - 3'. Khẳng định này đúng hay sai?",
            "opts": [
                  "Đúng, vì 1, 2, 3, 4, 5 là các số nguyên đếm được nên bắt buộc là biến rời rạc",
                  "Đúng, vì thang đo Likert luôn là biến số liên tục",
                  "Sai, đây là biến phân loại định danh vì các mức độ hoàn toàn không so sánh hơn kém được",
                  "Sai, đây là biến phân loại thứ bậc (Ordinal), khoảng cách giữa các mức độ không có ý nghĩa toán học định lượng"
            ],
            "ans": 3,
            "fb": "Chính xác! Đây là Bẫy kinh điển số 1: Mã hóa số trên thang đo thứ bậc không biến nó thành biến số định lượng, vì khoảng cách giữa 'Rất tốt' và 'Tốt' không đo lường bằng một đơn vị cụ thể như giữa 4kg và 5kg."
      }
],
    final_quiz: {
      q: "Trong hồ sơ một chuyến bay, thuộc tính 'Mã số chuyến bay' (ví dụ: VN215) và 'Thời gian bay thực tế' (ví dụ: 125,5 phút) lần lượt thuộc loại biến nào?",
      opts: [
        "Mã số chuyến bay: Phân loại định danh; Thời gian bay: Biến số liên tục",
        "Mã số chuyến bay: Biến số rời rạc; Thời gian bay: Biến số liên tục",
        "Mã số chuyến bay: Phân loại thứ bậc; Thời gian bay: Biến số rời rạc",
        "Cả hai đều là biến số liên tục"
      ],
      ans: 0,
      fb: [
        "Chính xác! Mã số chuyến bay là nhãn gọi tên (định danh), còn thời gian bay là đại lượng đo lường trên trục số thực (liên tục).",
        "Sai! Mã số chuyến bay chứa số nhưng chỉ là nhãn nhận diện, không dùng để cộng trừ nên không phải biến số rời rạc.",
        "Sai! Các mã chuyến bay không có thứ tự tự nhiên cao thấp hơn kém (VN215 không 'lớn hơn' VN216).",
        "Sai! Mã chuyến bay không phải là biến số liên tục."
      ]
    }
  },

  {
    id: "A2",
    cluster: "A",
    title: "Tóm tắt dữ liệu phân loại: Bảng tần số & Bảng liên hợp",
    sources: "Slide Week 02 (tr. 1–35); Stat20 Mục 2.2",
    ref: {
      "slide_file": "week02.pdf",
      "slide_name": "Tuần 02 — Tóm tắt dữ liệu (Phần 1)",
      "pages": "Slide 6 – 35",
      "page_start": 6,
      "section": "Phần 1: Dữ liệu phân loại — Bảng liên hợp, Bảng tần số & Tỉ lệ (Slide 6–35)",
      "stat20": "Stat20 Mục 2.2 (Categorical Summaries & Contingency Tables)",
      "key_points": [
            "Bảng liên hợp 2 chiều (Contingency Table) tóm tắt mối quan hệ giữa 2 biến phân loại",
            "Xác định đúng mẫu số: Tỉ lệ trên tổng hàng, tổng cột hay tổng toàn bảng",
            "Bài tập mẫu UET W02-EX03 và phân tích tiêu đề W02-WP01"
      ],
      "remind": "Nếu bạn hay tính nhầm tỉ lệ phần trăm hoặc chọn sai mẫu số trong bảng 2 chiều, hãy đọc lại Slide Week 02 từ trang 15 đến 25 về quy tắc 'Đọc trước khi tính'."
},
    desc: "Học cách tóm tắt một hoặc hai biến phân loại bằng Bảng tần số, Bảng tỉ lệ, Bảng liên hợp 2 chiều và chọn đúng mẫu số theo ngữ cảnh câu hỏi.",
    steps: [
      {
        t: "Tóm tắt một biến: Tần số và Tỉ lệ",
        c: `<p>Với một biến phân loại, phương pháp tóm tắt duy nhất có ý nghĩa là <b>đếm</b>:</p>
            <ul>
              <li><b>Tần số (Frequency / Count)</b>: Số lượng đơn vị quan sát rơi vào mỗi nhóm.</li>
              <li><b>Tỉ lệ (Proportion / Relative Frequency)</b>: Tần số chia cho tổng số đơn vị:
                  $$\\text{Tỉ lệ} = \\frac{\\text{Tần số nhóm}}{\\text{Tổng số quan sát}}$$
              </li>
            </ul>
            <p>Tổng các tỉ lệ của mọi nhóm luôn luôn bằng đúng $1$ (hay $100\\%$).</p>
            <div class="tip-box"><b>Khi nào dùng Tỉ lệ thay vì Tần số?</b> Khi muốn so sánh giữa các nhóm có quy mô tổng thể khác nhau! Ví dụ: 20 sinh viên trượt môn trong lớp 50 người (tỉ lệ 40%) nghiêm trọng hơn nhiều so với 40 sinh viên trượt môn trong khóa 400 người (tỉ lệ 10%).</div>`
      },
            {
        t: "Hai biến phân loại: Bảng liên hợp 2 chiều (Contingency Table)",
        c: `<p>Muốn xem xét mối liên hệ giữa hai biến phân loại, bài giảng Slide Week 02 (trang 15–19) sử dụng <b>Bảng liên hợp thảm họa Titanic</b> (2.201 hành khách):</p>
            <table class="data-table">
              <thead><tr><th>Độ tuổi \\ Kết quả</th><th>Sống sót</th><th>Tử vong</th><th>Tổng hàng</th></tr></thead>
              <tbody>
                <tr><td><b>Người lớn</b></td><td>654</td><td>1.438</td><td><b>2.092</b></td></tr>
                <tr><td><b>Trẻ em</b></td><td>57</td><td>52</td><td><b>109</b></td></tr>
                <tr><td><b>Tổng cột</b></td><td><b>711</b></td><td><b>1.490</b></td><td><b>2.201</b></td></tr>
              </tbody>
            </table>
            <p>Trong bảng trên: Ô giao nhau cho biết tần số kết hợp (ví dụ: có $57$ hành khách là trẻ em và sống sót). Tổng hàng và tổng cột đều cộng ra tổng chung $n = 2.201$.</p>`
      },
      {
        t: "Kỹ năng sống còn: Chọn đúng MẪU SỐ khi tính tỉ lệ",
        c: `<p>Từ bảng liên hợp Titanic (Slide 21–22), bài thi thường yêu cầu tính 3 loại tỉ lệ khác nhau. Điểm mấu chốt là <b>xác định đúng MẪU SỐ</b>:</p>
            <ol>
              <li><b>Tỉ lệ trên toàn bộ (Joint Proportion)</b>: Mẫu số là <b>Tổng chung toàn bảng (2.201)</b>.<br>
                  Ví dụ: Tỉ lệ trẻ em sống sót trong toàn bộ hành khách = $\\frac{57}{2201} \\approx 2{,}59\\%$.
              </li>
              <li><b>Tỉ lệ có điều kiện theo hàng (Row Conditional)</b>: Mẫu số là <b>Tổng hàng</b>.<br>
                  Ví dụ: <i>Trong số trẻ em</i>, tỉ lệ sống sót = $\\frac{57}{109} \\approx 52{,}29\\%$.<br>
                  <i>Trong số người lớn</i>, tỉ lệ sống sót = $\\frac{654}{2092} \\approx 31{,}26\\%$.
              </li>
              <li><b>Tỉ lệ có điều kiện theo cột (Column Conditional)</b>: Mẫu số là <b>Tổng cột</b>.<br>
                  Ví dụ: <i>Trong số những người sống sót</i>, tỉ lệ trẻ em = $\\frac{57}{711} \\approx 8{,}02\\%$.
              </li>
            </ol>
            <div class="tip-box"><b>Mẹo tìm mẫu số trong câu hỏi:</b> Hãy tìm cụm từ <i>&quot;Trong số...&quot;</i> hoặc <i>&quot;Biết rằng...&quot;</i>. Đối tượng đứng ngay sau cụm từ đó chính là <b>MẪU SỐ</b>!</div>`
      },
      {
        t: "Làm thế nào để biết hai biến có liên hệ với nhau?",
        c: `<p>Hai biến phân loại được coi là <b>có mối liên hệ (associated)</b> nếu sự phân bố của biến này thay đổi khi ta biết thông tin về biến kia (Slide 23–26).</p>
            <p>Trong bảng Titanic, tỉ lệ sống sót của trẻ em ($52{,}29\\%$) cao hơn hẳn tỉ lệ sống sót của người lớn ($31{,}26\\%$). Sự khác biệt này cho thấy giữa <b>Độ tuổi</b> và <b>Kết quả sống sót</b> có mối liên hệ rõ rệt!</p>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 02 — W02-EX01 & W02-EX02] Thảm họa Titanic: Số đếm hay Tỉ lệ?",
        q: "Bảng liên hợp thảm họa Titanic trong bài giảng (Slide 16–19) ghi nhận kết quả sống sót của 2.201 hành khách:<br>" +
           "- Người lớn: 654 người sống sót, 1.438 người thiệt mạng (Tổng: 2.092 người lớn).<br>" +
           "- Trẻ em: 57 người sống sót, 52 người thiệt mạng (Tổng: 109 trẻ em).<br>" +
           "Một bạn sinh viên nhìn vào bảng và kết luận: <i>'Người lớn có kết quả sống sót tốt hơn trẻ em vì 654 > 57'</i>. Hãy chỉ ra sai lầm của kết luận này và tính tỉ lệ sống sót chính xác của từng nhóm.",
        sol: "<b>Phân tích theo Slide Week 02 (trang 18–19):</b><br>" +
             "Sai lầm chí mạng: So sánh số đếm thô (654 vs 57) giữa hai nhóm có quy mô tổng thể chênh lệch quá lớn (2.092 người lớn vs 109 trẻ em). Muốn so sánh công bằng, bắt buộc phải dùng <b>Tỉ lệ có điều kiện</b>:<br>" +
             "- Tỉ lệ sống sót của người lớn: $P(\\text{Sống} \\mid \\text{Người lớn}) = \\frac{654}{2092} \\approx 31{,}3\\%$.<br>" +
             "- Tỉ lệ sống sót của trẻ em: $P(\\text{Sống} \\mid \\text{Trẻ em}) = \\frac{57}{109} \\approx 52{,}3\\%$.<br>" +
             "<b>Kết luận đúng:</b> Trẻ em có tỉ lệ sống sót cao hơn người lớn rất nhiều ($52{,}3\\% > 31{,}3\\%$) do nguyên tắc ưu tiên cứu hộ trẻ em!"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 02 — W02-EX03] Thử thách xác định Mẫu số trước khi tính",
        q: "Dựa vào bảng liên hợp Titanic (Slide 21–22) gồm tổng cộng 2.201 người, trong đó tổng số người sống sót là 711 người (654 người lớn, 57 trẻ em). Hãy xác định đúng mẫu số và tính giá trị của 3 câu hỏi sau:<br>" +
           "A. 'Trong số người lớn, bao nhiêu phần sống sót?'<br>" +
           "B. 'Trong số những người sống sót, bao nhiêu phần là trẻ em?'<br>" +
           "C. 'Trong toàn bộ hành khách, tỉ lệ trẻ em sống sót là bao nhiêu?'",
        sol: "<b>Đáp án chuẩn hóa theo Slide Week 02 (trang 22):</b><br>" +
             "- <b>Câu A:</b> Cụm từ <i>'Trong số người lớn'</i> chỉ định MẪU SỐ là tổng số người lớn ($2.092$).<br>" +
             "  $$\\text{Tỉ lệ} = \\frac{654}{2092} \\approx 31{,}26\\%$$<br>" +
             "- <b>Câu B:</b> Cụm từ <i>'Trong số người sống sót'</i> chỉ định MẪU SỐ là tổng người sống ($711$).<br>" +
             "  $$\\text{Tỉ lệ} = \\frac{57}{711} \\approx 8{,}02\\%$$<br>" +
             "- <b>Câu C:</b> Cụm từ <i>'Trong toàn bộ hành khách'</i> chỉ định MẪU SỐ là tổng toàn bảng ($2.201$).<br>" +
             "  $$\\text{Tỉ lệ} = \\frac{57}{2201} \\approx 2{,}59\\%$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 02 — W02-WP01] Phản biện bài báo: Tiêu đề có đúng không?",
        q: "Một bài báo nhìn vào bảng dữ liệu Titanic và giật tít: <i>'Hơn 90% số người sống sót là người lớn, vậy đi tàu Titanic là người lớn an toàn hơn trẻ em!'</i> (Slide 34–35). Dưới góc độ xác suất thống kê, hãy phân tích tại sao tiêu đề này ngụy biện và đánh tráo khái niệm.",
        sol: "<b>Phân tích phản biện theo Slide Week 02 (trang 34–35):</b><br>" +
             "1. Con số 'hơn 90%' thực chất là $\\frac{654}{711} \\approx 91{,}98\\%$, tức là xác suất $P(\\text{Người lớn} \\mid \\text{Sống sót})$.<br>" +
             "2. Khái niệm 'an toàn hơn' (xác suất sống sót khi gặp nạn) phải được đo bằng $P(\\text{Sống sót} \\mid \\text{Người lớn}) = 31{,}3\\%$, so sánh với $P(\\text{Sống sót} \\mid \\text{Trẻ em}) = 52{,}3\\%$.<br>" +
             "3. Người lớn chiếm tới 92% số người sống sót đơn giản là vì họ chiếm tới 95% tổng số người trên tàu ($2.092 / 2.201$), chứ không phải vì người lớn được an toàn hơn!"
      }
    
    ],
    pitfalls: [
      {
        bad: "Lấy luôn tổng chung của toàn bảng làm mẫu số cho mọi câu hỏi tính tỉ lệ.",
        good: "Đọc thật kỹ đề bài để tìm điều kiện thu hẹp không gian mẫu: 'trong số hàng nào' thì chia tổng hàng đó, 'trong số cột nào' thì chia tổng cột đó!"
      },
      {
        bad: "Kết luận biến A gây ra biến B (quan hệ nhân quả) chỉ vì thấy hai biến có liên hệ trong bảng liên hợp.",
        good: "Mối liên hệ thống kê (Association) KHÔNG đồng nghĩa với quan hệ Nhân quả (Causation). Có thể có biến ẩn thứ ba chi phối."
      }
    ],
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Trong bảng liên hợp hai chiều (Contingency table) giữa Ngành học và Giới tính, tỷ lệ phần trăm được tính trên tổng số sinh viên của toàn bộ bảng được gọi là:",
            "opts": [
                  "Tỷ lệ đồng thời (Joint proportion)",
                  "Tần số tương đối tích lũy",
                  "Tỷ lệ có điều kiện (Conditional proportion)",
                  "Tỷ lệ biên (Marginal proportion)"
            ],
            "ans": 0,
            "fb": "Chính xác! Tỷ lệ đồng thời được tính bằng số phần tử ở ô giao chia cho tổng cỡ mẫu toàn bảng (Grand total)."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Cho bảng khảo sát: Lớp CNTT có 40 Nam, 10 Nữ; Lớp KHMT có 30 Nam, 20 Nữ. Trong số các sinh viên Nữ, tỷ lệ sinh viên thuộc lớp CNTT là:",
            "opts": [
                  "$\\frac{40}{70} \\approx 57{,}14\\%$",
                  "$\\frac{10}{30} \\approx 33{,}33\\%$",
                  "$\\frac{10}{100} = 10\\%$",
                  "$\\frac{10}{50} = 20\\%$"
            ],
            "ans": 1,
            "fb": "Đúng! Tổng số sinh viên Nữ là $10 + 20 = 30$. Tỷ lệ có điều kiện trong nhóm Nữ thuộc lớp CNTT là $10/30 \\approx 33{,}33\\%$."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Hiện tượng một xu hướng tương quan xuất hiện trong từng phân nhóm nhỏ nhưng lại bị đảo ngược hoàn toàn khi gộp chung tất cả các nhóm lại được gọi là:",
            "opts": [
                  "Nghịch lý Simpson (Simpson's Paradox)",
                  "Nghịch lý Monty Hall",
                  "Ngoại lai đòn bẩy cao",
                  "Sai số chọn mẫu hệ thống"
            ],
            "ans": 0,
            "fb": "Chính xác! Nghịch lý Simpson xảy ra do sự hiện diện của một biến ẩn (Lurking/Confounding variable) phân bố không đồng đều giữa các nhóm."
      }
],
    final_quiz: {
      q: "Theo bảng liên hợp 50 sinh viên ở trên, hỏi trong số những sinh viên CÓ ĐI LÀM THÊM, tỉ lệ sinh viên Năm 2 là bao nhiêu?",
      opts: [
        "62,5% (10/16)",
        "50,0% (10/20)",
        "20,0% (10/50)",
        "31,25% (5/16)"
      ],
      ans: 0,
      fb: [
        "Chính xác! Cụm từ 'trong số những sinh viên có đi làm thêm' xác định mẫu số là tổng cột CÓ ĐI LÀM = 16. Tử số là 10. Tỉ lệ = 10/16 = 62,5%.",
        "Sai! Bạn đã lấy nhầm mẫu số là tổng hàng Năm 2 (10/20 = 50%). Đó là tỉ lệ đi làm thêm của sinh viên Năm 2.",
        "Sai! Bạn đã lấy mẫu số là tổng toàn trường 50 (10/50 = 20%).",
        "Sai! Phép tính sai số liệu."
      ]
    }
  },

  {
    id: "A3",
    cluster: "A",
    title: "Tóm tắt dữ liệu số: Tâm, Phân tán, Hình dạng & Ngoại lai",
    sources: "Slide Week 02 (tr. 36–114); Stat20 Mục 2.4",
    ref: {
      "slide_file": "week02.pdf",
      "slide_name": "Tuần 02 — Tóm tắt dữ liệu (Phần 2 & 3)",
      "pages": "Slide 36 – 114",
      "page_start": 36,
      "section": "Phần 2: Dữ liệu số (Slide 36–56), Phần 3: Đo lường phân tán (Slide 57–69) & Phần 4: Giá trị bất thường (Slide 70–95)",
      "stat20": "Stat20 Mục 2.4 (Numerical Summaries, IQR & Robustness)",
      "key_points": [
            "Đo độ tập trung: Trung bình (Mean) nhạy cảm ngoại lai vs Trung vị (Median) bền vững (Robust)",
            "Đo độ phân tán: Khoảng biến thiên (Range), Phương sai mẫu, Độ lệch chuẩn (SD), Tứ phân vị (IQR = Q3 - Q1)",
            "Quy tắc hàng rào Tukey xác định ngoại lai: [Q1 - 1.5*IQR, Q3 + 1.5*IQR]"
      ],
      "remind": "Nếu bạn chưa nắm chắc cách tìm Q1, Q3 hoặc công thức xác định ngoại lai 1.5*IQR, hãy mở lại Slide Week 02 các trang 44, 70–75 và 91 (bài mẫu W02-EX11)."
},
    desc: "Hiểu sâu 3 khía cạnh khi phân tích dữ liệu số: Tâm (Mean vs Median), Độ phân tán (SD vs IQR), Hình dạng phân phối (Skewness) và quy tắc 1.5×IQR phát hiện ngoại lai.",
    widget: "outlier_widget",
    steps: [
      {
        t: "Ba câu hỏi bắt buộc khi nhìn vào một biến số",
        c: `<p>Mỗi khi đối diện với một cột dữ liệu số, bạn luôn phải trả lời 3 câu hỏi:</p>
            <ol>
              <li><b>Tâm (Center) nằm ở đâu?</b> $\rightarrow$ Dùng Trung bình (Mean) hoặc Trung vị (Median).</li>
              <li><b>Độ phân tán (Spread) rộng bao nhiêu?</b> $\rightarrow$ Dùng Độ lệch chuẩn (SD) hoặc Khoảng tứ phân vị (IQR).</li>
              <li><b>Hình dạng phân phối (Shape) thế nào?</b> $\rightarrow$ Đối xứng hay Lệch? Có bao nhiêu đỉnh? Có giá trị ngoại lai không?</li>
            </ol>`
      },
      {
        t: "Thước đo Tâm: Trung bình (Mean) vs Trung vị (Median)",
        c: `<p>Giả sử ta có tập dữ liệu gồm $n$ số: $x_1, x_2, \\dots, x_n$:</p>
            <ul>
              <li><b>Trung bình mẫu (Mean) $\\bar{x}$</b>: Tổng tất cả chia cho số lượng:
                  $$\\bar{x} = \\frac{1}{n}\\sum_{i=1}^{n} x_i$$
              </li>
              <li><b>Trung vị (Median)</b>: Giá trị đứng chính giữa sau khi đã sắp xếp dãy số từ bé đến lớn. (Nếu $n$ chẵn, lấy trung bình cộng của 2 số ở giữa).</li>
            </ul>
            <div class="tip-box">
              <b>Tính bền vững (Robustness):</b><br>
              Trung bình $\\bar{x}$ <b>rất nhạy cảm với các giá trị cực đoan (ngoại lai)</b>. Chỉ cần một con số cực lớn xuất hiện, trung bình sẽ bị kéo vọt lên. Ngược lại, Trung vị là thước đo <b>bền vững (robust)</b> vì vị trí giữa của dãy số hầu như không đổi khi các đầu mút thay đổi!
            </div>`
      },
      {
        t: "Thước đo Phân tán: Khoảng biến thiên, IQR và Độ lệch chuẩn (SD)",
        c: `<p>Để đo xem dữ liệu tập trung xít xao hay tản mác ra xa tâm, ta có:</p>
            <ul>
              <li><b>Khoảng biến thiên (Range)</b>: $\\text{Range} = \\text{Max} - \\text{Min}$ (rất nhạy cảm với ngoại lai).</li>
              <li><b>Bộ 5 số tóm tắt (Five-number summary)</b>: $\\text{Min}, Q_1, \\text{Median}, Q_3, \\text{Max}$. Trong đó:
                <ul>
                  <li>$Q_1$ (Tứ phân vị thứ nhất): Điểm cắt 25% giá trị nhỏ nhất.</li>
                  <li>$Q_3$ (Tứ phân vị thứ ba): Điểm cắt 75% giá trị nhỏ nhất.</li>
                </ul>
              </li>
              <li><b>Khoảng tứ phân vị (IQR)</b>: Độ rộng của 50% dữ liệu nằm ở chính giữa:
                  $$\\text{IQR} = Q_3 - Q_1$$
                  <i>IQR là thước đo độ phân tán bền vững (đi kèm với Trung vị).</i>
              </li>
              <li><b>Phương sai mẫu $s^2$ và Độ lệch chuẩn mẫu $s$</b>:
                  $$s^2 = \\frac{1}{n-1}\\sum_{i=1}^{n} (x_i - \\bar{x})^2, \\quad s = \\sqrt{s^2}$$
                  <i>Lưu ý: Mẫu số là $n-1$ (bậc tự do) đối với mẫu dữ liệu thực nghiệm. $s$ đi kèm với Trung bình $\\bar{x}$.</i>
              </li>
            </ul>`
      },
      {
        t: "Tiêu chuẩn xác định Ngoại lai (Outlier) & Hình dạng phân phối",
        c: `<p><b>Quy tắc hàng rào Tukey ($1{,}5 \\times \\text{IQR}$):</b> Một điểm dữ liệu $x$ bị coi là giá trị ngoại lai nếu nằm ngoài hai rào chắn:</p>
            <ul>
              <li><b>Rào dưới (Lower Fence)</b>: $\\text{Cận dưới} = Q_1 - 1{,}5 \\times \\text{IQR}$</li>
              <li><b>Rào trên (Upper Fence)</b>: $\\text{Cận trên} = Q_3 + 1{,}5 \\times \\text{IQR}$</li>
            </ul>
            <p><b>Mối liên hệ giữa Hình dạng phân phối và các thước đo tâm:</b></p>
            <table class="data-table">
              <thead><tr><th>Hình dạng phân phối</th><th>Đặc điểm đồ thị</th><th>Quan hệ Mean vs Median</th><th>Nên chọn cặp thước đo nào?</th></tr></thead>
              <tbody>
                <tr><td><b>Đối xứng (Symmetric)</b></td><td>Hình chuông cân đối ở giữa</td><td>$\\text{Mean} \\approx \\text{Median}$</td><td><b>Mean và SD</b></td></tr>
                <tr><td><b>Lệch phải (Right-skewed)</b></td><td>Đuôi dài kéo về bên phải (thu nhập, giá nhà)</td><td>$\\text{Mean} &gt; \\text{Median}$</td><td><b>Median và IQR</b> (bền vững)</td></tr>
                <tr><td><b>Lệch trái (Left-skewed)</b></td><td>Đuôi dài kéo về bên trái (tuổi thọ)</td><td>$\\text{Mean} &lt; \\text{Median}$</td><td><b>Median và IQR</b> (bền vững)</td></tr>
              </tbody>
            </table>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 02 — W02-EX10] Bài toán thi bù OpenIntro 4e",
        q: "Trong một lớp học gồm 25 sinh viên, có 24 bạn thi đợt 1 với điểm trung bình đạt $\\bar{x} = 74$ điểm (Slide 88–89). Bạn sinh viên thứ 25 bị ốm phải thi bù và đạt 64 điểm. Hãy tính điểm trung bình mới của toàn bộ 25 sinh viên trong lớp.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 02 (trang 89):</b><br>" +
             "1. Tổng điểm thi của 24 bạn đầu tiên là: $\\sum_{i=1}^{24} x_i = 24 \\times 74 = 1776$ điểm.<br>" +
             "2. Sau khi cộng điểm của bạn thứ 25 ($64$ điểm), tổng điểm của cả 25 bạn là:<br>" +
             "   $$\\sum_{i=1}^{25} x_i = 1776 + 64 = 1840 \\text{ điểm}$$<br>" +
             "3. Điểm trung bình mới của cả lớp là:<br>" +
             "   $$\\bar{x}_{\\text{new}} = \\frac{1840}{25} = 73{,}6 \\text{ điểm}$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 02 — W02-EX11] Xác định Ngoại lai theo Hàng rào Tukey",
        q: "Cho 20 điểm thi đã sắp xếp tăng dần từ bài tập OpenIntro 4e (Slide 90–91):<br>" +
           "$$57, 66, 69, 71, 72, 73, 74, 77, 78, 78, 79, 79, 81, 81, 82, 83, 83, 88, 89, 94$$<br>" +
           "Biết $Q_1 = 72{,}5$ và $Q_3 = 82{,}5$. Hãy tính khoảng tứ phân vị $\\text{IQR}$, xác định hai hàng rào Tukey và kiểm tra xem có điểm ngoại lai nào không.",
        sol: "<b>Lời giải từng bước theo Slide Week 02 (trang 91):</b><br>" +
             "1. Tính khoảng tứ phân vị: $\\text{IQR} = Q_3 - Q_1 = 82{,}5 - 72{,}5 = 10$.<br>" +
             "2. Độ vươn hàng rào: $1{,}5 \\times \\text{IQR} = 1{,}5 \\times 10 = 15$.<br>" +
             "3. Xác định hai ngưỡng hàng rào:<br>" +
             "   - <b>Hàng rào dưới (Lower fence):</b> $Q_1 - 1{,}5\\text{IQR} = 72{,}5 - 15 = 57{,}5$.<br>" +
             "   - <b>Hàng rào trên (Upper fence):</b> $Q_3 + 1{,}5\\text{IQR} = 82{,}5 + 15 = 97{,}5$.<br>" +
             "4. <b>Kiểm tra ngoại lai:</b> Điểm thi $57 < 57{,}5$ (nằm ngoài hàng rào dưới) $\\rightarrow$ <b>57 là giá trị ngoại lai (outlier)</b> duy nhất của bộ dữ liệu."
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 02 — W02-CH02 & W02-CH03] Phản ví dụ: Mean = Median có đối xứng không?",
        q: "a) [W02-CH02] Dãy dữ liệu mẫu STAT20 gồm 11 quan sát có Trung bình $\\approx 8{,}455$, Trung vị $= 8$, $\\text{SD} \\approx 1{,}695$. Nếu thay một giá trị 6 bằng $-200$ (ngoại lai cực đoan), hãy quan sát sự biến động của Trung bình và Trung vị.<br>" +
           "b) [W02-CH03] Hãy chứng minh hoặc bác bỏ mệnh đề: <i>'Nếu Trung bình = Trung vị thì phân phối chắc chắn đối xứng'</i>.",
        sol: "<b>Phân tích bản chất theo Slide Week 02 (trang 75 & 79):</b><br>" +
             "a) Khi thay $6$ bằng $-200$ (Slide 75):<br>" +
             "   - <b>Trung vị (Median):</b> Vẫn giữ nguyên bằng $8$ (bền vững hoàn hảo!).<br>" +
             "   - <b>Trung bình (Mean):</b> Bị kéo sụt thê thảm từ $8{,}455$ xuống $-10{,}273$; độ lệch chuẩn SD vọt lên $62{,}94$.<br>" +
             "b) <b>Bác bỏ mệnh đề!</b> Mệnh đề trên là SAI (Slide 79). Phản ví dụ mẫu 5 số: $(-4, -1, 0, 2, 3)$.<br>" +
             "   - Tổng $= (-4) + (-1) + 0 + 2 + 3 = 0 \\implies \\text{Mean} = 0$.<br>" +
             "   - Số chính giữa là $0 \\implies \\text{Median} = 0$.<br>" +
             "   - Dãy số này hoàn toàn <b>không đối xứng</b> quanh 0 vì khoảng cách về phía âm kéo dài tới $-4$ trong khi phía dương chỉ tới $+3$!"
      }
    
    ],
    pitfalls: [
      {
        bad: "Dùng Trung bình và Độ lệch chuẩn để tóm tắt dữ liệu có chứa ngoại lai hoặc phân phối lệch mạnh.",
        good: "Khi dữ liệu bị lệch hoặc có ngoại lai, bắt buộc phải dùng cặp thước đo bền vững là Trung vị (Median) và IQR!"
      },
      {
        bad: "Nhầm lẫn chiều lệch: nghĩ rằng 'lệch phải' là đỉnh nhô về bên phải.",
        good: "Tên gọi 'lệch phải' (Right-skewed) đặt theo phía của CÁI ĐUÔI DÀI! Đuôi kéo dài về bên phải thì gọi là lệch phải."
      }
    ],
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Đại lượng nào sau đây đo độ phân tán của dữ liệu và có tính bền vững (Robust) chống lại giá trị ngoại lai?",
            "opts": [
                  "Độ lệch chuẩn mẫu ($s$)",
                  "Khoảng biến thiên ($Range = x_{max} - x_{min}$)",
                  "Khoảng tứ phân vị ($IQR = Q_3 - Q_1$)",
                  "Phương sai mẫu ($s^2$)"
            ],
            "ans": 2,
            "fb": "Chính xác! $IQR$ chỉ đo độ biến thiên của 50% dữ liệu trung tâm nên không bị ảnh hưởng bởi các giá trị cực đoan ở hai đầu mút."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Một tập dữ liệu điểm thi có hình dạng lệch phải rõ rệt (Right-skewed). So sánh nào sau đây là đúng về mối quan hệ giữa Số trung bình (Mean) và Trung vị (Median)?",
            "opts": [
                  "$\\text{Mean} = \\text{IQR}$",
                  "$\\text{Mean} < \\text{Median}$",
                  "$\\text{Mean} = \\text{Median}$",
                  "$\\text{Mean} > \\text{Median}$"
            ],
            "ans": 3,
            "fb": "Đúng! Đuôi dài bên phải kéo số trung bình lệch về phía các giá trị lớn, trong khi trung vị vẫn neo giữ ở vị trí chia đôi tập dữ liệu."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Cho mẫu số liệu có $Q_1 = 20$ và $Q_3 = 35$. Theo tiêu chuẩn hàng rào 1.5 IQR của Tukey, giá trị nào sau đây được xác định là một điểm ngoại lai (Outlier)?",
            "opts": [
                  "$30$",
                  "$45$",
                  "$60$",
                  "$15$"
            ],
            "ans": 2,
            "fb": "Chính xác! $IQR = 35 - 20 = 15$. Hàng rào trên: $Q_3 + 1{,}5 IQR = 35 + 1{,}5(15) = 35 + 22{,}5 = 57{,}5$. Giá trị $60 > 57{,}5$ nên là ngoại lai."
      }
],
    final_quiz: {
      q: "Một đồ thị phân phối thời gian chờ khám bệnh có dạng đuôi dài kéo về phía bên phải. Nhận định nào sau đây là ĐÚNG?",
      opts: [
        "Trung bình > Trung vị; nên dùng Trung vị và IQR để tóm tắt dữ liệu",
        "Trung bình < Trung vị; nên dùng Trung bình và Độ lệch chuẩn",
        "Trung bình = Trung vị; phân phối có tính đối xứng hoàn hảo",
        "Trung vị bị giá trị ngoại lai kéo lệch nhiều hơn Trung bình"
      ],
      ans: 0,
      fb: [
        "Chính xác! Phân phối lệch phải có các giá trị lớn kéo trung bình lên cao hơn trung vị (Mean > Median). Khi đó, Median và IQR là lựa chọn chuẩn xác vì tính bền vững.",
        "Sai! Đuôi dài bên phải kéo trung bình lớn hơn trung vị, không phải nhỏ hơn.",
        "Sai! Trung bình bằng trung vị chỉ xảy ra ở phân phối đối xứng.",
        "Sai! Trung vị có tính bền vững, ít bị kéo lệch hơn trung bình."
      ]
    }
  },

  {
    id: "A4",
    cluster: "A",
    title: "Tương quan tuyến tính & Hồi quy đơn giản (OLS)",
    sources: "Slide Week 04 (tr. 1–75); Stat20 Mục 2.10, 7.2",
    ref: {
      "slide_file": "week04.pdf",
      "slide_name": "Tuần 04 — Mối quan hệ giữa các biến & Hồi quy OLS",
      "pages": "Slide 1 – 75",
      "page_start": 1,
      "section": "Phần 1: Hệ số tương quan Pearson r (Slide 1–40) & Phần 2: Hồi quy tuyến tính bình phương tối thiểu OLS (Slide 41–75)",
      "stat20": "Stat20 Mục 2.10 & Mục 7.2 (Correlation & Simple Linear Regression)",
      "key_points": [
            "Hệ số tương quan r ∈ [-1, 1], đo mức độ tuyến tính, bất biến với phép đổi thang đo tuyến tính",
            "Đường hồi quy mẫu: y^ = b0 + b1*x với b1 = r * (sy / sx) và b0 = y_bar - b1 * x_bar",
            "Phần dư e = y - y^, tổng phần dư luôn bằng 0, hệ số xác định R^2 = r^2"
      ],
      "remind": "Nếu bạn chưa thành thạo bấm máy Casio tính b0, b1 hoặc diễn giải ý nghĩa kinh tế của hệ số góc b1, hãy ôn lại Slide Week 04 từ trang 45 đến trang 65."
},
    desc: "Hiểu bản chất Hệ số tương quan Pearson r, phương trình đường hồi quy bình phương tối thiểu (OLS), ý nghĩa của hệ số góc, hệ số chặn và phần dư.",
    steps: [
      {
        t: "Hệ số tương quan Pearson $r$: Đo quan hệ đường thẳng",
        c: `<p>Khi khảo sát mối liên hệ giữa hai biến số $X$ và $Y$, công cụ đầu tiên là <b>Hệ số tương quan mẫu $r$ (Pearson correlation coefficient)</b>:</p>
            <ul>
              <li>$r$ luôn nằm trong đoạn $[-1, 1]$.</li>
              <li><b>Dấu của $r$</b> cho biết chiều của mối quan hệ:
                <ul>
                  <li>$r &gt; 0$: Tương quan dương ($X$ tăng thì $Y$ có xu hướng tăng theo).</li>
                  <li>$r &lt; 0$: Tương quan âm ($X$ tăng thì $Y$ có xu hướng giảm).</li>
                  <li>$r = 0$: Không có mối liên hệ <i>tuyến tính</i>.</li>
                </ul>
              </li>
              <li><b>Độ lớn $|r|$</b> cho biết độ mạnh: $|r|$ càng gần $1$, các điểm dữ liệu càng tập trung sát vào một đường thẳng.</li>
            </ul>
            <div class="warn-box">
              <b>Hai định luật bắt buộc phải nhớ trong phòng thi:</b><br>
              1. $r$ chỉ đo mối liên hệ <b>TUYẾN TÍNH (đường thẳng)</b>. Nếu dữ liệu có mối quan hệ đường cong parabol hoàn hảo, $r$ vẫn có thể bằng 0!<br>
              2. <b>Tương quan KHÔNG đồng nghĩa với Nhân quả (Correlation is NOT Causation)!</b> $r$ cao giữa điểm thi và số giờ ngủ không có nghĩa ngủ nhiều làm tăng điểm thi.
            </div>`
      },
      {
        t: "Đường hồi quy tuyến tính đơn giản (OLS)",
        c: `<p>Mục tiêu của hồi quy là dùng biến giải thích $X$ để <b>dự đoán</b> giá trị của biến phản hồi $Y$ thông qua một phương trình đường thẳng:</p>
            $$\\hat{y} = b_0 + b_1 x$$
            <p>Trong đó:</p>
            <ul>
              <li>$\\hat{y}$ (đọc là y-mũ): Giá trị <b>dự đoán</b> của $Y$.</li>
              <li>$b_1$ (Hệ số góc / Slope): Cho biết khi $x$ tăng thêm $1$ đơn vị, giá trị dự đoán $\\hat{y}$ sẽ <b>thay đổi $b_1$ đơn vị</b>.
                  $$b_1 = r \\cdot \\frac{s_y}{s_x}$$
              </li>
              <li>$b_0$ (Hệ số chặn / Intercept): Giá trị dự đoán của $Y$ khi $x = 0$:
                  $$b_0 = \\bar{y} - b_1 \\bar{x}$$
              </li>
            </ul>
            <p>Đường thẳng này được gọi là đường <b>Bình phương tối thiểu (Ordinary Least Squares - OLS)</b> vì nó làm cho <i>tổng bình phương các sai số dự đoán là nhỏ nhất có thể</i>.</p>`
      },
      {
        t: "Phần dư (Residual): Sai số của mô hình",
        c: `<p>Với mỗi điểm dữ liệu thực tế $(x_i, y_i)$, khoảng cách chênh lệch thẳng đứng giữa giá trị quan sát thật và giá trị đường hồi quy dự đoán được gọi là <b>Phần dư ($e_i$)</b>:</p>
            $$e_i = y_i - \\hat{y}_i = \\text{Quan sát thật} - \\text{Giá trị dự đoán}$$
            <ul>
              <li>Nếu $e_i &gt; 0$: Điểm thực tế nằm <b>phía trên</b> đường hồi quy (mô hình dự đoán dưới mức).</li>
              <li>Nếu $e_i &lt; 0$: Điểm thực tế nằm <b>phía dưới</b> đường hồi quy (mô hình dự đoán quá mức).</li>
              <li>Nếu $e_i = 0$: Điểm thực tế nằm chính xác trên đường hồi quy.</li>
            </ul>
            <div class="tip-box"><b>Tính chất toán học đặc biệt của OLS:</b> Tổng đại số của tất cả các phần dư luôn luôn bằng đúng $0$: $\\sum_{i=1}^{n} e_i = 0$!</div>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 04 — W04-EX01 & W04-CH01] Tính chất của Hệ số tương quan Pearson r",
        q: "a) [W04-EX01] Nếu ta đổi thang đo nhiệt độ từ Celsius sang Fahrenheit ($y = 1{,}8x + 32$), hệ số tương quan $r$ giữa nhiệt độ và lượng điện tiêu thụ có thay đổi không?<br>" +
           "b) [W04-CH01] Chứng minh hoặc bác bỏ mệnh đề: <i>'Hệ số tương quan $r = 0$ đồng nghĩa với việc hai biến $X$ và $Y$ không có mối liên hệ nào'</i>.",
        sol: "<b>Phân tích lý thuyết theo Slide Week 04 (trang 16–19):</b><br>" +
             "a) Hệ số tương quan $r$ <b>bất biến với phép đổi thang đo tuyến tính dương</b>: $r(a x + b, y) = r(x, y)$ với mọi $a > 0$. Do đó $r$ không hề thay đổi!<br>" +
             "b) <b>Khẳng định SAI!</b> Hệ số Pearson $r$ chỉ đo mức độ <b>liên hệ tuyến tính (đường thẳng)</b>.<br>" +
             "   - Phản ví dụ kinh điển (Slide 19): Xét 5 điểm với $y = x^2$: $(-2, 4), (-1, 1), (0, 0), (1, 1), (2, 4)$.<br>" +
             "   - Do tính đối xứng hoàn hảo, $r(X, Y) = 0$, nhưng giữa $X$ và $Y$ có quan hệ hàm số phi tuyến hoàn hảo ($Y = X^2$)!"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 04 — W04-WP02] Suy ra Đường hồi quy OLS từ Thống kê tóm tắt",
        q: "Trong nghiên cứu mối liên hệ giữa tỉ lệ tốt nghiệp THPT ($x$, %) và tỉ lệ nghèo đói ($y$, %) tại các bang của Hoa Kỳ (Slide 44–45), số liệu tóm tắt cho thấy:<br>" +
           "$$\\bar{x} = 86{,}01\\%, \\quad s_x = 3{,}73\\%, \\quad \\bar{y} = 11{,}35\\%, \\quad s_y = 3{,}10\\%, \\quad r = -0{,}75$$<br>" +
           "Hãy tìm phương trình đường hồi quy tuyến tính mẫu $\\hat{y} = b_0 + b_1 x$ và nêu ý nghĩa hệ số góc $b_1$.",
        sol: "<b>Lời giải chi tiết theo Slide Week 04 (trang 45):</b><br>" +
             "1. Tính hệ số góc $b_1$:<br>" +
             "   $$b_1 = r \\frac{s_y}{s_x} = -0{,}75 \\times \\frac{3{,}10}{3{,}73} \\approx -0{,}623 \\approx -0{,}62$$<br>" +
             "2. Tính hệ số chặn $b_0$ dựa vào điểm trung bình $(\\bar{x}, \\bar{y})$ luôn thuộc đường hồi quy:<br>" +
             "   $$b_0 = \\bar{y} - b_1 \\bar{x} = 11{,}35 - (-0{,}623) \\times 86{,}01 \\approx 64{,}68$$<br>" +
             "3. Phương trình hồi quy mẫu: $\\hat{y} = 64{,}68 - 0{,}62 x$.<br>" +
             "4. <b>Ý nghĩa hệ số góc:</b> Khi tỉ lệ tốt nghiệp THPT của một bang tăng thêm $1\\%$, mô hình dự đoán tỉ lệ nghèo đói trung bình giảm đi $0{,}62\\%$."
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 04 — W04-Q02 & W04-WP01] Tính và Diễn giải Phần dư (Residual)",
        q: "Sử dụng mô hình hồi quy $\\hat{y} = 64{,}68 - 0{,}62 x$ ở trên. Bang Rhode Island có tỉ lệ tốt nghiệp thực tế là $x = 81\\%$ và tỉ lệ nghèo thực tế là $y = 12{,}8\\%$ (Slide 26, 36–37).<br>" +
           "a) Tính giá trị dự báo $\\hat{y}$ và phần dư $e$ cho bang Rhode Island.<br>" +
           "b) Diễn giải ý nghĩa của dấu phần dư vừa tìm được.",
        sol: "<b>Lời giải chi tiết theo Slide Week 04 (trang 37):</b><br>" +
             "a) Giá trị dự báo của mô hình (Fitted value):<br>" +
             "   $$\\hat{y} = 64{,}68 - 0{,}62 \\times 81 = 64{,}68 - 50{,}22 = 14{,}46\\%$$<br>" +
             "   Phần dư (Residual):<br>" +
             "   $$e = y - \\hat{y} = 12{,}8\\% - 14{,}46\\% = -1{,}66\\%$$<br>" +
             "b) <b>Ý nghĩa thực tế:</b> Phần dư mang dấu âm ($e = -1{,}66\\%$) chứng tỏ tỉ lệ nghèo thực tế của bang Rhode Island thấp hơn $1{,}66\\%$ so với mức nghèo mà mô hình dự đoán dựa trên tỉ lệ học vấn."
      }
    
    ],
    pitfalls: [
      {
        bad: "Tính phần dư bằng cách lấy Dự đoán trừ Quan sát: $e = \\hat{y} - y$.",
        good: "Luôn nhớ quy tắc: Phần dư = Quan sát thật TRỪ ĐI Dự đoán: $e = y - \\hat{y}$!"
      },
      {
        bad: "Nghĩ rằng nếu hệ số tương quan $r = -0{,}92$ thì mối quan hệ giữa $X$ và $Y$ là rất yếu vì $r$ mang số âm.",
        good: "Dấu âm chỉ cho biết chiều nghịch! Độ lớn $|r| = 0{,}92$ rất gần 1, chứng tỏ đây là một mối quan hệ tuyến tính CỰC KỲ MẠNH."
      }
    ],
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Nếu hệ số tương quan tuyến tính mẫu $r = 0$, ta có thể kết luận rằng:",
            "opts": [
                  "Phương sai của $y$ bằng 0",
                  "Không có mối quan hệ tương quan tuyến tính giữa $x$ và $y$",
                  "Hai biến hoàn toàn độc lập và không có bất kỳ quan hệ nào",
                  "Đường hồi quy có hệ số góc bằng 1"
            ],
            "ans": 1,
            "fb": "Chính xác! $r = 0$ chỉ khẳng định không có quan hệ tuyến tính, hai biến vẫn có thể phụ thuộc phi tuyến hoàn hảo (ví dụ: $y = x^2$ đối xứng qua 0)."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Trong mô hình OLS $\\hat{y} = b_0 + b_1 x$, nếu hệ số góc $b_1 = -1{,}5$, điều này có nghĩa là:",
            "opts": [
                  "Khi $x$ tăng thêm 1 đơn vị, giá trị $y$ chắc chắn giảm chính xác 1,5 đơn vị ở mọi quan sát",
                  "Hệ số xác định $R^2$ là một số âm",
                  "Hệ số tương quan $r$ chắc chắn bằng $-1{,}5$",
                  "Khi $x$ tăng thêm 1 đơn vị, giá trị trung bình dự báo của $y$ giảm đi 1,5 đơn vị"
            ],
            "ans": 3,
            "fb": "Đúng! $b_1$ phản ánh mức thay đổi trung bình của giá trị dự báo $\\hat{y}$, không phải giá trị thực tế của từng cá thể."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Cho phương trình hồi quy mẫu $\\hat{y} = 10 + 2x$. Tại điểm quan sát thực tế $(x_i = 4, y_i = 15)$, phần dư (Residual) $e_i = y_i - \\hat{y}_i$ có giá trị bằng:",
            "opts": [
                  "$-3$",
                  "$18$",
                  "$0$",
                  "$3$"
            ],
            "ans": 0,
            "fb": "Chính xác! Giá trị dự báo $\\hat{y}_i = 10 + 2(4) = 18$. Phần dư $e_i = y_i - \\hat{y}_i = 15 - 18 = -3$."
      }
],
    final_quiz: {
      q: "Phương trình hồi quy là $\\hat{y} = 5 + 2x$. Tại điểm dữ liệu có $x = 3$, giá trị quan sát thực tế là $y = 10$. Phần dư tại điểm này bằng bao nhiêu?",
      opts: [
        "-1",
        "+1",
        "11",
        "-11"
      ],
      ans: 0,
      fb: [
        "Chính xác! Giá trị dự đoán: $\\hat{y} = 5 + 2(3) = 11$. Phần dư: $e = y - \\hat{y} = 10 - 11 = -1$.",
        "Sai! Bạn đã lấy nhầm Dự đoán trừ Quan sát ($11 - 10 = 1$). Công thức chuẩn là Quan sát trừ Dự đoán ($10 - 11 = -1$).",
        "Sai! 11 là giá trị dự đoán $\\hat{y}$, không phải phần dư.",
        "Sai! Tính toán nhầm dấu."
      ]
    }
  },

  {
    id: "A5",
    cluster: "A",
    title: "Hồi quy tuyến tính bội cơ bản: Biến chỉ báo & Mức tham chiếu",
    sources: "Slide Week 04 (tr. 76–99); Stat20 Mục 2.12",
    ref: {
      "slide_file": "week04.pdf",
      "slide_name": "Tuần 04 — Hồi quy tuyến tính nâng cao",
      "pages": "Slide 76 – 99",
      "page_start": 76,
      "section": "Phần 3: Hồi quy với biến phân loại & Biến chỉ báo (Dummy Variables) (Slide 76–99)",
      "stat20": "Stat20 Mục 2.12 (Regression with Categorical Predictors)",
      "key_points": [
            "Biến chỉ báo Dummy: Nhận giá trị 1 nếu đối tượng thuộc nhóm, và 0 nếu ngược lại",
            "Mức tham chiếu (Baseline / Reference level): Nhóm bị khuyết hệ số, đóng vai trò mốc so sánh",
            "Ý nghĩa hệ số góc: Chênh lệch trung bình của nhóm chỉ báo so với nhóm tham chiếu"
      ],
      "remind": "Nếu bạn còn lúng túng khi viết phương trình hồi quy có biến Dummy hoặc đọc bảng output, hãy xem lại Slide Week 04 các trang 78–92."
},
    desc: "Mở rộng sang mô hình nhiều biến giải thích, cách diễn giải hệ số khi có mặt biến phân loại thông qua Biến chỉ báo (Dummy variable 0/1) và Mức tham chiếu.",
    steps: [
      {
        t: "Mô hình hồi quy tuyến tính bội (Multiple Regression)",
        c: `<p>Trong thực tế, một biến kết quả $Y$ thường chịu ảnh hưởng của nhiều yếu tố cùng lúc. Mô hình hồi quy bội có dạng:</p>
            $$\\hat{y} = b_0 + b_1 x_1 + b_2 x_2 + \\dots + b_k x_k$$
            <p><b>Cách đọc hệ số góc $b_j$:</b> $b_j$ đại diện cho mức thay đổi dự đoán của $Y$ khi biến $x_j$ tăng $1$ đơn vị, <b>với điều kiện TẤT CẢ các biến còn lại trong mô hình ĐƯỢC GIỮ NGUYÊN (ceteris paribus)</b>.</p>
            <div class="tip-box">Cụm từ <i>&quot;khi các biến khác không đổi&quot;</i> là câu thần chú bắt buộc phải có trong câu trả lời tự luận để đạt điểm tối đa!</div>`
      },
      {
        t: "Đưa biến phân loại vào hồi quy: Biến chỉ báo (Dummy Variable)",
        c: `<p>Một biến phân loại (ví dụ: Giới tính, Chuyên ngành) không thể đưa trực tiếp chữ cái vào phương trình toán. Ta phải mã hóa nó thành <b>Biến chỉ báo (Indicator / Dummy Variable)</b> nhận giá trị $0$ hoặc $1$:</p>
            <ul>
              <li>Chọn một nhóm làm <b>Mức tham chiếu (Reference Level / Baseline)</b>: Nhóm này được gán giá trị $0$.</li>
              <li>Nhóm còn lại được gán giá trị $1$.</li>
            </ul>
            <p><b>Ví dụ:</b> Biến Ngành học có 2 mức: <i>Khác</i> (gán $d = 0$, mức tham chiếu) và <i>CNTT</i> (gán $d = 1$). Phương trình hồi quy điểm số:</p>
            $$\\hat{y} = 10 + 2{,}5 \\cdot (\\text{Giờ học}) + 4{,}0 \\cdot d_{\\text{CNTT}}$$`
      },
      {
        t: "Cách giải thích hệ số của Biến chỉ báo",
        c: `<p>Trong phương trình trên:</p>
            <ul>
              <li>Với sinh viên ngành Khác ($d_{\\text{CNTT}} = 0$):
                  $$\\hat{y} = 10 + 2{,}5 \\cdot (\\text{Giờ học}) + 4{,}0(0) = 10 + 2{,}5 \\cdot (\\text{Giờ học})$$
              </li>
              <li>Với sinh viên ngành CNTT ($d_{\\text{CNTT}} = 1$):
                  $$\\hat{y} = 10 + 2{,}5 \\cdot (\\text{Giờ học}) + 4{,}0(1) = 14 + 2{,}5 \\cdot (\\text{Giờ học})$$
              </li>
            </ul>
            <p><b>Ý nghĩa hệ số $+4{,}0$:</b> Khi có <i>cùng số giờ học như nhau</i>, sinh viên ngành CNTT được dự đoán có điểm số cao hơn sinh viên ở mức tham chiếu (ngành Khác) trung bình là $4{,}0$ điểm!</p>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 04 — W04-Q04 & W04-WP03] Mô hình Giá sách và Biến chỉ báo Dummy",
        q: "Mô hình dự đoán giá bán của sách giáo khoa (USD) theo thể tích cuốn sách ($x$, $\\text{cm}^3$) và loại bìa (Slide 58–61) có dạng:<br>" +
           "$$\\widehat{\\text{price}} = 1{,}08 + 0{,}016 \\times \\text{volume} - 1{,}84 \\times D_{\\text{softback}}$$<br>" +
           "Trong đó biến chỉ báo $D_{\\text{softback}} = 1$ nếu là sách bìa mềm, và bằng $0$ nếu là sách bìa cứng. Hãy xác định mức tham chiếu (Baseline) và giải thích ý nghĩa hệ số $-1{,}84$.",
        sol: "<b>Phân tích chuẩn mực theo Slide Week 04 (trang 59 & 61):</b><br>" +
             "1. <b>Mức tham chiếu (Baseline):</b> Là nhóm có $D_{\\text{softback}} = 0$, tức là <b>Sách bìa cứng (Hardcover)</b>.<br>" +
             "2. <b>Ý nghĩa hệ số $-1{,}84$:</b> Khi so sánh hai cuốn sách có <b>cùng thể tích</b> (giữ `volume` cố định), cuốn sách bìa mềm được mô hình dự đoán có giá bán <b>thấp hơn trung bình 1,84 USD</b> so với cuốn sách bìa cứng."
      },
      {
        level: "Trung bình",
        t: "[Slide Week 04 — W04-EX05] Tính Giá trị dự báo cho Sách bìa mềm",
        q: "Một cuốn sách giáo trình bìa mềm có thể tích đo được là $\\text{volume} = 600\\text{ cm}^3$ (Slide 62–63). Dựa vào phương trình hồi quy trên, hãy tính giá bán dự báo của cuốn sách này.",
        sol: "<b>Lời giải chi tiết theo Slide Week 04 (trang 63):</b><br>" +
             "1. Vì cuốn sách là bìa mềm nên biến chỉ báo nhận giá trị $D_{\\text{softback}} = 1$.<br>" +
             "2. Thay $\\text{volume} = 600$ và $D_{\\text{softback}} = 1$ vào phương trình:<br>" +
             "   $$\\widehat{\\text{price}} = 1{,}08 + 0{,}016 \\times 600 - 1{,}84 \\times 1$$<br>" +
             "   $$\\widehat{\\text{price}} = 1{,}08 + 9{,}60 - 1{,}84 = 8{,}84 \\text{ USD}$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 04 — W04-Q05 & W04-CASE01] Mô hình Zagat: Nguyên tắc 'Giữ biến khác cố định'",
        q: "Dữ liệu khảo sát nhà hàng Zagat (Slide 64–66, 92–94) cho phương trình dự đoán giá bữa ăn (USD):<br>" +
           "$$\\widehat{\\text{price}} = -52{,}35 + 1{,}64 \\times \\text{food} + 1{,}89 \\times \\text{decor}$$<br>" +
           "Trong đó `food` và `decor` là điểm số đánh giá từ 1 đến 30.<br>" +
           "a) Diễn giải hệ số $1{,}64$ của biến `food`.<br>" +
           "b) Hai nhà hàng A và B có cùng điểm trang trí `decor` = 20. Nhà hàng A có điểm món ăn `food` cao hơn nhà hàng B là 3 điểm. Dự đoán giá bữa ăn ở nhà hàng nào đắt hơn và đắt hơn bao nhiêu?",
        sol: "<b>Phân tích theo Slide Week 04 (trang 66 & 94):</b><br>" +
             "a) <b>Diễn giải hệ số 1,64:</b> Khi so sánh hai nhà hàng có <b>cùng điểm trang trí decor</b>, nhà hàng nào có điểm món ăn food cao hơn 1 điểm thì giá bữa ăn dự báo trung bình cao hơn $1{,}64$ USD.<br>" +
             "b) Vì hai nhà hàng có cùng điểm `decor`, chênh lệch giá dự báo hoàn toàn do chênh lệch điểm `food` quyết định:<br>" +
             "   $$\\Delta \\widehat{\\text{price}} = 1{,}64 \\times \\Delta \\text{food} = 1{,}64 \\times 3 = 4{,}92 \\text{ USD}$$<br>" +
             "   Nhà hàng A được dự báo có giá đắt hơn nhà hàng B đúng $4{,}92$ USD."
      }
    
    ],
    pitfalls: [
      {
        bad: "Diễn giải hệ số $b_1$ trong hồi quy bội mà quên nói cụm từ 'các biến khác giữ nguyên'.",
        good: "Trong bài thi tự luận, thiếu cụm từ 'khi các biến giải thích khác không thay đổi' sẽ bị trừ ngay một nửa số điểm của câu đó!"
      },
      {
        bad: "Nhầm lẫn mức tham chiếu: gán giá trị 1 cho mức tham chiếu.",
        good: "Mức tham chiếu (Baseline) luôn là mức được gán giá trị 0. Hệ số của các biến chỉ báo đo độ chênh lệch so với mức tham chiếu này."
      }
    ],
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Khi đưa một biến phân loại có $k = 4$ mức (ví dụ: Năm 1, Năm 2, Năm 3, Năm 4) vào mô hình hồi quy tuyến tính, ta cần tạo ra bao nhiêu biến chỉ báo (Dummy variables)?",
            "opts": [
                  "$4$ biến chỉ báo",
                  "$1$ biến chỉ báo",
                  "$2$ biến chỉ báo",
                  "$3$ biến chỉ báo"
            ],
            "ans": 3,
            "fb": "Chính xác! Luôn cần $k - 1$ biến chỉ báo, mức còn lại được chọn làm mức tham chiếu (Reference level) để tránh hiện tượng đa cộng tuyến hoàn hảo."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Xét mô hình $\\hat{y} = 20 + 5x + 8 D_{Nam}$, trong đó $D_{Nam} = 1$ nếu là Nam và $0$ nếu là Nữ. Mức chênh lệch về tung độ gốc giữa Nam và Nữ là:",
            "opts": [
                  "$8$ đơn vị",
                  "$28$ đơn vị",
                  "$5$ đơn vị",
                  "$20$ đơn vị"
            ],
            "ans": 0,
            "fb": "Đúng! Hệ số của biến chỉ báo $8$ chính là độ dịch chuyển song song của đường hồi quy nhóm Nam so với nhóm tham chiếu Nữ."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Nếu một nhà nghiên cứu cố tình đưa cả 4 biến chỉ báo cho 4 mùa trong năm vào mô hình hồi quy có hệ số chặn $b_0$, ma trận dữ liệu sẽ gặp hiện tượng gì?",
            "opts": [
                  "Hệ số xác định $R^2$ vượt quá 1",
                  "Độ lệch chuẩn của phần dư bằng 0",
                  "Bẫy biến giả (Dummy variable trap) — ma trận bị suy biến không thể nghịch đảo",
                  "Hệ số góc của các biến bị đổi dấu"
            ],
            "ans": 2,
            "fb": "Chính xác! Vì tổng 4 biến chỉ báo luôn bằng 1 (bằng cột hệ số chặn), tạo ra mối quan hệ cộng tuyến hoàn hảo khiến phần mềm báo lỗi singular matrix."
      }
],
    final_quiz: {
      q: "Mô hình hồi quy: $\\hat{y} = 15 + 3x_1 - 4d_2$, trong đó $d_2 = 1$ nếu là nhân viên thời vụ, $0$ nếu là nhân viên chính thức. Con số -4 có ý nghĩa gì?",
      opts: [
        "Với cùng giá trị x1, nhân viên thời vụ có y dự đoán thấp hơn nhân viên chính thức 4 đơn vị",
        "Khi x1 tăng 1 đơn vị, y dự đoán giảm 4 đơn vị",
        "Nhân viên chính thức có y dự đoán thấp hơn nhân viên thời vụ 4 đơn vị",
        "Mức tham chiếu là nhân viên thời vụ"
      ],
      ans: 0,
      fb: [
        "Chính xác! Mức tham chiếu là nhân viên chính thức ($d_2 = 0$). Hệ số -4 nghĩa là khi $d_2 = 1$ (thời vụ), giá trị dự đoán bị giảm đi 4 đơn vị so với chính thức khi có cùng $x_1$.",
        "Sai! Con số -4 gắn với $d_2$, không phải tốc độ thay đổi theo $x_1$.",
        "Sai! Ngược chiều so sánh (thời vụ thấp hơn chính thức, không phải chính thức thấp hơn thời vụ).",
        "Sai! Mức tham chiếu là nhân viên chính thức (nhóm mang giá trị 0)."
      ]
    }
  }
];

if (typeof module !== 'undefined' && module.exports) {
  module.exports = CUM_A;
}
