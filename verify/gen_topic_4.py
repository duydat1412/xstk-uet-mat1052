# Topic 4: Các phân phối rời rạc: Nhị thức, Siêu bội & Poisson (TL4_1 -> TL4_8)
import math
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_topic_4():
    exercises = []

    # TL4_1 (Cơ bản)
    exercises.append({
        "id": "TL4_1", "topicId": 4, "level": "Cơ bản",
        "title": "Phân phối Nhị thức: Công thức Bernoulli, Kỳ vọng và Phương sai",
        "problem": "Một bài thi trắc nghiệm gồm 10 câu hỏi độc lập. Một sinh viên ôn tập khá tốt nên xác suất trả lời đúng mỗi câu là $p = 0{,}7$.<br>"
                   "1. Gọi $X$ là số câu trả lời đúng của sinh viên này. Cho biết tên phân phối và các tham số của $X$.<br>"
                   "2. Tính xác suất để sinh viên đó trả lời đúng chính xác 7 câu ($P(X = 7)$).<br>"
                   "3. Tính kỳ vọng $E(X)$, phương sai $\\operatorname{Var}(X)$ và độ lệch chuẩn $\\operatorname{SD}(X)$.",
        "analysis": "X tuân theo phân phối Nhị thức B(n=10, p=0.7). Dùng công thức P(X = k) = C(n, k) * p^k * (1-p)^(n-k). E(X) = np, Var(X) = np(1-p), SD(X) = sqrt(Var).",
        "hints": [
            "10 câu hỏi độc lập, cùng xác suất đúng p = 0.7 -> Phân phối Nhị thức B(10, 0.7).",
            "P(X = 7) = C(10, 7) * 0.7^7 * 0.3^3.",
            "E(X) = 10 * 0.7 = 7. Var(X) = 10 * 0.7 * 0.3 = 2.1."
        ],
        "steps": [
            "<b>Bước 1: Nhận diện phân phối và tham số `[+0,25đ]`</b><br>"
            "Các câu hỏi là các phép thử Bernoulli độc lập, mỗi câu chỉ có 2 kết quả (đúng/sai) với xác suất đúng không đổi $p = 0{,}7$.<br>"
            "Do đó, $X$ tuân theo <b>Phân phối Nhị thức</b> (Binomial distribution):<br>"
            "$$X \\sim B(n = 10,\\; p = 0{,}7)$$",
            "<b>Bước 2: Tính xác suất đúng đúng 7 câu P(X = 7) `[+0,40đ]`</b><br>"
            "Áp dụng công thức hàm khối xác suất nhị thức:<br>"
            "$$P(X = k) = C_n^k p^k (1 - p)^{n - k}$$"
            "Với $k = 7$:<br>"
            "$$P(X = 7) = C_{10}^7 \\times (0{,}7)^7 \\times (0{,}3)^{10 - 7} = 120 \\times (0{,}7)^7 \\times (0{,}3)^3$$"
            "$$P(X = 7) = 120 \\times 0{,}0823543 \\times 0{,}027 \\approx 0{,}2668\\text{ (26{,}68\\%)}$$",
            "<b>Bước 3: Tính kỳ vọng, phương sai và độ lệch chuẩn `[+0,35đ]`</b><br>"
            "- Kỳ vọng (số câu đúng trung bình):<br>"
            "$$E(X) = n \\cdot p = 10 \\times 0{,}7 = 7{,}0\\text{ (câu)}$$"
            "- Phương sai:<br>"
            "$$\\operatorname{Var}(X) = n \\cdot p \\cdot (1 - p) = 10 \\times 0{,}7 \\times 0{,}3 = 2{,}10\\text{ (câu}^2\\text{)}$$"
            "- Độ lệch chuẩn:<br>"
            "$$\\operatorname{SD}(X) = \\sqrt{\\operatorname{Var}(X)} = \\sqrt{2{,}10} \\approx 1{,}4491\\text{ (câu)}$$"
        ],
        "pro_tips": "Nhớ công thức tổ hợp $C_{10}^7 = C_{10}^3 = \\frac{10 \\times 9 \\times 8}{3 \\times 2 \\times 1} = 120$ để tính nhẩm nhanh không cần máy tính.",
        "pitfalls": "Quên số hạng $C_n^k$ mà chỉ tính $p^k(1-p)^{n-k}$, hoặc bấm nhầm lũy thừa $(0{,}3)^3$."
    })

    # TL4_2 (Cơ bản)
    exercises.append({
        "id": "TL4_2", "topicId": 4, "level": "Cơ bản",
        "title": "Phân phối Siêu bội: Rút mẫu không hoàn lại từ tập hữu hạn",
        "problem": "Một lô hàng gồm $N = 30$ linh kiện điện tử, trong đó có $M = 6$ linh kiện bị lỗi. Nhân viên kiểm toán chọn ngẫu nhiên $n = 4$ linh kiện không hoàn lại để kiểm tra.<br>"
                   "1. Gọi $X$ là số linh kiện lỗi được chọn ra. Xác định phân phối xác suất của $X$.<br>"
                   "2. Tính xác suất để trong 4 linh kiện chọn ra có đúng 1 linh kiện lỗi ($P(X = 1)$).<br>"
                   "3. Tính xác suất để chọn được ít nhất 1 linh kiện lỗi ($P(X \\ge 1)$).",
        "analysis": "Rút không hoàn lại n=4 từ tập N=30 có M=6 phần tử đặc biệt -> Siêu bội Hypergeometric HG(N=30, M=6, n=4). P(X=k) = C(M, k)*C(N-M, n-k) / C(N, n). P(X>=1) = 1 - P(X=0).",
        "hints": [
            "Rút không hoàn lại từ tập hữu hạn là dấu hiệu đặc trưng của phân phối Siêu bội.",
            "P(X = 1) = [C(6, 1) * C(24, 3)] / C(30, 4).",
            "Biến cố đối của 'ít nhất 1 lỗi' là 'không có lỗi nào' (X = 0)."
        ],
        "steps": [
            "<b>Bước 1: Xác định phân phối của X `[+0,25đ]`</b><br>"
            "Vì các linh kiện được chọn <i>không hoàn lại</i> từ tập hữu hạn gồm 30 linh kiện (gồm 6 lỗi và 24 tốt), biến ngẫu nhiên $X$ tuân theo <b>Phân phối Siêu bội</b> (Hypergeometric):<br>"
            "$$X \\sim HG(N = 30,\\; M = 6,\\; n = 4)$$",
            "<b>Bước 2: Tính xác suất có đúng 1 linh kiện lỗi P(X = 1) `[+0,40đ]`</b><br>"
            "Áp dụng công thức phân phối siêu bội:<br>"
            "$$P(X = k) = \\frac{C_M^k C_{N - M}^{n - k}}{C_N^n}$$"
            "Với $k = 1$:<br>"
            "- Chọn 1 linh kiện lỗi từ 6 linh kiện lỗi: $C_6^1 = 6$ cách.<br>"
            "- Chọn $4 - 1 = 3$ linh kiện tốt từ $30 - 6 = 24$ linh kiện tốt: $C_{24}^3 = \\frac{24 \\times 23 \\times 22}{6} = 2024$ cách.<br>"
            "- Chọn 4 linh kiện bất kỳ từ 30 linh kiện: $C_{30}^4 = \\frac{30 \\times 29 \\times 28 \\times 27}{24} = 27405$ cách.<br>"
            "$$P(X = 1) = \\frac{6 \\times 2024}{27405} = \\frac{12144}{27405} \\approx 0{,}4431\\text{ (44{,}31\\%)}$$",
            "<b>Bước 3: Tính xác suất có ít nhất 1 linh kiện lỗi P(X ≥ 1) `[+0,35đ]`</b><br>"
            "Sử dụng biến cố đối: Biến cố không có linh kiện lỗi nào ($X = 0$):<br>"
            "$$P(X = 0) = \\frac{C_6^0 C_{24}^4}{C_{30}^4} = \\frac{1 \\times 10626}{27405} \\approx 0{,}3877$$"
            "Do đó:<br>"
            "$$P(X \\ge 1) = 1 - P(X = 0) = 1 - \\frac{10626}{27405} = \\frac{16779}{27405} \\approx 0{,}6123\\text{ (61{,}23\\%)}$$"
        ],
        "pro_tips": "Bất cứ khi nào gặp cụm từ 'ít nhất 1' ($X \\ge 1$), hãy nghĩ ngay đến biến cố đối $1 - P(X = 0)$ để rút ngắn 80% thời gian tính toán!",
        "pitfalls": "Dùng nhầm công thức Nhị thức cho bài toán rút không hoàn lại khi kích thước mẫu $n=4$ so với $N=30$ khá lớn ($4/30 \\approx 13{,}3\\% > 5\\%$)."
    })

    # TL4_3 (Cơ bản)
    exercises.append({
        "id": "TL4_3", "topicId": 4, "level": "Cơ bản",
        "title": "Phân phối Poisson: Biến cố hiếm trong khoảng thời gian liên tục",
        "problem": "Số lượng cuộc gọi cấp cứu gọi đến một trung tâm y tế trong 1 giờ là một biến ngẫu nhiên tuân theo phân phối Poisson với cường độ trung bình $\\lambda = 2$ cuộc gọi/giờ.<br>"
                   "1. Viết công thức hàm khối xác suất $P(X = k)$ của số cuộc gọi trong 1 giờ.<br>"
                   "2. Tính xác suất trong 1 giờ có đúng 3 cuộc gọi cấp cứu ($P(X = 3)$).<br>"
                   "3. Tính xác suất trong 1 giờ có ít nhất 1 cuộc gọi cấp cứu ($P(X \\ge 1)$).",
        "analysis": "X ~ Pois(lambda = 2). Công thức P(X = k) = e^(-lambda) * lambda^k / k!. P(X >= 1) = 1 - P(X = 0) = 1 - e^(-lambda).",
        "hints": [
            "Công thức Poisson: P(X = k) = e^(-lambda) * lambda^k / k! với k = 0, 1, 2, ...",
            "P(X = 3) = e^(-2) * 2^3 / 3! = 8 * e^(-2) / 6.",
            "e^(-2) approx 0.135335."
        ],
        "steps": [
            "<b>Bước 1: Viết công thức pmf của phân phối Poisson `[+0,25đ]`</b><br>"
            "Biến ngẫu nhiên $X \\sim \\text{Poisson}(\\lambda = 2)$. Hàm khối xác suất là:<br>"
            "$$P(X = k) = \\frac{e^{-\\lambda} \\lambda^k}{k!} = \\frac{e^{-2} \\cdot 2^k}{k!}\\quad (k = 0, 1, 2, \\dots)$$",
            "<b>Bước 2: Tính xác suất có đúng 3 cuộc gọi P(X = 3) `[+0,40đ]`</b><br>"
            "Thay $k = 3$ vào công thức:<br>"
            "$$P(X = 3) = \\frac{e^{-2} \\cdot 2^3}{3!} = \\frac{e^{-2} \\times 8}{6} = \\frac{4}{3} e^{-2}$$"
            "Với $e^{-2} \\approx 0{,}135335$:<br>"
            "$$P(X = 3) = \\frac{4}{3} \\times 0{,}135335 \\approx 0{,}1804\\text{ (18{,}04\\%)}$$",
            "<b>Bước 3: Tính xác suất có ít nhất 1 cuộc gọi P(X ≥ 1) `[+0,35đ]`</b><br>"
            "Sử dụng biến cố đối: Không có cuộc gọi nào trong 1 giờ ($k = 0$):<br>"
            "$$P(X = 0) = \\frac{e^{-2} \\cdot 2^0}{0!} = \\frac{e^{-2} \\times 1}{1} = e^{-2} \\approx 0{,}1353$$"
            "Do đó:<br>"
            "$$P(X \\ge 1) = 1 - P(X = 0) = 1 - e^{-2} = 1 - 0{,}1353 = 0{,}8647\\text{ (86{,}47\\%)}$$"
        ],
        "pro_tips": "Đối với phân phối Poisson, luôn ghi nhớ tính chất đặc biệt: Kỳ vọng bằng đúng Phương sai: $E(X) = \\operatorname{Var}(X) = \\lambda$.",
        "pitfalls": "Tính $0! = 0$ dẫn đến chia cho 0 (nhớ rằng quy ước toán học $0! = 1$)."
    })

    # TL4_4 (Trung bình)
    exercises.append({
        "id": "TL4_4", "topicId": 4, "level": "Trung bình",
        "title": "So sánh mẫu có hoàn lại (Nhị thức) và không hoàn lại (Siêu bội)",
        "problem": "Một thùng hàng chứa 20 linh kiện, trong đó có 4 linh kiện lỗi và 16 linh kiện đạt chuẩn. Người kiểm tra lấy ngẫu nhiên 3 linh kiện.<br>"
                   "1. Nếu việc lấy mẫu là <b>CÓ hoàn lại</b>: Tính xác suất chọn được đúng 1 linh kiện lỗi.<br>"
                   "2. Nếu việc lấy mẫu là <b>KHÔNG hoàn lại</b>: Tính xác suất chọn được đúng 1 linh kiện lỗi.<br>"
                   "3. So sánh sai số giữa hai kết quả và nêu quy tắc kinh nghiệm khi nào được phép dùng Nhị thức để xấp xỉ Siêu bội.",
        "analysis": "Có hoàn lại: Nhị thức B(n=3, p=4/20=0.2). Không hoàn lại: Siêu bội HG(N=20, M=4, n=3). So sánh P_B(X=1) và P_HG(X=1). Quy tắc n/N <= 0.05.",
        "hints": [
            "Có hoàn lại: p = 4/20 = 0.2 không đổi qua các lần rút. Dùng B(3, 0.2).",
            "Không hoàn lại: Dùng C(4, 1)*C(16, 2) / C(20, 3).",
            "Quy tắc kinh nghiệm: Khi cỡ mẫu n chiếm không quá 5% tổng thể (n/N <= 0.05)."
        ],
        "steps": [
            "<b>Bước 1: Trường hợp CÓ hoàn lại (Mô hình Nhị thức) `[+0,35đ]`</b><br>"
            "Vì mỗi lần rút xong đều trả lại thùng, xác suất rút trúng linh kiện lỗi ở mỗi lần là cố định:<br>"
            "$$p = \\frac{4}{20} = 0{,}20$$"
            "Số linh kiện lỗi $X_1 \\sim B(n = 3,\\; p = 0{,}20)$:<br>"
            "$$P(X_1 = 1) = C_3^1 (0{,}20)^1 (0{,}80)^2 = 3 \\times 0{,}20 \\times 0{,}64 = 0{,}3840\\text{ (38{,}40\\%)}$$",
            "<b>Bước 2: Trường hợp KHÔNG hoàn lại (Mô hình Siêu bội) `[+0,35đ]`</b><br>"
            "Số linh kiện lỗi $X_2 \\sim HG(N = 20,\\; M = 4,\\; n = 3)$:<br>"
            "- $C_4^1 = 4$<br>"
            "- $C_{16}^2 = \\frac{16 \\times 15}{2} = 120$<br>"
            "- $C_{20}^3 = \\frac{20 \\times 19 \\times 18}{6} = 1140$<br>"
            "$$P(X_2 = 1) = \\frac{C_4^1 C_{16}^2}{C_{20}^3} = \\frac{4 \\times 120}{1140} = \\frac{480}{1140} = \\frac{8}{19} \\approx 0{,}4211\\text{ (42{,}11\\%)}$$",
            "<b>Bước 3: So sánh và Nêu quy tắc xấp xỉ `[+0,30đ]`</b><br>"
            "- Sai số giữa hai mô hình: $|0{,}4211 - 0{,}3840| = 0{,}0371$ (chênh lệch khoảng $3{,}71\\%$).<br>"
            "- <b>Nguyên nhân sai số đáng kể:</b> Tỉ lệ kích thước mẫu so với tổng thể ở đây là $\\frac{n}{N} = \\frac{3}{20} = 15\\% > 5\\%$. Việc rút không hoàn lại làm thay đổi đáng kể xác suất của các lần rút sau.<br>"
            "- <b>Quy tắc kinh nghiệm:</b> Chỉ được phép dùng phân phối Nhị thức để xấp xỉ phân phối Siêu bội khi cỡ mẫu rất nhỏ so với quy mô tổng thể, cụ thể là khi: $$\\frac{n}{N} \\le 0{,}05\\text{ (hay } n \\le 5\\% N\\text{)}$$"
        ],
        "pro_tips": "Khi $N$ rất lớn (ví dụ $N = 10000$), việc rút có hoàn lại hay không hoàn lại cho kết quả hầu như giống hệt nhau.",
        "pitfalls": "Áp dụng tùy tiện phân phối Nhị thức khi kích thước mẫu $n$ chiếm tỉ trọng lớn trong tổng thể $N$ ($n/N > 0{,}05$)."
    })

    # TL4_5 (Trung bình)
    exercises.append({
        "id": "TL4_5", "topicId": 4, "level": "Trung bình",
        "title": "Xấp xỉ Poisson cho phân phối Nhị thức với n lớn và p nhỏ",
        "problem": "Một nhà máy sản xuất chip bán dẫn có tỉ lệ chip bị lỗi vi mạch rất nhỏ là $p = 0{,}002$. Một kiện hàng gồm $n = 1000$ con chip được xuất xưởng.<br>"
                   "1. Nêu điều kiện để xấp xỉ phân phối Nhị thức bằng phân phối Poisson và xác định tham số $\\lambda$.<br>"
                   "2. Dùng xấp xỉ Poisson, tính xác suất để kiện hàng có đúng 3 chip lỗi.<br>"
                   "3. Tính xác suất để kiện hàng có nhiều hơn 2 chip lỗi ($P(X > 2)$).",
        "analysis": "X ~ B(n=1000, p=0.002). Điều kiện: n >= 100, p <= 0.01, np = lambda = 2 (np < 10). Xấp xỉ Pois(lambda=2). P(X=3) = e^(-2)*8/6. P(X > 2) = 1 - [P(0) + P(1) + P(2)].",
        "hints": [
            "Tham số lambda = n * p = 1000 * 0.002 = 2.",
            "P(X = 3) theo Poisson: e^(-2) * 2^3 / 3!.",
            "P(X > 2) = 1 - P(X <= 2) = 1 - [P(X=0) + P(X=1) + P(X=2)]."
        ],
        "steps": [
            "<b>Bước 1: Kiểm tra điều kiện xấp xỉ Poisson và tính λ `[+0,30đ]`</b><br>"
            "Số chip lỗi thực tế tuân theo $X \\sim B(n = 1000,\\; p = 0{,}002)$.<br>"
            "Thỏa mãn các điều kiện của Định lý biến cố hiếm Poisson:<br>"
            "- Số phép thử rất lớn: $n = 1000 \\ge 100$.<br>"
            "- Xác suất thành công rất bé: $p = 0{,}002 \\le 0{,}01$.<br>"
            "- Tích $\\lambda = n \\cdot p = 1000 \\times 0{,}002 = 2{,}0$ là một hằng số vừa phải ($np < 10$).<br>"
            "Do đó, ta xấp xỉ $X \\approx \\text{Poisson}(\\lambda = 2)$.",
            "<b>Bước 2: Tính xác suất có đúng 3 chip lỗi `[+0,35đ]`</b><br>"
            "$$P(X = 3) \\approx \\frac{e^{-2} \\cdot 2^3}{3!} = \\frac{8}{6} e^{-2} = \\frac{4}{3} \\times 0{,}135335 \\approx 0{,}1804\\text{ (18{,}04\\%)}$$"
            "<i>(Đối chiếu: Công thức chính xác Nhị thức $C_{1000}^3 (0{,}002)^3 (0{,}998)^{997} \\approx 0{,}1806$, sai số chỉ $0{,}0002$!)</i>",
            "<b>Bước 3: Tính xác suất có nhiều hơn 2 chip lỗi P(X > 2) `[+0,35đ]`</b><br>"
            "Ta tính biến cố đối $P(X \\le 2) = P(X = 0) + P(X = 1) + P(X = 2)$:<br>"
            "- $P(X = 0) = \\frac{e^{-2} \\cdot 2^0}{0!} = e^{-2} \\approx 0{,}1353$<br>"
            "- $P(X = 1) = \\frac{e^{-2} \\cdot 2^1}{1!} = 2 e^{-2} \\approx 0{,}2707$<br>"
            "- $P(X = 2) = \\frac{e^{-2} \\cdot 2^2}{2!} = 2 e^{-2} \\approx 0{,}2707$<br>"
            "Tổng xác suất tích lũy đến 2:<br>"
            "$$P(X \\le 2) = e^{-2}(1 + 2 + 2) = 5 e^{-2} = 5 \\times 0{,}135335 \\approx 0{,}6767$$"
            "Vậy xác suất có nhiều hơn 2 chip lỗi là:<br>"
            "$$P(X > 2) = 1 - P(X \\le 2) = 1 - 0{,}6767 = 0{,}3233\\text{ (32{,}33\\%)}$$"
        ],
        "pro_tips": "Khi tính tổng các số hạng Poisson: $e^{-\\lambda} \\sum \\frac{\\lambda^k}{k!}$, hãy rút thừa số chung $e^{-\\lambda}$ ra ngoài để bấm máy tính 1 lần duy nhất, tránh sai số tích lũy.",
        "pitfalls": "Nhầm lẫn giữa 'nhiều hơn 2' ($X > 2$, tức lấy từ 3 trở lên) và 'ít nhất 2' ($X \\ge 2$, tức lấy từ 2 trở lên)."
    })

    # TL4_6 (Trung bình)
    exercises.append({
        "id": "TL4_6", "topicId": 4, "level": "Trung bình",
        "title": "Phân phối Poisson theo khoảng thời gian tỷ lệ λt",
        "problem": "Số vụ tai nạn giao thông tại một ngã tư được mô hình hóa theo phân phối Poisson với tần suất trung bình 3 vụ trong 1 tháng (3 vụ/tháng). Giả sử số vụ tai nạn trong các khoảng thời gian không giao nhau là độc lập.<br>"
                   "1. Tính xác suất để trong nửa tháng (0,5 tháng) xảy ra đúng 1 vụ tai nạn.<br>"
                   "2. Tính xác suất để trong 2 tháng xảy ra ít nhất 4 vụ tai nạn.",
        "analysis": "Cường độ Poisson tỷ lệ thuận với độ dài khoảng thời gian: lambda_t = lambda * t. Trong 0.5 tháng: lambda_1 = 3 * 0.5 = 1.5. Trong 2 tháng: lambda_2 = 3 * 2 = 6. Dùng biến cố đối cho câu 2.",
        "hints": [
            "Khoảng thời gian 0.5 tháng: lambda = 3 * 0.5 = 1.5.",
            "Khoảng thời gian 2 tháng: lambda = 3 * 2 = 6.",
            "P(Y >= 4) = 1 - [P(Y=0) + P(Y=1) + P(Y=2) + P(Y=3)] với lambda = 6."
        ],
        "steps": [
            "<b>Bước 1: Xác định tham số Poisson cho nửa tháng `[+0,35đ]`</b><br>"
            "Cường độ cơ sở: $\\lambda = 3$ vụ/tháng.<br>"
            "Trong khoảng thời gian $t_1 = 0{,}5$ tháng, số vụ tai nạn $X_1$ tuân theo:<br>"
            "$$X_1 \\sim \\text{Poisson}(\\lambda_1 = \\lambda \\cdot t_1 = 3 \\times 0{,}5 = 1{,}5)$$"
            "Xác suất xảy ra đúng 1 vụ tai nạn trong nửa tháng:<br>"
            "$$P(X_1 = 1) = \\frac{e^{-1{,}5} (1{,}5)^1}{1!} = 1{,}5 \\cdot e^{-1{,}5}$$"
            "Với $e^{-1{,}5} \\approx 0{,}22313$:<br>"
            "$$P(X_1 = 1) = 1{,}5 \\times 0{,}22313 \\approx 0{,}3347\\text{ (33{,}47\\%)}$$",
            "<b>Bước 2: Xác định tham số Poisson cho 2 tháng `[+0,30đ]`</b><br>"
            "Trong khoảng thời gian $t_2 = 2$ tháng, số vụ tai nạn $X_2$ tuân theo:<br>"
            "$$X_2 \\sim \\text{Poisson}(\\lambda_2 = \\lambda \\cdot t_2 = 3 \\times 2 = 6{,}0)$$",
            "<b>Bước 3: Tính xác suất có ít nhất 4 vụ tai nạn trong 2 tháng `[+0,35đ]`</b><br>"
            "Ta tính biến cố đối $P(X_2 \\le 3)$:<br>"
            "- $P(X_2 = 0) = \\frac{e^{-6} \\cdot 6^0}{0!} = e^{-6}$<br>"
            "- $P(X_2 = 1) = \\frac{e^{-6} \\cdot 6^1}{1!} = 6 e^{-6}$<br>"
            "- $P(X_2 = 2) = \\frac{e^{-6} \\cdot 6^2}{2!} = 18 e^{-6}$<br>"
            "- $P(X_2 = 3) = \\frac{e^{-6} \\cdot 6^3}{6} = 36 e^{-6}$<br>"
            "Tổng tích lũy đến 3:<br>"
            "$$P(X_2 \\le 3) = e^{-6} (1 + 6 + 18 + 36) = 61 e^{-6}$$"
            "Với $e^{-6} \\approx 0{,}00247875$:<br>"
            "$$P(X_2 \\le 3) = 61 \\times 0{,}00247875 \\approx 0{,}1512$$"
            "Vậy xác suất xảy ra ít nhất 4 vụ tai nạn là:<br>"
            "$$P(X_2 \\ge 4) = 1 - P(X_2 \\le 3) = 1 - 0{,}1512 = 0{,}8488\\text{ (84{,}88\\%)}$$"
        ],
        "pro_tips": "Tính chất cộng của Poisson: Nếu các khoảng thời gian độc lập thì tổng các biến Poisson cũng là biến Poisson với tham số bằng tổng các tham số.",
        "pitfalls": "Quên điều chỉnh tham số $\\lambda$ theo thời gian mà vẫn giữ nguyên $\\lambda = 3$ cho cả 0,5 tháng và 2 tháng."
    })

    # TL4_7 (Nâng cao)
    exercises.append({
        "id": "TL4_7", "topicId": 4, "level": "Nâng cao",
        "title": "Phân phối Nhị thức: Bài toán tìm số phép thử tối thiểu n",
        "problem": "Một hệ thống phòng thủ tên lửa có xác suất đánh chặn thành công một mục tiêu trong mỗi lần phóng là $p = 0{,}8$. Các lần phóng tên lửa là hoàn toàn độc lập.<br>"
                   "1. Nếu phóng 5 quả tên lửa, tính xác suất đánh chặn thành công ít nhất 4 quả ($P(X \\ge 4)$).<br>"
                   "2. Để đảm bảo xác suất có ít nhất 1 quả tên lửa đánh chặn thành công mục tiêu đạt từ $99\\%$ ($0{,}99$) trở lên, hệ thống cần phóng tối thiểu bao nhiêu quả tên lửa?",
        "analysis": "1. X ~ B(5, 0.8). P(X >= 4) = P(X=4) + P(X=5). 2. Y ~ B(n, 0.8). P(ít nhất 1 trúng) = 1 - P(0 trúng) = 1 - (0.2)^n >= 0.99 <=> 0.2^n <= 0.01 <=> n >= ln(0.01)/ln(0.2) = 2.8614 => n = 3.",
        "hints": [
            "Câu 1: Tính riêng P(X = 4) và P(X = 5) rồi cộng lại.",
            "Câu 2: Xác suất bắn trượt mỗi phát là 1 - 0.8 = 0.2.",
            "Xác suất trượt cả n phát là 0.2^n. Cần 1 - 0.2^n >= 0.99."
        ],
        "steps": [
            "<b>Bước 1: Tính xác suất đánh chặn thành công ít nhất 4/5 quả tên lửa `[+0,40đ]`</b><br>"
            "Với $n = 5$ và $p = 0{,}8$, $X \\sim B(5;\\; 0{,}8)$.<br>"
            "- Xác suất trúng 4 quả:<br>"
            "$$P(X = 4) = C_5^4 (0{,}8)^4 (0{,}2)^1 = 5 \\times 0{,}4096 \\times 0{,}2 = 0{,}4096$$"
            "- Xác suất trúng cả 5 quả:<br>"
            "$$P(X = 5) = C_5^5 (0{,}8)^5 (0{,}2)^0 = 1 \\times 0{,}32768 \\times 1 = 0{,}32768$$"
            "Vậy xác suất trúng ít nhất 4 quả là:<br>"
            "$$P(X \\ge 4) = P(X = 4) + P(X = 5) = 0{,}4096 + 0{,}32768 = 0{,}73728 \\approx 0{,}7373\\text{ (73{,}73\\%)}$$",
            "<b>Bước 2: Thiết lập bất phương trình tìm số quả tối thiểu n `[+0,35đ]`</b><br>"
            "Gọi $n$ là số quả tên lửa cần phóng ($n \\in \\mathbb{N}^*$).<br>"
            "Xác suất mỗi quả bắn trượt là: $q = 1 - p = 1 - 0{,}8 = 0{,}2$.<br>"
            "Xác suất cả $n$ quả đều bắn trượt là: $(0{,}2)^n$.<br>"
            "Xác suất có ít nhất 1 quả đánh chặn thành công là:<br>"
            "$$P(\\text{Ít nhất 1 quả trúng}) = 1 - (0{,}2)^n$$"
            "Theo yêu cầu bài toán:<br>"
            "$$1 - (0{,}2)^n \\ge 0{,}99 \\iff (0{,}2)^n \\le 0{,}01$$",
            "<b>Bước 3: Giải bất phương trình mũ và kết luận `[+0,25đ]`</b><br>"
            "Lấy logarit tự nhiên (ln) hai vế (chú ý $\\ln(0{,}2) < 0$ nên đổi chiều bất đẳng thức):<br>"
            "$$n \\cdot \\ln(0{,}2) \\le \\ln(0{,}01) \\iff n \\ge \\frac{\\ln(0{,}01)}{\\ln(0{,}2)}$$"
            "Tính giá trị số:<br>"
            "- $\\ln(0{,}01) \\approx -4{,}60517$<br>"
            "- $\\ln(0{,}2) \\approx -1{,}60944$<br>"
            "$$n \\ge \\frac{-4{,}60517}{-1{,}60944} \\approx 2{,}8614$$"
            "Vì $n$ phải là số nguyên dương ($n \\in \\mathbb{Z}^+$), ta chọn giá trị nhỏ nhất thỏa mãn:<br>"
            "$$n = \\lceil 2{,}8614 \\rceil = 3$$"
            "<b>Kết luận:</b> Hệ thống cần phóng tối thiểu <b>3 quả tên lửa</b> để xác suất tiêu diệt mục tiêu đạt ít nhất 99%."
        ],
        "pro_tips": "Khi giải bất phương trình $\\ln(a^n) \\le \\ln(b)$ với cơ số $a < 1$, $\\ln(a)$ là số âm nên bắt buộc phải đảo chiều bất phương trình!",
        "pitfalls": "Quên đổi chiều bất phương trình khi chia cho $\\ln(0{,}2)$ dẫn đến $n \\le 2{,}86$ (vô lý)."
    })

    # TL4_8 (Nâng cao)
    exercises.append({
        "id": "TL4_8", "topicId": 4, "level": "Nâng cao",
        "title": "Phân phối Siêu bội: Quy trình nghiệm thu sản phẩm và Tối ưu chi phí",
        "problem": "Một công ty nhập một lô hàng gồm $N = 50$ thiết bị điện tử. Quy trình kiểm tra chất lượng để nghiệm thu được quy định như sau: Rút ngẫu nhiên không hoàn lại $n = 5$ thiết bị để kiểm định.<br>"
                   "- Nếu <b>không phát hiện bất kỳ thiết bị lỗi nào</b> ($X = 0$), công ty chấp nhận ngay lô hàng mà không cần kiểm tra thêm.<br>"
                   "- Nếu phát hiện <b>từ 1 thiết bị lỗi trở lên</b> ($X \\ge 1$), công ty sẽ từ chối nghiệm thu sơ bộ và tiến hành kiểm tra toàn bộ 50 thiết bị trong lô.<br>"
                   "Giả sử trên thực tế lô hàng này có $M = 3$ thiết bị bị lỗi.<br>"
                   "1. Xác định phân phối của số thiết bị lỗi $X$ tìm thấy trong mẫu 5 thiết bị.<br>"
                   "2. Tính xác suất để lô hàng được chấp nhận ngay ở bước sơ bộ.<br>"
                   "3. Tính số thiết bị lỗi kỳ vọng tìm thấy trong mẫu 5 thiết bị và xác suất công ty phải kiểm tra toàn bộ lô hàng.",
        "analysis": "X ~ HG(N=50, M=3, n=5). Chấp nhận ngay: X = 0. P(X=0) = C(3, 0)*C(47, 5) / C(50, 5). Kỳ vọng E(X) = n * (M/N) = 5 * (3/50) = 0.3 thiết bị lỗi. Phải kiểm tra toàn bộ: P(X >= 1) = 1 - P(X=0).",
        "hints": [
            "Lấy mẫu không hoàn lại 5 thiết bị từ 50 thiết bị -> Siêu bội HG(50, 3, 5).",
            "Chấp nhận ngay khi X = 0: C(47, 5) / C(50, 5).",
            "Kỳ vọng của phân phối siêu bội: E(X) = n * (M/N)."
        ],
        "steps": [
            "<b>Bước 1: Xác định mô hình phân phối của X `[+0,25đ]`</b><br>"
            "Biến ngẫu nhiên $X$ là số thiết bị lỗi tìm thấy khi rút mẫu $n = 5$ thiết bị không hoàn lại từ tập $N = 50$ thiết bị có $M = 3$ thiết bị lỗi.<br>"
            "Do đó, $X$ tuân theo <b>Phân phối Siêu bội</b>:<br>"
            "$$X \\sim HG(N = 50,\\; M = 3,\\; n = 5)$$",
            "<b>Bước 2: Tính xác suất lô hàng được chấp nhận ngay `[+0,40đ]`</b><br>"
            "Lô hàng được chấp nhận ngay khi và chỉ khi trong 5 thiết bị kiểm tra không có thiết bị lỗi nào ($X = 0$):<br>"
            "$$P(X = 0) = \\frac{C_3^0 \\cdot C_{47}^5}{C_{50}^5}$$"
            "Tính các tổ hợp:<br>"
            "- $C_3^0 = 1$<br>"
            "- $C_{47}^5 = \\frac{47 \\times 46 \\times 45 \\times 44 \\times 43}{120} = 1533939$<br>"
            "- $C_{50}^5 = \\frac{50 \\times 49 \\times 48 \\times 47 \\times 46}{120} = 2118760$<br>"
            "$$P(\\text{Chấp nhận ngay}) = \\frac{1533939}{2118760} \\approx 0{,}7240\\text{ (72{,}40\\%)}$$"
            "<i>(Mẹo rút gọn: $\\frac{47 \\times 46 \\times 45 \\times 44 \\times 43}{50 \\times 49 \\times 48 \\times 47 \\times 46} = \\frac{45 \\times 44 \\times 43}{50 \\times 49 \\times 48} = \\frac{85140}{117600} \\approx 0{,}7240$)</i>",
            "<b>Bước 3: Tính kỳ vọng E(X) và Xác suất phải kiểm tra toàn bộ `[+0,35đ]`</b><br>"
            "- Số thiết bị lỗi kỳ vọng phát hiện được trong mẫu:<br>"
            "$$E(X) = n \\cdot \\frac{M}{N} = 5 \\times \\frac{3}{50} = \\frac{15}{50} = 0{,}30\\text{ (thiết bị lỗi)}$$"
            "- Xác suất công ty phải tiến hành kiểm tra toàn bộ lô hàng là xác suất tìm thấy ít nhất 1 thiết bị lỗi ($X \\ge 1$):<br>"
            "$$P(\\text{Kiểm tra toàn bộ}) = P(X \\ge 1) = 1 - P(X = 0) = 1 - 0{,}7240 = 0{,}2760\\text{ (27{,}60\\%)}$$"
        ],
        "pro_tips": "Khi tính tỷ số $\\frac{C_{47}^5}{C_{50}^5}$, ta có thể viết thành tích xác suất có điều kiện: $\\frac{47}{50} \\times \\frac{46}{49} \\times \\frac{45}{48} \\times \\frac{44}{47} \\times \\frac{43}{46} = \\frac{45}{50} \\times \\frac{44}{49} \\times \\frac{43}{48}$, tính cực nhanh!",
        "pitfalls": "Dùng công thức kỳ vọng $np$ của Nhị thức mà không giải thích vì sao Siêu bội có công thức $n(M/N)$."
    })

    return exercises

if __name__ == "__main__":
    t4 = get_topic_4()
    print(f"Generated Topic 4: {len(t4)} exercises.")
