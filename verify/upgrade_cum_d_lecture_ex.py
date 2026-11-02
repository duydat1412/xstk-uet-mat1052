# verify/upgrade_cum_d_lecture_ex.py
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("content/cum_d.js", "r", encoding="utf-8") as f:
    text = f.read()

D1_EXAMPLES = """    examples: [
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
           "b) Tính trung bình của hộp $\\\\mu$ và độ lệch chuẩn của hộp $\\\\sigma$.",
        sol: "<b>Lời giải chi tiết theo Slide Week 07 (trang 28):</b><br>" +
             "a) Bảng phân phối xác suất của $X$ (tổng 10 vé):<br>" +
             "   - $p(0) = \\\\frac{2}{10} = 0{,}2$; $p(1) = \\\\frac{3}{10} = 0{,}3$; $p(2) = \\\\frac{1}{10} = 0{,}1$; $p(3) = \\\\frac{2}{10} = 0{,}2$; $p(4) = \\\\frac{2}{10} = 0{,}2$.<br>" +
             "b) Tính trung bình của hộp (Kỳ vọng):<br>" +
             "   $$\\\\mu = E(X) = 0(0{,}2) + 1(0{,}3) + 2(0{,}1) + 3(0{,}2) + 4(0{,}2) = 0 + 0{,}3 + 0{,}2 + 0{,}6 + 0{,}8 = 1{,}9$$<br>" +
             "   Tính $E(X^2)$:<br>" +
             "   $$E(X^2) = 0^2(0{,}2) + 1^2(0{,}3) + 2^2(0{,}1) + 3^2(0{,}2) + 4^2(0{,}2) = 0 + 0{,}3 + 0{,}4 + 1{,}8 + 3{,}2 = 5{,}5$$<br>" +
             "   Phương sai và độ lệch chuẩn của hộp:<br>" +
             "   $$\\\\operatorname{Var}(X) = E(X^2) - \\\\mu^2 = 5{,}5 - (1{,}9)^2 = 5{,}5 - 3{,}61 = 1{,}89$$<br>" +
             "   $$\\\\sigma = \\\\sqrt{1{,}89} \\\\approx 1{,}3748 \\\\approx 1{,}375$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 07 — Slide 21–24] Bản chất Biến ngẫu nhiên i.i.d. khi Lấy mẫu",
        q: "Từ chiếc hộp 10 lá thăm ở trên, một người thực hiện rút ngẫu nhiên $n$ lần. Giải thích rõ sự khác biệt bản chất giữa: (1) Rút CÓ HOÀN LẠI và (2) Rút KHÔNG HOÀN LẠI. Trường hợp nào các biến ngẫu nhiên kết quả $X_1, X_2, \\\\dots, X_n$ tạo thành một mẫu i.i.d.?",
        sol: "<b>Phân tích bản chất theo Slide Week 07 (trang 21–24):</b><br>" +
             "1. <b>Rút CÓ HOÀN LẠI:</b> Sau mỗi lần rút, lá thăm được trả lại vào hộp và xáo đều. Do đó thành phần của hộp không thay đổi $\\\\implies$ Mỗi lần rút tuân theo <b>cùng phân phối</b> gốc $\\\\mu=1{,}9, \\\\sigma=1{,}375$ và kết quả lần trước hoàn toàn <b>độc lập</b> với lần sau.<br>" +
             "   \\\\rightarrow <b>Đây chính là mẫu i.i.d. (independent and identically distributed)!</b><br>" +
             "2. <b>Rút KHÔNG HOÀN LẠI:</b> Sau mỗi lần rút, số vé trong hộp giảm đi, tỉ lệ các con số thay đổi tùy thuộc vào vé đã rút $\\\\implies$ Các biến ngẫu nhiên $X_1, X_2, \\\\dots$ bị phụ thuộc lẫn nhau, KHÔNG độc lập và phân phối có điều kiện bị thay đổi."
      }
    ]"""

