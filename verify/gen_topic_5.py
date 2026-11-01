# Topic 5: Tổng, Trung bình mẫu i.i.d. & Bất đẳng thức Chebyshev (TL5_1 -> TL5_8)
import math
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_topic_5():
    exercises = []

    # TL5_1 (Cơ bản)
    exercises.append({
        "id": "TL5_1", "topicId": 5, "level": "Cơ bản",
        "title": "Mô hình chiếc hộp (Box Model) và Định luật Căn bậc hai (Square Root Law)",
        "problem": "Một chiếc hộp chứa 5 tấm thẻ được đánh số: $\\{1,\\; 2,\\; 3,\\; 4,\\; 5\\}$. Rút ngẫu nhiên có hoàn lại $n = 100$ tấm thẻ từ hộp.<br>"
                   "1. Tính giá trị trung bình $\\mu$ và độ lệch chuẩn $\\sigma$ của các số ghi trong hộp.<br>"
                   "2. Gọi $S_{100}$ là tổng các số ghi trên 100 tấm thẻ rút ra. Tính kỳ vọng $E(S_{100})$ và độ lệch chuẩn $\\operatorname{SD}(S_{100})$.<br>"
                   "3. Gọi $\\bar{X}_{100}$ là trung bình cộng của các số ghi trên 100 tấm thẻ rút ra. Tính kỳ vọng $E(\\bar{X}_{100})$ và độ lệch chuẩn $\\operatorname{SD}(\\bar{X}_{100})$.",
        "analysis": "Hộp có 5 số đều khả năng: mu = (1+2+3+4+5)/5 = 3. Var = sum((x - 3)^2)/5 = (4+1+0+1+4)/5 = 2 => sigma = sqrt(2) approx 1.4142. Dùng định luật căn bậc hai: E(S_n) = n*mu, SD(S_n) = sigma*sqrt(n). E(Xbar_n) = mu, SD(Xbar_n) = sigma/sqrt(n).",
        "hints": [
            "Trung bình hộp mu = 3. Phương sai hộp sigma^2 = [(1-3)^2 + ... + (5-3)^2] / 5 = 2.",
            "Tổng S_100: E(S_100) = 100 * mu; SD(S_100) = sigma * sqrt(100).",
            "Trung bình Xbar_100: E(Xbar_100) = mu; SD(Xbar_100) = sigma / sqrt(100)."
        ],
        "steps": [
            "<b>Bước 1: Tính trung bình μ và độ lệch chuẩn σ của chiếc hộp `[+0,30đ]`</b><br>"
            "Các số trong hộp là $\\{1, 2, 3, 4, 5\\}$ với xác suất mỗi số bằng $p = 1/5 = 0{,}2$.<br>"
            "- Giá trị trung bình của hộp (Box Average):<br>"
            "$$\\mu = \\frac{1 + 2 + 3 + 4 + 5}{5} = \\frac{15}{5} = 3{,}0$$"
            "- Phương sai của hộp (Box Variance):<br>"
            "$$\\sigma^2 = \\frac{(1 - 3)^2 + (2 - 3)^2 + (3 - 3)^2 + (4 - 3)^2 + (5 - 3)^2}{5} = \\frac{4 + 1 + 0 + 1 + 4}{5} = \\frac{10}{5} = 2{,}0$$"
            "- Độ lệch chuẩn của hộp (Box SD):<br>"
            "$$\\sigma = \\sqrt{2{,}0} \\approx 1{,}4142$$",
            "<b>Bước 2: Tính kỳ vọng và độ lệch chuẩn của TỔNG S₁₀₀ `[+0,35đ]`</b><br>"
            "Theo Định luật Căn bậc hai (Square Root Law) cho tổng các biến ngẫu nhiên i.i.d.:<br>"
            "- Kỳ vọng của tổng:<br>"
            "$$E(S_{100}) = n \\cdot \\mu = 100 \\times 3{,}0 = 300{,}0$$"
            "- Độ lệch chuẩn của tổng:<br>"
            "$$\\operatorname{SD}(S_{100}) = \\sqrt{n} \\cdot \\sigma = \\sqrt{100} \\times \\sqrt{2} = 10 \\times 1{,}4142 \\approx 14{,}1421$$",
            "<b>Bước 3: Tính kỳ vọng và độ lệch chuẩn của TRUNG BÌNH X̄₁₀₀ `[+0,35đ]`</b><br>"
            "Theo Định luật Căn bậc hai cho trung bình mẫu i.i.d.:<br>"
            "- Kỳ vọng của trung bình mẫu:<br>"
            "$$E(\\bar{X}_{100}) = \\mu = 3{,}0$$"
            "- Sai số chuẩn của trung bình mẫu (Standard Error):<br>"
            "$$\\operatorname{SD}(\\bar{X}_{100}) = \\frac{\\sigma}{\\sqrt{n}} = \\frac{\\sqrt{2}}{\\sqrt{100}} = \\frac{1{,}4142}{10} \\approx 0{,}1414$$"
        ],
        "pro_tips": "Nhớ nhanh quy tắc tỉ lệ: Khi cỡ mẫu $n$ tăng gấp 100 lần, độ bất định của Tổng tăng gấp 10 lần (nhân $\\sqrt{n}$), nhưng độ bất định của Trung bình giảm đi 10 lần (chia $\\sqrt{n}$).",
        "pitfalls": "Nhầm lẫn nhân $\\sqrt{n}$ cho trung bình mẫu thay vì chia cho $\\sqrt{n}$."
    })

    # TL5_2 (Cơ bản)
    exercises.append({
        "id": "TL5_2", "topicId": 5, "level": "Cơ bản",
        "title": "Bất đẳng thức Chebyshev: Đánh giá xác suất khi chưa biết phân phối",
        "problem": "Một biến ngẫu nhiên $X$ có kỳ vọng $\\mu = E(X) = 50$ và độ lệch chuẩn $\\sigma = \\operatorname{SD}(X) = 5$. Chưa biết phân phối xác suất cụ thể của $X$.<br>"
                   "1. Phát biểu bất đẳng thức Chebyshev dạng 'trong khoảng' và dạng 'ngoài khoảng'.<br>"
                   "2. Đánh giá cận dưới cho xác suất $P(40 < X < 60)$.<br>"
                   "3. Đánh giá cận trên cho xác suất $P(|X - 50| \\ge 15)$.",
        "analysis": "Chebyshev: P(|X - mu| >= k*sigma) <= 1/k^2 và P(|X - mu| < k*sigma) >= 1 - 1/k^2. Câu 2: khoảng (40, 60) tương ứng |X - 50| < 10 = 2*sigma => k=2 => P >= 1 - 1/4 = 0.75. Câu 3: |X - 50| >= 15 = 3*sigma => k=3 => P <= 1/9 approx 0.1111.",
        "hints": [
            "Khoảng (40, 60) cách tâm mu = 50 một khoảng delta = 10.",
            "Số lần độ lệch chuẩn k = delta / sigma = 10 / 5 = 2.",
            "Cận dưới trong khoảng: >= 1 - 1/k^2. Cận trên ngoài khoảng: <= 1/k^2."
        ],
        "steps": [
            "<b>Bước 1: Phát biểu bất đẳng thức Chebyshev `[+0,30đ]`</b><br>"
            "Với mọi biến ngẫu nhiên $X$ có kỳ vọng $\\mu$ và phương sai hữu hạn $\\sigma^2$, và với mọi số thực $k > 0$:<br>"
            "- Dạng ngoài khoảng (Đuôi phân phối):<br>"
            "$$P(|X - \\mu| \\ge k\\sigma) \\le \\frac{1}{k^2}$$"
            "- Dạng trong khoảng (Vùng trung tâm):<br>"
            "$$P(|X - \\mu| < k\\sigma) \\ge 1 - \\frac{1}{k^2}$$",
            "<b>Bước 2: Đánh giá cận dưới cho xác suất P(40 < X < 60) `[+0,35đ]`</b><br>"
            "Biến cố $40 < X < 60$ tương đương với:<br>"
            "$$40 - 50 < X - 50 < 60 - 50 \\iff -10 < X - 50 < 10 \\iff |X - 50| < 10$$"
            "Vì $\\sigma = 5$, ta có $10 = 2 \\times 5 = 2\\sigma \\implies k = 2$.<br>"
            "Áp dụng bất đẳng thức Chebyshev dạng trong khoảng:<br>"
            "$$P(|X - 50| < 2\\sigma) \\ge 1 - \\frac{1}{2^2} = 1 - \\frac{1}{4} = 0{,}75\\text{ (hay 75\\%)}$$"
            "<b>Kết luận:</b> Xác suất để $X$ nằm giữa 40 và 60 luôn đạt ít nhất $75\\%$, bất kể $X$ mang phân phối gì.",
            "<b>Bước 3: Đánh giá cận trên cho xác suất P(|X - 50| ≥ 15) `[+0,35đ]`</b><br>"
            "Vì $\\sigma = 5$, khoảng cách $15 = 3 \\times 5 = 3\\sigma \\implies k = 3$.<br>"
            "Áp dụng bất đẳng thức Chebyshev dạng ngoài khoảng:<br>"
            "$$P(|X - 50| \\ge 3\\sigma) \\le \\frac{1}{3^2} = \\frac{1}{9} \\approx 0{,}1111\\text{ (hay 11{,}11\\%)}$$"
            "<b>Kết luận:</b> Xác suất để $X$ lệch khỏi giá trị trung bình từ 15 đơn vị trở lên không bao giờ vượt quá $11{,}11\\%$."
        ],
        "pro_tips": "Sức mạnh độc nhất vô nhị của Chebyshev là: Áp dụng được cho MỌI phân phối xác suất (kể cả phân phối quái dị, lệch mạnh) mà không cần giả định phân phối chuẩn!",
        "pitfalls": "Dùng $k = 10$ thay vì $k = 10/\\sigma = 2$ (quên chia cho độ lệch chuẩn)."
    })

    # TL5_3 (Cơ bản)
    exercises.append({
        "id": "TL5_3", "topicId": 5, "level": "Cơ bản",
        "title": "Định luật Số lớn Yếu (WLLN): Chứng minh và Ý nghĩa thực tiễn",
        "problem": "Cho dãy các biến ngẫu nhiên độc lập cùng phân phối (i.i.d.) $X_1, X_2, \\dots, X_n$ có cùng kỳ vọng $\\mu$ và phương sai $\\sigma^2 < \\infty$. Đặt $\\bar{X}_n = \\frac{1}{n}\\sum_{i=1}^n X_i$.<br>"
                   "1. Phát biểu Định luật số lớn yếu (Weak Law of Large Numbers - WLLN).<br>"
                   "2. Dùng bất đẳng thức Chebyshev để chứng minh định luật này.<br>"
                   "3. Nêu ý nghĩa của luật số lớn trong mô hình kinh doanh của các công ty bảo hiểm và sòng bạc.",
        "analysis": "WLLN: Voi moi epsilon > 0, lim P(|Xbar_n - mu| >= epsilon) = 0 khi n -> infinity. Chung minh: E(Xbar_n) = mu, Var(Xbar_n) = sigma^2/n. Ap dung Chebyshev voi k*sigma_Xbar = epsilon => P <= Var(Xbar_n)/epsilon^2 = sigma^2 / (n * epsilon^2) -> 0 khi n -> infty.",
        "hints": [
            "Trung bình mẫu Xbar_n có E(Xbar_n) = mu và Var(Xbar_n) = sigma^2 / n.",
            "Bất đẳng thức Chebyshev cho Xbar_n: P(|Xbar_n - mu| >= epsilon) <= Var(Xbar_n) / epsilon^2.",
            "Khi n tiến ra vô cùng, sigma^2 / (n * epsilon^2) tiến về 0."
        ],
        "steps": [
            "<b>Bước 1: Phát biểu Định luật số lớn yếu (WLLN) `[+0,30đ]`</b><br>"
            "Cho $X_1, X_2, \\dots, X_n$ là các biến ngẫu nhiên i.i.d. có kỳ vọng $\\mu$ và phương sai $\\sigma^2$ hữu hạn. Khi đó với mọi số dương $\\varepsilon > 0$ nhỏ tùy ý, ta có:<br>"
            "$$\\lim_{n \\to \\infty} P(|\\bar{X}_n - \\mu| \\ge \\varepsilon) = 0$$"
            "Hoặc tương đương:<br>"
            "$$\\lim_{n \\to \\infty} P(|\\bar{X}_n - \\mu| < \\varepsilon) = 1$$"
            "<i>(Nói cách khác: Trung bình mẫu $\\bar{X}_n$ hội tụ theo xác suất về kỳ vọng lý thuyết $\\mu$).</i>",
            "<b>Bước 2: Chứng minh bằng Bất đẳng thức Chebyshev `[+0,40đ]`</b><br>"
            "Xét biến ngẫu nhiên trung bình mẫu $\\bar{X}_n$:<br>"
            "- Kỳ vọng: $E(\\bar{X}_n) = \\mu$.<br>"
            "- Phương sai: $\\operatorname{Var}(\\bar{X}_n) = \\frac{\\sigma^2}{n}$.<br>"
            "Áp dụng bất đẳng thức Chebyshev cho biến $\\bar{X}_n$ với độ lệch $\\varepsilon > 0$:<br>"
            "$$P(|\\bar{X}_n - \\mu| \\ge \\varepsilon) \\le \\frac{\\operatorname{Var}(\\bar{X}_n)}{\\varepsilon^2} = \\frac{\\sigma^2}{n \\varepsilon^2}$$"
            "Lấy giới hạn hai vế khi $n \\to \\infty$, vì $\\sigma^2$ và $\\varepsilon^2 > 0$ là các hằng số cố định:<br>"
            "$$\\lim_{n \\to \\infty} \\frac{\\sigma^2}{n \\varepsilon^2} = 0$$"
            "Vì xác suất luôn không âm ($P \\ge 0$), theo nguyên lý kẹp ta suy ra:<br>"
            "$$0 \\le \\lim_{n \\to \\infty} P(|\\bar{X}_n - \\mu| \\ge \\varepsilon) \\le 0 \\implies \\lim_{n \\to \\infty} P(|\\bar{X}_n - \\mu| \\ge \\varepsilon) = 0\\text{ (đpcm)}.$$",
            "<b>Bước 3: Nêu ý nghĩa thực tiễn `[+0,30đ]`</b><br>"
            "- <b>Trong sòng bạc:</b> Dù trong 1 ván đơn lẻ kết quả hoàn toàn ngẫu nhiên và người chơi có thể thắng, nhưng khi có hàng triệu lượt chơi ($n$ cực lớn), tỉ lệ tiền thắng thực tế của nhà cái sẽ hội tụ chắc chắn về kỳ vọng toán học dương của họ. Nhà cái luôn luôn có lãi chắc chắn về dài hạn.<br>"
            "- <b>Trong bảo hiểm:</b> Một khách hàng gặp rủi ro là ngẫu nhiên, nhưng khi bán cho hàng chục ngàn hợp đồng ($n$ rất lớn), số tiền bồi thường trung bình mỗi hợp đồng sẽ bám sát kỳ vọng $\\mu$, giúp công ty định giá phí bảo hiểm chính xác và triệt tiêu rủi ro phá sản."
        ],
        "pro_tips": "Đây là câu hỏi lý thuyết kinh điển trong đề thi giữa kỳ UET. Luôn trình bày đủ 3 dòng: Kỳ vọng $\\bar{X}_n$, Phương sai $\\bar{X}_n$, và Bất đẳng thức Chebyshev chia cho $\\varepsilon^2$.",
        "pitfalls": "Quên ghi điều kiện $\\varepsilon > 0$ hoặc quên giải thích vì sao $\\operatorname{Var}(\\bar{X}_n) = \\sigma^2/n$."
    })

    # TL5_4 (Trung bình)
    exercises.append({
        "id": "TL5_4", "topicId": 5, "level": "Trung bình",
        "title": "Ước lượng khoảng tin cậy Chebyshev cho thời gian giao hàng",
        "problem": "Thời gian giao hàng của một ứng dụng đồ ăn nhanh có giá trị trung bình là $\\mu = 30$ phút và độ lệch chuẩn là $\\sigma = 6$ phút. Do địa hình và thời tiết, phân phối thời gian giao hàng không đối xứng và chưa xác định.<br>"
                   "1. Sử dụng bất đẳng thức Chebyshev, hãy tìm cận dưới của xác suất một đơn hàng bất kỳ được giao trong khoảng từ 18 đến 42 phút.<br>"
                   "2. Ứng dụng muốn đưa ra cam kết thời gian giao hàng trong khoảng $[30 - c,\\; 30 + c]$ phút sao cho xác suất đơn hàng đến đúng hạn trong khoảng này đạt ít nhất $8/9$ ($88{,}89\\%$). Hãy tìm giá trị $c$ tối thiểu thỏa mãn điều kiện.",
        "analysis": "1. Khoảng [18, 42] là |X - 30| < 12 = 2*sigma => k = 2. Cận dưới = 1 - 1/4 = 75%. 2. Đạt ít nhất 8/9 <=> 1 - 1/k^2 >= 8/9 <=> 1/k^2 <= 1/9 <=> k >= 3. c = k * sigma = 3 * 6 = 18 phút.",
        "hints": [
            "Độ rộng nửa khoảng delta = 42 - 30 = 30 - 18 = 12 phút.",
            "Số lần độ lệch chuẩn: k = 12 / 6 = 2.",
            "1 - 1/k^2 >= 8/9 -> 1/k^2 <= 1/9 -> k >= 3 -> c = 3 * 6 = 18 phút."
        ],
        "steps": [
            "<b>Bước 1: Tính cận dưới cho xác suất đơn hàng giao trong khoảng [18; 42] phút `[+0,40đ]`</b><br>"
            "Biến cố $18 < X < 42$ tương đương với:<br>"
            "$$18 - 30 < X - 30 < 42 - 30 \\iff -12 < X - 30 < 12 \\iff |X - 30| < 12$$"
            "Vì độ lệch chuẩn $\\sigma = 6$ phút, ta có:<br>"
            "$$k = \\frac{12}{\\sigma} = \\frac{12}{6} = 2$$"
            "Áp dụng bất đẳng thức Chebyshev:<br>"
            "$$P(|X - 30| < 2\\sigma) \\ge 1 - \\frac{1}{2^2} = 1 - \\frac{1}{4} = 0{,}75\\text{ (hay 75\\%)}$$"
            "Vậy xác suất đơn hàng được giao trong khoảng từ 18 đến 42 phút ít nhất là $75\\%$.",
            "<b>Bước 2: Tìm giá trị c để xác suất đạt ít nhất 8/9 `[+0,60đ]`</b><br>"
            "Yêu cầu bài toán: Tìm $c > 0$ sao cho:<br>"
            "$$P(|X - 30| < c) \\ge \\frac{8}{9}$$"
            "Theo bất đẳng thức Chebyshev, với $c = k\\sigma$, ta luôn có:<br>"
            "$$P(|X - 30| < k\\sigma) \\ge 1 - \\frac{1}{k^2}$$"
            "Để bảo đảm xác suất đạt ít nhất $8/9$ với mọi phân phối có thể có, ta cần:<br>"
            "$$1 - \\frac{1}{k^2} \\ge \\frac{8}{9} \\iff \\frac{1}{k^2} \\le 1 - \\frac{8}{9} = \\frac{1}{9}$$"
            "Vì $k > 0$, suy ra:<br>"
            "$$k^2 \\ge 9 \\iff k \\ge 3$$"
            "Do đó khoảng dung sai tối thiểu cần thiết là:<br>"
            "$$c = k \\cdot \\sigma = 3 \\times 6 = 18\\text{ (phút)}$$"
            "<b>Kết luận:</b> Khoảng thời gian cam kết cần đưa ra là $[30 - 18;\\; 30 + 18] = [12;\\; 48]$ phút (tức từ 12 đến 48 phút)."
        ],
        "pro_tips": "Dấu bất đẳng thức: Khi $1 - 1/k^2 \\ge 1 - \\alpha$, chuyển vế được $k \\ge \\frac{1}{\\sqrt{\\alpha}}$.",
        "pitfalls": "Quên nhân $k$ với $\\sigma$ ở bước cuối (kết luận $c = 3$ phút thay vì $c = 18$ phút)."
    })

    # TL5_5 (Trung bình)
    exercises.append({
        "id": "TL5_5", "topicId": 5, "level": "Trung bình",
        "title": "Mô hình chiếc hộp cho trò chơi quay số và Phân tích tổng tiền thưởng",
        "problem": "Một vòng quay may mắn có bảng phân phối tiền thưởng cho 1 lượt quay như sau:<br>"
                   "<table class='data-table'><tr><th>Mức thưởng x (nghìn đồng)</th><td>0</td><td>20</td><td>50</td><td>100</td><td>Tổng</td></tr>"
                   "<tr><th>Xác suất P(X = x)</th><td>0,50</td><td>0,30</td><td>0,15</td><td>0,05</td><td>1,00</td></tr></table>"
                   "Một người chơi thực hiện quay $n = 400$ lượt độc lập.<br>"
                   "1. Tính tiền thưởng kỳ vọng $\\mu$ và độ lệch chuẩn $\\sigma$ của 1 lượt quay.<br>"
                   "2. Tính kỳ vọng và độ lệch chuẩn của tổng số tiền thưởng mà người chơi nhận được sau 400 lượt.<br>"
                   "3. So sánh tốc độ tăng của Kỳ vọng tổng (theo $n$) và Độ lệch chuẩn tổng (theo $\\sqrt{n}$).",
        "analysis": "1. mu = 0(0.5) + 20(0.3) + 50(0.15) + 100(0.05) = 0 + 6 + 7.5 + 5 = 18.5 nghìn. E(X^2) = 0 + 400(0.3) + 2500(0.15) + 10000(0.05) = 120 + 375 + 500 = 995. Var(X) = 995 - 18.5^2 = 995 - 342.25 = 652.75 => sigma = sqrt(652.75) approx 25.54898. 2. n=400: E(S_400) = 400 * 18.5 = 7400 nghìn (7.4 triệu). SD(S_400) = 20 * 25.54898 = 510.9796 nghìn.",
        "hints": [
            "mu = sum x * p = 18.5 nghìn. E(X^2) = sum x^2 * p = 995.",
            "Var(X) = E(X^2) - mu^2 = 995 - 342.25 = 652.75.",
            "Tổng 400 lượt: E(S) = 400 * mu; SD(S) = sqrt(400) * sigma = 20 * sigma."
        ],
        "steps": [
            "<b>Bước 1: Tính kỳ vọng và độ lệch chuẩn của 1 lượt quay `[+0,40đ]`</b><br>"
            "- Kỳ vọng tiền thưởng 1 lượt:<br>"
            "$$\\mu = E(X) = 0(0{,}50) + 20(0{,}30) + 50(0{,}15) + 100(0{,}05) = 0 + 6{,}0 + 7{,}5 + 5{,}0 = 18{,}5\\text{ (nghìn đồng)}$$"
            "- Kỳ vọng của bình phương:<br>"
            "$$E(X^2) = 0^2(0{,}50) + 20^2(0{,}30) + 50^2(0{,}15) + 100^2(0{,}05)$$"
            "$$E(X^2) = 0 + 400(0{,}30) + 2500(0{,}15) + 10000(0{,}05) = 120 + 375 + 500 = 995{,}0$$"
            "- Phương sai và độ lệch chuẩn:<br>"
            "$$\\sigma^2 = \\operatorname{Var}(X) = E(X^2) - [E(X)]^2 = 995{,}0 - (18{,}5)^2 = 995{,}0 - 342{,}25 = 652{,}75$$"
            "$$\\sigma = \\sqrt{652{,}75} \\approx 25{,}5490\\text{ (nghìn đồng)}$$",
            "<b>Bước 2: Tính kỳ vọng và độ lệch chuẩn của tổng tiền thưởng sau 400 lượt `[+0,35đ]`</b><br>"
            "Gọi $S_{400} = \\sum_{i=1}^{400} X_i$ là tổng tiền thưởng.<br>"
            "- Kỳ vọng của tổng tiền thưởng:<br>"
            "$$E(S_{400}) = n \\cdot \\mu = 400 \\times 18{,}5 = 7400\\text{ (nghìn đồng) } = 7{,}4\\text{ triệu đồng}$$"
            "- Độ lệch chuẩn của tổng tiền thưởng:<br>"
            "$$\\operatorname{SD}(S_{400}) = \\sqrt{n} \\cdot \\sigma = \\sqrt{400} \\times 25{,}5490 = 20 \\times 25{,}5490 \\approx 510{,}98\\text{ (nghìn đồng)}$$",
            "<b>Bước 3: So sánh tốc độ tăng trưởng `[+0,25đ]`</b><br>"
            "- Kỳ vọng của tổng tăng tuyến tính theo số lượt $n$ (tỉ lệ với $n$).<br>"
            "- Độ lệch chuẩn của tổng chỉ tăng theo căn bậc hai $\\sqrt{n}$.<br>"
            "- Do đó tỉ số biến thiên $\\frac{\\operatorname{SD}(S_n)}{E(S_n)} = \\frac{\\sigma\\sqrt{n}}{n\\mu} = \\frac{\\sigma}{\\mu\\sqrt{n}}$ giảm dần về 0 khi $n$ tăng lớn. Dao động ngẫu nhiên trở nên rất nhỏ so với quy mô tổng thể!"
        ],
        "pro_tips": "Luôn quy đổi đơn vị rõ ràng (nghìn đồng $\\rightarrow$ triệu đồng) để bài làm sáng sủa và chuẩn chỉnh.",
        "pitfalls": "Bình phương nhầm $E(X^2)$ bằng $[E(X)]^2$."
    })

    # TL5_6 (Trung bình)
    exercises.append({
        "id": "TL5_6", "topicId": 5, "level": "Trung bình",
        "title": "So sánh cận Chebyshev với xác suất thực tế trên phân phối rời rạc",
        "problem": "Gieo một con xúc xắc 6 mặt cân đối và đồng chất. Gọi $X$ là số chấm xuất hiện ($X \\in \\{1, 2, 3, 4, 5, 6\\}$).<br>"
                   "1. Tính kỳ vọng $\\mu$ và độ lệch chuẩn $\\sigma$ của $X$.<br>"
                   "2. Dùng bất đẳng thức Chebyshev, hãy ước lượng cận dưới cho xác suất $P(|X - 3{,}5| < 2{,}5)$.<br>"
                   "3. Tính xác suất thực tế chính xác của biến cố trên và nhận xét lý do vì sao cận Chebyshev lại cách xa giá trị thực tế.",
        "analysis": "1. mu = 3.5. Var = (1+4+9+16+25+36)/6 - 3.5^2 = 91/6 - 12.25 = 15.1667 - 12.25 = 2.9167 = 35/12. sigma = sqrt(35/12) approx 1.7078. 2. delta = 2.5 => k = 2.5 / 1.7078 approx 1.46385. Chebyshev: P >= 1 - 1/k^2 = 1 - 1/(1.46385^2) = 1 - 2.9167/6.25 = 1 - 0.4667 = 0.5333 (53.33%). 3. Thuc te: |X - 3.5| < 2.5 <=> 1 < X < 6 <=> X in {2, 3, 4, 5} => P = 4/6 = 2/3 approx 0.6667 (66.67%).",
        "hints": [
            "mu = 3.5, Var(X) = 35/12 approx 2.9167 => sigma approx 1.7078.",
            "k = 2.5 / sigma = 2.5 / sqrt(35/12).",
            "Xác suất thực tế: X chỉ lấy các giá trị {2, 3, 4, 5} -> xác suất 4/6."
        ],
        "steps": [
            "<b>Bước 1: Tính kỳ vọng và độ lệch chuẩn của X `[+0,30đ]`</b><br>"
            "Mỗi mặt có xác suất $P(X = x) = 1/6$ với $x \\in \\{1, 2, 3, 4, 5, 6\\}$.<br>"
            "- Kỳ vọng:<br>"
            "$$\\mu = \\frac{1 + 2 + 3 + 4 + 5 + 6}{6} = \\frac{21}{6} = 3{,}5$$"
            "- Kỳ vọng bình phương:<br>"
            "$$E(X^2) = \\frac{1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2}{6} = \\frac{1 + 4 + 9 + 16 + 25 + 36}{6} = \\frac{91}{6} \\approx 15{,}1667$$"
            "- Phương sai và độ lệch chuẩn:<br>"
            "$$\\sigma^2 = \\frac{91}{6} - (3{,}5)^2 = \\frac{91}{6} - \\frac{49}{4} = \\frac{182 - 147}{12} = \\frac{35}{12} \\approx 2{,}9167$$"
            "$$\\sigma = \\sqrt{\\frac{35}{12}} \\approx 1{,}7078$$",
            "<b>Bước 2: Ước lượng cận dưới theo Bất đẳng thức Chebyshev `[+0,35đ]`</b><br>"
            "Ta xét biến cố $|X - 3{,}5| < 2{,}5$. Độ lệch $\\varepsilon = 2{,}5$.<br>"
            "Số lần độ lệch chuẩn:<br>"
            "$$k = \\frac{\\varepsilon}{\\sigma} = \\frac{2{,}5}{1{,}7078} \\approx 1{,}4639$$"
            "Áp dụng bất đẳng thức Chebyshev:<br>"
            "$$P(|X - 3{,}5| < 2{,}5) \\ge 1 - \\frac{1}{k^2} = 1 - \\frac{\\sigma^2}{\\varepsilon^2} = 1 - \\frac{2{,}9167}{(2{,}5)^2} = 1 - \\frac{2{,}9167}{6{,}25} = 1 - 0{,}4667 = 0{,}5333\\text{ (53{,}33\\%)}$$",
            "<b>Bước 3: Tính xác suất thực tế và Nhận xét `[+0,35đ]`</b><br>"
            "- Biến cố $|X - 3{,}5| < 2{,}5 \\iff -2{,}5 < X - 3{,}5 < 2{,}5 \\iff 1 < X < 6$.<br>"
            "Vì $X$ là số nguyên, các giá trị thỏa mãn là $X \\in \\{2, 3, 4, 5\\}$ (gồm 4 giá trị):<br>"
            "$$P(|X - 3{,}5| < 2{,}5) = \\frac{4}{6} = \\frac{2}{3} \\approx 0{,}6667\\text{ (66{,}67\\%)}$$"
            "- <b>Nhận xét:</b> Xác suất thực tế ($66{,}67\\%$) hoàn toàn thỏa mãn cận dưới Chebyshev ($66{,}67\\% \\ge 53{,}33\\%$). Cận Chebyshev thấp hơn thực tế vì Chebyshev là một cận tổng quát đúng cho <i>mọi</i> phân phối xác suất bất kỳ (kể cả những phân phối cực đoan nhất), do đó khi áp dụng cho các phân phối cụ thể có hình dạng 'đẹp' thì cận này khá thận trọng (conservative)."
        ],
        "pro_tips": "Công thức trực tiếp: $1 - \\frac{1}{k^2} = 1 - \\frac{\\sigma^2}{\\varepsilon^2}$, không cần làm tròn trung gian qua $k$.",
        "pitfalls": "Tính nhầm khoảng: $1 < X < 6$ mà lấy cả giá trị 1 và 6 (phải là dấu ngặt $<$ nên không lấy 2 đầu mút)."
    })

    # TL5_7 (Nâng cao)
    exercises.append({
        "id": "TL5_7", "topicId": 5, "level": "Nâng cao",
        "title": "Xác định kích thước mẫu n tối thiểu theo Chebyshev",
        "problem": "Một viện nghiên cứu muốn ước lượng chiều cao trung bình $\\mu$ của toàn bộ sinh viên trong một đại học quốc gia. Qua các nghiên cứu trước đây, người ta biết độ lệch chuẩn chiều cao của sinh viên là $\\sigma = 10\\text{ cm}$, nhưng chưa biết giá trị kỳ vọng $\\mu$.<br>"
                   "1. Sử dụng bất đẳng thức Chebyshev cho trung bình mẫu $\\bar{X}_n$, hãy thiết lập công thức xác định kích thước mẫu $n$ theo sai số cho phép $\\varepsilon$ và độ tin cậy $1 - \\alpha$.<br>"
                   "2. Cần điều tra tối thiểu bao nhiêu sinh viên ($n$) để đảm bảo sai số giữa chiều cao trung bình mẫu và chiều cao trung bình thực tế không vượt quá $\\varepsilon = 1\\text{ cm}$ với độ tin cậy ít nhất $95\\%$ ($0{,}95$)?",
        "analysis": "1. Chebyshev cho Xbar_n: P(|Xbar_n - mu| >= eps) <= Var(Xbar_n)/eps^2 = sigma^2 / (n * eps^2). Yeu cau P(|Xbar_n - mu| < eps) >= 1 - alpha <=> P(|Xbar_n - mu| >= eps) <= alpha. Vay sigma^2 / (n * eps^2) <= alpha <=> n >= sigma^2 / (alpha * eps^2). 2. sigma = 10, eps = 1, alpha = 0.05 => n >= 10^2 / (0.05 * 1^2) = 100 / 0.05 = 2000 sinh vien.",
        "hints": [
            "Độ tin cậy 95% tương ứng với mức rủi ro alpha = 1 - 0.95 = 0.05.",
            "Var(Xbar_n) = sigma^2 / n.",
            "sigma^2 / (n * eps^2) <= 0.05 -> n >= sigma^2 / (0.05 * eps^2)."
        ],
        "steps": [
            "<b>Bước 1: Thiết lập công thức tìm kích thước mẫu n theo Chebyshev `[+0,40đ]`</b><br>"
            "Giả sử mẫu điều tra gồm $n$ sinh viên $X_1, X_2, \\dots, X_n$ độc lập cùng phân phối có cùng $\\mu$ và $\\sigma$.<br>"
            "Trung bình mẫu $\\bar{X}_n$ có $E(\\bar{X}_n) = \\mu$ và $\\operatorname{Var}(\\bar{X}_n) = \\frac{\\sigma^2}{n}$.<br>"
            "Áp dụng bất đẳng thức Chebyshev cho $\\bar{X}_n$:<br>"
            "$$P(|\\bar{X}_n - \\mu| \\ge \\varepsilon) \\le \\frac{\\operatorname{Var}(\\bar{X}_n)}{\\varepsilon^2} = \\frac{\\sigma^2}{n \\varepsilon^2}$$"
            "Ta mong muốn sai số không vượt quá $\\varepsilon$ với độ tin cậy ít nhất $1 - \\alpha$:<br>"
            "$$P(|\\bar{X}_n - \\mu| < \\varepsilon) \\ge 1 - \\alpha \\iff P(|\\bar{X}_n - \\mu| \\ge \\varepsilon) \\le \\alpha$$"
            "Điều kiện đủ để thỏa mãn với mọi phân phối là:<br>"
            "$$\\frac{\\sigma^2}{n \\varepsilon^2} \\le \\alpha \\iff n \\ge \\frac{\\sigma^2}{\\alpha \\cdot \\varepsilon^2}$$",
            "<b>Bước 2: Thay số và Tính kích thước mẫu n tối thiểu `[+0,40đ]`</b><br>"
            "Các thông số đề bài cung cấp:<br>"
            "- Độ lệch chuẩn: $\\sigma = 10\\text{ cm} \\implies \\sigma^2 = 100$.<br>"
            "- Sai số cho phép: $\\varepsilon = 1\\text{ cm} \\implies \\varepsilon^2 = 1$.<br>"
            "- Độ tin cậy: $1 - \\alpha = 0{,}95 \\implies \\alpha = 1 - 0{,}95 = 0{,}05$.<br>"
            "Thay vào công thức vừa tìm được:<br>"
            "$$n \\ge \\frac{100}{0{,}05 \\times 1^2} = \\frac{100}{0{,}05} = 2000$$",
            "<b>Bước 3: Kết luận `[+0,20đ]`</b><br>"
            "Viện nghiên cứu cần điều tra tối thiểu <b>2000 sinh viên</b> để bảo đảm chắc chắn $95\\%$ rằng sai số của trung bình mẫu không vượt quá 1 cm.<br>"
            "<i>(Ghi chú so sánh: Nếu dùng phân phối Chuẩn/CLT, số mẫu cần thiết chỉ là $n \\approx (1{,}96 \\times 10 / 1)^2 \\approx 385$. Chebyshev đòi hỏi $n=2000$ lớn hơn nhiều vì nó không giả định phân phối chuẩn mà bảo đảm an toàn cho mọi hình dạng phân phối!).</i>"
        ],
        "pro_tips": "Nhớ công thức mẫu: $n \\ge \\frac{\\sigma^2}{\\alpha \\varepsilon^2}$. Đây là công thức nền tảng trong lý thuyết mẫu lớn không tham số.",
        "pitfalls": "Dùng nhầm $\\alpha = 0{,}95$ thay vì $\\alpha = 1 - 0{,}95 = 0{,}05$ dẫn đến kết quả kích thước mẫu nhỏ vô lý."
    })

    # TL5_8 (Nâng cao)
    exercises.append({
        "id": "TL5_8", "topicId": 5, "level": "Nâng cao",
        "title": "Phân tích Bánh xe Roulette: Mô hình chiếc hộp và Quy luật nhà cái luôn thắng",
        "problem": "Bánh xe Roulette kiểu Pháp gồm 37 ô được đánh số từ $0$ đến $36$ (trong đó có 1 ô số 0 màu xanh lá, 18 ô số đỏ và 18 ô số đen). Một người chơi đặt cược 100.000 đồng vào cửa 'Số đỏ'.<br>"
                   "- Nếu quả bóng rơi vào ô màu đỏ (xác suất $18/37$): người chơi nhận lại 100.000 đồng tiền cược và được thưởng thêm 100.000 đồng (lãi ròng $+100$ nghìn đồng).<br>"
                   "- Nếu quả bóng rơi vào ô màu đen hoặc ô số 0 (xác suất $19/37$): người chơi mất toàn bộ 100.000 đồng tiền cược (lãi ròng $-100$ nghìn đồng).<br>"
                   "1. Lập bảng mô hình chiếc hộp biểu diễn số tiền lãi ròng của người chơi trong 1 ván cược. Tính lãi kỳ vọng $\\mu$ và độ lệch chuẩn $\\sigma$ của người chơi.<br>"
                   "2. Một sòng bạc ghi nhận $n = 100.000$ lượt cược như vậy trong 1 tuần. Gọi $S_{n}$ là tổng tiền lãi của sòng bạc (tiền sòng bạc thắng từ người chơi). Tính kỳ vọng $E(S_n)$ và độ lệch chuẩn $\\operatorname{SD}(S_n)$ của sòng bạc.<br>"
                   "3. Dùng Định lý giới hạn trung tâm, hãy ước tính xác suất sòng bạc bị thua lỗ (tổng tiền lãi $S_n < 0$) sau 100.000 lượt cược.",
        "analysis": "1. Nguoi choi: X = +100 voi p = 18/37; X = -100 voi p = 19/37. mu = 100*(18/37) - 100*(19/37) = -100/37 approx -2.7027 nghin dong. E(X^2) = 100^2 = 10000. Var(X) = 10000 - (-2.7027)^2 = 9992.695 => sigma = 99.963 nghin dong. 2. Song bac: Tien lai Y = -X. mu_casino = +2.7027 nghin dong. sigma_casino = 99.963 nghin dong. Sau n=100000: E(S_n) = 100000 * 2.7027 = 270270 nghin (270.27 trieu dong). SD(S_n) = sqrt(100000) * 99.963 = 316.2277 * 99.963 = 31611.1 nghin (31.61 trieu dong). 3. P(S_n < 0): Z = (0 - 270.27) / 31.61 = -8.55 => P < 10^(-17) approx 0! Song bac khong bao gio lo.",
        "hints": [
            "Người chơi có kỳ vọng âm: mu = 100*(18/37) - 100*(19/37) = -100/37 nghìn đồng.",
            "Tiền sòng bạc thắng = Tiền người chơi thua -> Sòng bạc có kỳ vọng dương mu_casino = +100/37 nghìn đồng.",
            "Sau 100.000 ván: Kỳ vọng thắng của sòng bạc là hơn 270 triệu đồng, trong khi độ lệch chuẩn chỉ khoảng 31,6 triệu đồng (Z = -8.55)."
        ],
        "steps": [
            "<b>Bước 1: Mô hình chiếc hộp cho 1 ván cược của người chơi `[+0,35đ]`</b><br>"
            "Chiếc hộp đại diện cho người chơi có 37 tấm thẻ:<br>"
            "- 18 tấm ghi $+100$ (khi bóng vào ô đỏ).<br>"
            "- 19 tấm ghi $-100$ (khi bóng vào ô đen hoặc ô 0).<br>"
            "- Lãi kỳ vọng của người chơi:<br>"
            "$$\\mu_{\\text{người}} = 100 \\times \\frac{18}{37} + (-100) \\times \\frac{19}{37} = -\\frac{100}{37} \\approx -2{,}7027\\text{ (nghìn đồng/ván)}$$"
            "- Độ lệch chuẩn của người chơi:<br>"
            "$$E(X^2) = 100^2 = 10000 \\implies \\sigma^2 = 10000 - (-2{,}7027)^2 \\approx 9992{,}695$$"
            "$$\\sigma_{\\text{người}} = \\sqrt{9992{,}695} \\approx 99{,}9635\\text{ (nghìn đồng)}$$",
            "<b>Bước 2: Phân tích tài chính của sòng bạc sau 100.000 ván `[+0,35đ]`</b><br>"
            "Vì tiền thắng của sòng bạc là tiền thua của người chơi, với mỗi ván cược sòng bạc thu được lãi $Y = -X$:<br>"
            "- Kỳ vọng của sòng bạc mỗi ván: $\\mu_{\\text{sòng bạc}} = +2{,}7027$ nghìn đồng.<br>"
            "- Độ lệch chuẩn mỗi ván: $\\sigma_{\\text{sòng bạc}} = 99{,}9635$ nghìn đồng.<br>"
            "Sau $n = 100.000$ ván cược:<br>"
            "- Tổng tiền lãi kỳ vọng của sòng bạc:<br>"
            "$$E(S_n) = n \\cdot \\mu_{\\text{sòng bạc}} = 100.000 \\times 2{,}7027 = 270.270\\text{ (nghìn đồng)} \\approx 270{,}27\\text{ triệu đồng}$$"
            "- Độ lệch chuẩn của tổng tiền lãi sòng bạc:<br>"
            "$$\\operatorname{SD}(S_n) = \\sqrt{n} \\cdot \\sigma = \\sqrt{100.000} \\times 99{,}9635 = 316{,}2277 \\times 99{,}9635 \\approx 31.611\\text{ (nghìn đồng)} \\approx 31{,}61\\text{ triệu đồng}$$",
            "<b>Bước 3: Ước tính xác suất sòng bạc bị thua lỗ `[+0,30đ]`</b><br>"
            "Theo Định lý Giới hạn Trung tâm, tổng tiền lãi của sòng bạc $S_n$ tuân theo xấp xỉ chuẩn:<br>"
            "$$S_n \\sim N(\\mu_S = 270{,}27;\\; \\sigma_S^2 = 31{,}61^2)$$<br>"
            "Sòng bạc bị thua lỗ khi tổng tiền lãi $S_n < 0$. Chuẩn hóa giá trị 0:<br>"
            "$$Z = \\frac{0 - \\mu_S}{\\sigma_S} = \\frac{0 - 270{,}27}{31{,}61} \\approx -8{,}55$$"
            "Xác suất bị thua lỗ là:<br>"
            "$$P(S_n < 0) = P(Z < -8{,}55) = \\Phi(-8{,}55) \\approx 0\\text{ (nhỏ hơn } 10^{-17}\\text{)}$$"
            "<b>Kết luận:</b> Xác suất sòng bạc thua lỗ trong tuần là một con số bằng $0$ trên thực tế. Sòng bạc được toán học bảo đảm chiến thắng $100\\%$ nhờ Luật số lớn và lợi thế nhà cái (House Edge $2{,}7\\%$)!"
        ],
        "pro_tips": "Nhớ kết luận: Trong cờ bạc, người chơi đặt cược vào vận may ngắn hạn ($n=1$), còn nhà cái đặt cược vào Luật số lớn dài hạn ($n \\to \\infty$).",
        "pitfalls": "Quên đổi dấu khi chuyển từ bài toán 'người chơi' sang 'sòng bạc'."
    })

    return exercises

if __name__ == "__main__":
    t5 = get_topic_5()
    print(f"Generated Topic 5: {len(t5)} exercises.")
