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
        q: "Thời gian chờ xe buýt (phút) là biến ngẫu nhiên liên tục X có hàm mật độ f(x) = 0,2 khi 0 ≤ x ≤ 5 và f(x) = 0 ở ngoài (Slide 45-47). Tính xác suất để một hành khách phải chờ từ 1 đến 3 phút.",
        sol: "<b>Áp dụng công thức tích phân diện tích:</b><br>" +
             "$$P(1 \\le X \\le 3) = \\int_{1}^{3} f(x) \\, dx = \\int_{1}^{3} 0{,}2 \\, dx = [0{,}2x]_{1}^{3} = 0{,}2(3) - 0{,}2(1) = 0{,}6 - 0{,}2 = 0{,}40\\text{ (40\\%)}$$."
      },
      {
        level: "Trung bình",
        q: "Biến ngẫu nhiên liên tục X nhận giá trị trong đoạn [0, b] (với b > 0) có hàm tích lũy F(x) = x²/9 khi 0 ≤ x ≤ b, F(x) = 0 khi x < 0 và F(x) = 1 khi x > b (Slide 82-83 — Bài tập 2). Hãy xác định giá trị của b và tìm hàm mật độ f(x).",
        sol: "<b>Ý 1: Tìm b:</b><br>" +
             "Vì $X$ là biến liên tục nên hàm tích lũy $F(x)$ phải liên tục tại điểm biên $b$:<br>" +
             "$$F(b) = 1 \\iff \\frac{b^2}{9} = 1 \\implies b^2 = 9 \\implies b = 3\\text{ (vì } b &gt; 0\\text{)}$$<br>" +
             "<b>Ý 2: Tìm hàm mật độ f(x):</b><br>" +
             "Lấy đạo hàm của $F(x)$ trên từng khoảng:<br>" +
             "- Khi $0 &lt; x &lt; 3$: $f_X(x) = F_X'(x) = \\left(\\frac{x^2}{9}\\right)' = \\frac{2x}{9}$.<br>" +
             "- Khi $x &lt; 0$ hoặc $x &gt; 3$: $f_X(x) = 0$.<br>" +
             "$$f_X(x) = \\begin{cases} \\frac{2x}{9}, &amp; 0 &lt; x &lt; 3 \\\\ 0, &amp; \\text{ngược lại} \\end{cases}$$"
      },
      {
        level: "Vận dụng",
        q: "Tìm hằng số k để hàm số f(x) = k · (1 - x²) với 0 ≤ x ≤ 1 (và bằng 0 ở ngoài) là một hàm mật độ xác suất hợp lệ. Sau đó tính P(X > 0,5).",
        sol: "<b>Bước 1: Tìm k:</b> Áp dụng điều kiện chuẩn hóa $\\int_{-\\infty}^\\infty f(x)dx = 1$:<br>" +
             "$$\\int_{0}^{1} k (1 - x^2) \\, dx = k \\left[ x - \\frac{x^3}{3} \\right]_{0}^{1} = k \\left( 1 - \\frac{1}{3} \\right) = \\frac{2}{3}k = 1 \\implies k = \\frac{3}{2} = 1{,}5$$<br>" +
             "<b>Bước 2: Tính P(X > 0,5):</b><br>" +
             "$$P(X &gt; 0{,}5) = \\int_{0{,}5}^{1} \\frac{3}{2}(1 - x^2) \\, dx = \\frac{3}{2} \\left[ x - \\frac{x^3}{3} \\right]_{0{,}5}^{1}$$<br>" +
             "$$= \\frac{3}{2} \\left[ \\left(1 - \\frac{1}{3}\\right) - \\left(0{,}5 - \\frac{0{,}125}{3}\\right) \\right] = \\frac{3}{2} \\left[ \\frac{2}{3} - \\left(\\frac{1}{2} - \\frac{1}{24}\\right) \\right] = \\frac{3}{2} \\left[ \\frac{2}{3} - \\frac{11}{24} \\right] = \\frac{3}{2} \\cdot \\frac{5}{24} = \\frac{5}{16} = 0{,}3125$$."
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
        q: "Cho biến ngẫu nhiên liên tục X có hàm mật độ f(x) = 2x khi 0 < x < 1 (và bằng 0 ở ngoài) (Slide 49 — Ví dụ 13). Hãy tính E(X).",
        sol: "<b>Áp dụng công thức tích phân:</b><br>" +
             "$$E(X) = \\int_{0}^{1} x \\cdot f(x) \\, dx = \\int_{0}^{1} x \\cdot (2x) \\, dx = \\int_{0}^{1} 2x^2 \\, dx = \\left[ \\frac{2x^3}{3} \\right]_{0}^{1} = \\frac{2}{3} \\approx 0{,}6667$$."
      },
      {
        level: "Trung bình",
        q: "Cũng biến ngẫu nhiên X ở trên (f(x) = 2x trên (0, 1)). Hãy tính E(X²), Var(X) và SD(X).",
        sol: "<b>Bước 1: Tính E(X²):</b><br>" +
             "$$E(X^2) = \\int_{0}^{1} x^2 \\cdot f(x) \\, dx = \\int_{0}^{1} x^2 \\cdot (2x) \\, dx = \\int_{0}^{1} 2x^3 \\, dx = \\left[ \\frac{2x^4}{4} \\right]_{0}^{1} = \\frac{1}{2} = 0{,}50$$<br>" +
             "<b>Bước 2: Tính Var(X):</b><br>" +
             "$$\\operatorname{Var}(X) = E(X^2) - [E(X)]^2 = \\frac{1}{2} - \\left(\\frac{2}{3}\\right)^2 = \\frac{1}{2} - \\frac{4}{9} = \\frac{9 - 8}{18} = \\frac{1}{18} \\approx 0{,}0556$$<br>" +
             "<b>Bước 3: Tính SD(X):</b><br>" +
             "$$\\operatorname{SD}(X) = \\sqrt{\\frac{1}{18}} = \\frac{1}{3\\sqrt{2}} \\approx 0{,}2357$$."
      },
      {
        level: "Vận dụng",
        q: "Từ Bài tập 2 ở Slide 83: X có f(x) = 2x/9 trên khoảng (0, 3). Tính kỳ vọng và phương sai của biến ngẫu nhiên Y = 3X + 4.",
        sol: "<b>Bước 1: Tính E(X) và Var(X):</b><br>" +
             "- $E(X) = \\int_{0}^{3} x \\cdot \\frac{2x}{9} \\, dx = \\frac{2}{9} \\left[ \\frac{x^3}{3} \\right]_{0}^{3} = \\frac{2}{9} \\times 9 = 2{,}0$.<br>" +
             "- $E(X^2) = \\int_{0}^{3} x^2 \\cdot \\frac{2x}{9} \\, dx = \\frac{2}{9} \\left[ \\frac{x^4}{4} \\right]_{0}^{3} = \\frac{2}{9} \\times \\frac{81}{4} = 4{,}5$.<br>" +
             "- $\\operatorname{Var}(X) = 4{,}5 - 2{,}0^2 = 0{,}5$.<br>" +
             "<b>Bước 2: Tính cho Y = 3X + 4:</b><br>" +
             "- $E(Y) = 3 \\cdot E(X) + 4 = 3(2{,}0) + 4 = 10{,}0$.<br>" +
             "- $\\operatorname{Var}(Y) = 3^2 \\cdot \\operatorname{Var}(X) = 9 \\times 0{,}5 = 4{,}5$."
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
        q: "Thời gian xe buýt đến bến tuân theo phân phối đều từ 0 đến 10 phút, tức X ~ U(0, 10) (Slide 51-53). Tính xác suất để một hành khách phải chờ ít hơn 3 phút.",
        sol: "<b>Áp dụng công thức tỉ lệ chiều dài đoạn:</b><br>" +
             "$$P(X &lt; 3) = P(0 \\le X \\le 3) = \\frac{3 - 0}{10 - 0} = \\frac{3}{10} = 0{,}30\\text{ (30\\%)}$$."
      },
      {
        level: "Trung bình",
        q: "Tính kỳ vọng và độ lệch chuẩn của thời gian chờ xe buýt trong ví dụ trên (X ~ U(0, 10)).",
        sol: "<b>Bước 1: Kỳ vọng:</b><br>" +
             "$$E(X) = \\frac{a + b}{2} = \\frac{0 + 10}{2} = 5{,}0\\text{ (phút)}$$<br>" +
             "<b>Bước 2: Phương sai:</b><br>" +
             "$$\\operatorname{Var}(X) = \\frac{(b - a)^2}{12} = \\frac{(10 - 0)^2}{12} = \\frac{100}{12} = \\frac{25}{3} \\approx 8{,}3333\\text{ (phút}^2\\text{)}$$<br>" +
             "<b>Bước 3: Độ lệch chuẩn:</b><br>" +
             "$$\\operatorname{SD}(X) = \\sqrt{\\frac{25}{3}} = \\frac{5}{\\sqrt{3}} \\approx 2{,}8868\\text{ (phút)}$$."
      },
      {
        level: "Vận dụng",
        q: "Một xe buýt X ~ U(0, 10). Biết rằng bạn đã đứng chờ ở bến được 4 phút mà xe vẫn chưa tới. Tính xác suất để bạn phải chờ thêm ít nhất 3 phút nữa (tức tổng thời gian chờ vượt quá 7 phút).",
        sol: "<b>Phân tích:</b> Đây là bài toán Xác suất có điều kiện trên phân phối liên tục: $P(X &gt; 7 \\mid X &gt; 4)$.<br>" +
             "$$P(X &gt; 7 \\mid X &gt; 4) = \\frac{P(X &gt; 7 \\cap X &gt; 4)}{P(X &gt; 4)} = \\frac{P(X &gt; 7)}{P(X &gt; 4)}$$<br>" +
             "- $P(X &gt; 7) = \\frac{10 - 7}{10} = \\frac{3}{10} = 0{,}3$.<br>" +
             "- $P(X &gt; 4) = \\frac{10 - 4}{10} = \\frac{6}{10} = 0{,}6$.<br>" +
             "$$\\implies P(X &gt; 7 \\mid X &gt; 4) = \\frac{0{,}3}{0{,}6} = 0{,}50\\text{ (50\\%)}$$."
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
        q: "Điểm thi môn Xác suất Thống kê tuân theo phân phối chuẩn N(μ = 70, σ² = 10²). Một sinh viên đạt 85 điểm thì giá trị chuẩn hóa Z bằng bao nhiêu?",
        sol: "<b>Áp dụng công thức chuẩn hóa Z:</b><br>" +
             "$$Z = \\frac{X - \\mu}{\\sigma} = \\frac{85 - 70}{10} = \\frac{15}{10} = 1{,}5$$<br>" +
             "<b>Ý nghĩa:</b> Điểm của sinh viên này cao hơn điểm trung bình của lớp đúng 1,5 độ lệch chuẩn."
      },
      {
        level: "Trung bình",
        q: "Một máy chiết nước ngọt đóng chai tự động có dung tích phân phối chuẩn N(500, 5²). Dùng quy tắc 68–95–99,7 để tính xấp xỉ xác suất một chai nước có dung tích lớn hơn 510 ml.",
        sol: "<b>Bước 1:</b> Chuẩn hóa giá trị 510:<br>" +
             "$$Z = \\frac{510 - 500}{5} = \\frac{10}{5} = 2{,}0$$<br>" +
             "<b>Bước 2:</b> Theo quy tắc thực nghiệm, khoảng trong 2 SD quanh trung bình (từ 490 đến 510) chiếm 95% dữ liệu.<br>" +
             "<b>Bước 3:</b> Phần diện tích hai đuôi (nhỏ hơn 490 hoặc lớn hơn 510) chiếm $100\\% - 95\\% = 5\\%$.<br>" +
             "Vì phân phối chuẩn đối xứng hoàn hảo, đuôi bên phải chiếm một nửa:<br>" +
             "$$P(X &gt; 510) = P(Z &gt; 2) \\approx \\frac{5\\%}{2} = 2{,}5\\% = 0{,}025$$."
      },
      {
        level: "Vận dụng",
        q: "Bài tập 3 Slide 84-85: Khối lượng người Việt Nam có phân phối chuẩn N(65, 5²). Giả sử khối lượng của những người được chọn độc lập. Một thang máy chở tối đa 10 người và tải trọng 700 kg. Tính xác suất để 10 người ngẫu nhiên vào thang máy mà không bị quá tải.",
        sol: "<b>Bước 1: Xác định phân phối của tổng 10 người:</b><br>" +
             "Gọi $X_i \\sim \\mathcal{N}(65, 5^2)$ là cân nặng người thứ $i$. Đặt $S_{10} = X_1 + \\dots + X_{10}$.<br>" +
             "- Kỳ vọng của tổng: $E(S_{10}) = 10 \\times 65 = 650\\text{ kg}$.<br>" +
             "- Phương sai của tổng: $\\operatorname{Var}(S_{10}) = 10 \\times 5^2 = 250\\text{ kg}^2$.<br>" +
             "- Độ lệch chuẩn: $\\operatorname{SD}(S_{10}) = \\sqrt{250} = 5\\sqrt{10} \\approx 15{,}8114\\text{ kg}$.<br>" +
             "Vì tổng các biến chuẩn độc lập cũng là biến chuẩn $\\implies S_{10} \\sim \\mathcal{N}(650, 250)$.<br>" +
             "<b>Bước 2: Tính xác suất không quá tải P(S₁₀ ≤ 700):</b><br>" +
             "$$Z = \\frac{700 - 650}{5\\sqrt{10}} = \\frac{50}{15{,}8114} \\approx 3{,}1623$$<br>" +
             "$$P(S_{10} \\le 700) = \\Phi(3{,}1623) \\approx 0{,}9992\\text{ (hay } 99{,}92\\%\\text{)}$$<br>" +
             "<b>Kết luận:</b> Xác suất thang máy không bị quá tải xấp xỉ 99,92%."
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
        q: "Thời gian chờ giữa các lần bảo trì máy chủ có phân phối mũ với kỳ vọng 5 tháng. Tham số tốc độ λ bằng bao nhiêu và phương sai bằng bao nhiêu?",
        sol: "<b>Bước 1:</b> Vì $E(X) = \\frac{1}{\\lambda} = 5 \\implies \\lambda = \\frac{1}{5} = 0{,}2\\text{ (lần/tháng)}$.<br>" +
             "<b>Bước 2:</b> Phương sai:<br>" +
             "$$\\operatorname{Var}(X) = \\frac{1}{\\lambda^2} = 5^2 = 25\\text{ (tháng}^2\\text{)}$$."
      },
      {
        level: "Trung bình",
        q: "Thời gian phục vụ một khách hàng tại quầy giao dịch là biến ngẫu nhiên X ~ Exp(λ = 0,5 phút⁻¹). Tính xác suất để một khách hàng được phục vụ trong hơn 4 phút.",
        sol: "<b>Áp dụng công thức xác suất đuôi phải:</b><br>" +
             "$$P(X &gt; 4) = e^{-\\lambda x} = e^{-0{,}5 \\times 4} = e^{-2} \\approx 0{,}1353\\text{ (hay } 13{,}53\\%\\text{)}$$."
      },
      {
        level: "Vận dụng",
        q: "Bài tập 4 Ý 4 Slide 88: Khoảng cách X từ nơi ở đến trường của một sinh viên có phân phối mũ với kỳ vọng 5 km (λ = 1/5 = 0,2). Tính xác suất chính xác để khoảng cách của một sinh viên nằm trong khoảng từ 4,9 km đến 5,2 km.",
        sol: "<b>Áp dụng công thức xác suất khoảng của phân phối mũ:</b><br>" +
             "$$P(4{,}9 &lt; X &lt; 5{,}2) = e^{-\\lambda(4{,}9)} - e^{-\\lambda(5{,}2)} = e^{-4{,}9/5} - e^{-5{,}2/5} = e^{-0{,}98} - e^{-1{,}04}$$<br>" +
             "$$= 0{,}37531 - 0{,}35345 \\approx 0{,}0219\\text{ (hay } 2{,}19\\%\\text{)}$$<br>" +
             "<i>Nhận xét: Đây là xác suất chính xác cho 1 sinh viên đơn lẻ, rất khác với xác suất trung bình của 100 sinh viên (được tính bằng CLT ở bài sau)!</i>"
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
        q: "Thời gian xử lý một yêu cầu có trung bình μ = 12 phút và độ lệch chuẩn σ = 6 phút (Slide 76-77 — Ví dụ 20). Chọn ngẫu nhiên độc lập 64 yêu cầu. Tính xác suất để thời gian xử lý trung bình nhỏ hơn 11 phút.",
        sol: "<b>Bước 1: Kiểm tra điều kiện:</b> Các yêu cầu độc lập, cùng phân phối, cỡ mẫu $n = 64 &gt; 30$.<br>" +
             "<b>Bước 2: Phân phối của trung bình mẫu:</b><br>" +
             "- $E(\\bar{X}_{64}) = \\mu = 12\\text{ phút}$.<br>" +
             "- $\\operatorname{SD}(\\bar{X}_{64}) = \\frac{\\sigma}{\\sqrt{n}} = \\frac{6}{\\sqrt{64}} = \\frac{6}{8} = 0{,}75\\text{ phút}$.<br>" +
             "Theo CLT: $\\bar{X}_{64} \\approx \\mathcal{N}(12, \\, 0{,}75^2)$.<br>" +
             "<b>Bước 3: Chuẩn hóa Z và tra bảng:</b><br>" +
             "$$Z = \\frac{11 - 12}{0{,}75} = \\frac{-1}{0{,}75} \\approx -1{,}3333$$<br>" +
             "$$P(\\bar{X}_{64} &lt; 11) \\approx \\Phi(-1{,}33) = 1 - \\Phi(1{,}33) = 1 - 0{,}9082 = 0{,}0918\\text{ (hay } 9{,}18\\%\\text{)}$$."
      },
      {
        level: "Trung bình",
        q: "Bài tập 4 Ý 3 Slide 87: Khoảng cách từ nhà đến trường có μ = 5 km, σ = 5 km. Chọn ngẫu nhiên 100 sinh viên. Dùng CLT tính xác suất khoảng cách trung bình của 100 sinh viên nằm trong (4,9; 5,2) km.",
        sol: "<b>Bước 1:</b> $n = 100 \\ge 30$, $\\mu = 5$, $\\sigma = 5$.<br>" +
             "- $E(\\bar{X}_{100}) = 5\\text{ km}$.<br>" +
             "- $\\operatorname{SD}(\\bar{X}_{100}) = \\frac{5}{\\sqrt{100}} = \\frac{5}{10} = 0{,}5\\text{ km}$.<br>" +
             "<b>Bước 2: Chuẩn hóa hai đầu mút:</b><br>" +
             "- Tại $4{,}9$: $Z_1 = \\frac{4{,}9 - 5}{0{,}5} = -0{,}20$.<br>" +
             "- Tại $5{,}2$: $Z_2 = \\frac{5{,}2 - 5}{0{,}5} = +0{,}40$.<br>" +
             "<b>Bước 3: Tra bảng:</b><br>" +
             "$$P(4{,}9 &lt; \\bar{X}_{100} &lt; 5{,}2) \\approx \\Phi(0{,}40) - \\Phi(-0{,}20) = \\Phi(0{,}40) - [1 - \\Phi(0{,}20)]$$<br>" +
             "$$= 0{,}6554 - (1 - 0{,}5793) = 0{,}6554 - 0{,}4207 = 0{,}2347\\text{ (hay } 23{,}47\\%\\text{)}$$."
      },
      {
        level: "Vận dụng",
        q: "Bài tập 5 Slide 89-91: Tuổi thọ linh kiện có trung bình 100 giờ và độ lệch chuẩn 30 giờ. Khi linh kiện hỏng được thay ngay. Dùng CLT ước tính số linh kiện n cần có sao cho xác suất hệ thống chạy ít nhất 2000 giờ đạt tối thiểu 95%.",
        sol: "<b>Bước 1: Thiết lập mô hình:</b><br>" +
             "Tổng thời gian hoạt động $S_n = X_1 + \\dots + X_n$.<br>" +
             "- $E(S_n) = 100n$, $\\operatorname{SD}(S_n) = 30\\sqrt{n}$.<br>" +
             "- Theo CLT: $P(S_n \\ge 2000) \\approx \\Phi\\left(\\frac{100n - 2000}{30\\sqrt{n}}\\right) \\ge 0{,}95$.<br>" +
             "<b>Bước 2: Giải bất phương trình ẩn u = √n:</b><br>" +
             "Ta có giá trị phân vị $\\Phi(1{,}64485) = 0{,}95$. Do đó:<br>" +
             "$$\\frac{100n - 2000}{30\\sqrt{n}} \\ge 1{,}64485 \\implies 100n - 2000 \\ge 49{,}3455\\sqrt{n}$$<br>" +
             "Đặt $u = \\sqrt{n} &gt; 0$: $100u^2 - 49{,}3455u - 2000 \\ge 0$.<br>" +
             "Giải phương trình bậc hai: $\\Delta = (-49{,}3455)^2 - 4(100)(-2000) \\approx 802435 \\implies \\sqrt{\\Delta} \\approx 895{,}79$.<br>" +
             "$$u \\ge \\frac{49{,}3455 + 895{,}79}{200} \\approx 4{,}7257 \\implies n = u^2 \\ge 4{,}7257^2 \\approx 22{,}33$$<br>" +
             "<b>Bước 3: Kiểm tra các số nguyên lân cận:</b><br>" +
             "- Với $n = 22$: $Z = \\frac{100(22) - 2000}{30\\sqrt{22}} = \\frac{200}{140{,}71} \\approx 1{,}4213 \\implies \\Phi(1{,}4213) \\approx 0{,}9224 &lt; 95\\%$.<br>" +
             "- Với $n = 23$: $Z = \\frac{100(23) - 2000}{30\\sqrt{23}} = \\frac{300}{143{,}87} \\approx 2{,}0851 \\implies \\Phi(2{,}0851) \\approx 0{,}9815 &gt; 95\\%$.<br>" +
             "<b>Kết luận:</b> Cần chọn $n = 23$ linh kiện (gồm 1 linh kiện ban đầu và 22 linh kiện dự phòng)."
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
