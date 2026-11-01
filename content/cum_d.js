// ==========================================================================
// CỤM D: TỔNG, TRUNG BÌNH, BẤT ĐẲNG THỨC CHEBYSHEV & LUẬT SỐ LỚN YẾU
// Bao gồm: Bài D1, D2, D3, D4
// Nguồn: Slide UET Week 07 (tr. 21–40); Stat20 Chương 4 (Mục 4.13, 4.14)
// Kiểm chứng số học: verify/verify_cum_d.py
// ==========================================================================

const CUM_D = [
  {
    id: "D1",
    cluster: "D",
    title: "Biến ngẫu nhiên i.i.d. & Mô hình chiếc hộp (Box Model)",
    sources: "Slide Week 07 (tr. 21–24); Stat20 Mục 4.13",
    desc: "Mô hình hóa phép thử phức hợp bằng Mô hình chiếc hộp. Khái niệm i.i.d. (độc lập và cùng phân phối) làm nền tảng cho toàn bộ thống kê suy luận.",
    steps: [
      {
        t: "Khái niệm biến ngẫu nhiên i.i.d.",
        c: `<p>Trong thống kê, giả thiết quan trọng nhất khi thu thập dữ liệu là <b>i.i.d. (Independent and Identically Distributed - Độc lập và Cùng phân phối)</b>.</p>
            <p>Các biến ngẫu nhiên $X_1, X_2, \\dots, X_n$ được gọi là <b>i.i.d.</b> nếu:</p>
            <ol>
              <li><b>Cùng phân phối (Identically Distributed)</b>: Mọi biến $X_i$ đều tuân theo cùng một quy luật xác suất, có cùng kỳ vọng $\\mu$ và cùng độ lệch chuẩn $\\sigma$.</li>
              <li><b>Độc lập (Independent)</b>: Giá trị quan sát được của biến này hoàn toàn không làm thay đổi phân phối xác suất của bất kỳ biến nào khác.</li>
            </ol>`
      },
      {
        t: "Mô hình chiếc hộp (The Box Model) của Freedman",
        c: `<p>Mô hình chiếc hộp biểu diễn một phép thử ngẫu nhiên bằng việc <b>rút ngẫu nhiên có hoàn lại $n$ lần từ một chiếc hộp chứa các lá phiếu ghi số</b>:</p>
            <ul>
              <li>Mỗi lá phiếu trong hộp đại diện cho một kết quả có thể nhận được.</li>
              <li>Trung bình của tất cả các số trong hộp là <b>$\\mu$ (Box Average)</b>.</li>
              <li>Độ lệch chuẩn của các số trong hộp là <b>$\\sigma$ (Box SD)</b>.</li>
              <li>Mỗi lần rút thẻ độc lập có hoàn lại cho ta một biến ngẫu nhiên $X_i$ có $E(X_i) = \\mu$ và $\\operatorname{SD}(X_i) = \\sigma$.</li>
            </ul>
            <div class="tip-box">
              <b>Mọi bài toán thực tế đều quy về Mô hình chiếc hộp:</b><br>
              - Tung xúc xắc $n$ lần $\\equiv$ Rút $n$ lần từ hộp chứa $\\{1, 2, 3, 4, 5, 6\\}$.<br>
              - Đếm số mặt ngửa khi tung đồng xu $n$ lần $\\equiv$ Hộp có phiếu $\\{0, 1\\}$.<br>
              - Khảo sát $n$ cử tri $\\equiv$ Hộp có phiếu $\\{1\\}$ (đồng ý) và $\\{0\\}$ (phản đối).
            </div>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        q: "Gieo một con xúc xắc cân đối. Hãy biểu diễn phép thử này dưới dạng Mô hình chiếc hộp và tính trung bình μ cùng độ lệch chuẩn σ của chiếc hộp.",
        sol: "<b>Bước 1:</b> Chiếc hộp chứa 6 lá phiếu: $[1, 2, 3, 4, 5, 6]$. Rút có hoàn lại 1 lá.<br>" +
             "<b>Bước 2:</b> Trung bình của hộp:<br>" +
             "$$\\mu = \\frac{1 + 2 + 3 + 4 + 5 + 6}{6} = \\frac{21}{6} = 3{,}5$$<br>" +
             "<b>Bước 3:</b> Phương sai của hộp (tổng thể):<br>" +
             "$$\\sigma^2 = \\frac{1}{6}\\sum (x - 3{,}5)^2 = \\frac{(-2{,}5)^2 + (-1{,}5)^2 + (-0{,}5)^2 + 0{,}5^2 + 1{,}5^2 + 2{,}5^2}{6} = \\frac{17{,}5}{6} \\approx 2{,}9167$$<br>" +
             "<b>Bước 4:</b> Độ lệch chuẩn: $\\sigma = \\sqrt{2{,}9167} \\approx 1{,}7078$."
      },
      {
        level: "Trung bình",
        q: "Một hộp chứa 10 lá thăm ghi các số: [0, 0, 1, 1, 1, 2, 3, 3, 4, 4] (Slide 27-28). Hãy tính trung bình μ và phương sai σ² của hộp.",
        sol: "<b>Bước 1:</b> Tính trung bình $\\mu$:<br>" +
             "$$\\mu = \\frac{0(2) + 1(3) + 2(1) + 3(2) + 4(2)}{10} = \\frac{0 + 3 + 2 + 6 + 8}{10} = \\frac{19}{10} = 1{,}9$$<br>" +
             "<b>Bước 2:</b> Tính phương sai $\\sigma^2 = \\frac{1}{10}\\sum (x - 1{,}9)^2$:<br>" +
             "- $(0 - 1{,}9)^2 \\times 2 = 3{,}61 \\times 2 = 7{,}22$<br>" +
             "- $(1 - 1{,}9)^2 \\times 3 = 0{,}81 \\times 3 = 2{,}43$<br>" +
             "- $(2 - 1{,}9)^2 \\times 1 = 0{,}01 \\times 1 = 0{,}01$<br>" +
             "- $(3 - 1{,}9)^2 \\times 2 = 1{,}21 \\times 2 = 2{,}42$<br>" +
             "- $(4 - 1{,}9)^2 \\times 2 = 4{,}41 \\times 2 = 8{,}82$<br>" +
             "$$\\sigma^2 = \\frac{7{,}22 + 2{,}43 + 0{,}01 + 2{,}42 + 8{,}82}{10} = \\frac{20{,}90}{10} = 2{,}09$$<br>" +
             "$\\implies \\sigma = \\sqrt{2{,}09} \\approx 1{,}4457$."
      },
      {
        level: "Vận dụng",
        q: "Trong trò chơi Roulette kiểu Mỹ, bánh xe có 38 ô: 18 ô Đỏ, 18 ô Đen, và 2 ô Xanh (0, 00). Nếu đặt 1 USD vào Đỏ: trúng thì nhận lại 2 USD (lãi 1 USD); trượt thì mất 1 USD (lãi -1 USD). Hãy lập mô hình chiếc hộp biểu diễn số tiền lãi cho 1 ván chơi.",
        sol: "<b>Phân tích:</b><br>" +
             "- Số phiếu thắng (ghi $+1$): $18$ phiếu.<br>" +
             "- Số phiếu thua (ghi $-1$): $18 + 2 = 20$ phiếu.<br>" +
             "- Tổng số phiếu: $38$ phiếu.<br>" +
             "<b>Tính kỳ vọng của chiếc hộp:</b><br>" +
             "$$\\mu = (+1) \\times \\frac{18}{38} + (-1) \\times \\frac{20}{38} = -\\frac{2}{38} = -\\frac{1}{19} \\approx -0{,}0526\\text{ USD}$$<br>" +
             "<b>Kết luận:</b> Mỗi ván cược 1 USD, người chơi kỳ vọng mất trung bình $5{,}26$ cent. Đây chính là lợi nhuận kỳ vọng của sòng bạc (House Edge)!"
      }
    ],
    pitfalls: [
      {
        bad: "Nhầm lẫn giữa rút CÓ HOÀN LẠI và KHÔNG HOÀN LẠI trong mô hình chiếc hộp.",
        good: "Mô hình chiếc hộp chuẩn của Freedman BẮT BUỘC phải là rút CÓ HOÀN LẠI để đảm bảo các lần rút hoàn toàn độc lập và cùng phân phối (i.i.d.)!"
      },
      {
        bad: "Tính trung bình của hộp bằng cách cộng các giá trị khác nhau rồi chia cho số loại giá trị (bỏ qua tần số xuất hiện).",
        good: "Phải nhân với tần số xuất hiện của từng lá phiếu (tính trung bình có trọng số)!"
      }
    ],
    final_quiz: {
      q: "Điều kiện nào sau đây là BẮT BUỘC để các lần rút từ chiếc hộp được coi là các biến ngẫu nhiên i.i.d.?",
      opts: [
        "Rút ngẫu nhiên CÓ HOÀN LẠI",
        "Rút ngẫu nhiên KHÔNG HOÀN LẠI",
        "Chiếc hộp phải chứa các số tự nhiên liên tiếp",
        "Số lần rút n phải bằng số lá phiếu trong hộp"
      ],
      ans: 0,
      fb: [
        "Chính xác! Rút có hoàn lại đảm bảo xác suất và thành phần hộp ở mọi lần rút đều giống hệt nhau (cùng phân phối) và không ảnh hưởng lẫn nhau (độc lập).",
        "Sai! Rút không hoàn lại làm thay đổi thành phần trong hộp ở các lần sau, khiến các biến phụ thuộc lẫn nhau.",
        "Sai! Hộp có thể chứa bất kỳ số thực nào.",
        "Sai! Số lần rút n hoàn toàn độc lập với quy mô hộp."
      ]
    }
  },

  {
    id: "D2",
    cluster: "D",
    title: "Tổng và Trung bình của các biến i.i.d.: Quy tắc căn bậc hai",
    sources: "Slide Week 07 (tr. 25–32); Stat20 Mục 4.14",
    desc: "Nắm vững hai công thức quan trọng nhất của học phần: Kỳ vọng và Độ lệch chuẩn của Tổng Sn (σ√n) và Trung bình mẫu X̄n (σ/√n). Quy tắc căn bậc hai.",
    steps: [
      {
        t: "Hai công thức cốt tử: Tổng $S_n$ vs Trung bình $\\bar{X}_n$",
        c: `<p>Cho $X_1, X_2, \\dots, X_n$ là các biến ngẫu nhiên i.i.d. với trung bình $\\mu$ và độ lệch chuẩn $\\sigma$:</p>
            <table class="data-table">
              <thead><tr><th>Đại lượng mẫu</th><th>Ký hiệu & Định nghĩa</th><th>Kỳ vọng</th><th>Phương sai</th><th>Độ lệch chuẩn (SD)</th></tr></thead>
              <tbody>
                <tr><td><b>Tổng mẫu</b></td><td>$$S_n = \\sum_{i=1}^n X_i$$</td><td>$$E(S_n) = n \\cdot \\mu$$</td><td>$$\\operatorname{Var}(S_n) = n \\cdot \\sigma^2$$</td><td>$$\\operatorname{SD}(S_n) = \\sigma \\sqrt{n}$$</td></tr>
                <tr><td><b>Trung bình mẫu</b></td><td>$$\\bar{X}_n = \\frac{S_n}{n}$$</td><td>$$E(\\bar{X}_n) = \\mu$$</td><td>$$\\operatorname{Var}(\\bar{X}_n) = \\frac{\\sigma^2}{n}$$</td><td>$$\\operatorname{SD}(\\bar{X}_n) = \\frac{\\sigma}{\\sqrt{n}}$$</td></tr>
              </tbody>
            </table>
            <div class="tip-box">
              <b>Bản chất đối nghịch cần ghi nhớ:</b><br>
              - <b>Tổng $S_n$</b>: Độ lệch chuẩn tăng theo $\\sqrt{n}$ $\\rightarrow$ Tổng càng ngày càng &quot;dãn rộng&quot; ra.<br>
              - <b>Trung bình mẫu $\\bar{X}_n$</b>: Độ lệch chuẩn giảm theo $\\frac{1}{\\sqrt{n}}$ $\\rightarrow$ Trung bình càng ngày càng &quot;co cụm xít xao&quot; quanh tâm $\\mu$. Càng thu thập nhiều dữ liệu, trung bình mẫu càng chính xác!
            </div>`
      },
      {
        t: "Quy tắc Căn bậc hai (The Square Root Law)",
        c: `<p>Để độ lệch chuẩn của trung bình mẫu $\\operatorname{SD}(\\bar{X}_n) = \\frac{\\sigma}{\\sqrt{n}}$ <b>giảm đi một nửa</b> (tức độ chính xác tăng gấp đôi), ta cần làm gì với cỡ mẫu $n$?</p>
            $$\\frac{\\sigma}{\\sqrt{n_{\\text{mới}}}} = \\frac{1}{2} \\cdot \\frac{\\sigma}{\\sqrt{n}} \\implies \\sqrt{n_{\\text{mới}}} = 2\\sqrt{n} \\implies n_{\\text{mới}} = 4n$$
            <div class="warn-box">
              <b>CẠM BẪY TRẮC NGHIỆM:</b><br>
              Muốn sai số giảm đi $m$ lần, cỡ mẫu phải tăng lên **$m^2$ lần**! Chứ KHÔNG PHẢI tăng $m$ lần.<br>
              - Giảm sai số 2 lần $\\implies$ Tăng cỡ mẫu gấp $4$ lần.<br>
              - Giảm sai số 3 lần $\\implies$ Tăng cỡ mẫu gấp $9$ lần.<br>
              - Giảm sai số 10 lần $\\implies$ Tăng cỡ mẫu gấp $100$ lần!
            </div>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        q: "Một chiếc hộp có độ lệch chuẩn σ = 2. Rút ngẫu nhiên độc lập có hoàn lại 100 lần. Hãy tính độ lệch chuẩn của Tổng các lần rút và của Trung bình các lần rút.",
        sol: "<b>Bước 1:</b> Độ lệch chuẩn của Tổng $S_{100}$:<br>" +
             "$$\\operatorname{SD}(S_{100}) = \\sigma \\sqrt{n} = 2 \\times \\sqrt{100} = 2 \\times 10 = 20$$<br>" +
             "<b>Bước 2:</b> Độ lệch chuẩn của Trung bình $\\bar{X}_{100}$:<br>" +
             "$$\\operatorname{SD}(\\bar{X}_{100}) = \\frac{\\sigma}{\\sqrt{n}} = \\frac{2}{\\sqrt{100}} = \\frac{2}{10} = 0{,}2$$."
      },
      {
        level: "Trung bình",
        q: "Tung một con xúc xắc cân đối 100 lần độc lập. Biết mỗi lần tung có kỳ vọng μ = 3,5 và độ lệch chuẩn σ ≈ 1,71. Tính kỳ vọng và độ lệch chuẩn của tổng số chấm sau 100 lần tung.",
        sol: "<b>Bước 1:</b> Kỳ vọng của tổng:<br>" +
             "$$E(S_{100}) = n \\cdot \\mu = 100 \\times 3{,}5 = 350\\text{ (chấm)}$$<br>" +
             "<b>Bước 2:</b> Độ lệch chuẩn của tổng:<br>" +
             "$$\\operatorname{SD}(S_{100}) = \\sigma \\sqrt{n} = 1{,}71 \\times \\sqrt{100} = 1{,}71 \\times 10 = 17{,}1\\text{ (chấm)}$$."
      },
      {
        level: "Vận dụng",
        q: "Một viện nghiên cứu muốn ước lượng mức chi tiêu trung bình của sinh viên với độ lệch chuẩn của trung bình mẫu là 50 nghìn đồng. Ban đầu họ khảo sát 100 sinh viên và thấy độ lệch chuẩn mẫu đạt 150 nghìn đồng. Họ cần khảo sát TỔNG CỘNG bao nhiêu sinh viên để đạt mục tiêu trên?",
        sol: "<b>Phân tích:</b><br>" +
             "- Độ lệch chuẩn hiện tại của trung bình mẫu là $150$ nghìn. Mục tiêu là đưa về $50$ nghìn (giảm đi $150/50 = 3$ lần).<br>" +
             "- Theo quy tắc căn bậc hai, muốn độ lệch chuẩn trung bình giảm đi 3 lần, cỡ mẫu mới phải gấp $3^2 = 9$ lần cỡ mẫu ban đầu:<br>" +
             "$$n_{\\text{mới}} = 100 \\times 3^2 = 100 \\times 9 = 900\\text{ (sinh viên)}$$<br>" +
             "<b>Kết luận:</b> Cần khảo sát tổng cộng 900 sinh viên."
      }
    ],
    pitfalls: [
      {
        bad: "Nhầm lẫn giữa công thức của Tổng (nhân căn n) và của Trung bình (chia căn n).",
        good: "Tổng thì cộng dồn nên phải to ra (nhân √n). Trung bình thì chia đều nên phải nhỏ lại (chia √n)!"
      },
      {
        bad: "Cho rằng muốn sai số giảm 2 lần thì chỉ cần khảo sát thêm gấp đôi số người.",
        good: "Sai số giảm theo √n, nên muốn giảm 2 lần bắt buộc phải tăng gấp 4 lần số người!"
      }
    ],
    final_quiz: {
      q: "Muốn độ lệch chuẩn của trung bình mẫu giảm đi một nửa (giảm 2 lần), cần tăng cỡ mẫu n lên bao nhiêu lần?",
      opts: [
        "4 lần",
        "2 lần",
        "8 lần",
        "√2 lần"
      ],
      ans: 0,
      fb: [
        "Chính xác! Theo công thức SD(X̄) = σ / √n, muốn SD giảm một nửa thì √n phải tăng gấp đôi, nghĩa là n phải tăng 2^2 = 4 lần.",
        "Sai! Nếu n tăng 2 lần, SD chỉ giảm √2 ≈ 1,414 lần.",
        "Sai! 8 lần là 2^3.",
        "Sai! Cỡ mẫu phải là số nguyên lần."
      ]
    }
  },

  {
    id: "D3",
    cluster: "D",
    title: "Bất đẳng thức Chebyshev: Cận trên của xác suất sai lệch",
    sources: "Slide Week 07 (tr. 33–37) [CHỈ CÓ TRONG SLIDE UET]",
    desc: "Định lý kỳ diệu áp dụng cho MỌI phân phối có phương sai hữu hạn. Đánh giá cận trên của rủi ro sai lệch xa khỏi tâm mà không cần biết hình dạng phân phối.",
    steps: [
      {
        t: "Bất đẳng thức Chebyshev là gì?",
        c: `<p>Cho biến ngẫu nhiên $X$ bất kỳ có kỳ vọng $\\mu$ và độ lệch chuẩn $\\sigma$ hữu hạn. Với mọi số thực $k &gt; 1$:</p>
            $$P(|X - \\mu| \\ge k\\sigma) \\le \\frac{1}{k^2}$$
            <p>Hoặc phát biểu dưới dạng xác suất nằm trong khoảng:</p>
            $$P(|X - \\mu| &lt; k\\sigma) \\ge 1 - \\frac{1}{k^2}$$
            <p><b>Dạng theo khoảng cách tuyệt đối $\\epsilon &gt; 0$:</b></p>
            $$P(|X - \\mu| \\ge \\epsilon) \\le \\frac{\\sigma^2}{\\epsilon^2}$$
            <div class="tip-box">
              <b>Sức mạnh vô địch của Chebyshev:</b><br>
              Định lý này <b>ĐÚNG VỚI MỌI PHÂN PHỐI</b> (dù là phân phối lệch phải, lệch trái, nhiều đỉnh, hay kỳ dị thế nào đi nữa). Nó cho ta một <b>cận trên an toàn tuyệt đối</b> của xác suất một giá trị đi chệch quá xa khỏi tâm!
            </div>`
      },
      {
        t: "Các cận số liệu thông dụng cần nhớ",
        c: `<table class="data-table">
              <thead><tr><th>Số độ lệch chuẩn $k$</th><th>Khoảng giá trị</th><th>Xác suất nằm NGOÀI khoảng: $\\le 1/k^2$</th><th>Xác suất nằm TRONG khoảng: $\\ge 1 - 1/k^2$</th></tr></thead>
              <tbody>
                <tr><td>$k = 2$</td><td>$(\\mu - 2\\sigma, \\mu + 2\\sigma)$</td><td>$$\\le \\frac{1}{4} = 25\\%$$</td><td>$$\\ge 1 - \\frac{1}{4} = 75\\%$$</td></tr>
                <tr><td>$k = 3$</td><td>$(\\mu - 3\\sigma, \\mu + 3\\sigma)$</td><td>$$\\le \\frac{1}{9} \\approx 11{,}11\\%$$</td><td>$$\\ge 1 - \\frac{1}{9} \\approx 88{,}89\\%$$</td></tr>
                <tr><td>$k = 4$</td><td>$(\\mu - 4\\sigma, \\mu + 4\\sigma)$</td><td>$$\\le \\frac{1}{16} = 6{,}25\\%$$</td><td>$$\\ge 1 - \\frac{1}{16} = 93{,}75\\%$$</td></tr>
              </tbody>
            </table>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        q: "Theo bất đẳng thức Chebyshev, xác suất để một biến ngẫu nhiên nhận giá trị lệch khỏi kỳ vọng từ 3 độ lệch chuẩn trở lên, tức P(|X - μ| ≥ 3σ), tối đa bằng bao nhiêu?",
        sol: "<b>Áp dụng công thức trực tiếp với k = 3:</b><br>" +
             "$$P(|X - \\mu| \\ge 3\\sigma) \\le \\frac{1}{3^2} = \\frac{1}{9} \\approx 0{,}1111\\text{ (hay } 11{,}11\\%\\text{)}$$."
      },
      {
        level: "Trung bình",
        q: "Một xưởng cơ khí sản xuất bu-lông có chiều dài trung bình μ = 50 mm và độ lệch chuẩn σ = 1 mm (chưa biết dạng phân phối). Hãy dùng Chebyshev để tìm cận dưới cho xác suất một bu-lông có chiều dài nằm trong khoảng từ 46 mm đến 54 mm.",
        sol: "<b>Bước 1:</b> Xác định khoảng cách sai lệch: $|X - 50| &lt; 4$ mm.<br>" +
             "<b>Bước 2:</b> Tính số độ lệch chuẩn $k$: $k = \\frac{4}{\\sigma} = \\frac{4}{1} = 4$.<br>" +
             "<b>Bước 3:</b> Áp dụng Chebyshev dạng khoảng:<br>" +
             "$$P(46 &lt; X &lt; 54) = P(|X - 50| &lt; 4\\sigma) \\ge 1 - \\frac{1}{4^2} = 1 - \\frac{1}{16} = \\frac{15}{16} = 0{,}9375\\text{ (93{,}75\\%)}$$<br>" +
             "<b>Kết luận:</b> Ít nhất 93,75% số bu-lông có chiều dài đạt tiêu chuẩn."
      },
      {
        level: "Vận dụng",
        q: "Điểm thi của một môn học có trung bình μ = 70 và độ lệch chuẩn σ = 10. Tìm cận trên cho xác suất để một sinh viên có điểm thi nhỏ hơn 40 hoặc lớn hơn 100.",
        sol: "<b>Bước 1:</b> Điểm nhỏ hơn 40 hoặc lớn hơn 100 tương đương với $|X - 70| \\ge 30$.<br>" +
             "<b>Bước 2:</b> Số độ lệch chuẩn $k$: $k = \\frac{30}{\\sigma} = \\frac{30}{10} = 3$.<br>" +
             "<b>Bước 3:</b> Áp dụng Chebyshev:<br>" +
             "$$P(|X - 70| \\ge 30) = P(|X - \\mu| \\ge 3\\sigma) \\le \\frac{1}{3^2} = \\frac{1}{9} \\approx 11{,}11\\%$$\\text{."
      }
    ],
    pitfalls: [
      {
        bad: "Nghĩ rằng Chebyshev cho ra xác suất chính xác.",
        good: "Chebyshev CHỈ LÀ MỘT CẬN TRÊN (hoặc cận dưới) mang tính bảo thủ, an toàn cho mọi phân phối. Nó không phải xác suất chính xác!"
      },
      {
        bad: "Áp dụng quy tắc 68–95–99,7 của phân phối Chuẩn cho bài toán chưa biết dạng phân phối.",
        good: "Quy tắc 68–95–99,7 CHỈ ĐƯỢC DÙNG khi đề bài khẳng định là phân phối CHUẨN! Nếu đề ghi 'chưa biết phân phối' thì BẮT BUỘC phải dùng Chebyshev!"
      }
    ],
    final_quiz: {
      q: "Theo bất đẳng thức Chebyshev, xác suất để biến ngẫu nhiên X sai lệch khỏi kỳ vọng từ 2 độ lệch chuẩn trở lên, P(|X - μ| ≥ 2σ), có cận trên bằng bao nhiêu?",
      opts: [
        "1/4 (25%)",
        "1/2 (50%)",
        "1/9 (11,1%)",
        "5% (0,05)"
      ],
      ans: 0,
      fb: [
        "Chính xác! Cận trên theo Chebyshev là 1/k^2 với k = 2, tức 1/4 = 25%.",
        "Sai! 1/2 là 1/k, không bình phương.",
        "Sai! 1/9 ứng với k = 3.",
        "Sai! 5% là quy tắc 2 SD của phân phối Chuẩn N(μ, σ^2), Chebyshev cho cận thô hơn là 25%."
      ]
    }
  },

  {
    id: "D4",
    cluster: "D",
    title: "Luật số lớn yếu (WLLN): Bản chất & Ứng dụng",
    sources: "Slide Week 07 (tr. 38–40) [CHỈ CÓ TRONG SLIDE UET]",
    desc: "Cầu nối giữa Xác suất lý thuyết và Thực tiễn thực nghiệm. Chứng minh định lý bằng Chebyshev và giải mã nguyên lý vì sao sòng bạc và bảo hiểm luôn có lãi.",
    steps: [
      {
        t: "Phát biểu Định lý Luật số lớn yếu (WLLN)",
        c: `<p>Cho $X_1, X_2, \\dots, X_n$ là dãy các biến ngẫu nhiên i.i.d. có kỳ vọng $\\mu$ và phương sai $\\sigma^2 &lt; \\infty$. Đặt $\\bar{X}_n = \\frac{1}{n}\\sum_{i=1}^n X_i$ là trung bình mẫu.</p>
            <p>Khi đó, với mọi số thực $\\epsilon &gt; 0$ dù nhỏ tùy ý:</p>
            $$\\lim_{n \\to \\infty} P(|\\bar{X}_n - \\mu| \\ge \\epsilon) = 0$$
            <p>Hay nói cách khác, trung bình mẫu <b>hội tụ theo xác suất</b> về kỳ vọng thật $\\mu$:</p>
            $$\\bar{X}_n \\xrightarrow{P} \\mu \\quad (n \\to \\infty)$$`
      },
      {
        t: "Chứng minh định lý tuyệt đẹp chỉ bằng 1 dòng Chebyshev!",
        c: `<p>Ta áp dụng bất đẳng thức Chebyshev trực tiếp cho biến ngẫu nhiên Trung bình mẫu $\\bar{X}_n$:</p>
            <ul>
              <li>Kỳ vọng: $E(\\bar{X}_n) = \\mu$.</li>
              <li>Phương sai: $\\operatorname{Var}(\\bar{X}_n) = \\frac{\\sigma^2}{n}$.</li>
            </ul>
            <p>Áp dụng Chebyshev với sai số $\\epsilon$:</p>
            $$P(|\\bar{X}_n - \\mu| \\ge \\epsilon) \\le \\frac{\\operatorname{Var}(\\bar{X}_n)}{\\epsilon^2} = \\frac{\\sigma^2}{n \\cdot \\epsilon^2}$$
            <p>Khi cho cỡ mẫu $n \\to \\infty$, vì tử số $\\sigma^2$ và mẫu số $\\epsilon^2$ là các hằng số hữu hạn, nên đại lượng $\\frac{\\sigma^2}{n \\epsilon^2} \\to 0$!</p>
            <div class="tip-box">Một phép chứng minh giải tích mẫu mực mà giám khảo UET rất thích hỏi trong câu hỏi lý thuyết tự luận!</div>`
      },
      {
        t: "Ý nghĩa thực tiễn: Vì sao Nhà cái không bao giờ thua?",
        c: `<p>Một người chơi bước vào casino có thể may mắn trúng độc đắc ở vài ván đầu. Nhưng với sòng bạc:</p>
            <ul>
              <li>Mỗi ngày có hàng trăm nghìn lượt đặt cược ($n$ cực lớn).</li>
              <li>Kỳ vọng lợi nhuận trên mỗi ván cược của nhà cái là số dương $\\mu &gt; 0$ (nhờ luật chơi được thiết kế có lợi thế nhà cái).</li>
              <li>Theo Luật số lớn, tỉ lệ tiền thắng thực tế trung bình của sòng bạc $\\bar{X}_n$ <b>chắc chắn sẽ tiến sát về đúng kỳ vọng lý thuyết $\\mu$</b> với rủi ro gần như bằng 0.</li>
            </ul>
            <p>Tương tự với các công ty bảo hiểm: Khi số lượng hợp đồng $n$ đủ lớn, khoản tiền bồi thường trung bình mỗi người sẽ ổn định kỳ lạ quanh kỳ vọng rủi ro tính toán từ trước.</p>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        q: "Luật số lớn yếu khẳng định điều gì khi cỡ mẫu n tiến ra vô cùng?",
        sol: "<b>Khẳng định:</b> Khi cỡ mẫu $n$ tăng vô hạn, trung bình mẫu $\\bar{X}_n$ sẽ tiến sát (hội tụ theo xác suất) về giá trị kỳ vọng thực tế $\\mu$, và xác suất để nó đi lệch khỏi $\\mu$ quá một khoảng $\\epsilon$ sẽ tiến về 0."
      },
      {
        level: "Trung bình",
        q: "Tung một đồng xu cân đối (μ = 0,5, σ = 0,5). Dùng bất đẳng thức Chebyshev chứng minh rằng xác suất để tỉ lệ mặt ngửa chệch khỏi 0,5 quá 0,1 sẽ nhỏ hơn 0,05 khi tung ít nhất 500 lần.",
        sol: "<b>Bước 1:</b> Tỉ lệ mặt ngửa chính là trung bình mẫu $\\bar{X}_n$. Ta có $\\mu = 0{,}5; \\sigma = 0{,}5; \\epsilon = 0{,}1$.<br>" +
             "<b>Bước 2:</b> Áp dụng Chebyshev cho trung bình mẫu:<br>" +
             "$$P(|\\bar{X}_n - 0{,}5| \\ge 0{,}1) \\le \\frac{\\sigma^2}{n \\epsilon^2} = \\frac{0{,}5^2}{n \\times 0{,}1^2} = \\frac{0{,}25}{0{,}01 n} = \\frac{25}{n}$$<br>" +
             "<b>Bước 3:</b> Để xác suất này $\\le 0{,}05$:<br>" +
             "$$\\frac{25}{n} \\le 0{,}05 \\implies n \\ge \\frac{25}{0{,}05} = 500$$<br>" +
             "<b>Kết luận:</b> Khi tung từ 500 lần trở lên, xác suất sai lệch quá 0,1 chắc chắn không vượt quá 5%."
      },
      {
        level: "Vận dụng",
        q: "Một cuộc thăm dò ý kiến muốn ước lượng tỉ lệ cử tri ủng hộ ứng viên A sao cho độ lệch không quá 2% (ε = 0,02) với độ tin cậy ít nhất 95% (xác suất sai lệch không quá 5%). Hãy dùng Chebyshev để tìm cỡ mẫu n cần thiết (biết rằng với phân phối nhị thức, σ² = p(1-p) luôn ≤ 0,25).",
        sol: "<b>Bước 1:</b> Ta có $\\operatorname{Var}(X) = p(1-p) \\le 0{,}25$ với mọi $p$. Sai số $\\epsilon = 0{,}02$. Xác suất cho phép $\\alpha = 0{,}05$.<br>" +
             "<b>Bước 2:</b> Theo Chebyshev:<br>" +
             "$$P(|\\bar{X}_n - p| \\ge 0{,}02) \\le \\frac{\\sigma^2}{n \\epsilon^2} \\le \\frac{0{,}25}{n \\times 0{,}02^2} = \\frac{0{,}25}{0{,}0004 n} = \\frac{625}{n}$$<br>" +
             "<b>Bước 3:</b> Thiết lập bất phương trình:<br>" +
             "$$\\frac{625}{n} \\le 0{,}05 \\implies n \\ge \\frac{625}{0{,}05} = 12.500\\text{ (người)}$$<br>" +
             "<i>Nhận xét: Chebyshev cho cận rất an toàn (12.500 người). Sau này khi học CLT (Cụm E), nhờ phân phối Chuẩn ta sẽ thấy chỉ cần cỡ mẫu khoảng 2.400 người là đủ!</i>"
      }
    ],
    pitfalls: [
      {
        bad: "Nghĩ rằng Luật số lớn nói rằng nếu bạn vừa thua 5 ván liên tiếp thì ván tiếp theo bạn sẽ có xác suất thắng cao hơn (Ngụy biện con bạc - Gambler's Fallacy).",
        good: "Đồng xu hay bánh xe quay không có ký ức! Luật số lớn làm cho tỉ lệ hội tụ bằng cách PHA LOÃNG các ván chơi trong một số lượng ván khổng lồ, chứ không 'bù trừ' may rủi trong tương lai!"
      },
      {
        bad: "Nhầm lẫn giữa Luật số lớn (nói về sự ổn định của TRUNG BÌNH) và Định lý giới hạn trung tâm CLT (nói về HÌNH DÁNG HÌNH CHUÔNG của phân phối).",
        good: "Luật số lớn chỉ khẳng định trung bình tiến về một con số μ; còn CLT cho biết phân phối của trung bình mẫu có dạng đường cong hình chuông Gauss!"
      }
    ],
    final_quiz: {
      q: "Nội dung cốt lõi của Luật số lớn yếu (WLLN) khẳng định điều gì khi cỡ mẫu n tiến dần đến vô cùng?",
      opts: [
        "Trung bình mẫu tiến gần và hội tụ về kỳ vọng lý thuyết μ",
        "Tổng các giá trị mẫu luôn bằng kỳ vọng",
        "Phân phối gốc ban đầu tự động biến thành phân phối chuẩn",
        "Phương sai của tổng mẫu tiến về 0"
      ],
      ans: 0,
      fb: [
        "Chính xác! Khi cỡ mẫu n càng lớn, trung bình mẫu càng hội tụ ổn định về kỳ vọng thực tế μ.",
        "Sai! Tổng mẫu Sn dao động rộng ra với SD = σ√n, không bao giờ cố định.",
        "Sai! Phân phối gốc giữ nguyên, chỉ có phân phối của trung bình mẫu mới có dạng chuẩn (theo CLT).",
        "Sai! Phương sai của tổng là n*σ^2 tiến ra vô cùng, chỉ có phương sai của trung bình (σ^2/n) mới tiến về 0."
      ]
    }
  }
];

if (typeof module !== 'undefined' && module.exports) {
  module.exports = CUM_D;
}
