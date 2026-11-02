// ==========================================================================
// CỤM B: LÝ THUYẾT XÁC SUẤT
// Bao gồm: Bài B1, B2, B3, B4, B5
// Nguồn: Slide UET Week 05 (tr. 1–93), Stat20 Chương 3, OpenIntro Statistics Ch.3
// Kiểm chứng số học: verify/verify_cum_b.py
// ==========================================================================

const CUM_B = [
  {
    id: "B1",
    cluster: "B",
    title: "Không gian mẫu, Biến cố & 3 Tiên đề Kolmogorov",
    sources: "Slide Week 05 (tr. 1–30); Stat20 Mục 3.1",
    desc: "Xây dựng nền móng giải tích xác suất: Không gian mẫu, biến cố, và 3 tiên đề Kolmogorov đảm bảo tính nhất quán của toán học xác suất.",
    steps: [
      {
        t: "Phép thử ngẫu nhiên & Không gian mẫu $\\Omega$",
        c: `<p>Trong lý thuyết xác suất, mọi tính toán đều xuất phát từ một <b>Phép thử ngẫu nhiên (Random Experiment)</b> — hành động mà ta không thể biết trước kết quả chính xác, nhưng biết trước toàn bộ các kết quả có thể xảy ra:</p>
            <ul>
              <li><b>Không gian mẫu (Sample Space, ký hiệu $\\Omega$ hoặc $S$)</b>: Tập hợp chứa TẤT CẢ các kết quả có thể xảy ra của phép thử.</li>
              <li><b>Kết quả sơ cấp (Outcome, $\\omega$)</b>: Một phần tử đơn lẻ thuộc $\\Omega$ ($\\,\\omega \\in \\Omega$).</li>
            </ul>
            <div class="tip-box">
              <b>Ví dụ kinh điển:</b><br>
              - Tung một đồng xu: $\\Omega = \\{\\text{Ngửa (N)}, \\text{Sấp (S)}\\}$.<br>
              - Gieo một con xúc xắc 6 mặt: $\\Omega = \\{1, 2, 3, 4, 5, 6\\}$.<br>
              - Tung 2 đồng xu: $\\Omega = \\{\\text{NN}, \\text{NS}, \\text{SN}, \\text{SS}\\}$.
            </div>`
      },
      {
        t: "Biến cố (Event) là gì?",
        c: `<p><b>Biến cố (Event, ký hiệu $A, B, C$)</b> là một tập con bất kỳ của không gian mẫu ($A \\subseteq \\Omega$).</p>
            <ul>
              <li>Ta nói biến cố $A$ <b>xảy ra</b> nếu kết quả thực tế của phép thử rơi vào tập $A$.</li>
              <li><b>Biến cố chắc chắn (Certain event)</b>: Chính là toàn bộ không gian mẫu $\\Omega$. Luôn luôn xảy ra.</li>
              <li><b>Biến cố không thể (Impossible event)</b>: Là tập rỗng $\\emptyset$. Không bao giờ xảy ra.</li>
            </ul>
            <p><b>Ví dụ:</b> Gieo xúc xắc $\\Omega = \\{1, 2, 3, 4, 5, 6\\}$. Gọi $A$ là biến cố 'ra mặt chẵn' $\\implies A = \\{2, 4, 6\\}$.</p>`
      },
      {
        t: "Ba tiên đề xác suất của Kolmogorov (Axioms of Probability)",
        c: `<p>Năm 1933, nhà toán học vĩ đại Andrey Kolmogorov đã đặt nền móng cho xác suất hiện đại bằng 3 tiên đề duy nhất:</p>
            <ol>
              <li><b>Tiên đề 1 (Tính không âm)</b>: Xác suất của mọi biến cố $A$ luôn là số không âm:
                  $$P(A) \\ge 0$$
              </li>
              <li><b>Tiên đề 2 (Chuẩn hóa)</b>: Xác suất của toàn bộ không gian mẫu luôn bằng 1:
                  $$P(\\Omega) = 1$$
              </li>
              <li><b>Tiên đề 3 (Tính cộng vô hạn)</b>: Nếu các biến cố $A_1, A_2, \\dots$ xung khắc từng đôi một ($A_i \\cap A_j = \\emptyset$ với mọi $i \\neq j$), thì:
                  $$P(A_1 \\cup A_2 \\cup \\dots) = P(A_1) + P(A_2) + \\dots$$
              </li>
            </ol>
            <div class="tip-box">
              <b>Trực giác hình học:</b> Hãy tưởng tượng không gian mẫu $\\Omega$ là một thửa đất có diện tích chuẩn bằng $1$. Xác suất $P(A)$ chính là diện tích phần đất thuộc về biến cố $A$. Vì là diện tích, nó không thể âm ($P \\ge 0$), toàn bộ thửa đất bằng $1$, và ghép các mảnh đất không chồng lấn lên nhau thì diện tích bằng tổng diện tích từng mảnh!
            </div>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        q: "Tung một con xúc xắc cân đối. Hãy xác định không gian mẫu $\\Omega$, biến cố $A$ là 'xuất hiện số nguyên tố', và tính $P(A)$.",
        sol: "<b>Bước 1:</b> Không gian mẫu gồm 6 mặt: $\\Omega = \\{1, 2, 3, 4, 5, 6\\}$.<br>" +
             "<b>Bước 2:</b> Các số nguyên tố trong $\\Omega$ là $2, 3, 5$. Do đó $A = \\{2, 3, 5\\}$.<br>" +
             "<b>Bước 3:</b> Vì xúc xắc cân đối, mỗi mặt có xác suất $1/6$. Theo tiên đề 3:<br>" +
             "$$P(A) = P(\\{2\\}) + P(\\{3\\}) + P(\\{5\\}) = \\frac{1}{6} + \\frac{1}{6} + \\frac{1}{6} = \\frac{3}{6} = 0{,}5$$."
      },
      {
        level: "Trung bình",
        q: "Tung đồng thời hai đồng xu cân đối. Tìm xác suất để xuất hiện 'ít nhất một mặt ngửa'.",
        sol: "<b>Bước 1:</b> Không gian mẫu $\\Omega = \\{\\text{NN}, \\text{NS}, \\text{SN}, \\text{SS}\\}$, gồm 4 phần tử đồng khả năng, mỗi phần tử có xác suất $1/4$.<br>" +
             "<b>Bước 2:</b> Gọi $A$ là biến cố 'ít nhất một mặt ngửa': $A = \\{\\text{NN}, \\text{NS}, \\text{SN}\\}$.<br>" +
             "<b>Bước 3:</b> $P(A) = \\frac{3}{4} = 0{,}75$."
      },
      {
        level: "Vận dụng",
        q: "Từ 3 tiên đề Kolmogorov, hãy chứng minh một cách chặt chẽ rằng xác suất của biến cố không thể bằng 0: $P(\\emptyset) = 0$, và với mọi biến cố $A$ luôn có $0 \\le P(A) \\le 1$.",
        sol: "<b>Chứng minh $P(\\emptyset) = 0$:</b><br>" +
             "- Ta có $\\Omega = \\Omega \\cup \\emptyset$. Vì $\\Omega \\cap \\emptyset = \\emptyset$ (xung khắc), theo Tiên đề 3:<br>" +
             "$$P(\\Omega) = P(\\Omega) + P(\\emptyset)$$<br>" +
             "- Thay $P(\\Omega) = 1$ (Tiên đề 2) vào: $1 = 1 + P(\\emptyset) \\implies P(\\emptyset) = 0$.<br>" +
             "<b>Chứng minh $P(A) \\le 1$:</b><br>" +
             "- Ta có $\\Omega = A \\cup A^c$ với $A \\cap A^c = \\emptyset$.<br>" +
             "- Theo Tiên đề 3: $P(\\Omega) = P(A) + P(A^c) \\implies 1 = P(A) + P(A^c)$.<br>" +
             "- Vì $P(A^c) \\ge 0$ (Tiên đề 1), suy ra $P(A) = 1 - P(A^c) \\le 1$. Kết hợp Tiên đề 1 $\\implies 0 \\le P(A) \\le 1$."
      }
    ],
    pitfalls: [
      {
        bad: "Tính ra xác suất lớn hơn 1 hoặc nhỏ hơn 0 rồi cứ thế viết vào bài thi.",
        good: "Xác suất là một thước đo chuẩn hóa chặt chẽ trên đoạn [0, 1]. Nếu tính ra P = 1,2 hay P = -0,3 thì 100% bạn đã áp dụng sai công thức, hãy dừng lại kiểm tra ngay!"
      },
      {
        bad: "Cộng xác suất của hai biến cố bất kỳ mà không kiểm tra xem chúng có xung khắc hay không.",
        good: "Tiên đề cộng $P(A \\cup B) = P(A) + P(B)$ CHỈ ĐƯỢC PHÉP DÙNG khi $A$ và $B$ không có phần tử chung ($A \\cap B = \\emptyset$)!"
      }
    ],
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Tiên đề xác suất nào sau đây thuộc 3 tiên đề nền tảng của Kolmogorov?",
            "opts": [
                  "$P(A \\cap B) = P(A)P(B)$ với mọi biến cố",
                  "$0 \\le P(A) \\le 1$ với mọi biến cố $A$ và $P(S) = 1$",
                  "$P(A) = 0 \\iff A = \\emptyset$",
                  "$P(A \\cup B) = P(A) + P(B)$ với mọi cặp biến cố bất kỳ"
            ],
            "ans": 1,
            "fb": "Chính xác! 3 tiên đề Kolmogorov gồm: Tính không âm ($P(A) \\ge 0$), Tính chuẩn hóa ($P(S) = 1$), và Tính cộng vô hạn cho các biến cố xung khắc."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Tung đồng thời hai con xúc xắc cân đối 6 mặt. Số phần tử của không gian mẫu $S$ là:",
            "opts": [
                  "$36$",
                  "$12$",
                  "$24$",
                  "$6$"
            ],
            "ans": 0,
            "fb": "Đúng! Theo quy tắc nhân, mỗi con xúc xắc có 6 kết quả $\\implies |S| = 6 \\times 6 = 36$ kết quả đồng khả năng."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Một biến cố $A$ có xác suất $P(A) = 0$. Khẳng định nào sau đây là chính xác nhất trong giải tích xác suất hiện đại?",
            "opts": [
                  "Biến cố đối $\\bar{A}$ có xác suất bằng 0",
                  "$A$ độc lập với chính nó nhưng không độc lập với không gian mẫu",
                  "$A$ là biến cố không thể xảy ra (đối với không gian rời rạc hữu hạn), nhưng trong không gian liên tục $A$ vẫn có thể xảy ra",
                  "$A$ bắt buộc phải là tập rỗng $A = \\emptyset$"
            ],
            "ans": 2,
            "fb": "Chính xác! Trong không gian xác suất liên tục (như chọn một số thực ngẫu nhiên trên $[0, 1]$), xác suất chọn trúng điểm $0{,}5$ là $0$, nhưng điểm này hoàn toàn thuộc không gian mẫu."
      }
],
    final_quiz: {
      q: "Điều kiện bắt buộc để áp dụng tiên đề cộng $P(A \\cup B) = P(A) + P(B)$ là gì?",
      opts: [
        "A và B là hai biến cố xung khắc (A ∩ B = ∅)",
        "A và B là hai biến cố độc lập (P(A ∩ B) = P(A)P(B))",
        "A và B phải có cùng xác suất P(A) = P(B)",
        "A và B phải cùng là tập con của không gian mẫu"
      ],
      ans: 0,
      fb: [
        "Chính xác! Tiên đề 3 Kolmogorov chỉ áp dụng khi hai biến cố xung khắc nhau từng đôi một (không có phần tử chung).",
        "Sai! Bạn đã mắc bẫy chí mạng giữa 'độc lập' và 'xung khắc'. Khi độc lập, P(A ∪ B) = P(A) + P(B) - P(A)P(B), không thể cộng đơn thuần được.",
        "Sai! Không cần hai biến cố có cùng xác suất.",
        "Sai! Mọi biến cố đều là tập con của không gian mẫu, nhưng nếu giao nhau thì sẽ bị đếm trùng phần giao."
      ]
    }
  },

  {
    id: "B2",
    cluster: "B",
    title: "Quy tắc cộng, Biến cố đối & Nguyên lý bao hàm - loại trừ",
    sources: "Slide Week 05 (tr. 31–50); Stat20 Mục 3.1, 3.3.9",
    desc: "Làm chủ quy tắc cộng xác suất tổng quát cho hai biến cố bất kỳ, kỹ thuật biến cố đối (vũ khí tối thượng cho dạng 'ít nhất một') và biểu đồ Venn.",
    steps: [
      {
        t: "Biến cố đối (Complement) & Quy tắc bù trừ",
        c: `<p>Cho biến cố $A$. <b>Biến cố đối</b> (ký hiệu là $A^c$ hoặc $\\bar{A}$) là biến cố <i>'Biến cố $A$ không xảy ra'</i>:</p>
            $$P(A^c) = 1 - P(A)$$
            <div class="tip-box">
              <b>Vũ khí tối thượng: Từ khóa &quot;Ít nhất một&quot; (At least one)</b><br>
              Khi đề bài yêu cầu tính xác suất để có <i>'ít nhất 1 lần thành công'</i> trong $n$ lần thử, cách tính trực tiếp (1 lần, 2 lần,..., n lần) cực kỳ dài dòng và dễ sót. Hãy dùng biến cố đối:<br>
              $$\\text{Biến cố đối của 'Ít nhất 1'} \\equiv \\text{'Không có lần nào' (None)}$$
              $$P(\\text{Ít nhất 1}) = 1 - P(\\text{Không có lần nào})$$
            </div>`
      },
      {
        t: "Quy tắc cộng tổng quát (Nguyên lý Bao hàm - Loại trừ)",
        c: `<p>Nếu hai biến cố $A$ và $B$ <b>không xung khắc</b> (tức là có thể đồng thời xảy ra, $A \\cap B \\neq \\emptyset$):</p>
            $$P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$$
            <p><b>Vì sao phải trừ đi $P(A \\cap B)$?</b></p>
            <p>Khi bạn cộng $P(A)$ và $P(B)$, phần diện tích giao nhau $A \\cap B$ đã nằm trong cả hai tập hợp, tức là nó bị <b>đếm trùng hai lần</b>! Ta buộc phải trừ bớt một lần để kết quả phản ánh đúng diện tích hợp của hai biến cố.</p>
            <div class="tip-box">
              <b>Biểu đồ Venn:</b> Hình dung $A$ là hình tròn bên trái, $B$ là hình tròn bên phải. Phần chung ở giữa là $A \\cap B$. Phép tính $P(A) + P(B) - P(A \\cap B)$ quét trọn vẹn toàn bộ vùng phủ sóng của cả hai hình tròn mà không bị đếm đúp.
            </div>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        q: "Gieo một con xúc xắc cân đối. Gọi A là biến cố 'ra số chẵn', B là biến cố 'ra số lớn hơn hoặc bằng 4'. Tính xác suất P(A ∪ B).",
        sol: "<b>Bước 1:</b> Liệt kê các phần tử:<br>" +
             "- $\\Omega = \\{1, 2, 3, 4, 5, 6\\}$<br>" +
             "- $A = \\{2, 4, 6\\} \\implies P(A) = 3/6$<br>" +
             "- $B = \\{4, 5, 6\\} \\implies P(B) = 3/6$<br>" +
             "- Phần giao: $A \\cap B = \\{4, 6\\} \\implies P(A \\cap B) = 2/6$<br>" +
             "<b>Bước 2:</b> Áp dụng quy tắc cộng tổng quát:<br>" +
             "$$P(A \\cup B) = P(A) + P(B) - P(A \\cap B) = \\frac{3}{6} + \\frac{3}{6} - \\frac{2}{6} = \\frac{4}{6} = \\frac{2}{3} \\approx 0{,}6667$$."
      },
      {
        level: "Trung bình",
        q: "Tung 4 đồng xu cân đối độc lập. Tính xác suất để có ít nhất một mặt ngửa xuất hiện.",
        sol: "<b>Bước 1:</b> Gọi $A$ là biến cố 'có ít nhất một mặt ngửa'.<br>" +
             "<b>Bước 2:</b> Xét biến cố đối $A^c$: 'không có mặt ngửa nào' (tức là cả 4 lần đều ra mặt Sấp: SSSS).<br>" +
             "<b>Bước 3:</b> Vì mỗi lần tung độc lập, xác suất ra sấp là $1/2$:<br>" +
             "$$P(A^c) = P(\\text{SSSS}) = \\left(\\frac{1}{2}\\right)^4 = \\frac{1}{16}$$<br>" +
             "<b>Bước 4:</b> Áp dụng quy tắc bù trừ:<br>" +
             "$$P(A) = 1 - P(A^c) = 1 - \\frac{1}{16} = \\frac{15}{16} = 0{,}9375\\text{ (hay } 93{,}75\\%\\text{)}$$."
      },
      {
        level: "Vận dụng",
        q: "Một lớp sinh viên có 60% thích môn Toán, 50% thích môn Lập trình và 30% thích cả hai môn. Chọn ngẫu nhiên một sinh viên. Tính xác suất sinh viên đó không thích môn nào trong hai môn trên.",
        sol: "<b>Bước 1:</b> Gọi $T$ là thích Toán ($P(T) = 0{,}6$), $L$ là thích Lập trình ($P(L) = 0{,}5$). Phần giao $P(T \\cap L) = 0{,}3$.<br>" +
             "<b>Bước 2:</b> Xác suất sinh viên thích ít nhất một môn ($T \\cup L$):<br>" +
             "$$P(T \\cup L) = P(T) + P(L) - P(T \\cap L) = 0{,}6 + 0{,}5 - 0{,}3 = 0{,}8\\text{ (80\\%)}$$<br>" +
             "<b>Bước 3:</b> Biến cố 'không thích môn nào' chính là đối lập của 'thích ít nhất một môn':<br>" +
             "$$P(\\text{Không thích môn nào}) = 1 - P(T \\cup L) = 1 - 0{,}8 = 0{,}2\\text{ (20\\%)}$$."
      }
    ],
    pitfalls: [
      {
        bad: "Tính P(A ∪ B) bằng cách lấy P(A) + P(B) = 0,6 + 0,5 = 1,1 (lớn hơn 1).",
        good: "Khi hai biến cố có thể cùng xảy ra, bắt buộc phải trừ đi phần giao P(A ∩ B). Không có xác suất nào được phép vượt quá 1!"
      },
      {
        bad: "Nhầm lẫn giữa biến cố đối của 'tất cả đều đạt' là 'tất cả đều trượt'.",
        good: "Biến cố đối của 'Tất cả đều đạt' là 'Có ít nhất một người không đạt' (chứ không phải tất cả đều trượt)!"
      }
    ],
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Công thức cộng xác suất cho hai biến cố $A$ và $B$ bất kỳ là:",
            "opts": [
                  "$P(A \\cup B) = P(A) + P(B) + P(A \\cap B)$",
                  "$P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$",
                  "$P(A \\cup B) = P(A) P(B)$",
                  "$P(A \\cup B) = P(A) + P(B)$"
            ],
            "ans": 1,
            "fb": "Chính xác! Phần giao $A \\cap B$ được tính hai lần (trong $P(A)$ và trong $P(B)$) nên phải trừ đi 1 lần."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Cho $P(A) = 0{,}6$, $P(B) = 0{,}7$ và $P(A \\cap B) = 0{,}4$. Xác suất để ít nhất một trong hai biến cố xảy ra là:",
            "opts": [
                  "$0{,}30$",
                  "$1{,}30$",
                  "$0{,}42$",
                  "$0{,}90$"
            ],
            "ans": 3,
            "fb": "Đúng! $P(A \\cup B) = 0{,}6 + 0{,}7 - 0{,}4 = 0{,}90$."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Cho hai biến cố $A$ và $B$ có $P(A) = 0{,}7$ và $P(B) = 0{,}8$. Bất đẳng thức Bonferroni khẳng định xác suất đồng thời $P(A \\cap B)$ phải thỏa mãn:",
            "opts": [
                  "$P(A \\cap B) = 0{,}56$",
                  "$P(A \\cap B) \\ge 0{,}50$",
                  "$P(A \\cap B) \\le 0{,}50$",
                  "$P(A \\cap B) \\ge 0{,}70$"
            ],
            "ans": 1,
            "fb": "Chính xác! Vì $P(A \\cup B) \\le 1 \\implies P(A \\cap B) = P(A) + P(B) - P(A \\cup B) \\ge 0{,}7 + 0{,}8 - 1 = 0{,}50$."
      }
],
    final_quiz: {
      q: "Cho hai biến cố A và B có P(A) = 0,5; P(B) = 0,4 và P(A ∩ B) = 0,2. Xác suất P(A ∪ B) bằng bao nhiêu?",
      opts: [
        "0,7",
        "0,9",
        "0,1",
        "0,3"
      ],
      ans: 0,
      fb: [
        "Chính xác! P(A ∪ B) = P(A) + P(B) - P(A ∩ B) = 0,5 + 0,4 - 0,2 = 0,7. Phải trừ đi 0,2 để phần giao không bị đếm đúp.",
        "Sai! Bạn đã lấy 0,5 + 0,4 = 0,9 và quên trừ đi phần giao P(A ∩ B).",
        "Sai! 0,1 là kết quả tính toán sai lệch.",
        "Sai! 0,3 là xác suất của A mà không có B (P(A \\ B) = 0,5 - 0,2 = 0,3)."
      ]
    }
  },

  {
    id: "B3",
    cluster: "B",
    title: "Xác suất có điều kiện & Quy tắc nhân",
    sources: "Slide Week 05 (tr. 51–68); Stat20 Mục 3.3.3, 3.3.4",
    desc: "Khái niệm then chốt của xác suất: Cập nhật xác suất khi có thêm thông tin. Công thức Bayes nền tảng và quy tắc nhân cho các phép thử liên tiếp không hoàn lại.",
    steps: [
      {
        t: "Xác suất có điều kiện $P(A \\mid B)$ là gì?",
        c: `<p><b>Xác suất có điều kiện $P(A \\mid B)$</b> (đọc là: <i>xác suất của $A$ biết rằng $B$ đã xảy ra</i>) đo lường khả năng xảy ra của $A$ khi ta đã có thêm thông tin chắc chắn rằng $B$ đã xuất hiện:</p>
            $$P(A \\mid B) = \\frac{P(A \\cap B)}{P(B)} \\quad (\\text{với } P(B) &gt; 0)$$
            <div class="tip-box">
              <b>Trực giác 'Thu hẹp vũ trụ':</b><br>
              Ban đầu, không gian mẫu của bạn là toàn bộ $\\Omega$. Nhưng ngay khi bạn biết rằng $B$ đã xảy ra, <b>toàn bộ vũ trụ của bạn thu nhỏ lại chỉ còn đúng tập $B$</b>! Các kết quả nằm ngoài $B$ không còn khả năng xảy ra nữa. Lúc này, phần duy nhất của $A$ còn tồn tại là phần nằm lọt trong $B$ (tức là $A \\cap B$). Do đó, ta lấy diện tích $A \\cap B$ chia cho diện tích vũ trụ mới $P(B)$.
            </div>`
      },
      {
        t: "Quy tắc nhân xác suất (Multiplication Rule)",
        c: `<p>Từ định nghĩa xác suất có điều kiện, nhân chéo mẫu số ta thu được <b>Quy tắc nhân</b> dùng để tính xác suất của một giao (hai biến cố cùng xảy ra):</p>
            $$P(A \\cap B) = P(B) \\cdot P(A \\mid B) = P(A) \\cdot P(B \\mid A)$$
            <p><b>Mở rộng cho 3 biến cố (Quy tắc chuỗi / Chain Rule):</b></p>
            $$P(A \\cap B \\cap C) = P(A) \\cdot P(B \\mid A) \\cdot P(C \\mid A \\cap B)$$
            <div class="tip-box">
              <b>Ứng dụng thực tế: Rút thăm không hoàn lại!</b><br>
              Khi bạn rút các phần tử từ một hộp mà không hoàn lại, mỗi lần rút sẽ làm thay đổi thành phần trong hộp ở lần rút tiếp theo. Quy tắc nhân chính là công cụ để giải quyết bài toán này từng bước một.
            </div>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        q: "Biết P(A ∩ B) = 0,2 và P(B) = 0,4. Hãy tính xác suất có điều kiện P(A | B).",
        sol: "<b>Áp dụng công thức:</b><br>" +
             "$$P(A \\mid B) = \\frac{P(A \\cap B)}{P(B)} = \\frac{0{,}2}{0{,}4} = 0{,}5$$."
      },
      {
        level: "Trung bình",
        q: "Một hộp có 5 thẻ bài, trong đó có 2 thẻ màu đỏ và 3 thẻ màu đen. Rút ngẫu nhiên lần lượt 2 thẻ không hoàn lại. Tính xác suất để cả hai thẻ rút ra đều là màu đỏ.",
        sol: "<b>Bước 1:</b> Gọi $R_1$ là lần 1 rút được thẻ đỏ, $R_2$ là lần 2 rút được thẻ đỏ.<br>" +
             "<b>Bước 2:</b> Ở lần rút thứ nhất, có 2 thẻ đỏ trong 5 thẻ: $P(R_1) = 2/5 = 0{,}4$.<br>" +
             "<b>Bước 3:</b> Sau khi đã rút 1 thẻ đỏ (không hoàn lại), trong hộp chỉ còn lại 4 thẻ, trong đó có đúng 1 thẻ đỏ: $P(R_2 \\mid R_1) = 1/4 = 0{,}25$.<br>" +
             "<b>Bước 4:</b> Áp dụng quy tắc nhân:<br>" +
             "$$P(R_1 \\cap R_2) = P(R_1) \\cdot P(R_2 \\mid R_1) = \\frac{2}{5} \\times \\frac{1}{4} = \\frac{2}{20} = 0{,}10\\text{ (10\\%)}$$."
      },
      {
        level: "Vận dụng",
        q: "Trong kho có 10 chiếc máy tính xách tay, trong đó có 3 chiếc bị lỗi phần cứng. Một kỹ sư kiểm tra ngẫu nhiên lần lượt 3 chiếc không hoàn lại. Tính xác suất để cả 3 chiếc đều hoạt động tốt.",
        sol: "<b>Bước 1:</b> Tổng số máy = 10, máy tốt = 7, máy lỗi = 3.<br>" +
             "<b>Bước 2:</b> Gọi $T_1, T_2, T_3$ lần lượt là chiếc thứ 1, 2, 3 hoạt động tốt.<br>" +
             "<b>Bước 3:</b> Áp dụng quy tắc chuỗi:<br>" +
             "- Lần 1: $P(T_1) = \\frac{7}{10}$ (còn lại 9 máy, 6 máy tốt).<br>" +
             "- Lần 2: $P(T_2 \\mid T_1) = \\frac{6}{9}$ (còn lại 8 máy, 5 máy tốt).<br>" +
             "- Lần 3: $P(T_3 \\mid T_1 \\cap T_2) = \\frac{5}{8}$.<br>" +
             "<b>Bước 4:</b> Nhân xác suất:<br>" +
             "$$P(T_1 \\cap T_2 \\cap T_3) = \\frac{7}{10} \\times \\frac{6}{9} \\times \\frac{5}{8} = \\frac{210}{720} = \\frac{7}{24} \\approx 0{,}2917\\text{ (29{,}17\\%)}$$."
      }
    ],
    pitfalls: [
      {
        bad: "Nhầm lẫn thứ tự điều kiện: tưởng rằng P(A | B) và P(B | A) là bằng nhau.",
        good: "P(A | B) và P(B | A) HOÀN TOÀN KHÁC NHAU vì mẫu số khác nhau! Ví dụ: P(Mang thai | Giới tính nữ) rất khác với P(Giới tính nữ | Mang thai) = 1."
      },
      {
        bad: "Quên giảm mẫu số khi lấy mẫu không hoàn lại (vẫn chia cho 5 ở lần rút thứ hai).",
        good: "Đã rút không hoàn lại thì mỗi bước số phần tử trong hộp phải giảm đi 1: từ 5 xuống 4, rồi xuống 3!"
      }
    ],
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Công thức định nghĩa xác suất có điều kiện $P(A \\mid B)$ là:",
            "opts": [
                  "$P(A \\mid B) = \\frac{P(A \\cap B)}{P(B)}$ với điều kiện $P(B) > 0$",
                  "$P(A \\mid B) = \\frac{P(B \\mid A)}{P(B)}$",
                  "$P(A \\mid B) = \\frac{P(A)}{P(B)}$",
                  "$P(A \\mid B) = P(A) P(B)$"
            ],
            "ans": 0,
            "fb": "Chính xác! Xác suất của $A$ khi biết $B$ đã xảy ra thu hẹp không gian mẫu về tập $B$."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Một hộp có 5 bi trắng và 3 bi đen. Rút lần lượt 2 viên bi không hoàn lại. Xác suất viên thứ nhất trắng VÀ viên thứ hai đen là:",
            "opts": [
                  "$\\frac{3}{8}$",
                  "$\\frac{5}{8} \\times \\frac{3}{8} = \\frac{15}{64} \\approx 0{,}2344$",
                  "$\\frac{5}{8} \\times \\frac{3}{7} = \\frac{15}{56} \\approx 0{,}2679$",
                  "$\\frac{5}{8} + \\frac{3}{7} \\approx 1{,}0536$"
            ],
            "ans": 2,
            "fb": "Đúng! Theo quy tắc nhân: $P(T_1 \\cap Đ_2) = P(T_1) P(Đ_2 \\mid T_1) = \\frac{5}{8} \\times \\frac{3}{7} = \\frac{15}{56}$."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Một bệnh hiếm gặp có tỷ lệ mắc $P(D) = 0{,}001$. Xét nghiệm có độ nhạy $P(+ \\mid D) = 0{,}99$ và tỷ lệ dương tính giả $P(+ \\mid \\bar{D}) = 0{,}05$. Khi một người nhận kết quả dương tính, xác suất người đó thực sự mắc bệnh xấp xỉ là:",
            "opts": [
                  "$50\\%$",
                  "$99\\%$",
                  "$94\\%$",
                  "$1{,}94\\%$"
            ],
            "ans": 3,
            "fb": "Chính xác! Áp dụng Bayes: $P(+ ) = 0{,}001(0{,}99) + 0{,}999(0{,}05) = 0{,}00099 + 0{,}04995 = 0{,}05094$. Suy ra $P(D \\mid +) = 0{,}00099 / 0{,}05094 \\approx 0{,}0194 = 1{,}94\\%$ (Bẫy kinh điển: tỷ lệ nền bệnh quá thấp!)."
      }
],
    final_quiz: {
      q: "Hộp có 5 quả cầu gồm 2 đỏ và 3 xanh. Rút liên tiếp 2 quả không hoàn lại. Xác suất để quả thứ nhất màu đỏ VÀ quả thứ hai màu đỏ là:",
      opts: [
        "0,10 (hay 1/10)",
        "0,16 (hay 4/25)",
        "0,40 (hay 2/5)",
        "0,20 (hay 1/5)"
      ],
      ans: 0,
      fb: [
        "Chính xác! Lần 1 rút đỏ xác suất 2/5. Sau đó còn lại 4 quả (1 đỏ), lần 2 rút đỏ với xác suất 1/4. Nhân lại: (2/5) * (1/4) = 2/20 = 0,10.",
        "Sai! Bạn đã tính theo kiểu CÓ HOÀN LẠI: (2/5) * (2/5) = 4/25 = 0,16.",
        "Sai! 0,40 chỉ là xác suất rút đỏ ở lần thứ nhất.",
        "Sai! Tính toán nhầm mẫu số."
      ]
    }
  },

  {
    id: "B4",
    cluster: "B",
    title: "Tính Độc lập vs Tính Xung khắc: Phân biệt cốt tử",
    sources: "Slide Week 05 (tr. 69–80); Stat20 Mục 3.3.5, 3.3.8",
    desc: "Xóa tan nhầm lẫn phổ biến nhất trong xác suất giữa Độc lập (Independent) và Xung khắc (Disjoint). Bài học xương máu từ vụ án Sally Clark.",
    steps: [
      {
        t: "Định nghĩa toán học của Tính Độc lập (Independence)",
        c: `<p>Hai biến cố $A$ và $B$ được gọi là <b>Độc lập (Independent)</b> nếu việc $B$ xảy ra hay không xảy ra <b>hoàn toàn không làm thay đổi xác suất</b> của $A$:</p>
            $$P(A \\mid B) = P(A) \\quad \\text{hoặc} \\quad P(A \\cap B) = P(A) \\cdot P(B)$$
            <div class="tip-box">
              <b>Ý nghĩa thực tế:</b> Tung một đồng xu 10 lần liên tiếp ra mặt Ngửa. Lần thứ 11, xác suất ra Ngửa vẫn là $0{,}5$, vì các lần tung là độc lập. Đồng xu không có trí nhớ!
            </div>`
      },
      {
        t: "Bảng đối chiếu: Độc lập vs Xung khắc",
        c: `<div class="warn-box">
              <b>⚠️ CẠM BẪY SỐ 1 TRONG ĐỀ THI: Đừng bao giờ đánh đồng Độc lập và Xung khắc!</b>
            </div>
            <table class="data-table">
              <thead><tr><th>Tiêu chí so sánh</th><th>Biến cố Xung khắc (Disjoint / Mutually Exclusive)</th><th>Biến cố Độc lập (Independent)</th></tr></thead>
              <tbody>
                <tr><td><b>Bản chất ý nghĩa</b></td><td>Hai biến cố <b>không thể cùng xảy ra</b> trong một lần thử.</td><td>Biến cố này xảy ra <b>không làm ảnh hưởng</b> đến xác suất của biến cố kia.</td></tr>
                <tr><td><b>Quan hệ tập hợp</b></td><td>Tập giao rỗng: $A \\cap B = \\emptyset$.</td><td>Tập giao KHÔNG rỗng (vẫn cùng xảy ra được).</td></tr>
                <tr><td><b>Xác suất của Giao</b></td><td>$$P(A \\cap B) = 0$$</td><td>$$P(A \\cap B) = P(A) \\cdot P(B)$$</td></tr>
                <tr><td><b>Xác suất của Hợp</b></td><td>$$P(A \\cup B) = P(A) + P(B)$$</td><td>$$P(A \\cup B) = P(A) + P(B) - P(A)P(B)$$</td></tr>
                <tr><td><b>Mối liên hệ giữa 2 khái niệm</b></td><td colspan="2"><b>Nếu hai biến cố có xác suất dương ($P(A)>0, P(B)>0$) mà XUNG KHẮC nhau thì chúng KHÔNG THỂ ĐỘC LẬP!</b><br>
                <i>Giải thích:</i> Nếu chúng xung khắc, khi biết $B$ xảy ra thì chắc chắn $A$ không xảy ra ($P(A|B) = 0 \\neq P(A)$). Thông tin về $B$ đã làm xác suất của $A$ sụp đổ về 0, nghĩa là chúng <b>cực kỳ phụ thuộc vào nhau</b>!</td></tr>
              </tbody>
            </table>`
      },
      {
        t: "Bài học lịch sử: Vụ án Sally Clark",
        c: `<p>Trong lịch sử tư pháp Anh quốc, Sally Clark bị kết án oan vì hai đứa con sơ sinh đột tử. Chuyên gia y tế tính xác suất một đứa trẻ đột tử là $1/8500$, rồi lấy bình phương $(1/8500)^2 \\approx 1/73\\text{ triệu}$ để khẳng định khả năng vô tội gần như bằng 0!</p>
            <p>Hội Thống kê Hoàng gia Anh đã can thiệp và chỉ ra sai lầm chết người: <b>Hai cái chết không hề độc lập</b> (chúng mang chung gen di truyền và môi trường sống). Khi không độc lập, việc nhân xác suất là hoàn toàn sai trái.</p>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        q: "Hai biến cố A và B độc lập với P(A) = 0,3 và P(B) = 0,5. Tính P(A ∩ B) và P(A ∪ B).",
        sol: "<b>Vì A và B độc lập:</b><br>" +
             "- Xác suất giao: $P(A \\cap B) = P(A) \\cdot P(B) = 0{,}3 \\times 0{,}5 = 0{,}15$.<br>" +
             "- Xác suất hợp: $P(A \\cup B) = P(A) + P(B) - P(A \\cap B) = 0{,}3 + 0{,}5 - 0{,}15 = 0{,}65$."
      },
      {
        level: "Trung bình",
        q: "Một bài thi gồm 2 câu hỏi độc lập. Sinh viên A có xác suất làm đúng câu 1 là 0,8 và làm đúng câu 2 là 0,7. Tính xác suất sinh viên đó làm đúng ít nhất một câu.",
        sol: "<b>Cách 1 (Dùng quy tắc cộng độc lập):</b><br>" +
             "$$P(\\text{Đúng ít nhất 1}) = P(C_1) + P(C_2) - P(C_1 \\cap C_2) = 0{,}8 + 0{,}7 - (0{,}8 \\times 0{,}7) = 1{,}5 - 0{,}56 = 0{,}94$$.<br>" +
             "<b>Cách 2 (Dùng biến cố đối):</b><br>" +
             "Xác suất sai cả 2 câu: $(1 - 0{,}8) \\times (1 - 0{,}7) = 0{,}2 \\times 0{,}3 = 0{,}06$.<br>" +
             "$\\implies P(\\text{Đúng ít nhất 1}) = 1 - 0{,}06 = 0{,}94$."
      },
      {
        level: "Vận dụng",
        q: "Một hệ thống điện tử có 2 rơ-le mắc song song hoạt động độc lập. Xác suất rơ-le 1 hỏng là 0,05; rơ-le 2 hỏng là 0,08. Hệ thống chỉ ngừng hoạt động khi CẢ HAI rơ-le cùng hỏng. Tính xác suất hệ thống hoạt động bình thường.",
        sol: "<b>Bước 1:</b> Vì 2 rơ-le hoạt động độc lập, xác suất cả hai cùng hỏng là:<br>" +
             "$$P(\\text{Cả 2 hỏng}) = 0{,}05 \\times 0{,}08 = 0{,}004\\text{ (0{,}4\\%)}$$<br>" +
             "<b>Bước 2:</b> Hệ thống hoạt động bình thường khi không phải cả hai cùng hỏng (biến cố đối):<br>" +
             "$$P(\\text{Hoạt động}) = 1 - P(\\text{Cả 2 hỏng}) = 1 - 0{,}004 = 0{,}996\\text{ (99{,}6\\%)}$$."
      }
    ],
    pitfalls: [
      {
        bad: "Thấy A và B xung khắc liền suy ra P(A ∩ B) = P(A)P(B).",
        good: "Khi xung khắc, P(A ∩ B) = 0! Chỉ khi độc lập mới có công thức nhân P(A ∩ B) = P(A)P(B)."
      },
      {
        bad: "Nghĩ rằng hai sự kiện không liên quan trong đời thực thì tự động xung khắc với nhau trong toán học.",
        good: "Không liên quan trong đời thực nghĩa là ĐỘC LẬP, không phải xung khắc!"
      }
    ],
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Khẳng định nào sau đây định nghĩa chính xác hai biến cố $A$ và $B$ độc lập thống kê?",
            "opts": [
                  "$P(A \\cup B) = P(A) + P(B)$",
                  "$A \\cap B = \\emptyset$",
                  "$P(A \\cap B) = P(A) P(B)$",
                  "$P(A \\mid B) = 0$"
            ],
            "ans": 2,
            "fb": "Chính xác! Độc lập là một thuộc tính thông tin: biến cố này xảy ra không làm thay đổi xác suất biến cố kia."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Cho hai biến cố $A$ và $B$ độc lập có $P(A) = 0{,}4$ và $P(B) = 0{,}5$. Xác suất $P(A \\cup B)$ bằng:",
            "opts": [
                  "$0{,}20$",
                  "$0{,}90$",
                  "$0{,}50$",
                  "$0{,}70$"
            ],
            "ans": 3,
            "fb": "Đúng! $P(A \\cap B) = 0{,}4 \\times 0{,}5 = 0{,}20$. Áp dụng công thức cộng: $P(A \\cup B) = 0{,}4 + 0{,}5 - 0{,}20 = 0{,}70$."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Giả sử $A$ và $B$ là hai biến cố có $P(A) > 0$ và $P(B) > 0$. Nếu $A$ và $B$ xung khắc ($A \\cap B = \\emptyset$), liệu chúng có thể độc lập với nhau không?",
            "opts": [
                  "Có, vì xung khắc nghĩa là chúng không liên quan đến nhau nên độc lập",
                  "Không bao giờ, vì $P(A \\cap B) = 0$ trong khi $P(A)P(B) > 0$, hai vế không thể bằng nhau",
                  "Có, nếu $P(A) + P(B) = 1$",
                  "Chỉ độc lập khi $P(A) = P(B)$"
            ],
            "ans": 1,
            "fb": "Chính xác! Bẫy kinh điển số 4: Xung khắc là phụ thuộc cực đại (nếu $A$ xảy ra thì chắc chắn $B$ không xảy ra, tức $P(B \\mid A) = 0 \\ne P(B)$)."
      }
],
    final_quiz: {
      q: "Cho hai biến cố A và B độc lập với nhau, có P(A) = 0,3 và P(B) = 0,5. Xác suất P(A ∩ B) bằng bao nhiêu?",
      opts: [
        "0,15",
        "0,80",
        "0,00",
        "0,65"
      ],
      ans: 0,
      fb: [
        "Chính xác! Vì A và B độc lập nên P(A ∩ B) = P(A) * P(B) = 0,3 * 0,5 = 0,15.",
        "Sai! 0,80 là tổng P(A) + P(B), không phải giao.",
        "Sai! P(A ∩ B) = 0 chỉ đúng khi hai biến cố XUNG KHẮC, không phải độc lập.",
        "Sai! 0,65 là xác suất của hợp P(A ∪ B) = 0,3 + 0,5 - 0,15 = 0,65."
      ]
    }
  },

  {
    id: "B5",
    cluster: "B",
    title: "Giải tích kết hợp & Kỹ thuật đếm (Quy tắc nhân, Hoán vị, Tổ hợp)",
    sources: "Slide Week 05 (tr. 81–93); Stat20 Mục 3.4.2",
    desc: "Trang bị các quy tắc đếm căn bản: Quy tắc nhân, Hoán vị, Chỉnh hợp và Tổ hợp C(n, k). Cột trụ để xây dựng các phân phối Nhị thức và Siêu bội.",
    steps: [
      {
        t: "Quy tắc nhân và Quy tắc cộng trong giải tích kết hợp",
        c: `<p>Để tính xác suất cổ điển $P(A) = \\frac{|A|}{|\\Omega|}$, ta cần đếm số phần tử của tập hợp mà không phải liệt kê thủ công:</p>
            <ul>
              <li><b>Quy tắc nhân (Multiplication Rule)</b>: Một công việc gồm $k$ bước liên tiếp. Bước 1 có $n_1$ cách, bước 2 có $n_2$ cách,... thì tổng số cách hoàn thành công việc là:
                  $$N = n_1 \\times n_2 \\times \\dots \\times n_k$$
              </li>
              <li><b>Quy tắc cộng (Addition Rule)</b>: Nếu một công việc có thể làm theo một trong hai phương án loại trừ lẫn nhau (phương án 1 có $n_1$ cách, phương án 2 có $n_2$ cách) $\\implies$ Tổng số cách là $n_1 + n_2$.</li>
            </ul>`
      },
      {
        t: "Hoán vị, Chỉnh hợp và Tổ hợp: Khi nào xét thứ tự?",
        c: `<p>Điểm mấu chốt khi giải bài toán đếm là tự hỏi: <b>THỨ TỰ CÓ QUAN TRỌNG KHÔNG?</b></p>
            <table class="data-table">
              <thead><tr><th>Khái niệm</th><th>Ý nghĩa</th><th>Thứ tự?</th><th>Công thức</th><th>Ví dụ</th></tr></thead>
              <tbody>
                <tr><td><b>Hoán vị $P_n$</b></td><td>Xếp toàn bộ $n$ phần tử vào $n$ vị trí.</td><td><b>CÓ</b></td><td>$$n! = n(n-1)\\dots 1$$</td><td>Xếp 5 người vào một hàng dọc: $5! = 120$ cách.</td></tr>
                <tr><td><b>Chỉnh hợp $A_n^k$</b></td><td>Chọn $k$ phần tử từ $n$ phần tử VÀ xếp thứ tự.</td><td><b>CÓ</b></td><td>$$A_n^k = \\frac{n!}{(n-k)!}$$</td><td>Chọn 3 người từ 10 người làm Trưởng, Phó, Thư ký: $A_{10}^3 = 720$.</td></tr>
                <tr><td><b>Tổ hợp $C_n^k$</b></td><td>Chọn $k$ phần tử từ $n$ phần tử KHÔNG xét thứ tự.</td><td><b>KHÔNG</b></td><td>$$C_n^k = \\binom{n}{k} = \\frac{n!}{k!(n-k)!}$$</td><td>Chọn 3 người từ 10 người đi dự hội nghị: $C_{10}^3 = 120$.</td></tr>
              </tbody>
            </table>
            <div class="tip-box">
              <b>Phân biệt siêu nhanh:</b> Nếu đổi chỗ 2 người được chọn mà vai trò của họ thay đổi $\\rightarrow$ Dùng <b>Chỉnh hợp $A_n^k$</b>. Nếu đổi chỗ mà nhóm người đó vẫn giữ nguyên vai trò $\\rightarrow$ Dùng <b>Tổ hợp $C_n^k$</b>!
            </div>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        q: "Có bao nhiêu cách chọn 3 sinh viên từ một nhóm 10 sinh viên để thành lập một nhóm làm bài tập lớn?",
        sol: "<b>Phân tích:</b> Các thành viên trong nhóm làm bài tập có vai trò bình đẳng, việc đổi chỗ các thành viên không tạo ra nhóm mới $\\implies$ Không xét thứ tự, dùng <b>Tổ hợp</b>.<br>" +
             "$$C_{10}^3 = \\frac{10!}{3! \\cdot 7!} = \\frac{10 \\times 9 \\times 8}{3 \\times 2 \\times 1} = 120\\text{ cách}$$."
      },
      {
        level: "Trung bình",
        q: "Một mã PIN bảo mật của ứng dụng ngân hàng gồm 4 chữ số (mỗi chữ số từ 0 đến 9). Có bao nhiêu mã PIN khác nhau nếu: (a) Các chữ số được phép lặp lại; (b) Các chữ số phải đôi một khác nhau?",
        sol: "<b>Ý (a) Được lặp lại:</b> Mỗi vị trí trong 4 vị trí đều có 10 cách chọn (từ 0 đến 9). Theo quy tắc nhân:<br>" +
             "$$N = 10 \\times 10 \\times 10 \\times 10 = 10^4 = 10.000\\text{ mã}$$<br>" +
             "<b>Ý (b) Đôi một khác nhau:</b> Chọn 4 chữ số từ 10 chữ số và có xét thứ tự (vị trí hàng nghìn, trăm, chục, đơn vị) $\\implies$ Chỉnh hợp:<br>" +
             "$$A_{10}^4 = \\frac{10!}{6!} = 10 \\times 9 \\times 8 \\times 7 = 5.040\\text{ mã}$$."
      },
      {
        level: "Vận dụng",
        q: "Một hộp chứa 6 quả cầu đỏ và 4 quả cầu xanh. Rút ngẫu nhiên đồng thời 3 quả cầu. Tính xác suất để rút được đúng 2 quả đỏ và 1 quả xanh.",
        sol: "<b>Bước 1:</b> Tổng số cách rút 3 quả bất kỳ từ 10 quả cầu (không gian mẫu):<br>" +
             "$$|\\Omega| = C_{10}^3 = \\frac{10 \\times 9 \\times 8}{3 \\times 2 \\times 1} = 120$$<br>" +
             "<b>Bước 2:</b> Số cách chọn 2 quả đỏ từ 6 quả đỏ: $C_6^2 = \\frac{6 \\times 5}{2 \\times 1} = 15$.<br>" +
             "<b>Bước 3:</b> Số cách chọn 1 quả xanh từ 4 quả xanh: $C_4^1 = 4$.<br>" +
             "<b>Bước 4:</b> Theo quy tắc nhân, số kết quả thuận lợi là $|A| = C_6^2 \\times C_4^1 = 15 \\times 4 = 60$.<br>" +
             "<b>Bước 5:</b> Xác suất cần tìm:<br>" +
             "$$P(A) = \\frac{|A|}{|\\Omega|} = \\frac{60}{120} = 0{,}50\\text{ (50\\%)}$$."
      }
    ],
    pitfalls: [
      {
        bad: "Dùng nhầm Chỉnh hợp A(n, k) thay vì Tổ hợp C(n, k) khi chọn người vào cùng một ban đại diện.",
        good: "Luôn kiểm tra: việc xếp người có kèm chức danh cụ thể (Chủ tịch, Phó chủ tịch) hay không. Không có chức danh thì luôn dùng C(n, k)!"
      },
      {
        bad: "Nhân nhầm xác suất khi các quả cầu được rút đồng thời.",
        good: "Rút đồng thời chính là mô hình lấy mẫu không hoàn lại, sử dụng công thức tổ hợp tỷ lệ (phân phối siêu bội)."
      }
    ],
    quizzes: [
      {
            "level": "Nhận biết",
            "badge": "🟢 Cấp độ 1: Nhận biết",
            "q": "Số cách chọn một ban cán sự gồm 1 lớp trưởng, 1 lớp phó và 1 bí thư từ 30 sinh viên là một bài toán:",
            "opts": [
                  "Chỉnh hợp không lặp $A_{30}^3$",
                  "Hoán vị $P_{30}$",
                  "Chỉnh hợp lặp $30^3$",
                  "Tổ hợp $C_{30}^3$"
            ],
            "ans": 0,
            "fb": "Chính xác! Vì 3 chức danh khác nhau nên việc chọn có phân biệt thứ tự/vai trò, đây là bài toán chỉnh hợp."
      },
      {
            "level": "Thông hiểu",
            "badge": "🟡 Cấp độ 2: Thông hiểu",
            "q": "Có bao nhiêu cách chọn ra 4 sinh viên từ một nhóm 10 sinh viên đi dự hội nghị mà không phân biệt chức vụ?",
            "opts": [
                  "$C_{10}^4 = 210$",
                  "$10^4 = 10000$",
                  "$40$",
                  "$A_{10}^4 = 5040$"
            ],
            "ans": 0,
            "fb": "Đúng! Không phân biệt thứ tự là bài toán tổ hợp: $C_{10}^4 = \\frac{10!}{4!6!} = 210$ cách."
      },
      {
            "level": "Vận dụng",
            "badge": "🔴 Cấp độ 3: Vận dụng & Bẫy",
            "q": "Một phòng thi có 23 sinh viên. Xác suất để có ít nhất hai sinh viên có cùng ngày sinh nhật (năm có 365 ngày) là:",
            "opts": [
                  "$1 - \\left(\\frac{364}{365}\\right)^{23} \\approx 6{,}1\\%$",
                  "$\\frac{C_{23}^2}{365} \\approx 69{,}3\\%$",
                  "$\\frac{23}{365} \\approx 6{,}3\\%$",
                  "$1 - \\frac{A_{365}^{23}}{365^{23}} \\approx 50{,}7\\%$"
            ],
            "ans": 3,
            "fb": "Chính xác! Nghịch lý ngày sinh (Birthday Paradox): Biến cố đối là mọi người đều có ngày sinh khác nhau, với 23 người xác suất trùng đã vượt 50%!"
      }
],
    final_quiz: {
      q: "Chọn ngẫu nhiên 3 người từ một nhóm gồm 10 người (không phân biệt thứ tự hay chức vụ). Có bao nhiêu cách chọn khác nhau?",
      opts: [
        "120",
        "720",
        "30",
        "1000"
      ],
      ans: 0,
      fb: [
        "Chính xác! Vì không phân biệt thứ tự nên dùng Tổ hợp: C(10, 3) = (10*9*8)/(3*2*1) = 120 cách.",
        "Sai! 720 là Chỉnh hợp A(10, 3) = 10*9*8, chỉ dùng khi có phân biệt thứ tự (ví dụ: Trưởng, Phó, Thư ký).",
        "Sai! 30 là lấy 10 * 3, không có cơ sở toán học.",
        "Sai! 1000 là 10^3, dùng khi chọn 3 người có hoàn lại và có xét thứ tự."
      ]
    }
  }
];

if (typeof module !== 'undefined' && module.exports) {
  module.exports = CUM_B;
}
