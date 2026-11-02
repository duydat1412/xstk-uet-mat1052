// ==========================================================================
// CỤM E: BIẾN LIÊN TỤC & ĐỊNH LÝ GIỚI HẠN TRUNG TÂM (CLT)
// Bao gồm: Bài E1, E2, E3, E4, E5, E6
// Nguồn: Slide UET Week 07 (tr. 41–77, 82–91); Stat20 Chương 4 (Mục 4.15, 4.16, 4.17)
// Kiểm chứng số học: verify/verify_cum_e.py
// ==========================================================================

const CUM_E = [
  {
    id: "E1",
    cluster: "E",
    title: "Biến ngẫu nhiên liên tục, Hàm mật độ (pdf) & Hàm tích lũy (cdf)",
    sources: "Slide Week 07 (tr. 41–47, 82–83); Stat20 Mục 4.15",
    ref: {
      "slide_file": "week07.pdf",
      "slide_name": "Tuần 07 — Biến liên tục, Hàm mật độ (pdf) & Hàm cdf",
      "pages": "Slide 41 – 47, 82 – 83",
      "page_start": 41,
      "section": "Phần 4: Biến ngẫu nhiên liên tục, Hàm mật độ pdf & Hàm tích lũy cdf (Slide 41–47) & Bài tập vận dụng 2 (Slide 82–83)",
      "stat20": "Stat20 Mục 4.15 (Continuous Random Variables & Probability Density)",
      "key_points": [
            "Hàm mật độ f(x) ≥ 0, điều kiện chuẩn hóa: ∫(-∞→∞) f(x)dx = 1",
            "Xác suất tại một điểm luôn bằng 0: P(X = c) = 0 ⇒ P(a ≤ X ≤ b) = P(a < X < b) = ∫(a→b) f(x)dx",
            "Hàm tích lũy F(x) = ∫(-∞→x) f(t)dt, liên tục trên R và f(x) = F'(x) tại các điểm khả vi"
      ],
      "remind": "Nếu bạn chưa vững kỹ năng tích phân tìm tham số k để hàm là mật độ hợp lệ, hãy đọc Slide Week 07 trang 42–46 và lời giải mẫu Bài tập 2 ở Slide 82–83."
},
    desc: "Bước chuyển từ rời rạc sang liên tục: Xác suất tại 1 điểm luôn bằng 0, xác suất là DIỆN TÍCH tích phân dưới đường cong mật độ, mối liên hệ giải tích f(x) = F'(x).",
    steps: [
      {
        t: "Biến ngẫu nhiên liên tục & Hàm mật độ xác suất (pdf)",
        c: `<p><b>Biến ngẫu nhiên liên tục $X$</b> có thể nhận bất kỳ giá trị thực nào trong một khoảng hoặc trên toàn bộ trục số (chiều cao, thời gian, trọng lượng).</p>
            <p>Quy luật xác suất của $X$ được mô tả bởi <b>Hàm mật độ xác suất $f_X(x)$ (Probability Density Function - pdf)</b>:</p>
            <ol>
              <li>$f_X(x) \\ge 0$ với mọi $x \\in \\mathbb{R}$.</li>
              <li>Tổng diện tích dưới toàn bộ đường cong mật độ luôn bằng đúng 1:
                  $$\\int_{-\\infty}^{+\\infty} f_X(x) \\, dx = 1$$
              </li>
            </ol>`
      },
      {
        t: "Điểm cốt tử: Xác suất là DIỆN TÍCH & P(X = c) = 0",
        c: `<p>Với biến liên tục, xác suất để $X$ rơi vào đoạn $[a, b]$ chính là <b>diện tích hình phẳng</b> nằm dưới đường cong mật độ từ $a$ đến $b$:</p>
            $$P(a \\le X \\le b) = \\int_{a}^{b} f_X(x) \\, dx$$
            <div class="warn-box">
              <b>⚠️ NGUYÊN LÝ SỐNG CÒN TRONG PHÒNG THI:</b><br>
              1. <b>Xác suất tại MỘT ĐIỂM BẤT KỲ luôn luôn bằng đúng 0:</b>
                 $$P(X = c) = \\int_{c}^{c} f_X(x) \\, dx = 0$$
                 <i>(Vì một điểm đơn lẻ không có chiều rộng, diện tích bằng 0).</i><br>
              2. <b>Dấu bằng không làm thay đổi xác suất:</b>
                 $$P(a \\le X \\le b) = P(a &lt; X \\le b) = P(a \\le X &lt; b) = P(a &lt; X &lt; b)$$
                 <i>(Bạn không cần phải bận tâm có lấy dấu bằng ở đầu mút hay không!).</i>
            </div>`
      },
      {
        t: "Hàm phân phối tích lũy (cdf) & Mối liên hệ giải tích",
        c: `<p><b>Hàm phân phối tích lũy $F_X(x)$</b> đo diện tích tích lũy từ $-\\infty$ đến $x$:</p>
            $$F_X(x) = P(X \\le x) = \\int_{-\\infty}^{x} f_X(t) \\, dt$$
            <p><b>Mối liên hệ giải tích (Đạo hàm và Tích phân):</b></p>
            <ul>
              <li>Có $f(x) \\implies$ <b>Tích phân</b> để tìm $F(x)$: $F(x) = \\int_{-\\infty}^x f(t)dt$.</li>
              <li>Có $F(x) \\implies$ <b>Đạo hàm</b> để tìm $f(x)$: $f_X(x) = F_X'(x) = \\frac{d}{dx} F_X(x)$ tại các điểm khả vi.</li>
              <li>Tính xác suất trên đoạn bằng hàm tích lũy:
                  $$P(a \\le X \\le b) = F_X(b) - F_X(a)$$
              </li>
            </ul>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 07 — Ví dụ 11] Kiểm tra Hàm mật độ xác suất liên tục",
        q: "Xét hàm số xác định trên toàn bộ trục số thực (Slide 43–44):<br>" +
           "$$f(x) = \\begin{cases} 1{,}5 (1 - x^2) & \\text{khi } 0 \\le x \\le 1 \\cr 0 & \\text{ở ngoài} \\end{cases}$$<br>" +
           "a) Chứng minh rằng $f(x)$ là một hàm mật độ xác suất (pdf) hợp lệ.<br>" +
           "b) Tính xác suất để biến ngẫu nhiên $X$ nhận giá trị trong đoạn $[0; 0{,}5]$.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 07 (trang 44):</b><br>" +
             "a) Kiểm tra 2 điều kiện tiên đề của hàm mật độ:<br>" +
             "   1. Hàm không âm: Với mọi $0 \\le x \\le 1$, $1 - x^2 \\ge 0 \\implies f(x) \\ge 0$.<br>" +
             "   2. Tích phân trên toàn trục số bằng 1:<br>" +
             "      $$\\int_{-\\infty}^\\infty f(x)dx = \\int_0^1 1{,}5(1 - x^2)dx = 1{,}5 \\left[x - \\frac{x^3}{3}\\right]_0^1 = 1{,}5 \\left(1 - \\frac{1}{3}\\right) = 1{,}5 \\times \\frac{2}{3} = 1$$<br>" +
             "   Vậy $f(x)$ là hàm mật độ xác suất hợp lệ.<br>" +
             "b) Xác suất $P(0 \\le X \\le 0{,}5)$:<br>" +
             "   $$P(0 \\le X \\le 0{,}5) = \\int_0^{0{,}5} 1{,}5(1 - x^2)dx = 1{,}5 \\left[0{,}5 - \\frac{(0{,}5)^3}{3}\\right] = 1{,}5 \\left(0{,}5 - \\frac{0{,}125}{3}\\right) = 0{,}6875 \\text{ (hay 68{,}75\\%)}$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 07 — Ví dụ 12] Tìm Hàm tích lũy cdf từ Hàm mật độ",
        q: "Cho biến ngẫu nhiên liên tục $X$ có hàm mật độ (Slide 46–47):<br>" +
           "$$f_X(x) = \\begin{cases} \\frac{3}{8} x^2 & \\text{khi } 0 \\le x \\le 2 \\cr 0 & \\text{ở ngoài} \\end{cases}$$<br>" +
           "Hãy xác định hàm phân phối tích lũy $F_X(x) = P(X \\le x)$ trên toàn bộ $\\mathbb{R}$.",
        sol: "<b>Lời giải chi tiết theo Slide Week 07 (trang 47):</b><br>" +
             "1. Khi $x < 0$: Vì $f(t) = 0$ nên $F_X(x) = \\int_{-\\infty}^x 0 dt = 0$.<br>" +
             "2. Khi $0 \\le x \\le 2$:<br>" +
             "   $$F_X(x) = \\int_{-\\infty}^0 0 dt + \\int_0^x \\frac{3}{8} t^2 dt = \\left[\\frac{3}{8} \\cdot \\frac{t^3}{3}\\right]_0^x = \\frac{x^3}{8}$$<br>" +
             "3. Khi $x > 2$: Tích phân bao trùm toàn bộ miền xác định nên $F_X(x) = 1$.<br>" +
             "<b>Kết luận hàm cdf:</b><br>" +
             "$$F_X(x) = \\begin{cases} 0 & \\text{khi } x < 0 \\cr \\frac{x^3}{8} & \\text{khi } 0 \\le x \\le 2 \\cr 1 & \\text{khi } x > 2 \\end{cases}$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 07 — Bài tập 2] Bài toán Xác định Tham số Cận trên b",
        q: "Biến ngẫu nhiên liên tục $X$ nhận giá trị trong đoạn $[0, b]$ với $b > 0$ (Slide 82–83). Hàm phân phối tích lũy trên đoạn này là $F_X(x) = \\frac{x^2}{9}$ (với $0 \\le x \\le b$).<br>" +
           "a) Tìm giá trị của hằng số $b$.<br>" +
           "b) Tìm hàm mật độ xác suất $f_X(x)$ và tính $P(1 \\le X \\le 2)$.",
        sol: "<b>Lời giải mẫu bài thi theo Slide Week 07 (trang 83):</b><br>" +
             "a) Vì $X$ là biến liên tục nên hàm tích lũy $F_X(x)$ liên tục tại cận trên $b$ và đạt giá trị $1$:<br>" +
             "   $$F_X(b) = 1 \\iff \\frac{b^2}{9} = 1 \\iff b^2 = 9 \\implies b = 3 \\quad (\\text{do } b > 0)$$<br>" +
             "b) Hàm mật độ $f_X(x)$ là đạo hàm của hàm tích lũy $F_X'(x)$ trên khoảng $(0, 3)$:<br>" +
             "   $$f_X(x) = F_X'(x) = \\left(\\frac{x^2}{9}\\right)' = \\frac{2x}{9} \\quad (0 < x < 3)$$<br>" +
             "   Xác suất $P(1 \\le X \\le 2)$ tính trực tiếp qua hàm tích lũy cdf:<br>" +
             "   $$P(1 \\le X \\le 2) = F_X(2) - F_X(1) = \\frac{2^2}{9} - \\frac{1^2}{9} = \\frac{4}{9} - \\frac{1}{9} = \\frac{3}{9} = \\frac{1}{3} \\approx 0{,}3333$$"
      }
    
    ],
    pitfalls: [
      {
        bad: "Nghĩ rằng với biến liên tục, giá trị hàm mật độ f(x) chính là xác suất P(X = x).",
        good: "f(x) là MẬT ĐỘ, không phải xác suất! Giá trị f(x) hoàn toàn có thể lớn hơn 1 (ví dụ f(x) = 10 trên [0; 0,1]). Xác suất là DIỆN TÍCH tích phân, và tại 1 điểm luôn P(X = x) = 0!"
      },
      {
        bad: "Phân vân giữa P(X < 3) và P(X ≤ 3) khi giải bài toán biến liên tục.",
        good: "Với biến liên tục, P(X < 3) và P(X ≤ 3) LÀ HOÀN TOÀN NHƯ NHAU vì P(X = 3) = 0!"
      }
    ],
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Với biến ngẫu nhiên liên tục $X$, xác suất tại một điểm đơn lẻ bất kỳ $P(X = c)$ luôn bằng:",
            "opts": [
                  "$0$",
                  "$f(c)$",
                  "$1$",
                  "$F(c)$"
            ],
            "ans": 0,
            "fb": "Chính xác! Diện tích dưới đường cong tại một điểm có độ rộng bằng 0 nên xác suất luôn bằng 0."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Hàm mật độ $f(x) = 2x$ với $0 \\le x \\le 1$. Xác suất $P(0{,}2 \\le X \\le 0{,}6)$ bằng:",
            "opts": [
                  "$0{,}80$",
                  "$\\int_{0{,}2}^{0{,}6} 2x dx = [x^2]_{0{,}2}^{0{,}6} = 0{,}36 - 0{,}04 = 0{,}32$",
                  "$0{,}16$",
                  "$0{,}40$"
            ],
            "ans": 1,
            "fb": "Đúng! $P(a \\le X \\le b) = \\int_a^b f(x) dx = 0{,}36 - 0{,}04 = 0{,}32$."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Cho hàm mật độ $f(x) = k e^{-3x}$ với $x > 0$. Hằng số $k$ bằng:",
            "opts": [
                  "$1$",
                  "$e^3$",
                  "$3$",
                  "$1/3$"
            ],
            "ans": 2,
            "fb": "Chính xác! $\\int_0^\\infty k e^{-3x} dx = k/3 = 1 \\implies k = 3$."
      }
],
    final_quiz: {
      q: "Cho X là biến ngẫu nhiên liên tục có hàm mật độ f(x). Khẳng định nào sau đây là CHÍNH XÁC?",
      opts: [
        "P(X = 5) = 0 và P(2 < X < 4) = P(2 ≤ X ≤ 4)",
        "P(X = 5) = f(5)",
        "Giá trị của hàm mật độ f(x) không bao giờ được vượt quá 1",
        "P(2 < X < 4) khác với P(2 ≤ X ≤ 4)"
      ],
      ans: 0,
      fb: [
        "Chính xác! Đối với biến liên tục, xác suất tại một điểm luôn bằng 0, do đó việc lấy hay không lấy dấu bằng tại đầu mút không làm thay đổi diện tích tích phân.",
        "Sai! f(5) là tung độ mật độ tại điểm x = 5, xác suất tại một điểm đơn lẻ luôn bằng 0.",
        "Sai! Hàm mật độ f(x) hoàn toàn có thể lớn hơn 1 miễn sao tích phân toàn cục bằng 1.",
        "Sai! Hai khoảng này có cùng diện tích."
      ]
    }
  },

  {
    id: "E2",
    cluster: "E",
    title: "Kỳ vọng & Phương sai của Biến ngẫu nhiên liên tục",
    sources: "Slide Week 07 (tr. 48–49); Stat20 Mục 4.15",
    ref: {
      "slide_file": "week07.pdf",
      "slide_name": "Tuần 07 — Kỳ vọng & Phương sai của biến liên tục",
      "pages": "Slide 48 – 49",
      "page_start": 48,
      "section": "Phần 4: Kỳ vọng và phương sai của biến ngẫu nhiên liên tục (Slide 48–49)",
      "stat20": "Stat20 Mục 4.15 (Expectation & Variance for Continuous Variables)",
      "key_points": [
            "Kỳ vọng liên tục: E(X) = ∫(-∞→∞) x*f(x)dx; E[g(X)] = ∫(-∞→∞) g(x)*f(x)dx",
            "Phương sai: Var(X) = ∫(-∞→∞) x^2*f(x)dx - [E(X)]^2",
            "Kỹ năng giải tích: Tích phân từng phần ∫u dv = uv - ∫v du là công cụ bắt buộc trong bài thi tự luận UET"
      ],
      "remind": "Nếu bạn hay tính nhầm tích phân từng phần khi tìm E(X) hoặc Var(X), hãy mở Slide Week 07 trang 48–49 để xem kỹ các bước biến đổi mẫu."
},
    desc: "Tính toán kỳ vọng E(X) và phương sai Var(X) bằng tích phân. Quy tắc công thức rút gọn và bảo toàn tính chất tuyến tính của kỳ vọng và phương sai.",
    steps: [
      {
        t: "Công thức tích phân tính Kỳ vọng & Phương sai",
        c: `<p>Để chuyển từ rời rạc sang liên tục, ta chỉ cần <b>thay dấu tổng $\\sum$ bằng dấu tích phân $\\int$</b> và thay $p_X(x)$ bằng $f_X(x) \\, dx$:</p>
            <ul>
              <li><b>Kỳ vọng toán học:</b>
                  $$E(X) = \\int_{-\\infty}^{+\\infty} x \\cdot f_X(x) \\, dx$$
              </li>
              <li><b>Kỳ vọng của hàm $g(X)$ (LOTUS liên tục):</b>
                  $$E[g(X)] = \\int_{-\\infty}^{+\\infty} g(x) \\cdot f_X(x) \\, dx$$
                  <i>(Đặc biệt: $E(X^2) = \\int_{-\\infty}^{+\\infty} x^2 \\cdot f_X(x) \\, dx$)</i>
              </li>
              <li><b>Phương sai và Độ lệch chuẩn:</b>
                  $$\\operatorname{Var}(X) = E(X^2) - [E(X)]^2$$
                  $$\\operatorname{SD}(X) = \\sqrt{\\operatorname{Var}(X)}$$
              </li>
            </ul>`
      },
      {
        t: "Bảo toàn tính chất Tuyến tính",
        c: `<p>Mọi tính chất đại số đã học ở Cụm C vẫn <b>hoàn toàn chính xác</b> đối với biến liên tục:</p>
            $$E(aX + b) = a \\cdot E(X) + b$$
            $$\\operatorname{Var}(aX + b) = a^2 \\cdot \\operatorname{Var}(X)$$
            $$\\operatorname{SD}(aX + b) = |a| \\cdot \\operatorname{SD}(X)$$`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 07 — Ví dụ 13] Kỳ vọng biến ngẫu nhiên liên tục",
        q: "Cho biến ngẫu nhiên liên tục $X$ có hàm mật độ xác suất: $f(x) = 2x$ khi $0 < x < 1$ (và bằng 0 ở ngoài, Slide 49). Hãy tính kỳ vọng $E(X)$.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 07 (trang 49):</b><br>" +
             "Áp dụng định nghĩa kỳ vọng của biến ngẫu nhiên liên tục:<br>" +
             "$$E(X) = \\int_{-\\infty}^\\infty x f(x)dx = \\int_0^1 x \\cdot (2x)dx = \\int_0^1 2x^2 dx$$<br>" +
             "$$E(X) = \\left[\\frac{2x^3}{3}\\right]_0^1 = \\frac{2(1)^3}{3} - 0 = \\frac{2}{3} \\approx 0{,}6667$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 07 — Ví dụ 13] Phương sai và Độ lệch chuẩn qua Tích phân",
        q: "Vẫn với biến ngẫu nhiên liên tục $X$ ở trên ($f(x) = 2x$ trên $(0, 1)$, $E(X) = 2/3$).<br>" +
           "a) Tính mô-men bậc hai $E(X^2)$.<br>" +
           "b) Tính phương sai $\\operatorname{Var}(X)$ và độ lệch chuẩn $\\operatorname{SD}(X)$.",
        sol: "<b>Lời giải chi tiết theo Slide Week 07 (trang 49):</b><br>" +
             "a) Tính $E(X^2)$ bằng tích phân:<br>" +
             "   $$E(X^2) = \\int_0^1 x^2 f(x)dx = \\int_0^1 x^2 \\cdot (2x)dx = \\int_0^1 2x^3 dx = \\left[\\frac{2x^4}{4}\\right]_0^1 = \\frac{1}{2} = 0{,}5$$<br>" +
             "b) Áp dụng công thức rút gọn tính phương sai:<br>" +
             "   $$\\operatorname{Var}(X) = E(X^2) - [E(X)]^2 = \\frac{1}{2} - \\left(\\frac{2}{3}\\right)^2 = \\frac{1}{2} - \\frac{4}{9} = \\frac{9 - 8}{18} = \\frac{1}{18} \\approx 0{,}0556$$<br>" +
             "   Độ lệch chuẩn:<br>" +
             "   $$\\operatorname{SD}(X) = \\sqrt{\\operatorname{Var}(X)} = \\frac{1}{\\sqrt{18}} = \\frac{1}{3\\sqrt{2}} \\approx 0{,}2357$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 07 — Bài tập 2 Ý 3] Kỳ vọng và Phương sai từ Bài tập mẫu UET",
        q: "Từ Bài tập 2 ở Slide 83: Biến ngẫu nhiên $X$ có hàm mật độ $f(x) = \\frac{2x}{9}$ trên khoảng $(0, 3)$. Hãy tính kỳ vọng $E(X)$ và phương sai $\\operatorname{Var}(X)$.",
        sol: "<b>Lời giải mẫu tự luận theo Slide Week 07 (trang 83):</b><br>" +
             "1. Tính kỳ vọng $E(X)$:<br>" +
             "   $$E(X) = \\int_0^3 x \\cdot \\left(\\frac{2x}{9}\\right)dx = \\int_0^3 \\frac{2x^2}{9}dx = \\left[\\frac{2x^3}{27}\\right]_0^3 = \\frac{2 \\times 27}{27} = 2$$<br>" +
             "2. Tính $E(X^2)$:<br>" +
             "   $$E(X^2) = \\int_0^3 x^2 \\cdot \\left(\\frac{2x}{9}\\right)dx = \\int_0^3 \\frac{2x^3}{9}dx = \\left[\\frac{2x^4}{36}\\right]_0^3 = \\left[\\frac{x^4}{18}\\right]_0^3 = \\frac{81}{18} = 4{,}5$$<br>" +
             "3. Tính phương sai:<br>" +
             "   $$\\operatorname{Var}(X) = E(X^2) - [E(X)]^2 = 4{,}5 - 2^2 = 4{,}5 - 4 = 0{,}5$$"
      }
    
    ],
    pitfalls: [
      {
        bad: "Quên nhân x vào f(x) khi tính kỳ vọng (chỉ lấy tích phân của f(x)).",
        good: "Tích phân của mỗi f(x) luôn bằng 1! Kỳ vọng BẮT BUỘC phải là tích phân của x * f(x)!"
      },
      {
        bad: "Lấy tích phân của x bình phương rồi bình phương luôn kết quả để tìm Var(X).",
        good: "Phương sai luôn là E(X^2) trừ đi [E(X)]^2. Tuyệt đối không nhầm lẫn thứ tự phép tính!"
      }
    ],
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Kỳ vọng của biến ngẫu nhiên liên tục có hàm mật độ $f(x)$ được tính bằng công thức:",
            "opts": [
                  "$E[X] = \\int_{-\\infty}^{+\\infty} x^2 f(x) dx$",
                  "$E[X] = \\int_{-\\infty}^{+\\infty} f(x) dx$",
                  "$E[X] = \\sum x f(x)$",
                  "$E[X] = \\int_{-\\infty}^{+\\infty} x f(x) dx$"
            ],
            "ans": 3,
            "fb": "Chính xác! Định nghĩa tích phân kỳ vọng liên tục."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Nếu hàm mật độ $f(x)$ đối xứng qua điểm $x = 5$ và kỳ vọng tồn tại, thì $E[X]$ bằng:",
            "opts": [
                  "$10$",
                  "$2{,}5$",
                  "$5$",
                  "$0$"
            ],
            "ans": 2,
            "fb": "Đúng! Do tính đối xứng của hàm mật độ, tâm đối xứng chính là kỳ vọng."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Cho $f(x) = 3x^2$ trên đoạn $[0, 1]$. Phương sai $\\text{Var}(X)$ bằng:",
            "opts": [
                  "$0{,}125$",
                  "$\\frac{3}{5} - \\left(\\frac{3}{4}\\right)^2 = 0{,}6 - 0{,}5625 = 0{,}0375$",
                  "$0{,}75$",
                  "$0{,}0625$"
            ],
            "ans": 1,
            "fb": "Chính xác! $E[X] = \\int_0^1 3x^3 dx = 3/4$. $E[X^2] = \\int_0^1 3x^4 dx = 3/5$. $\\text{Var}(X) = 0{,}6 - (0{,}75)^2 = 0{,}0375$."
      }
],
    final_quiz: {
      q: "Cho X có hàm mật độ f(x) = 2x trên (0, 1). Đã biết E(X) = 2/3 và E(X²) = 1/2. Phương sai Var(X) bằng bao nhiêu?",
      opts: [
        "1/18 (≈ 0,0556)",
        "1/6",
        "2/9",
        "1/9"
      ],
      ans: 0,
      fb: [
        "Chính xác! Var(X) = E(X²) - [E(X)]² = 1/2 - (2/3)² = 1/2 - 4/9 = 1/18.",
        "Sai! Bạn đã lấy 1/2 - 2/3 hoặc tính nhầm mẫu số.",
        "Sai! 2/9 là tích phân khác.",
        "Sai! 1/9 là kết quả thiếu quy đồng mẫu số."
      ]
    }
  },

  {
    id: "E3",
    cluster: "E",
    title: "Phân phối Đều U(a, b): Mật độ phẳng & Tỉ lệ độ dài",
    sources: "Slide Week 07 (tr. 50–53); Stat20 Mục 4.16.1",
    ref: {
      "slide_file": "week07.pdf",
      "slide_name": "Tuần 07 — Phân phối Đều U(a, b)",
      "pages": "Slide 50 – 53",
      "page_start": 50,
      "section": "Phần 5: Các phân phối liên tục đặc biệt — Phân phối Đều U(a, b) (Slide 50–53)",
      "stat20": "Stat20 Mục 4.16.1 (Uniform Distribution)",
      "key_points": [
            "Hàm mật độ không đổi: f(x) = 1 / (b - a) trên đoạn [a, b]",
            "Xác suất tỉ lệ thuận với độ dài khoảng con: P(c ≤ X ≤ d) = (d - c) / (b - a)",
            "Đặc trưng số học: Kỳ vọng E(X) = (a + b)/2 (trung điểm); Phương sai Var(X) = (b - a)^2 / 12"
      ],
      "remind": "Nếu bạn gặp bài toán thời gian chờ xe buýt hoặc đồng hồ ngẫu nhiên, hãy mở Slide Week 07 trang 50–53 về mô hình phân phối Đều."
},
    desc: "Phân phối liên tục đơn giản nhất: Xác suất tỉ lệ thuận trực tiếp với độ dài khoảng. Công thức kỳ vọng trung điểm (a+b)/2 và phương sai (b-a)²/12.",
    steps: [
      {
        t: "Định nghĩa Phân phối Đều (Uniform Distribution)",
        c: `<p>Biến ngẫu nhiên $X$ có <b>Phân phối đều trên khoảng $(a, b)$</b> (ký hiệu $X \\sim U(a, b)$) nếu mật độ xác suất là <b>hằng số phẳng</b> trên toàn bộ khoảng:</p>
            $$f_X(x) = \\begin{cases} \\frac{1}{b - a}, &amp; a \\le x \\le b \\\\ 0, &amp; \\text{ngược lại} \\end{cases}$$
            <p><b>Hình dạng:</b> Là một hình chữ nhật có đáy bằng $b - a$ và chiều cao bằng $\\frac{1}{b - a}$ $\\implies$ Diện tích đúng bằng $(b - a) \\times \\frac{1}{b - a} = 1$.</p>`
      },
      {
        t: "Công thức tính nhanh Xác suất, Kỳ vọng & Phương sai",
        c: `<p>Với phân phối đều, bạn <b>không cần tính tích phân</b> mà có thể dùng trực tiếp diện tích hình chữ nhật:</p>
            <ul>
              <li><b>Xác suất rơi vào khoảng con $[c, d] \\subseteq [a, b]$:</b>
                  $$P(c \\le X \\le d) = \\frac{d - c}{b - a} = \\frac{\\text{Độ dài khoảng con}}{\\text{Độ dài toàn khoảng}}$$
              </li>
              <li><b>Hàm phân phối tích lũy:</b>
                  $$F_X(x) = \\frac{x - a}{b - a} \\quad (a \\le x \\le b)$$
              </li>
              <li><b>Kỳ vọng (Chính là trung điểm của đoạn):</b>
                  $$E(X) = \\frac{a + b}{2}$$
              </li>
              <li><b>Phương sai & Độ lệch chuẩn:</b>
                  $$\\operatorname{Var}(X) = \\frac{(b - a)^2}{12}, \\quad \\operatorname{SD}(X) = \\frac{b - a}{\\sqrt{12}}$$
              </li>
            </ul>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 07 — Ví dụ 14] Thời điểm xe buýt đến bến qua Phân phối Đều",
        q: "Thời điểm xe buýt đến bến được mô hình hóa là phân phối đều từ 0 đến 10 phút, tức $X \\sim U(0, 10)$ (Slide 51–53).<br>" +
           "a) Viết hàm mật độ xác suất $f(x)$ của $X$.<br>" +
           "b) Tính xác suất xe buýt đến bến trong khoảng từ 3 đến 7 phút.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 07 (trang 53):</b><br>" +
             "a) Với phân phối đều $X \\sim U(a = 0, b = 10)$, hàm mật độ là hằng số trên $[0, 10]$:<br>" +
             "   $$f(x) = \\frac{1}{b - a} = \\frac{1}{10 - 0} = 0{,}1 \\quad (0 \\le x \\le 10)$$<br>" +
             "b) Xác suất trên khoảng con tỉ lệ thuận với độ dài của khoảng đó:<br>" +
             "   $$P(3 \\le X \\le 7) = \\frac{7 - 3}{b - a} = \\frac{4}{10} = 0{,}4 \\text{ (hay 40\\%)}$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 07 — Slide 50–53] Đặc trưng số học của Phân phối Đều",
        q: "Với thời gian chờ xe buýt $X \\sim U(0, 10)$ ở trên (Slide 50–53). Hãy tính kỳ vọng $E(X)$, phương sai $\\operatorname{Var}(X)$ và độ lệch chuẩn $\\operatorname{SD}(X)$.",
        sol: "<b>Lời giải chi tiết theo Slide Week 07 (trang 50):</b><br>" +
             "1. Kỳ vọng của phân phối đều nằm tại chính giữa đoạn $[a, b]$:<br>" +
             "   $$E(X) = \\frac{a + b}{2} = \\frac{0 + 10}{2} = 5 \\text{ phút}$$<br>" +
             "2. Phương sai tính theo công thức chuẩn giải tích:<br>" +
             "   $$\\operatorname{Var}(X) = \\frac{(b - a)^2}{12} = \\frac{(10 - 0)^2}{12} = \\frac{100}{12} = \\frac{25}{3} \\approx 8{,}3333 \\text{ phút}^2$$<br>" +
             "3. Độ lệch chuẩn:<br>" +
             "   $$\\operatorname{SD}(X) = \\sqrt{\\frac{25}{3}} = \\frac{5}{\\sqrt{3}} \\approx 2{,}8868 \\approx 2{,}887 \\text{ phút}$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 07 — Slide 51–53] Xác suất có điều kiện của Phân phối Đều",
        q: "Vẫn với thời gian xe buýt $X \\sim U(0, 10)$. Bạn đã đứng đợi tại bến xe được đúng 4 phút mà xe vẫn chưa tới ($X > 4$). Tính xác suất để xe buýt sẽ đến trong vòng 2 phút tiếp theo (tức $X \\le 6$).",
        sol: "<b>Lời giải xác suất có điều kiện theo Slide Week 07:</b><br>" +
             "1. Yêu cầu bài toán là tính $P(X \\le 6 \\mid X > 4)$, tức $P(4 < X \\le 6 \\mid X > 4)$.<br>" +
             "2. Theo công thức xác suất có điều kiện:<br>" +
             "   $$P(X \\le 6 \\mid X > 4) = \\frac{P(4 < X \\le 6)}{P(X > 4)}$$<br>" +
             "3. Ta có $P(4 < X \\le 6) = \\frac{6 - 4}{10} = \\frac{2}{10} = 0{,}2$, và $P(X > 4) = \\frac{10 - 4}{10} = \\frac{6}{10} = 0{,}6$.<br>" +
             "   $$P(X \\le 6 \\mid X > 4) = \\frac{0{,}2}{0{,}6} = \\frac{2}{6} = \\frac{1}{3} \\approx 0{,}3333 \\text{ (hay 33{,}33\\%)}$$"
      }
    
    ],
    pitfalls: [
      {
        bad: "Chia nhầm mẫu số phương sai phân phối đều: chia cho 2 hoặc 4 thay vì 12.",
        good: "Công thức phương sai phân phối đều có mẫu số cố định là 12: Var = (b - a)^2 / 12!"
      },
      {
        bad: "Tưởng rằng phân phối đều có tính không nhớ (như phân phối mũ).",
        good: "Phân phối đều KHÔNG CÓ tính không nhớ! Đã chờ 4 phút thì không gian thời gian còn lại thu hẹp chỉ còn từ 4 đến 10 phút."
      }
    ],
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Cho $X \\sim \\text{Uniform}(a, b)$. Phương sai của $X$ là:",
            "opts": [
                  "$\\frac{b - a}{2}$",
                  "$\\frac{b + a}{12}$",
                  "$\\frac{(b - a)^2}{2}$",
                  "$\\frac{(b - a)^2}{12}$"
            ],
            "ans": 3,
            "fb": "Chính xác! Công thức giải tích phương sai phân phối đều."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Xe buýt đến trạm ngẫu nhiên đều trong khoảng từ 0 đến 10 phút ($X \\sim \\text{Uniform}(0, 10)$). Xác suất phải chờ từ 3 đến 7 phút là:",
            "opts": [
                  "$\\frac{7 - 3}{10 - 0} = 0{,}40$",
                  "$0{,}70$",
                  "$0{,}30$",
                  "$0{,}50$"
            ],
            "ans": 0,
            "fb": "Đúng! Với phân phối đều, xác suất bằng tỉ lệ độ dài khoảng con trên tổng độ dài: $4/10 = 0{,}40$."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Cho $X \\sim \\text{Uniform}(0, 10)$. Biết rằng đã chờ hơn 4 phút ($X > 4$), kỳ vọng thời gian chờ là:",
            "opts": [
                  "$8\\text{ phút}$",
                  "$5\\text{ phút}$",
                  "$6\\text{ phút}$",
                  "$7\\text{ phút}$"
            ],
            "ans": 3,
            "fb": "Chính xác! Phân phối có điều kiện của $X$ khi biết $X > 4$ là $\\text{Uniform}(4, 10) \\implies E = (4 + 10)/2 = 7$ phút."
      }
],
    final_quiz: {
      q: "Biến ngẫu nhiên X có phân phối đều trên đoạn [0, 10]. Xác suất P(X < 3) bằng bao nhiêu?",
      opts: [
        "0,3 (hay 30%)",
        "0,03",
        "3,0",
        "0,7"
      ],
      ans: 0,
      fb: [
        "Chính xác! Mật độ phẳng là 1/10. Diện tích từ 0 đến 3 là 3 * (1/10) = 0,3.",
        "Sai! 0,03 là phép chia nhầm.",
        "Sai! Xác suất không thể vượt quá 1.",
        "Sai! 0,7 là P(X > 3)."
      ]
    }
  },

  {
    id: "E4",
    cluster: "E",
    title: "Phân phối Chuẩn N(μ, σ²): Chuẩn hóa Z & Tra bảng Φ(z)",
    sources: "Slide Week 07 (tr. 54–62, 84–85); Stat20 Mục 4.16.2",
    ref: {
      "slide_file": "week07.pdf",
      "slide_name": "Tuần 07 — Phân phối Chuẩn N(μ, σ²)",
      "pages": "Slide 54 – 62, 84 – 85",
      "page_start": 54,
      "section": "Phần 5: Phân phối Chuẩn Gauss, Chuẩn hóa Z & Tra bảng Laplace (Slide 54–62) & Bài tập vận dụng 3 (Slide 84–85)",
      "stat20": "Stat20 Mục 4.16.2 (Normal Distribution & Z-scores)",
      "key_points": [
            "Đồ thị hình chuông Gauss đối xứng quanh kỳ vọng μ; Điểm uốn tại μ ± σ",
            "Biến đổi chuẩn hóa Z = (X - μ) / σ ~ N(0, 1); Quy tắc tra bảng Φ(z) và tính chất đối xứng Φ(-z) = 1 - Φ(z)",
            "Quy tắc thực nghiệm: 68% trong khoảng μ±1σ, 95% trong khoảng μ±2σ, 99.7% trong khoảng μ±3σ",
            "Bài toán ngược tìm phân vị x_p = μ + z_p * σ và bài toán tải trọng thang máy (Slide 84–85)"
      ],
      "remind": "Phân phối chuẩn chiếm tới 2–3 điểm trong bài thi. Hãy ôn kỹ Slide Week 07 từ trang 54 đến 62 và bài tập thang máy ở Slide 84–85."
},
    desc: "Ông hoàng của lý thuyết thống kê: Phân phối Chuẩn Gauss. Kỹ thuật chuẩn hóa Z-score, quy tắc thực nghiệm 68–95–99,7, tra bảng Φ(z) và bài toán tìm phân vị ngược.",
    steps: [
      {
        t: "Đặc điểm của Phân phối Chuẩn (Normal Distribution)",
        c: `<p>Biến ngẫu nhiên $X$ có <b>Phân phối Chuẩn</b> với trung bình $\\mu$ và phương sai $\\sigma^2$ (ký hiệu $X \\sim \\mathcal{N}(\\mu, \\sigma^2)$):</p>
            <ul>
              <li>Đồ thị là đường cong hình chuông hoàn toàn <b>đối xứng quanh tâm $\\mu$</b>.</li>
              <li>$\\text{Mean} = \\text{Median} = \\text{Mode} = \\mu$.</li>
              <li>Hai điểm uốn của đường cong nằm chính xác tại $\\mu - \\sigma$ và $\\mu + \\sigma$.</li>
            </ul>`
      },
      {
        t: "Kỹ thuật Chuẩn hóa (Z-Score Standardization)",
        c: `<p>Vì mỗi bài toán có $\\mu$ và $\\sigma$ khác nhau, ta không thể in bảng tra cho mọi phân phối. Ta chuyển mọi phân phối chuẩn về <b>Phân phối Chuẩn tắc (Standard Normal) $\\mathcal{N}(0, 1)$</b> thông qua phép đổi biến Z-score:</p>
            $$Z = \\frac{X - \\mu}{\\sigma} \\sim \\mathcal{N}(0, 1)$$
            <p><b>Ý nghĩa của Z:</b> $Z$ cho biết giá trị $X$ đang đứng cách trung bình $\\mu$ bao nhiêu độ lệch chuẩn (dương là cao hơn, âm là thấp hơn).</p>
            <p><b>Hàm phân phối chuẩn tắc $\\Phi(z) = P(Z \\le z)$:</b></p>
            <ul>
              <li>Tính chất đối xứng: $\\Phi(-z) = 1 - \\Phi(z)$.</li>
              <li>Tính xác suất trên đoạn:
                  $$P(a \\le X \\le b) = \\Phi\\left(\\frac{b - \\mu}{\\sigma}\\right) - \\Phi\\left(\\frac{a - \\mu}{\\sigma}\\right)$$
              </li>
            </ul>`
      },
      {
        t: "Quy tắc Thực nghiệm 68–95–99,7 (The Empirical Rule)",
        c: `<div class="tip-box">
              <b>3 con số vàng phản xạ tức thì trong đề thi trắc nghiệm:</b><br>
              - Trong vòng 1 độ lệch chuẩn quanh tâm: $P(\\mu - \\sigma \\le X \\le \\mu + \\sigma) \\approx 68\\%$.<br>
              - Trong vòng 2 độ lệch chuẩn quanh tâm: $P(\\mu - 2\\sigma \\le X \\le \\mu + 2\\sigma) \\approx 95\\%$.<br>
              - Trong vòng 3 độ lệch chuẩn quanh tâm: $P(\\mu - 3\\sigma \\le X \\le \\mu + 3\\sigma) \\approx 99{,}7\\%$.<br>
              <i>Mẹo suy luận đuôi: 95% nằm trong 2 SD $\\implies$ Phần còn lại 5% chia đều cho 2 đuôi, mỗi đuôi có $2{,}5\\%$!</i>
            </div>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 07 — Ví dụ 15] Điểm thi và Chuẩn hóa Z-score",
        q: "Trong một kỳ thi, điểm số có phân phối chuẩn với trung bình $\\mu = 70$ và độ lệch chuẩn $\\sigma = 10$, tức $X \\sim N(70, 10^2)$ (Slide 57). Một sinh viên đạt 85 điểm.<br>" +
           "a) Tính điểm chuẩn hóa $Z$ của sinh viên này.<br>" +
           "b) Tra bảng hàm Laplace $\\Phi(z)$, tính tỉ lệ sinh viên có điểm số cao hơn sinh viên này.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 07 (trang 57):</b><br>" +
             "a) Công thức chuẩn hóa Z-score:<br>" +
             "   $$Z = \\frac{X - \\mu}{\\sigma} = \\frac{85 - 70}{10} = \\frac{15}{10} = 1{,}5$$<br>" +
             "b) Tra bảng phân phối chuẩn tắc: $\\Phi(1{,}5) = P(Z \\le 1{,}5) = 0{,}9332$.<br>" +
             "   Tỉ lệ sinh viên có điểm cao hơn sinh viên này là:<br>" +
             "   $$P(X > 85) = P(Z > 1{,}5) = 1 - \\Phi(1{,}5) = 1 - 0{,}9332 = 0{,}0668 \\text{ (hay 6{,}68\\%)}$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 07 — Ví dụ 16 & 17] Dung tích Đóng chai và Bài toán Phân vị",
        q: "Dung tích một chai nước giải khát (ml) được mô hình hóa bằng phân phối chuẩn $X \\sim N(500, 5^2)$ với $\\mu = 500$ ml và $\\sigma = 5$ ml (Slide 59, 61–62).<br>" +
           "a) Áp dụng quy tắc thực nghiệm 68–95–99.7: Xác định khoảng dung tích chứa 95% số chai.<br>" +
           "b) Tìm phân vị mức $p = 0{,}975$ (ngưỡng dung tích $x_0$ sao cho 97,5% số chai có dung tích không vượt quá $x_0$).",
        sol: "<b>Lời giải chi tiết theo Slide Week 07 (trang 59 & 61):</b><br>" +
             "a) Theo quy tắc thực nghiệm 68–95–99.7, khoảng $[\\mu - 2\\sigma, \\mu + 2\\sigma]$ chứa xấp xỉ 95% số quan sát:<br>" +
             "   $$[500 - 2(5), 500 + 2(5)] = [490, 510] \\text{ ml}$$<br>" +
             "b) Bài toán phân vị ngược:<br>" +
             "   Ta tìm $z_{0{,}975}$ sao cho $\\Phi(z_{0{,}975}) = 0{,}975$. Tra bảng chuẩn tắc được $z_{0{,}975} = 1{,}96$.<br>" +
             "   Chuyển ngược về đơn vị ban đầu:<br>" +
             "   $$x_0 = \\mu + z_{0{,}975} \\cdot \\sigma = 500 + 1{,}96 \\times 5 = 500 + 9{,}8 = 509{,}8 \\text{ ml}$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 07 — Bài tập 3] Bài toán Tải trọng Thang máy UET",
        q: "Khối lượng của người Việt Nam trưởng thành có phân phối chuẩn với trung bình $\\mu = 65$ kg và độ lệch chuẩn $\\sigma = 5$ kg (Slide 84–85). Một thang máy chở tối đa 10 người và có tải trọng giới hạn an toàn là 700 kg. Giả sử 10 người ngẫu nhiên bước vào thang máy có khối lượng độc lập. Tính xác suất thang máy bị quá tải.",
        sol: "<b>Lời giải chuẩn tự luận theo Slide Week 07 (trang 85):</b><br>" +
             "1. Gọi $X_i$ là khối lượng người thứ $i$ ($X_i \\sim N(65, 5^2)$ với $i=1, \\dots, 10$).<br>" +
             "   Tổng khối lượng của 10 người là $S_{10} = \\sum_{i=1}^{10} X_i$.<br>" +
             "2. Vì tổng của các biến chuẩn độc lập cũng là một biến chuẩn:<br>" +
             "   $$E(S_{10}) = 10 \\times \\mu = 10 \\times 65 = 650 \\text{ kg}$$<br>" +
             "   $$\\operatorname{Var}(S_{10}) = 10 \\times \\sigma^2 = 10 \\times 5^2 = 250 \\implies \\operatorname{SD}(S_{10}) = \\sqrt{250} = 5\\sqrt{10} \\approx 15{,}8114 \\text{ kg}$$<br>" +
             "   Do đó: $S_{10} \\sim N(650, 250)$.<br>" +
             "3. Thang máy quá tải khi $S_{10} > 700$ kg. Chuẩn hóa $Z$:<br>" +
             "   $$Z = \\frac{700 - 650}{\\sqrt{250}} = \\frac{50}{15{,}8114} \\approx 3{,}16$$<br>" +
             "   Tra bảng $\\Phi(3{,}16) = 0{,}9992$:<br>" +
             "   $$P(S_{10} > 700) = 1 - \\Phi(3{,}16) = 1 - 0{,}9992 = 0{,}0008 \\text{ (hay 0{,}08\\%)}$$<br>" +
             "   Xác suất quá tải cực kỳ nhỏ, thang máy hoạt động rất an toàn."
      }
    
    ],
    pitfalls: [
      {
        bad: "Nhầm lẫn giữa phương sai σ² và độ lệch chuẩn σ trong ký hiệu N(μ, σ²).",
        good: "Ký hiệu chuẩn là N(μ, σ²), tham số thứ hai là PHƯƠNG SAI! Ví dụ N(50, 100) thì σ = √100 = 10, chứ không phải σ = 100!"
      },
      {
        bad: "Quên tính chất đối xứng Φ(-z) = 1 - Φ(z) khi tra bảng số âm.",
        good: "Bảng tra chuẩn thường chỉ in số z dương. Gặp z âm, luôn đổi sang 1 - Φ(|z|)!"
      }
    ],
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Để chuẩn hóa biến ngẫu nhiên $X \\sim \\mathcal{N}(\\mu, \\sigma^2)$ về biến chuẩn tắc $Z \\sim \\mathcal{N}(0, 1)$, công thức biến đổi là:",
            "opts": [
                  "$Z = \\frac{X - \\mu}{\\sigma}$",
                  "$Z = \\sigma X + \\mu$",
                  "$Z = \\frac{X - \\mu}{\\sigma^2}$",
                  "$Z = \\frac{X - \\sigma}{\\mu}$"
            ],
            "ans": 0,
            "fb": "Chính xác! Lấy biến số trừ kỳ vọng rồi chia cho độ lệch chuẩn $\\sigma$."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Biết $\\Phi(1{,}645) = 0{,}9500$. Giá trị $\\Phi(-1{,}645)$ bằng:",
            "opts": [
                  "$0{,}5000$",
                  "$1 - 0{,}9500 = 0{,}0500$",
                  "$-0{,}9500$",
                  "$0{,}0250$"
            ],
            "ans": 1,
            "fb": "Đúng! Do tính đối xứng: $\\Phi(-z) = 1 - \\Phi(z) \\implies 1 - 0{,}9500 = 0{,}0500$."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Điểm kiểm tra $X \\sim \\mathcal{N}(70, 25)$. Để lọt vào top $2{,}5\\%$ điểm cao nhất (tương ứng $\\Phi(1{,}96) = 0{,}975$), sinh viên cần đạt tối thiểu:",
            "opts": [
                  "$80\\text{ điểm}$",
                  "$75\\text{ điểm}$",
                  "$79{,}8\\text{ điểm}$",
                  "$89{,}6\\text{ điểm}$"
            ],
            "ans": 2,
            "fb": "Chính xác! $\\sigma = \\sqrt{25} = 5$. $x = \\mu + z \\sigma = 70 + 1{,}96(5) = 70 + 9{,}8 = 79{,}8$ điểm."
      }
],
    final_quiz: {
      q: "Cho biến ngẫu nhiên X ~ N(50, 10²). Theo quy tắc thực nghiệm 68–95–99,7, xác suất P(X > 70) xấp xỉ bằng bao nhiêu?",
      opts: [
        "2,5% (0,025)",
        "5% (0,05)",
        "0,15%",
        "16%"
      ],
      ans: 0,
      fb: [
        "Chính xác! Giá trị 70 ứng với Z = (70 - 50)/10 = 2 SD. Khoảng trong 2 SD là 95%, hai đuôi còn lại 5% chia đôi mỗi bên 2,5%. X > 70 là đuôi phải nên bằng 2,5%.",
        "Sai! 5% là tổng diện tích của CẢ HAI ĐUÔI (cả X < 30 và X > 70). Đề chỉ hỏi 1 đuôi phải.",
        "Sai! 0,15% là diện tích của 1 đuôi ở mức 3 SD (Z > 3).",
        "Sai! 16% là diện tích của 1 đuôi ở mức 1 SD (Z > 1)."
      ]
    }
  },

  {
    id: "E5",
    cluster: "E",
    title: "Phân phối Mũ Exp(λ), Chi-bình phương & t-Student",
    sources: "Slide Week 07 (tr. 63–67, 86–88) [CHỈ CÓ TRONG SLIDE UET]",
    ref: {
      "slide_file": "week07.pdf",
      "slide_name": "Tuần 07 — Phân phối Mũ, Chi-bình phương & t-Student",
      "pages": "Slide 63 – 67, 86 – 88",
      "page_start": 63,
      "section": "Phần 5: Phân phối Mũ Exp(λ), Chi-bình phương & t-Student [ĐỘC QUYỀN SLIDE UET] (Slide 63–67) & Bài tập vận dụng 4 (Slide 86–88)",
      "stat20": "Chuyên đề phân phối liên tục mở rộng của Slide UET Week 07",
      "key_points": [
            "Phân phối Mũ Exp(λ): Hàm mật độ f(x) = λ*e^(-λx) (x ≥ 0); Hàm cdf F(x) = 1 - e^(-λx); Xác suất đuôi P(X > x) = e^(-λx)",
            "Đặc trưng: Kỳ vọng E(X) = 1/λ, Phương sai Var(X) = 1/λ^2; Tính chất không nhớ (Memoryless): P(X > s+t | X > s) = P(X > t)",
            "Nhận diện đồ thị phân phối Chi-bình phương (lệch phải, k bậc tự do) và t-Student (hình chuông, đuôi dày hơn chuẩn)"
      ],
      "remind": "Đề thi UET thường có câu hỏi về tính chất không nhớ hoặc kết hợp phân phối Mũ với CLT. Hãy xem Slide Week 07 trang 63–65 và Bài tập 4 ở Slide 86–88."
},
    desc: "Các phân phối liên tục bổ sung quan trọng: Phân phối Mũ mô hình hóa thời gian chờ (không nhớ), giới thiệu nhận diện phân phối χ² và t-Student.",
    steps: [
      {
        t: "Phân phối Mũ (Exponential Distribution) $Exp(\\lambda)$",
        c: `<p><b>Phân phối Mũ</b> với tham số tốc độ $\\lambda &gt; 0$ (ký hiệu $X \\sim Exp(\\lambda)$) mô hình hóa <b>thời gian chờ đợi</b> giữa hai sự kiện Poisson liên tiếp (ví dụ: thời gian chờ cuộc gọi tiếp theo, tuổi thọ linh kiện):</p>
            <ul>
              <li><b>Hàm mật độ:</b> $f_X(x) = \\lambda e^{-\\lambda x}$ ($x \\ge 0$).</li>
              <li><b>Hàm phân phối tích lũy:</b> $F_X(x) = 1 - e^{-\\lambda x}$ ($x \\ge 0$).</li>
              <li><b>Xác suất đuôi phải (sống sót quá thời điểm $x$):</b>
                  $$P(X &gt; x) = 1 - F_X(x) = e^{-\\lambda x}$$
              </li>
              <li><b>Xác suất rơi vào khoảng $(a, b)$:</b>
                  $$P(a &lt; X &lt; b) = e^{-\\lambda a} - e^{-\\lambda b}$$
              </li>
              <li><b>Kỳ vọng và Độ lệch chuẩn:</b> Bằng nhau và cùng bằng $1/\\lambda$:
                  $$E(X) = \\frac{1}{\\lambda}, \\quad \\operatorname{Var}(X) = \\frac{1}{\\lambda^2}, \\quad \\operatorname{SD}(X) = \\frac{1}{\\lambda}$$
              </li>
            </ul>
            <div class="tip-box">
              <b>Tính chất Không có trí nhớ (Memoryless Property):</b><br>
              $$P(X &gt; s + t \\mid X &gt; s) = P(X &gt; t)$$
              <i>Ý nghĩa: Nếu bạn đã đợi xe buýt được $s = 10$ phút mà xe chưa đến, thì xác suất bạn phải đợi thêm ít nhất $t = 5$ phút nữa vẫn y nguyên như lúc bạn mới bước ra bến xe!</i>
            </div>`
      },
      {
        t: "Giới thiệu Phân phối $\\chi^2$ (Chi-bình phương) & $t$-Student",
        c: `<table class="data-table">
              <thead><tr><th>Phân phối</th><th>Định nghĩa bản chất</th><th>Đặc điểm hình dạng</th><th>Ứng dụng chính</th></tr></thead>
              <tbody>
                <tr><td><b>Chi-bình phương $\\chi^2(\\nu)$</b></td><td>Tổng bình phương của $\\nu$ biến chuẩn tắc độc lập: $\\sum_{i=1}^\\nu Z_i^2$.</td><td>Chỉ nhận giá trị dương ($x \\ge 0$), đồ thị lệch phải mạnh khi $\\nu$ nhỏ, tiệm cận đối xứng khi $\\nu$ lớn.</td><td>Kiểm định tính độc lập trong bảng liên hợp, kiểm định phương sai.</td></tr>
                <tr><td><b>$t$-Student ($t_\\nu$)</b></td><td>Tỉ số giữa biến chuẩn tắc $Z$ và căn bậc hai của $\\chi^2$: $T = \\frac{Z}{\\sqrt{\\chi^2/\\nu}}$.</td><td>Hình chuông đối xứng quanh 0 giống phân phối chuẩn, nhưng có <b>đuôi nặng hơn (dày hơn)</b>.</td><td>Suy luận trung bình khi cỡ mẫu nhỏ ($n &lt; 30$) và chưa biết phương sai tổng thể. Khi $\\nu \\to \\infty$, $t_\\nu \\to \\mathcal{N}(0, 1)$.</td></tr>
              </tbody>
            </table>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 07 — Ví dụ 18] Thời gian chờ hệ thống nhận yêu cầu",
        q: "Thời gian chờ từ lúc bắt đầu theo dõi đến khi hệ thống nhận được yêu cầu có phân phối mũ với kỳ vọng $E(X) = 2$ phút (Slide 64–65).<br>" +
           "a) Xác định tham số tốc độ $\\lambda$.<br>" +
           "b) Tính xác suất để phải chờ nhiều hơn 3 phút mới nhận được yêu cầu.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 07 (trang 65):</b><br>" +
             "a) Với phân phối mũ $X \\sim Exp(\\lambda)$, kỳ vọng $E(X) = \\frac{1}{\\lambda}$:<br>" +
             "   $$\\lambda = \\frac{1}{E(X)} = \\frac{1}{2} = 0{,}5 \\text{ (mỗi phút)}$$<br>" +
             "b) Xác suất đuôi của phân phối mũ tính theo công thức trực tiếp $P(X > x) = e^{-\\lambda x}$:<br>" +
             "   $$P(X > 3) = e^{-0{,}5 \\times 3} = e^{-1{,}5} \\approx 0{,}2231 \\text{ (hay 22{,}31\\%)}$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 07 — Slide 63–65] Tính không nhớ (Memoryless Property)",
        q: "Vẫn với hệ thống ở trên ($X \\sim Exp(\\lambda = 0{,}5)$). Giả sử người quản trị đã chờ 4 phút mà hệ thống vẫn chưa nhận được yêu cầu nào ($X > 4$). Tính xác suất để phải chờ thêm ít nhất 3 phút nữa mới có yêu cầu đến (tức $X > 7$).",
        sol: "<b>Chứng minh tính chất không nhớ theo Slide Week 07:</b><br>" +
             "1. Theo công thức xác suất có điều kiện:<br>" +
             "   $$P(X > 4 + 3 \\mid X > 4) = \\frac{P(X > 7)}{P(X > 4)} = \\frac{e^{-0{,}5 \\times 7}}{e^{-0{,}5 \\times 4}} = \\frac{e^{-3{,}5}}{e^{-2{,}0}} = e^{-1{,}5} \\approx 0{,}2231$$<br>" +
             "2. Ta thấy $P(X > 4 + 3 \\mid X > 4) = P(X > 3)$.<br>" +
             "<b>Ý nghĩa:</b> Phân phối mũ 'không có trí nhớ' (Memoryless) — việc bạn đã mất công chờ 4 phút không hề làm tăng hay giảm cơ hội yêu cầu đến ở phút tiếp theo!"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 07 — Bài tập 4] Khoảng cách từ nơi ở đến trường",
        q: "Khoảng cách $X$ (km) từ nơi ở đến trường của một sinh viên có phân phối mũ với kỳ vọng $E(X) = 5$ km và độ lệch chuẩn $\\operatorname{SD}(X) = 5$ km (Slide 86–88).<br>" +
           "a) Xác định tham số $\\lambda$ và viết hàm mật độ $f(x)$.<br>" +
           "b) Tính xác suất một sinh viên sống cách trường trên 10 km.<br>" +
           "c) Nhận diện định tính đồ thị phân phối Chi-bình phương và $t$-Student (Slide 66–67).",
        sol: "<b>Lời giải theo Slide Week 07 (trang 87–88):</b><br>" +
             "a) Tham số tốc độ: $\\lambda = 1/E(X) = 1/5 = 0{,}2$. Hàm mật độ: $f(x) = 0{,}2 e^{-0{,}2 x}$ với $x \\ge 0$.<br>" +
             "b) Xác suất sinh viên sống cách trường trên 10 km:<br>" +
             "   $$P(X > 10) = e^{-0{,}2 \\times 10} = e^{-2} \\approx 0{,}1353 \\text{ (hay 13{,}53\\%)}$$<br>" +
             "c) Nhận diện theo Slide 66–67:<br>" +
             "   - <b>Phân phối Chi-bình phương ($\\chi^2$):</b> Luôn không âm ($x \\ge 0$), đồ thị lệch phải mạnh ở bậc tự do $\\nu$ nhỏ, dần đối xứng khi $\\nu$ lớn.<br>" +
             "   - <b>Phân phối $t$-Student:</b> Đối xứng hình chuông quanh 0 giống chuẩn tắc nhưng có <b>đuôi dày hơn</b> (Heavy-tailed); khi bậc tự do $\\nu \\to \\infty$, $t$-Student hội tụ về Chuẩn tắc $N(0, 1)$."
      }
    
    ],
    pitfalls: [
      {
        bad: "Nhầm lẫn giữa kỳ vọng E(X) = 1/λ và E(X) = λ trong phân phối mũ.",
        good: "Trong phân phối Poisson, E = λ. Nhưng trong phân phối Mũ, E = 1/λ! Luôn nhớ nghịch đảo tham số tốc độ để ra thời gian trung bình!"
      },
      {
        bad: "Quên dấu trừ trong hàm mũ e^(-λx).",
        good: "Hàm mật độ và xác suất đuôi phải luôn giảm dần về 0 khi x tăng, do đó bắt buộc phải có dấu trừ: e^(-λx)!"
      }
    ],
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Tính chất 'không nhớ' (Memoryless): $P(X > s + t \\mid X > s) = P(X > t)$ là đặc trưng của phân phối liên tục nào?",
            "opts": [
                  "Phân phối Chi-bình phương",
                  "Phân phối Chuẩn (Normal)",
                  "Phân phối Mũ (Exponential)",
                  "Phân phối Đều (Uniform)"
            ],
            "ans": 2,
            "fb": "Chính xác! Phân phối Mũ mô hình hóa tuổi thọ của các thiết bị không bị lão hóa cơ học."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Tuổi thọ linh kiện $X \\sim \\text{Exp}(\\lambda = 0{,}2)$ (trung bình 5 năm). Xác suất linh kiện sống quá 5 năm là:",
            "opts": [
                  "$e^{-0{,}2 \\times 5} = e^{-1} \\approx 0{,}3679$",
                  "$0{,}5000$",
                  "$0{,}2000$",
                  "$1 - e^{-1} \\approx 0{,}6321$"
            ],
            "ans": 0,
            "fb": "Đúng! $P(X > t) = e^{-\\lambda t} = e^{-1} \\approx 0{,}3679$."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Nếu $Z_1, Z_2, \\dots, Z_k$ là các biến ngẫu nhiên độc lập cùng tuân theo chuẩn tắc $\\mathcal{N}(0, 1)$, thì tổng bình phương $W = \\sum_{i=1}^k Z_i^2$ tuân theo phân phối:",
            "opts": [
                  "Phân phối Mũ $\\text{Exp}(k)$",
                  "Phân phối Chi-bình phương với $k$ bậc tự do: $\\chi^2(k)$",
                  "Phân phối $t$-Student với $k$ bậc tự do",
                  "Phân phối Chuẩn $\\mathcal{N}(0, k)$"
            ],
            "ans": 1,
            "fb": "Chính xác! Định nghĩa toán học của phân phối Chi-bình phương."
      }
],
    final_quiz: {
      q: "Biến ngẫu nhiên X có phân phối mũ Exp(λ = 0,5). Giá trị trung bình E(X) bằng bao nhiêu?",
      opts: [
        "2,0",
        "0,5",
        "1,0",
        "0,25"
      ],
      ans: 0,
      fb: [
        "Chính xác! Phân phối mũ có kỳ vọng E(X) = 1/λ = 1/0,5 = 2,0.",
        "Sai! 0,5 là tham số tốc độ λ, không phải kỳ vọng.",
        "Sai! Tính toán nhầm.",
        "Sai! 0,25 là λ²."
      ]
    }
  },

  {
    id: "E6",
    cluster: "E",
    title: "Định lý giới hạn trung tâm (CLT) & Ứng dụng bài thi",
    sources: "Slide Week 07 (tr. 68–77, 86–91); Stat20 Mục 4.17",
    ref: {
      "slide_file": "week07.pdf",
      "slide_name": "Tuần 07 — Định lý Giới hạn Trung tâm (CLT)",
      "pages": "Slide 68 – 77, 89 – 91",
      "page_start": 68,
      "section": "Phần 6: Định lý giới hạn trung tâm (CLT) (Slide 68–77) & Phần 7: Bài tập vận dụng 5 — Bóng đèn dự phòng / Cỡ mẫu (Slide 89–91)",
      "stat20": "Stat20 Mục 4.17 (Central Limit Theorem)",
      "key_points": [
            "Phát biểu CLT: Với mẫu i.i.d. có kỳ vọng μ và phương sai σ^2 hữu hạn, khi n đủ lớn (n ≥ 30):",
            "Tổng mẫu Sn ≈ N(n*μ, n*σ^2) ⇒ Z = (Sn - n*μ) / (σ*√n) ~ N(0, 1)",
            "Trung bình mẫu X_bar ≈ N(μ, σ^2/n) ⇒ Z = (X_bar - μ) / (σ/√n) ~ N(0, 1)",
            "Bài toán tìm số lượng linh kiện dự phòng n: Đặt ẩn phụ u = √n, giải bất phương trình bậc hai (Bài tập 5, Slide 89–91)"
      ],
      "remind": "Đây là bài toán 'chốt hạ' phân loại điểm 9–10 của UET. Hãy xem thật kỹ lời giải phương trình bậc hai tìm n = 23 bóng đèn ở Slide Week 07 trang 89–91."
},
    desc: "Định lý vĩ đại nhất của xác suất thống kê: Tổng hoặc Trung bình của các biến i.i.d. luôn xấp xỉ phân phối Chuẩn khi n đủ lớn, BẤT KỂ phân phối gốc là gì! Dạng bài tìm cỡ mẫu n.",
    widget: "clt_widget",
    steps: [
      {
        t: "Phát biểu Định lý Giới hạn Trung tâm (CLT)",
        c: `<p>Cho $X_1, X_2, \\dots, X_n$ là các biến ngẫu nhiên <b>i.i.d.</b> có kỳ vọng $\\mu$ và phương sai $\\sigma^2 &lt; \\infty$ (với <b>bất kỳ hình dạng phân phối nào</b>: lệch phải, phẳng, rời rạc...).</p>
            <p>Khi cỡ mẫu $n$ đủ lớn (thường $n \\ge 30$), ta có:</p>
            <ol>
              <li><b>Tổng mẫu $S_n = \\sum X_i$</b> xấp xỉ phân phối Chuẩn:
                  $$S_n \\approx \\mathcal{N}\\left(n\\mu, \\, n\\sigma^2\\right) \\implies Z = \\frac{S_n - n\\mu}{\\sigma\\sqrt{n}} \\xrightarrow{d} \\mathcal{N}(0, 1)$$
              </li>
              <li><b>Trung bình mẫu $\\bar{X}_n = \\frac{S_n}{n}$</b> xấp xỉ phân phối Chuẩn:
                  $$\\bar{X}_n \\approx \\mathcal{N}\\left(\\mu, \\, \\frac{\\sigma^2}{n}\\right) \\implies Z = \\frac{\\bar{X}_n - \\mu}{\\sigma/\\sqrt{n}} \\xrightarrow{d} \\mathcal{N}(0, 1)$$
              </li>
            </ol>
            <div class="tip-box">
              <b>VÌ SAO ĐỊNH LÝ NÀY MẠNH ĐẾN KINH NGẠC?</b><br>
              Vì nó <b>KHÔNG ĐÒI HỎI PHÂN PHỐI GỐC PHẢI LÀ CHUẨN</b>! Bạn có thể bắt đầu từ một phân phối cực kỳ méo mó (như phân phối mũ hay xúc xắc), nhưng khi cộng dồn hoặc lấy trung bình của nhiều biến thì hình chuông Gauss đối xứng luôn luôn kỳ diệu xuất hiện!
            </div>`
      },
      {
        t: "3 Điều kiện tiên quyết để áp dụng CLT trong bài tự luận",
        c: `<ol>
              <li>Các biến ngẫu nhiên phải <b>độc lập và cùng phân phối (i.i.d.)</b>.</li>
              <li>Phương sai $\\sigma^2$ phải hữu hạn (khác $\\infty$).</li>
              <li>Cỡ mẫu $n$ phải <b>đủ lớn</b>:
                <ul>
                  <li>Nếu phân phối gốc đã đối xứng: $n \\ge 15-20$ là đã xấp xỉ tốt.</li>
                  <li>Quy ước chung cho mọi phân phối: $n \\ge 30$.</li>
                  <li>Nếu phân phối gốc cực kỳ lệch: cần $n \\ge 50-100$.</li>
                </ul>
              </li>
            </ol>
            <div class="warn-box"><b>CÂU NÓI BẮT BUỘC TRONG BÀI THI TỰ LUẬN:</b> Luôn viết câu: <i>&quot;Vì các biến ngẫu nhiên độc lập, cùng phân phối và cỡ mẫu $n = \\dots \\ge 30$, theo Định lý Giới hạn Trung tâm ta có...&quot;</i> để lấy trọn 0,25đ lập luận!</div>`
      },
      {
        t: "Dạng bài tự luận đỉnh cao: Tìm cỡ mẫu $n$ bằng ẩn phụ $u = \\sqrt{n}$",
        c: `<p>Trong Bài tập 5 (Slide 89–91), đề bài yêu cầu tìm số lượng linh kiện $n$ để tổng tuổi thọ $S_n \\ge T$ đạt xác suất ít nhất $1 - \\alpha$:</p>
            $$P(S_n \\ge T) \\approx \\Phi\\left(\\frac{n\\mu - T}{\\sigma\\sqrt{n}}\\right) \\ge 1 - \\alpha \\implies \\frac{n\\mu - T}{\\sigma\\sqrt{n}} \\ge z_\\alpha$$
            <p><b>Thuật toán giải:</b></p>
            <ol>
              <li>Đặt ẩn phụ $u = \\sqrt{n} &gt; 0 \\implies n = u^2$.</li>
              <li>Phương trình trở thành bất phương trình bậc hai:
                  $$\\mu \\cdot u^2 - (z_\\alpha \\cdot \\sigma) \\cdot u - T \\ge 0$$
              </li>
              <li>Giải tam thức bậc hai lấy nghiệm dương $u \\ge u_0 \\implies n \\ge u_0^2$.</li>
              <li>Làm tròn lên số nguyên gần nhất và thử lại để kết luận!</li>
            </ol>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 07 — Ví dụ 20] Thời gian Xử lý Yêu cầu qua Định lý CLT",
        q: "Thời gian xử lý một yêu cầu dịch vụ có trung bình $\\mu = 12$ phút và độ lệch chuẩn $\\sigma = 6$ phút (Slide 76–77). Một ca làm việc xử lý độc lập $n = 36$ yêu cầu. Gọi $S_{36}$ là tổng thời gian xử lý của cả ca.<br>" +
           "a) Xác định phân phối xấp xỉ của $S_{36}$ theo Định lý giới hạn trung tâm.<br>" +
           "b) Tính xác suất tổng thời gian xử lý không vượt quá 7,5 giờ (450 phút).",
        sol: "<b>Lời giải chi tiết theo Slide Week 07 (trang 77):</b><br>" +
             "a) Vì cỡ mẫu $n = 36 \\ge 30$, theo Định lý giới hạn trung tâm (CLT):<br>" +
             "   - $E(S_{36}) = n \\cdot \\mu = 36 \\times 12 = 432 \\text{ phút}$.<br>" +
             "   - $\\operatorname{SD}(S_{36}) = \\sigma \\sqrt{n} = 6 \\times \\sqrt{36} = 6 \\times 6 = 36 \\text{ phút}$.<br>" +
             "   Do đó: $S_{36} \\approx N(432, 36^2) = N(432, 1296)$.<br>" +
             "b) Chuẩn hóa biến $Z$ với ngưỡng 450 phút:<br>" +
             "   $$Z = \\frac{450 - 432}{36} = \\frac{18}{36} = 0{,}5$$<br>" +
             "   Tra bảng Laplace: $\\Phi(0{,}5) = 0{,}6915$.<br>" +
             "   $$P(S_{36} \\le 450) = P(Z \\le 0{,}5) = \\Phi(0{,}5) = 0{,}6915 \\text{ (hay 69{,}15\\%)}$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 07 — Bài tập 4 Ý 3] Khoảng cách Trung bình của 100 Sinh viên",
        q: "Khoảng cách từ nhà đến trường có phân phối mũ với $\\mu = 5$ km và $\\sigma = 5$ km (Slide 87). Khảo sát ngẫu nhiên $n = 100$ sinh viên. Dù phân phối gốc là phân phối mũ cực kỳ lệch phải, hãy áp dụng CLT để tính xác suất khoảng cách trung bình của 100 sinh viên nằm trong khoảng từ 4,5 km đến 5,5 km.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 07 (trang 87):</b><br>" +
             "1. Với cỡ mẫu lớn $n = 100$, theo CLT trung bình mẫu $\\bar{X}_{100}$ xấp xỉ phân phối Chuẩn:<br>" +
             "   - $E(\\bar{X}_{100}) = \\mu = 5 \\text{ km}$.<br>" +
             "   - $\\operatorname{SD}(\\bar{X}_{100}) = \\frac{\\sigma}{\\sqrt{n}} = \\frac{5}{\\sqrt{100}} = \\frac{5}{10} = 0{,}5 \\text{ km}$.<br>" +
             "   Suy ra: $\\bar{X}_{100} \\approx N(5, 0{,}5^2) = N(5, 0{,}25)$.<br>" +
             "2. Tính xác suất $P(4{,}5 \\le \\bar{X}_{100} \\le 5{,}5)$:<br>" +
             "   - Tại cận dưới: $z_1 = \\frac{4{,}5 - 5}{0{,}5} = -1{,}0$.<br>" +
             "   - Tại cận trên: $z_2 = \\frac{5{,}5 - 5}{0{,}5} = +1{,}0$.<br>" +
             "   $$P(4{,}5 \\le \\bar{X}_{100} \\le 5{,}5) = \\Phi(1{,}0) - \\Phi(-1{,}0) = 2\\Phi(1{,}0) - 1$$<br>" +
             "   Tra bảng $\\Phi(1{,}0) = 0{,}8413$:<br>" +
             "   $$P = 2(0{,}8413) - 1 = 1{,}6826 - 1 = 0{,}6826 \\text{ (hay 68{,}26\\%)}$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 07 — Bài tập 5] Bài toán Bóng đèn Dự phòng Phân loại 9–10 Điểm UET",
        q: "Một hệ thống cần một linh kiện thiết yếu để hoạt động liên tục (Slide 89–91). Khi linh kiện hỏng, một linh kiện dự phòng cùng loại sẽ được thay thế tức thì. Tuổi thọ mỗi linh kiện là biến ngẫu nhiên độc lập có trung bình $\\mu = 100$ giờ và độ lệch chuẩn $\\sigma = 30$ giờ (hoặc $\\sigma = 20$). Cần chuẩn bị tối thiểu bao nhiêu linh kiện $n$ để hệ thống hoạt động liên tục ít nhất $T = 2000$ giờ với xác suất không dưới 99% ($0{,}99$)?",
        sol: "<b>Lời giải kinh điển bằng Tam thức bậc hai theo Slide Week 07 (trang 90–91):</b><br>" +
             "1. Gọi $X_i$ là tuổi thọ linh kiện thứ $i$. Tổng thời gian hoạt động là $S_n = \\sum_{i=1}^n X_i$.<br>" +
             "   Theo CLT: $S_n \\approx N(n\\mu, n\\sigma^2) = N(100n, 900n) \\implies \\operatorname{SD}(S_n) = 30\\sqrt{n}$.<br>" +
             "2. Yêu cầu $P(S_n \\ge 2000) \\ge 0{,}99 \\iff P\\left(Z \\ge \\frac{2000 - 100n}{30\\sqrt{n}}\\right) \\ge 0{,}99$.<br>" +
             "   Tương đương: $\\frac{100n - 2000}{30\\sqrt{n}} \\ge z_{0{,}99} \\approx 2{,}3263$ (hoặc với $\\sigma=20$ thì mẫu số là $20\\sqrt{n}$).<br>" +
             "3. Nhân chéo chuyển vế, đặt ẩn phụ $u = \\sqrt{n} > 0$:<br>" +
             "   $$100u^2 - 69{,}789u - 2000 \\ge 0$$<br>" +
             "   Giải phương trình bậc hai: $\\Delta = (-69{,}789)^2 - 4(100)(-2000) = 4870{,}5 + 800000 = 804870{,}5 \\implies \\sqrt{\\Delta} \\approx 897{,}14$.<br>" +
             "   Nghiệm dương:<br>" +
             "   $$u \\ge \\frac{69{,}789 + 897{,}14}{200} = \\frac{966{,}93}{200} \\approx 4{,}835$$<br>" +
             "   Suy ra: $n = u^2 \\ge (4{,}835)^2 \\approx 23{,}38$.<br>" +
             "4. <b>Kết luận:</b> Vì $n$ nguyên nên bắt buộc phải làm tròn LÊN: <b>cần tối thiểu $n = 24$ linh kiện</b> (với $\\sigma=20$ nghiệm là $n = 23$ linh kiện)."
      }
    
    ],
    pitfalls: [
      {
        bad: "Nghĩ rằng điều kiện của CLT là phân phối gốc ban đầu phải là phân phối Chuẩn.",
        good: "Phân phối gốc KHÔNG CẦN chuẩn! Điểm vĩ đại của CLT là phân phối gốc dù lệch hay quái dị đến đâu thì TỔNG và TRUNG BÌNH của chúng vẫn tiến về phân phối chuẩn!"
      },
      {
        bad: "Quên chia căn bậc hai của n khi tính độ lệch chuẩn của trung bình mẫu.",
        good: "Độ lệch chuẩn của X̄ là σ/√n! Nếu quên chia √n, bạn sẽ tính sai hoàn toàn Z-score."
      }
    ],
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Theo Định lý Giới hạn Trung tâm (CLT), khi cỡ mẫu $n$ đủ lớn ($n \\ge 30$), tổng $S_n = \\sum_{i=1}^n X_i$ của các biến i.i.d. có phân phối xấp xỉ:",
            "opts": [
                  "$\\mathcal{N}(\\mu, \\sigma^2)$",
                  "$\\mathcal{N}(\\mu, \\sigma^2/n)$",
                  "Phân phối Đều",
                  "$\\mathcal{N}(n\\mu, n\\sigma^2)$"
            ],
            "ans": 3,
            "fb": "Chính xác! Tổng $S_n$ xấp xỉ chuẩn với kỳ vọng $n\\mu$ và phương sai $n\\sigma^2$."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Rút mẫu $n = 100$ từ tổng thể có $\\mu = 50, \\sigma = 10$. Khoảng đối xứng chứa $95\\%$ giá trị trung bình mẫu $\\bar{X}$ (với $z = 1{,}96$) là:",
            "opts": [
                  "$[30{,}4; 69{,}6]$",
                  "$[48{,}04; 51{,}96]$",
                  "$[40; 60]$",
                  "$[49; 51]$"
            ],
            "ans": 1,
            "fb": "Đúng! $SE = 10/\\sqrt{100} = 1$. Khoảng $95\\%: [50 - 1{,}96(1); 50 + 1{,}96(1)] = [48{,}04; 51{,}96]$."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Trong bài toán bóng đèn dự phòng UET ($\\mu = 100, \\sigma = 20, T = 2000$), sau khi chuẩn hóa $P(S_n \\ge 2000) \\ge 0{,}99$, phương trình bậc hai $100u^2 - 49{,}35u - 2000 \\ge 0$ (với $u = \\sqrt{n}$) cho số bóng đèn tối thiểu là:",
            "opts": [
                  "$n = 20$ bóng đèn",
                  "$n = 22$ bóng đèn",
                  "$n = 23$ bóng đèn",
                  "$n = 25$ bóng đèn"
            ],
            "ans": 2,
            "fb": "Chính xác! Bẫy kinh điển số 10: Nghiệm $u \\ge 4{,}726 \\implies n \\ge 22{,}33$. Vì $n$ nguyên nên bắt buộc phải làm tròn LÊN $n = 23$ bóng."
      }
],
    final_quiz: {
      q: "Điều kiện nào sau đây KHÔNG PHẢI là điều kiện bắt buộc để áp dụng Định lý giới hạn trung tâm (CLT)?",
      opts: [
        "Phân phối gốc ban đầu bắt buộc phải là phân phối Chuẩn",
        "Các biến ngẫu nhiên phải độc lập với nhau",
        "Các biến ngẫu nhiên phải có cùng phân phối",
        "Phương sai của phân phối gốc phải hữu hạn"
      ],
      ans: 0,
      fb: [
        "Chính xác! Phân phối gốc KHÔNG CẦN là phân phối chuẩn. Định lý giới hạn trung tâm đúng cho hầu hết mọi hình dạng phân phối gốc miễn là phương sai hữu hạn và cỡ mẫu đủ lớn.",
        "Sai! Tính độc lập là điều kiện bắt buộc.",
        "Sai! Cùng phân phối là điều kiện i.i.d. chuẩn mực.",
        "Sai! Phương sai hữu hạn là điều kiện toán học bắt buộc."
      ]
    }
  }
];

if (typeof module !== 'undefined' && module.exports) {
  module.exports = CUM_E;
}
