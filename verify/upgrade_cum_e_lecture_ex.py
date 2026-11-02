# verify/upgrade_cum_e_lecture_ex.py
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("content/cum_e.js", "r", encoding="utf-8") as f:
    text = f.read()

E1_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 07 — Ví dụ 11] Kiểm tra Hàm mật độ xác suất liên tục",
        q: "Xét hàm số xác định trên toàn bộ trục số thực (Slide 43–44):<br>" +
           "$$f(x) = \\\\begin{cases} 1{,}5 (1 - x^2) & \\\\text{khi } 0 \\\\le x \\\\le 1 \\\\cr 0 & \\\\text{ở ngoài} \\\\end{cases}$$<br>" +
           "a) Chứng minh rằng $f(x)$ là một hàm mật độ xác suất (pdf) hợp lệ.<br>" +
           "b) Tính xác suất để biến ngẫu nhiên $X$ nhận giá trị trong đoạn $[0; 0{,}5]$.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 07 (trang 44):</b><br>" +
             "a) Kiểm tra 2 điều kiện tiên đề của hàm mật độ:<br>" +
             "   1. Hàm không âm: Với mọi $0 \\\\le x \\\\le 1$, $1 - x^2 \\\\ge 0 \\\\implies f(x) \\\\ge 0$.<br>" +
             "   2. Tích phân trên toàn trục số bằng 1:<br>" +
             "      $$\\\\int_{-\\\\infty}^\\\\infty f(x)dx = \\\\int_0^1 1{,}5(1 - x^2)dx = 1{,}5 \\\\left[x - \\\\frac{x^3}{3}\\\\right]_0^1 = 1{,}5 \\\\left(1 - \\\\frac{1}{3}\\\\right) = 1{,}5 \\\\times \\\\frac{2}{3} = 1$$<br>" +
             "   Vậy $f(x)$ là hàm mật độ xác suất hợp lệ.<br>" +
             "b) Xác suất $P(0 \\\\le X \\\\le 0{,}5)$:<br>" +
             "   $$P(0 \\\\le X \\\\le 0{,}5) = \\\\int_0^{0{,}5} 1{,}5(1 - x^2)dx = 1{,}5 \\\\left[0{,}5 - \\\\frac{(0{,}5)^3}{3}\\\\right] = 1{,}5 \\\\left(0{,}5 - \\\\frac{0{,}125}{3}\\\\right) = 0{,}6875 \\\\text{ (hay 68{,}75\\\\%)}$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 07 — Ví dụ 12] Tìm Hàm tích lũy cdf từ Hàm mật độ",
        q: "Cho biến ngẫu nhiên liên tục $X$ có hàm mật độ (Slide 46–47):<br>" +
           "$$f_X(x) = \\\\begin{cases} \\\\frac{3}{8} x^2 & \\\\text{khi } 0 \\\\le x \\\\le 2 \\\\cr 0 & \\\\text{ở ngoài} \\\\end{cases}$$<br>" +
           "Hãy xác định hàm phân phối tích lũy $F_X(x) = P(X \\\\le x)$ trên toàn bộ $\\\\mathbb{R}$.",
        sol: "<b>Lời giải chi tiết theo Slide Week 07 (trang 47):</b><br>" +
             "1. Khi $x < 0$: Vì $f(t) = 0$ nên $F_X(x) = \\\\int_{-\\\\infty}^x 0 dt = 0$.<br>" +
             "2. Khi $0 \\\\le x \\\\le 2$:<br>" +
             "   $$F_X(x) = \\\\int_{-\\\\infty}^0 0 dt + \\\\int_0^x \\\\frac{3}{8} t^2 dt = \\\\left[\\\\frac{3}{8} \\\\cdot \\\\frac{t^3}{3}\\\\right]_0^x = \\\\frac{x^3}{8}$$<br>" +
             "3. Khi $x > 2$: Tích phân bao trùm toàn bộ miền xác định nên $F_X(x) = 1$.<br>" +
             "<b>Kết luận hàm cdf:</b><br>" +
             "$$F_X(x) = \\\\begin{cases} 0 & \\\\text{khi } x < 0 \\\\cr \\\\frac{x^3}{8} & \\\\text{khi } 0 \\\\le x \\\\le 2 \\\\cr 1 & \\\\text{khi } x > 2 \\\\end{cases}$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 07 — Bài tập 2] Bài toán Xác định Tham số Cận trên b",
        q: "Biến ngẫu nhiên liên tục $X$ nhận giá trị trong đoạn $[0, b]$ với $b > 0$ (Slide 82–83). Hàm phân phối tích lũy trên đoạn này là $F_X(x) = \\\\frac{x^2}{9}$ (với $0 \\\\le x \\\\le b$).<br>" +
           "a) Tìm giá trị của hằng số $b$.<br>" +
           "b) Tìm hàm mật độ xác suất $f_X(x)$ và tính $P(1 \\\\le X \\\\le 2)$.",
        sol: "<b>Lời giải mẫu bài thi theo Slide Week 07 (trang 83):</b><br>" +
             "a) Vì $X$ là biến liên tục nên hàm tích lũy $F_X(x)$ liên tục tại cận trên $b$ và đạt giá trị $1$:<br>" +
             "   $$F_X(b) = 1 \\\\iff \\\\frac{b^2}{9} = 1 \\\\iff b^2 = 9 \\\\implies b = 3 \\\\quad (\\\\text{do } b > 0)$$<br>" +
             "b) Hàm mật độ $f_X(x)$ là đạo hàm của hàm tích lũy $F_X'(x)$ trên khoảng $(0, 3)$:<br>" +
             "   $$f_X(x) = F_X'(x) = \\\\left(\\\\frac{x^2}{9}\\\\right)' = \\\\frac{2x}{9} \\\\quad (0 < x < 3)$$<br>" +
             "   Xác suất $P(1 \\\\le X \\\\le 2)$ tính trực tiếp qua hàm tích lũy cdf:<br>" +
             "   $$P(1 \\\\le X \\\\le 2) = F_X(2) - F_X(1) = \\\\frac{2^2}{9} - \\\\frac{1^2}{9} = \\\\frac{4}{9} - \\\\frac{1}{9} = \\\\frac{3}{9} = \\\\frac{1}{3} \\\\approx 0{,}3333$$"
      }
    ]"""

E2_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 07 — Ví dụ 13] Kỳ vọng biến ngẫu nhiên liên tục",
        q: "Cho biến ngẫu nhiên liên tục $X$ có hàm mật độ xác suất: $f(x) = 2x$ khi $0 < x < 1$ (và bằng 0 ở ngoài, Slide 49). Hãy tính kỳ vọng $E(X)$.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 07 (trang 49):</b><br>" +
             "Áp dụng định nghĩa kỳ vọng của biến ngẫu nhiên liên tục:<br>" +
             "$$E(X) = \\\\int_{-\\\\infty}^\\\\infty x f(x)dx = \\\\int_0^1 x \\\\cdot (2x)dx = \\\\int_0^1 2x^2 dx$$<br>" +
             "$$E(X) = \\\\left[\\\\frac{2x^3}{3}\\\\right]_0^1 = \\\\frac{2(1)^3}{3} - 0 = \\\\frac{2}{3} \\\\approx 0{,}6667$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 07 — Ví dụ 13] Phương sai và Độ lệch chuẩn qua Tích phân",
        q: "Vẫn với biến ngẫu nhiên liên tục $X$ ở trên ($f(x) = 2x$ trên $(0, 1)$, $E(X) = 2/3$).<br>" +
           "a) Tính mô-men bậc hai $E(X^2)$.<br>" +
           "b) Tính phương sai $\\\\operatorname{Var}(X)$ và độ lệch chuẩn $\\\\operatorname{SD}(X)$.",
        sol: "<b>Lời giải chi tiết theo Slide Week 07 (trang 49):</b><br>" +
             "a) Tính $E(X^2)$ bằng tích phân:<br>" +
             "   $$E(X^2) = \\\\int_0^1 x^2 f(x)dx = \\\\int_0^1 x^2 \\\\cdot (2x)dx = \\\\int_0^1 2x^3 dx = \\\\left[\\\\frac{2x^4}{4}\\\\right]_0^1 = \\\\frac{1}{2} = 0{,}5$$<br>" +
             "b) Áp dụng công thức rút gọn tính phương sai:<br>" +
             "   $$\\\\operatorname{Var}(X) = E(X^2) - [E(X)]^2 = \\\\frac{1}{2} - \\\\left(\\\\frac{2}{3}\\\\right)^2 = \\\\frac{1}{2} - \\\\frac{4}{9} = \\\\frac{9 - 8}{18} = \\\\frac{1}{18} \\\\approx 0{,}0556$$<br>" +
             "   Độ lệch chuẩn:<br>" +
             "   $$\\\\operatorname{SD}(X) = \\\\sqrt{\\\\operatorname{Var}(X)} = \\\\frac{1}{\\\\sqrt{18}} = \\\\frac{1}{3\\\\sqrt{2}} \\\\approx 0{,}2357$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 07 — Bài tập 2 Ý 3] Kỳ vọng và Phương sai từ Bài tập mẫu UET",
        q: "Từ Bài tập 2 ở Slide 83: Biến ngẫu nhiên $X$ có hàm mật độ $f(x) = \\\\frac{2x}{9}$ trên khoảng $(0, 3)$. Hãy tính kỳ vọng $E(X)$ và phương sai $\\\\operatorname{Var}(X)$.",
        sol: "<b>Lời giải mẫu tự luận theo Slide Week 07 (trang 83):</b><br>" +
             "1. Tính kỳ vọng $E(X)$:<br>" +
             "   $$E(X) = \\\\int_0^3 x \\\\cdot \\\\left(\\\\frac{2x}{9}\\\\right)dx = \\\\int_0^3 \\\\frac{2x^2}{9}dx = \\\\left[\\\\frac{2x^3}{27}\\\\right]_0^3 = \\\\frac{2 \\\\times 27}{27} = 2$$<br>" +
             "2. Tính $E(X^2)$:<br>" +
             "   $$E(X^2) = \\\\int_0^3 x^2 \\\\cdot \\\\left(\\\\frac{2x}{9}\\\\right)dx = \\\\int_0^3 \\\\frac{2x^3}{9}dx = \\\\left[\\\\frac{2x^4}{36}\\\\right]_0^3 = \\\\left[\\\\frac{x^4}{18}\\\\right]_0^3 = \\\\frac{81}{18} = 4{,}5$$<br>" +
             "3. Tính phương sai:<br>" +
             "   $$\\\\operatorname{Var}(X) = E(X^2) - [E(X)]^2 = 4{,}5 - 2^2 = 4{,}5 - 4 = 0{,}5$$"
      }
    ]"""