D2_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 07 — Ví dụ 8] Tổng số điểm của 25 lần rút thẻ từ Hộp",
        q: "Từ hộp có các lá thăm $[0, 0, 1, 1, 1, 2, 3, 3, 4, 4]$ với $\\\\mu = 1{,}9$ và $\\\\sigma = 1{,}375$ (Slide 29–30). Rút ngẫu nhiên độc lập có hoàn lại $n = 25$ lần. Gọi $S_{25} = X_1 + X_2 + \\\\dots + X_{25}$ là tổng số điểm ghi trên 25 lá thăm rút được.<br>" +
           "a) Tính kỳ vọng của tổng $E(S_{25})$.<br>" +
           "b) Tính độ lệch chuẩn của tổng $\\\\operatorname{SD}(S_{25})$.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 07 (trang 30):</b><br>" +
             "a) Theo quy tắc nhân $n$ của kỳ vọng tổng:<br>" +
             "   $$E(S_{25}) = n \\\\cdot \\\\mu = 25 \\\\times 1{,}9 = 47{,}5$$<br>" +
             "b) Theo Quy tắc căn bậc hai (Square Root Law) cho tổng các biến i.i.d.:<br>" +
             "   $$\\\\operatorname{Var}(S_{25}) = n \\\\cdot \\\\sigma^2 = 25 \\\\times 1{,}89 = 47{,}25$$<br>" +
             "   $$\\\\operatorname{SD}(S_{25}) = \\\\sigma \\\\sqrt{n} = 1{,}3748 \\\\times \\\\sqrt{25} = 1{,}3748 \\\\times 5 \\\\approx 6{,}874 \\\\approx 6{,}875$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 07 — Ví dụ 8] Trung bình mẫu của 25 lần rút thẻ",
        q: "Cũng với phép thử rút có hoàn lại $n = 25$ lần ở trên (Slide 29–30). Gọi $\\\\bar{X}_{25} = \\\\frac{S_{25}}{25}$ là số điểm trung bình của một lá thăm trong mẫu 25 lần rút.<br>" +
           "a) Tính kỳ vọng của trung bình mẫu $E(\\\\bar{X}_{25})$.<br>" +
           "b) Tính độ lệch chuẩn của trung bình mẫu $\\\\operatorname{SD}(\\\\bar{X}_{25})$.",
        sol: "<b>Lời giải chuẩn xác theo Slide Week 07 (trang 30):</b><br>" +
             "a) Kỳ vọng của trung bình mẫu bằng đúng trung bình tổng thể:<br>" +
             "   $$E(\\\\bar{X}_{25}) = \\\\mu = 1{,}9$$<br>" +
             "b) Độ lệch chuẩn của trung bình mẫu giảm theo nghịch đảo căn bậc hai của cỡ mẫu ($1/\\\\sqrt{n}$):<br>" +
             "   $$\\\\operatorname{SD}(\\\\bar{X}_{25}) = \\\\frac{\\\\sigma}{\\\\sqrt{n}} = \\\\frac{1{,}3748}{\\\\sqrt{25}} = \\\\frac{1{,}3748}{5} \\\\approx 0{,}275$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 07 — Slide 26] Ứng dụng Quy tắc Căn bậc hai (Square Root Law)",
        q: "Một nhà nghiên cứu đang đo độ dày linh kiện với độ lệch chuẩn trung bình mẫu hiện tại là $\\\\operatorname{SD}(\\\\bar{X}) = 0{,}275$ mm khi dùng cỡ mẫu $n = 25$. Để nâng cao độ chính xác của phép đo, nhà nghiên cứu muốn giảm độ lệch chuẩn của trung bình mẫu đi 4 lần (xuống còn $\\\\approx 0{,}06875$ mm). Cần phải tăng cỡ mẫu lên bao nhiêu lần và cỡ mẫu mới $n'$ là bao nhiêu?",
        sol: "<b>Phân tích định lý theo Slide Week 07 (trang 26):</b><br>" +
             "1. Theo công thức: $\\\\operatorname{SD}(\\\\bar{X}) = \\\\frac{\\\\sigma}{\\\\sqrt{n}}$. Để $\\\\operatorname{SD}(\\\\bar{X})$ giảm đi $k = 4$ lần, mẫu số $\\\\sqrt{n}$ phải tăng lên $4$ lần.<br>" +
             "2. Do đó, cỡ mẫu $n$ phải tăng lên $k^2 = 4^2 = 16$ lần!<br>" +
             "   $$n' = n \\\\times 16 = 25 \\\\times 16 = 400 \\\\text{ quan sát}$$<br>" +
             "<b>Kết luận quy tắc vàng:</b> Muốn độ chính xác tăng gấp đôi, cỡ mẫu phải tăng gấp 4; muốn độ chính xác tăng gấp 4, cỡ mẫu phải tăng gấp 16!"
      }
    ]"""

D3_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 07 — Slide 34] Đánh giá Xác suất Sai lệch bằng BĐT Chebyshev",
        q: "Cho một biến ngẫu nhiên $X$ có phân phối bất kỳ (chưa biết là phân phối gì) với kỳ vọng $\\\\mu$ và độ lệch chuẩn $\\\\sigma$. Dùng Bất đẳng thức Chebyshev đánh giá cận trên của xác suất để $X$ nhận giá trị lệch khỏi kỳ vọng từ 2 độ lệch chuẩn trở lên ($P(|X - \\\\mu| \\\\ge 2\\\\sigma)$).",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 07 (trang 34):</b><br>" +
             "Bất đẳng thức Chebyshev phát biểu rằng với mọi $k > 0$:<br>" +
             "$$P(|X - \\\\mu| \\\\ge k\\\\sigma) \\\\le \\\\frac{1}{k^2}$$<br>" +
             "Thay $k = 2$ vào bất đẳng thức:<br>" +
             "$$P(|X - \\\\mu| \\\\ge 2\\\\sigma) \\\\le \\\\frac{1}{2^2} = \\\\frac{1}{4} = 0{,}25 \\\\text{ (hay 25\\\\%)}$$<br>" +
             "Tương đương: Xác suất để biến ngẫu nhiên nằm trong khoảng $[\\\\mu - 2\\\\sigma, \\\\mu + 2\\\\sigma]$ đạt ít nhất $1 - 0{,}25 = 75\\\\%$ đối với MỌI phân phối xác suất!"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 07 — Ví dụ 9] Giám sát Nhiệt độ Lò sấy UET",
        q: "Một nhà máy cần theo dõi nhiệt độ thật $\\\\mu$ của lò sấy (Slide 35–36). Mỗi phép đo là biến ngẫu nhiên có kỳ vọng $\\\\mu$ và độ lệch chuẩn $\\\\sigma = 2^\\\\circ\\\\text{C}$. Các phép đo độc lập. Gọi $\\\\bar{X}_n$ là trung bình của $n$ lần đo. Cần thực hiện ít nhất bao nhiêu lần đo để xác suất sai lệch $|\\\\bar{X}_n - \\\\mu| \\\\ge 1^\\\\circ\\\\text{C}$ không vượt quá 5% ($0{,}05$)?",
        sol: "<b>Lời giải chi tiết theo Slide Week 07 (trang 36):</b><br>" +
             "1. Trung bình mẫu $\\\\bar{X}_n$ có $E(\\\\bar{X}_n) = \\\\mu$ và phương sai $\\\\operatorname{Var}(\\\\bar{X}_n) = \\\\frac{\\\\sigma^2}{n} = \\\\frac{4}{n}$.<br>" +
             "2. Áp dụng Bất đẳng thức Chebyshev dạng sai số tuyệt đối $\\\\epsilon = 1^\\\\circ\\\\text{C}$:<br>" +
             "   $$P(|\\\\bar{X}_n - \\\\mu| \\\\ge \\\\epsilon) \\\\le \\\\frac{\\\\operatorname{Var}(\\\\bar{X}_n)}{\\\\epsilon^2} = \\\\frac{4/n}{1^2} = \\\\frac{4}{n}$$<br>" +
             "3. Yêu cầu xác suất này không vượt quá $0{,}05$:<br>" +
             "   $$\\\\frac{4}{n} \\\\le 0{,}05 \\\\iff n \\\\ge \\\\frac{4}{0{,}05} = 80$$<br>" +
             "<b>Kết luận:</b> Cần đo ít nhất <b>80 lần</b> để bảo đảm độ tin cậy theo BĐT Chebyshev."
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 07 — Slide 37] So sánh Đánh giá Chebyshev vs Quy tắc Phân phối Chuẩn",
        q: "Tại sao ở $k = 2$, BĐT Chebyshev cho xác suất sai lệch là $\\\\le 25\\\\%$, trong khi quy tắc thực nghiệm phân phối chuẩn lại cho xác suất sai lệch chỉ khoảng $5\\\\%$? Khi nào trong bài thi bắt buộc phải dùng BĐT Chebyshev?",
        sol: "<b>Phân tích bản chất theo Slide Week 07 (trang 37):</b><br>" +
             "1. <b>Lý do chênh lệch:</b> Bất đẳng thức Chebyshev là cận trên cho <b>MỌI phân phối xác suất khả dĩ</b> (kể cả phân phối hai đỉnh, phân phối cực kỳ lệch hay phân phối có đuôi rất nặng). Quy tắc $5\\\\%$ chỉ đúng cho duy nhất hình chuông đối xứng chuẩn Gauss.<br>" +
             "2. <b>Khi nào bắt buộc dùng Chebyshev:</b> Khi đề bài <b>không cho biết dạng phân phối</b> của biến ngẫu nhiên (hoặc biết rõ phân phối không phải chuẩn) và cỡ mẫu $n$ chưa đủ lớn để áp dụng Định lý giới hạn trung tâm."
      }
    ]"""

