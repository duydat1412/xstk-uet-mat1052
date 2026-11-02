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
    ref: {
      "slide_file": "week07.pdf",
      "slide_name": "Tuần 07 — Biến ngẫu nhiên i.i.d. & Mô hình chiếc hộp",
      "pages": "Slide 21 – 24",
      "page_start": 21,
      "section": "Phần 2: Các biến ngẫu nhiên độc lập cùng phân phối (i.i.d.) & Mô hình chiếc hộp (Slide 21–24)",
      "stat20": "Stat20 Mục 4.13 (Independent and Identically Distributed & Box Models)",
      "key_points": [
            "Biến ngẫu nhiên i.i.d. (independent and identically distributed): Độc lập và cùng tuân theo một quy luật xác suất",
            "Mô hình chiếc hộp (Box model): Rút thăm n lần CÓ hoàn lại từ một hộp vé ghi các con số",
            "Chuyển dịch tư duy: Xem mọi bài toán lấy mẫu ngẫu nhiên như việc rút thẻ từ một chiếc hộp trừu tượng"
      ],
      "remind": "Nếu bạn chưa hình dung được mô hình chiếc hộp liên hệ thế nào với các biến ngẫu nhiên trong bài thi, hãy mở lại Slide Week 07 trang 21–24."
},
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
        t: "[Slide Week 07 — Ví dụ 6] Gieo cặp xúc xắc qua Mô hình Chiếc hộp",
        q: "Xét phép thử: Gieo đồng thời một cặp xúc xắc 6 mặt cân đối và tính tổng số chấm xuất hiện (Slide 24). Hãy biểu diễn phép thử này dưới dạng Mô hình chiếc hộp (Box model) và xác định các tấm vé bên trong hộp.",
        sol: "<b>Lời giải theo Slide Week 07 (trang 24):</b><br>" +
             "1. Mỗi lần gieo một cặp xúc xắc, tổng số chấm có thể nhận các giá trị từ $2$ đến $12$.<br>" +
             "2. Có 36 kết quả sơ cấp đồng khả năng. Ta mô hình hóa bằng <b>một chiếc hộp chứa 36 tấm vé</b> ghi các con số tổng tương ứng:<br>" +
             "   - 1 vé ghi [2] (ứng với $(1,1)$);<br>" +
             "   - 2 vé ghi [3]; 3 vé ghi [4]; 4 vé ghi [5]; 5 vé ghi [6];<br>" +
             "   - 6 vé ghi [7] (tổng phổ biến nhất);<br>" +
             "   - 5 vé ghi [8]; 4 vé ghi [9]; 3 vé ghi [10]; 2 vé ghi [11];<br>" +
             "   - 1 vé ghi [12] (ứng với $(6,6)$).<br>" +
             "3. Mỗi lần gieo cặp xúc xắc tương đương với việc <b>rút ngẫu nhiên một tấm vé</b> từ chiếc hộp 36 vé này."
      },
      {
        level: "Trung bình",
        t: "[Slide Week 07 — Ví dụ 7] Hộp 10 lá thăm và Trung bình của Hộp",
        q: "Một chiếc hộp chứa 10 lá thăm ghi các số: $[0, 0, 1, 1, 1, 2, 3, 3, 4, 4]$ (Slide 27–28). Rút ngẫu nhiên một lá thăm từ hộp.<br>" +
           "a) Lập bảng phân phối xác suất của số ghi trên lá thăm rút ra.<br>" +
           "b) Tính trung bình của hộp $\\mu$ và độ lệch chuẩn của hộp $\\sigma$.",
        sol: "<b>Lời giải chi tiết theo Slide Week 07 (trang 28):</b><br>" +
             "a) Bảng phân phối xác suất của $X$ (tổng 10 vé):<br>" +
             "   - $p(0) = \\frac{2}{10} = 0{,}2$; $p(1) = \\frac{3}{10} = 0{,}3$; $p(2) = \\frac{1}{10} = 0{,}1$; $p(3) = \\frac{2}{10} = 0{,}2$; $p(4) = \\frac{2}{10} = 0{,}2$.<br>" +
             "b) Tính trung bình của hộp (Kỳ vọng):<br>" +
             "   $$\\mu = E(X) = 0(0{,}2) + 1(0{,}3) + 2(0{,}1) + 3(0{,}2) + 4(0{,}2) = 0 + 0{,}3 + 0{,}2 + 0{,}6 + 0{,}8 = 1{,}9$$<br>" +
             "   Tính $E(X^2)$:<br>" +
             "   $$E(X^2) = 0^2(0{,}2) + 1^2(0{,}3) + 2^2(0{,}1) + 3^2(0{,}2) + 4^2(0{,}2) = 0 + 0{,}3 + 0{,}4 + 1{,}8 + 3{,}2 = 5{,}5$$<br>" +
             "   Phương sai và độ lệch chuẩn của hộp:<br>" +
             "   $$\\operatorname{Var}(X) = E(X^2) - \\mu^2 = 5{,}5 - (1{,}9)^2 = 5{,}5 - 3{,}61 = 1{,}89$$<br>" +
             "   $$\\sigma = \\sqrt{1{,}89} \\approx 1{,}3748 \\approx 1{,}375$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 07 — Slide 21–24] Bản chất Biến ngẫu nhiên i.i.d. khi Lấy mẫu",
        q: "Từ chiếc hộp 10 lá thăm ở trên, một người thực hiện rút ngẫu nhiên $n$ lần. Giải thích rõ sự khác biệt bản chất giữa: (1) Rút CÓ HOÀN LẠI và (2) Rút KHÔNG HOÀN LẠI. Trường hợp nào các biến ngẫu nhiên kết quả $X_1, X_2, \\dots, X_n$ tạo thành một mẫu i.i.d.?",
        sol: "<b>Phân tích bản chất theo Slide Week 07 (trang 21–24):</b><br>" +
             "1. <b>Rút CÓ HOÀN LẠI:</b> Sau mỗi lần rút, lá thăm được trả lại vào hộp và xáo đều. Do đó thành phần của hộp không thay đổi $\\implies$ Mỗi lần rút tuân theo <b>cùng phân phối</b> gốc $\\mu=1{,}9, \\sigma=1{,}375$ và kết quả lần trước hoàn toàn <b>độc lập</b> với lần sau.<br>" +
             "   \\rightarrow <b>Đây chính là mẫu i.i.d. (independent and identically distributed)!</b><br>" +
             "2. <b>Rút KHÔNG HOÀN LẠI:</b> Sau mỗi lần rút, số vé trong hộp giảm đi, tỉ lệ các con số thay đổi tùy thuộc vào vé đã rút $\\implies$ Các biến ngẫu nhiên $X_1, X_2, \\dots$ bị phụ thuộc lẫn nhau, KHÔNG độc lập và phân phối có điều kiện bị thay đổi."
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
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Các biến ngẫu nhiên $X_1, X_2, \\dots, X_n$ được gọi là i.i.d. nếu chúng thỏa mãn:",
            "opts": [
                  "Có tương quan tuyến tính bằng 0",
                  "Độc lập với nhau và cùng tuân theo một phân phối xác suất chung",
                  "Có cùng kỳ vọng nhưng phân phối khác nhau",
                  "Tất cả đều là phân phối chuẩn"
            ],
            "ans": 1,
            "fb": "Chính xác! i.i.d. = independent and identically distributed."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Trong mô hình chiếc hộp (Box Model) chứa 3 vé: $[1, 2, 6]$. Giá trị trung bình của chiếc hộp là:",
            "opts": [
                  "$2$",
                  "$9$",
                  "$4{,}5$",
                  "$3$"
            ],
            "ans": 3,
            "fb": "Đúng! $\\mu = \\frac{1 + 2 + 6}{3} = 3$."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Rút $n = 100$ lần có hoàn lại từ một chiếc hộp có $\\mu = 5, \\sigma = 2$. Sai số chuẩn của tổng các vé rút ra là:",
            "opts": [
                  "$200$",
                  "$2$",
                  "$20$",
                  "$0{,}2$"
            ],
            "ans": 2,
            "fb": "Chính xác! $\\text{SD}(S_{100}) = \\sqrt{n} \\cdot \\sigma = \\sqrt{100} \\times 2 = 10 \\times 2 = 20$."
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
    ref: {
      "slide_file": "week07.pdf",
      "slide_name": "Tuần 07 — Tổng & Trung bình mẫu: Quy tắc căn bậc hai",
      "pages": "Slide 25 – 32",
      "page_start": 25,
      "section": "Phần 2: Tổng và trung bình của các biến i.i.d. — Square Root Law (Slide 25–32)",
      "stat20": "Stat20 Mục 4.14 (Sum and Average of i.i.d. Variables)",
      "key_points": [
            "Tổng Sn = X1 + ... + Xn: E(Sn) = n*μ, SD(Sn) = σ*√n (quy tắc nhân căn n)",
            "Trung bình mẫu X_bar = Sn / n: E(X_bar) = μ, SD(X_bar) = σ / √n (sai số giảm theo 1/√n)",
            "Quy tắc căn bậc hai (Square Root Law): Muốn giảm sai số đo lường đi k lần, phải tăng cỡ mẫu gấp k^2 lần"
      ],
      "remind": "Đây là dạng bài trắc nghiệm tính nhanh rất phổ biến. Hãy mở Slide Week 07 trang 26–30 để ghi nhớ sự khác biệt giữa σ*√n và σ/√n."
},
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
        t: "[Slide Week 07 — Ví dụ 8] Tổng số điểm của 25 lần rút thẻ từ Hộp",
        q: "Từ hộp có các lá thăm $[0, 0, 1, 1, 1, 2, 3, 3, 4, 4]$ với $\\mu = 1{,}9$ và $\\sigma = 1{,}375$ (Slide 29–30). Rút ngẫu nhiên độc lập có hoàn lại $n = 25$ lần. Gọi $S_{25} = X_1 + X_2 + \\dots + X_{25}$ là tổng số điểm ghi trên 25 lá thăm rút được.<br>" +
           "a) Tính kỳ vọng của tổng $E(S_{25})$.<br>" +
           "b) Tính độ lệch chuẩn của tổng $\\operatorname{SD}(S_{25})$.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 07 (trang 30):</b><br>" +
             "a) Theo quy tắc nhân $n$ của kỳ vọng tổng:<br>" +
             "   $$E(S_{25}) = n \\cdot \\mu = 25 \\times 1{,}9 = 47{,}5$$<br>" +
             "b) Theo Quy tắc căn bậc hai (Square Root Law) cho tổng các biến i.i.d.:<br>" +
             "   $$\\operatorname{Var}(S_{25}) = n \\cdot \\sigma^2 = 25 \\times 1{,}89 = 47{,}25$$<br>" +
             "   $$\\operatorname{SD}(S_{25}) = \\sigma \\sqrt{n} = 1{,}3748 \\times \\sqrt{25} = 1{,}3748 \\times 5 \\approx 6{,}874 \\approx 6{,}875$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 07 — Ví dụ 8] Trung bình mẫu của 25 lần rút thẻ",
        q: "Cũng với phép thử rút có hoàn lại $n = 25$ lần ở trên (Slide 29–30). Gọi $\\bar{X}_{25} = \\frac{S_{25}}{25}$ là số điểm trung bình của một lá thăm trong mẫu 25 lần rút.<br>" +
           "a) Tính kỳ vọng của trung bình mẫu $E(\\bar{X}_{25})$.<br>" +
           "b) Tính độ lệch chuẩn của trung bình mẫu $\\operatorname{SD}(\\bar{X}_{25})$.",
        sol: "<b>Lời giải chuẩn xác theo Slide Week 07 (trang 30):</b><br>" +
             "a) Kỳ vọng của trung bình mẫu bằng đúng trung bình tổng thể:<br>" +
             "   $$E(\\bar{X}_{25}) = \\mu = 1{,}9$$<br>" +
             "b) Độ lệch chuẩn của trung bình mẫu giảm theo nghịch đảo căn bậc hai của cỡ mẫu ($1/\\sqrt{n}$):<br>" +
             "   $$\\operatorname{SD}(\\bar{X}_{25}) = \\frac{\\sigma}{\\sqrt{n}} = \\frac{1{,}3748}{\\sqrt{25}} = \\frac{1{,}3748}{5} \\approx 0{,}275$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 07 — Slide 26] Ứng dụng Quy tắc Căn bậc hai (Square Root Law)",
        q: "Một nhà nghiên cứu đang đo độ dày linh kiện với độ lệch chuẩn trung bình mẫu hiện tại là $\\operatorname{SD}(\\bar{X}) = 0{,}275$ mm khi dùng cỡ mẫu $n = 25$. Để nâng cao độ chính xác của phép đo, nhà nghiên cứu muốn giảm độ lệch chuẩn của trung bình mẫu đi 4 lần (xuống còn $\\approx 0{,}06875$ mm). Cần phải tăng cỡ mẫu lên bao nhiêu lần và cỡ mẫu mới $n'$ là bao nhiêu?",
        sol: "<b>Phân tích định lý theo Slide Week 07 (trang 26):</b><br>" +
             "1. Theo công thức: $\\operatorname{SD}(\\bar{X}) = \\frac{\\sigma}{\\sqrt{n}}$. Để $\\operatorname{SD}(\\bar{X})$ giảm đi $k = 4$ lần, mẫu số $\\sqrt{n}$ phải tăng lên $4$ lần.<br>" +
             "2. Do đó, cỡ mẫu $n$ phải tăng lên $k^2 = 4^2 = 16$ lần!<br>" +
             "   $$n' = n \\times 16 = 25 \\times 16 = 400 \\text{ quan sát}$$<br>" +
             "<b>Kết luận quy tắc vàng:</b> Muốn độ chính xác tăng gấp đôi, cỡ mẫu phải tăng gấp 4; muốn độ chính xác tăng gấp 4, cỡ mẫu phải tăng gấp 16!"
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
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Theo quy tắc căn bậc hai (Square root law), sai số chuẩn của trung bình mẫu $SE(\\bar{X})$ bằng:",
            "opts": [
                  "$\\frac{\\sigma}{\\sqrt{n}}$",
                  "$\\sigma \\sqrt{n}$",
                  "$\\frac{\\sigma}{n}$",
                  "$\\frac{\\sigma^2}{n}$"
            ],
            "ans": 0,
            "fb": "Chính xác! Độ biến thiên của trung bình mẫu tỷ lệ nghịch với căn bậc hai cỡ mẫu."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Một mẫu gồm $n = 64$ quan sát độc lập từ tổng thể có $\\sigma = 16$. Sai số chuẩn $SE(\\bar{X})$ bằng:",
            "opts": [
                  "$1$",
                  "$0{,}25$",
                  "$2$",
                  "$8$"
            ],
            "ans": 2,
            "fb": "Đúng! $SE(\\bar{X}) = 16 / \\sqrt{64} = 16 / 8 = 2$."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Để giảm sai số chuẩn của trung bình mẫu xuống còn một phần ba ($1/3$ lần), ta cần tăng kích thước mẫu $n$ lên:",
            "opts": [
                  "$6$ lần",
                  "$27$ lần",
                  "$3$ lần",
                  "$9$ lần"
            ],
            "ans": 3,
            "fb": "Chính xác! Vì $SE \\propto 1/\\sqrt{n}$, muốn $SE$ giảm 3 lần thì $\\sqrt{n}$ phải tăng 3 lần $\\implies n$ tăng $3^2 = 9$ lần."
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
    ref: {
      "slide_file": "week07.pdf",
      "slide_name": "Tuần 07 — Bất đẳng thức Chebyshev",
      "pages": "Slide 33 – 37",
      "page_start": 33,
      "section": "Phần 3: Bất đẳng thức Chebyshev và cận trên sai lệch [CHUYÊN ĐỀ ĐỘC QUYỀN SLIDE UET] (Slide 33–37)",
      "stat20": "Nội dung nâng cao riêng biệt của Slide UET (không có trong Stat20)",
      "key_points": [
            "Bất đẳng thức Chebyshev: P(|X - μ| ≥ k*σ) ≤ 1 / k^2 (với mọi k > 0)",
            "Dạng sai số tuyệt đối ε: P(|X - μ| ≥ ε) ≤ Var(X) / ε^2",
            "Ưu điểm tối cao: Đúng cho MỌI phân phối xác suất bất kỳ (kể cả phân phối lệch, rời rạc hay liên tục)"
      ],
      "remind": "Nếu gặp bài toán yêu cầu 'đánh giá xác suất mà không biết dạng phân phối', hãy mở ngay Slide Week 07 trang 34–37 về Bất đẳng thức Chebyshev."
},
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
        t: "[Slide Week 07 — Slide 34] Đánh giá Xác suất Sai lệch bằng BĐT Chebyshev",
        q: "Cho một biến ngẫu nhiên $X$ có phân phối bất kỳ (chưa biết là phân phối gì) với kỳ vọng $\\mu$ và độ lệch chuẩn $\\sigma$. Dùng Bất đẳng thức Chebyshev đánh giá cận trên của xác suất để $X$ nhận giá trị lệch khỏi kỳ vọng từ 2 độ lệch chuẩn trở lên ($P(|X - \\mu| \\ge 2\\sigma)$).",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 07 (trang 34):</b><br>" +
             "Bất đẳng thức Chebyshev phát biểu rằng với mọi $k > 0$:<br>" +
             "$$P(|X - \\mu| \\ge k\\sigma) \\le \\frac{1}{k^2}$$<br>" +
             "Thay $k = 2$ vào bất đẳng thức:<br>" +
             "$$P(|X - \\mu| \\ge 2\\sigma) \\le \\frac{1}{2^2} = \\frac{1}{4} = 0{,}25 \\text{ (hay 25\\%)}$$<br>" +
             "Tương đương: Xác suất để biến ngẫu nhiên nằm trong khoảng $[\\mu - 2\\sigma, \\mu + 2\\sigma]$ đạt ít nhất $1 - 0{,}25 = 75\\%$ đối với MỌI phân phối xác suất!"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 07 — Ví dụ 9] Giám sát Nhiệt độ Lò sấy UET",
        q: "Một nhà máy cần theo dõi nhiệt độ thật $\\mu$ của lò sấy (Slide 35–36). Mỗi phép đo là biến ngẫu nhiên có kỳ vọng $\\mu$ và độ lệch chuẩn $\\sigma = 2^\\circ\\text{C}$. Các phép đo độc lập. Gọi $\\bar{X}_n$ là trung bình của $n$ lần đo. Cần thực hiện ít nhất bao nhiêu lần đo để xác suất sai lệch $|\\bar{X}_n - \\mu| \\ge 1^\\circ\\text{C}$ không vượt quá 5% ($0{,}05$)?",
        sol: "<b>Lời giải chi tiết theo Slide Week 07 (trang 36):</b><br>" +
             "1. Trung bình mẫu $\\bar{X}_n$ có $E(\\bar{X}_n) = \\mu$ và phương sai $\\operatorname{Var}(\\bar{X}_n) = \\frac{\\sigma^2}{n} = \\frac{4}{n}$.<br>" +
             "2. Áp dụng Bất đẳng thức Chebyshev dạng sai số tuyệt đối $\\epsilon = 1^\\circ\\text{C}$:<br>" +
             "   $$P(|\\bar{X}_n - \\mu| \\ge \\epsilon) \\le \\frac{\\operatorname{Var}(\\bar{X}_n)}{\\epsilon^2} = \\frac{4/n}{1^2} = \\frac{4}{n}$$<br>" +
             "3. Yêu cầu xác suất này không vượt quá $0{,}05$:<br>" +
             "   $$\\frac{4}{n} \\le 0{,}05 \\iff n \\ge \\frac{4}{0{,}05} = 80$$<br>" +
             "<b>Kết luận:</b> Cần đo ít nhất <b>80 lần</b> để bảo đảm độ tin cậy theo BĐT Chebyshev."
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 07 — Slide 37] So sánh Đánh giá Chebyshev vs Quy tắc Phân phối Chuẩn",
        q: "Tại sao ở $k = 2$, BĐT Chebyshev cho xác suất sai lệch là $\\le 25\\%$, trong khi quy tắc thực nghiệm phân phối chuẩn lại cho xác suất sai lệch chỉ khoảng $5\\%$? Khi nào trong bài thi bắt buộc phải dùng BĐT Chebyshev?",
        sol: "<b>Phân tích bản chất theo Slide Week 07 (trang 37):</b><br>" +
             "1. <b>Lý do chênh lệch:</b> Bất đẳng thức Chebyshev là cận trên cho <b>MỌI phân phối xác suất khả dĩ</b> (kể cả phân phối hai đỉnh, phân phối cực kỳ lệch hay phân phối có đuôi rất nặng). Quy tắc $5\\%$ chỉ đúng cho duy nhất hình chuông đối xứng chuẩn Gauss.<br>" +
             "2. <b>Khi nào bắt buộc dùng Chebyshev:</b> Khi đề bài <b>không cho biết dạng phân phối</b> của biến ngẫu nhiên (hoặc biết rõ phân phối không phải chuẩn) và cỡ mẫu $n$ chưa đủ lớn để áp dụng Định lý giới hạn trung tâm."
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
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Bất đẳng thức Chebyshev $P(|X - \\mu| < k\\sigma) \\ge 1 - \\frac{1}{k^2}$ áp dụng được cho:",
            "opts": [
                  "MỌI biến ngẫu nhiên có phương sai hữu hạn, không phụ thuộc vào phân phối",
                  "Chỉ khi $k \\ge 5$",
                  "Chỉ các biến ngẫu nhiên có phân phối Chuẩn",
                  "Chỉ các biến ngẫu nhiên rời rạc"
            ],
            "ans": 0,
            "fb": "Chính xác! Chebyshev có tính phi tham số tuyệt đối, đúng cho bất kỳ phân phối nào."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Theo Chebyshev, tỷ lệ dữ liệu nằm trong khoảng 2 độ lệch chuẩn quanh trung bình $[\\mu - 2\\sigma, \\mu + 2\\sigma]$ luôn ít nhất là:",
            "opts": [
                  "$50\\%$",
                  "$75\\%$",
                  "$95\\%$",
                  "$68\\%$"
            ],
            "ans": 1,
            "fb": "Đúng! $1 - 1/2^2 = 1 - 0{,}25 = 0{,}75 = 75\\%$."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Cho $X$ có $\\mu = 50, \\sigma = 5$. Cận dưới xác suất $P(35 < X < 65)$ là:",
            "opts": [
                  "$99\\%$",
                  "$95\\%$",
                  "$\\frac{8}{9} \\approx 88{,}89\\%$",
                  "$75\\%$"
            ],
            "ans": 2,
            "fb": "Chính xác! Khoảng $(35, 65) \\iff |X - 50| < 15 = 3\\sigma \\implies k = 3$. Xác suất $\\ge 1 - 1/3^2 = 8/9 \\approx 88{,}89\\%$."
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
    ref: {
      "slide_file": "week07.pdf",
      "slide_name": "Tuần 07 — Luật số lớn yếu (WLLN)",
      "pages": "Slide 38 – 40",
      "page_start": 38,
      "section": "Phần 3: Luật số lớn yếu — Weak Law of Large Numbers [ĐỘC QUYỀN SLIDE UET] (Slide 38–40)",
      "stat20": "Nội dung giải tích xác suất nâng cao của Slide UET",
      "key_points": [
            "Phát biểu WLLN: lim (n→∞) P(|X_bar_n - μ| ≥ ε) = 0 với mọi sai số ε > 0 tùy ý",
            "Ý nghĩa toán học: Trung bình mẫu hội tụ theo xác suất về kỳ vọng thực của tổng thể",
            "Ứng dụng thực tế: Cơ sở toán học nền tảng cho ngành bảo hiểm, casino và thống kê suy diễn"
      ],
      "remind": "Nếu bạn muốn hiểu bản chất chứng minh WLLN từ BĐT Chebyshev (Var(X_bar) = σ^2/n → 0), hãy xem Slide Week 07 trang 38–40."
},
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
        t: "[Slide Week 07 — Slide 38] Bản chất Toán học của Luật số lớn yếu (WLLN)",
        q: "Dùng Bất đẳng thức Chebyshev chứng minh chặt chẽ phát biểu của Luật số lớn yếu: Cho dãy biến ngẫu nhiên $X_1, X_2, \\dots, X_n$ i.i.d. có kỳ vọng $\\mu$ và phương sai $\\sigma^2$ hữu hạn. Chứng minh với mọi $\\epsilon > 0$ tùy ý:<br>" +
           "$$\\lim_{n \\to \\infty} P(|\\bar{X}_n - \\mu| \\ge \\epsilon) = 0$$",
        sol: "<b>Chứng minh giải tích theo Slide Week 07 (trang 38):</b><br>" +
             "1. Ta có $E(\\bar{X}_n) = \\mu$ và $\\operatorname{Var}(\\bar{X}_n) = \\frac{\\sigma^2}{n}$.<br>" +
             "2. Áp dụng Bất đẳng thức Chebyshev cho biến $\\bar{X}_n$ với sai số $\\epsilon > 0$:<br>" +
             "   $$0 \\le P(|\\bar{X}_n - \\mu| \\ge \\epsilon) \\le \\frac{\\operatorname{Var}(\\bar{X}_n)}{\\epsilon^2} = \\frac{\\sigma^2}{n \\cdot \\epsilon^2}$$<br>" +
             "3. Lấy giới hạn hai vế khi $n \\to \\infty$ (với $\\sigma^2$ và $\\epsilon^2$ là các hằng số dương cố định):<br>" +
             "   $$\\lim_{n \\to \\infty} \\frac{\\sigma^2}{n \\cdot \\epsilon^2} = 0$$<br>" +
             "   Theo nguyên lý kẹp (Squeeze Theorem), ta suy ra $\\lim_{n \\to \\infty} P(|\\bar{X}_n - \\mu| \\ge \\epsilon) = 0$ (ĐPCM)."
      },
      {
        level: "Trung bình",
        t: "[Slide Week 07 — Ví dụ 10] Bác bỏ Ngộ nhận Con bạc (Gambler's Fallacy)",
        q: "Sau 10 lần tung một đồng xu cân đối đều ra mặt Sấp, một người đánh cược khẳng định: <i>'Theo Luật số lớn, lần thứ 11 chắc chắn khả năng ra mặt Ngửa phải cao hơn rất nhiều để bù trừ lại cho cân bằng!'</i> (Slide 39–40). Khẳng định này đúng hay sai? Luật số lớn hoạt động theo cơ chế nào?",
        sol: "<b>Phân tích bản chất theo Slide Week 07 (trang 40):</b><br>" +
             "1. <b>Khẳng định SAI HOÀN TOÀN (Ngộ nhận con bạc)!</b> Các lần tung đồng xu là hoàn toàn độc lập, đồng xu không có trí nhớ. Ở lần tung thứ 11, xác suất ra mặt Ngửa vẫn chính xác bằng $0{,}5$.<br>" +
             "2. <b>Cơ chế của Luật số lớn là LÀM LOÃNG (Dilution), KHÔNG PHẢI BÙ TRỪ (Compensation):</b><br>" +
             "   - Chênh lệch 10 lần sấp ban đầu sẽ không mất đi.<br>" +
             "   - Nhưng khi $n$ tăng lên 10.000 hay 1.000.000 lần, con số 10 này khi chia cho mẫu số $n$ khổng lồ sẽ bị triệt tiêu về $0$: $\\frac{10}{1.000.000} = 0{,}00001 \\to 0$!"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 07 — Slide 40] Ứng dụng WLLN trong Quản trị Rủi ro Bảo hiểm",
        q: "Một công ty bảo hiểm bán 100.000 hợp đồng bảo hiểm xe máy độc lập trong một năm. Xác suất một xe gặp sự cố trong năm là $p = 0{,}02$ với số tiền bồi thường là 50 triệu đồng. Giải thích tại sao bán cho 1 khách hàng là canh bạc rủi ro lớn, nhưng bán cho 100.000 khách hàng thì lợi nhuận của công ty lại an toàn tuyệt đối nhờ Luật số lớn yếu.",
        sol: "<b>Phân tích kinh tế lượng theo Slide Week 07 (trang 40):</b><br>" +
             "1. Với 1 khách hàng: Biến cố nhận bồi thường là ngẫu nhiên cực đoan (hoặc 0 đồng hoặc mất ngay 50 triệu), rủi ro phương sai rất lớn.<br>" +
             "2. Với $n = 100.000$ hợp đồng độc lập: Tỉ lệ số vụ yêu cầu bồi thường $\\bar{X}_n$ tuân theo Luật số lớn yếu. Phương sai của tỉ lệ bồi thường là:<br>" +
             "   $$\\operatorname{Var}(\\bar{X}_n) = \\frac{p(1-p)}{n} = \\frac{0{,}02 \\times 0{,}98}{100.000} = 1{,}96 \\times 10^{-7} \\approx 0$$<br>" +
             "   Tỉ lệ bồi thường thực tế gần như chắc chắn $100\\%$ sẽ hội tụ sát nút về $2\\%$ (tức khoảng đúng 2.000 vụ bồi thường). Do đó công ty bảo hiểm chủ động định phí để thu lợi nhuận ổn định mà không lo phá sản."
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
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Luật số lớn yếu (WLLN) khẳng định rằng khi cỡ mẫu $n \\to \\infty$, trung bình mẫu $\\bar{X}_n$ sẽ:",
            "opts": [
                  "Hội tụ theo xác suất về kỳ vọng tổng thể $\\mu$",
                  "Có phương sai tiến dần tới vô cùng",
                  "Luôn luôn bằng chính xác $\\mu$ tại mọi bước thử",
                  "Biến thiên ngẫu nhiên không có giới hạn"
            ],
            "ans": 0,
            "fb": "Chính xác! $\\lim_{n \\to \\infty} P(|\\bar{X}_n - \\mu| < \\epsilon) = 1$."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Một sòng bạc hoạt động có lãi dựa trên nguyên lý toán học nào sau đây?",
            "opts": [
                  "Bất đẳng thức Jensen",
                  "Luật số lớn: khi số lượt chơi $n$ đủ lớn, tỷ lệ thắng trung bình của nhà cái hội tụ chắc chắn về kỳ vọng dương",
                  "Định lý Bayes",
                  "Phân phối Chi-bình phương"
            ],
            "ans": 1,
            "fb": "Đúng! Lợi nhuận của nhà cái được đảm bảo bằng Luật số lớn với hàng triệu lượt cược."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Một người tung đồng xu thấy ra 10 lần liên tiếp mặt Ngửa, liền tin rằng lần thứ 11 chắc chắn khả năng ra Sấp cao hơn để 'bù đắp lại'. Sai lầm tâm lý này gọi là:",
            "opts": [
                  "Quy luật bù trừ xác suất Kolmogorov",
                  "Hội tụ theo phân phối",
                  "Nghịch lý Simpson",
                  "Ngụy biện con bạc (Gambler's fallacy) — Luật số lớn làm 'loãng' chứ không 'bù trừ'"
            ],
            "ans": 3,
            "fb": "Chính xác! Các lần tung là độc lập, đồng xu không có trí nhớ, xác suất lần thứ 11 ra Sấp vẫn là 0,5."
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
