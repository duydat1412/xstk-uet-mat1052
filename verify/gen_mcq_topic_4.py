import sys
import json
import math

sys.stdout.reconfigure(encoding='utf-8')

def fmt(val, digits=4):
    res = f"{val:.{digits}f}".rstrip('0').rstrip('.')
    return res.replace('.', ',')

mcqs_4 = []

# TN4_01: Nhận diện mô hình - Rút có hoàn lại vs không hoàn lại
mcqs_4.append({
    "id": "TN4_01",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Cơ bản",
    "question": "Một kiện hàng có 30 sản phẩm, trong đó có 6 phế phẩm. Người kiểm tra rút ngẫu nhiên lần lượt 5 sản phẩm KHÔNG HOÀN LẠI để kiểm tra. Gọi $X$ là số phế phẩm tìm thấy trong 5 sản phẩm đó. Biến ngẫu nhiên $X$ tuân theo phân phối nào?",
    "options": [
        "Phân phối Siêu bội (Hypergeometric)",
        "Phân phối Nhị thức (Binomial)",
        "Phân phối Poisson",
        "Phân phối Chuẩn (Normal)"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì phép thử rút không hoàn lại từ một tập hợp hữu hạn ($N=30$, có $M=6$ phế phẩm, lấy mẫu kích thước $n=5$) khiến xác suất rút được phế phẩm thay đổi sau mỗi lần rút (các lần rút phụ thuộc). Do đó số phế phẩm $X$ tuân theo phân phối Siêu bội $X \\sim HG(N=30, M=6, n=5)$.\n\nPhân tích bẫy sai:\n- Phương án B: Nhị thức chỉ áp dụng khi rút CÓ HOÀN LẠI (xác suất $p$ không đổi qua các lần rút).\n- Phương án C: Poisson dùng để đếm số biến cố xảy ra trong một khoảng thời gian/không gian liên tục.\n- Phương án D: $X$ là biến rời rạc đếm được, không thể là phân phối liên tục Chuẩn.",
    "source": "Slide Week 07 tr. 15; Stat20 Mục 4.9"
})

# TN4_02: Nhận diện mô hình Poisson
mcqs_4.append({
    "id": "TN4_02",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Cơ bản",
    "question": "Số lượng tin nhắn rác gửi đến một hòm thư điện tử trong khoảng thời gian từ 8h00 đến 9h00 sáng mỗi ngày thường được mô hình hóa phù hợp nhất bằng phân phối xác suất nào sau đây?",
    "options": [
        "Phân phối Poisson",
        "Phân phối Siêu bội",
        "Phân phối Đều rời rạc",
        "Phân phối Bernoulli"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì biến số đếm số lần xảy ra của một sự kiện ngẫu nhiên độc lập trong một khoảng thời gian liên tục cố định với tốc độ xuất hiện trung bình không đổi là định nghĩa tiêu chuẩn của Phân phối Poisson $Po(\\lambda)$.\n\nPhân tích bẫy sai:\n- Phương án B: Siêu bội chỉ dùng cho rút không hoàn lại từ tập hữu hạn.\n- Phương án C: Đều rời rạc đòi hỏi các số lượng tin nhắn khác nhau phải có cùng xác suất (vô lý trong thực tế).\n- Phương án D: Bernoulli chỉ nhận 2 giá trị 0 hoặc 1.",
    "source": "Slide Week 07 tr. 16; Stat20 Mục 4.10"
})

# TN4_03: Kỳ vọng và phương sai của Nhị thức B(n, p)
# n = 20, p = 0.25 -> E = 5, Var = 20 * 0.25 * 0.75 = 3.75, SD = sqrt(3.75) ≈ 1.9365
e_03 = 20 * 0.25
var_03 = 20 * 0.25 * 0.75
sd_03 = math.sqrt(var_03)

mcqs_4.append({
    "id": "TN4_03",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Cơ bản",
    "question": "Một bài thi trắc nghiệm gồm 20 câu hỏi độc lập, mỗi câu có 4 phương án trả lời và chỉ có 1 phương án đúng. Một thí sinh chọn ngẫu nhiên hoàn toàn cả 20 câu. Gọi $X$ là số câu trả lời đúng. Kỳ vọng và phương sai của $X$ lần lượt là:",
    "options": [
        f"E(X) = {fmt(e_03)} và Var(X) = {fmt(var_03)}",
        f"E(X) = {fmt(e_03)} và Var(X) = {fmt(e_03)}",
        f"E(X) = {fmt(e_03)} và Var(X) = {fmt(sd_03)}",
        "E(X) = 4 và Var(X) = 3"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì $X \\sim B(n=20, p=0,25)$:\n- Kỳ vọng: $E(X) = np = 20 \\cdot 0,25 = 5$.\n- Phương sai: $\\operatorname{Var}(X) = np(1-p) = 20 \\cdot 0,25 \\cdot 0,75 = 3,75$.\n\nPhân tích bẫy sai:\n- Phương án B: Nhầm sang tính chất của phân phối Poisson (Var = E = 5).\n- Phương án C: $\\sqrt{3,75} \\approx 1,9365$ là độ lệch chuẩn $\\sigma$, không phải phương sai.\n- Phương án D: Sai phép tính.",
    "source": "Slide Week 07 tr. 15; Stat20 Mục 4.8"
})

# TN4_04: Tính xác suất nhị thức chính xác P(X = k)
# n = 5, p = 0.4. P(X = 2) = C(5, 2) * 0.4^2 * 0.6^3 = 10 * 0.16 * 0.216 = 0.3456
p_04 = math.comb(5, 2) * (0.4**2) * (0.6**3)
mcqs_4.append({
    "id": "TN4_04",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Cơ bản",
    "question": "Cho biến ngẫu nhiên $X \\sim B(n = 5, p = 0,4)$. Xác suất $P(X = 2)$ bằng bao nhiêu?",
    "options": [
        "0,3456",
        "0,03456",
        "0,2304",
        "0,0864"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì áp dụng công thức hàm xác suất nhị thức:\n$P(X = 2) = C_5^2 \\cdot (0,4)^2 \\cdot (1 - 0,4)^{5-2} = 10 \\cdot 0,16 \\cdot (0,6)^3 = 10 \\cdot 0,16 \\cdot 0,216 = 0,3456$.\n\nPhân tích bẫy sai:\n- Phương án B: Sai do dịch dấu phẩy thập phân.\n- Phương án C: $0,2304$ là $P(X=1)$.\n- Phương án D: $0,0864$ là kết quả khi quên nhân hệ số tổ hợp $C_5^2 = 10$ ($0,16 \\cdot 0,216 = 0,03456$).",
    "source": "Slide Week 07 tr. 15; Stat20 Mục 4.8"
})

# TN4_05: Đặc trưng độc nhất của phân phối Poisson
mcqs_4.append({
    "id": "TN4_05",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Cơ bản",
    "question": "Biến ngẫu nhiên $X \\sim Po(\\lambda = 4)$. Độ lệch chuẩn $\\sigma(X)$ của $X$ bằng bao nhiêu?",
    "options": [
        "2",
        "4",
        "16",
        "0,25"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì đối với phân phối Poisson $Po(\\lambda)$:\n- Kỳ vọng $E(X) = \\lambda = 4$.\n- Phương sai $\\operatorname{Var}(X) = \\lambda = 4$.\n- Do đó độ lệch chuẩn là căn bậc hai của phương sai: $\\sigma(X) = \\sqrt{\\operatorname{Var}(X)} = \\sqrt{4} = 2$.\n\nPhân tích bẫy sai:\n- Phương án B: 4 là phương sai $\\operatorname{Var}(X)$, câu hỏi hỏi độ lệch chuẩn $\\sigma$.\n- Phương án C: Bình phương nhầm phương sai $4^2 = 16$.\n- Phương án D: Nghịch đảo $1/4 = 0,25$.",
    "source": "Slide Week 07 tr. 16; Stat20 Mục 4.10"
})

# TN4_06: Tính xác suất Poisson P(X = 0)
# lambda = 3 -> P(X = 0) = exp(-3) ≈ 0.0498
p_06 = math.exp(-3)
mcqs_4.append({
    "id": "TN4_06",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Cơ bản",
    "question": "Trung bình mỗi phút có 3 cuộc gọi đến một tổng đài ($X \\sim Po(3)$). Xác suất để trong một phút bất kỳ KHÔNG CÓ cuộc gọi nào đến tổng đài ($P(X = 0)$) là:",
    "options": [
        "\\(e^{-3} \\approx 0,0498\\)",
        "0",
        "\\(1 - e^{-3} \\approx 0,9502\\)",
        "\\(3 \\cdot e^{-3} \\approx 0,1494\\)"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo công thức Poisson với $k = 0$:\n$P(X = 0) = \\frac{\\lambda^0 e^{-\\lambda}}{0!} = \\frac{1 \\cdot e^{-3}}{1} = e^{-3} \\approx 0,0498$ (khoảng 4,98%).\n\nPhân tích bẫy sai:\n- Phương án B: Ngộ nhận rằng trung bình có 3 cuộc gọi thì xác suất 0 cuộc gọi phải bằng 0.\n- Phương án C: $1 - e^{-3}$ là xác suất CÓ ÍT NHẤT một cuộc gọi ($P(X \\ge 1)$).\n- Phương án D: $3 e^{-3}$ là xác suất có ĐÚNG 1 cuộc gọi ($P(X = 1)$).",
    "source": "Slide Week 07 tr. 16; Stat20 Mục 4.10"
})

# TN4_07: Điều kiện xấp xỉ Poisson cho Nhị thức
mcqs_4.append({
    "id": "TN4_07",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Cơ bản",
    "question": "Phân phối Nhị thức $B(n, p)$ có thể được xấp xỉ tốt bởi phân phối Poisson $Po(\\lambda = np)$ trong điều kiện nào sau đây?",
    "options": [
        "Số phép thử $n$ rất lớn ($n \\ge 20$ hoặc $n \\ge 100$) và xác suất thành công $p$ rất nhỏ ($p \\le 0,05$), sao cho tích $\\lambda = np$ ở mức vừa phải ($np \\le 10$)",
        "Số phép thử $n$ rất nhỏ và $p$ rất gần 0,5",
        "Cả $n$ và $p$ đều rất lớn",
        "Khi $p = 0,5$ và $n \\ge 30$"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo Luật các biến cố hiếm (Law of Rare Events), phân phối Nhị thức hội tụ về Poisson khi $n \\to \\infty$ và $p \\to 0$ sao cho tích $np = \\lambda$ là một hằng số hữu hạn. Quy tắc thực hành là $n$ lớn ($n \\ge 20$ hoặc $100$) và $p$ nhỏ ($p \\le 0,05$), tích $np \\le 10$.\n\nPhân tích bẫy sai:\n- Phương án B, C: Sai điều kiện lý thuyết.\n- Phương án D: Khi $p = 0,5$ và $n \\ge 30$, ta phải dùng xấp xỉ CHUẨN (Normal approximation / CLT), không dùng Poisson vì $p$ không hề nhỏ.",
    "source": "Slide Week 07 tr. 16; Stat20 Mục 4.10"
})

# TN4_08: Thực hành tính xấp xỉ Poisson
# n = 1000, p = 0.002 -> lambda = np = 2.
# P(X = 3) approx 2^3 * exp(-2) / 6 = 8 / 6 * exp(-2) = 4/3 * 0.135335 ≈ 0.1804
p_08 = (2**3 * math.exp(-2)) / 6
mcqs_4.append({
    "id": "TN4_08",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Trung bình",
    "question": "Tỷ lệ một người bị dị ứng nghiêm trọng sau khi tiêm một loại vắc-xin là $p = 0,002$. Tiêm vắc-xin này cho $n = 1.000$ người độc lập. Sử dụng xấp xỉ Poisson, xác suất có đúng 3 người bị dị ứng xấp xỉ bằng bao nhiêu?",
    "options": [
        "0,1804",
        "0,2707",
        "0,1353",
        "0,0613"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì:\n- Ta có $n = 1.000$ rất lớn và $p = 0,002$ rất nhỏ $\\implies \\lambda = n \\cdot p = 1.000 \\cdot 0,002 = 2$.\n- Dùng xấp xỉ Poisson $Po(\\lambda = 2)$ để tính xác suất tại $k = 3$:\n$P(X = 3) \\approx \\frac{2^3 \\cdot e^{-2}}{3!} = \\frac{8 \\cdot e^{-2}}{6} = \\frac{4}{3} \\cdot e^{-2} \\approx \\frac{4}{3} \\cdot 0,135335 \\approx 0,1804$ (tức 18,04%).\n\nPhân tích bẫy sai:\n- Phương án B: 0,2707 là xác suất tại $k=1$ hoặc $k=2$ ($2^2 e^{-2} / 2 = 2 e^{-2} \\approx 0,2707$).\n- Phương án C: 0,1353 là xác suất tại $k=0$ ($e^{-2} \\approx 0,1353$).\n- Phương án D: Sai số học.",
    "source": "Slide Week 07 tr. 16; Stat20 Mục 4.10"
})

# TN4_09: So sánh phương sai Siêu bội và Nhị thức
mcqs_4.append({
    "id": "TN4_09",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Trung bình",
    "question": "Giả sử một lô hàng có $N$ sản phẩm, trong đó có $M$ phế phẩm ($p = M/N$). Rút ngẫu nhiên $n$ sản phẩm. So sánh phương sai của số phế phẩm khi rút KHÔNG HOÀN LẠI (Siêu bội) so với khi rút CÓ HOÀN LẠI (Nhị thức):",
    "options": [
        "Phương sai của Siêu bội luôn NHỎ HƠN phương sai của Nhị thức do có hệ số hiệu chỉnh tổng thể hữu hạn \\(\\frac{N-n}{N-1} < 1\\)",
        "Phương sai của Siêu bội luôn LỚN HƠN phương sai của Nhị thức",
        "Phương sai của hai phân phối luôn bằng nhau và cùng bằng $np(1-p)$",
        "Kỳ vọng của Siêu bội nhỏ hơn kỳ vọng của Nhị thức"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo công thức phương sai siêu bội:\n$\\operatorname{Var}_{HG}(X) = n p (1 - p) \\cdot \\frac{N - n}{N - 1} = \\operatorname{Var}_{Binomial}(X) \\cdot \\frac{N - n}{N - 1}$.\nVới $n > 1$, hệ số hiệu chỉnh tổng thể hữu hạn $\\frac{N-n}{N-1} < 1$. Ý nghĩa thực tế: việc rút không hoàn lại loại bỏ dần các phần tử đã lấy, làm giảm độ bất định của các lần rút sau so với việc rút có hoàn lại!\nChú ý: Cả hai đều có CÙNG kỳ vọng $E(X) = n \\frac{M}{N} = np$.\n\nPhân tích bẫy sai:\n- Phương án B: Ngược với bản chất toán học.\n- Phương án C: Bẫy ngộ nhận hai phương sai bằng nhau.\n- Phương án D: Sai vì kỳ vọng của chúng hoàn toàn bằng nhau.",
    "source": "Slide Week 07 tr. 15; Stat20 Mục 4.9"
})

# TN4_10: Kỳ vọng của phân phối Siêu bội
# N = 50, M = 10, n = 5 -> E(X) = 5 * (10 / 50) = 5 * 0.2 = 1.0
mcqs_4.append({
    "id": "TN4_10",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Cơ bản",
    "question": "Một tổ có 50 sinh viên, trong đó có 10 sinh viên giỏi. Chọn ngẫu nhiên không hoàn lại 5 sinh viên đi dự đại hội. Số sinh viên giỏi kỳ vọng có mặt trong đoàn đại biểu là:",
    "options": [
        "1,0 sinh viên",
        "0,5 sinh viên",
        "2,0 sinh viên",
        "0,2 sinh viên"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì áp dụng công thức kỳ vọng của phân phối Siêu bội $X \\sim HG(N=50, M=10, n=5)$:\n$E(X) = n \\cdot \\frac{M}{N} = 5 \\cdot \\frac{10}{50} = 5 \\cdot 0,2 = 1,0$ sinh viên.\n\nPhân tích bẫy sai:\n- Phương án B: Sai do tính $5 \\cdot 10 / 100 = 0,5$.\n- Phương án C: Sai phép tính.\n- Phương án D: 0,2 mới chỉ là tỷ lệ sinh viên giỏi trong tổ ($M/N$), chưa nhân kích thước mẫu $n=5$.",
    "source": "Slide Week 07 tr. 15; Stat20 Mục 4.9"
})

# TN4_11: Poisson với khoảng thời gian thay đổi
# Tốc độ lambda = 2 khách / phút. Khoảng thời gian 3 phút -> lambda_new = 2 * 3 = 6 khách.
# P(X = 5 trong 3 phút) = 6^5 * exp(-6) / 5! = 7776 * exp(-6) / 120 = 64.8 * exp(-6) ≈ 0.1606
p_11 = (6**5 * math.exp(-6)) / 120
mcqs_4.append({
    "id": "TN4_11",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Trung bình",
    "question": "Khách hàng đến một cây ATM với tốc độ trung bình 2 người/phút theo phân phối Poisson. Tốc độ trung bình số khách đến cây ATM trong một khoảng thời gian 3 phút là bao nhiêu và xác suất có đúng 5 khách đến trong 3 phút đó là bao nhiêu?",
    "options": [
        "\\(\\lambda' = 6\\) khách và \\(P(X = 5) \\approx 0,1606\\)",
        "\\(\\lambda' = 2\\) khách và \\(P(X = 5) \\approx 0,0361\\)",
        "\\(\\lambda' = 6\\) khách và \\(P(X = 5) \\approx 0,0803\\)",
        "\\(\\lambda' = 5\\) khách và \\(P(X = 5) \\approx 0,1755\\)"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo tính chất tỷ lệ của quá trình Poisson:\n- Khi khoảng thời gian tăng lên $t = 3$ phút, tham số Poisson mới tỷ lệ thuận theo thời gian: $\\lambda' = \\lambda \\cdot t = 2 \\times 3 = 6$ khách.\n- Xác suất có đúng 5 khách trong 3 phút này:\n$P(X = 5) = \\frac{(\\lambda')^5 \\cdot e^{-\\lambda'}}{5!} = \\frac{6^5 \\cdot e^{-6}}{120} = \\frac{7.776 \\cdot e^{-6}}{120} = 64,8 \\cdot e^{-6} \\approx 0,1606$ (tức 16,06%).\n\nPhân tích bẫy sai:\n- Phương án B: Sai do giữ nguyên $\\lambda = 2$ của 1 phút thay vì nhân với 3 phút.\n- Phương án C: Sai số học khi chia cho $5!$.\n- Phương án D: Nhầm tham số $\\lambda$ thành số khách cần tính.",
    "source": "Slide Week 07 tr. 16; Stat20 Mục 4.10"
})

# TN4_12: Tính xác suất Siêu bội cụ thể
# Hộp có 8 đỏ, 4 xanh (N=12). Rút không hoàn lại n=3.
# P(X=2 đỏ) = C(8,2) * C(4,1) / C(12,3) = 28 * 4 / 220 = 112 / 220 = 28 / 55 ≈ 0.5091
c_8_2 = math.comb(8, 2)
c_4_1 = math.comb(4, 1)
c_12_3 = math.comb(12, 3)
p_12 = (c_8_2 * c_4_1) / c_12_3
mcqs_4.append({
    "id": "TN4_12",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Trung bình",
    "question": "Một hộp có 8 viên bi đỏ và 4 viên bi xanh (tổng cộng 12 viên bi). Rút ngẫu nhiên đồng thời 3 viên bi. Xác suất để rút được đúng 2 viên bi đỏ bằng bao nhiêu?",
    "options": [
        "28/55 (khoảng 50,91%)",
        "14/55 (khoảng 25,45%)",
        "4/11 (khoảng 36,36%)",
        "2/3 (khoảng 66,67%)"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì áp dụng công thức phân phối Siêu bội $HG(N=12, M=8, n=3)$:\n- Số cách chọn 2 bi đỏ từ 8 bi đỏ: $C_8^2 = \\frac{8 \\cdot 7}{2} = 28$.\n- Số cách chọn 1 bi xanh từ 4 bi xanh: $C_4^1 = 4$.\n- Số cách chọn 3 bi bất kỳ từ 12 bi: $C_{12}^3 = \\frac{12 \\cdot 11 \\cdot 10}{6} = 220$.\n- Xác suất: $P(X = 2) = \\frac{C_8^2 \\cdot C_4^1}{C_{12}^3} = \\frac{28 \\cdot 4}{220} = \\frac{112}{220} = \\frac{28}{55} \\approx 0,5091$ (50,91%).\n\nPhân tích bẫy sai:\n- Phương án B: 14/55 là xác suất rút được đúng 1 bi đỏ ($C_8^1 C_4^2 / 220 = 8 \\cdot 6 / 220 = 48/220 = 12/55$).\n- Phương án C, D: Phép tính sai tổ hợp.",
    "source": "Slide Week 07 tr. 15; Stat20 Mục 4.9"
})

# TN4_13: Giá trị có xác suất lớn nhất (Mode) của Nhị thức
# n = 10, p = 0.3. (n+1)p = 11 * 0.3 = 3.3.
# (n+1)p - 1 = 2.3 <= k <= 3.3 -> k = 3
mcqs_4.append({
    "id": "TN4_13",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Nâng cao",
    "question": "Cho biến ngẫu nhiên $X \\sim B(n = 10, p = 0,3)$. Giá trị $k$ nào của $X$ có xác suất xuất hiện lớn nhất ($P(X = k)$ đạt cực đại - hay mốt/mode của phân phối)?",
    "options": [
        "k = 3",
        "k = 2",
        "k = 4",
        "k = 5"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì mốt (mode) của phân phối Nhị thức $B(n, p)$ là số nguyên $k$ thỏa mãn bất đẳng thức:\n$(n + 1)p - 1 \\le k \\le (n + 1)p$.\nỞ đây: $(10 + 1) \\cdot 0,3 - 1 = 3,3 - 1 = 2,3 \\le k \\le 3,3$.\nSố nguyên duy nhất nằm trong đoạn $[2,3; 3,3]$ là $k = 3$.\n(Kiểm tra xác suất: $P(X=3) \\approx 0,2668$ là lớn nhất so với $P(X=2) \\approx 0,2335$ và $P(X=4) \\approx 0,2001$).\n\nPhân tích bẫy sai:\n- Phương án B, C, D: Đều có xác suất nhỏ hơn giá trị tại $k=3$.",
    "source": "Slide Week 07 tr. 15"
})

# TN4_14: Phân phối Bernoulli - Phương sai cực đại
mcqs_4.append({
    "id": "TN4_14",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Cơ bản",
    "question": "Biến ngẫu nhiên $X \\sim Bernoulli(p)$ đạt phương sai lớn nhất khi tham số $p$ bằng bao nhiêu và giá trị phương sai cực đại đó là bao nhiêu?",
    "options": [
        "$p = 0,5$ và $\\operatorname{Var}(X) = 0,25$",
        "$p = 1,0$ và $\\operatorname{Var}(X) = 1,00$",
        "$p = 0,0$ và $\\operatorname{Var}(X) = 0,00$",
        "$p = 0,5$ và $\\operatorname{Var}(X) = 0,50$"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì hàm phương sai của Bernoulli là $f(p) = p(1 - p) = p - p^2$.\nLấy đạo hàm: $f'(p) = 1 - 2p = 0 \\iff p = 0,5$.\nTại $p = 0,5$, phương sai cực đại là: $\\operatorname{Var}_{\\max} = 0,5 \\cdot (1 - 0,5) = 0,25$.\nÝ nghĩa trực giác: Khi $p = 0,5$, kết quả là khó đoán định và bất định nhất (tung đồng xu cân đối), do đó phương sai (độ bất định) đạt đỉnh cao nhất.\n\nPhân tích bẫy sai:\n- Phương án B, C: Tại $p = 1$ hoặc $p = 0$, biến ngẫu nhiên trở thành hằng số chắc chắn, phương sai bằng 0 (cực tiểu chứ không phải cực đại!).\n- Phương án D: Nhầm $p(1-p)$ bằng 0,5 thay vì 0,25.",
    "source": "Slide Week 07 tr. 10; Stat20 Mục 4.8"
})

# TN4_15: Bài toán kiểm tra chấp nhận lô hàng (Acceptance Sampling)
# Lô 100 sp có 10 phế phẩm. Lấy n = 4. Chấp nhận nếu số phế phẩm = 0.
# P(chấp nhận) = C(90, 4) / C(100, 4)
# C(90, 4) = 90 * 89 * 88 * 87 / 24 = 2555190
# C(100, 4) = 100 * 99 * 98 * 97 / 24 = 3921225
# P = 2555190 / 3921225 ≈ 0.6516
p_15 = math.comb(90, 4) / math.comb(100, 4)
mcqs_4.append({
    "id": "TN4_15",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Nâng cao",
    "question": "Một lô hàng gồm 100 sản phẩm, trong đó có 10 sản phẩm lỗi. Quy trình nghiệm thu quy định: lấy ngẫu nhiên không hoàn lại 4 sản phẩm để kiểm tra, nếu không có bất kỳ sản phẩm lỗi nào trong 4 sản phẩm đó thì lô hàng được chấp nhận. Xác suất để lô hàng này được chấp nhận xấp xỉ bằng bao nhiêu?",
    "options": [
        "Khoảng 65,16%",
        "Khoảng 90,00%",
        "Khoảng 65,61%",
        "Khoảng 34,84%"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì áp dụng mô hình Siêu bội $HG(N=100, M=10, n=4)$:\n- Số sản phẩm tốt trong lô: $100 - 10 = 90$ sản phẩm.\n- Biến cố lô hàng được chấp nhận là lấy được cả 4 sản phẩm tốt từ 90 sản phẩm tốt:\n$P(X = 0) = \\frac{C_{90}^4 \\cdot C_{10}^0}{C_{100}^4} = \\frac{\\frac{90 \\cdot 89 \\cdot 88 \\cdot 87}{24}}{\\frac{100 \\cdot 99 \\cdot 98 \\cdot 97}{24}} = \\frac{2.555.190}{3.921.225} \\approx 0,6516$ (tức 65,16%).\n(Nếu tính theo xác suất có điều kiện: $\\frac{90}{100} \\times \\frac{89}{99} \\times \\frac{88}{98} \\times \\frac{87}{97} \\approx 0,6516$).\n\nPhân tích bẫy sai:\n- Phương án B: 90% là tỷ lệ sản phẩm tốt ban đầu ($90/100$).\n- Phương án C: $0,9^4 = 0,6561$ là kết quả nếu coi là rút CÓ HOÀN LẠI (Nhị thức).\n- Phương án D: $1 - 0,6516 = 0,3484$ là xác suất lô hàng BỊ TỪ CHỐI.",
    "source": "Slide Week 07 tr. 15; Stat20 Mục 4.9"
})

# TN4_16: Phân phối Hình học (Geometric RV)
# P(X = k) = (1-p)^{k-1} * p. p = 0.2. P(X = 3) = 0.8^2 * 0.2 = 0.64 * 0.2 = 0.128
mcqs_4.append({
    "id": "TN4_16",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Trung bình",
    "question": "Một người chơi bóng rổ ném bóng vào rổ với xác suất thành công ở mỗi lần ném độc lập là $p = 0,2$. Người này ném liên tục cho đến khi bóng vào rổ lần đầu tiên thì dừng lại. Gọi $X$ là số lần ném cho đến khi thành công lần đầu. Xác suất người này phải ném đúng 3 lần ($P(X = 3)$) bằng bao nhiêu?",
    "options": [
        "0,128",
        "0,008",
        "0,048",
        "0,512"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì để ném thành công lần đầu ở lần thứ 3, hai lần đầu tiên phải ném trượt và lần thứ 3 ném trúng:\n- Xác suất trượt mỗi lần: $1 - 0,2 = 0,8$.\n- Xác suất theo phân phối Hình học: $P(X = 3) = (1 - p)^{3-1} \\cdot p = (0,8)^2 \\cdot 0,2 = 0,64 \\cdot 0,2 = 0,128$ (tức 12,8%).\n\nPhân tích bẫy sai:\n- Phương án B: $0,2^3 = 0,008$ là xác suất cả 3 lần đều trúng.\n- Phương án C: Sai do nhân $3 \\cdot 0,8 \\cdot 0,2 = 0,48$.\n- Phương án D: $0,8^3 = 0,512$ là xác suất cả 3 lần đều trượt.",
    "source": "Stat20 Mục 4.8"
})

# TN4_17: Tính chất cộng của phân phối Poisson
# X1 ~ Po(lambda1 = 2), X2 ~ Po(lambda2 = 3) độc lập -> X1 + X2 ~ Po(2 + 3 = 5)
mcqs_4.append({
    "id": "TN4_17",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Cơ bản",
    "question": "Cho hai biến ngẫu nhiên độc lập $X_1 \\sim Po(\\lambda_1 = 2)$ và $X_2 \\sim Po(\\lambda_2 = 3)$. Tổng $Y = X_1 + X_2$ tuân theo phân phối nào?",
    "options": [
        "Phân phối Poisson với tham số \\(\\lambda = 5\\)",
        "Phân phối Poisson với tham số \\(\\lambda = 6\\)",
        "Phân phối Nhị thức với $n = 5$",
        "Phân phối Chuẩn với trung bình 5 và phương sai 25"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo tính chất tự nhiên (tính ổn định / reproductive property) của phân phối Poisson: Tổng của hai biến ngẫu nhiên Poisson độc lập là một biến ngẫu nhiên Poisson có tham số bằng tổng các tham số:\n$X_1 + X_2 \\sim Po(\\lambda_1 + \\lambda_2) = Po(2 + 3) = Po(5)$.\n\nPhân tích bẫy sai:\n- Phương án B: Sai do nhân các tham số $2 \\cdot 3 = 6$.\n- Phương án C, D: Sai phân phối.",
    "source": "Slide Week 07 tr. 16"
})

# TN4_18: Xác suất nhị thức P(X >= 1)
# n = 4, p = 0.5. P(X >= 1) = 1 - P(X = 0) = 1 - 0.5^4 = 1 - 0.0625 = 0.9375 = 15/16
mcqs_4.append({
    "id": "TN4_18",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Cơ bản",
    "question": "Tung một đồng xu cân đối đồng chất 4 lần. Xác suất để xuất hiện MẶT NGỬA ÍT NHẤT MỘT LẦN bằng bao nhiêu?",
    "options": [
        "15/16 (93,75%)",
        "1/16 (6,25%)",
        "1/2 (50%)",
        "3/4 (75%)"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì biến cố đối của 'ít nhất một mặt ngửa' là 'không có mặt ngửa nào' (cả 4 lần đều sấp):\n$P(X = 0) = (0,5)^4 = \\frac{1}{16} = 0,0625$.\nDo đó: $P(X \\ge 1) = 1 - P(X = 0) = 1 - \\frac{1}{16} = \\frac{15}{16} = 0,9375$ (93,75%).\n\nPhân tích bẫy sai:\n- Phương án B: 1/16 là xác suất của biến cố đối (không có lần nào ngửa).\n- Phương án C: 1/2 là xác suất của 1 lần tung đơn lẻ.\n- Phương án D: Ước lượng cảm tính.",
    "source": "Slide Week 07 tr. 15; Stat20 Mục 4.8"
})

# TN4_19: Điều kiện để phân phối Siêu bội xấp xỉ phân phối Nhị thức
mcqs_4.append({
    "id": "TN4_19",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Trung bình",
    "question": "Trong thực tế điều tra xã hội học và chọn mẫu, phân phối Siêu bội $HG(N, M, n)$ (rút không hoàn lại) có thể được xấp xỉ an toàn bằng phân phối Nhị thức $B(n, p = M/N)$ khi thỏa mãn điều kiện kinh nghiệm nào?",
    "options": [
        "Kích thước mẫu $n$ chiếm tỷ lệ rất nhỏ so với tổng thể $N$ (thường là \\(n/N \\le 0,05\\) hoặc \\(n/N \\le 0,10\\))",
        "Khi kích thước mẫu $n$ bằng đúng kích thước tổng thể $N$",
        "Khi số lượng đặc trưng $M$ phải lớn hơn một nửa tổng thể ($M > N/2$)",
        "Khi kích thước mẫu $n > 100$ bất kể tổng thể $N$ là bao nhiêu"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì khi tỷ lệ lấy mẫu $n/N \\le 0,05$ (mẫu chiếm dưới 5% tổng thể), hệ số hiệu chỉnh tổng thể hữu hạn $\\frac{N-n}{N-1} \\approx 1$. Việc rút một vài cá thể từ một tổng thể khổng lồ làm thay đổi xác suất của các cá thể còn lại không đáng kể, do đó bài toán rút không hoàn lại xấp xỉ như rút có hoàn lại (Nhị thức).\n\nPhân tích bẫy sai:\n- Phương án B: Khi $n = N$, ta lấy hết toàn bộ tổng thể, không còn tính ngẫu nhiên.\n- Phương án C, D: Đều sai quy tắc xấp xỉ thống kê chuẩn.",
    "source": "Slide Week 07 tr. 15; Stat20 Mục 4.9"
})

# TN4_20: Poisson P(X <= 1)
# lambda = 1. P(X <= 1) = P(X=0) + P(X=1) = exp(-1) + 1 * exp(-1) = 2 exp(-1) ≈ 2 * 0.367879 = 0.7358
p_20 = 2 * math.exp(-1)
mcqs_4.append({
    "id": "TN4_20",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Trung bình",
    "question": "Một tổng đài nhận trung bình 1 cuộc gọi báo hỏng mỗi giờ ($X \\sim Po(\\lambda = 1)$). Xác suất để trong một giờ tổng đài nhận ĐƯỢC TỐI ĐA 1 CUỘC GỌI ($P(X \\le 1)$) bằng bao nhiêu?",
    "options": [
        "\\(2e^{-1} \\approx 0,7358\\)",
        "\\(e^{-1} \\approx 0,3679\\)",
        "\\(1 - 2e^{-1} \\approx 0,2642\\)",
        "0,5000"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì 'tối đa 1 cuộc gọi' nghĩa là có 0 cuộc gọi hoặc đúng 1 cuộc gọi:\n$P(X \\le 1) = P(X = 0) + P(X = 1) = \\frac{1^0 e^{-1}}{0!} + \\frac{1^1 e^{-1}}{1!} = e^{-1} + e^{-1} = 2e^{-1} \\approx 2 \\cdot 0,367879 \\approx 0,7358$ (73,58%).\n\nPhân tích bẫy sai:\n- Phương án B: $e^{-1} \\approx 0,3679$ chỉ tính riêng trường hợp đúng 0 hoặc đúng 1 cuộc gọi.\n- Phương án C: $1 - 2e^{-1} \\approx 0,2642$ là xác suất có TỪ 2 CUỘC GỌI TRỞ LÊN ($P(X \\ge 2)$).\n- Phương án D: Đoán mò.",
    "source": "Slide Week 07 tr. 16; Stat20 Mục 4.10"
})

# TN4_21: Phương sai Siêu bội tính bằng số cụ thể
# N = 10, M = 4, n = 3. p = 0.4.
# Var = n * p * (1-p) * (N-n)/(N-1) = 3 * 0.4 * 0.6 * (10-3)/(10-1) = 0.72 * 7/9 = 0.72 * 0.777777 = 0.56
var_21 = 3 * 0.4 * 0.6 * (7 / 9)
mcqs_4.append({
    "id": "TN4_21",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Nâng cao",
    "question": "Một nhóm có 10 thành viên, gồm 4 nữ và 6 nam. Chọn ngẫu nhiên không hoàn lại 3 thành viên để lập ban cán sự. Gọi $X$ là số thành viên nữ được chọn ($X \\sim HG(N=10, M=4, n=3)$). Phương sai $\\operatorname{Var}(X)$ bằng bao nhiêu?",
    "options": [
        "0,56",
        "0,72",
        "1,20",
        "0,748"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì áp dụng công thức phương sai của phân phối Siêu bội:\n$\\operatorname{Var}(X) = n \\cdot \\frac{M}{N} \\cdot \\left(1 - \\frac{M}{N}\\right) \\cdot \\frac{N - n}{N - 1}$.\nỞ đây: $n = 3, N = 10, M = 4 \\implies p = 4/10 = 0,4$.\n- Phương sai nếu là Nhị thức: $n p (1 - p) = 3 \\cdot 0,4 \\cdot 0,6 = 0,72$.\n- Hệ số hiệu chỉnh FPC: $\\frac{N - n}{N - 1} = \\frac{10 - 3}{10 - 1} = \\frac{7}{9}$.\n- Phương sai Siêu bội: $\\operatorname{Var}(X) = 0,72 \\cdot \\frac{7}{9} = 0,56$.\n\nPhân tích bẫy sai:\n- Phương án B: 0,72 là phương sai khi coi là rút CÓ HOÀN LẠI (quên nhân hệ số hiệu chỉnh FPC 7/9).\n- Phương án C: 1,20 là kỳ vọng $E(X) = 3 \\cdot 0,4 = 1,20$.\n- Phương án D: $\\sqrt{0,56} \\approx 0,7483$ là độ lệch chuẩn $\\sigma(X)$, không phải phương sai.",
    "source": "Slide Week 07 tr. 15; Stat20 Mục 4.9"
})

# TN4_22: Xấp xỉ Poisson - Xác suất có ít nhất 1 lỗi
# n = 500, p = 0.004 -> lambda = 500 * 0.004 = 2.
# P(X >= 1) = 1 - exp(-2) ≈ 1 - 0.135335 = 0.8647
p_22 = 1 - math.exp(-2)
mcqs_4.append({
    "id": "TN4_22",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Trung bình",
    "question": "Một cuốn sách có 500 trang. Xác suất một trang bất kỳ có lỗi in là $p = 0,004$, các trang độc lập nhau. Dùng xấp xỉ Poisson, xác suất để trong toàn bộ cuốn sách có ÍT NHẤT MỘT TRANG BỊ LỖI IN là bao nhiêu?",
    "options": [
        "Khoảng 86,47%",
        "Khoảng 13,53%",
        "Khoảng 27,07%",
        "Khoảng 99,99%"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì:\n- Tham số Poisson: $\\lambda = n \\cdot p = 500 \\cdot 0,004 = 2$.\n- Biến cố đối của 'ít nhất một trang bị lỗi' là 'không có trang nào bị lỗi' ($X = 0$):\n$P(X = 0) = e^{-\\lambda} = e^{-2} \\approx 0,135335$.\n- Xác suất có ít nhất một trang bị lỗi:\n$P(X \\ge 1) = 1 - P(X = 0) = 1 - e^{-2} \\approx 1 - 0,135335 = 0,864665 \\approx 86,47\\%$.\n\nPhân tích bẫy sai:\n- Phương án B: 13,53% là xác suất KHÔNG CÓ trang nào lỗi ($P(X=0)$).\n- Phương án C: 27,07% là xác suất có đúng 1 trang lỗi ($2 e^{-2}$).\n- Phương án D: Ước lượng cảm tính sai.",
    "source": "Slide Week 07 tr. 16; Stat20 Mục 4.10"
})

# TN4_23: Nhận diện mô hình tổng quát
mcqs_4.append({
    "id": "TN4_023",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Cơ bản",
    "question": "Bảng tóm tắt nào sau đây về các mô hình xác suất rời rạc là HOÀN TOÀN CHÍNH XÁC?",
    "options": [
        "Nhị thức: Rút có hoàn lại, các lần rút độc lập; Siêu bội: Rút không hoàn lại từ tổng thể hữu hạn, các lần rút phụ thuộc; Poisson: Đếm biến cố hiếm trong khoảng liên tục",
        "Nhị thức: Rút không hoàn lại; Siêu bội: Rút có hoàn lại; Poisson: Biến liên tục",
        "Nhị thức: Có kỳ vọng bằng phương sai; Poisson: Có phương sai luôn nhỏ hơn kỳ vọng",
        "Siêu bội: Các lần thử độc lập nhau; Nhị thức: Các lần thử phụ thuộc nhau"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì đây là phân biệt cốt lõi nhất giữa 3 mô hình rời rạc kinh điển (Slide Week 07 và Stat20 Ch.4):\n- Nhị thức: số phép thử $n$ cố định, xác suất $p$ không đổi (rút có hoàn lại), các phép thử độc lập.\n- Siêu bội: kích thước tổng thể $N$ và mẫu $n$ cố định, rút không hoàn lại nên xác suất thay đổi (phụ thuộc).\n- Poisson: đếm số lần xuất hiện của biến cố trong khoảng liên tục, kỳ vọng và phương sai luôn bằng nhau ($\\lambda$).\n\nPhân tích bẫy sai:\n- Phương án B, C, D: Đều đảo ngược hoặc sai lệch các đặc tính căn bản.",
    "source": "Slide Week 07 tr. 15-16; Stat20 Mục 4.8 - 4.10"
})

# Fix ID of last question if needed to be TN4_23
mcqs_4[-1]["id"] = "TN4_23"

print(f"Total MCQs for Topic 4: {len(mcqs_4)}")

with open('content/mcq_topic_4.json', 'w', encoding='utf-8') as f:
    json.dump(mcqs_4, f, ensure_ascii=False, indent=2)
print("Saved content/mcq_topic_4.json")