D4_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 07 — Slide 38] Bản chất Toán học của Luật số lớn yếu (WLLN)",
        q: "Dùng Bất đẳng thức Chebyshev chứng minh chặt chẽ phát biểu của Luật số lớn yếu: Cho dãy biến ngẫu nhiên $X_1, X_2, \\\\dots, X_n$ i.i.d. có kỳ vọng $\\\\mu$ và phương sai $\\\\sigma^2$ hữu hạn. Chứng minh với mọi $\\\\epsilon > 0$ tùy ý:<br>" +
           "$$\\\\lim_{n \\\\to \\\\infty} P(|\\\\bar{X}_n - \\\\mu| \\\\ge \\\\epsilon) = 0$$",
        sol: "<b>Chứng minh giải tích theo Slide Week 07 (trang 38):</b><br>" +
             "1. Ta có $E(\\\\bar{X}_n) = \\\\mu$ và $\\\\operatorname{Var}(\\\\bar{X}_n) = \\\\frac{\\\\sigma^2}{n}$.<br>" +
             "2. Áp dụng Bất đẳng thức Chebyshev cho biến $\\\\bar{X}_n$ với sai số $\\\\epsilon > 0$:<br>" +
             "   $$0 \\\\le P(|\\\\bar{X}_n - \\\\mu| \\\\ge \\\\epsilon) \\\\le \\\\frac{\\\\operatorname{Var}(\\\\bar{X}_n)}{\\\\epsilon^2} = \\\\frac{\\\\sigma^2}{n \\\\cdot \\\\epsilon^2}$$<br>" +
             "3. Lấy giới hạn hai vế khi $n \\\\to \\\\infty$ (với $\\\\sigma^2$ và $\\\\epsilon^2$ là các hằng số dương cố định):<br>" +
             "   $$\\\\lim_{n \\\\to \\\\infty} \\\\frac{\\\\sigma^2}{n \\\\cdot \\\\epsilon^2} = 0$$<br>" +
             "   Theo nguyên lý kẹp (Squeeze Theorem), ta suy ra $\\\\lim_{n \\\\to \\\\infty} P(|\\\\bar{X}_n - \\\\mu| \\\\ge \\\\epsilon) = 0$ (ĐPCM)."
      },
      {
        level: "Trung bình",
        t: "[Slide Week 07 — Ví dụ 10] Bác bỏ Ngộ nhận Con bạc (Gambler's Fallacy)",
        q: "Sau 10 lần tung một đồng xu cân đối đều ra mặt Sấp, một người đánh cược khẳng định: <i>'Theo Luật số lớn, lần thứ 11 chắc chắn khả năng ra mặt Ngửa phải cao hơn rất nhiều để bù trừ lại cho cân bằng!'</i> (Slide 39–40). Khẳng định này đúng hay sai? Luật số lớn hoạt động theo cơ chế nào?",
        sol: "<b>Phân tích bản chất theo Slide Week 07 (trang 40):</b><br>" +
             "1. <b>Khẳng định SAI HOÀN TOÀN (Ngộ nhận con bạc)!</b> Các lần tung đồng xu là hoàn toàn độc lập, đồng xu không có trí nhớ. Ở lần tung thứ 11, xác suất ra mặt Ngửa vẫn chính xác bằng $0{,}5$.<br>" +
             "2. <b>Cơ chế của Luật số lớn là LÀM LOÃNG (Dilution), KHÔNG PHẢI BÙ TRỪ (Compensation):</b><br>" +
             "   - Chênh lệch 10 lần sấp ban đầu sẽ không mất đi.<br>" +
             "   - Nhưng khi $n$ tăng lên 10.000 hay 1.000.000 lần, con số 10 này khi chia cho mẫu số $n$ khổng lồ sẽ bị triệt tiêu về $0$: $\\\\frac{10}{1.000.000} = 0{,}00001 \\\\to 0$!"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 07 — Slide 40] Ứng dụng WLLN trong Quản trị Rủi ro Bảo hiểm",
        q: "Một công ty bảo hiểm bán 100.000 hợp đồng bảo hiểm xe máy độc lập trong một năm. Xác suất một xe gặp sự cố trong năm là $p = 0{,}02$ với số tiền bồi thường là 50 triệu đồng. Giải thích tại sao bán cho 1 khách hàng là canh bạc rủi ro lớn, nhưng bán cho 100.000 khách hàng thì lợi nhuận của công ty lại an toàn tuyệt đối nhờ Luật số lớn yếu.",
        sol: "<b>Phân tích kinh tế lượng theo Slide Week 07 (trang 40):</b><br>" +
             "1. Với 1 khách hàng: Biến cố nhận bồi thường là ngẫu nhiên cực đoan (hoặc 0 đồng hoặc mất ngay 50 triệu), rủi ro phương sai rất lớn.<br>" +
             "2. Với $n = 100.000$ hợp đồng độc lập: Tỉ lệ số vụ yêu cầu bồi thường $\\\\bar{X}_n$ tuân theo Luật số lớn yếu. Phương sai của tỉ lệ bồi thường là:<br>" +
             "   $$\\\\operatorname{Var}(\\\\bar{X}_n) = \\\\frac{p(1-p)}{n} = \\\\frac{0{,}02 \\\\times 0{,}98}{100.000} = 1{,}96 \\\\times 10^{-7} \\\\approx 0$$<br>" +
             "   Tỉ lệ bồi thường thực tế gần như chắc chắn $100\\\\%$ sẽ hội tụ sát nút về $2\\\\%$ (tức khoảng đúng 2.000 vụ bồi thường). Do đó công ty bảo hiểm chủ động định phí để thu lợi nhuận ổn định mà không lo phá sản."
      }
    ]"""

# Replace in cum_d.js
for lid, ex_code in [("D1", D1_EXAMPLES), ("D2", D2_EXAMPLES), ("D3", D3_EXAMPLES), ("D4", D4_EXAMPLES)]:
    p = rf'(id:\s*["\']{lid}["\'][\s\S]*?examples:\s*\[)[\s\S]*?(\]\s*,\s*pitfalls:)'
    text = re.sub(p, lambda m, code=ex_code: m.group(1) + "\n" + code[16:-1] + "\n    " + m.group(2), text)

with open("content/cum_d.js", "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully upgraded content/cum_d.js with exact lecture examples!")