E3_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 07 — Ví dụ 14] Thời điểm xe buýt đến bến qua Phân phối Đều",
        q: "Thời điểm xe buýt đến bến được mô hình hóa là phân phối đều từ 0 đến 10 phút, tức $X \\\\sim U(0, 10)$ (Slide 51–53).<br>" +
           "a) Viết hàm mật độ xác suất $f(x)$ của $X$.<br>" +
           "b) Tính xác suất xe buýt đến bến trong khoảng từ 3 đến 7 phút.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 07 (trang 53):</b><br>" +
             "a) Với phân phối đều $X \\\\sim U(a = 0, b = 10)$, hàm mật độ là hằng số trên $[0, 10]$:<br>" +
             "   $$f(x) = \\\\frac{1}{b - a} = \\\\frac{1}{10 - 0} = 0{,}1 \\\\quad (0 \\\\le x \\\\le 10)$$<br>" +
             "b) Xác suất trên khoảng con tỉ lệ thuận với độ dài của khoảng đó:<br>" +
             "   $$P(3 \\\\le X \\\\le 7) = \\\\frac{7 - 3}{b - a} = \\\\frac{4}{10} = 0{,}4 \\\\text{ (hay 40\\\\%)}$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 07 — Slide 50–53] Đặc trưng số học của Phân phối Đều",
        q: "Với thời gian chờ xe buýt $X \\\\sim U(0, 10)$ ở trên (Slide 50–53). Hãy tính kỳ vọng $E(X)$, phương sai $\\\\operatorname{Var}(X)$ và độ lệch chuẩn $\\\\operatorname{SD}(X)$.",
        sol: "<b>Lời giải chi tiết theo Slide Week 07 (trang 50):</b><br>" +
             "1. Kỳ vọng của phân phối đều nằm tại chính giữa đoạn $[a, b]$:<br>" +
             "   $$E(X) = \\\\frac{a + b}{2} = \\\\frac{0 + 10}{2} = 5 \\\\text{ phút}$$<br>" +
             "2. Phương sai tính theo công thức chuẩn giải tích:<br>" +
             "   $$\\\\operatorname{Var}(X) = \\\\frac{(b - a)^2}{12} = \\\\frac{(10 - 0)^2}{12} = \\\\frac{100}{12} = \\\\frac{25}{3} \\\\approx 8{,}3333 \\\\text{ phút}^2$$<br>" +
             "3. Độ lệch chuẩn:<br>" +
             "   $$\\\\operatorname{SD}(X) = \\\\sqrt{\\\\frac{25}{3}} = \\\\frac{5}{\\\\sqrt{3}} \\\\approx 2{,}8868 \\\\approx 2{,}887 \\\\text{ phút}$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 07 — Slide 51–53] Xác suất có điều kiện của Phân phối Đều",
        q: "Vẫn với thời gian xe buýt $X \\\\sim U(0, 10)$. Bạn đã đứng đợi tại bến xe được đúng 4 phút mà xe vẫn chưa tới ($X > 4$). Tính xác suất để xe buýt sẽ đến trong vòng 2 phút tiếp theo (tức $X \\\\le 6$).",
        sol: "<b>Lời giải xác suất có điều kiện theo Slide Week 07:</b><br>" +
             "1. Yêu cầu bài toán là tính $P(X \\\\le 6 \\\\mid X > 4)$, tức $P(4 < X \\\\le 6 \\\\mid X > 4)$.<br>" +
             "2. Theo công thức xác suất có điều kiện:<br>" +
             "   $$P(X \\\\le 6 \\\\mid X > 4) = \\\\frac{P(4 < X \\\\le 6)}{P(X > 4)}$$<br>" +
             "3. Ta có $P(4 < X \\\\le 6) = \\\\frac{6 - 4}{10} = \\\\frac{2}{10} = 0{,}2$, và $P(X > 4) = \\\\frac{10 - 4}{10} = \\\\frac{6}{10} = 0{,}6$.<br>" +
             "   $$P(X \\\\le 6 \\\\mid X > 4) = \\\\frac{0{,}2}{0{,}6} = \\\\frac{2}{6} = \\\\frac{1}{3} \\\\approx 0{,}3333 \\\\text{ (hay 33{,}33\\\\%)}$$"
      }
    ]"""

E4_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 07 — Ví dụ 15] Điểm thi và Chuẩn hóa Z-score",
        q: "Trong một kỳ thi, điểm số có phân phối chuẩn với trung bình $\\\\mu = 70$ và độ lệch chuẩn $\\\\sigma = 10$, tức $X \\\\sim N(70, 10^2)$ (Slide 57). Một sinh viên đạt 85 điểm.<br>" +
           "a) Tính điểm chuẩn hóa $Z$ của sinh viên này.<br>" +
           "b) Tra bảng hàm Laplace $\\\\Phi(z)$, tính tỉ lệ sinh viên có điểm số cao hơn sinh viên này.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 07 (trang 57):</b><br>" +
             "a) Công thức chuẩn hóa Z-score:<br>" +
             "   $$Z = \\\\frac{X - \\\\mu}{\\\\sigma} = \\\\frac{85 - 70}{10} = \\\\frac{15}{10} = 1{,}5$$<br>" +
             "b) Tra bảng phân phối chuẩn tắc: $\\\\Phi(1{,}5) = P(Z \\\\le 1{,}5) = 0{,}9332$.<br>" +
             "   Tỉ lệ sinh viên có điểm cao hơn sinh viên này là:<br>" +
             "   $$P(X > 85) = P(Z > 1{,}5) = 1 - \\\\Phi(1{,}5) = 1 - 0{,}9332 = 0{,}0668 \\\\text{ (hay 6{,}68\\\\%)}$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 07 — Ví dụ 16 & 17] Dung tích Đóng chai và Bài toán Phân vị",
        q: "Dung tích một chai nước giải khát (ml) được mô hình hóa bằng phân phối chuẩn $X \\\\sim N(500, 5^2)$ với $\\\\mu = 500$ ml và $\\\\sigma = 5$ ml (Slide 59, 61–62).<br>" +
           "a) Áp dụng quy tắc thực nghiệm 68–95–99.7: Xác định khoảng dung tích chứa 95% số chai.<br>" +
           "b) Tìm phân vị mức $p = 0{,}975$ (ngưỡng dung tích $x_0$ sao cho 97,5% số chai có dung tích không vượt quá $x_0$).",
        sol: "<b>Lời giải chi tiết theo Slide Week 07 (trang 59 & 61):</b><br>" +
             "a) Theo quy tắc thực nghiệm 68–95–99.7, khoảng $[\\\\mu - 2\\\\sigma, \\\\mu + 2\\\\sigma]$ chứa xấp xỉ 95% số quan sát:<br>" +
             "   $$[500 - 2(5), 500 + 2(5)] = [490, 510] \\\\text{ ml}$$<br>" +
             "b) Bài toán phân vị ngược:<br>" +
             "   Ta tìm $z_{0{,}975}$ sao cho $\\\\Phi(z_{0{,}975}) = 0{,}975$. Tra bảng chuẩn tắc được $z_{0{,}975} = 1{,}96$.<br>" +
             "   Chuyển ngược về đơn vị ban đầu:<br>" +
             "   $$x_0 = \\\\mu + z_{0{,}975} \\\\cdot \\\\sigma = 500 + 1{,}96 \\\\times 5 = 500 + 9{,}8 = 509{,}8 \\\\text{ ml}$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 07 — Bài tập 3] Bài toán Tải trọng Thang máy UET",
        q: "Khối lượng của người Việt Nam trưởng thành có phân phối chuẩn với trung bình $\\\\mu = 65$ kg và độ lệch chuẩn $\\\\sigma = 5$ kg (Slide 84–85). Một thang máy chở tối đa 10 người và có tải trọng giới hạn an toàn là 700 kg. Giả sử 10 người ngẫu nhiên bước vào thang máy có khối lượng độc lập. Tính xác suất thang máy bị quá tải.",
        sol: "<b>Lời giải chuẩn tự luận theo Slide Week 07 (trang 85):</b><br>" +
             "1. Gọi $X_i$ là khối lượng người thứ $i$ ($X_i \\\\sim N(65, 5^2)$ với $i=1, \\\\dots, 10$).<br>" +
             "   Tổng khối lượng của 10 người là $S_{10} = \\\\sum_{i=1}^{10} X_i$.<br>" +
             "2. Vì tổng của các biến chuẩn độc lập cũng là một biến chuẩn:<br>" +
             "   $$E(S_{10}) = 10 \\\\times \\\\mu = 10 \\\\times 65 = 650 \\\\text{ kg}$$<br>" +
             "   $$\\\\operatorname{Var}(S_{10}) = 10 \\\\times \\\\sigma^2 = 10 \\\\times 5^2 = 250 \\\\implies \\\\operatorname{SD}(S_{10}) = \\\\sqrt{250} = 5\\\\sqrt{10} \\\\approx 15{,}8114 \\\\text{ kg}$$<br>" +
             "   Do đó: $S_{10} \\\\sim N(650, 250)$.<br>" +
             "3. Thang máy quá tải khi $S_{10} > 700$ kg. Chuẩn hóa $Z$:<br>" +
             "   $$Z = \\\\frac{700 - 650}{\\\\sqrt{250}} = \\\\frac{50}{15{,}8114} \\\\approx 3{,}16$$<br>" +
             "   Tra bảng $\\\\Phi(3{,}16) = 0{,}9992$:<br>" +
             "   $$P(S_{10} > 700) = 1 - \\\\Phi(3{,}16) = 1 - 0{,}9992 = 0{,}0008 \\\\text{ (hay 0{,}08\\\\%)}$$<br>" +
             "   Xác suất quá tải cực kỳ nhỏ, thang máy hoạt động rất an toàn."
      }
    ]"""

