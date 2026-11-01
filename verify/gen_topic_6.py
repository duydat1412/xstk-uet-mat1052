# Topic 6: Biến liên tục, Phân phối Đều, Mũ & Chuẩn (TL6_1 -> TL6_8)
import math
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_topic_6():
    exercises = []

    # TL6_1 (Cơ bản)
    exercises.append({
        "id": "TL6_1", "topicId": 6, "level": "Cơ bản",
        "title": "Hàm mật độ (pdf), Hàm phân phối (cdf) và Tính xác suất",
        "problem": "Cho biến ngẫu nhiên liên tục $X$ có hàm mật độ xác suất (pdf) xác định bởi:<br>"
                   "$$f(x) = \\begin{cases} k x^2 & \\text{khi } 0 \\le x \\le 3 \\\\ 0 & \\text{nơi khác} \\end{cases}$$"
                   "1. Tìm hằng số chuẩn hóa $k$ để $f(x)$ là một hàm mật độ xác suất hợp lệ.<br>"
                   "2. Xác định hàm phân phối tích lũy $F(x) = P(X \\le x)$ trên toàn bộ trục số thực $\\mathbb{R}$.<br>"
                   "3. Tính xác suất $P(1 \\le X \\le 2)$ bằng hai cách: (a) Dùng tích phân của $f(x)$; (b) Dùng hàm phân phối $F(x)$.",
        "analysis": "1. Integral_{-infty}^{+infty} f(x) dx = 1 => int_0^3 k*x^2 dx = k * 9 = 1 => k = 1/9. 2. F(x) = int_0^x (1/9) t^2 dt = x^3 / 27 tren [0, 3]. 3. P(1 <= X <= 2) = int_1^2 (1/9) x^2 dx = (8 - 1)/27 = 7/27 approx 0.2593. F(2) - F(1) = 8/27 - 1/27 = 7/27.",
        "hints": [
            "Điều kiện chuẩn hóa của hàm mật độ: Tích phân toàn phần bằng 1.",
            "Tích phân x^2 là x^3 / 3. Cận từ 0 đến 3 cho ra 27/3 = 9.",
            "F(x) = int_{-infty}^x f(t) dt. Với x in [0, 3]: F(x) = x^3 / 27."
        ],
        "steps": [
            "<b>Bước 1: Tìm hằng số chuẩn hóa k `[+0,35đ]`</b><br>"
            "Để $f(x)$ là một hàm mật độ xác suất hợp lệ, nó phải thỏa mãn điều kiện chuẩn hóa:<br>"
            "$$\\int_{-\\infty}^{+\\infty} f(x)\\, dx = 1 \\iff \\int_0^3 k x^2\\, dx = 1$$"
            "Tính tích phân:<br>"
            "$$k \\left[ \\frac{x^3}{3} \\right]_0^3 = k \\left( \\frac{27}{3} - 0 \\right) = 9k = 1 \\iff k = \\frac{1}{9}$$"
            "Vậy hàm mật độ là: $f(x) = \\frac{1}{9} x^2$ với $x \\in [0, 3]$.",
            "<b>Bước 2: Tìm hàm phân phối tích lũy F(x) `[+0,35đ]`</b><br>"
            "Theo định nghĩa: $F(x) = \\int_{-\\infty}^x f(t)\\, dt$:<br>"
            "- Khi $x < 0$: $F(x) = 0$.<br>"
            "- Khi $0 \\le x \\le 3$:<br>"
            "$$F(x) = \\int_0^x \\frac{1}{9} t^2\\, dt = \\left[ \\frac{t^3}{27} \\right]_0^x = \\frac{x^3}{27}$$"
            "- Khi $x > 3$: $F(x) = 1$.<br>"
            "Tóm lại:<br>"
            "$$F(x) = \\begin{cases} 0 & \\text{khi } x < 0 \\\\ \\frac{x^3}{27} & \\text{khi } 0 \\le x \\le 3 \\\\ 1 & \\text{khi } x > 3 \\end{cases}$$",
            "<b>Bước 3: Tính xác suất P(1 ≤ X ≤ 2) bằng 2 cách `[+0,30đ]`</b><br>"
            "- <b>Cách 1 (Dùng tích phân hàm mật độ):</b><br>"
            "$$P(1 \\le X \\le 2) = \\int_1^2 \\frac{1}{9} x^2\\, dx = \\left[ \\frac{x^3}{27} \\right]_1^2 = \\frac{2^3}{27} - \\frac{1^3}{27} = \\frac{8 - 1}{27} = \\frac{7}{27} \\approx 0{,}2593\\text{ (25{,}93\\%)}$$"
            "- <b>Cách 2 (Dùng hàm phân phối tích lũy):</b><br>"
            "$$P(1 \\le X \\le 2) = F(2) - F(1) = \\frac{2^3}{27} - \\frac{1^3}{27} = \\frac{8}{27} - \\frac{1}{27} = \\frac{7}{27} \\approx 0{,}2593$$"
        ],
        "pro_tips": "Đối với biến liên tục, xác suất tại 1 điểm đơn lẻ luôn bằng 0 ($P(X = c) = 0$), do đó $P(1 \\le X \\le 2) = P(1 < X < 2) = P(1 \\le X < 2) = P(1 < X \\le 2)$.",
        "pitfalls": "Quên định nghĩa từng khoảng của hàm $F(x)$ (chỉ viết mỗi công thức $x^3/27$ mà bỏ qua $x < 0$ và $x > 3$)."
    })

    # TL6_2 (Cơ bản)
    exercises.append({
        "id": "TL6_2", "topicId": 6, "level": "Cơ bản",
        "title": "Phân phối Đều U(a, b): Hàm mật độ, Kỳ vọng, Phương sai và Xác suất điều kiện",
        "problem": "Cho biến ngẫu nhiên liên tục $X$ có phân phối đều trên đoạn $[2, 8]$, ký hiệu $X \\sim U(2, 8)$.<br>"
                   "1. Viết hàm mật độ xác suất $f(x)$ và hàm phân phối tích lũy $F(x)$.<br>"
                   "2. Tính kỳ vọng $E(X)$, phương sai $\\operatorname{Var}(X)$ và độ lệch chuẩn $\\operatorname{SD}(X)$.<br>"
                   "3. Tính xác suất $P(3 \\le X \\le 6)$ và xác suất có điều kiện $P(X > 5 \\mid X > 3)$.",
        "analysis": "X ~ U(a=2, b=8). f(x) = 1/(8-2) = 1/6 tren [2, 8]. F(x) = (x-2)/6. E(X) = (2+8)/2 = 5. Var(X) = (8-2)^2 / 12 = 36/12 = 3. SD(X) = sqrt(3) approx 1.7321. P(3 <= X <= 6) = (6-3)/6 = 3/6 = 0.5. P(X > 5 | X > 3) = P(X > 5) / P(X > 3) = [(8-5)/6] / [(8-3)/6] = 3/5 = 0.6.",
        "hints": [
            "Độ dài khoảng b - a = 8 - 2 = 6. f(x) = 1/6.",
            "E(X) = (a + b) / 2 = 5. Var(X) = (b - a)^2 / 12 = 36 / 12 = 3.",
            "P(X > 5 | X > 3) = (8 - 5) / (8 - 3) = 3 / 5."
        ],
        "steps": [
            "<b>Bước 1: Viết hàm mật độ f(x) và hàm phân phối F(x) `[+0,30đ]`</b><br>"
            "Với $a = 2, b = 8$, độ dài đoạn là $b - a = 8 - 2 = 6$.<br>"
            "- Hàm mật độ:<br>"
            "$$f(x) = \\begin{cases} \\frac{1}{b - a} = \\frac{1}{6} & \\text{khi } 2 \\le x \\le 8 \\\\ 0 & \\text{nơi khác} \\end{cases}$$"
            "- Hàm phân phối tích lũy:<br>"
            "$$F(x) = \\begin{cases} 0 & \\text{khi } x < 2 \\\\ \\frac{x - 2}{6} & \\text{khi } 2 \\le x \\le 8 \\\\ 1 & \\text{khi } x > 8 \\end{cases}$$",
            "<b>Bước 2: Tính kỳ vọng, phương sai và độ lệch chuẩn `[+0,35đ]`</b><br>"
            "- Kỳ vọng (trung điểm của khoảng):<br>"
            "$$E(X) = \\frac{a + b}{2} = \\frac{2 + 8}{2} = 5{,}0$$"
            "- Phương sai:<br>"
            "$$\\operatorname{Var}(X) = \\frac{(b - a)^2}{12} = \\frac{(8 - 2)^2}{12} = \\frac{36}{12} = 3{,}0$$"
            "- Độ lệch chuẩn:<br>"
            "$$\\operatorname{SD}(X) = \\sqrt{3{,}0} \\approx 1{,}7321$$",
            "<b>Bước 3: Tính xác suất thường và xác suất có điều kiện `[+0,35đ]`</b><br>"
            "- Xác suất $P(3 \\le X \\le 6)$ bằng tỉ số độ dài hình chữ nhật:<br>"
            "$$P(3 \\le X \\le 6) = \\frac{6 - 3}{8 - 2} = \\frac{3}{6} = 0{,}50\\text{ (50\\%)}$$"
            "- Xác suất có điều kiện $P(X > 5 \\mid X > 3)$:<br>"
            "Vì biến cố $X > 5$ là tập con của $X > 3$ (tức $(5, 8] \\cap (3, 8] = (5, 8]$):<br>"
            "$$P(X > 5 \\mid X > 3) = \\frac{P(X > 5 \\cap X > 3)}{P(X > 3)} = \\frac{P(X > 5)}{P(X > 3)} = \\frac{\\frac{8 - 5}{6}}{\\frac{8 - 3}{6}} = \\frac{3}{5} = 0{,}60\\text{ (60\\%)}$$"
        ],
        "pro_tips": "Đối với phân phối đều, xác suất có điều kiện chỉ đơn giản là tỉ số độ dài hình học: $\\frac{8 - 5}{8 - 3} = \\frac{3}{5} = 0{,}60$!",
        "pitfalls": "Quên chia cho 12 ở mẫu số của phương sai $\\operatorname{Var}(X) = \\frac{(b-a)^2}{12}$."
    })

    # TL6_3 (Cơ bản)
    exercises.append({
        "id": "TL6_3", "topicId": 6, "level": "Cơ bản",
        "title": "Phân phối Chuẩn N(μ, σ²): Chuẩn hóa Z-score và Tra bảng",
        "problem": "Điểm thi kết thúc học phần môn Xác suất thống kê của sinh viên có phân phối chuẩn với điểm trung bình $\\mu = 60$ điểm và độ lệch chuẩn $\\sigma = 10$ điểm ($X \\sim N(60,\\; 10^2)$). Cho biết: $\\Phi(1{,}5) \\approx 0{,}9332$; $\\Phi(1{,}0) \\approx 0{,}8413$; $\\Phi(2{,}0) \\approx 0{,}9772$.<br>"
                   "1. Tính tỉ lệ sinh viên đạt điểm Giỏi từ 75 điểm trở lên ($P(X \\ge 75)$).<br>"
                   "2. Tính tỉ lệ sinh viên đạt điểm trong khoảng từ 50 đến 70 điểm ($P(50 \\le X \\le 70)$).<br>"
                   "3. Tính tỉ lệ sinh viên thi không đạt (dưới 40 điểm: $P(X < 40)$).",
        "analysis": "Z = (X - 60)/10. 1. X >= 75 => Z >= (75-60)/10 = 1.5 => 1 - Phi(1.5) = 1 - 0.9332 = 0.0668 (6.68%). 2. 50 <= X <= 70 => -1 <= Z <= 1 => Phi(1) - Phi(-1) = 2*Phi(1) - 1 = 2(0.8413) - 1 = 0.6826 (68.26%). 3. X < 40 => Z < -2 => Phi(-2) = 1 - Phi(2) = 1 - 0.9772 = 0.0228 (2.28%).",
        "hints": [
            "Công thức chuẩn hóa: Z = (X - mu) / sigma.",
            "P(X >= 75) = P(Z >= 1.5) = 1 - Phi(1.5).",
            "Tính chất đối xứng: Phi(-z) = 1 - Phi(z)."
        ],
        "steps": [
            "<b>Bước 1: Tính tỉ lệ sinh viên đạt từ 75 điểm trở lên `[+0,35đ]`</b><br>"
            "Chuẩn hóa biến ngẫu nhiên $X$ về biến chuẩn tắc $Z = \\frac{X - \\mu}{\\sigma} = \\frac{X - 60}{10} \\sim N(0, 1)$:<br>"
            "Tại $X = 75$: $Z = \\frac{75 - 60}{10} = 1{,}5$.<br>"
            "$$P(X \\ge 75) = P(Z \\ge 1{,}5) = 1 - \\Phi(1{,}5)$$"
            "Tra bảng: $\\Phi(1{,}5) \\approx 0{,}9332$:<br>"
            "$$P(X \\ge 75) = 1 - 0{,}9332 = 0{,}0668\\text{ (6{,}68\\%)}$$",
            "<b>Bước 2: Tính tỉ lệ sinh viên đạt điểm trong khoảng [50; 70] `[+0,35đ]`</b><br>"
            "Chuẩn hóa 2 đầu mút:<br>"
            "- Tại $X = 50$: $Z_1 = \\frac{50 - 60}{10} = -1{,}0$.<br>"
            "- Tại $X = 70$: $Z_2 = \\frac{70 - 60}{10} = +1{,}0$.<br>"
            "$$P(50 \\le X \\le 70) = P(-1{,}0 \\le Z \\le 1{,}0) = \\Phi(1{,}0) - \\Phi(-1{,}0)$$"
            "Áp dụng tính chất đối xứng $\\Phi(-z) = 1 - \\Phi(z)$:<br>"
            "$$\\Phi(1{,}0) - [1 - \\Phi(1{,}0)] = 2\\Phi(1{,}0) - 1 = 2(0{,}8413) - 1 = 1{,}6826 - 1 = 0{,}6826\\text{ (68{,}26\\%)}$$"
            "<i>(Đây chính là quy tắc kinh nghiệm 68% cho khoảng 1 độ lệch chuẩn [mu - sigma, mu + sigma]!).</i>",
            "<b>Bước 3: Tính tỉ lệ sinh viên dưới 40 điểm `[+0,30đ]`</b><br>"
            "Tại $X = 40$: $Z = \\frac{40 - 60}{10} = -2{,}0$.<br>"
            "$$P(X < 40) = P(Z < -2{,}0) = \\Phi(-2{,}0) = 1 - \\Phi(2{,}0)$$"
            "Tra bảng: $\\Phi(2{,}0) \\approx 0{,}9772$:<br>"
            "$$P(X < 40) = 1 - 0{,}9772 = 0{,}0228\\text{ (2{,}28\\%)}$$"
        ],
        "pro_tips": "Thuộc lòng 3 con số đối xứng vàng: $P(-1 \\le Z \\le 1) \\approx 68{,}26\\%$, $P(-2 \\le Z \\le 2) \\approx 95{,}44\\%$, $P(-3 \\le Z \\le 3) \\approx 99{,}73\\%$.",
        "pitfalls": "Quên đổi chiều đối xứng: tính $\\Phi(-2) = -\\Phi(2)$ (sai nghiêm trọng, xác suất không thể âm; đúng là $1 - \\Phi(2)$)."
    })

    # TL6_4 (Trung bình)
    exercises.append({
        "id": "TL6_4", "topicId": 6, "level": "Trung bình",
        "title": "Phân vị chuẩn và Bài toán xác định ngưỡng điểm (Quantile Cutoff)",
        "problem": "Điểm thi TOEIC của sinh viên một trường đại học tuân theo phân phối chuẩn với trung bình $\\mu = 500$ điểm và độ lệch chuẩn $\\sigma = 100$ điểm ($X \\sim N(500,\\; 100^2)$). Cho biết giá trị phân vị chuẩn: $\\Phi(1{,}645) \\approx 0{,}9500$; $\\Phi(1{,}50) \\approx 0{,}9332$.<br>"
                   "1. Nhà trường muốn trao học bổng cho Top $5\\%$ sinh viên có điểm thi cao nhất trường. Hãy xác định mức điểm chuẩn tối thiểu để được nhận học bổng ($x^*$).<br>"
                   "2. Xác định tỉ lệ sinh viên đạt điểm từ mức trung vị (500 điểm) đến dưới 650 điểm.",
        "analysis": "1. Top 5% cao nhat <=> P(X >= x*) = 0.05 <=> P(X <= x*) = 0.95. Chuẩn hóa Z* = (x* - 500)/100 = 1.645 => x* = 500 + 1.645 * 100 = 664.5 điểm. 2. P(500 <= X < 650): Tại 500 có Z1 = 0 (Phi(0) = 0.5). Tại 650 có Z2 = (650-500)/100 = 1.5. P = Phi(1.5) - Phi(0) = 0.9332 - 0.5000 = 0.4332 (43.32%).",
        "hints": [
            "Top 5% cao nhất nghĩa là có 95% sinh viên có điểm thấp hơn ngưỡng này: Phi(Z*) = 0.95.",
            "Tra ngược bảng chuẩn: Phi(1.645) = 0.95 -> Z* = 1.645.",
            "x* = mu + Z* * sigma."
        ],
        "steps": [
            "<b>Bước 1: Thiết lập phương trình tìm ngưỡng điểm Top 5% `[+0,35đ]`</b><br>"
            "Gọi $x^*$ là mức điểm tối thiểu để lọt vào Top 5% sinh viên cao nhất.<br>"
            "Biến cố sinh viên thuộc Top 5% tương ứng với:<br>"
            "$$P(X \\ge x^*) = 0{,}05 \\iff P(X < x^*) = 1 - 0{,}05 = 0{,}95$$"
            "Chuẩn hóa phương trình:<br>"
            "$$P\\left( Z < \\frac{x^* - 500}{100} \\right) = \\Phi\\left( \\frac{x^* - 500}{100} \\right) = 0{,}95$$",
            "<b>Bước 2: Tra bảng chuẩn tắc ngược và tính ngưỡng x* `[+0,35đ]`</b><br>"
            "Tra bảng phân phối chuẩn tắc ngược với xác suất tích lũy $p = 0{,}95$, ta được giá trị phân vị $Z_{0{,}95}$:<br>"
            "$$Z^* = 1{,}645$$"
            "Do đó:<br>"
            "$$\\frac{x^* - 500}{100} = 1{,}645 \\iff x^* = 500 + 1{,}645 \\times 100 = 500 + 164{,}5 = 664{,}5\\text{ (điểm)}$$"
            "<b>Kết luận:</b> Sinh viên cần đạt tối thiểu <b>664,5 điểm</b> (hoặc từ 665 điểm nếu làm tròn số nguyên) để lọt vào Top 5% nhận học bổng.",
            "<b>Bước 3: Tính tỉ lệ sinh viên đạt từ 500 đến dưới 650 điểm `[+0,30đ]`</b><br>"
            "Chuẩn hóa khoảng $[500;\\; 650)$:<br>"
            "- Tại $X = 500$: $Z_1 = \\frac{500 - 500}{100} = 0{,}00$.<br>"
            "- Tại $X = 650$: $Z_2 = \\frac{650 - 500}{100} = 1{,}50$.<br>"
            "Xác suất cần tính:<br>"
            "$$P(500 \\le X < 650) = \\Phi(1{,}50) - \\Phi(0{,}00)$$"
            "Vì phân phối chuẩn đối xứng nên $\\Phi(0{,}00) = 0{,}5000$. Đề bài cho $\\Phi(1{,}50) \\approx 0{,}9332$:<br>"
            "$$P(500 \\le X < 650) = 0{,}9332 - 0{,}5000 = 0{,}4332\\text{ (43{,}32\\%)}$$"
        ],
        "pro_tips": "Nhớ công thức chuyển đổi 2 chiều: Từ $X$ sang $Z$: $Z = \\frac{X - \\mu}{\\sigma}$; Từ $Z$ ngược lại $X$: $X = \\mu + Z \\cdot \\sigma$.",
        "pitfalls": "Tra nhầm $Z = 0{,}05$ hoặc nhầm Top 5% là diện tích $5\\%$ bên trái thay vì bên phải."
    })

    # TL6_5 (Trung bình)
    exercises.append({
        "id": "TL6_5", "topicId": 6, "level": "Trung bình",
        "title": "Phân phối Mũ Exp(λ) và Tính chất không nhớ (Memoryless)",
        "problem": "Thời gian phục vụ một khách hàng tại quầy giao dịch là biến ngẫu nhiên liên tục $T$ tuân theo phân phối mũ với thời gian phục vụ trung bình là 5 phút ($E(T) = 5$ phút, tức $\\lambda = 1/5 = 0{,}2$ phút$^{-1}$).<br>"
                   "1. Viết hàm mật độ xác suất $f(t)$ và hàm phân phối tích lũy $F(t)$ của $T$.<br>"
                   "2. Tính xác suất một khách hàng được phục vụ xong trong vòng 3 phút đầu tiên ($P(T \\le 3)$).<br>"
                   "3. Biết một khách hàng đã được phục vụ suốt 4 phút mà vẫn chưa xong. Tính xác suất khách hàng này phải phục vụ thêm ít nhất 3 phút nữa ($P(T > 7 \\mid T > 4)$) và giải thích tính chất không nhớ.",
        "analysis": "T ~ Exp(lambda=0.2). f(t) = 0.2*e^(-0.2*t) for t >= 0. F(t) = 1 - e^(-0.2*t). P(T <= 3) = 1 - e^(-0.6) = 1 - 0.54881 = 0.4512. P(T > 7 | T > 4) = P(T > 4+3 | T > 4) = P(T > 3) = e^(-0.2*3) = e^(-0.6) = 0.5488.",
        "hints": [
            "Thời gian trung bình 1/lambda = 5 phút -> lambda = 0.2.",
            "P(T <= 3) = 1 - e^(-lambda * 3) = 1 - e^(-0.6).",
            "Tính chất không nhớ: P(T > s + t | T > s) = P(T > t) = e^(-lambda * t)."
        ],
        "steps": [
            "<b>Bước 1: Xác định hàm mật độ f(t) và hàm phân phối F(t) `[+0,30đ]`</b><br>"
            "Tham số tỉ lệ (rate): $\\lambda = \\frac{1}{E(T)} = \\frac{1}{5} = 0{,}2\\text{ (phút}^{-1}\\text{)}$.<br>"
            "- Hàm mật độ xác suất:<br>"
            "$$f(t) = \\begin{cases} 0{,}2 e^{-0{,}2 t} & \\text{khi } t \\ge 0 \\\\ 0 & \\text{khi } t < 0 \\end{cases}$$"
            "- Hàm phân phối tích lũy:<br>"
            "$$F(t) = P(T \\le t) = 1 - e^{-0{,}2 t}\\quad (t \\ge 0)$$",
            "<b>Bước 2: Tính xác suất phục vụ xong trong 3 phút đầu P(T ≤ 3) `[+0,35đ]`</b><br>"
            "Thay $t = 3$ vào hàm phân phối tích lũy:<br>"
            "$$P(T \\le 3) = F(3) = 1 - e^{-0{,}2 \\times 3} = 1 - e^{-0{,}6}$$"
            "Với $e^{-0{,}6} \\approx 0{,}54881$:<br>"
            "$$P(T \\le 3) = 1 - 0{,}54881 = 0{,}45119 \\approx 0{,}4512\\text{ (45{,}12\\%)}$$",
            "<b>Bước 3: Tính xác suất điều kiện và Giải thích tính chất không nhớ `[+0,35đ]`</b><br>"
            "Theo định nghĩa xác suất có điều kiện:<br>"
            "$$P(T > 7 \\mid T > 4) = \\frac{P(T > 7 \\cap T > 4)}{P(T > 4)} = \\frac{P(T > 7)}{P(T > 4)}$$"
            "Với phân phối mũ: $P(T > t) = 1 - F(t) = e^{-\\lambda t}$:<br>"
            "$$P(T > 7 \\mid T > 4) = \\frac{e^{-0{,}2 \\times 7}}{e^{-0{,}2 \\times 4}} = \\frac{e^{-1{,}4}}{e^{-0{,}8}} = e^{-1{,}4 - (-0{,}8)} = e^{-0{,}6} = P(T > 3) \\approx 0{,}5488\\text{ (54{,}88\\%)}$$<br>"
            "<b>Giải thích tính chất không nhớ (Memoryless Property):</b> Phân phối Mũ là phân phối liên tục DUY NHẤT có tính chất không có bộ nhớ: Quá khứ đã chờ bao lâu ($s = 4$ phút) hoàn toàn không ảnh hưởng đến xác suất phải chờ thêm trong tương lai ($t = 3$ phút nữa). Hệ thống 'quên sạch' thời gian đã trôi qua!"
        ],
        "pro_tips": "Công thức ghi nhớ nhanh: $P(T > s + t \\mid T > s) = P(T > t) = e^{-\\lambda t}$.",
        "pitfalls": "Tính nhầm $P(T > 7 \\mid T > 4) = P(T > 7) - P(T > 4)$ (sai công thức xác suất có điều kiện)."
    })

    # TL6_6 (Trung bình)
    exercises.append({
        "id": "TL6_6", "topicId": 6, "level": "Trung bình",
        "title": "Quy tắc kinh nghiệm 68–95–99,7% và Kiểm soát chất lượng (Quality Control)",
        "problem": "Một dây chuyền đóng lon nước ngọt tự động rót thể tích nước vào mỗi lon tuân theo phân phối chuẩn với trung bình $\\mu = 330\\text{ ml}$ và độ lệch chuẩn $\\sigma = 2\\text{ ml}$ ($X \\sim N(330,\\; 2^2)$).<br>"
                   "1. Sử dụng <b>Quy tắc kinh nghiệm 68–95–99,7%</b>, hãy xác định các khoảng dung tích tương ứng chứa $68\\%$, $95\\%$ và $99{,}7\\%$ số lon nước sản xuất ra.<br>"
                   "2. Một lon nước bị coi là 'Lỗi nghiêm trọng' nếu dung tích dưới $324\\text{ ml}$ (quá thiếu) hoặc trên $336\\text{ ml}$ (quá tràn). Hãy tính tỉ lệ các lon nước bị lỗi nghiêm trọng.",
        "analysis": "1. [mu - sigma, mu + sigma] = [328, 332] (68%). [mu - 2*sigma, mu + 2*sigma] = [326, 334] (95%). [mu - 3*sigma, mu + 3*sigma] = [324, 336] (99.7%). 2. Loi nghiem trong la ngoai khoang 3 sigma => 1 - 0.997 = 0.003 (0.3% hay 3 lon / 1000 lon).",
        "hints": [
            "Khoảng 68%: mu +- 1*sigma. Khoảng 95%: mu +- 2*sigma. Khoảng 99.7%: mu +- 3*sigma.",
            "324 = 330 - 3*2 = mu - 3*sigma; 336 = 330 + 3*2 = mu + 3*sigma.",
            "Lỗi nghiêm trọng là phần đuôi nằm ngoài [mu - 3*sigma, mu + 3*sigma]."
        ],
        "steps": [
            "<b>Bước 1: Xác định các khoảng dung tích theo Quy tắc 68–95–99,7% `[+0,50đ]`</b><br>"
            "Với $\\mu = 330\\text{ ml}$ và $\\sigma = 2\\text{ ml}$:<br>"
            "- <b>Khoảng chứa xấp xỉ 68% số lon</b> ($[\\mu - \\sigma;\\; \\mu + \\sigma]$):<br>"
            "$$[330 - 2;\\; 330 + 2] = [328\\text{ ml};\\; 332\\text{ ml}]$$"
            "- <b>Khoảng chứa xấp xỉ 95% số lon</b> ($[\\mu - 2\\sigma;\\; \\mu + 2\\sigma]$):<br>"
            "$$[330 - 2(2);\\; 330 + 2(2)] = [330 - 4;\\; 330 + 4] = [326\\text{ ml};\\; 334\\text{ ml}]$$"
            "- <b>Khoảng chứa xấp xỉ 99,7% số lon</b> ($[\\mu - 3\\sigma;\\; \\mu + 3\\sigma]$):<br>"
            "$$[330 - 3(2);\\; 330 + 3(2)] = [330 - 6;\\; 330 + 6] = [324\\text{ ml};\\; 336\\text{ ml}]$$",
            "<b>Bước 2: Tính tỉ lệ các lon nước bị lỗi nghiêm trọng `[+0,50đ]`</b><br>"
            "Khoảng dung tích đạt chuẩn an toàn là $[324\\text{ ml};\\; 336\\text{ ml}]$, tương ứng với khoảng 3 độ lệch chuẩn quanh giá trị trung bình $[\\mu - 3\\sigma;\\; \\mu + 3\\sigma]$.<br>"
            "Theo Quy tắc kinh nghiệm:<br>"
            "$$P(324 \\le X \\le 336) \\approx 0{,}997\\text{ (99{,}7\\%)}$$"
            "Biến cố lon bị lỗi nghiêm trọng (quá thiếu $X < 324$ hoặc quá tràn $X > 336$) chính là phần bù nằm ngoài khoảng 3 độ lệch chuẩn:<br>"
            "$$P(\\text{Lỗi nghiêm trọng}) = P(X < 324) + P(X > 336) = 1 - P(324 \\le X \\le 336)$$"
            "$$P(\\text{Lỗi nghiêm trọng}) \\approx 1 - 0{,}997 = 0{,}003\\text{ (0{,}3\\%)}$$"
            "<b>Kết luận:</b> Trung bình trong 1000 lon nước sản xuất ra chỉ có khoảng 3 lon bị lỗi nghiêm trọng."
        ],
        "pro_tips": "Do tính đối xứng, tỉ lệ lon quá thiếu là $0{,}3\\% / 2 = 0{,}15\\%$, và tỉ lệ lon quá tràn cũng là $0{,}15\\%$.",
        "pitfalls": "Nhầm $\\mu \\pm 2\\sigma$ với $\\mu \\pm 3\\sigma$."
    })

    # TL6_7 (Nâng cao)
    exercises.append({
        "id": "TL6_7", "topicId": 6, "level": "Nâng cao",
        "title": "Chính sách bảo hành sản phẩm: Tối ưu hóa thời hạn bảo hành",
        "problem": "Tuổi thọ của một dòng màn hình máy tính cao cấp tuân theo phân phối chuẩn với tuổi thọ trung bình là $\\mu = 1000$ ngày và độ lệch chuẩn $\\sigma = 100$ ngày ($T \\sim N(1000,\\; 100^2)$). Cho biết: $\\Phi(-2{,}054) \\approx 0{,}0200$; $\\Phi(-2{,}00) \\approx 0{,}0228$.<br>"
                   "1. Nếu nhà sản xuất áp dụng thời hạn bảo hành là $T_0 = 800$ ngày, hãy tính tỉ lệ sản phẩm bán ra bị hỏng trong thời gian bảo hành và phải chịu trách nhiệm sửa chữa miễn phí.<br>"
                   "2. Để tối ưu hóa chi phí bảo hành, ban giám đốc yêu cầu quy định thời hạn bảo hành $T^*$ sao cho có <b>tối đa $2\\%$</b> ($0{,}02$) số sản phẩm bị lỗi trong thời gian bảo hành. Hãy tìm thời hạn bảo hành tối đa $T^*$ mà hãng nên công bố.",
        "analysis": "1. P(T <= 800): Z = (800 - 1000)/100 = -2.0 => Phi(-2.0) = 1 - Phi(2.0) = 0.0228 (2.28%). 2. P(T <= T*) = 0.02 => Z = (T* - 1000)/100 = -2.054 => T* = 1000 - 2.054 * 100 = 794.6 ngày (khoảng 794 ngày).",
        "hints": [
            "Sản phẩm hỏng trong bảo hành khi Tuổi thọ T <= Thời hạn bảo hành T0.",
            "Tại T0 = 800: Z = (800 - 1000) / 100 = -2.0.",
            "Muốn P(T <= T*) = 0.02 -> tra ngược Z có tích lũy 0.02 -> Z = -2.054."
        ],
        "steps": [
            "<b>Bước 1: Tính tỉ lệ sản phẩm hỏng với thời hạn bảo hành 800 ngày `[+0,40đ]`</b><br>"
            "Sản phẩm bị hỏng trong thời gian bảo hành nếu tuổi thọ $T \\le 800$ ngày.<br>"
            "Chuẩn hóa giá trị 800 ngày:<br>"
            "$$Z = \\frac{800 - \\mu}{\\sigma} = \\frac{800 - 1000}{100} = \\frac{-200}{100} = -2{,}0$$"
            "Xác suất sản phẩm phải bảo hành là:<br>"
            "$$P(T \\le 800) = \\Phi(-2{,}0) \\approx 0{,}0228\\text{ (2{,}28\\%)}$$"
            "Vậy nếu bảo hành 800 ngày, hãng sẽ phải bảo hành cho khoảng $2{,}28\\%$ tổng số màn hình bán ra.",
            "<b>Bước 2: Thiết lập phương trình tìm thời hạn bảo hành tối đa T* `[+0,35đ]`</b><br>"
            "Hãng yêu cầu tỉ lệ bảo hành không vượt quá $2\\%$:<br>"
            "$$P(T \\le T^*) \\le 0{,}02$$"
            "Chuẩn hóa biến số:<br>"
            "$$P\\left( Z \\le \\frac{T^* - 1000}{100} \\right) = \\Phi\\left( \\frac{T^* - 1000}{100} \\right) \\le 0{,}02$$",
            "<b>Bước 3: Tra bảng chuẩn tắc ngược và kết luận `[+0,25đ]`</b><br>"
            "Tra bảng chuẩn tắc với xác suất tích lũy $p = 0{,}02$:<br>"
            "$$Z_{0{,}02} \\approx -2{,}054$$"
            "Do đó:<br>"
            "$$\\frac{T^* - 1000}{100} = -2{,}054 \\iff T^* = 1000 - 2{,}054 \\times 100 = 1000 - 205{,}4 = 794{,}6\\text{ (ngày)}$$"
            "<b>Kết luận:</b> Hãng nên công bố thời hạn bảo hành tối đa là <b>794 ngày</b> (khoảng 2 năm 2 tháng) để đảm bảo tỉ lệ màn hình hỏng phải bảo hành không vượt quá $2\\%$."
        ],
        "pro_tips": "Vì xác suất $0{,}02 < 0{,}5$, giá trị $Z$ chắc chắn phải mang dấu âm ($Z < 0$).",
        "pitfalls": "Quên dấu trừ khi tìm $Z$ dẫn đến thời hạn bảo hành $> 1000$ ngày (sai thực tế)."
    })

    # TL6_8 (Nâng cao)
    exercises.append({
        "id": "TL6_8", "topicId": 6, "level": "Nâng cao",
        "title": "Định lý LOTUS và Biến đổi biến ngẫu nhiên liên tục",
        "problem": "Cho biến ngẫu nhiên liên tục $X$ có phân phối đều trên đoạn $[0, 2]$, tức $X \\sim U(0, 2)$.<br>"
                   "1. Sử dụng <b>Định lý thống kê viên vô thức (LOTUS)</b>, hãy tính kỳ vọng $E(X^2)$ và $E(e^X)$.<br>"
                   "2. Đặt biến ngẫu nhiên mới $Y = X^2$. Hãy tìm hàm phân phối tích lũy $F_Y(y)$ và hàm mật độ xác suất $f_Y(y)$ của $Y$.<br>"
                   "3. Dùng hàm mật độ $f_Y(y)$ vừa tìm được để tính lại kỳ vọng $E(Y)$ và đối chiếu với câu 1.",
        "analysis": "1. f_X(x) = 1/2 tren [0, 2]. E(X^2) = int_0^2 x^2 (1/2) dx = (1/2) [8/3] = 4/3. E(e^X) = int_0^2 e^x (1/2) dx = (1/2)(e^2 - 1). 2. Y = X^2 in [0, 4]. F_Y(y) = P(X^2 <= y) = P(X <= sqrt(y)) = F_X(sqrt(y)) = sqrt(y)/2. f_Y(y) = F'_Y(y) = 1 / (4*sqrt(y)) tren [0, 4]. 3. E(Y) = int_0^4 y * (1/(4*sqrt(y))) dy = (1/4) int_0^4 y^(1/2) dy = (1/4) [ (2/3) y^(3/2) ]_0^4 = (1/4) * (2/3) * 8 = 4/3. Kết quả trùng khớp hoàn hảo!",
        "hints": [
            "Hàm mật độ của X là f_X(x) = 1/2 trên [0, 2].",
            "Định lý LOTUS: E(g(X)) = int g(x) * f_X(x) dx.",
            "F_Y(y) = P(Y <= y) = P(X^2 <= y) = P(X <= sqrt(y)) vì X >= 0."
        ],
        "steps": [
            "<b>Bước 1: Tính E(X²) và E(eˣ) bằng Định lý LOTUS `[+0,35đ]`</b><br>"
            "Hàm mật độ của $X \\sim U(0, 2)$ là $f_X(x) = \\frac{1}{2}$ với $x \\in [0, 2]$.<br>"
            "Áp dụng Định lý LOTUS: $E(g(X)) = \\int_{-\\infty}^{+\\infty} g(x) f_X(x)\\, dx$:<br>"
            "- Tính $E(X^2)$:<br>"
            "$$E(X^2) = \\int_0^2 x^2 \\cdot \\frac{1}{2}\\, dx = \\frac{1}{2} \\left[ \\frac{x^3}{3} \\right]_0^2 = \\frac{1}{2} \\times \\frac{8}{3} = \\frac{4}{3} \\approx 1{,}3333$$"
            "- Tính $E(e^X)$:<br>"
            "$$E(e^X) = \\int_0^2 e^x \\cdot \\frac{1}{2}\\, dx = \\frac{1}{2} \\left[ e^x \\right]_0^2 = \\frac{e^2 - 1}{2} \\approx \\frac{7{,}389 - 1}{2} \\approx 3{,}1945$$",
            "<b>Bước 2: Tìm hàm phân phối tích lũy và hàm mật độ của Y = X² `[+0,35đ]`</b><br>"
            "Vì $X \\in [0, 2]$ nên $Y = X^2 \\in [0, 4]$.<br>"
            "Với mọi $y \\in [0, 4]$, hàm phân phối tích lũy của $Y$ là:<br>"
            "$$F_Y(y) = P(Y \\le y) = P(X^2 \\le y) = P(-\\sqrt{y} \\le X \\le \\sqrt{y})$$"
            "Vì $X \\ge 0$, điều này thu gọn lại thành:<br>"
            "$$F_Y(y) = P(X \\le \\sqrt{y}) = F_X(\\sqrt{y}) = \\frac{\\sqrt{y}}{2}$$"
            "Lấy đạo hàm của $F_Y(y)$ theo $y$ để tìm hàm mật độ xác suất $f_Y(y)$:<br>"
            "$$f_Y(y) = F'_Y(y) = \\frac{d}{dy}\\left( \\frac{1}{2} y^{1/2} \\right) = \\frac{1}{2} \\times \\frac{1}{2} y^{-1/2} = \\frac{1}{4\\sqrt{y}}\\quad (0 < y \\le 4)$$",
            "<b>Bước 3: Tính E(Y) theo hàm mật độ f_Y(y) và Đối chiếu `[+0,30đ]`</b><br>"
            "Áp dụng định nghĩa kỳ vọng cho biến $Y$:<br>"
            "$$E(Y) = \\int_0^4 y \\cdot f_Y(y)\\, dy = \\int_0^4 y \\cdot \\frac{1}{4\\sqrt{y}}\\, dy = \\frac{1}{4} \\int_0^4 y^{1/2}\\, dy$$"
            "Tính tích phân:<br>"
            "$$\\int_0^4 y^{1/2}\\, dy = \\left[ \\frac{2}{3} y^{3/2} \\right]_0^4 = \\frac{2}{3} (4)^{3/2} = \\frac{2}{3} \\times 8 = \\frac{16}{3}$$"
            "Do đó:<br>"
            "$$E(Y) = \\frac{1}{4} \\times \\frac{16}{3} = \\frac{4}{3}$$"
            "<b>Đối chiếu:</b> Hai cách tính hoàn toàn cho ra cùng một đáp số $E(Y) = E(X^2) = 4/3$, khẳng định tính đúng đắn của Định lý LOTUS!"
        ],
        "pro_tips": "LOTUS cho phép ta tính trực tiếp kỳ vọng của một hàm biến ngẫu nhiên $g(X)$ mà không cần tốn công đi tìm hàm phân phối của biến mới!",
        "pitfalls": "Quên nhân đạo hàm chuỗi khi tìm hàm mật độ của hàm hợp."
    })

    return exercises

if __name__ == "__main__":
    t6 = get_topic_6()
    print(f"Generated Topic 6: {len(t6)} exercises.")
