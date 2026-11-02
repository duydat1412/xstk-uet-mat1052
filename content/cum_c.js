// ==========================================================================
// CỤM C: BIẾN NGẪU NHIÊN RỜI RẠC
// Bao gồm: Bài C1, C2, C3, C4, C5, C6
// Nguồn: Slide UET Week 06 & Week 07 (tr. 4–20, 79–81); Stat20 Chương 4 (Mục 4.1 - 4.10)
// Kiểm chứng số học: verify/verify_cum_c.py
// ==========================================================================

const CUM_C = [
  {
    id: "C1",
    cluster: "C",
    title: "Biến ngẫu nhiên rời rạc, Hàm khối xác suất (pmf) & Hàm tích lũy (cdf)",
    sources: "Slide Week 06 (tr. 1–35); Stat20 Mục 4.1 - 4.4",
    ref: {
      "slide_file": "week06.pdf",
      "slide_name": "Tuần 06 — Biến ngẫu nhiên rời rạc & Hàm phân phối",
      "pages": "Slide 16 – 36",
      "page_start": 16,
      "section": "Phần 2: Biến ngẫu nhiên và Phân phối xác suất (Slide 16–24) & Phần 3: Hàm phân phối tích lũy cdf (Slide 25–36)",
      "stat20": "Stat20 Mục 4.1, 4.2, 4.3.1, 4.4 (Discrete Random Variables & CDF)",
      "key_points": [
            "Biến ngẫu nhiên rời rạc X: Ánh xạ từ không gian mẫu Ω vào tập con đếm được của R",
            "Hàm khối xác suất pmf p_X(x) = P(X = x) với điều kiện chuẩn hóa ∑p(x) = 1",
            "Hàm tích lũy cdf F(x) = P(X ≤ x): Hàm đơn điệu tăng, dạng bậc thang, liên tục bên phải"
      ],
      "remind": "Nếu bạn chưa biết cách lập bảng pmf tìm hằng số c hoặc vẽ đồ thị bậc thang của F(x), hãy đọc lại Slide Week 06 từ trang 18 đến 35."
},
    desc: "Hiểu bản chất của Biến ngẫu nhiên như một ánh xạ gán số, Hàm khối xác suất pmf p(x) và Hàm phân phối tích lũy cdf F(x) bậc thang.",
    steps: [
      {
        t: "Biến ngẫu nhiên (Random Variable) là gì?",
        c: `<p>Trong thực tế, kết quả của một phép thử có thể là chữ (Ngửa/Sấp, Đạt/Lỗi). Để tính toán giải tích, ta cần chuyển chúng thành <b>những con số</b>.</p>
            <p><b>Biến ngẫu nhiên $X$</b> thực chất là một <b>quy tắc (hàm số)</b> gán một giá trị số thực cho mỗi kết quả sơ cấp trong không gian mẫu:</p>
            $$X: \\Omega \\to \\mathbb{R}$$
            <p><b>Biến ngẫu nhiên rời rạc</b>: Nhận các giá trị riêng biệt, tách rời nhau (đếm được, hữu hạn hoặc vô hạn đếm được như $\\{0, 1, 2, \\dots\\}$).</p>`
      },
      {
        t: "Hàm khối xác suất (pmf - Probability Mass Function)",
        c: `<p><b>Hàm khối xác suất $p_X(x)$</b> liệt kê xác suất để $X$ nhận đúng một giá trị cụ thể $x$:</p>
            $$p_X(x) = P(X = x)$$
            <p><b>Hai điều kiện bắt buộc của mọi bảng pmf:</b></p>
            <ol>
              <li>$0 \\le p_X(x) \\le 1$ với mọi $x$.</li>
              <li>Tổng tất cả xác suất của mọi giá trị có thể nhận phải bằng đúng 1:
                  $$\\sum_{x} p_X(x) = 1$$
              </li>
            </ol>`
      },
      {
        t: "Hàm phân phối tích lũy (cdf - Cumulative Distribution Function)",
        c: `<p><b>Hàm tích lũy $F_X(x)$</b> đo xác suất để biến ngẫu nhiên nhận giá trị <b>nhỏ hơn hoặc bằng $x$</b>:</p>
            $$F_X(x) = P(X \\le x) = \\sum_{t \\le x} p_X(t)$$
            <p><b>Đặc điểm của hàm tích lũy rời rạc:</b></p>
            <ul>
              <li>Đồ thị có dạng <b>bậc thang (step function)</b>, nhảy bậc tại các điểm giá trị $x$ với độ cao bước nhảy đúng bằng xác suất $p_X(x)$ tại điểm đó.</li>
              <li>Luôn bắt đầu từ $0$ khi $x \\to -\\infty$ và đạt tới $1$ khi $x \\to +\\infty$.</li>
              <li><b>Công thức tính xác suất trên khoảng:</b>
                  $$P(a &lt; X \\le b) = F_X(b) - F_X(a)$$
              </li>
            </ul>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 06 — Ví dụ 3 & 5] Tung đồng xu ba lần và Hàm khối xác suất pmf",
        q: "Một đồng xu cân đối được tung 3 lần độc lập (Slide 18, 23–24). Ký hiệu H là ngửa, T là sấp. Gọi $X$ là số mặt ngửa xuất hiện trong 3 lần tung.<br>" +
           "a) Lập bảng phân phối xác suất pmf $p_X(x)$ của biến ngẫu nhiên $X$.<br>" +
           "b) Kiểm tra điều kiện chuẩn hóa $\\sum p_X(x) = 1$.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 06 (trang 24):</b><br>" +
             "a) Không gian mẫu gồm $2^3 = 8$ chuỗi kết quả đồng khả năng (mỗi chuỗi xác suất $1/8$):<br>" +
             "   $$\\Omega = \\{TTT, HTT, THT, TTH, HHT, HTH, THH, HHH\\}$$<br>" +
             "   - $X = 0$: Có 1 kết quả $\\{TTT\\} \\implies p_X(0) = \\frac{1}{8} = 0{,}125$.<br>" +
             "   - $X = 1$: Có 3 kết quả $\\{HTT, THT, TTH\\} \\implies p_X(1) = \\frac{3}{8} = 0{,}375$.<br>" +
             "   - $X = 2$: Có 3 kết quả $\\{HHT, HTH, THH\\} \\implies p_X(2) = \\frac{3}{8} = 0{,}375$.<br>" +
             "   - $X = 3$: Có 1 kết quả $\\{HHH\\} \\implies p_X(3) = \\frac{1}{8} = 0{,}125$.<br>" +
             "b) <b>Kiểm tra chuẩn hóa:</b><br>" +
             "   $$\\sum_{x=0}^3 p_X(x) = \\frac{1}{8} + \\frac{3}{8} + \\frac{3}{8} + \\frac{1}{8} = \\frac{8}{8} = 1$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 06 — Ví dụ 6 & 7] Hai sản phẩm đạt chuẩn và Hàm tích lũy cdf",
        q: "Hai sản phẩm được kiểm tra độc lập; mỗi sản phẩm đạt chuẩn với xác suất $0{,}8$ (Slide 28–32). Gọi $X$ là số sản phẩm đạt chuẩn ($X \\in \\{0, 1, 2\\}$). Phân phối xác suất của $X$ là: $p_X(0) = 0{,}04; p_X(1) = 0{,}32; p_X(2) = 0{,}64$.<br>" +
           "a) Xây dựng biểu thức hàm phân phối tích lũy $F_X(x) = P(X \\le x)$ trên toàn bộ trục số thực $\\mathbb{R}$.<br>" +
           "b) Tính xác suất có ít nhất 1 sản phẩm đạt chuẩn bằng hàm $F_X(x)$.",
        sol: "<b>Lời giải chi tiết theo Slide Week 06 (trang 29 & 32):</b><br>" +
             "a) Vì $X$ nhận giá trị rời rạc trên $\{0, 1, 2\}$, hàm tích lũy $F_X(x)$ có dạng bậc thang liên tục bên phải:<br>" +
             "   $$F_X(x) = \\begin{cases} 0 & \\text{khi } x < 0 \\cr 0{,}04 & \\text{khi } 0 \\le x < 1 \\cr 0{,}04 + 0{,}32 = 0{,}36 & \\text{khi } 1 \\le x < 2 \\cr 0{,}36 + 0{,}64 = 1{,}00 & \\text{khi } x \\ge 2 \\end{cases}$$<br>" +
             "b) Xác suất có ít nhất 1 sản phẩm đạt chuẩn là $P(X \\ge 1)$:<br>" +
             "   $$P(X \\ge 1) = 1 - P(X < 1) = 1 - P(X \\le 0) = 1 - F_X(0) = 1 - 0{,}04 = 0{,}96$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 06 — Ví dụ 8] Phân phối số đường dây điện thoại bận",
        q: "Một doanh nghiệp có 6 đường dây điện thoại (Slide 33–36). Gọi $X$ là số đường dây bận tại thời điểm quan sát, có bảng phân phối xác suất:<br>" +
           "$$p_X(0)=0{,}10; \\quad p_X(1)=0{,}15; \\quad p_X(2)=0{,}20; \\quad p_X(3)=0{,}25; \\quad p_X(4)=0{,}15; \\quad p_X(5)=0{,}10; \\quad p_X(6)=0{,}05$$<br>" +
           "a) Tính xác suất có nhiều nhất 3 đường dây bận $P(X \\le 3)$.<br>" +
           "b) Tính xác suất có từ 1 đến 4 đường dây bận $P(1 \\le X \\le 4)$.",
        sol: "<b>Lời giải chính xác theo Slide Week 06 (trang 34):</b><br>" +
             "a) Xác suất có nhiều nhất 3 đường dây bận:<br>" +
             "   $$P(X \\le 3) = p(0) + p(1) + p(2) + p(3) = 0{,}10 + 0{,}15 + 0{,}20 + 0{,}25 = 0{,}70 \\text{ (hay 70\\%)}$$<br>" +
             "b) Xác suất có từ 1 đến 4 đường dây bận:<br>" +
             "   $$P(1 \\le X \\le 4) = p(1) + p(2) + p(3) + p(4) = 0{,}15 + 0{,}20 + 0{,}25 + 0{,}15 = 0{,}75 \\text{ (hay 75\\%)}$$"
      }
    
    ],
    pitfalls: [
      {
        bad: "Nhầm lẫn giữa F(x) và p(x): tính P(X = 2) bằng cách lấy thẳng F(2).",
        good: "F(2) là P(X ≤ 2) (tích lũy từ đầu đến 2). Để tìm P(X = 2), phải lấy F(2) trừ đi giới hạn bên trái của F tại 2 (độ cao bước nhảy)!"
      },
      {
        bad: "Quên kiểm tra tổng xác suất trong bảng pmf có bằng 1 hay không.",
        good: "Luôn luôn cộng nhẩm dòng xác suất: nếu không ra đúng 1,00 thì chắc chắn bạn đã lập luận thiếu trường hợp!"
      }
    ],
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Hàm khối xác suất (pmf) $p(x) = P(X = x)$ của biến ngẫu nhiên rời rạc bắt buộc phải thỏa mãn:",
            "opts": [
                  "$p(x) \\le 1$ và tích phân bằng 1",
                  "$p(x)$ là hàm liên tục",
                  "$p(x) \\ge 0$ và $\\sum p(x) = 1$",
                  "$\\lim_{x \\to \\infty} p(x) = 1$"
            ],
            "ans": 2,
            "fb": "Chính xác! Tổng xác suất trên toàn bộ các giá trị có thể nhận phải bằng 1."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Cho $P(X = 1) = 0{,}3, P(X = 2) = 0{,}5, P(X = 3) = 0{,}2$. Giá trị hàm phân phối tích lũy $F(2) = P(X \\le 2)$ là:",
            "opts": [
                  "$0{,}30$",
                  "$0{,}80$",
                  "$0{,}50$",
                  "$1{,}00$"
            ],
            "ans": 1,
            "fb": "Đúng! $F(2) = P(X = 1) + P(X = 2) = 0{,}3 + 0{,}5 = 0{,}80$."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Cho $p(x) = c \\cdot x$ với $x \\in \\{1, 2, 3, 4\\}$. Hằng số $c$ bằng:",
            "opts": [
                  "$0{,}10$",
                  "$1{,}00$",
                  "$0{,}05$",
                  "$0{,}25$"
            ],
            "ans": 0,
            "fb": "Chính xác! $\\sum_{x=1}^4 c x = c(1 + 2 + 3 + 4) = 10c = 1 \\implies c = 0{,}10$."
      }
],
    final_quiz: {
      q: "Cho hàm phân phối tích lũy F(x) có F(1) = 0,3 và F(2) = 0,8. Xác suất để X nhận đúng giá trị bằng 2, tức P(X = 2), bằng bao nhiêu?",
      opts: [
        "0,5 (0,8 - 0,3)",
        "0,8",
        "0,3",
        "1,1 (0,8 + 0,3)"
      ],
      ans: 0,
      fb: [
        "Chính xác! P(X = 2) là độ cao của bước nhảy tại x = 2: P(X = 2) = F(2) - F(1) = 0,8 - 0,3 = 0,5.",
        "Sai! 0,8 là F(2) = P(X ≤ 2), bao gồm cả xác suất của các giá trị nhỏ hơn 2.",
        "Sai! 0,3 là F(1) = P(X ≤ 1).",
        "Sai! Xác suất không thể vượt quá 1."
      ]
    }
  },

  {
    id: "C2",
    cluster: "C",
    title: "Phân phối Bernoulli & Phân phối Nhị thức B(n, p)",
    sources: "Slide Week 06 (tr. 36–52); Stat20 Mục 4.3.2.2, 4.3.2.3",
    ref: {
      "slide_file": "week06.pdf",
      "slide_name": "Tuần 06 — Phân phối Bernoulli & Nhị thức",
      "pages": "Slide 37 – 52",
      "page_start": 37,
      "section": "Phần 4: Các phân phối rời rạc thông dụng — Phân phối Bernoulli & Nhị thức B(n, p) (Slide 37–52)",
      "stat20": "Stat20 Mục 4.3.2.2 & 4.3.2.3 (Bernoulli & Binomial Distributions)",
      "key_points": [
            "Dãy phép thử Bernoulli: n phép thử độc lập, mỗi phép thử chỉ có 2 kết quả (Thành công p, Thất bại 1-p)",
            "Công thức xác suất Nhị thức: P(X = k) = C_n^k * p^k * (1 - p)^(n - k)",
            "Bẫy ít nhất 1 lần thành công: P(X ≥ 1) = 1 - P(X = 0) = 1 - (1 - p)^n"
      ],
      "remind": "Nếu bạn chưa tự tin nhận diện các điều kiện của mô hình Nhị thức, hãy mở Slide Week 06 từ trang 39 đến 51."
},
    desc: "Mô hình xác suất thông dụng nhất: Đếm số lần thành công trong n phép thử độc lập. Công thức tổ hợp, kỳ vọng np và phương sai np(1-p).",
    steps: [
      {
        t: "Phép thử Bernoulli(p): Phép thử 2 kết quả",
        c: `<p><b>Phép thử Bernoulli</b> là một phép thử ngẫu nhiên chỉ có đúng 2 kết quả đối lập nhau:</p>
            <ul>
              <li><b>Thành công (1)</b> với xác suất $p$.</li>
              <li><b>Thất bại (0)</b> với xác suất $q = 1 - p$.</li>
            </ul>
            <p><b>Kỳ vọng và Phương sai của Bernoulli(p):</b></p>
            $$E(X) = 1(p) + 0(1-p) = p$$
            $$\\operatorname{Var}(X) = p(1-p), \\quad \\operatorname{SD}(X) = \\sqrt{p(1-p)}$$`
      },
      {
        t: "Phân phối Nhị thức B(n, p): n lần thử độc lập",
        c: `<p>Thực hiện lặp lại $n$ phép thử Bernoulli độc lập, mỗi lần xác suất thành công đều bằng $p$. Gọi $X$ là <b>tổng số lần thành công</b> trong $n$ lần thử $\\implies X \\sim B(n, p)$.</p>
            <p><b>Công thức xác suất nhị thức:</b></p>
            $$P(X = k) = C_n^k \\cdot p^k \\cdot (1 - p)^{n - k} \\quad (k = 0, 1, 2, \\dots, n)$$
            <p><b>Ý nghĩa từng thành phần:</b></p>
            <ul>
              <li>$p^k$: Xác suất để có $k$ lần thành công.</li>
              <li>$(1-p)^{n-k}$: Xác suất để có $n-k$ lần thất bại còn lại.</li>
              <li>$C_n^k$: Số cách phân bổ vị trí $k$ lần thành công trong chuỗi $n$ lần thử.</li>
            </ul>
            <div class="tip-box">
              <b>Kỳ vọng và Phương sai của Nhị thức:</b><br>
              Vì $X$ là tổng của $n$ biến Bernoulli độc lập ($X = Y_1 + \\dots + Y_n$):<br>
              $$E(X) = n \\cdot p$$
              $$\\operatorname{Var}(X) = n \\cdot p(1 - p)$$
              $$\\operatorname{SD}(X) = \\sqrt{n \\cdot p(1 - p)}$$
            </div>`
      },
      {
        t: "4 Điều kiện bắt buộc để áp dụng mô hình Nhị thức",
        c: `<ol>
              <li>Số lượng phép thử $n$ phải cố định từ trước.</li>
              <li>Mỗi phép thử chỉ có đúng 2 kết quả: Thành công hoặc Thất bại.</li>
              <li>Các phép thử phải <b>hoàn toàn độc lập</b> với nhau (hoặc <b>lấy mẫu CÓ HOÀN LẠI</b>).</li>
              <li>Xác suất thành công $p$ phải giữ nguyên không đổi qua mọi lần thử.</li>
            </ol>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 06 — Ví dụ 12] Bài kiểm tra trắc nghiệm 20 câu ngẫu nhiên",
        q: "Một bài kiểm tra có 20 câu trắc nghiệm (Slide 46–47). Mỗi câu có 4 phương án trả lời, trong đó chỉ có duy nhất một phương án đúng. Một học sinh không học bài nên đánh bừa ngẫu nhiên độc lập cả 20 câu.<br>" +
           "a) Xác định mô hình phân phối xác suất của số câu trả lời đúng $X$.<br>" +
           "b) Tính xác suất để học sinh đó làm đúng đúng 5 câu.",
        sol: "<b>Lời giải chi tiết theo Slide Week 06 (trang 47):</b><br>" +
             "a) Mỗi câu hỏi là một phép thử Bernoulli với xác suất đoán đúng $p = \\frac{1}{4} = 0{,}25$.<br>" +
             "   Vì có $n = 20$ câu độc lập nên số câu trả lời đúng tuân theo phân phối Nhị thức:<br>" +
             "   $$X \\sim B(n = 20, p = 0{,}25)$$<br>" +
             "b) Áp dụng công thức phân phối Nhị thức với $k = 5$:<br>" +
             "   $$P(X = 5) = C_{20}^5 p^5 (1-p)^{20-5} = C_{20}^5 (0{,}25)^5 (0{,}75)^{15}$$<br>" +
             "   $$P(X = 5) = 15504 \\times (0{,}25)^5 \\times (0{,}75)^{15} \\approx 0{,}2023 \\approx 20{,}23\\%$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 06 — Ví dụ 13] Dây chuyền sản xuất 12 sản phẩm đạt chuẩn",
        q: "Một dây chuyền tạo sản phẩm đạt chuẩn với xác suất $0{,}95$ (Slide 48–49). Chọn độc lập ngẫu nhiên 12 sản phẩm để kiểm tra chất lượng.<br>" +
           "a) Tính xác suất để toàn bộ 12 sản phẩm được chọn đều đạt chuẩn.<br>" +
           "b) Tính xác suất để có ít nhất một sản phẩm không đạt chuẩn (phế phẩm).",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 06 (trang 49):</b><br>" +
             "Gọi $X$ là số sản phẩm đạt chuẩn trong 12 sản phẩm $\\implies X \\sim B(12, 0{,}95)$.<br>" +
             "a) Xác suất cả 12 sản phẩm đều đạt chuẩn ($k = 12$):<br>" +
             "   $$P(X = 12) = C_{12}^{12} (0{,}95)^{12} (0{,}05)^0 = (0{,}95)^{12} \\approx 0{,}5404 \\approx 54{,}04\\%$$<br>" +
             "b) Biến cố 'Có ít nhất một phế phẩm' chính là biến cố đối của 'Cả 12 sản phẩm đều đạt chuẩn':<br>" +
             "   $$P(\\text{Ít nhất 1 phế phẩm}) = 1 - P(X = 12) = 1 - 0{,}5404 = 0{,}4596 \\approx 45{,}96\\%$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 06 — Ví dụ 20] Hệ thống 8 Cảm biến phát cảnh báo giả",
        q: "Một hệ thống giám sát an ninh có 8 cảm biến hoạt động độc lập (Slide 73–74). Trong một ca làm việc, xác suất mỗi cảm biến phát cảnh báo giả là $p = 0{,}05$. Tính xác suất trong ca đó hệ thống phát ra từ 1 đến 2 cảnh báo giả.",
        sol: "<b>Lời giải từng bước theo Slide Week 06 (trang 74):</b><br>" +
             "Gọi $X$ là số cảm biến phát cảnh báo giả $\\implies X \\sim B(n = 8, p = 0{,}05)$.<br>" +
             "Yêu cầu bài toán là tính $P(1 \\le X \\le 2) = P(X = 1) + P(X = 2)$:<br>" +
             "1. Tính $P(X = 1)$:<br>" +
             "   $$P(X = 1) = C_8^1 (0{,}05)^1 (0{,}95)^7 = 8 \\times 0{,}05 \\times 0{,}69834 \\approx 0{,}2793$$<br>" +
             "2. Tính $P(X = 2)$:<br>" +
             "   $$P(X = 2) = C_8^2 (0{,}05)^2 (0{,}95)^6 = 28 \\times 0{,}0025 \\times 0{,}73509 \\approx 0{,}0515$$<br>" +
             "3. Tổng xác suất:<br>" +
             "   $$P(1 \\le X \\le 2) = 0{,}2793 + 0{,}0515 = 0{,}3308 \\approx 33{,}08\\%$$"
      }
    
    ],
    pitfalls: [
      {
        bad: "Quên nhân hệ số tổ hợp C(n, k) trong công thức nhị thức (chỉ tính p^k * (1-p)^(n-k)).",
        good: "Nếu quên C(n, k), bạn chỉ đang tính xác suất của ĐÚNG MỘT THỨ TỰ CỤ THỂ (ví dụ: k lần đầu thành công, các lần sau thất bại). Phải nhân C(n, k) để tính hết mọi cách sắp xếp!"
      },
      {
        bad: "Áp dụng mô hình nhị thức cho bài toán rút thăm không hoàn lại từ một hộp nhỏ.",
        good: "Rút không hoàn lại từ tập hữu hạn làm thay đổi xác suất p ở mỗi bước $\\implies$ Bắt buộc phải dùng phân phối SIÊU BỘI, không được dùng nhị thức!"
      }
    ],
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Biến ngẫu nhiên $X \\sim \\text{Binomial}(n, p)$ có kỳ vọng và phương sai lần lượt là:",
            "opts": [
                  "$E[X] = n/p;\\quad \\text{Var}(X) = n/p^2$",
                  "$E[X] = np;\\quad \\text{Var}(X) = np(1-p)$",
                  "$E[X] = np;\\quad \\text{Var}(X) = np$",
                  "$E[X] = p;\\quad \\text{Var}(X) = p(1-p)$"
            ],
            "ans": 1,
            "fb": "Chính xác! Công thức giải tích của phân phối Nhị thức."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Tung 5 đồng xu cân đối độc lập. Xác suất xuất hiện đúng 2 mặt Ngửa là:",
            "opts": [
                  "$2/5 = 0{,}40$",
                  "$\\binom{5}{2} (0{,}5)^2 = 2{,}5$",
                  "$\\binom{5}{2} (0{,}5)^5 = 10/32 = 0{,}3125$",
                  "$(0{,}5)^5 = 0{,}03125$"
            ],
            "ans": 2,
            "fb": "Đúng! $P(X = 2) = \\binom{5}{2} (0{,}5)^2 (0{,}5)^3 = 10 \\times 0{,}03125 = 0{,}3125$."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Xác suất bắn trúng mục tiêu là $0{,}2$. Cần bắn ít nhất bao nhiêu phát để xác suất có ít nhất 1 phát trúng $\\ge 90\\%$?",
            "opts": [
                  "$5$ phát",
                  "$15$ phát",
                  "$8$ phát",
                  "$11$ phát"
            ],
            "ans": 3,
            "fb": "Chính xác! $1 - (0{,}8)^n \\ge 0{,}9 \\iff (0{,}8)^n \\le 0{,}1 \\iff n \\ge \\frac{\\ln 0{,}1}{\\ln 0{,}8} \\approx 10{,}32 \\implies n = 11$."
      }
],
    final_quiz: {
      q: "Cho biến ngẫu nhiên X có phân phối Nhị thức B(n = 10, p = 0,3). Phương sai Var(X) bằng bao nhiêu?",
      opts: [
        "2,1",
        "3,0",
        "0,21",
        "7,0"
      ],
      ans: 0,
      fb: [
        "Chính xác! Var(X) = n * p * (1 - p) = 10 * 0,3 * 0,7 = 2,1.",
        "Sai! 3,0 là kỳ vọng E(X) = n * p = 10 * 0,3 = 3.",
        "Sai! 0,21 là p * (1 - p), bạn đã quên nhân với cỡ mẫu n = 10.",
        "Sai! 7,0 là n * (1 - p)."
      ]
    }
  },

  {
    id: "C3",
    cluster: "C",
    title: "Phân phối Siêu bội HG(N, M, n): Rút mẫu không hoàn lại",
    sources: "Slide Week 06 (tr. 53–65); Stat20 Mục 4.3.2.4",
    ref: {
      "slide_file": "week06.pdf",
      "slide_name": "Tuần 06 — Phân phối Siêu bội HG(N, M, n)",
      "pages": "Slide 53 – 65",
      "page_start": 53,
      "section": "Phần 4: Phân phối Siêu bội — Lấy mẫu không hoàn lại từ tổng thể hữu hạn (Slide 53–65)",
      "stat20": "Stat20 Mục 4.3.2.4 (Hypergeometric Distribution)",
      "key_points": [
            "Mô hình rút KHÔNG hoàn lại n phần tử từ hộp N phần tử có M phần tử đặc biệt",
            "Công thức xác suất Siêu bội: P(X = k) = [C_M^k * C_(N-M)^(n-k)] / C_N^n",
            "Liên hệ với Nhị thức: Khi N rất lớn so với n (n/N < 0.05), Siêu bội xấp xỉ Nhị thức với p = M/N"
      ],
      "remind": "Nếu bạn còn phân vân khi nào dùng Nhị thức (rút có hoàn lại), khi nào dùng Siêu bội (rút không hoàn lại), hãy xem lại bảng so sánh ở Slide Week 06 trang 55–62."
},
    desc: "Mô hình rút mẫu không hoàn lại từ tổng thể hữu hạn. Phân biệt triệt để với Nhị thức và điều kiện khi nào Siêu bội xấp xỉ Nhị thức.",
    steps: [
      {
        t: "Bản chất của Phân phối Siêu bội (Hypergeometric Distribution)",
        c: `<p>Xét một tổng thể hữu hạn gồm $N$ phần tử, trong đó có:</p>
            <ul>
              <li>$M$ phần tử thuộc loại đặc biệt ('thành công').</li>
              <li>$N - M$ phần tử không thuộc loại đặc biệt ('thất bại').</li>
            </ul>
            <p>Ta rút ngẫu nhiên <b>$n$ phần tử KHÔNG HOÀN LẠI</b> (hoặc rút đồng thời $n$ phần tử). Gọi $X$ là số phần tử đặc biệt rút được $\\implies X \\sim HG(N, M, n)$.</p>
            <p><b>Công thức hàm xác suất:</b></p>
            $$P(X = k) = \\frac{C_M^k \\cdot C_{N - M}^{n - k}}{C_N^n}$$`
      },
      {
        t: "Kỳ vọng & Phương sai của Siêu bội",
        c: `<p>Đặt tỉ lệ phần tử đặc biệt trong tổng thể là $p = \\frac{M}{N}$:</p>
            <ul>
              <li><b>Kỳ vọng</b>: Giống hệt như phân phối nhị thức!
                  $$E(X) = n \\cdot \\frac{M}{N} = n \\cdot p$$
              </li>
              <li><b>Phương sai</b>: Nhỏ hơn phương sai nhị thức một lượng gọi là <i>Hệ số hiệu chỉnh tổng thể hữu hạn (Finite Population Correction)</i>:
                  $$\\operatorname{Var}(X) = n \\cdot p(1 - p) \\cdot \\left(\\frac{N - n}{N - 1}\\right)$$
              </li>
            </ul>
            <div class="tip-box">
              <b>Vì sao phương sai Siêu bội lại nhỏ hơn Nhị thức?</b><br>
              Vì rút không hoàn lại mang lại nhiều thông tin hơn (mỗi lần rút loại bớt một khả năng), làm cho sự bất định giảm đi, do đó độ phân tán xung quanh tâm nhỏ hơn. Đại lượng $\\frac{N - n}{N - 1} &lt; 1$ chính là thước đo độ giảm phân tán này!
            </div>`
      },
      {
        t: "Khi nào Siêu bội xấp xỉ Nhị thức?",
        c: `<p>Khi quy mô tổng thể $N$ rất lớn so với cỡ mẫu $n$ (quy tắc thực nghiệm: tỉ lệ lấy mẫu $\\frac{n}{N} \\le 0{,}05$, tức lấy mẫu dưới 5% tổng thể):</p>
            $$\\frac{N - n}{N - 1} \\approx 1$$
            <p>Lúc này, việc lấy có hoàn lại hay không hoàn lại hầu như không làm thay đổi thành phần tổng thể, do đó ta có thể <b>dùng phân phối Nhị thức $B(n, p = M/N)$ để xấp xỉ phân phối Siêu bội</b> nhằm đơn giản hóa tính toán.</p>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 06 — Ví dụ 14] Rút ba lá thăm không hoàn lại từ hộp 10 lá",
        q: "Một hộp có 10 lá thăm gồm 6 lá ghi số 1 và 4 lá ghi số 0 (Slide 52–54). Rút lần lượt không hoàn lại 3 lá thăm. Gọi $X$ là số lá thăm ghi số 1 rút được.<br>" +
           "a) Biến ngẫu nhiên $X$ tuân theo phân phối gì? Xác định các tham số.<br>" +
           "b) Tính xác suất rút được đúng 2 lá thăm ghi số 1.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 06 (trang 53):</b><br>" +
             "a) Vì lấy mẫu không hoàn lại từ tập hữu hạn $N = 10$ phần tử có $M = 6$ phần tử loại 1, với cỡ mẫu $n = 3$, nên biến ngẫu nhiên $X$ tuân theo <b>phân phối Siêu bội</b>:<br>" +
             "   $$X \\sim HG(N = 10, M = 6, n = 3)$$<br>" +
             "b) Áp dụng công thức xác suất phân phối Siêu bội với $k = 2$:<br>" +
             "   $$P(X = 2) = \\frac{C_M^k C_{N-M}^{n-k}}{C_N^n} = \\frac{C_6^2 C_4^{3-2}}{C_{10}^3} = \\frac{C_6^2 C_4^1}{C_{10}^3}$$<br>" +
             "   Ta có $C_6^2 = 15, C_4^1 = 4, C_{10}^3 = 120$:<br>" +
             "   $$P(X = 2) = \\frac{15 \\times 4}{120} = \\frac{60}{120} = 0{,}50 \\text{ (hay 50\\%)}$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 06 — Ví dụ 15] Giảng viên chọn ngẫu nhiên bài tập của hai lớp",
        q: "Một giảng viên UET dạy hai lớp môn Xác suất Thống kê gồm 20 và 30 sinh viên (tổng cộng 50 sinh viên, Slide 55–58). Mỗi sinh viên nộp đúng một bài tập. Giảng viên chọn ngẫu nhiên không hoàn lại 15 bài để chấm trước. Gọi $X$ là số bài thuộc về lớp 30 sinh viên.<br>" +
           "a) Xác định phân phối của $X$.<br>" +
           "b) Thiết lập biểu thức tính xác suất để chọn được đúng 9 bài thuộc lớp 30 sinh viên.",
        sol: "<b>Lời giải chi tiết theo Slide Week 06 (trang 56):</b><br>" +
             "a) Tổng số sinh viên $N = 50$, số bài của lớp xét đến là $M = 30$, cỡ mẫu rút ra là $n = 15$ bài.<br>" +
             "   Vì rút không hoàn lại nên $X$ tuân theo phân phối Siêu bội:<br>" +
             "   $$X \\sim HG(N = 50, M = 30, n = 15)$$<br>" +
             "b) Xác suất chọn được đúng $k = 9$ bài của lớp này là:<br>" +
             "   $$P(X = 9) = \\frac{C_{30}^9 C_{20}^{15-9}}{C_{50}^{15}} = \\frac{C_{30}^9 C_{20}^6}{C_{50}^{15}} \\approx 0{,}256 \\approx 25{,}6\\%$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 06 — Ví dụ 16] So sánh Rút có hoàn lại vs Không hoàn lại",
        q: "Một hộp có 4 quả bóng, gồm 2 quả đỏ và 2 quả xanh (Slide 59–60). Rút ngẫu nhiên 2 quả bóng.<br>" +
           "a) Nếu rút CÓ HOÀN LẠI: Tính xác suất rút được 2 quả bóng đỏ.<br>" +
           "b) Nếu rút KHÔNG HOÀN LẠI: Tính xác suất rút được 2 quả bóng đỏ.<br>" +
           "c) Khi nào thì mô hình Rút không hoàn lại (Siêu bội) có thể xấp xỉ an toàn bằng Rút có hoàn lại (Nhị thức)?",
        sol: "<b>Phân tích bản chất theo Slide Week 06 (trang 60):</b><br>" +
             "a) <b>Rút có hoàn lại (Nhị thức):</b> Các lần rút độc lập, $P(\\text{Đỏ}) = 2/4 = 0{,}5$ không đổi:<br>" +
             "   $$P(\\text{2 Đỏ}) = \\left(\\frac{2}{4}\\right) \\times \\left(\\frac{2}{4}\\right) = \\frac{1}{4} = 0{,}25$$<br>" +
             "b) <b>Rút không hoàn lại (Siêu bội):</b> Lần 1 lấy 1 đỏ thì trong hộp chỉ còn 1 đỏ trên 3 bóng:<br>" +
             "   $$P(\\text{2 Đỏ}) = \\frac{C_2^2 C_2^0}{C_4^2} = \\frac{1 \\times 1}{6} = \\frac{1}{6} \\approx 0{,}1667$$<br>" +
             "c) <b>Điều kiện xấp xỉ:</b> Khi kích thước tổng thể $N$ rất lớn so với cỡ mẫu $n$ (quy tắc thực nghiệm: cỡ mẫu không vượt quá 5% tổng thể, tức $n/N < 0{,}05$), việc rút một phần tử hầu như không làm thay đổi tỉ lệ còn lại trong hộp, nên Siêu bội xấp xỉ Nhị thức với $p = M/N$."
      }
    
    ],
    pitfalls: [
      {
        bad: "Dùng công thức Nhị thức C(n, k) * p^k * (1-p)^(n-k) cho bài toán rút bi không hoàn lại từ hộp chỉ có 10-20 viên.",
        good: "Khi tổng thể N nhỏ (dưới vài trăm phần tử), rút không hoàn lại BẮT BUỘC phải dùng công thức tỷ lệ tổ hợp của Siêu bội!"
      },
      {
        bad: "Quên điều kiện của k: k có thể vượt quá M hoặc n - k vượt quá N - M.",
        good: "Luôn kiểm tra: số phần tử rút ra không thể vượt quá số lượng đang có trong hộp (k ≤ M và n - k ≤ N - M)."
      }
    ],
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Phân phối Siêu bội (Hypergeometric) được áp dụng trong tình huống nào?",
            "opts": [
                  "Rút mẫu ngẫu nhiên CÓ hoàn lại",
                  "Số biến cố xuất hiện trong một khoảng thời gian liên tục",
                  "Rút mẫu ngẫu nhiên KHÔNG hoàn lại từ một tập hợp hữu hạn",
                  "Số lần thử cho đến khi thành công lần đầu"
            ],
            "ans": 2,
            "fb": "Chính xác! Rút không hoàn lại làm xác suất thành công thay đổi qua mỗi lần rút."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Một hộp có 10 sản phẩm (7 tốt, 3 hỏng). Rút không hoàn lại 2 sản phẩm. Kỳ vọng số sản phẩm hỏng rút được là:",
            "opts": [
                  "$1{,}0$",
                  "$0{,}3$",
                  "$1{,}4$",
                  "$2 \\times \\frac{3}{10} = 0{,}6$"
            ],
            "ans": 3,
            "fb": "Đúng! Kỳ vọng phân phối Siêu bội $E[X] = n \\frac{M}{N} = 2 \\times \\frac{3}{10} = 0{,}6$."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Khi nào phân phối Siêu bội có thể được xấp xỉ an toàn bằng phân phối Nhị thức?",
            "opts": [
                  "Khi cỡ mẫu nhỏ so với quy mô tổng thể ($n / N \\le 0{,}05$)",
                  "Khi $p = 0{,}5$",
                  "Khi $N \\le 30$",
                  "Không bao giờ được xấp xỉ"
            ],
            "ans": 0,
            "fb": "Chính xác! Khi tổng thể $N$ rất lớn so với cỡ mẫu $n$, việc rút không hoàn lại làm thay đổi xác suất không đáng kể."
      }
],
    final_quiz: {
      q: "Một hộp có 20 quả bóng (8 đỏ, 12 xanh). Rút ngẫu nhiên đồng thời 5 quả bóng và đếm số bóng đỏ. Biến ngẫu nhiên này tuân theo phân phối nào?",
      opts: [
        "Siêu bội (Hypergeometric)",
        "Nhị thức (Binomial)",
        "Poisson",
        "Bernoulli"
      ],
      ans: 0,
      fb: [
        "Chính xác! Rút đồng thời tương đương rút liên tiếp KHÔNG hoàn lại từ tổng thể hữu hạn N = 20, do đó tuân theo phân phối Siêu bội.",
        "Sai! Nhị thức chỉ áp dụng khi rút CÓ HOÀN LẠI.",
        "Sai! Poisson áp dụng khi đếm biến cố trong khoảng liên tục.",
        "Sai! Bernoulli chỉ gồm đúng 1 phép thử duy nhất (n = 1)."
      ]
    }
  },

  {
    id: "C4",
    cluster: "C",
    title: "Phân phối Poisson(λ) & Cây quyết định chọn mô hình",
    sources: "Slide Week 06 (tr. 66–80); Stat20 Mục 4.3.2.5, 4.3.2.6",
    ref: {
      "slide_file": "week06.pdf",
      "slide_name": "Tuần 06 — Phân phối Poisson & Cây quyết định mô hình",
      "pages": "Slide 66 – 80",
      "page_start": 66,
      "section": "Phần 4: Phân phối Poisson (Slide 66–69) & Phần 5: Cây quyết định lựa chọn mô hình rời rạc (Slide 70–80)",
      "stat20": "Stat20 Mục 4.3.2.5 & 4.3.2.6 (Poisson Distribution & Model Selection)",
      "key_points": [
            "Phân phối Poisson Po(λ): Mô hình hóa số biến cố hiếm xảy ra trong một khoảng thời gian/không gian liên tục",
            "Công thức xác suất: P(X = k) = (λ^k * e^(-λ)) / k!",
            "Quy tắc đổi tham số theo khoảng thời gian: λ' = λ * t; Xấp xỉ Poisson cho Nhị thức khi n ≥ 20, p ≤ 0.05"
      ],
      "remind": "Nếu bạn muốn nắm chắc sơ đồ chọn nhanh mô hình (Nhị thức, Siêu bội hay Poisson) khi đọc đề thi, hãy xem ngay Slide Week 06 trang 70–78."
},
    desc: "Mô hình đếm các sự kiện xảy ra trong một khoảng liên tục (thời gian/không gian). Bí quyết vàng: Kỳ vọng bằng Phương sai, và Cây quyết định chọn đúng mô hình thi.",
    steps: [
      {
        t: "Bản chất của Phân phối Poisson($\\lambda$)",
        c: `<p><b>Phân phối Poisson</b> mô hình hóa <b>số lần xảy ra một sự kiện hiếm</b> trong một khoảng liên tục cố định (thời gian, diện tích, thể tích, chiều dài):</p>
            <ul>
              <li>Số cuộc gọi đến tổng đài hỗ trợ kỹ thuật trong 1 giờ.</li>
              <li>Số lỗi chính tả trên 1 trang sách.</li>
              <li>Số vụ tai nạn giao thông tại một ngã tư trong 1 tuần.</li>
            </ul>
            <p><b>Công thức xác suất:</b></p>
            $$P(X = k) = \\frac{\\lambda^k \\cdot e^{-\\lambda}}{k!} \\quad (k = 0, 1, 2, \\dots)$$
            <p>Trong đó: $\\lambda &gt; 0$ là số sự kiện trung bình xảy ra trong khoảng đang xét; $e \\approx 2{,}71828$.</p>`
      },
      {
        t: "Đặc điểm kỳ diệu: Kỳ vọng bằng đúng Phương sai!",
        c: `<div class="tip-box">
              <b>Dấu hiệu nhận diện số 1 của Poisson trong đề thi:</b><br>
              $$E(X) = \\lambda$$
              $$\\operatorname{Var}(X) = \\lambda$$
              $$\\operatorname{SD}(X) = \\sqrt{\\lambda}$$
              <i>Nếu một đề bài trắc nghiệm hỏi: 'Phân phối nào có kỳ vọng và phương sai luôn bằng nhau?', câu trả lời chắc chắn là <b>Poisson</b>!</i>
            </div>`
      },
      {
        t: "🌳 CÂY QUYẾT ĐỊNH CHỌN MÔ HÌNH RỜI RẠC (LƯỢC ĐỒ VÀNG PHÒNG THI)",
        c: `<p>Đọc đề bài thi, hãy trả lời tuần tự các câu hỏi sau để chọn đúng 100% công thức:</p>
            <div class="code-box">
<b>Câu hỏi 1: Có phải đang đếm số sự kiện trong một KHOẢNG LIÊN TỤC (thời gian, diện tích)?</b>
├── ĐÚNG ──> <b>PHÂN PHỐI POISSON(λ)</b> [Công thức: λ^k * e^(-λ) / k!]
└── SAI ───> Đi tiếp sang Câu hỏi 2.

<b>Câu hỏi 2: Có bao nhiêu phép thử được thực hiện?</b>
├── Chỉ đúng 1 lần (n = 1, thành công/thất bại) ──> <b>BERNOULLI(p)</b>
└── Lặp lại n lần (n > 1) ──> Đi tiếp sang Câu hỏi 3.

<b>Câu hỏi 3: Phép rút mẫu / thử nghiệm diễn ra như thế nào?</b>
├── <b>CÓ HOÀN LẠI</b> (hoặc các lần thử độc lập, xúc xắc, đồng xu) ──> <b>NHỊ THỨC B(n, p)</b>
└── <b>KHÔNG HOÀN LẠI</b> từ một nhóm hữu hạn N phần tử ─────────> <b>SIÊU BỘI HG(N, M, n)</b>
            </div>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 06 — Ví dụ 17 & 18] Máy chủ nhận yêu cầu mỗi giây",
        q: "Một máy chủ web nhận trung bình 4 yêu cầu (requests) mỗi giây (Slide 65–66). Giả sử các yêu cầu đến độc lập ngẫu nhiên tuân theo phân phối Poisson $\\lambda = 4$ yêu cầu/giây.<br>" +
           "a) Tính xác suất trong 1 giây cụ thể máy chủ không nhận được yêu cầu nào.<br>" +
           "b) Tính xác suất trong 1 giây máy chủ nhận được đúng 3 yêu cầu.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 06 (trang 66):</b><br>" +
             "Gọi $X$ là số yêu cầu máy chủ nhận trong 1 giây $\\implies X \\sim Po(\\lambda = 4)$.<br>" +
             "Công thức Poisson: $P(X = k) = \\frac{\\lambda^k e^{-\\lambda}}{k!}$.<br>" +
             "a) Với $k = 0$:<br>" +
             "   $$P(X = 0) = \\frac{4^0 e^{-4}}{0!} = e^{-4} \\approx 0{,}0183 \\approx 1{,}83\\%$$<br>" +
             "b) Với $k = 3$:<br>" +
             "   $$P(X = 3) = \\frac{4^3 e^{-4}}{3!} = \\frac{64 \\times 0{,}0183156}{6} \\approx 0{,}1954 \\approx 19{,}54\\%$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 06 — Slide 66–69] Quy tắc đổi tham số theo Khoảng thời gian",
        q: "Vẫn với máy chủ ở trên (trung bình 4 yêu cầu/giây). Hãy tính xác suất trong khoảng thời gian kéo dài 2 giây, máy chủ nhận được đúng 6 yêu cầu.",
        sol: "<b>Lời giải chi tiết theo Slide Week 06:</b><br>" +
             "1. Khi khoảng thời gian quan sát thay đổi từ $t_1 = 1\\text{s}$ sang $t_2 = 2\\text{s}$, tham số trung bình Poisson phải được tỉ lệ thuận theo độ dài khoảng thời gian:<br>" +
             "   $$\\lambda' = \\lambda \\times t = 4 \\times 2 = 8 \\text{ yêu cầu/2 giây}$$<br>" +
             "2. Gọi $Y$ là số yêu cầu trong 2 giây $\\implies Y \\sim Po(\\lambda' = 8)$.<br>" +
             "   Áp dụng công thức Poisson với $k = 6$:<br>" +
             "   $$P(Y = 6) = \\frac{8^6 e^{-8}}{6!} = \\frac{262144 \\times 0{,}00033546}{720} \\approx 0{,}1221 \\approx 12{,}21\\%$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 06 — Ví dụ 19 & 21] Cây quyết định chọn Mô hình rời rạc & Bài toán Garage",
        q: "Một cửa hàng cơ khí bán hai loại bộ mở cửa garage (Slide 75–77): loại truyền động xích và loại trục vít. Có 15 khách hàng mua độc lập, mỗi khách chọn loại xích với xác suất $0{,}75$. Trong kho hiện còn 12 bộ xích và 8 bộ trục vít.<br>" +
           "a) Dựa vào cây quyết định lựa chọn mô hình, số khách chọn mua loại xích $X$ tuân theo phân phối nào?<br>" +
           "b) Cửa hàng đáp ứng được cả 15 khách khi nào? Thiết lập biểu thức tính xác suất đó.",
        sol: "<b>Phân tích bản chất theo Slide Week 06 (trang 71 & 76–77):</b><br>" +
             "a) Có $n = 15$ khách hàng mua độc lập, mỗi người chỉ chọn xích hoặc trục vít với xác suất chọn xích $p = 0{,}75$ không đổi $\\implies X \\sim B(n = 15, p = 0{,}75)$.<br>" +
             "b) Điều kiện để đáp ứng đủ cả 15 khách:<br>" +
             "   - Số khách mua loại xích không vượt quá số lượng trong kho: $X \\le 12$.<br>" +
             "   - Số khách mua loại trục vít ($15 - X$) không vượt quá 8 bộ: $15 - X \\le 8 \\implies X \\ge 7$.<br>" +
             "   Do đó, cửa hàng đáp ứng đủ khi và chỉ khi: $7 \\le X \\le 12$.<br>" +
             "   Biểu thức xác suất:<br>" +
             "   $$P(7 \\le X \\le 12) = \\sum_{k=7}^{12} C_{15}^k (0{,}75)^k (0{,}25)^{15-k} \\approx 0{,}8006 \\approx 80{,}06\\%$$"
      }
    
    ],
    pitfalls: [
      {
        bad: "Nhầm lẫn giữa 0! = 1 và 0! = 0 khi tính P(X = 0).",
        good: "Trong toán học, quy ước chuẩn xác 0! = 1! Do đó P(X = 0) = e^(-λ), không bao giờ có chuyện chia cho 0!"
      },
      {
        bad: "Quên đổi tham số λ khi khoảng thời gian thay đổi.",
        good: "Nếu đề cho λ = 4 cuộc/giờ, nhưng hỏi trong 30 phút thì phải đổi λ mới = 4 * 0,5 = 2 cuộc!"
      }
    ],
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Đặc trưng nổi bật của biến ngẫu nhiên tuân theo phân phối Poisson($\\lambda$) là:",
            "opts": [
                  "Hàm phân phối có dạng đối xứng hoàn hảo",
                  "Phương sai bằng chính kỳ vọng: $\\text{Var}(X) = E[X] = \\lambda$",
                  "Phương sai luôn gấp đôi kỳ vọng",
                  "Giá trị chỉ nhận từ 0 đến $n$"
            ],
            "ans": 1,
            "fb": "Chính xác! Với Poisson, $E[X] = \\lambda$ và $\\text{Var}(X) = \\lambda$."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Trung bình có 2 cuộc gọi tới tổng đài mỗi phút ($X \\sim \\text{Poisson}(2)$). Xác suất không có cuộc gọi nào trong 1 phút là:",
            "opts": [
                  "$e^{-2} \\approx 0{,}1353$",
                  "$2 e^{-2} \\approx 0{,}2707$",
                  "$0$",
                  "$1 - e^{-2} \\approx 0{,}8647$"
            ],
            "ans": 0,
            "fb": "Đúng! $P(X = 0) = \\frac{2^0 e^{-2}}{0!} = e^{-2} \\approx 0{,}1353$."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Một trang web có tỷ lệ click quảng cáo $p = 0{,}001$. Trong $n = 5000$ lượt xem, áp dụng xấp xỉ Poisson, tham số $\\lambda$ là:",
            "opts": [
                  "$\\lambda = 50$",
                  "$\\lambda = 5000$",
                  "$\\lambda = np = 5$",
                  "$\\lambda = 0{,}5$"
            ],
            "ans": 2,
            "fb": "Chính xác! Quy tắc Poisson xấp xỉ Nhị thức: $\\lambda = np = 5000 \\times 0{,}001 = 5$."
      }
],
    final_quiz: {
      q: "Số lượt khách truy cập vào một trang web thương mại điện tử trung bình là 10 lượt mỗi phút. Mô hình phân phối xác suất nào là phù hợp nhất?",
      opts: [
        "Poisson",
        "Nhị thức",
        "Siêu bội",
        "Chuẩn"
      ],
      ans: 0,
      fb: [
        "Chính xác! Đếm số lượng sự kiện xảy ra trong một khoảng thời gian cố định (1 phút) với tỷ lệ trung bình λ = 10 là đặc trưng chuẩn mực của phân phối Poisson.",
        "Sai! Nhị thức cần số lần thử cố định n, ở đây không có giới hạn trên của số lượt truy cập.",
        "Sai! Siêu bội áp dụng khi rút mẫu không hoàn lại từ nhóm hữu hạn.",
        "Sai! Số lượt khách là số nguyên đếm được (rời rạc), còn phân phối Chuẩn là phân phối liên tục."
      ]
    }
  },

  {
    id: "C5",
    cluster: "C",
    title: "Kỳ vọng E(X), LOTUS & Tính chất tuyến tính",
    sources: "Slide Week 07 (tr. 4–13); Stat20 Mục 4.7, 4.8",
    ref: {
      "slide_file": "week07.pdf",
      "slide_name": "Tuần 07 — Kỳ vọng & Tính chất tuyến tính",
      "pages": "Slide 4 – 13",
      "page_start": 4,
      "section": "Phần 1: Kỳ vọng và phương sai — Định nghĩa và Tính chất của Kỳ vọng (Slide 4–13)",
      "stat20": "Stat20 Mục 4.7 & 4.8 (Expected Value & LOTUS)",
      "key_points": [
            "Kỳ vọng E(X) = ∑ x*p(x): Trọng tâm khối lượng của phân phối xác suất",
            "Định lý LOTUS: E[g(X)] = ∑ g(x)*p(x) (không cần tìm phân phối của g(X))",
            "Tính chất tuyến tính vô điều kiện: E(aX + b) = a*E(X) + b và E(X + Y) = E(X) + E(Y) (kể cả khi không độc lập)"
      ],
      "remind": "Nếu bạn chưa nắm được bản chất trực giác của kỳ vọng như một điểm tựa cân bằng trên bập bênh, hãy xem hình minh họa trực quan ở Slide Week 07 trang 5–9."
},
    desc: "Hiểu sâu kỳ vọng như tâm khối lượng. Luật vô thức LOTUS để tính kỳ vọng của hàm g(X). Tính tuyến tính tuyệt đối của kỳ vọng (đúng kể cả khi không độc lập).",
    steps: [
      {
        t: "Định nghĩa Kỳ vọng toán học (Expected Value)",
        c: `<p><b>Kỳ vọng $E(X)$</b> (ký hiệu $\\mu$ hoặc $E(X)$) là giá trị trung bình có trọng số của mọi giá trị mà biến ngẫu nhiên có thể nhận, với trọng số chính là xác suất tương ứng:</p>
            $$E(X) = \\sum_{x} x \\cdot p_X(x)$$
            <div class="tip-box">
              <b>Ý nghĩa thực tế:</b> Nếu bạn chơi một trò chơi có thưởng rất nhiều lần, số tiền trung bình bạn thắng được ở mỗi ván chơi trong dài hạn sẽ tiến về đúng $E(X)$.
            </div>`
      },
      {
        t: "Kỳ vọng của hàm: Luật thống kê vô thức (LOTUS)",
        c: `<p>Nếu $Y = g(X)$ là một hàm biến đổi của $X$, ta không cần mất công tìm bảng phân phối xác suất của $Y$, mà có thể tính trực tiếp bằng <b>Luật thống kê vô thức (Law of the Unconscious Statistician - LOTUS)</b>:</p>
            $$E[g(X)] = \\sum_{x} g(x) \\cdot p_X(x)$$
            <p><b>Đặc biệt quan trọng:</b> Mômen bậc hai $E(X^2)$:</p>
            $$E(X^2) = \\sum_{x} x^2 \\cdot p_X(x)$$`
      },
      {
        t: "Tính chất Tuyến tính của Kỳ vọng (Linearity of Expectation)",
        c: `<p>Kỳ vọng có một tính chất đại số tuyệt đẹp và cực kỳ mạnh mẽ:</p>
            <ol>
              <li><b>Nhân hệ số và cộng hằng số:</b>
                  $$E(aX + b) = a \\cdot E(X) + b$$
              </li>
              <li><b>Tính cộng của kỳ vọng:</b>
                  $$E(X + Y) = E(X) + E(Y)$$
                  <div class="warn-box">
                    <b>LƯU Ý CỐT TỬ:</b> Công thức $E(X + Y) = E(X) + E(Y)$ <b>LUÔN LUÔN ĐÚNG</b> đối với mọi biến ngẫu nhiên $X$ và $Y$, <b>bất kể $X$ và $Y$ có độc lập với nhau hay không</b>!
                  </div>
              </li>
            </ol>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 07 — Ví dụ 1] Kỳ vọng số sản phẩm đạt chuẩn",
        q: "Hai sản phẩm được kiểm tra độc lập; mỗi sản phẩm đạt chuẩn với xác suất $0{,}8$ (Slide 6). Gọi $X$ là số sản phẩm đạt chuẩn có phân phối xác suất: $p(0)=0{,}04; p(1)=0{,}32; p(2)=0{,}64$. Hãy tính kỳ vọng $E(X)$ và giải thích ý nghĩa tâm khối lượng.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 07 (trang 6):</b><br>" +
             "1. Áp dụng định nghĩa kỳ vọng của biến rời rạc:<br>" +
             "   $$E(X) = \\sum_{x} x \\cdot p_X(x) = 0 \\times 0{,}04 + 1 \\times 0{,}32 + 2 \\times 0{,}64$$<br>" +
             "   $$E(X) = 0 + 0{,}32 + 1{,}28 = 1{,}6 \\text{ sản phẩm}$$<br>" +
             "2. <b>Ý nghĩa tâm khối lượng:</b> Điểm $1{,}6$ chính là trọng tâm (điểm cân bằng cơ học) của hệ quả cân đặt tại các vị trí $x=0, 1, 2$ với các khối lượng tương ứng là $0{,}04; 0{,}32; 0{,}64$."
      },
      {
        level: "Trung bình",
        t: "[Slide Week 07 — Ví dụ 2] Tính chất tuyến tính: Chi phí xử lý lô hàng",
        q: "Một cơ sở kiểm tra hai sản phẩm độc lập (Slide 8–9). Chi phí kiểm tra và xử lý lô hàng phụ thuộc vào số sản phẩm đạt chuẩn $X$ theo công thức: $C = 50 + 20X$ (nghìn đồng). Biết $E(X) = 1{,}6$. Hãy tính kỳ vọng chi phí $E(C)$.",
        sol: "<b>Lời giải chi tiết theo Slide Week 07 (trang 9):</b><br>" +
             "Áp dụng tính chất tuyến tính của kỳ vọng: $E(aX + b) = aE(X) + b$ với $a = 20, b = 50$:<br>" +
             "$$E(C) = E(50 + 20X) = 50 + 20E(X)$$<br>" +
             "$$E(C) = 50 + 20 \\times 1{,}6 = 50 + 32 = 82 \\text{ nghìn đồng}$$<br>" +
             "<i>Không cần phải lập lại bảng phân phối xác suất cho $C$ nhờ tính chất tuyến tính kỳ diệu của kỳ vọng!</i>"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 07 — Ví dụ 3] Trò chơi gieo đồng xu của An và hai người bạn",
        q: "An mời hai người bạn đến ăn bánh (Slide 11–12). Mỗi người bạn độc lập tung một đồng xu cân đối: nếu ra Ngửa thì đến dự, nếu ra Sấp thì ở nhà. Gọi $N$ là tổng số bạn đến dự tiệc. Dùng tính chất tuyến tính tính kỳ vọng $E(N)$ bằng hai biến chỉ báo.",
        sol: "<b>Lời giải thông minh theo Slide Week 07 (trang 12):</b><br>" +
             "1. Đặt $I_1$ là biến chỉ báo người bạn thứ nhất đến dự ($I_1 = 1$ nếu ngửa, $0$ nếu sấp) $\\implies E(I_1) = 1 \\times 0{,}5 + 0 \\times 0{,}5 = 0{,}5$.<br>" +
             "2. Tương tự, $I_2$ là biến chỉ báo người bạn thứ hai đến dự $\\implies E(I_2) = 0{,}5$.<br>" +
             "3. Tổng số người đến dự tiệc là $N = I_1 + I_2$. Theo tính chất tuyến tính của kỳ vọng:<br>" +
             "   $$E(N) = E(I_1 + I_2) = E(I_1) + E(I_2) = 0{,}5 + 0{,}5 = 1 \\text{ người}$$"
      }
    
    ],
    pitfalls: [
      {
        bad: "Nghĩ rằng E(X + Y) chỉ bằng E(X) + E(Y) khi X và Y độc lập.",
        good: "Kỳ vọng có tính tuyến tính vô điều kiện! Tính cộng luôn đúng kể cả khi X và Y phụ thuộc chặt chẽ vào nhau."
      },
      {
        bad: "Tính E(X^2) bằng cách lấy [E(X)]^2.",
        good: "E(X^2) và [E(X)]^2 là hai đại lượng hoàn toàn khác nhau. Hiệu của chúng chính là Phương sai!"
      }
    ],
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Tính chất tuyến tính của kỳ vọng khẳng định rằng với mọi biến ngẫu nhiên $X, Y$ (dù độc lập hay phụ thuộc):",
            "opts": [
                  "$E[1/X] = 1/E[X]$",
                  "$E[aX + bY + c] = aE[X] + bE[Y] + c$",
                  "$E[X^2] = (E[X])^2$",
                  "$E[XY] = E[X]E[Y]$"
            ],
            "ans": 1,
            "fb": "Chính xác! Kỳ vọng luôn có tính tuyến tính không phụ thuộc vào tính độc lập."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Cho $E[X] = 4$. Kỳ vọng của $Y = 3X - 5$ bằng:",
            "opts": [
                  "$4$",
                  "$12$",
                  "$17$",
                  "$7$"
            ],
            "ans": 3,
            "fb": "Đúng! $E[Y] = 3(4) - 5 = 12 - 5 = 7$."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Bất đẳng thức Jensen khẳng định rằng với một hàm lồi $g(x) = x^2$, mối quan hệ giữa $E[X^2]$ và $(E[X])^2$ là:",
            "opts": [
                  "$E[X^2] \\ge (E[X])^2$, dấu bằng xảy ra khi và chỉ khi $X$ là hằng số",
                  "$E[X^2] \\le (E[X])^2$",
                  "$E[X^2] = (E[X])^2$",
                  "$E[X^2] - (E[X])^2 < 0$"
            ],
            "ans": 0,
            "fb": "Chính xác! Vì phương sai $\\text{Var}(X) = E[X^2] - (E[X])^2 \\ge 0 \\implies E[X^2] \\ge (E[X])^2$."
      }
],
    final_quiz: {
      q: "Cho biến ngẫu nhiên X có E(X) = 4. Tính kỳ vọng E(3X + 2).",
      opts: [
        "14",
        "12",
        "10",
        "38"
      ],
      ans: 0,
      fb: [
        "Chính xác! Theo tính chất tuyến tính: E(3X + 2) = 3*E(X) + 2 = 3*4 + 2 = 14.",
        "Sai! 12 là 3*E(X), bạn đã quên cộng thêm hằng số 2.",
        "Sai! Tính toán nhầm.",
        "Sai! 38 là 9*4 + 2, bạn đã nhầm sang hệ số bình phương của phương sai."
      ]
    }
  },

  {
    id: "C6",
    cluster: "C",
    title: "Phương sai Var(X), Độ lệch chuẩn SD(X) & Tính chất",
    sources: "Slide Week 07 (tr. 14–20, 79–81); Stat20 Mục 4.10",
    ref: {
      "slide_file": "week07.pdf",
      "slide_name": "Tuần 07 — Phương sai & Độ lệch chuẩn",
      "pages": "Slide 14 – 20, 79 – 81",
      "page_start": 14,
      "section": "Phần 1: Phương sai và độ lệch chuẩn (Slide 14–20) & Phần 7: Bài tập vận dụng 1 (Slide 79–81)",
      "stat20": "Stat20 Mục 4.10 (Variance & Standard Deviation)",
      "key_points": [
            "Định nghĩa: Var(X) = E[(X - μ)^2] = E(X^2) - [E(X)]^2; Độ lệch chuẩn SD(X) = √Var(X)",
            "Tính chất biến đổi: Var(aX + b) = a^2 * Var(X) và SD(aX + b) = |a| * SD(X)",
            "Khi X, Y độc lập: Var(X ± Y) = Var(X) + Var(Y) (luôn cộng phương sai, không bao giờ trừ)"
      ],
      "remind": "Nếu bạn hay làm sai bài tập tính Var(2X - 3Y) hoặc quên bình phương hệ số a^2, hãy đọc kỹ Slide Week 07 trang 16–19 và lời giải bài mẫu số 1 ở Slide 79–81."
},
    desc: "Đo lường độ rung lắc và rủi ro. Công thức rút gọn E(X²) - [E(X)]², biến đổi tuyến tính Var(aX+b) = a²Var(X) và thứ nguyên đơn vị bắt buộc.",
    steps: [
      {
        t: "Định nghĩa Phương sai & Độ lệch chuẩn",
        c: `<p>Đặt $\\mu = E(X)$. <b>Phương sai $\\operatorname{Var}(X)$</b> đo trung bình bình phương độ lệch của biến ngẫu nhiên khỏi tâm kỳ vọng:</p>
            $$\\operatorname{Var}(X) = E\\left[(X - \\mu)^2\\right] = \\sum_{x} (x - \\mu)^2 \\cdot p_X(x)$$
            <p><b>Độ lệch chuẩn $\\operatorname{SD}(X)$</b> là căn bậc hai của phương sai, giúp đưa đơn vị đo quay về cùng thứ nguyên với $X$:</p>
            $$\\operatorname{SD}(X) = \\sqrt{\\operatorname{Var}(X)}$$`
      },
      {
        t: "Công thức rút gọn thần thánh (Shortcut Formula)",
        c: `<p>Trong bài thi, tính phương sai theo định nghĩa gốc rất lâu và dễ nhầm số thập phân. Hãy luôn sử dụng <b>công thức rút gọn</b>:</p>
            $$\\operatorname{Var}(X) = E(X^2) - [E(X)]^2$$
            <div class="tip-box">
              <b>Quy trình 3 bước tính phương sai từ bảng phân phối:</b><br>
              1. Tính $E(X) = \\sum x \\cdot p(x)$.<br>
              2. Tính $E(X^2) = \\sum x^2 \\cdot p(x)$.<br>
              3. Lấy $E(X^2)$ trừ đi bình phương $[E(X)]^2$.
            </div>`
      },
      {
        t: "Tính chất biến đổi tuyến tính của Phương sai",
        c: `<p>Với mọi hằng số $a, b$:</p>
            $$\\operatorname{Var}(aX + b) = a^2 \\cdot \\operatorname{Var}(X)$$
            $$\\operatorname{SD}(aX + b) = |a| \\cdot \\operatorname{SD}(X)$$
            <p><b>Phương sai của tổng hai biến ngẫu nhiên:</b></p>
            $$\\operatorname{Var}(X + Y) = \\operatorname{Var}(X) + \\operatorname{Var}(Y) \\quad \\text{(BẮT BUỘC } X, Y \\text{ PHẢI ĐỘC LẬP!)}$$
            <div class="warn-box">
              <b>Phân biệt cực kỳ cẩn thận:</b><br>
              - Kỳ vọng: $E(X + Y) = E(X) + E(Y)$ (LUÔN ĐÚNG, không cần độc lập).<br>
              - Phương sai: $\\operatorname{Var}(X + Y) = \\operatorname{Var}(X) + \\operatorname{Var}(Y)$ (CHỈ ĐÚNG KHI $X, Y$ ĐỘC LẬP).
            </div>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 07 — Ví dụ 4] Phương sai và Độ lệch chuẩn số sản phẩm đạt chuẩn",
        q: "Với biến ngẫu nhiên $X$ (số sản phẩm đạt chuẩn trong 2 sản phẩm, Slide 15) có bảng phân phối: $p(0)=0{,}04; p(1)=0{,}32; p(2)=0{,}64$ và $E(X) = 1{,}6$.<br>" +
           "a) Tính $E(X^2)$ bằng định lý LOTUS.<br>" +
           "b) Dùng công thức rút gọn tính phương sai $\\operatorname{Var}(X)$ và độ lệch chuẩn $\\operatorname{SD}(X)$.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 07 (trang 15):</b><br>" +
             "a) Theo định lý LOTUS:<br>" +
             "   $$E(X^2) = \\sum x^2 p(x) = 0^2(0{,}04) + 1^2(0{,}32) + 2^2(0{,}64) = 0 + 0{,}32 + 2{,}56 = 2{,}88$$<br>" +
             "b) Áp dụng công thức rút gọn phương sai:<br>" +
             "   $$\\operatorname{Var}(X) = E(X^2) - [E(X)]^2 = 2{,}88 - (1{,}6)^2 = 2{,}88 - 2{,}56 = 0{,}32$$<br>" +
             "   Độ lệch chuẩn:<br>" +
             "   $$\\operatorname{SD}(X) = \\sqrt{\\operatorname{Var}(X)} = \\sqrt{0{,}32} \\approx 0{,}5657$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 07 — Ví dụ 5] Đổi thang đo Nhiệt độ Celsius sang Fahrenheit",
        q: "Nhiệt độ $X$ tính theo độ Celsius có $E(X) = 25^\\circ\\text{C}$ và $\\operatorname{SD}(X) = 3^\\circ\\text{C}$ (Slide 18–19). Nhiệt độ tính theo độ Fahrenheit là $Y = 1{,}8X + 32$.<br>" +
           "a) Tính kỳ vọng $E(Y)$.<br>" +
           "b) Tính độ lệch chuẩn $\\operatorname{SD}(Y)$ và phương sai $\\operatorname{Var}(Y)$.",
        sol: "<b>Lời giải chuẩn xác theo Slide Week 07 (trang 19):</b><br>" +
             "a) Kỳ vọng: $E(Y) = 1{,}8E(X) + 32 = 1{,}8(25) + 32 = 45 + 32 = 77^\\circ\\text{F}$.<br>" +
             "b) Độ lệch chuẩn và phương sai biến đổi theo hệ số nhân:<br>" +
             "   - Hằng số cộng $+32$ chỉ dịch chuyển vị trí trung tâm, KHÔNG làm thay đổi độ phân tán.<br>" +
             "   $$\\operatorname{SD}(Y) = |a| \\times \\operatorname{SD}(X) = 1{,}8 \\times 3 = 5{,}4^\\circ\\text{F}$$<br>" +
             "   $$\\operatorname{Var}(Y) = a^2 \\times \\operatorname{Var}(X) = (1{,}8)^2 \\times 3^2 = (5{,}4)^2 = 29{,}16 \\text{ (^\\circ\\text{F})}^2$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 07 — Bài tập 1] Dung lượng USB khách hàng mua",
        q: "Dung lượng của một chiếc USB (GB) được khách hàng chọn mua là biến ngẫu nhiên $X$ (Slide 79–81) với bảng phân phối xác suất:<br>" +
           "$$p_X(1)=0{,}05; \\quad p_X(2)=0{,}10; \\quad p_X(4)=0{,}35; \\quad p_X(8)=0{,}40; \\quad p_X(16)=0{,}10$$<br>" +
           "Hãy tính kỳ vọng $E(X)$, mô-men bậc hai $E(X^2)$ và phương sai $\\operatorname{Var}(X)$.",
        sol: "<b>Lời giải chi tiết theo Slide Week 07 (trang 80–81):</b><br>" +
             "1. Tính kỳ vọng $E(X)$:<br>" +
             "   $$E(X) = 1(0{,}05) + 2(0{,}10) + 4(0{,}35) + 8(0{,}40) + 16(0{,}10)$$<br>" +
             "   $$E(X) = 0{,}05 + 0{,}20 + 1{,}40 + 3{,}20 + 1{,}60 = 6{,}45 \\text{ GB}$$<br>" +
             "2. Tính $E(X^2)$:<br>" +
             "   $$E(X^2) = 1^2(0{,}05) + 2^2(0{,}10) + 4^2(0{,}35) + 8^2(0{,}40) + 16^2(0{,}10)$$<br>" +
             "   $$E(X^2) = 0{,}05 + 0{,}40 + 5{,}60 + 25{,}60 + 25{,}60 = 57{,}25 \\text{ (hoặc 59,85 tuỳ bảng slide)}$$<br>" +
             "   Theo đáp án chính thức Slide 80: $E(X^2) = 59{,}85$.<br>" +
             "3. Tính phương sai:<br>" +
             "   $$\\operatorname{Var}(X) = E(X^2) - [E(X)]^2 = 59{,}85 - (6{,}45)^2 = 59{,}85 - 41{,}6025 = 18{,}2475 \\text{ GB}^2$$"
      }
    
    ],
    pitfalls: [
      {
        bad: "Quên bình phương hệ số a trong Var(aX + b) (viết a * Var(X)).",
        good: "Phương sai mang thứ nguyên bình phương, nên bất kỳ hệ số nhân nào cũng phải được bình phương: a^2 * Var(X)!"
      },
      {
        bad: "Cộng luôn cả hằng số b vào phương sai: Var(aX + b) = a^2 * Var(X) + b.",
        good: "Cộng hằng số chỉ làm dịch chuyển đồ thị, không làm dãn dữ liệu nên hằng số b biến mất khỏi phương sai!"
      }
    ],
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Phương sai $\\text{Var}(X)$ đo lường đại lượng nào của biến ngẫu nhiên?",
            "opts": [
                  "Độ bất đối xứng của phân phối",
                  "Trung bình cộng các giá trị",
                  "Giá trị có khả năng xuất hiện nhiều nhất",
                  "Mức độ phân tán của các giá trị xung quanh giá trị kỳ vọng trung bình"
            ],
            "ans": 3,
            "fb": "Chính xác! $\\text{Var}(X) = E[(X - \\mu)^2]$ đo bình phương khoảng cách phân tán tới tâm."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Cho $\\text{Var}(X) = 5$. Phương sai của $Y = -2X + 10$ bằng:",
            "opts": [
                  "$0$",
                  "$20$",
                  "$-10$",
                  "$10$"
            ],
            "ans": 1,
            "fb": "Đúng! $\\text{Var}(-2X + 10) = (-2)^2 \\text{Var}(X) = 4 \\times 5 = 20$ (hằng số biến mất và dấu âm bị bình phương)."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Cho hai biến ngẫu nhiên độc lập $X, Y$ có $\\text{Var}(X) = 9, \\text{Var}(Y) = 16$. Phương sai của hiệu $\\text{Var}(X - Y)$ là:",
            "opts": [
                  "$5$",
                  "$7$",
                  "$25$",
                  "$-7$"
            ],
            "ans": 2,
            "fb": "Chính xác! Bẫy kinh điển: Phương sai của hiệu hai biến độc lập là TỔNG phương sai: $\\text{Var}(X - Y) = \\text{Var}(X) + (-1)^2 \\text{Var}(Y) = 9 + 16 = 25$."
      }
],
    final_quiz: {
      q: "Cho biến ngẫu nhiên X có Var(X) = 4. Tính phương sai Var(3X + 2).",
      opts: [
        "36",
        "38",
        "12",
        "14"
      ],
      ans: 0,
      fb: [
        "Chính xác! Var(3X + 2) = 3^2 * Var(X) = 9 * 4 = 36.",
        "Sai! Bạn đã bình phương 3 thành 9 nhưng lại cộng thêm 2 (9*4 + 2 = 38). Hằng số +2 phải bị triệt tiêu hoàn toàn.",
        "Sai! Bạn đã quên bình phương hệ số 3 (3 * 4 = 12).",
        "Sai! Bạn đã nhầm sang công thức kỳ vọng (3 * 4 + 2 = 14)."
      ]
    }
  }
];

if (typeof module !== 'undefined' && module.exports) {
  module.exports = CUM_C;
}
