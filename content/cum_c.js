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
        q: "Tung 2 đồng xu cân đối. Gọi X là số mặt ngửa xuất hiện. Lập bảng phân phối xác suất (pmf) và tính F(1).",
        sol: "<b>Bước 1:</b> Không gian mẫu $\\Omega = \\{\\text{SS}, \\text{SN}, \\text{NS}, \\text{NN}\\}$. Các giá trị của $X \\in \\{0, 1, 2\\}$.<br>" +
             "- $P(X = 0) = P(\\text{SS}) = 1/4 = 0{,}25$.<br>" +
             "- $P(X = 1) = P(\\{\\text{SN}, \\text{NS}\\}) = 2/4 = 0{,}50$.<br>" +
             "- $P(X = 2) = P(\\text{NN}) = 1/4 = 0{,}25$.<br>" +
             "<b>Bước 2:</b> Bảng pmf:<br>" +
             "<table class='data-table'><tr><th>x</th><td>0</td><td>1</td><td>2</td><td>Tổng</td></tr><tr><th>p(x)</th><td>0,25</td><td>0,50</td><td>0,25</td><td>1,00</td></tr></table><br>" +
             "<b>Bước 3:</b> Tính $F(1) = P(X \\le 1) = P(X = 0) + P(X = 1) = 0{,}25 + 0{,}50 = 0{,}75$."
      },
      {
        level: "Trung bình",
        q: "Biến ngẫu nhiên X nhận các giá trị x ∈ {1, 2, 3, 4} với hàm xác suất p(x) = c · x. Tìm hằng số chuẩn hóa c và tính P(X ≥ 3).",
        sol: "<b>Bước 1:</b> Dùng điều kiện tổng xác suất bằng 1:<br>" +
             "$$\\sum_{x=1}^{4} p(x) = c(1) + c(2) + c(3) + c(4) = c(1 + 2 + 3 + 4) = 10c = 1 \\implies c = \\frac{1}{10} = 0{,}10$$<br>" +
             "<b>Bước 2:</b> Bảng xác suất: $p(1)=0{,}1; p(2)=0{,}2; p(3)=0{,}3; p(4)=0{,}4$.<br>" +
             "<b>Bước 3:</b> $P(X \\ge 3) = p(3) + p(4) = 0{,}3 + 0{,}4 = 0{,}70$."
      },
      {
        level: "Vận dụng",
        q: "Cho hàm tích lũy F(x) của biến ngẫu nhiên X: F(x) = 0 nếu x < 0; F(x) = 0,2 nếu 0 ≤ x < 2; F(x) = 0,7 nếu 2 ≤ x < 5; F(x) = 1 nếu x ≥ 5. Hãy tìm các giá trị mà X có thể nhận và xác suất tương ứng.",
        sol: "<b>Phân tích:</b> Biến ngẫu nhiên $X$ chỉ nhận các giá trị tại các điểm mà hàm $F(x)$ có bước nhảy (gián đoạn):<br>" +
             "- Tại $x = 0$: bước nhảy từ $0$ lên $0{,}2 \\implies P(X = 0) = 0{,}2 - 0 = 0{,}2$.<br>" +
             "- Tại $x = 2$: bước nhảy từ $0{,}2$ lên $0{,}7 \\implies P(X = 2) = 0{,}7 - 0{,}2 = 0{,}5$.<br>" +
             "- Tại $x = 5$: bước nhảy từ $0{,}7$ lên $1{,}0 \\implies P(X = 5) = 1{,}0 - 0{,}7 = 0{,}3$.<br>" +
             "<b>Kết luận:</b> $X$ nhận các giá trị $\\{0, 2, 5\\}$ với xác suất tương ứng là $0{,}2; 0{,}5; 0{,}3$."
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
        q: "Gieo một con xúc xắc cân đối 10 lần độc lập. Tính xác suất để xuất hiện mặt 6 đúng 3 lần.",
        sol: "<b>Bước 1:</b> Nhận diện mô hình: Số lần thử $n = 10$. Thành công là ra mặt 6 $\\implies p = 1/6$. Thất bại $q = 5/6$. Các lần tung độc lập $\\implies X \\sim B(10, 1/6)$.<br>" +
             "<b>Bước 2:</b> Áp dụng công thức với $k = 3$:<br>" +
             "$$P(X = 3) = C_{10}^3 \\cdot \\left(\\frac{1}{6}\\right)^3 \\cdot \\left(\\frac{5}{6}\\right)^7$$<br>" +
             "$$P(X = 3) = 120 \\cdot \\frac{1}{216} \\cdot \\frac{78125}{279936} = 120 \\cdot 0{,}00463 \\cdot 0{,}27908 \\approx 0{,}1550\\text{ (15{,}50\\%)}$$."
      },
      {
        level: "Trung bình",
        q: "Một bài thi trắc nghiệm gồm 20 câu, mỗi câu có 4 phương án (chỉ 1 phương án đúng). Một sinh viên khoanh ngẫu nhiên hoàn toàn cả 20 câu. Tính kỳ vọng và độ lệch chuẩn của số câu sinh viên đó làm đúng.",
        sol: "<b>Bước 1:</b> Nhận diện mô hình: $n = 20, p = 1/4 = 0{,}25 \\implies X \\sim B(20, 0{,}25)$.<br>" +
             "<b>Bước 2:</b> Kỳ vọng số câu đúng:<br>" +
             "$$E(X) = n \\cdot p = 20 \\times 0{,}25 = 5\\text{ (câu)}$$<br>" +
             "<b>Bước 3:</b> Phương sai và độ lệch chuẩn:<br>" +
             "$$\\operatorname{Var}(X) = n p (1 - p) = 20 \\times 0{,}25 \\times 0{,}75 = 3{,}75$$<br>" +
             "$$\\operatorname{SD}(X) = \\sqrt{3{,}75} \\approx 1{,}9365\\text{ (câu)}$$."
      },
      {
        level: "Vận dụng",
        q: "Một dây chuyền sản xuất vi mạch có tỉ lệ lỗi là 5%. Chọn ngẫu nhiên có hoàn lại 100 vi mạch. Tính xác suất để có ít nhất 1 vi mạch bị lỗi.",
        sol: "<b>Bước 1:</b> Gọi $X$ là số vi mạch lỗi trong 100 vi mạch $\\implies X \\sim B(100, 0{,}05)$.<br>" +
             "<b>Bước 2:</b> Yêu cầu tính $P(X \\ge 1)$. Dùng biến cố đối $X = 0$ (không có vi mạch nào lỗi):<br>" +
             "$$P(X = 0) = C_{100}^0 \\cdot (0{,}05)^0 \\cdot (0{,}95)^{100} = 1 \\cdot 1 \\cdot (0{,}95)^{100} \\approx 0{,}00592$$<br>" +
             "<b>Bước 3:</b> Xác suất cần tìm:<br>" +
             "$$P(X \\ge 1) = 1 - P(X = 0) = 1 - 0{,}00592 = 0{,}99408 \\approx 99{,}41\\%$$\\text{."
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
        q: "Một hộp có 20 viên bi, gồm 8 viên màu đỏ và 12 viên màu xanh. Rút ngẫu nhiên không hoàn lại 5 viên. Lập công thức tính xác suất rút được đúng 2 viên đỏ.",
        sol: "<b>Bước 1:</b> Nhận diện: Tổng thể $N = 20$, số bi đỏ $M = 8$, số bi xanh $N - M = 12$, cỡ mẫu $n = 5$, số bi đỏ cần tìm $k = 2$.<br>" +
             "<b>Bước 2:</b> Áp dụng công thức Siêu bội:<br>" +
             "$$P(X = 2) = \\frac{C_8^2 \\cdot C_{12}^3}{C_{20}^5}$$<br>" +
             "<b>Bước 3:</b> Thay số: $C_8^2 = 28$, $C_{12}^3 = 220$, $C_{20}^5 = 15504$:<br>" +
             "$$P(X = 2) = \\frac{28 \\times 220}{15504} = \\frac{6160}{15504} \\approx 0{,}3973\\text{ (39{,}73\\%)}$$."
      },
      {
        level: "Trung bình",
        q: "Tính kỳ vọng và phương sai của số bi đỏ rút được trong ví dụ trên.",
        sol: "<b>Bước 1:</b> Tỉ lệ bi đỏ $p = \\frac{M}{N} = \\frac{8}{20} = 0{,}4$.<br>" +
             "<b>Bước 2:</b> Kỳ vọng: $E(X) = n \\cdot p = 5 \\times 0{,}4 = 2{,}0\\text{ (viên đỏ)}$.<br>" +
             "<b>Bước 3:</b> Phương sai:<br>" +
             "$$\\operatorname{Var}(X) = n p (1 - p) \\cdot \\left(\\frac{N - n}{N - 1}\\right) = 5 \\times 0{,}4 \\times 0{,}6 \\times \\left(\\frac{20 - 5}{20 - 1}\\right) = 1{,}2 \\times \\frac{15}{19} \\approx 0{,}9474$$."
      },
      {
        level: "Vận dụng",
        q: "Một lô hàng 5000 linh kiện chứa 250 linh kiện lỗi. Rút ngẫu nhiên 10 linh kiện để kiểm tra. Hãy giải thích vì sao trong trường hợp này ta có thể dùng mô hình Nhị thức thay cho Siêu bội.",
        sol: "<b>Phân tích:</b><br>" +
             "- Tổng thể $N = 5000$, cỡ mẫu $n = 10$.<br>" +
             "- Tỉ lệ lấy mẫu: $\\frac{n}{N} = \\frac{10}{5000} = 0{,}002 = 0{,}2\\% &lt; 5\\%$.<br>" +
             "- Hệ số hiệu chỉnh: $\\frac{5000 - 10}{5000 - 1} = \\frac{4990}{4999} \\approx 0{,}9982 \\approx 1$.<br>" +
             "<b>Kết luận:</b> Vì tổng thể cực lớn và cỡ mẫu rất nhỏ, việc rút một vài linh kiện hầu như không ảnh hưởng đến tỉ lệ lỗi $p = 250/5000 = 0{,}05$. Do đó, xấp xỉ Nhị thức $B(10, 0{,}05)$ cho kết quả chính xác cao mà tính toán nhanh hơn rất nhiều."
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
        q: "Số cuộc gọi đến một tổng đài khẩn cấp trung bình là 4 cuộc/giờ và tuân theo phân phối Poisson. Tính xác suất trong 1 giờ tổng đài nhận được đúng 2 cuộc gọi.",
        sol: "<b>Bước 1:</b> Tham số trung bình $\\lambda = 4$.<br>" +
             "<b>Bước 2:</b> Áp dụng công thức với $k = 2$:<br>" +
             "$$P(X = 2) = \\frac{4^2 \\cdot e^{-4}}{2!} = \\frac{16 \\cdot e^{-4}}{2} = 8 \\cdot e^{-4} \\approx 8 \\times 0{,}018316 \\approx 0{,}1465\\text{ (14{,}65\\%)}$$."
      },
      {
        level: "Trung bình",
        q: "Cũng tổng đài trên (λ = 4 cuộc/giờ). Tính xác suất trong 1 giờ tổng đài nhận được ít nhất 1 cuộc gọi.",
        sol: "<b>Bước 1:</b> Yêu cầu $P(X \\ge 1)$. Dùng biến cố đối $X = 0$ (không có cuộc gọi nào):<br>" +
             "$$P(X = 0) = \\frac{4^0 \\cdot e^{-4}}{0!} = \\frac{1 \\cdot e^{-4}}{1} = e^{-4} \\approx 0{,}0183$$<br>" +
             "<b>Bước 2:</b> Xác suất cần tìm:<br>" +
             "$$P(X \\ge 1) = 1 - P(X = 0) = 1 - e^{-4} = 1 - 0{,}0183 = 0{,}9817\\text{ (98{,}17\\%)}$$."
      },
      {
        level: "Vận dụng",
        q: "Một công ty bảo hiểm bán 1000 hợp đồng cho 1000 người độc lập. Xác suất một người tử vong trong năm là p = 0,002. Hãy dùng phân phối Poisson xấp xỉ xác suất có đúng 3 người tử vong trong năm.",
        sol: "<b>Phân tích:</b> Đây là Nhị thức $B(n = 1000, p = 0{,}002)$ với $n$ rất lớn và $p$ rất nhỏ.<br>" +
             "- Tham số Poisson: $\\lambda = n \\cdot p = 1000 \\times 0{,}002 = 2{,}0$.<br>" +
             "- Áp dụng công thức Poisson với $k = 3$:<br>" +
             "$$P(X = 3) \\approx \\frac{2^3 \\cdot e^{-2}}{3!} = \\frac{8 \\cdot e^{-2}}{6} = \\frac{4}{3} \\cdot e^{-2} \\approx 1{,}3333 \\times 0{,}135335 \\approx 0{,}1804\\text{ (18{,}04\\%)}$$."
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
        q: "Biến ngẫu nhiên X nhận các giá trị 0, 1, 2 với xác suất tương ứng là 0,2; 0,5; 0,3. Hãy tính kỳ vọng E(X).",
        sol: "<b>Áp dụng công thức định nghĩa:</b><br>" +
             "$$E(X) = \\sum x \\cdot p(x) = 0(0{,}2) + 1(0{,}5) + 2(0{,}3) = 0 + 0{,}5 + 0{,}6 = 1{,}1$$."
      },
      {
        level: "Trung bình",
        q: "Cho biến ngẫu nhiên X có E(X) = 4. Hãy tính kỳ vọng của biến ngẫu nhiên Y = 3X + 2.",
        sol: "<b>Áp dụng tính chất tuyến tính:</b><br>" +
             "$$E(Y) = E(3X + 2) = 3 \\cdot E(X) + 2 = 3(4) + 2 = 12 + 2 = 14$$."
      },
      {
        level: "Vận dụng",
        q: "Một cơ sở kiểm tra hai sản phẩm độc lập. Mỗi sản phẩm đạt chuẩn với xác suất 0,8. Gọi X là số sản phẩm đạt chuẩn. Chi phí xử lý lô hàng là C = 50 + 20X (nghìn đồng). Tính chi phí xử lý kỳ vọng E(C).",
        sol: "<b>Bước 1:</b> Tính kỳ vọng của $X$: Vì kiểm tra 2 sản phẩm độc lập cùng xác suất $0{,}8 \\implies X \\sim B(2, 0{,}8)$.<br>" +
             "$$E(X) = n \\cdot p = 2 \\times 0{,}8 = 1{,}6\\text{ (sản phẩm đạt)}$$<br>" +
             "<b>Bước 2:</b> Tính chi phí kỳ vọng:<br>" +
             "$$E(C) = E(50 + 20X) = 50 + 20 \\cdot E(X) = 50 + 20(1{,}6) = 50 + 32 = 82\\text{ (nghìn đồng)}$$."
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
        q: "Biến ngẫu nhiên X nhận 0, 1, 2 với xác suất 0,2; 0,5; 0,3 (đã biết E(X) = 1,1). Hãy tính E(X²) và Var(X).",
        sol: "<b>Bước 1:</b> Tính $E(X^2) = 0^2(0{,}2) + 1^2(0{,}5) + 2^2(0{,}3) = 0 + 0{,}5 + 4(0{,}3) = 0{,}5 + 1{,}2 = 1{,}7$.<br>" +
             "<b>Bước 2:</b> Áp dụng công thức rút gọn:<br>" +
             "$$\\operatorname{Var}(X) = E(X^2) - [E(X)]^2 = 1{,}7 - (1{,}1)^2 = 1{,}7 - 1{,}21 = 0{,}49$$."
      },
      {
        level: "Trung bình",
        q: "Cho biến ngẫu nhiên X có phương sai Var(X) = 4. Hãy tính Var(3X + 2).",
        sol: "<b>Áp dụng tính chất biến đổi tuyến tính:</b><br>" +
             "$$\\operatorname{Var}(3X + 2) = 3^2 \\cdot \\operatorname{Var}(X) = 9 \\cdot 4 = 36$$.<br>" +
             "<i>Lưu ý: Hằng số +2 bị triệt tiêu hoàn toàn vì cộng hằng số không làm thay đổi độ phân tán!</i>"
      },
      {
        level: "Vận dụng",
        q: "Dung lượng USB bán ra tại một cửa hàng có phân phối: 1 GB (0,05), 2 GB (0,10), 4 GB (0,35), 8 GB (0,40), 16 GB (0,10). Tính độ lệch chuẩn SD(X) kèm đúng thứ nguyên đơn vị.",
        sol: "<b>Bước 1:</b> Tính $E(X) = 1(0{,}05) + 2(0{,}10) + 4(0{,}35) + 8(0{,}40) + 16(0{,}10) = 6{,}45\\text{ GB}$.<br>" +
             "<b>Bước 2:</b> Tính $E(X^2) = 1(0{,}05) + 4(0{,}10) + 16(0{,}35) + 64(0{,}40) + 256(0{,}10) = 57{,}25\\text{ GB}^2$.<br>" +
             "<b>Bước 3:</b> $\\operatorname{Var}(X) = 57{,}25 - 6{,}45^2 = 57{,}25 - 41{,}6025 = 15{,}6475\\text{ GB}^2$.<br>" +
             "<b>Bước 4:</b> $\\operatorname{SD}(X) = \\sqrt{15{,}6475} \\approx 3{,}9557\\text{ GB}$."
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