E5_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 07 — Ví dụ 18] Thời gian chờ hệ thống nhận yêu cầu",
        q: "Thời gian chờ từ lúc bắt đầu theo dõi đến khi hệ thống nhận được yêu cầu có phân phối mũ với kỳ vọng $E(X) = 2$ phút (Slide 64–65).<br>" +
           "a) Xác định tham số tốc độ $\\\\lambda$.<br>" +
           "b) Tính xác suất để phải chờ nhiều hơn 3 phút mới nhận được yêu cầu.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 07 (trang 65):</b><br>" +
             "a) Với phân phối mũ $X \\\\sim Exp(\\\\lambda)$, kỳ vọng $E(X) = \\\\frac{1}{\\\\lambda}$:<br>" +
             "   $$\\\\lambda = \\\\frac{1}{E(X)} = \\\\frac{1}{2} = 0{,}5 \\\\text{ (mỗi phút)}$$<br>" +
             "b) Xác suất đuôi của phân phối mũ tính theo công thức trực tiếp $P(X > x) = e^{-\\\\lambda x}$:<br>" +
             "   $$P(X > 3) = e^{-0{,}5 \\\\times 3} = e^{-1{,}5} \\\\approx 0{,}2231 \\\\text{ (hay 22{,}31\\\\%)}$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 07 — Slide 63–65] Tính không nhớ (Memoryless Property)",
        q: "Vẫn với hệ thống ở trên ($X \\\\sim Exp(\\\\lambda = 0{,}5)$). Giả sử người quản trị đã chờ 4 phút mà hệ thống vẫn chưa nhận được yêu cầu nào ($X > 4$). Tính xác suất để phải chờ thêm ít nhất 3 phút nữa mới có yêu cầu đến (tức $X > 7$).",
        sol: "<b>Chứng minh tính chất không nhớ theo Slide Week 07:</b><br>" +
             "1. Theo công thức xác suất có điều kiện:<br>" +
             "   $$P(X > 4 + 3 \\\\mid X > 4) = \\\\frac{P(X > 7)}{P(X > 4)} = \\\\frac{e^{-0{,}5 \\\\times 7}}{e^{-0{,}5 \\\\times 4}} = \\\\frac{e^{-3{,}5}}{e^{-2{,}0}} = e^{-1{,}5} \\\\approx 0{,}2231$$<br>" +
             "2. Ta thấy $P(X > 4 + 3 \\\\mid X > 4) = P(X > 3)$.<br>" +
             "<b>Ý nghĩa:</b> Phân phối mũ 'không có trí nhớ' (Memoryless) — việc bạn đã mất công chờ 4 phút không hề làm tăng hay giảm cơ hội yêu cầu đến ở phút tiếp theo!"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 07 — Bài tập 4] Khoảng cách từ nơi ở đến trường",
        q: "Khoảng cách $X$ (km) từ nơi ở đến trường của một sinh viên có phân phối mũ với kỳ vọng $E(X) = 5$ km và độ lệch chuẩn $\\\\operatorname{SD}(X) = 5$ km (Slide 86–88).<br>" +
           "a) Xác định tham số $\\\\lambda$ và viết hàm mật độ $f(x)$.<br>" +
           "b) Tính xác suất một sinh viên sống cách trường trên 10 km.<br>" +
           "c) Nhận diện định tính đồ thị phân phối Chi-bình phương và $t$-Student (Slide 66–67).",
        sol: "<b>Lời giải theo Slide Week 07 (trang 87–88):</b><br>" +
             "a) Tham số tốc độ: $\\\\lambda = 1/E(X) = 1/5 = 0{,}2$. Hàm mật độ: $f(x) = 0{,}2 e^{-0{,}2 x}$ với $x \\\\ge 0$.<br>" +
             "b) Xác suất sinh viên sống cách trường trên 10 km:<br>" +
             "   $$P(X > 10) = e^{-0{,}2 \\\\times 10} = e^{-2} \\\\approx 0{,}1353 \\\\text{ (hay 13{,}53\\\\%)}$$<br>" +
             "c) Nhận diện theo Slide 66–67:<br>" +
             "   - <b>Phân phối Chi-bình phương ($\\\\chi^2$):</b> Luôn không âm ($x \\\\ge 0$), đồ thị lệch phải mạnh ở bậc tự do $\\\\nu$ nhỏ, dần đối xứng khi $\\\\nu$ lớn.<br>" +
             "   - <b>Phân phối $t$-Student:</b> Đối xứng hình chuông quanh 0 giống chuẩn tắc nhưng có <b>đuôi dày hơn</b> (Heavy-tailed); khi bậc tự do $\\\\nu \\\\to \\\\infty$, $t$-Student hội tụ về Chuẩn tắc $N(0, 1)$."
      }
    ]"""

E6_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 07 — Ví dụ 20] Thời gian Xử lý Yêu cầu qua Định lý CLT",
        q: "Thời gian xử lý một yêu cầu dịch vụ có trung bình $\\\\mu = 12$ phút và độ lệch chuẩn $\\\\sigma = 6$ phút (Slide 76–77). Một ca làm việc xử lý độc lập $n = 36$ yêu cầu. Gọi $S_{36}$ là tổng thời gian xử lý của cả ca.<br>" +
           "a) Xác định phân phối xấp xỉ của $S_{36}$ theo Định lý giới hạn trung tâm.<br>" +
           "b) Tính xác suất tổng thời gian xử lý không vượt quá 7,5 giờ (450 phút).",
        sol: "<b>Lời giải chi tiết theo Slide Week 07 (trang 77):</b><br>" +
             "a) Vì cỡ mẫu $n = 36 \\\\ge 30$, theo Định lý giới hạn trung tâm (CLT):<br>" +
             "   - $E(S_{36}) = n \\\\cdot \\\\mu = 36 \\\\times 12 = 432 \\\\text{ phút}$.<br>" +
             "   - $\\\\operatorname{SD}(S_{36}) = \\\\sigma \\\\sqrt{n} = 6 \\\\times \\\\sqrt{36} = 6 \\\\times 6 = 36 \\\\text{ phút}$.<br>" +
             "   Do đó: $S_{36} \\\\approx N(432, 36^2) = N(432, 1296)$.<br>" +
             "b) Chuẩn hóa biến $Z$ với ngưỡng 450 phút:<br>" +
             "   $$Z = \\\\frac{450 - 432}{36} = \\\\frac{18}{36} = 0{,}5$$<br>" +
             "   Tra bảng Laplace: $\\\\Phi(0{,}5) = 0{,}6915$.<br>" +
             "   $$P(S_{36} \\\\le 450) = P(Z \\\\le 0{,}5) = \\\\Phi(0{,}5) = 0{,}6915 \\\\text{ (hay 69{,}15\\\\%)}$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 07 — Bài tập 4 Ý 3] Khoảng cách Trung bình của 100 Sinh viên",
        q: "Khoảng cách từ nhà đến trường có phân phối mũ với $\\\\mu = 5$ km và $\\\\sigma = 5$ km (Slide 87). Khảo sát ngẫu nhiên $n = 100$ sinh viên. Dù phân phối gốc là phân phối mũ cực kỳ lệch phải, hãy áp dụng CLT để tính xác suất khoảng cách trung bình của 100 sinh viên nằm trong khoảng từ 4,5 km đến 5,5 km.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 07 (trang 87):</b><br>" +
             "1. Với cỡ mẫu lớn $n = 100$, theo CLT trung bình mẫu $\\\\bar{X}_{100}$ xấp xỉ phân phối Chuẩn:<br>" +
             "   - $E(\\\\bar{X}_{100}) = \\\\mu = 5 \\\\text{ km}$.<br>" +
             "   - $\\\\operatorname{SD}(\\\\bar{X}_{100}) = \\\\frac{\\\\sigma}{\\\\sqrt{n}} = \\\\frac{5}{\\\\sqrt{100}} = \\\\frac{5}{10} = 0{,}5 \\\\text{ km}$.<br>" +
             "   Suy ra: $\\\\bar{X}_{100} \\\\approx N(5, 0{,}5^2) = N(5, 0{,}25)$.<br>" +
             "2. Tính xác suất $P(4{,}5 \\\\le \\\\bar{X}_{100} \\\\le 5{,}5)$:<br>" +
             "   - Tại cận dưới: $z_1 = \\\\frac{4{,}5 - 5}{0{,}5} = -1{,}0$.<br>" +
             "   - Tại cận trên: $z_2 = \\\\frac{5{,}5 - 5}{0{,}5} = +1{,}0$.<br>" +
             "   $$P(4{,}5 \\\\le \\\\bar{X}_{100} \\\\le 5{,}5) = \\\\Phi(1{,}0) - \\\\Phi(-1{,}0) = 2\\\\Phi(1{,}0) - 1$$<br>" +
             "   Tra bảng $\\\\Phi(1{,}0) = 0{,}8413$:<br>" +
             "   $$P = 2(0{,}8413) - 1 = 1{,}6826 - 1 = 0{,}6826 \\\\text{ (hay 68{,}26\\\\%)}$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 07 — Bài tập 5] Bài toán Bóng đèn Dự phòng Phân loại 9–10 Điểm UET",
        q: "Một hệ thống cần một linh kiện thiết yếu để hoạt động liên tục (Slide 89–91). Khi linh kiện hỏng, một linh kiện dự phòng cùng loại sẽ được thay thế tức thì. Tuổi thọ mỗi linh kiện là biến ngẫu nhiên độc lập có trung bình $\\\\mu = 100$ giờ và độ lệch chuẩn $\\\\sigma = 30$ giờ (hoặc $\\\\sigma = 20$). Cần chuẩn bị tối thiểu bao nhiêu linh kiện $n$ để hệ thống hoạt động liên tục ít nhất $T = 2000$ giờ với xác suất không dưới 99% ($0{,}99$)?",
        sol: "<b>Lời giải kinh điển bằng Tam thức bậc hai theo Slide Week 07 (trang 90–91):</b><br>" +
             "1. Gọi $X_i$ là tuổi thọ linh kiện thứ $i$. Tổng thời gian hoạt động là $S_n = \\\\sum_{i=1}^n X_i$.<br>" +
             "   Theo CLT: $S_n \\\\approx N(n\\\\mu, n\\\\sigma^2) = N(100n, 900n) \\\\implies \\\\operatorname{SD}(S_n) = 30\\\\sqrt{n}$.<br>" +
             "2. Yêu cầu $P(S_n \\\\ge 2000) \\\\ge 0{,}99 \\\\iff P\\\\left(Z \\\\ge \\\\frac{2000 - 100n}{30\\\\sqrt{n}}\\\\right) \\\\ge 0{,}99$.<br>" +
             "   Tương đương: $\\\\frac{100n - 2000}{30\\\\sqrt{n}} \\\\ge z_{0{,}99} \\\\approx 2{,}3263$ (hoặc với $\\\\sigma=20$ thì mẫu số là $20\\\\sqrt{n}$).<br>" +
             "3. Nhân chéo chuyển vế, đặt ẩn phụ $u = \\\\sqrt{n} > 0$:<br>" +
             "   $$100u^2 - 69{,}789u - 2000 \\\\ge 0$$<br>" +
             "   Giải phương trình bậc hai: $\\\\Delta = (-69{,}789)^2 - 4(100)(-2000) = 4870{,}5 + 800000 = 804870{,}5 \\\\implies \\\\sqrt{\\\\Delta} \\\\approx 897{,}14$.<br>" +
             "   Nghiệm dương:<br>" +
             "   $$u \\\\ge \\\\frac{69{,}789 + 897{,}14}{200} = \\\\frac{966{,}93}{200} \\\\approx 4{,}835$$<br>" +
             "   Suy ra: $n = u^2 \\\\ge (4{,}835)^2 \\\\approx 23{,}38$.<br>" +
             "4. <b>Kết luận:</b> Vì $n$ nguyên nên bắt buộc phải làm tròn LÊN: <b>cần tối thiểu $n = 24$ linh kiện</b> (với $\\\\sigma=20$ nghiệm là $n = 23$ linh kiện)."
      }
    ]"""

# Replace in cum_e.js
for lid, ex_code in [("E1", E1_EXAMPLES), ("E2", E2_EXAMPLES), ("E3", E3_EXAMPLES), ("E4", E4_EXAMPLES), ("E5", E5_EXAMPLES), ("E6", E6_EXAMPLES)]:
    p = rf'(id:\s*["\']{lid}["\'][\s\S]*?examples:\s*\[)[\s\S]*?(\]\s*,\s*pitfalls:)'
    text = re.sub(p, lambda m, code=ex_code: m.group(1) + "\n" + code[16:-1] + "\n    " + m.group(2), text)

with open("content/cum_e.js", "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully upgraded content/cum_e.js with exact lecture examples!")
