import sys
import json
import math

sys.stdout.reconfigure(encoding='utf-8')

def fmt(val, digits=4):
    res = f"{val:.{digits}f}".rstrip('0').rstrip('.')
    return res.replace('.', ',')

mcqs_5 = []

# TN5_01: Quy luật căn bậc hai cho Tổng rút được
# Box SD = 3, n = 100 -> SD(Sum) = 3 * sqrt(100) = 30
mcqs_5.append({
    "id": "TN5_01",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Một chiếc hộp chứa các tấm vé có độ lệch chuẩn $\\sigma = 3$. Rút ngẫu nhiên có hoàn lại $n = 100$ lần. Độ lệch chuẩn của TỔNG các số rút được ($S_n$) bằng bao nhiêu?",
    "options": [
        "30",
        "300",
        "3",
        "0,3"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo Quy luật căn bậc hai (Square Root Law) của mô hình chiếc hộp:\n$\\sigma(S_n) = \\sigma \\cdot \\sqrt{n} = 3 \\cdot \\sqrt{100} = 3 \\cdot 10 = 30$.\n\nPhân tích bẫy sai:\n- Phương án B: Sai do nhân $n \\cdot \\sigma = 100 \\cdot 3 = 300$ (ngộ nhận rằng độ lệch chuẩn của tổng tăng tỷ lệ thuận với $n$; thực chất chỉ kỳ vọng mới nhân $n$, còn độ lệch chuẩn chỉ nhân $\\sqrt{n}$ do có sự triệt tiêu ngẫu nhiên giữa các lần rút).\n- Phương án C: Giữ nguyên $\\sigma = 3$.\n- Phương án D: 0,3 là độ lệch chuẩn của TRUNG BÌNH MẪU $\\sigma(\\bar{X}_n) = \\sigma / \\sqrt{n} = 3 / 10 = 0,3$.",
    "source": "Slide Week 07 tr. 23; Stat20 Mục 4.12"
})

# TN5_02: Độ lệch chuẩn của Trung bình mẫu
# Box SD = 20, n = 400 -> SD(Mean) = 20 / sqrt(400) = 20 / 20 = 1.0
mcqs_5.append({
    "id": "TN5_02",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Thu nhập của cư dân một khu đô thị có độ lệch chuẩn $\\sigma = 20$ triệu đồng. Khảo sát một mẫu ngẫu nhiên độc lập gồm $n = 400$ người. Sai số chuẩn (độ lệch chuẩn của thu nhập trung bình mẫu $\\bar{X}_n$) bằng bao nhiêu?",
    "options": [
        "1,0 triệu đồng",
        "0,05 triệu đồng",
        "400 triệu đồng",
        "20 triệu đồng"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì sai số chuẩn của trung bình mẫu từ $n$ biến i.i.d. là:\n$\\sigma(\\bar{X}_n) = \\frac{\\sigma}{\\sqrt{n}} = \\frac{20}{\\sqrt{400}} = \\frac{20}{20} = 1,0$ triệu đồng.\n\nPhân tích bẫy sai:\n- Phương án B: Sai do chia cho $n=400$ thay vì $\\sqrt{n}$ ($20/400 = 0,05$).\n- Phương án C: Nhầm sang độ lệch chuẩn của TỔNG thu nhập: $\\sigma(S_n) = 20 \\cdot 20 = 400$.\n- Phương án D: Giữ nguyên $\\sigma = 20$ là sai vì trung bình của 400 người phải có độ biến động nhỏ hơn nhiều so với từng cá nhân.",
    "source": "Slide Week 07 tr. 25; Stat20 Mục 4.13"
})

# TN5_03: So sánh khi kích thước mẫu n tăng gấp 4
mcqs_5.append({
    "id": "TN5_03",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Khi tăng kích thước mẫu $n$ lên gấp 4 lần ($n' = 4n$), độ lệch chuẩn của Tổng rút được $\\sigma(S_n)$ và độ lệch chuẩn của Trung bình mẫu $\\sigma(\\bar{X}_n)$ thay đổi như thế nào?",
    "options": [
        "\\(\\sigma(S_n)\\) tăng gấp 2 lần, còn \\(\\sigma(\\bar{X}_n)\\) giảm đi 2 lần",
        "\\(\\sigma(S_n)\\) tăng gấp 4 lần, còn \\(\\sigma(\\bar{X}_n)\\) giảm đi 4 lần",
        "Cả hai đại lượng đều tăng gấp 2 lần",
        "Cả hai đại lượng đều không đổi vì độ lệch chuẩn của tổng thể không đổi"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì:\n- Đối với tổng: $\\sigma(S_{4n}) = \\sigma \\sqrt{4n} = 2 \\cdot \\sigma \\sqrt{n} = 2 \\cdot \\sigma(S_n)$ (tăng gấp $\\sqrt{4} = 2$ lần).\n- Đối với trung bình: $\\sigma(\\bar{X}_{4n}) = \\frac{\\sigma}{\\sqrt{4n}} = \\frac{1}{2} \\cdot \\frac{\\sigma}{\\sqrt{n}} = \\frac{1}{2} \\sigma(\\bar{X}_n)$ (giảm đi $\\sqrt{4} = 2$ lần).\n\nPhân tích bẫy sai:\n- Phương án B: Sai do quên căn bậc hai (nhầm theo hệ số 4 thay vì 2).\n- Phương án C: Nhầm chiều biến thiên của trung bình mẫu.\n- Phương án D: Độ lệch chuẩn của mẫu thay đổi theo kích thước mẫu $n$ dù $\\sigma$ tổng thể không đổi.",
    "source": "Slide Week 07 tr. 26; Stat20 Mục 4.13"
})

# TN5_04: Mô hình hộp nhị phân 0-1
# Hộp có 3 vé [1] và 7 vé [0]. p = 0.3. mu = 0.3, sigma = sqrt(0.3 * 0.7) = sqrt(0.21) ≈ 0.4583
mcqs_5.append({
    "id": "TN5_04",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Một chiếc hộp chứa 3 tấm vé ghi số [1] và 7 tấm vé ghi số [0]. Trung bình của hộp ($\\mu$) và độ lệch chuẩn của hộp ($\\sigma$) lần lượt là:",
    "options": [
        "\\(\\mu = 0,3\\) và \\(\\sigma = \\sqrt{0,21} \\approx 0,4583\\)",
        "\\(\\mu = 0,3\\) và \\(\\sigma = 0,21\\)",
        "\\(\\mu = 0,5\\) và \\(\\sigma = 0,5\\)",
        "\\(\\mu = 3\\) và \\(\\sigma = 7\\)"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì đối với hộp nhị phân chỉ gồm các vé [0] và [1]:\n- Tỷ lệ vé [1] là $p = \\frac{3}{3 + 7} = 0,3$.\n- Trung bình của hộp: $\\mu = p = 0,3$.\n- Phương sai của hộp: $\\sigma^2 = p(1 - p) = 0,3 \\cdot 0,7 = 0,21$.\n- Độ lệch chuẩn của hộp: $\\sigma = \\sqrt{0,21} \\approx 0,4583$.\n\nPhân tích bẫy sai:\n- Phương án B: 0,21 là phương sai $\\sigma^2$, chưa khai căn bậc hai để ra độ lệch chuẩn.\n- Phương án C: 0,5 là trường hợp số vé 0 và 1 bằng nhau.\n- Phương án D: Nhầm số lượng vé với giá trị trung bình.",
    "source": "Slide Week 07 tr. 22; Stat20 Mục 4.11"
})

# TN5_05: Bất đẳng thức Chebyshev dạng cơ bản k = 2
# P(|X - mu| >= 2 * sigma) <= 1 / 2^2 = 1/4 = 0.25 -> P(|X - mu| < 2 * sigma) >= 1 - 0.25 = 0.75
mcqs_5.append({
    "id": "TN5_05",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Cho biến ngẫu nhiên $X$ bất kỳ có kỳ vọng $\\mu$ và phương sai $\\sigma^2$. Theo bất đẳng thức Chebyshev, xác suất để $X$ nhận giá trị nằm trong khoảng $(\\mu - 2\\sigma; \\mu + 2\\sigma)$ luôn đạt ÍT NHẤT là bao nhiêu?",
    "options": [
        "75% (tức 0,75)",
        "95% (tức 0,95)",
        "50% (tức 0,50)",
        "88,89% (tức 8/9)"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo bất đẳng thức Chebyshev dạng phần bù với $k = 2$:\n$P(|X - \\mu| < 2\\sigma) \\ge 1 - \\frac{1}{k^2} = 1 - \\frac{1}{2^2} = 1 - 0,25 = 0,75$ (75%).\nBất đẳng thức này đúng cho MỌI phân phối xác suất.\n\nPhân tích bẫy sai:\n- Phương án B: 95% là quy tắc kinh nghiệm của phân phối CHUẨN ($N(\\mu, \\sigma^2)$), không phải bất đẳng thức Chebyshev tổng quát.\n- Phương án C: Sai phép tính.\n- Phương án D: $8/9 \\approx 88,89\\%$ là kết quả khi $k = 3$ ($1 - 1/9 = 8/9$).",
    "source": "Slide Week 07 tr. 34-35"
})

# TN5_06: Bất đẳng thức Chebyshev dạng đuôi k = 3
# P(|X - mu| >= 3 * sigma) <= 1 / 3^2 = 1/9 ≈ 0.1111
mcqs_5.append({
    "id": "TN5_06",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Với biến ngẫu nhiên $X$ có kỳ vọng $\\mu = 50$ và độ lệch chuẩn $\\sigma = 4$, cận trên Chebyshev cho xác suất $P(|X - 50| \\ge 12)$ là:",
    "options": [
        "1/9 (khoảng 11,11%)",
        "1/3",
        "1/16",
        "8/9"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì khoảng cách lệch là $12 = 3 \\cdot 4 = 3\\sigma \\implies k = 3$.\nTheo bất đẳng thức Chebyshev:\n$P(|X - 50| \\ge 12) = P(|X - \\mu| \\ge 3\\sigma) \\le \\frac{1}{k^2} = \\frac{1}{3^2} = \\frac{1}{9} \\approx 0,1111$ (11,11%).\n\nPhân tích bẫy sai:\n- Phương án B: Sai do quên bình phương: $1/k = 1/3$.\n- Phương án C: Sai do lấy $1/12$ hoặc $1/4^2 = 1/16$.\n- Phương án D: 8/9 là cận dưới của biến cố ngược lại $P(|X - 50| < 12) \\ge 8/9$.",
    "source": "Slide Week 07 tr. 34-35"
})

# TN5_07: Điểm mạnh độc nhất của Bất đẳng thức Chebyshev
mcqs_5.append({
    "id": "TN5_07",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Ưu điểm vượt trội lớn nhất của Bất đẳng thức Chebyshev so với các phương pháp tính xác suất khác là gì?",
    "options": [
        "Nó áp dụng được cho MỌI biến ngẫu nhiên (bất kể phân phối rời rạc, liên tục, lệch mạnh hay nhiều đỉnh), chỉ cần biết kỳ vọng $\\mu$ và phương sai $\\sigma^2$ hữu hạn",
        "Nó luôn cho kết quả xác suất chính xác 100% không có sai số",
        "Nó chỉ áp dụng được riêng cho phân phối Chuẩn",
        "Nó không cần biết phương sai của biến ngẫu nhiên"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì Chebyshev là bất đẳng thức phi tham số (non-parametric), áp dụng phổ quát cho bất kỳ phân phối nào mà không cần giả định về hình dạng của phân phối đó, chỉ cần tồn tại $\\mu$ và $\\sigma^2$.\n\nPhân tích bẫy sai:\n- Phương án B: Chebyshev chỉ cung cấp CẬN TRÊN hoặc CẬN DƯỚI (bounds), không phải xác suất chính xác, và cận này thường khá lỏng.\n- Phương án C: Phân phối chuẩn dùng bảng tra Z-score, không cần đến Chebyshev.\n- Phương án D: Chebyshev bắt buộc phải biết phương sai $\\sigma^2$ hữu hạn.",
    "source": "Slide Week 07 tr. 33"
})

# TN5_08: Chebyshev cho Trung bình mẫu
# n = 100, mu = 10, sigma = 2 -> sigma(X_bar) = 2 / 10 = 0.2
# P(|X_bar - 10| >= 0.6) <= Var(X_bar) / 0.6^2 = (0.2)^2 / 0.36 = 0.04 / 0.36 = 1/9 ≈ 0.1111
mcqs_5.append({
    "id": "TN5_08",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Trung bình",
    "question": "Cho $X_1, \\dots, X_{100}$ là mẫu ngẫu nhiên gồm 100 biến i.i.d. có kỳ vọng $\\mu = 10$ và độ lệch chuẩn $\\sigma = 2$. Đánh giá xác suất để trung bình mẫu $\\bar{X}_{100}$ sai lệch so với $\\mu$ từ 0,6 trở lên ($P(|\\bar{X}_{100} - 10| \\ge 0,6)$) theo Chebyshev:",
    "options": [
        "\\(P(|\\bar{X}_{100} - 10| \\ge 0,6) \\le 1/9 \\approx 0,1111\\)",
        "\\(P(|\\bar{X}_{100} - 10| \\ge 0,6) \\le 1/3\\)",
        "\\(P(|\\bar{X}_{100} - 10| \\ge 0,6) \\le 4/0,36 \\approx 11,11\\)",
        "\\(P(|\\bar{X}_{100} - 10| \\ge 0,6) \\ge 8/9\\)"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì đối với trung bình mẫu $\\bar{X}_{100}$:\n- Độ lệch chuẩn của trung bình mẫu: $\\sigma(\\bar{X}_{100}) = \\frac{\\sigma}{\\sqrt{n}} = \\frac{2}{\\sqrt{100}} = \\frac{2}{10} = 0,2$.\n- Khoảng sai số $\\varepsilon = 0,6 = 3 \\cdot 0,2 = 3 \\sigma(\\bar{X}_{100}) \\implies k = 3$.\n- Theo Chebyshev: $P(|\\bar{X}_{100} - 10| \\ge 0,6) \\le \\frac{1}{k^2} = \\frac{1}{3^2} = \\frac{1}{9} \\approx 0,1111$.\n\nPhân tích bẫy sai:\n- Phương án B: Quên bình phương: $1/k = 1/3$.\n- Phương án C: Sai do lấy $\\sigma^2$ của tổng thể chia cho $\\varepsilon^2$ ($4 / 0,36$) mà quên chia cho mẫu số $n=100$ (xác suất > 1 là vô nghĩa).\n- Phương án D: Đảo ngược chiều bất đẳng thức.",
    "source": "Slide Week 07 tr. 36-37"
})

# TN5_09: Phát biểu Luật số lớn yếu (WLLN)
mcqs_5.append({
    "id": "TN5_09",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Phát biểu toán học nào sau đây biểu diễn ĐÚNG nội dung của Luật số lớn yếu (Weak Law of Large Numbers - WLLN) đối với dãy biến i.i.d. có kỳ vọng hữu hạn $\\mu$?",
    "options": [
        "Với mọi \\(\\varepsilon > 0\\), \\(\\lim_{n \\to \\infty} P(|\\bar{X}_n - \\mu| < \\varepsilon) = 1\\) (hoặc \\(\\lim_{n \\to \\infty} P(|\\bar{X}_n - \\mu| \\ge \\varepsilon) = 0\\))",
        "Khi $n \\to \\infty$, tổng $S_n$ tiến dần về kỳ vọng $\\mu$",
        "Khi $n \\to \\infty$, phương sai của tổng $S_n$ tiến dần về 0",
        "Với mọi $n$, trung bình mẫu $\\bar{X}_n$ luôn bằng đúng $\\mu$"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì Luật số lớn yếu khẳng định sự hội tụ theo xác suất: khi kích thước mẫu $n$ tiến ra vô cùng, xác suất để trung bình mẫu $\\bar{X}_n$ sai lệch so với kỳ vọng lý thuyết $\\mu$ một khoảng dù nhỏ tùy ý $\\varepsilon$ sẽ tiến dần về 0 (tức xác suất nằm sát $\\mu$ tiến về 1).\n\nPhân tích bẫy sai:\n- Phương án B: Sai vì TỔNG $S_n$ tiến ra vô cùng theo $n\\mu$, chỉ có TRUNG BÌNH MẪU mới hội tụ về $\\mu$.\n- Phương án C: Sai vì phương sai của tổng là $n\\sigma^2 \\to \\infty$.\n- Phương án D: $\\bar{X}_n$ là biến ngẫu nhiên, nó không cố định bằng $\\mu$ với mọi $n$.",
    "source": "Slide Week 07 tr. 38; Stat20 Mục 4.13"
})

# TN5_10: Chứng minh WLLN bằng Bất đẳng thức Chebyshev
mcqs_5.append({
    "id": "TN5_10",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Trung bình",
    "question": "Trong giáo trình và slide Week 07, Luật số lớn yếu được chứng minh một cách chặt chẽ dựa trên bất đẳng thức nào sau đây?",
    "options": [
        "Áp dụng Bất đẳng thức Chebyshev cho trung bình mẫu: \\(P(|\\bar{X}_n - \\mu| \\ge \\varepsilon) \\le \\frac{\\sigma^2}{n \\varepsilon^2}\\), vế phải tiến về 0 khi $n \\to \\infty$",
        "Áp dụng Bất đẳng thức Cauchy-Schwarz",
        "Áp dụng Bất đẳng thức Jensen",
        "Áp dụng Định lý Pythagoras"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo Week 07 (tr. 38-39):\nBiến trung bình mẫu $\\bar{X}_n$ có kỳ vọng $\\mu$ và phương sai $\\operatorname{Var}(\\bar{X}_n) = \\frac{\\sigma^2}{n}$.\nÁp dụng trực tiếp bất đẳng thức Chebyshev cho $\\bar{X}_n$ với sai số $\\varepsilon$:\n$P(|\\bar{X}_n - \\mu| \\ge \\varepsilon) \\le \\frac{\\operatorname{Var}(\\bar{X}_n)}{\\varepsilon^2} = \\frac{\\sigma^2}{n \\varepsilon^2}$.\nVới $\\varepsilon > 0$ và $\\sigma^2 < \\infty$ cố định, khi cho $n \\to \\infty$ thì $\\frac{\\sigma^2}{n \\varepsilon^2} \\to 0$. Định lý được chứng minh hoàn tất.\n\nPhân tích bẫy sai:\n- Phương án B, C, D: Đều là các bất đẳng thức toán học khác, không dùng để chứng minh trực tiếp WLLN.",
    "source": "Slide Week 07 tr. 38-39"
})

# TN5_11: Xác định kích thước mẫu n theo Chebyshev
# sigma = 4, epsilon = 0.5, alpha = 0.05.
# n >= sigma^2 / (alpha * epsilon^2) = 16 / (0.05 * 0.25) = 16 / 0.0125 = 1280
n_11 = 16 / (0.05 * 0.25)
mcqs_5.append({
    "id": "TN5_11",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Nâng cao",
    "question": "Cần khảo sát một mẫu ngẫu nhiên độc lập tối thiểu bao nhiêu quan sát ($n$) từ tổng thể có độ lệch chuẩn $\\sigma = 4$ để theo Bất đẳng thức Chebyshev, ta có thể bảo đảm với độ tin cậy ít nhất 95% rằng trung bình mẫu $\\bar{X}_n$ sai lệch so với kỳ vọng $\\mu$ không quá 0,5 đơn vị ($P(|\\bar{X}_n - \\mu| < 0,5) \\ge 0,95$)?",
    "options": [
        "n = 1.280",
        "n = 246",
        "n = 320",
        "n = 64"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo hệ quả của bất đẳng thức Chebyshev cho trung bình mẫu:\n$P(|\\bar{X}_n - \\mu| \\ge \\varepsilon) \\le \\frac{\\sigma^2}{n \\varepsilon^2} \\le \\alpha$.\nỞ đây: $\\sigma = 4$, sai số $\\varepsilon = 0,5$, và mức rủi ro $\\alpha = 1 - 0,95 = 0,05$.\nSuy ra:\n$n \\ge \\frac{\\sigma^2}{\\alpha \\cdot \\varepsilon^2} = \\frac{4^2}{0,05 \\cdot (0,5)^2} = \\frac{16}{0,05 \\cdot 0,25} = \\frac{16}{0,0125} = 1.280$.\n\nPhân tích bẫy sai:\n- Phương án B: $n \\approx 246$ là kích thước mẫu tính theo xấp xỉ PHÂN PHỐI CHUẨN ($z_{0,025} = 1,96 \\implies n = \\frac{1,96^2 \\cdot 16}{0,25} \\approx 245,86$). Chebyshev không đòi hỏi phân phối chuẩn nên cho cận an toàn lớn hơn (1.280).\n- Phương án C, D: Sai số học do quên bình phương $\\varepsilon$ hoặc $\\sigma$.",
    "source": "Slide Week 07 tr. 40"
})

# TN5_12: Trực giác sòng bạc và Luật số lớn
mcqs_5.append({
    "id": "TN5_12",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Trong một trò chơi cá cược, mỗi ván người chơi có kỳ vọng lợi nhuận là $-0,05$ đô-la (nhà cái có kỳ vọng $+0,05$ đô-la). Nếu một người chơi chơi 1.000.000 ván, theo Luật số lớn điều gì gần như chắc chắn sẽ xảy ra?",
    "options": [
        "Người chơi gần như chắc chắn phá sản và chịu lỗ bình quân khoảng 0,05 đô-la cho mỗi ván chơi",
        "Người chơi có thể lội ngược dòng thắng đậm vì 1.000.000 ván sẽ có lúc chuỗi may mắn xuất hiện",
        "Người chơi sẽ hòa vốn vì số ván thắng và thua sẽ cân bằng hoàn hảo bằng nhau",
        "Phương sai của tổng tiền thua sẽ giảm dần về 0"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo WLLN, khi số ván $n = 1.000.000$ rất lớn, trung bình số tiền thắng/thua mỗi ván $\\bar{X}_n$ sẽ hội tụ ngặt nghèo về kỳ vọng lý thuyết $\\mu = -0,05$ đô-la. Tổng số tiền người chơi mất sau 1 triệu ván xấp xỉ $1.000.000 \\times (-0,05) = -50.000$ đô-la. Đây là lý do các sòng bạc luôn kiếm được lợi nhuận khổng lồ và không bao giờ bị thua lỗ trong dài hạn.\n\nPhân tích bẫy sai:\n- Phương án B: Bẫy tâm lý ngụy biện con bạc (Gambler's fallacy).\n- Phương án C: Bẫy ngộ nhận luật bù trừ số ván.\n- Phương án D: Phương sai của TỔNG tiền luôn tăng theo $n\\sigma^2$, không giảm về 0.",
    "source": "Stat20 Mục 4.13; Slide Week 07 tr. 38"
})

# TN5_13: Rút xúc xắc 100 lần - Kỳ vọng và SD của tổng
# Xúc xắc: mu = 3.5, sigma = sqrt(35/12) ≈ 1.7078
# E(S_100) = 100 * 3.5 = 350.
# SD(S_100) = sqrt(35/12) * sqrt(100) = sqrt(3500 / 12) = sqrt(291.667) ≈ 17.078
e_13 = 100 * 3.5
sd_13 = math.sqrt(35 / 12) * 10
mcqs_5.append({
    "id": "TN5_13",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Trung bình",
    "question": "Gieo một con xúc xắc cân đối 6 mặt 100 lần độc lập. Biết mỗi lần gieo có số chấm kỳ vọng $\\mu = 3,5$ và phương sai $\\sigma^2 = 35/12 \\approx 2,9167$. Kỳ vọng và độ lệch chuẩn của TỔNG số chấm sau 100 lần gieo lần lượt là:",
    "options": [
        "\\(E(S_{100}) = 350\\) và \\(\\sigma(S_{100}) \\approx 17,08\\)",
        "\\(E(S_{100}) = 350\\) và \\(\\sigma(S_{100}) \\approx 170,78\\)",
        "\\(E(S_{100}) = 3,5\\) và \\(\\sigma(S_{100}) \\approx 0,1708\\)",
        "\\(E(S_{100}) = 350\\) và \\(\\sigma(S_{100}) = 291,67\\)"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo công thức tổng của $n$ biến i.i.d.:\n- Kỳ vọng tổng: $E(S_n) = n \\cdot \\mu = 100 \\cdot 3,5 = 350$.\n- Phương sai tổng: $\\operatorname{Var}(S_n) = n \\cdot \\sigma^2 = 100 \\cdot \\frac{35}{12} \\approx 291,67$.\n- Độ lệch chuẩn tổng: $\\sigma(S_n) = \\sqrt{\\operatorname{Var}(S_n)} = \\sqrt{291,67} \\approx 17,08$.\n\nPhân tích bẫy sai:\n- Phương án B: Sai do tính $\\sigma(S_n) = n \\cdot \\sigma = 100 \\cdot 1,7078 = 170,78$ (nhân $n$ thay vì $\\sqrt{n}$).\n- Phương án C: Đây là kỳ vọng và SD của TRUNG BÌNH MẪU $\\bar{X}_{100}$, không phải của TỔNG.\n- Phương án D: 291,67 là phương sai của tổng, chưa lấy căn bậc hai.",
    "source": "Slide Week 07 tr. 23"
})

# TN5_14: Đánh giá thời gian giao hàng theo Chebyshev
# mu = 30 phút, sigma = 5 phút. P(20 < X < 40) = P(|X - 30| < 10)
# k = 10 / 5 = 2 -> P >= 1 - 1/4 = 0.75
mcqs_5.append({
    "id": "TN5_14",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Thời gian giao hàng của một quán ăn có trung bình $\\mu = 30$ phút và độ lệch chuẩn $\\sigma = 5$ phút. Chưa biết quy luật phân phối cụ thể của thời gian giao hàng. Theo Bất đẳng thức Chebyshev, xác suất để một đơn hàng được giao trong khoảng từ 20 đến 40 phút tối thiểu bằng bao nhiêu?",
    "options": [
        "75%",
        "95%",
        "88,89%",
        "50%"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì khoảng từ 20 đến 40 phút tương ứng với khoảng sai lệch quanh trung bình:\n$|X - 30| < 10$.\nVì $\\sigma = 5$, khoảng cách sai lệch là $10 = 2 \\sigma \\implies k = 2$.\nTheo Chebyshev: $P(|X - 30| < 2 \\cdot 5) \\ge 1 - \\frac{1}{2^2} = 1 - 0,25 = 0,75$ (75%).\n\nPhân tích bẫy sai:\n- Phương án B: 95% là quy tắc phân phối chuẩn, không áp dụng được khi chưa biết phân phối cụ thể.\n- Phương án C: 88,89% ứng với $k=3$ (từ 15 đến 45 phút).\n- Phương án D: Sai số học.",
    "source": "Slide Week 07 tr. 35"
})

# TN5_15: Sai lầm phổ biến khi áp dụng Chebyshev
mcqs_5.append({
    "id": "TN5_15",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Trung bình",
    "question": "Khi áp dụng Bất đẳng thức Chebyshev $P(|X - \\mu| \\ge k\\sigma) \\le \\frac{1}{k^2}$, điều kiện bắt buộc đối với hằng số $k$ để bất đẳng thức mang lại thông tin có ý nghĩa thực tế là gì?",
    "options": [
        "\\(k > 1\\)",
        "\\(k > 0\\)",
        "\\(k\\) phải là số nguyên dương",
        "\\(k \\ge 3\\)"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì nếu $k \\le 1$ thì vế phải $\\frac{1}{k^2} \\ge 1$. Ta luôn biết xác suất của mọi biến cố luôn nhỏ hơn hoặc bằng 1, do đó kết luận $P(\\dots) \\le 1$ hoặc $P(\\dots) \\ge 0$ là một mệnh đề hiển nhiên (trivial), không đem lại bất kỳ thông tin hữu ích nào. Để chặn được cận trên $< 1$, bắt buộc $k > 1$.\n\nPhân tích bẫy sai:\n- Phương án B: Với $0 < k \\le 1$, bất đẳng thức vẫn đúng về mặt toán học nhưng vô nghĩa vì cận trên $\\ge 1$.\n- Phương án C: $k$ có thể là số thực bất kỳ lớn hơn 1 (ví dụ $k = 1,5$ hoặc $k = \\sqrt{5}$), không bắt buộc phải nguyên.\n- Phương án D: $k=2$ đã cho cận 75% rất hữu ích.",
    "source": "Slide Week 07 tr. 34"
})

# TN5_16: Chebyshev với k không nguyên
# k = sqrt(5) ≈ 2.236. P(|X - mu| >= sqrt(5) * sigma) <= 1 / 5 = 0.20 -> P(...) >= 1 - 0.20 = 0.80
mcqs_5.append({
    "id": "TN5_16",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Trung bình",
    "question": "Cho biến ngẫu nhiên $X$ có $\\mu = 100$ và $\\sigma = 10$. Khoảng đối xứng quanh trung bình $(\\mu - c; \\mu + c)$ nào sau đây được Chebyshev bảo đảm chắc chắn chứa ÍT NHẤT 80% giá trị của $X$?",
    "options": [
        "\\((100 - 10\\sqrt{5}; 100 + 10\\sqrt{5})\\) (khoảng [77,64; 122,36])",
        "\\([80; 120]\\)",
        "\\([70; 130]\\)",
        "\\([90; 110]\\)"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì ta cần xác suất chứa ít nhất $80\\% = 0,80$:\n$1 - \\frac{1}{k^2} = 0,80 \\iff \\frac{1}{k^2} = 0,20 = \\frac{1}{5} \\iff k^2 = 5 \\iff k = \\sqrt{5} \\approx 2,236$.\nĐộ rộng bán kính sai lệch: $c = k \\cdot \\sigma = \\sqrt{5} \\cdot 10 \\approx 22,36$.\nDo đó khoảng cần tìm là $(100 - 22,36; 100 + 22,36) = (77,64; 122,36)$.\n\nPhân tích bẫy sai:\n- Phương án B: $[80; 120]$ ứng với $k=2$, chỉ đảm bảo ít nhất $1 - 1/4 = 75\\% < 80\\%$.\n- Phương án C: $[70; 130]$ ứng với $k=3$, đảm bảo ít nhất $88,89\\%$ (rộng hơn mức tối thiểu cần thiết).\n- Phương án D: $[90; 110]$ ứng với $k=1$, Chebyshev cho cận $1 - 1 = 0\\%$.",
    "source": "Slide Week 07 tr. 35"
})

# TN5_17: Phân biệt Tổng và Trung bình trong mô hình chiếc hộp
mcqs_5.append({
    "id": "TN5_17",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Trong mô hình chiếc hộp rút có hoàn lại $n$ lần, phát biểu nào sau đây là ĐÚNG khi nói về xu hướng biến thiên khi số lần rút $n$ tăng dần?",
    "options": [
        "Độ lệch chuẩn của Tổng $S_n$ tăng dần theo $\\sqrt{n}$, trong khi độ lệch chuẩn của Trung bình $\\bar{X}_n$ giảm dần theo $1/\\sqrt{n}$",
        "Độ lệch chuẩn của cả Tổng và Trung bình đều tăng dần theo $n$",
        "Độ lệch chuẩn của cả Tổng và Trung bình đều giảm dần về 0",
        "Độ lệch chuẩn của Tổng không đổi, chỉ có độ lệch chuẩn của Trung bình giảm"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì:\n- $\\sigma(S_n) = \\sigma \\sqrt{n} \\to \\infty$ khi $n \\to \\infty$ (tổng của càng nhiều số ngẫu nhiên thì khoảng giá trị tuyệt đối càng phân tán rộng ra).\n- $\\sigma(\\bar{X}_n) = \\frac{\\sigma}{\\sqrt{n}} \\to 0$ khi $n \\to \\infty$ (chia cho $n$ khiến các sai số ngẫu nhiên triệt tiêu lẫn nhau, giá trị trung bình gom tụ cực kỳ sát về tâm $\\mu$).\n\nPhân tích bẫy sai:\n- Phương án B, C, D: Đều mô tả sai quy luật căn bậc hai.",
    "source": "Slide Week 07 tr. 26; Stat20 Mục 4.13"
})

# TN5_18: Trung bình và SD của hộp vé bất kỳ
# Vé: [1, 2, 9]. n = 3 vé.
# mu = (1 + 2 + 9) / 3 = 12 / 3 = 4.
# var = [(1-4)^2 + (2-4)^2 + (9-4)^2] / 3 = [9 + 4 + 25] / 3 = 38 / 3 ≈ 12.6667
# SD = sqrt(38/3) ≈ 3.559
mcqs_5.append({
    "id": "TN5_18",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Trung bình",
    "question": "Một chiếc hộp chứa đúng 3 tấm vé mang số: [1, 2, 9]. Trung bình của hộp $\\mu$ và phương sai của hộp $\\sigma^2$ lần lượt là:",
    "options": [
        "\\(\\mu = 4\\) và \\(\\sigma^2 = 38/3 \\approx 12,67\\)",
        "\\(\\mu = 4\\) và \\(\\sigma^2 = 19\\)",
        "\\(\\mu = 4\\) và \\(\\sigma = 38/3\\)",
        "\\(\\mu = 3\\) và \\(\\sigma^2 = 12\\)"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì đối với chiếc hộp gồm $N=3$ vé mang số hữu hạn (xem như tổng thể):\n- Trung bình của hộp: $\\mu = \\frac{1 + 2 + 9}{3} = \\frac{12}{3} = 4$.\n- Phương sai của hộp (chia cho $N=3$): $\\sigma^2 = \\frac{(1-4)^2 + (2-4)^2 + (9-4)^2}{3} = \\frac{(-3)^2 + (-2)^2 + 5^2}{3} = \\frac{9 + 4 + 25}{3} = \\frac{38}{3} \\approx 12,67$.\n\nPhân tích bẫy sai:\n- Phương án B: Sai do chia cho $N-1 = 2$ ($38/2 = 19$, đây là phương sai mẫu, trong khi hộp đóng vai trò là tổng thể nên chia cho $N$).\n- Phương án C: Nhầm phương sai với độ lệch chuẩn.\n- Phương án D: Sai số học.",
    "source": "Slide Week 07 tr. 22; Stat20 Mục 4.11"
})

# TN5_19: Đánh giá xác suất theo Chebyshev với phân phối bất đối xứng
# X >= 0, mu = 20, sigma = 5. Danh gia P(X >= 40)
# Chu y: |X - 20| >= 20 <=> X >= 40 hoac X <= 0.
# P(|X - 20| >= 20) <= sigma^2 / 20^2 = 25 / 400 = 1/16 = 0.0625.
# Do X >= 0, nen P(X >= 40) <= P(|X - 20| >= 20) <= 0.0625
mcqs_5.append({
    "id": "TN5_19",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Nâng cao",
    "question": "Biến ngẫu nhiên không âm $X \\ge 0$ có kỳ vọng $\\mu = 20$ và độ lệch chuẩn $\\sigma = 5$. Đánh giá cận trên của xác suất $P(X \\ge 40)$ bằng Bất đẳng thức Chebyshev:",
    "options": [
        "\\(P(X \\ge 40) \\le 1/16 = 0,0625\\)",
        "\\(P(X \\ge 40) \\le 1/4 = 0,25\\)",
        "\\(P(X \\ge 40) \\le 0,50\\)",
        "\\(P(X \\ge 40) = 0\\)"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì:\n- Ta có biến cố $\\{X \\ge 40\\}$ tương đương $\\{X - 20 \\ge 20\\}$.\n- Biến cố này là tập con của biến cố hai phía: $\\{|X - 20| \\ge 20\\}$ (gồm $X \\ge 40$ hoặc $X \\le 0$).\n- Áp dụng Chebyshev với $\\varepsilon = 20 = 4\\sigma \\implies k = 4$:\n$P(X \\ge 40) \\le P(|X - 20| \\ge 20) \\le \\frac{\\sigma^2}{\\varepsilon^2} = \\frac{5^2}{20^2} = \\frac{25}{400} = \\frac{1}{16} = 0,0625$ (6,25%).\n\nPhân tích bẫy sai:\n- Phương án B: Sai do lấy $k = 40/20 = 2 \\implies 1/2^2 = 0,25$ (nhầm độ lệch là 10 thay vì 20).\n- Phương án C: Dùng bất đẳng thức Markov ($E(X)/a = 20/40 = 0,5$), nhưng Chebyshev cho cận chặt hơn nhiều (0,0625).\n- Phương án D: Sai hoàn toàn.",
    "source": "Slide Week 07 tr. 34"
})

# TN5_20: Định lý Chebyshev và phân phối Chuẩn so sánh
mcqs_5.append({
    "id": "TN5_20",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Trung bình",
    "question": "Trong khoảng $(\\mu - 3\\sigma; \\mu + 3\\sigma)$, Bất đẳng thức Chebyshev bảo đảm chứa ít nhất bao nhiêu phần trăm dữ liệu, và nếu phân phối là Phân phối Chuẩn thì thực tế chứa bao nhiêu phần trăm dữ liệu?",
    "options": [
        "Chebyshev bảo đảm ít nhất 88,89%, còn Phân phối Chuẩn thực tế chứa 99,73%",
        "Chebyshev bảo đảm ít nhất 95%, còn Phân phối Chuẩn thực tế chứa 99%",
        "Cả hai đều cho kết quả giống hệt nhau là 99,73%",
        "Chebyshev bảo đảm 99,73%, còn Phân phối Chuẩn là 88,89%"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì:\n- Theo Chebyshev với $k=3$: $P(|X - \\mu| < 3\\sigma) \\ge 1 - \\frac{1}{3^2} = 1 - \\frac{1}{9} = \\frac{8}{9} \\approx 88,89\\%$.\n- Đối với Phân phối Chuẩn $N(\\mu, \\sigma^2)$, do có dạng hình chuông đặc thù với đuôi tiêu biến nhanh theo hàm mũ $e^{-z^2/2}$, diện tích trong khoảng $\\pm 3\\sigma$ đạt tới $99,73\\%$.\nĐiều này minh họa rõ nét tính chất 'an toàn nhưng lỏng' của Chebyshev đối với mọi phân phối so với trường hợp phân phối Chuẩn cụ thể.\n\nPhân tích bẫy sai:\n- Phương án B, C, D: Đều nhầm lẫn số liệu giữa hai định lý.",
    "source": "Slide Week 07 tr. 35 & tr. 54"
})

# TN5_21: WLLN và tính không chệch của trung bình mẫu
mcqs_5.append({
    "id": "TN5_21",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Hai đặc tính then chốt khẳng định trung bình mẫu $\\bar{X}_n$ là một ước lượng xuất sắc cho kỳ vọng tổng thể $\\mu$ là:",
    "options": [
        "Tính không chệch ($E(\\bar{X}_n) = \\mu$) và Tính nhất quán ($\\operatorname{Var}(\\bar{X}_n) = \\frac{\\sigma^2}{n} \\to 0$ khi $n \\to \\infty$ theo WLLN)",
        "Tính đối xứng và tính có phương sai cố định không đổi theo $n$",
        "Tính độc lập và tính luôn nhận giá trị nguyên",
        "Tính có phân phối đều và kỳ vọng luôn bằng 0"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì:\n- Tính không chệch (Unbiasedness): Kỳ vọng của trung bình mẫu luôn bằng đúng tham số thực $\\mu$ với mọi $n$.\n- Tính nhất quán (Consistency): Khi kích thước mẫu $n$ tăng vô hạn, phương sai giảm về 0, đảm bảo theo WLLN rằng trung bình mẫu hội tụ theo xác suất về giá trị thực $\\mu$.\n\nPhân tích bẫy sai:\n- Phương án B, C, D: Đều sai các định nghĩa lý thuyết thống kê cơ bản.",
    "source": "Slide Week 07 tr. 25, 38; Stat20 Mục 4.13"
})

# TN5_22: Tổng của n biến Bernoulli - Quy về Nhị thức
mcqs_5.append({
    "id": "TN5_22",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Nếu chiếc hộp chỉ chứa các tấm vé [0] và [1] với tỷ lệ vé [1] là $p$, thì Tổng các số rút được sau $n$ lần rút có hoàn lại ($S_n = \\sum_{i=1}^n X_i$) chính là:",
    "options": [
        "Biến ngẫu nhiên có Phân phối Nhị thức $B(n, p)$, đếm số lần rút được vé [1]",
        "Biến ngẫu nhiên có Phân phối Siêu bội $HG(N, M, n)$",
        "Biến ngẫu nhiên có Phân phối Poisson $Po(np)$",
        "Biến ngẫu nhiên Bernoulli(p)"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì mỗi lần rút có hoàn lại là một phép thử Bernoulli($p$) độc lập với $X_i \\in \\{0, 1\\}$. Khi đó tổng $S_n = X_1 + \\dots + X_n$ chính là số lần thành công (số lần rút được vé 1) trong $n$ phép thử Bernoulli độc lập, đó là định nghĩa chính xác 100% của Phân phối Nhị thức $B(n, p)$.\n\nPhân tích bẫy sai:\n- Phương án B: Siêu bội chỉ xuất hiện khi rút KHÔNG hoàn lại.\n- Phương án C: Poisson chỉ là phân phối xấp xỉ khi $n$ lớn, $p$ nhỏ.\n- Phương án D: Bernoulli chỉ ứng với $n=1$.",
    "source": "Slide Week 07 tr. 22; Stat20 Mục 4.11"
})

print(f"Total MCQs for Topic 5: {len(mcqs_5)}")

with open('content/mcq_topic_5.json', 'w', encoding='utf-8') as f:
    json.dump(mcqs_5, f, ensure_ascii=False, indent=2)
print("Saved content/mcq_topic_5.json")
