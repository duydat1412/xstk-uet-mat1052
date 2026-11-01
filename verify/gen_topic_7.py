# Topic 7: Định lý giới hạn trung tâm (CLT) & Bài toán kích thước mẫu (TL7_1 -> TL7_8)
import math
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_topic_7():
    exercises = []

    # TL7_1 (Cơ bản)
    exercises.append({
        "id": "TL7_1", "topicId": 7, "level": "Cơ bản",
        "title": "Áp dụng Định lý giới hạn trung tâm cho tổng xúc xắc",
        "problem": "Gieo một con xúc xắc 6 mặt cân đối và đồng chất $n = 100$ lần độc lập. Gọi $X_i$ là số chấm ở lần gieo thứ $i$ ($i = 1, 2, \\dots, 100$) và $S_{100} = \\sum_{i=1}^{100} X_i$ là tổng số chấm thu được sau 100 lần gieo.<br>"
                   "Biết rằng mỗi lần gieo có: $\\mu = 3{,}5$ và $\\sigma = \\sqrt{35/12} \\approx 1{,}7078$. Cho biết $\\Phi(1{,}17) \\approx 0{,}8790$.<br>"
                   "1. Phát biểu Định lý giới hạn trung tâm (CLT) áp dụng cho tổng $S_{100}$.<br>"
                   "2. Xác định kỳ vọng $E(S_{100})$ và độ lệch chuẩn $\\operatorname{SD}(S_{100})$.<br>"
                   "3. Dùng CLT tính xấp xỉ xác suất để tổng số chấm nằm trong khoảng từ 330 đến 370 ($P(330 \\le S_{100} \\le 370)$).",
        "analysis": "CLT: Khi n lon (n=100 >= 30), S_n ~ N(n*mu, n*sigma^2). E(S_100) = 100*3.5 = 350. SD(S_100) = 10 * 1.7078 = 17.078. Khoang [330, 370] cach tam 350 mot khoang +-20. Z = 20 / 17.078 approx 1.171. P = 2*Phi(1.17) - 1 = 2(0.8790) - 1 = 0.7580.",
        "hints": [
            "E(S_100) = 100 * 3.5 = 350.",
            "SD(S_100) = sqrt(100) * 1.7078 = 17.078.",
            "Chuẩn hóa Z1 = (330 - 350) / 17.078 = -1.17; Z2 = +1.17."
        ],
        "steps": [
            "<b>Bước 1: Phát biểu Định lý giới hạn trung tâm (CLT) `[+0,25đ]`</b><br>"
            "Theo CLT: Cho $X_1, X_2, \\dots, X_n$ là các biến ngẫu nhiên độc lập cùng phân phối (i.i.d.) có kỳ vọng $\\mu$ và phương sai $\\sigma^2$ hữu hạn. Khi kích thước mẫu $n$ đủ lớn ($n \\ge 30$), tổng $S_n = \\sum_{i=1}^n X_i$ xấp xỉ tuân theo phân phối chuẩn:<br>"
            "$$S_n \\approx N(\\mu_S = n\\mu,\\; \\sigma_S^2 = n\\sigma^2)$$",
            "<b>Bước 2: Tính kỳ vọng và độ lệch chuẩn của S₁₀₀ `[+0,35đ]`</b><br>"
            "Với $n = 100$, $\\mu = 3{,}5$ và $\\sigma = 1{,}7078$:<br>"
            "- Kỳ vọng của tổng:<br>"
            "$$\\mu_S = E(S_{100}) = n \\cdot \\mu = 100 \\times 3{,}5 = 350{,}0$$"
            "- Độ lệch chuẩn của tổng:<br>"
            "$$\\sigma_S = \\operatorname{SD}(S_{100}) = \\sqrt{n} \\cdot \\sigma = \\sqrt{100} \\times 1{,}7078 = 10 \\times 1{,}7078 = 17{,}078$$"
            "Do đó: $S_{100} \\approx N(350;\\; 17{,}078^2)$.",
            "<b>Bước 3: Tính xác suất tổng số chấm từ 330 đến 370 `[+0,40đ]`</b><br>"
            "Chuẩn hóa hai đầu mút của biến cố $330 \\le S_{100} \\le 370$:<br>"
            "- Đầu mút dưới: $Z_1 = \\frac{330 - 350}{17{,}078} = \\frac{-20}{17{,}078} \\approx -1{,}17$<br>"
            "- Đầu mút trên: $Z_2 = \\frac{370 - 350}{17{,}078} = \\frac{+20}{17{,}078} \\approx +1{,}17$<br>"
            "Xác suất xấp xỉ chuẩn là:<br>"
            "$$P(330 \\le S_{100} \\le 370) \\approx P(-1{,}17 \\le Z \\le 1{,}17) = \\Phi(1{,}17) - \\Phi(-1{,}17)$$"
            "$$= 2\\Phi(1{,}17) - 1 = 2 \\times 0{,}8790 - 1 = 1{,}7580 - 1 = 0{,}7580\\text{ (75{,}80\\%)}$$"
        ],
        "pro_tips": "Mặc dù mỗi lần gieo xúc xắc mang phân phối đều rời rạc hình chữ nhật, nhưng tổng của 100 lần gieo đã trở thành hình chuông phân phối chuẩn cực kỳ mượt mà!",
        "pitfalls": "Quên căn bậc hai của $n$ khi tính độ lệch chuẩn (lấy $n \\times \\sigma = 170{,}78$ thay vì $\\sqrt{n} \\times \\sigma = 17{,}078$)."
    })

    # TL7_2 (Cơ bản)
    exercises.append({
        "id": "TL7_2", "topicId": 4, "level": "Cơ bản", # Note: topicId 7
        "topicId": 7,
        "title": "Bài toán thang máy chở khách: Tổng các biến phân phối chuẩn",
        "problem": "Một thang máy của tòa nhà chung cư có tải trọng quy định tối đa là $700\\text{ kg}$. Có 10 người cùng bước vào thang máy. Cân nặng của mỗi người là các biến ngẫu nhiên độc lập cùng tuân theo phân phối chuẩn với trung bình $\\mu = 65\\text{ kg}$ và độ lệch chuẩn $\\sigma = 5\\text{ kg}$ ($X_i \\sim N(65,\\; 5^2)$). Cho biết: $\\Phi(3{,}16) \\approx 0{,}9992$.<br>"
                   "1. Xác định phân phối xác suất chính xác của tổng cân nặng $S_{10}$ của 10 người.<br>"
                   "2. Tính xác suất thang máy bị quá tải trọng ($P(S_{10} > 700)$).<br>"
                   "3. Giải thích tại sao trong bài toán này ta không cần điều kiện $n \\ge 30$ của Định lý giới hạn trung tâm.",
        "analysis": "1. Tong cua cac bien doc lap phan phoi chuan la bien phan phoi chuan CHINH XAC (khong can xap xi). S_10 ~ N(10*65, 10*25) = N(650, 250). SD(S_10) = sqrt(250) = 5*sqrt(10) approx 15.8114 kg. 2. P(S_10 > 700): Z = (700 - 650) / 15.8114 = 50 / 15.8114 = 3.1623. P = 1 - Phi(3.16) = 1 - 0.9992 = 0.0008 (0.08%). 3. Vi tong the ban dau da la chuan.",
        "hints": [
            "Tổng của các biến chuẩn độc lập luôn luôn có phân phối chuẩn với mọi n.",
            "E(S_10) = 10 * 65 = 650 kg. Var(S_10) = 10 * 5^2 = 250 kg^2.",
            "Z = (700 - 650) / sqrt(250) = 50 / 15.8114 approx 3.16."
        ],
        "steps": [
            "<b>Bước 1: Xác định phân phối xác suất chính xác của S₁₀ `[+0,35đ]`</b><br>"
            "Vì các biến ngẫu nhiên thành phần $X_i$ là độc lập và bản thân chúng <i>đã tuân theo phân phối chuẩn</i> $N(65,\\; 5^2)$, theo tính chất bảo toàn của phân phối chuẩn, tổng $S_{10} = \\sum_{i=1}^{10} X_i$ tuân theo <b>phân phối chuẩn chính xác</b> (không cần xấp xỉ):<br>"
            "- Kỳ vọng của tổng: $\\mu_S = 10 \\times 65 = 650\\text{ kg}$.<br>"
            "- Phương sai của tổng: $\\sigma_S^2 = 10 \\times 5^2 = 10 \\times 25 = 250\\text{ kg}^2$.<br>"
            "- Độ lệch chuẩn của tổng: $\\sigma_S = \\sqrt{250} = 5\\sqrt{10} \\approx 15{,}8114\\text{ kg}$.<br>"
            "Vậy: $S_{10} \\sim N(650;\\; 250)$.",
            "<b>Bước 2: Tính xác suất thang máy bị quá tải `[+0,35đ]`</b><br>"
            "Thang máy bị quá tải khi tổng khối lượng vượt quá $700\\text{ kg}$ ($S_{10} > 700$).<br>"
            "Chuẩn hóa giá trị 700 kg:<br>"
            "$$Z = \\frac{700 - \\mu_S}{\\sigma_S} = \\frac{700 - 650}{15{,}8114} = \\frac{50}{15{,}8114} \\approx 3{,}16$$"
            "Xác suất bị quá tải là:<br>"
            "$$P(S_{10} > 700) = P(Z > 3{,}16) = 1 - \\Phi(3{,}16)$$"
            "Tra bảng chuẩn tắc: $\\Phi(3{,}16) \\approx 0{,}9992$:<br>"
            "$$P(S_{10} > 700) = 1 - 0{,}9992 = 0{,}0008\\text{ (hay 0{,}08\\%)}$$"
            "<b>Kết luận:</b> Khả năng thang máy bị quá tải là cực kỳ hiếm gặp (chỉ khoảng 8 phần vạn).",
            "<b>Bước 3: Giải thích điều kiện n < 30 `[+0,30đ]`</b><br>"
            "Định lý CLT chỉ cần thiết khi phân phối gốc của các biến thành phần $X_i$ <i>chưa phải là chuẩn</i> (ví dụ phân phối đều, phân phối mũ, nhị thức...), lúc đó cần $n \\ge 30$ để trung bình/tổng dần dần tạo thành hình chuông chuẩn.<br>"
            "Còn ở bài này, bản thân mỗi cá nhân $X_i$ đã có cân nặng phân phối chuẩn, do đó tổng của chúng luôn mang phân phối chuẩn chính xác với <b>mọi kích thước $n$</b> (kể cả khi $n = 2$ hay $n = 10$)."
        ],
        "pro_tips": "Nhớ kỹ: 'Tổng của các biến chuẩn độc lập là biến chuẩn' (đúng với mọi $n$), còn 'CLT' chỉ dùng khi biến gốc không chuẩn và cần $n \\ge 30$.",
        "pitfalls": "Tính độ lệch chuẩn của tổng là $10 \\times 5 = 50\\text{ kg}$ thay vì $\\sqrt{10} \\times 5 = 15{,}81\\text{ kg}$."
    })

    # TL7_3 (Trung bình)
    exercises.append({
        "id": "TL7_3", "topicId": 7, "level": "Trung bình",
        "title": "Áp dụng CLT cho Trung bình mẫu: Thời gian phục vụ khách hàng",
        "problem": "Thời gian giải quyết một thủ tục hành chính tại một cơ quan công quyền là biến ngẫu nhiên có trung bình $\\mu = 12$ phút và độ lệch chuẩn $\\sigma = 4$ phút (chưa rõ dạng phân phối). Khảo sát ngẫu nhiên một mẫu gồm $n = 64$ người dân đến làm thủ tục.<br>"
                   "1. Nêu phân phối xấp xỉ của thời gian phục vụ trung bình $\\bar{X}_{64}$ theo CLT và tính các tham số của phân phối này.<br>"
                   "2. Tính xác suất để thời gian phục vụ trung bình của 64 người này ít hơn 11 phút ($P(\\bar{X}_{64} < 11)$). Cho biết $\\Phi(2{,}0) \\approx 0{,}9772$.",
        "analysis": "1. n = 64 >= 30, CLT ap dung cho trung binh mau: Xbar_n ~ N(mu, sigma^2/n). E(Xbar) = 12 phut. SD(Xbar) = sigma / sqrt(n) = 4 / sqrt(64) = 4 / 8 = 0.5 phut. 2. P(Xbar < 11): Z = (11 - 12)/0.5 = -1 / 0.5 = -2.0. P = Phi(-2.0) = 1 - Phi(2.0) = 1 - 0.9772 = 0.0228 (2.28%).",
        "hints": [
            "Cỡ mẫu n = 64 >= 30 -> áp dụng CLT.",
            "Sai số chuẩn của trung bình mẫu: SE = sigma / sqrt(n) = 4 / 8 = 0.5 phút.",
            "Chuẩn hóa Z = (11 - 12) / 0.5 = -2.0. Tra Phi(-2.0)."
        ],
        "steps": [
            "<b>Bước 1: Xác định phân phối xấp xỉ của trung bình mẫu X̄₆₄ `[+0,40đ]`</b><br>"
            "Vì kích thước mẫu $n = 64 \\ge 30$, theo Định lý giới hạn trung tâm (CLT), biến ngẫu nhiên trung bình mẫu $\\bar{X}_{64} = \\frac{1}{64}\\sum_{i=1}^{64} X_i$ xấp xỉ tuân theo phân phối chuẩn:<br>"
            "$$\\bar{X}_{64} \\approx N\\left( \\mu_{\\bar{X}} = \\mu,\\; \\sigma_{\\bar{X}}^2 = \\frac{\\sigma^2}{n} \\right)$$"
            "Tính các tham số cụ thể:<br>"
            "- Kỳ vọng của trung bình mẫu:<br>"
            "$$\\mu_{\\bar{X}} = \\mu = 12{,}0\\text{ (phút)}$$"
            "- Sai số chuẩn (Standard Error) của trung bình mẫu:<br>"
            "$$\\sigma_{\\bar{X}} = \\frac{\\sigma}{\\sqrt{n}} = \\frac{4}{\\sqrt{64}} = \\frac{4}{8} = 0{,}5\\text{ (phút)}$$"
            "Do đó: $\\bar{X}_{64} \\approx N(12{,}0;\\; 0{,}5^2)$.",
            "<b>Bước 2: Tính xác suất thời gian trung bình ít hơn 11 phút `[+0,40đ]`</b><br>"
            "Ta cần tính xác suất $P(\\bar{X}_{64} < 11)$.<br>"
            "Chuẩn hóa giá trị 11 phút:<br>"
            "$$Z = \\frac{11 - \\mu_{\\bar{X}}}{\\sigma_{\\bar{X}}} = \\frac{11 - 12}{0{,}5} = \\frac{-1}{0{,}5} = -2{,}0$$"
            "Xác suất cần tìm là:<br>"
            "$$P(\\bar{X}_{64} < 11) \\approx P(Z < -2{,}0) = \\Phi(-2{,}0)$$"
            "Theo tính chất đối xứng: $\\Phi(-2{,}0) = 1 - \\Phi(2{,}0)$. Đề bài cho $\\Phi(2{,}0) \\approx 0{,}9772$:<br>"
            "$$P(\\bar{X}_{64} < 11) = 1 - 0{,}9772 = 0{,}0228\\text{ (2{,}28\\%)}$$",
            "<b>Bước 3: Kết luận `[+0,20đ]`</b><br>"
            "Xác suất để thời gian xử lý hồ sơ trung bình của 64 người dân ít hơn 11 phút là $2{,}28\\%$."
        ],
        "pro_tips": "Đối với bài toán Trung bình mẫu $\\bar{X}_n$, mẫu số của công thức chuẩn hóa luôn luôn là $\\frac{\\sigma}{\\sqrt{n}}$ (chia cho $\\sqrt{n}$).",
        "pitfalls": "Quên chia căn $n$: dùng $\\sigma = 4$ thay vì $\\sigma/\\sqrt{n} = 0{,}5$ dẫn đến $Z = (11-12)/4 = -0{,}25$ (sai hoàn toàn)."
    })

    # TL7_4 (Trung bình)
    exercises.append({
        "id": "TL7_4", "topicId": 7, "level": "Trung bình",
        "title": "Quãng đường đi học và So sánh các kích thước mẫu n khác nhau",
        "problem": "Quãng đường từ nhà đến trường của sinh viên có phân phối lệch phải (phân phối mũ) với kỳ vọng $\\mu = 5\\text{ km}$ và độ lệch chuẩn $\\sigma = 5\\text{ km}$. Cho biết: $\\Phi(2{,}0) \\approx 0{,}9772$; $\\Phi(1{,}2) \\approx 0{,}8849$.<br>"
                   "1. Khảo sát một mẫu gồm $n = 100$ sinh viên. Dùng CLT, tính xác suất để quãng đường trung bình $\\bar{X}_{100}$ nằm giữa 4 km và 6 km ($P(4 \\le \\bar{X}_{100} \\le 6)$).<br>"
                   "2. Khi kích thước mẫu giảm xuống còn $n = 36$ sinh viên, hãy tính lại xác suất trên ($P(4 \\le \\bar{X}_{36} \\le 6)$).<br>"
                   "3. So sánh kết quả ở 2 trường hợp và giải thích quy luật hội tụ của trung bình mẫu.",
        "analysis": "1. n = 100: SE = 5 / sqrt(100) = 0.5 km. P(4 <= Xbar <= 6): Z in [-1/0.5, 1/0.5] = [-2, 2]. P = 2*Phi(2) - 1 = 2(0.9772) - 1 = 0.9544 (95.44%). 2. n = 36: SE = 5 / sqrt(36) = 5/6 approx 0.8333 km. Z in [-1/(5/6), 1/(5/6)] = [-1.2, 1.2]. P = 2*Phi(1.2) - 1 = 2(0.8849) - 1 = 0.7698 (76.98%). 3. Khi n tang, SE giam, phan phoi tap trung chat che hon quanh mu.",
        "hints": [
            "Với n = 100: SE = 5 / 10 = 0.5 km -> Z = (6 - 5) / 0.5 = 2.0.",
            "Với n = 36: SE = 5 / 6 = 0.8333 km -> Z = (6 - 5) / (5/6) = 1.2.",
            "P(-z <= Z <= z) = 2*Phi(z) - 1."
        ],
        "steps": [
            "<b>Bước 1: Tính xác suất với kích thước mẫu n = 100 `[+0,40đ]`</b><br>"
            "Với $n = 100$ sinh viên, sai số chuẩn của trung bình mẫu là:<br>"
            "$$\\sigma_{\\bar{X}_{100}} = \\frac{\\sigma}{\\sqrt{n}} = \\frac{5}{\\sqrt{100}} = \\frac{5}{10} = 0{,}5\\text{ (km)}$$"
            "Chuẩn hóa khoảng $[4;\\; 6]$:<br>"
            "- $Z_1 = \\frac{4 - 5}{0{,}5} = -2{,}0$<br>"
            "- $Z_2 = \\frac{6 - 5}{0{,}5} = +2{,}0$<br>"
            "Xác suất quãng đường trung bình rơi vào $[4;\\; 6]$ km:<br>"
            "$$P(4 \\le \\bar{X}_{100} \\le 6) \\approx 2\\Phi(2{,}0) - 1 = 2(0{,}9772) - 1 = 1{,}9544 - 1 = 0{,}9544\\text{ (95{,}44\\%)}$$",
            "<b>Bước 2: Tính xác suất với kích thước mẫu n = 36 `[+0,35đ]`</b><br>"
            "Với $n = 36$ sinh viên, sai số chuẩn của trung bình mẫu là:<br>"
            "$$\\sigma_{\\bar{X}_{36}} = \\frac{\\sigma}{\\sqrt{n}} = \\frac{5}{\\sqrt{36}} = \\frac{5}{6} \\approx 0{,}8333\\text{ (km)}$$"
            "Chuẩn hóa khoảng $[4;\\; 6]$:<br>"
            "- $Z_1 = \\frac{4 - 5}{5/6} = -\\frac{6}{5} = -1{,}20$<br>"
            "- $Z_2 = \\frac{6 - 5}{5/6} = +\\frac{6}{5} = +1{,}20$<br>"
            "Xác suất tương ứng:<br>"
            "$$P(4 \\le \\bar{X}_{36} \\le 6) \\approx 2\\Phi(1{,}20) - 1 = 2(0{,}8849) - 1 = 1{,}7698 - 1 = 0{,}7698\\text{ (76{,}98\\%)}$$",
            "<b>Bước 3: So sánh và Rút ra quy luật `[+0,25đ]`</b><br>"
            "- Khi kích thước mẫu tăng từ $n = 36$ lên $n = 100$, xác suất trung bình mẫu bám sát quanh giá trị thực $\\mu = 5$ tăng mạnh từ $76{,}98\\%$ lên $95{,}44\\%$.<br>"
            "- <b>Quy luật:</b> Sai số chuẩn tỉ lệ nghịch với $\\sqrt{n}$ ($\\sigma/\\sqrt{n}$). Khi kích thước mẫu $n$ càng lớn, đồ thị phân phối của $\\bar{X}_n$ càng co cụm hẹp lại quanh kỳ vọng $\\mu$, làm cho trung bình mẫu ước lượng ngày càng chính xác và tin cậy."
        ],
        "pro_tips": "Nhớ rằng để giảm sai số chuẩn đi 2 lần, ta phải tăng kích thước mẫu lên gấp $2^2 = 4$ lần!",
        "pitfalls": "Tính sai phân số chia cho phân số: $1 / (5/6) = 6/5 = 1{,}2$ (một số bạn bấm máy tính nhầm thành $1/5/6 = 0{,}033$)."
    })

    # TL7_5 (Trung bình)
    exercises.append({
        "id": "TL7_5", "topicId": 7, "level": "Trung bình",
        "title": "Xấp xỉ Chuẩn cho Nhị thức với Hiệu chỉnh liên tục (Continuity Correction)",
        "problem": "Tung một đồng xu cân đối và đồng chất $n = 100$ lần độc lập. Gọi $X$ là số lần xuất hiện mặt ngửa ($X \\sim B(100,\\; 0{,}5)$). Cho biết: $\\Phi(1{,}1) \\approx 0{,}8643$; $\\Phi(1{,}0) \\approx 0{,}8413$.<br>"
                   "1. Tính kỳ vọng $\\mu$ và độ lệch chuẩn $\\sigma$ của $X$. Kiểm tra điều kiện áp dụng định lý De Moivre – Laplace.<br>"
                   "2. Áp dụng Định lý giới hạn trung tâm <b>CÓ hiệu chỉnh liên tục</b>, hãy tính xấp xỉ xác suất số lần mặt ngửa xuất hiện từ 45 đến 55 lần ($P(45 \\le X \\le 55)$).<br>"
                   "3. So sánh kết quả trên nếu tính KHÔNG có hiệu chỉnh liên tục và giải thích ý nghĩa hình học của việc hiệu chỉnh $\\pm 0{,}5$.",
        "analysis": "1. mu = np = 50, Var = np(1-p) = 25 => sigma = 5. np = 50 >= 10, n(1-p) = 50 >= 10 -> Thoa man De Moivre - Laplace. 2. Co hieu chinh: P(45 <= X <= 55) = P(44.5 <= Y <= 55.5). Z1 = (44.5 - 50)/5 = -1.1; Z2 = (55.5 - 50)/5 = +1.1. P = 2*Phi(1.1) - 1 = 2(0.8643) - 1 = 0.7286 (72.86%). 3. Khong hieu chinh: Z in [-1.0, 1.0] -> 2*Phi(1.0) - 1 = 0.6826 (68.26%). Sai so toi 4.6%!",
        "hints": [
            "mu = 100 * 0.5 = 50; sigma = sqrt(100 * 0.5 * 0.5) = 5.",
            "Quy tắc hiệu chỉnh liên tục: 45 lùi nửa đơn vị thành 44.5; 55 tiến nửa đơn vị thành 55.5.",
            "Z = (55.5 - 50) / 5 = 5.5 / 5 = 1.1."
        ],
        "steps": [
            "<b>Bước 1: Tính tham số và Kiểm tra điều kiện `[+0,30đ]`</b><br>"
            "Số mặt ngửa $X \\sim B(n = 100,\\; p = 0{,}5)$:<br>"
            "- Kỳ vọng: $\\mu = n p = 100 \\times 0{,}5 = 50$.<br>"
            "- Phương sai: $\\sigma^2 = n p (1 - p) = 100 \\times 0{,}5 \\times 0{,}5 = 25$.<br>"
            "- Độ lệch chuẩn: $\\sigma = \\sqrt{25} = 5{,}0$.<br>"
            "Kiểm tra điều kiện: $n p = 50 \\ge 10$ và $n(1 - p) = 50 \\ge 10$. Điều kiện xấp xỉ chuẩn (Định lý De Moivre – Laplace) được thỏa mãn rất tốt.",
            "<b>Bước 2: Tính xấp xỉ CÓ hiệu chỉnh liên tục `[+0,40đ]`</b><br>"
            "Vì $X$ là biến rời rạc nhận các giá trị nguyên, mỗi giá trị nguyên $k$ thực chất tương ứng với cột hình chữ nhật trải dài từ $k - 0{,}5$ đến $k + 0{,}5$ trên trục số thực.<br>"
            "Do đó khoảng rời rạc $45 \\le X \\le 55$ được mở rộng sang biến liên tục $Y \\sim N(50,\\; 5^2)$ là:<br>"
            "$$P(45 \\le X \\le 55) \\approx P(44{,}5 \\le Y \\le 55{,}5)$$"
            "Chuẩn hóa hai đầu mút:<br>"
            "- $Z_1 = \\frac{44{,}5 - 50}{5} = \\frac{-5{,}5}{5} = -1{,}10$<br>"
            "- $Z_2 = \\frac{55{,}5 - 50}{5} = \\frac{+5{,}5}{5} = +1{,}10$<br>"
            "Xác suất tính được là:<br>"
            "$$P(45 \\le X \\le 55) \\approx 2\\Phi(1{,}10) - 1 = 2(0{,}8643) - 1 = 1{,}7286 - 1 = 0{,}7286\\text{ (72{,}86\\%)}$$",
            "<b>Bước 3: So sánh khi KHÔNG hiệu chỉnh và Giải thích ý nghĩa `[+0,30đ]`</b><br>"
            "- Nếu tính trực tiếp không hiệu chỉnh:<br>"
            "$$Z_1 = \\frac{45 - 50}{5} = -1{,}0;\\quad Z_2 = \\frac{55 - 50}{5} = +1{,}0$$"
            "$$P_{\\text{không hiệu chỉnh}} = 2\\Phi(1{,}0) - 1 = 2(0{,}8413) - 1 = 0{,}6826\\text{ (68{,}26\\%)}$$<br>"
            "- <b>Đánh giá sai số:</b> Nếu không hiệu chỉnh, kết quả bị thiếu hụt tới $72{,}86\\% - 68{,}26\\% = 4{,}60\\%$! Nguyên nhân là vì đã bỏ sót nửa cột bên trái của giá trị 45 (từ 44,5 đến 45) và nửa cột bên phải của giá trị 55 (từ 55 đến 55,5). Hiệu chỉnh liên tục bao trùm trọn vẹn diện tích của toàn bộ các cột histogram."
        ],
        "pro_tips": "Quy tắc nằm lòng hiệu chỉnh liên tục: Đầu mút dưới có dấu $\\le$ thì lùi $0{,}5$; Đầu mút trên có dấu $\\le$ thì tiến $0{,}5$.",
        "pitfalls": "Hiệu chỉnh nhầm chiều (ví dụ 45 tăng lên 45,5 là sai vì làm thu hẹp khoảng cần tính)."
    })

    # TL7_6 (Nâng cao)
    exercises.append({
        "id": "TL7_6", "topicId": 7, "level": "Nâng cao",
        "title": "Khảo sát thăm dò dư luận: Xác định kích thước mẫu n cho Tỷ lệ",
        "problem": "Một kênh truyền hình muốn tiến hành một cuộc thăm dò ý kiến cử tri để ước lượng tỉ lệ ủng hộ một dự luật mới. Yêu cầu cuộc khảo sát phải có <b>sai số biên không vượt quá $\\pm 3\\%$</b> ($E = 0{,}03$) với <b>độ tin cậy $95\\%$</b> ($Z_{0{,}025} = 1{,}96$).<br>"
                   "1. Sử dụng CLT cho tỉ lệ mẫu $\\hat{p}$, hãy thiết lập công thức xác định kích thước mẫu khảo sát tối thiểu $n$.<br>"
                   "2. Trong trường hợp chưa có bất kỳ thông tin gì về tỉ lệ ủng hộ thực tế (trường hợp rủi ro tối đa $p = 0{,}5$), đài truyền hình cần phỏng vấn tối thiểu bao nhiêu cử tri?<br>"
                   "3. Nếu qua khảo sát thăm dò nhỏ ban đầu, người ta biết tỉ lệ ủng hộ chỉ dao động xung quanh $20\\%$ ($p = 0{,}2$), kích thước mẫu cần thiết sẽ giảm xuống còn bao nhiêu?",
        "analysis": "1. p_hat ~ N(p, p(1-p)/n). Sai so bien E = Z_{alpha/2} * sqrt(p(1-p)/n) <= 0.03 => n >= [Z_{alpha/2}^2 * p(1-p)] / E^2. 2. Truong hop xau nhat p = 0.5: p(1-p) = 0.25 (cuc dai). n >= [1.96^2 * 0.25] / 0.03^2 = [3.8416 * 0.25] / 0.0009 = 0.9604 / 0.0009 = 1067.11 => n = 1068 cu tri. 3. Khi p = 0.2: p(1-p) = 0.16. n >= [3.8416 * 0.16] / 0.0009 = 0.614656 / 0.0009 = 682.95 => n = 683 cu tri.",
        "hints": [
            "Công thức sai số biên của tỉ lệ: E = Z * sqrt(p(1-p) / n).",
            "Bình phương hai vế: n >= [Z^2 * p * (1 - p)] / E^2.",
            "Tích p(1-p) lớn nhất bằng 0.25 khi p = 0.5 (trường hợp thận trọng nhất)."
        ],
        "steps": [
            "<b>Bước 1: Thiết lập công thức tìm kích thước mẫu n `[+0,35đ]`</b><br>"
            "Gọi $X$ là số cử tri ủng hộ trong mẫu ngẫu nhiên gồm $n$ cử tri. Tỉ lệ ủng hộ của mẫu là $\\hat{p} = \\frac{X}{n}$.<br>"
            "Theo CLT cho phân phối tỉ lệ, khi $n$ đủ lớn:<br>"
            "$$\\hat{p} \\approx N\\left( p,\\; \\frac{p(1 - p)}{n} \\right)$$"
            "Sai số biên của ước lượng tỉ lệ với độ tin cậy $1 - \\alpha = 0{,}95$ ($Z_{\\alpha/2} = 1{,}96$) là:<br>"
            "$$E = Z_{\\alpha/2} \\sqrt{\\frac{p(1 - p)}{n}}$$"
            "Để sai số không vượt quá mức cho phép $E$:<br>"
            "$$Z_{\\alpha/2} \\sqrt{\\frac{p(1 - p)}{n}} \\le E \\iff \\sqrt{n} \\ge \\frac{Z_{\\alpha/2} \\sqrt{p(1 - p)}}{E} \\iff n \\ge \\frac{Z_{\\alpha/2}^2 \\cdot p(1 - p)}{E^2}$$",
            "<b>Bước 2: Tính kích thước mẫu cho trường hợp xấu nhất p = 0,5 `[+0,35đ]`</b><br>"
            "Hàm số $f(p) = p(1 - p) = p - p^2$ đạt giá trị lớn nhất bằng $0{,}25$ tại $p = 0{,}5$.<br>"
            "Do đó, khi chưa biết thông tin gì về $p$, việc chọn $p = 0{,}5$ sẽ đảm bảo kích thước mẫu $n$ luôn đủ lớn và an toàn cho mọi tình huống thực tế:<br>"
            "$$n \\ge \\frac{(1{,}96)^2 \\times 0{,}5 \\times (1 - 0{,}5)}{(0{,}03)^2} = \\frac{3{,}8416 \\times 0{,}25}{0{,}0009} = \\frac{0{,}9604}{0{,}0009} \\approx 1067{,}11$$"
            "Vì cỡ mẫu phải là số nguyên, ta luôn làm tròn lên số nguyên tiếp theo:<br>"
            "$$n = \\lceil 1067{,}11 \\rceil = 1068\\text{ (cử tri)}$$"
            "<b>Kết luận:</b> Cần phỏng vấn tối thiểu <b>1068 cử tri</b>.",
            "<b>Bước 3: Tính kích thước mẫu khi biết p ≈ 0,2 `[+0,30đ]`</b><br>"
            "Khi đã có thông tin sơ bộ $p = 0{,}2$, ta có: $p(1 - p) = 0{,}2 \\times 0{,}8 = 0{,}16$:<br>"
            "$$n \\ge \\frac{(1{,}96)^2 \\times 0{,}16}{(0{,}03)^2} = \\frac{3{,}8416 \\times 0{,}16}{0{,}0009} = \\frac{0{,}614656}{0{,}0009} \\approx 682{,}95$$"
            "Làm tròn lên số nguyên tiếp theo:<br>"
            "$$n = \\lceil 682{,}95 \\rceil = 683\\text{ (cử tri)}$$"
            "<b>Nhận xét:</b> Việc có thêm thông tin ban đầu $p = 0{,}2$ giúp tiết kiệm được $1068 - 683 = 385$ cuộc phỏng vấn (giảm hơn $36\\%$ chi phí điều tra)."
        ],
        "pro_tips": "Con số xấp xỉ 1068 (hoặc ~1000 người) chính là quy chuẩn cỡ mẫu quốc tế thường thấy trên các bản tin khảo sát chính trị và thị trường!",
        "pitfalls": "Làm tròn số học thông thường xuống 1067 (nhớ rằng trong tính cỡ mẫu, LUÔN LUÔN làm tròn lên $\\lceil \\dots \\rceil$ để bảo đảm sai số không bị đội lên quá 3%)."
    })

    # TL7_7 (Nâng cao)
    exercises.append({
        "id": "TL7_7", "topicId": 7, "level": "Nâng cao",
        "title": "Bóng đèn dự phòng và Giải phương trình bậc hai tìm kích thước mẫu n",
        "problem": "Một hệ thống quan trắc khoa học dưới đáy biển sâu cần hoạt động chiếu sáng liên tục trong ít nhất $T_0 = 2000\\text{ giờ}$. Khi một bóng đèn bị cháy, hệ thống cơ học sẽ lập tức tự động thay thế bằng một bóng đèn mới dự phòng (thời gian thay thế xem như bằng 0).<br>"
                   "Tuổi thọ của mỗi bóng đèn là các biến ngẫu nhiên độc lập có cùng kỳ vọng $\\mu = 100\\text{ giờ}$ và độ lệch chuẩn $\\sigma = 30\\text{ giờ}$.<br>"
                   "Hỏi phòng thí nghiệm cần lắp đặt dự phòng <b>tối thiểu bao nhiêu bóng đèn ($n$)</b> để đảm bảo xác suất hệ thống chiếu sáng hoạt động liên tục suốt 2000 giờ đạt từ $95\\%$ ($0{,}95$) trở lên?<br>"
                   "<i>Cho biết: Giá trị phân vị chuẩn $\\Phi(1{,}645) \\approx 0{,}9500$.</i>",
        "analysis": "Goi n la so bong den. Tong thoi gian chieu sang T_n = sum_{i=1}^n X_i. Theo CLT: T_n ~ N(n*mu, n*sigma^2) = N(100n, 900n). Yeu cau: P(T_n >= 2000) >= 0.95 <=> P(Z >= (2000 - 100n)/(30*sqrt(n))) >= 0.95 <=> (2000 - 100n)/(30*sqrt(n)) <= -1.645. Nhan cheo: 2000 - 100n <= -49.35*sqrt(n) <=> 100n - 49.35*sqrt(n) - 2000 >= 0. Dat u = sqrt(n) > 0. Giai phuong trinh bac hai: 100 u^2 - 49.35 u - 2000 >= 0 => u >= 4.7257 => n >= 22.33 => n = 23 bong.",
        "hints": [
            "Tổng thời gian sáng là T_n = X1 + X2 + ... + Xn.",
            "Yêu cầu P(T_n >= 2000) >= 0.95 tương đương Z <= -1.645.",
            "Đặt u = sqrt(n), phương trình trở thành phương trình bậc hai: 100*u^2 - 49.35*u - 2000 >= 0."
        ],
        "steps": [
            "<b>Bước 1: Mô hình hóa bài toán và Áp dụng Định lý giới hạn trung tâm `[+0,35đ]`</b><br>"
            "Gọi $n$ là số lượng bóng đèn cần sử dụng ($n \\in \\mathbb{N}^*$).<br>"
            "Tổng thời gian chiếu sáng của $n$ bóng đèn là $T_n = \\sum_{i=1}^n X_i$.<br>"
            "Vì các bóng đèn hoạt động độc lập và $n$ đủ lớn, theo CLT:<br>"
            "$$T_n \\approx N(\\mu_n = n\\mu = 100n,\\; \\sigma_n^2 = n\\sigma^2 = n \\times 30^2 = 900n)$$"
            "Độ lệch chuẩn là $\\sigma_n = \\sqrt{900n} = 30\\sqrt{n}$.",
            "<b>Bước 2: Thiết lập bất phương trình chuẩn hóa xác suất `[+0,35đ]`</b><br>"
            "Hệ thống hoạt động liên tục suốt 2000 giờ khi và chỉ khi $T_n \\ge 2000$.<br>"
            "Chuẩn hóa biến số $T_n$:<br>"
            "$$P(T_n \\ge 2000) = P\\left( \\frac{T_n - 100n}{30\\sqrt{n}} \\ge \\frac{2000 - 100n}{30\\sqrt{n}} \\right) = P\\left( Z \\ge \\frac{2000 - 100n}{30\\sqrt{n}} \\right)$$"
            "$$= 1 - \\Phi\\left( \\frac{2000 - 100n}{30\\sqrt{n}} \\right)$$"
            "Yêu cầu xác suất đạt từ $95\\%$ trở lên:<br>"
            "$$1 - \\Phi\\left( \\frac{2000 - 100n}{30\\sqrt{n}} \\right) \\ge 0{,}95 \\iff \\Phi\\left( \\frac{2000 - 100n}{30\\sqrt{n}} \\right) \\le 0{,}05$$"
            "Tra bảng chuẩn tắc: $\\Phi(-1{,}645) = 0{,}05$. Do hàm $\\Phi$ đồng biến, ta có:<br>"
            "$$\\frac{2000 - 100n}{30\\sqrt{n}} \\le -1{,}645$$",
            "<b>Bước 3: Đặt ẩn phụ u = √n và Giải phương trình bậc hai `[+0,30đ]`</b><br>"
            "Nhân cả hai vế với mẫu số dương $30\\sqrt{n} > 0$:<br>"
            "$$2000 - 100n \\le -1{,}645 \\times 30\\sqrt{n} = -49{,}35\\sqrt{n}$$"
            "Chuyển tất cả sang vế phải:<br>"
            "$$100n - 49{,}35\\sqrt{n} - 2000 \\ge 0$$"
            "Đặt ẩn phụ $u = \\sqrt{n} > 0$. Ta được bất phương trình bậc hai:<br>"
            "$$100u^2 - 49{,}35u - 2000 \\ge 0$$"
            "Tính biệt thức $\\Delta$:<br>"
            "$$\\Delta = (-49{,}35)^2 - 4(100)(-2000) = 2435{,}42 + 800000 = 802435{,}42$$"
            "$$\\sqrt{\\Delta} = \\sqrt{802435{,}42} \\approx 895{,}7876$$"
            "Nghiệm dương của phương trình là:<br>"
            "$$u \\ge \\frac{49{,}35 + 895{,}7876}{2 \\times 100} = \\frac{945{,}1376}{200} \\approx 4{,}7257$$"
            "Bình phương hai vế để tìm $n$:<br>"
            "$$n = u^2 \\ge (4{,}7257)^2 \\approx 22{,}332$$"
            "Vì số lượng bóng đèn phải là số nguyên dương, ta làm tròn lên:<br>"
            "$$n = \\lceil 22{,}332 \\rceil = 23$$"
            "<b>Kết luận:</b> Cần trang bị tối thiểu <b>23 bóng đèn</b> để đảm bảo hệ thống hoạt động liên tục suốt 2000 giờ với độ tin cậy $95\\%$."
        ],
        "pro_tips": "Đây chính là Bài tập vận dụng 5 trong slide week07 (trang 90-91). Kỹ thuật đặt $u = \\sqrt{n}$ để giải bất phương trình bậc hai là dạng bài phân loại 9-10 điểm của đề thi giữa kỳ!",
        "pitfalls": "Quên dấu âm $-1{,}645$ khi đổi từ $1 - \\Phi \\ge 0{,}95$ sang $\\Phi \\le 0{,}05$, dẫn đến phương trình sai hoàn toàn."
    })

    # TL7_8 (Nâng cao)
    exercises.append({
        "id": "TL7_8", "topicId": 7, "level": "Nâng cao",
        "title": "Quản trị rủi ro bảo hiểm: Doanh thu, Chi bồi thường và Xác suất vỡ quỹ",
        "problem": "Một công ty bảo hiểm phát hành $n = 10.000$ hợp đồng bảo hiểm xe máy trong năm với mức phí thu về là $100.000\\text{ đồng/hợp đồng}$. Xác suất một hợp đồng gặp sự cố bồi thường trong năm là $p = 0{,}01$. Mỗi vụ bồi thường công ty phải chi trả số tiền cố định là $5.000.000\\text{ đồng}$. Giả sử các vụ tai nạn của các chủ xe là độc lập.<br>"
                   "1. Tính tổng doanh thu phí bảo hiểm thu về và số vụ bồi thường kỳ vọng trong năm.<br>"
                   "2. Dùng Định lý giới hạn trung tâm, hãy ước tính xác suất công ty bị thua lỗ trong năm tài chính này (tức tổng tiền chi bồi thường vượt quá tổng doanh thu phí).<br>"
                   "3. Để đảm bảo an toàn tuyệt đối sao cho xác suất chi trả vượt quá quỹ dự phòng nhỏ hơn $0{,}1\\%$ ($Z_{0{,}001} = 3{,}09$), công ty cần chuẩn bị quỹ dự phòng bồi thường tối thiểu là bao nhiêu tiền?",
        "analysis": "1. Doanh thu = 10000 * 100.000 = 1.000.000.000 VND (1 ty dong). So vu boi thuong K ~ B(10000, 0.01). mu_K = 100 vu, sigma_K = sqrt(10000 * 0.01 * 0.99) = sqrt(99) approx 9.94987 vu. 2. Tien boi thuong S = K * 5.000.000 VND. Cong ty lo khi S > 1 ty <=> K > 1.000.000.000 / 5.000.000 = 200 vu. Chuẩn hóa Z = (200 - 100) / 9.94987 = 100 / 9.95 = 10.05. P(K > 200) = 1 - Phi(10.05) approx 0 (nho hon 10^(-20)). 3. Quy du phong: Can P(K > k*) <= 0.001 <=> (k* - 100)/9.95 = 3.09 <=> k* = 100 + 3.09 * 9.95 = 100 + 30.7455 = 130.75 vu. So tien = 131 * 5.000.000 = 655.000.000 VND (655 trieu dong).",
        "hints": [
            "Doanh thu = 1 tỷ đồng. Mỗi vụ chi 5 triệu -> Lỗ khi có hơn 200 vụ tai nạn.",
            "Số vụ tai nạn K có kỳ vọng mu = 100 vụ, độ lệch chuẩn sigma = sqrt(99) = 9.95 vụ.",
            "200 vụ cách kỳ vọng tới 10 lần độ lệch chuẩn (Z = 10.05)!"
        ],
        "steps": [
            "<b>Bước 1: Tính doanh thu và Kỳ vọng số vụ bồi thường `[+0,30đ]`</b><br>"
            "- Tổng doanh thu phí bảo hiểm thu về:<br>"
            "$$\\text{Doanh thu} = 10.000 \\times 100.000 = 1.000.000.000\\text{ (đồng) } = 1\\text{ tỷ đồng}$$"
            "- Gọi $K$ là số vụ tai nạn phát sinh bồi thường. Vì các hợp đồng độc lập, $K \\sim B(n = 10.000,\\; p = 0{,}01)$:<br>"
            "  + Số vụ bồi thường kỳ vọng: $E(K) = n \\cdot p = 10.000 \\times 0{,}01 = 100\\text{ (vụ)}$<br>"
            "  + Độ lệch chuẩn số vụ bồi thường:<br>"
            "$$\\sigma_K = \\sqrt{n p (1 - p)} = \\sqrt{10.000 \\times 0{,}01 \\times 0{,}99} = \\sqrt{99} \\approx 9{,}9499\\text{ (vụ)}$$",
            "<b>Bước 2: Tính xác suất công ty bảo hiểm bị thua lỗ `[+0,35đ]`</b><br>"
            "Mỗi vụ bồi thường chi trả 5 triệu đồng ($5.000.000$ đồng).<br>"
            "Tổng số tiền chi trả bồi thường là: $S = K \\times 5.000.000$ đồng.<br>"
            "Công ty bị lỗ khi tiền chi vượt quá doanh thu thu vào:<br>"
            "$$S > 1.000.000.000 \\iff K \\times 5.000.000 > 1.000.000.000 \\iff K > 200\\text{ (vụ)}$$"
            "Theo CLT, biến $K$ xấp xỉ chuẩn $N(100;\\; 9{,}95^2)$. Chuẩn hóa giá trị 200 vụ:<br>"
            "$$Z = \\frac{200 - 100}{9{,}9499} = \\frac{100}{9{,}9499} \\approx 10{,}05$$"
            "Xác suất bị thua lỗ là:<br>"
            "$$P(\\text{Lỗ}) = P(K > 200) = 1 - \\Phi(10{,}05) \\approx 0\\text{ (nhỏ hơn } 10^{-20}\\text{)}$$"
            "<b>Kết luận:</b> Xác suất công ty bảo hiểm bị lỗ là bằng $0$ trên thực tế.",
            "<b>Bước 3: Xác định quỹ dự phòng bồi thường an toàn `[+0,35đ]`</b><br>"
            "Để rủi ro vỡ quỹ nhỏ hơn $0{,}1\\%$ ($0{,}001$), số vụ tai nạn tối đa cần dự phòng $k^*$ phải thỏa mãn:<br>"
            "$$P(K > k^*) \\le 0{,}001 \\iff P(K \\le k^*) \\ge 0{,}999$$"
            "Chuẩn hóa: $\\frac{k^* - 100}{9{,}9499} = Z_{0{,}001} = 3{,}09$:<br>"
            "$$k^* = 100 + 3{,}09 \\times 9{,}9499 = 100 + 30{,}745 \\approx 130{,}75\\text{ (vụ)}$$"
            "Làm tròn lên số vụ an toàn: $k^* = 131$ vụ bồi thường.<br>"
            "Quỹ dự phòng tài chính tối thiểu cần thiết:<br>"
            "$$\\text{Quỹ dự phòng} = 131 \\times 5.000.000 = 655.000.000\\text{ (đồng) } = 655\\text{ triệu đồng}$$"
            "<i>(Nhận xét: Trong 1 tỷ đồng doanh thu, công ty chỉ cần trích ra 655 triệu làm quỹ bồi thường an toàn 99,9%, 345 triệu đồng còn lại là lợi nhuận chắc chắn và chi phí quản lý vận hành!).</i>"
        ],
        "pro_tips": "Đây là bài toán kinh tế thực tế xuất sắc minh họa vì sao ngành bảo hiểm là một trong những ngành kinh doanh có biên lợi nhuận ổn định nhất trên thế giới nhờ Luật số lớn và CLT.",
        "pitfalls": "Quên nhân số vụ với số tiền bồi thường 5.000.000 đồng khi tính số tiền của quỹ dự phòng."
    })

    return exercises

if __name__ == "__main__":
    t7 = get_topic_7()
    print(f"Generated Topic 7: {len(t7)} exercises.")
