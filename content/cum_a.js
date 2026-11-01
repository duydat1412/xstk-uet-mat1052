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
        q: "Xác định loại của biến: 'Số lỗi cú pháp trong một bài nộp code của sinh viên'.",
        sol: "<b>Phân tích:</b> Số lỗi cú pháp là kết quả của việc đếm (0 lỗi, 1 lỗi, 2 lỗi,...), chỉ nhận các giá trị nguyên không âm tách rời và phép tính trung bình số lỗi có ý nghĩa thực tế.<br><b>Kết luận:</b> Biến số, loại <b>Rời rạc (Discrete Numerical)</b>."
      },
      {
        level: "Trung bình",
        q: "Biến 'Mức độ hài lòng của khách hàng' với các mức: 'Rất không hài lòng', 'Bình thường', 'Hài lòng', 'Rất hài lòng' thuộc loại nào?",
        sol: "<b>Phân tích:</b> Đây là các nhãn chữ (biến phân loại), nhưng giữa các nhãn có thứ tự mức độ tăng dần rõ rệt ('Rất không hài lòng' &lt; 'Hài lòng').<br><b>Kết luận:</b> Biến phân loại, loại <b>Thứ bậc (Ordinal Categorical)</b>."
      },
      {
        level: "Vận dụng",
        q: "Một nhân viên y tế ghi nhận: (1) Mã định danh căn cước công dân; (2) Nồng độ oxy trong máu SpO2 (đo bằng %); (3) Giai đoạn tiến triển bệnh (Giai đoạn I, II, III). Hãy phân loại chính xác từng biến.",
        sol: "<b>Phân tích từng biến:</b><br>" +
             "1. Căn cước công dân: Dãy số nhưng chỉ dùng để nhận diện người, tính trung bình vô nghĩa $\rightarrow$ <b>Phân loại Định danh (Nominal)</b>.<br>" +
             "2. Nồng độ SpO2: Đo lường liên tục (có thể là 97,5%, 98,2%) $\rightarrow$ <b>Biến số Liên tục (Continuous Numerical)</b>.<br>" +
             "3. Giai đoạn bệnh: Nhóm bệnh có mức độ nghiêm trọng tăng dần $\rightarrow$ <b>Phân loại Thứ bậc (Ordinal)</b>."
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
        c: `<p>Muốn xem xét mối liên hệ giữa hai biến phân loại, ta xếp chúng vào <b>Bảng liên hợp (Two-way Contingency Table)</b>: một biến đặt theo hàng, một biến đặt theo cột.</p>
            <table class="data-table">
              <thead><tr><th>Năm học \\ Đi làm thêm</th><th>Có đi làm thêm</th><th>Không đi làm</th><th>Tổng hàng</th></tr></thead>
              <tbody>
                <tr><td><b>Năm 1</b></td><td>6</td><td>24</td><td><b>30</b></td></tr>
                <tr><td><b>Năm 2</b></td><td>10</td><td>10</td><td><b>20</b></td></tr>
                <tr><td><b>Tổng cột</b></td><td><b>16</b></td><td><b>34</b></td><td><b>50</b></td></tr>
              </tbody>
            </table>
            <p>Trong bảng trên: Ô giao nhau cho biết tần số kết hợp (ví dụ: có $10$ sinh viên vừa là Năm 2, vừa có đi làm thêm). Tổng hàng và tổng cột đều phải cộng ra tổng chung $n = 50$.</p>`
      },
      {
        t: "Kỹ năng sống còn: Chọn đúng MẪU SỐ khi tính tỉ lệ",
        c: `<p>Trong bảng liên hợp, đề thi thường yêu cầu tính 3 loại tỉ lệ khác nhau. Điểm mấu chốt là <b>xác định đúng MẪU SỐ</b>:</p>
            <ol>
              <li><b>Tỉ lệ trên toàn bộ (Joint Proportion)</b>: Mẫu số là <b>Tổng chung toàn bảng (50)</b>.<br>
                  Ví dụ: Tỉ lệ sinh viên vừa học Năm 2 vừa đi làm thêm = $\\frac{10}{50} = 20\\%$.
              </li>
              <li><b>Tỉ lệ có điều kiện theo hàng (Row Conditional Proportion)</b>: Mẫu số là <b>Tổng hàng</b>.<br>
                  Ví dụ: <i>Trong số các sinh viên Năm 2</i>, tỉ lệ đi làm thêm = $\\frac{10}{20} = 50\\%$.
              </li>
              <li><b>Tỉ lệ có điều kiện theo cột (Column Conditional Proportion)</b>: Mẫu số là <b>Tổng cột</b>.<br>
                  Ví dụ: <i>Trong số những người có đi làm thêm</i>, tỉ lệ sinh viên Năm 2 = $\\frac{10}{16} = 62{,}5\\%$.
              </li>
            </ol>
            <div class="tip-box"><b>Mẹo tìm mẫu số trong câu hỏi:</b> Hãy tìm cụm từ <i>&quot;Trong số...&quot;</i>, <i>&quot;Tính trong nhóm...&quot;</i> hoặc <i>&quot;Biết rằng...&quot;</i>. Đối tượng đứng ngay sau cụm từ đó chính là <b>MẪU SỐ</b>!</div>`
      },
      {
        t: "Làm thế nào để biết hai biến có liên hệ với nhau?",
        c: `<p>Hai biến phân loại được coi là <b>có mối liên hệ (associated)</b> nếu sự phân bố của biến này thay đổi khi ta biết thông tin về biến kia.</p>
            <p>Trong ví dụ trên, hãy so sánh tỉ lệ đi làm thêm theo từng năm học:</p>
            <ul>
              <li>Ở sinh viên Năm 1: Tỉ lệ đi làm thêm là $\\frac{6}{30} = 20\\%$.</li>
              <li>Ở sinh viên Năm 2: Tỉ lệ đi làm thêm là $\\frac{10}{20} = 50\\%$.</li>
            </ul>
            <p>Vì $50\\% \\neq 20\\%$ (chênh lệch rất lớn), ta kết luận: <b>Năm học có liên hệ với xu hướng đi làm thêm</b> (sinh viên năm trên có xu hướng đi làm nhiều hơn). Nếu hai tỉ lệ này bằng nhau hoặc xấp xỉ nhau, ta nói hai biến không có mối liên hệ.</p>
            <div class="warn-box"><b>Lưu ý quan trọng:</b> Tỉ lệ có điều kiện theo hàng chính là bản chất của <b>Xác suất có điều kiện</b> $P(\\text{Đi làm} \\mid \\text{Năm 2}) = \\frac{10}{20} = 0{,}5$ mà chúng ta sẽ học ở Cụm B!</div>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        q: "Một lớp học có 20 sinh viên CNTT, 18 sinh viên Điện tử và 12 sinh viên Cơ học. Tính tỉ lệ sinh viên ngành CNTT trong lớp.",
        sol: "<b>Bước 1:</b> Tính tổng số sinh viên: $n = 20 + 18 + 12 = 50$.<br>" +
             "<b>Bước 2:</b> Tỉ lệ sinh viên CNTT = $\\frac{20}{50} = 0{,}40 = 40\\%$.<br>" +
             "<b>Kết luận:</b> Sinh viên ngành CNTT chiếm 40% sĩ số lớp."
      },
      {
        level: "Trung bình",
        q: "Dựa vào bảng liên hợp ở trên, tính tỉ lệ sinh viên không đi làm thêm trong số các sinh viên Năm 1.",
        sol: "<b>Bước 1:</b> Xác định mẫu số: Cụm từ 'trong số các sinh viên Năm 1' cho biết mẫu số là Tổng hàng Năm 1 = 30.<br>" +
             "<b>Bước 2:</b> Tử số là số sinh viên Năm 1 không đi làm thêm = 24.<br>" +
             "<b>Bước 3:</b> Tỉ lệ = $\\frac{24}{30} = 0{,}80 = 80\\%$.<br>" +
             "<b>Kết luận:</b> 80% sinh viên Năm 1 không đi làm thêm."
      },
      {
        level: "Vận dụng",
        q: "Dựa vào bảng trên, so sánh hai tỉ lệ: (A) Tỉ lệ sinh viên Năm 1 có đi làm thêm trên toàn trường; (B) Tỉ lệ sinh viên Năm 1 trong nhóm những người có đi làm thêm. Hai tỉ lệ này có bằng nhau không?",
        sol: "<b>Tính tỉ lệ (A):</b> Mẫu số là Tổng toàn bộ 50. Tỉ lệ (A) = $\\frac{6}{50} = 12\\%$.<br>" +
             "<b>Tính tỉ lệ (B):</b> Mẫu số là Tổng cột người có đi làm thêm 16. Tỉ lệ (B) = $\\frac{6}{16} = 37{,}5\\%$.<br>" +
             "<b>Kết luận:</b> Hai tỉ lệ hoàn toàn khác nhau ($12\\% \\neq 37{,}5\\%$). Điều này chứng minh việc chọn nhầm mẫu số sẽ làm sai lệch hoàn toàn kết quả bài toán."
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
        q: "Cho dãy điểm thi của 5 sinh viên: 4, 6, 7, 8, 10. Hãy tính Trung bình, Trung vị và Khoảng biến thiên (Range).",
        sol: "<b>Trung bình:</b> $\\bar{x} = \\frac{4 + 6 + 7 + 8 + 10}{5} = \\frac{35}{5} = 7{,}0$.<br>" +
             "<b>Trung vị:</b> Dãy có 5 số (lẻ), số ở vị trí chính giữa (thứ 3) là $7{,}0$.<br>" +
             "<b>Khoảng biến thiên:</b> $\\text{Range} = 10 - 4 = 6$."
      },
      {
        level: "Trung bình",
        q: "Dãy điểm thi của 11 sinh viên: 4, 6, 7, 7, 8, 8, 8, 9, 9, 10, 18. Tính Median, $Q_1, Q_3, \\text{IQR}$ và kiểm tra xem giá trị 18 có phải là ngoại lai không.",
        sol: "<b>Bước 1:</b> Dãy đã xếp thứ tự gồm 11 số. Số ở giữa (vị trí 6) là $\\text{Median} = 8$.<br>" +
             "<b>Bước 2:</b> Nửa dưới gồm 5 số $[4, 6, 7, 7, 8] \\implies Q_1 = 7$.<br>" +
             "<b>Bước 3:</b> Nửa trên gồm 5 số $[8, 9, 9, 10, 18] \\implies Q_3 = 9$.<br>" +
             "<b>Bước 4:</b> $\\text{IQR} = Q_3 - Q_1 = 9 - 7 = 2$.<br>" +
             "<b>Bước 5:</b> Rào trên = $Q_3 + 1{,}5 \\times \\text{IQR} = 9 + 1{,}5(2) = 12$.<br>" +
             "Vì điểm $18 &gt; 12$, nên $18$ <b>chính xác là một giá trị ngoại lai</b>!"
      },
      {
        level: "Vận dụng",
        q: "Một công ty công nghệ có 10 nhân viên lương 15 triệu/tháng và 1 Giám đốc lương 200 triệu/tháng. Khi báo cáo mức lương tiêu biểu cho ứng viên mới, phòng nhân sự nên dùng Trung bình hay Trung vị? Vì sao?",
        sol: "<b>Tính toán:</b><br>" +
             "- Tổng lương = $10 \\times 15 + 200 = 350$ triệu. Trung bình lương $\\bar{x} = \\frac{350}{11} \\approx 31{,}8$ triệu.<br>" +
             "- Trung vị lương = 15 triệu.<br>" +
             "<b>Phân tích:</b> Phân phối lương bị <b>lệch phải rất nặng</b> do mức lương cực đoan 200 triệu của Giám đốc kéo trung bình lên gần 32 triệu (cao hơn gấp đôi lương của toàn bộ nhân viên).<br>" +
             "<b>Kết luận:</b> Phải dùng <b>Trung vị (15 triệu)</b> vì nó phản ánh trung thực mức lương thực tế của đa số nhân viên mà không bị ngoại lai bóp méo."
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
        q: "Cho đường hồi quy dự đoán điểm thi theo số giờ học: $\\hat{y} = 2 + 1{,}5 x$. Nêu ý nghĩa của con số 1,5.",
        sol: "<b>Phân tích:</b> Con số $1{,}5$ là hệ số góc $b_1$.<br>" +
             "<b>Kết luận:</b> Khi một sinh viên học thêm $1$ giờ ($x$ tăng 1 đơn vị), điểm thi dự đoán của sinh viên đó sẽ tăng thêm $1{,}5$ điểm."
      },
      {
        level: "Trung bình",
        q: "Đường hồi quy dự đoán giá nhà (triệu đồng) theo diện tích ($m^2$) là $\\hat{y} = 200 + 25 x$. Một căn nhà có diện tích $80 m^2$ được bán thực tế với giá $2150$ triệu đồng. Hãy tính giá dự đoán và phần dư.",
        sol: "<b>Bước 1:</b> Tính giá trị dự đoán $\\hat{y}$ khi $x = 80$:<br>" +
             "$$\\hat{y} = 200 + 25(80) = 200 + 2000 = 2200\\text{ (triệu đồng)}$$<br>" +
             "<b>Bước 2:</b> Tính phần dư $e = y - \\hat{y}$:<br>" +
             "$$e = 2150 - 2200 = -50\\text{ (triệu đồng)}$$<br>" +
             "<b>Kết luận:</b> Phần dư âm ($-50$ triệu), nghĩa là căn nhà này được bán rẻ hơn $50$ triệu so với mức giá mà mô hình dự đoán."
      },
      {
        level: "Vận dụng",
        q: "Cho tập dữ liệu 5 điểm: $(1, 2), (2, 3), (3, 5), (4, 7), (5, 8)$. Đường hồi quy tìm được là $\\hat{y} = 0{,}2 + 1{,}6 x$. Hãy tính phần dư tại cả 5 điểm và kiểm tra xem tổng phần dư có bằng 0 không.",
        sol: "<b>Tính phần dư từng điểm:</b><br>" +
             "- Tại $x=1$: $\\hat{y} = 0{,}2 + 1{,}6(1) = 1{,}8 \\implies e_1 = 2 - 1{,}8 = +0{,}2$<br>" +
             "- Tại $x=2$: $\\hat{y} = 0{,}2 + 1{,}6(2) = 3{,}4 \\implies e_2 = 3 - 3{,}4 = -0{,}4$<br>" +
             "- Tại $x=3$: $\\hat{y} = 0{,}2 + 1{,}6(3) = 5{,}0 \\implies e_3 = 5 - 5{,}0 = 0{,}0$<br>" +
             "- Tại $x=4$: $\\hat{y} = 0{,}2 + 1{,}6(4) = 6{,}6 \\implies e_4 = 7 - 6{,}6 = +0{,}4$<br>" +
             "- Tại $x=5$: $\\hat{y} = 0{,}2 + 1{,}6(5) = 8{,}2 \\implies e_5 = 8 - 8{,}2 = -0{,}2$<br>" +
             "<b>Tổng phần dư:</b><br>" +
             "$$\\sum e_i = (+0{,}2) + (-0{,}4) + 0{,}0 + (+0{,}4) + (-0{,}2) = 0{,}00$$<br>" +
             "Đúng theo tính chất toán học của phương pháp OLS!"
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
        q: "Phương trình dự đoán mức lương (triệu/tháng): $\\hat{y} = 12 + 1{,}5 x_1 + 0{,}8 x_2$, trong đó $x_1$ là số năm kinh nghiệm, $x_2$ là số chứng chỉ quốc tế. Diễn giải ý nghĩa con số 1,5.",
        sol: "<b>Phân tích:</b> Con số $1{,}5$ là hệ số trước $x_1$.<br>" +
             "<b>Kết luận chuẩn:</b> Khi số năm kinh nghiệm ($x_1$) tăng thêm $1$ năm, mức lương dự đoán sẽ tăng thêm $1{,}5$ triệu đồng/tháng, <i>với điều kiện số lượng chứng chỉ quốc tế ($x_2$) không thay đổi</i>."
      },
      {
        level: "Trung bình",
        q: "Mô hình giá thuê nhà: $\\hat{y} = 3 + 0{,}08 x_1 + 2 d_{\\text{ĐH}}$, trong đó $x_1$ là diện tích ($m^2$), $d_{\\text{ĐH}} = 1$ nếu có điều hòa, $0$ nếu không có. Một phòng $40 m^2$ có điều hòa được dự đoán giá thuê bao nhiêu?",
        sol: "<b>Bước 1:</b> Xác định các giá trị: $x_1 = 40$, vì có điều hòa nên $d_{\\text{ĐH}} = 1$.<br>" +
             "<b>Bước 2:</b> Thay số vào mô hình:<br>" +
             "$$\\hat{y} = 3 + 0{,}08(40) + 2(1) = 3 + 3{,}2 + 2 = 8{,}2\\text{ (triệu đồng/tháng)}$$<br>" +
             "<b>Kết luận:</b> Giá thuê dự đoán là 8,2 triệu đồng/tháng."
      },
      {
        level: "Vận dụng",
        q: "Với mô hình trên, hai phòng trọ A và B có diện tích bằng nhau là $50 m^2$. Phòng A có điều hòa, phòng B không có điều hòa. Mức giá thuê dự đoán của phòng A chênh lệch so với phòng B bao nhiêu?",
        sol: "<b>Phân tích:</b> Vì hai phòng có cùng diện tích ($x_1$ như nhau), sự chênh lệch giá thuê dự đoán chỉ đến từ biến chỉ báo điều hòa.<br>" +
             "$$\\hat{y}_A - \\hat{y}_B = [3 + 0{,}08(50) + 2(1)] - [3 + 0{,}08(50) + 2(0)] = 2(1) - 2(0) = 2\\text{ (triệu)}$$<br>" +
             "<b>Kết luận:</b> Phòng A có điều hòa được dự đoán giá cao hơn phòng B đúng bằng hệ số $2$ triệu đồng/tháng."
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
