# Topic 3: Biến rời rạc, pmf, cdf, Kỳ vọng & Phương sai (TL3_1 -> TL3_8)
import sys

def get_topic_3():
    exercises = []

    exercises.append({
        "id": "TL3_1", "topicId": 3, "level": "Cơ bản",
        "title": "Tìm hằng số chuẩn hóa, tính kỳ vọng và phương sai từ pmf",
        "problem": "Biến ngẫu nhiên rời rạc $X$ nhận các giá trị trong tập $\\{1, 2, 3, 4\\}$ với hàm khối xác suất có dạng:<br>"
                   "$$p_X(x) = c \\cdot (5 - x)$$"
                   "1. Xác định giá trị của hằng số $c$ và lập bảng phân phối xác suất của $X$.<br>"
                   "2. Tính kỳ vọng $E(X)$.<br>"
                   "3. Tính phương sai $\\operatorname{Var}(X)$ và độ lệch chuẩn $\\operatorname{SD}(X)$ bằng công thức rút gọn.",
        "analysis": "Dùng điều kiện tổng xác suất sum p(x) = 1 để tìm c. Sau đó tính E(X) = sum x*p(x), E(X^2) = sum x^2*p(x), Var = E(X^2) - [E(X)]^2.",
        "hints": [
            "Tính tổng: c*(4 + 3 + 2 + 1) = 10c = 1 => c = 0.1.",
            "Xác suất tương ứng: p(1)=0.4, p(2)=0.3, p(3)=0.2, p(4)=0.1.",
            "E(X) = 1(0.4) + 2(0.3) + 3(0.2) + 4(0.1) = 2.0. E(X^2) = 1(0.4) + 4(0.3) + 9(0.2) + 16(0.1) = 5.0."
        ],
        "steps": [
            "<b>Bước 1: Tìm hằng số c và lập bảng pmf `[+0,35đ]`</b><br>"
            "Theo điều kiện chuẩn hóa của pmf: $\\sum_{x=1}^4 p_X(x) = 1$:<br>"
            "$$c(5 - 1) + c(5 - 2) + c(5 - 3) + c(5 - 4) = 1 \\implies c(4 + 3 + 2 + 1) = 10c = 1 \\implies c = 0{,}10$$<br>"
            "Bảng phân phối xác suất của $X$:<br>"
            "<table class='data-table'><tr><th>x</th><td>1</td><td>2</td><td>3</td><td>4</td><td>Tổng</td></tr>"
            "<tr><th>p(x)</th><td>0,40</td><td>0,30</td><td>0,20</td><td>0,10</td><td>1,00</td></tr></table>",
            "<b>Bước 2: Tính kỳ vọng E(X) `[+0,30đ]`</b><br>"
            "$$E(X) = \\sum x \\cdot p(x) = 1(0{,}40) + 2(0{,}30) + 3(0{,}20) + 4(0{,}10) = 0{,}4 + 0{,}6 + 0{,}6 + 0{,}4 = 2{,}00$$",
            "<b>Bước 3: Tính phương sai và độ lệch chuẩn `[+0,35đ]`</b><br>"
            "- Tính mômen bậc hai: $E(X^2) = 1^2(0{,}40) + 2^2(0{,}30) + 3^2(0{,}20) + 4^2(0{,}10) = 0{,}4 + 1{,}2 + 1{,}8 + 1{,}6 = 5{,}00$.<br>"
            "- Phương sai: $\\operatorname{Var}(X) = E(X^2) - [E(X)]^2 = 5{,}00 - 2{,}00^2 = 5{,}00 - 4{,}00 = 1{,}00$.<br>"
            "- Độ lệch chuẩn: $\\operatorname{SD}(X) = \\sqrt{\\operatorname{Var}(X)} = \\sqrt{1{,}00} = 1{,}00$."
        ],
        "pro_tips": "Luôn có dòng 'Tổng = 1,00' trong bảng pmf để lấy trọn điểm chuẩn hóa.",
        "pitfalls": "Quên bình phương E(X) khi lấy hiệu (tính 5.0 - 2.0 = 3.0 là sai)."
    })

    exercises.append({
        "id": "TL3_2", "topicId": 3, "level": "Cơ bản",
        "title": "Bài tập USB Slide 79–81: Tính phương sai bằng cả hai cách",
        "problem": "Dung lượng một chiếc USB khách hàng mua là biến ngẫu nhiên rời rạc $X$ (GB) có bảng phân phối sau:<br>"
                   "<table class='data-table'><tr><th>x (GB)</th><td>1</td><td>2</td><td>4</td><td>8</td><td>16</td></tr>"
                   "<tr><th>p(x)</th><td>0,05</td><td>0,10</td><td>0,35</td><td>0,40</td><td>0,10</td></tr></table>"
                   "1. Tính $E(X)$ và $E(X^2)$.<br>"
                   "2. Tính phương sai $\\operatorname{Var}(X)$ trực tiếp theo định nghĩa $\\sum (x - \\mu)^2 p(x)$.<br>"
                   "3. Kiểm tra lại bằng công thức rút gọn $\\operatorname{Var}(X) = E(X^2) - [E(X)]^2$ và tính $\\operatorname{SD}(X)$ kèm đơn vị.",
        "analysis": "Bài tập nguyên văn trong slide bài giảng UET Week 07 (tr. 79-81). Yêu cầu đối chiếu 2 cách tính và ghi đúng đơn vị GB, GB^2.",
        "hints": [
            "E(X) = 1(0.05) + 2(0.10) + 4(0.35) + 8(0.40) + 16(0.10) = 6.45 GB.",
            "E(X^2) = 1(0.05) + 4(0.10) + 16(0.35) + 64(0.40) + 256(0.10) = 57.25 GB^2.",
            "Var = 57.25 - 6.45^2 = 15.6475 GB^2. SD = sqrt(15.6475) approx 3.9557 GB."
        ],
        "steps": [
            "<b>Bước 1: Tính E(X) và E(X²) `[+0,30đ]`</b><br>"
            "$$E(X) = 1(0{,}05) + 2(0{,}10) + 4(0{,}35) + 8(0{,}40) + 16(0{,}10) = 0{,}05 + 0{,}20 + 1{,}40 + 3{,}20 + 1{,}60 = 6{,}45\\text{ GB}$$<br>"
            "$$E(X^2) = 1(0{,}05) + 4(0{,}10) + 16(0{,}35) + 64(0{,}40) + 256(0{,}10) = 0{,}05 + 0{,}40 + 5{,}60 + 25{,}60 + 25{,}60 = 57{,}25\\text{ GB}^2$$",
            "<b>Bước 2: Tính Var(X) từ định nghĩa với μ = 6,45 `[+0,35đ]`</b><br>"
            "$$\\operatorname{Var}(X) = \\sum (x - 6{,}45)^2 p(x)$$<br>"
            "- $(1 - 6{,}45)^2 \\times 0{,}05 = 29{,}7025 \\times 0{,}05 = 1{,}485125$<br>"
            "- $(2 - 6{,}45)^2 \\times 0{,}10 = 19{,}8025 \\times 0{,}10 = 1{,}980250$<br>"
            "- $(4 - 6{,}45)^2 \\times 0{,}35 = 6{,}0025 \\times 0{,}35 = 2{,}100875$<br>"
            "- $(8 - 6{,}45)^2 \\times 0{,}40 = 2{,}4025 \\times 0{,}40 = 0{,}961000$<br>"
            "- $(16 - 6{,}45)^2 \\times 0{,}10 = 91{,}2025 \\times 0{,}10 = 9{,}120250$<br>"
            "Cộng lại: $\\operatorname{Var}(X) = 15{,}6475\\text{ GB}^2$.",
            "<b>Bước 3: Kiểm tra bằng công thức rút gọn và tính SD `[+0,35đ]`</b><br>"
            "$$\\operatorname{Var}(X) = 57{,}25 - (6{,}45)^2 = 57{,}25 - 41{,}6025 = 15{,}6475\\text{ GB}^2$$ (trùng khớp hoàn toàn).<br>"
            "Độ lệch chuẩn: $\\operatorname{SD}(X) = \\sqrt{15{,}6475} \\approx 3{,}9557\\text{ GB}$."
        ],
        "pro_tips": "Slide 81 ghi rất rõ: đơn vị của phương sai là GB^2, đơn vị độ lệch chuẩn là GB. Không được thiếu đơn vị!",
        "pitfalls": "Quên ghi mũ 2 ở đơn vị của phương sai (ghi GB thay vì GB^2) sẽ bị trừ 0,25đ."
    })

    exercises.append({
        "id": "TL3_3", "topicId": 3, "level": "Cơ bản",
        "title": "Thiết lập hàm cdf F(x) bậc thang và tính xác suất trên khoảng",
        "problem": "Cho bảng phân phối xác suất của $X$ như sau:<br>"
                   "<table class='data-table'><tr><th>x</th><td>0</td><td>1</td><td>3</td><td>5</td></tr>"
                   "<tr><th>p(x)</th><td>0,2</td><td>0,3</td><td>0,4</td><td>0,1</td></tr></table>"
                   "1. Viết công thức tường minh của hàm phân phối tích lũy $F_X(x)$ trên toàn bộ trục số thực $\\mathbb{R}$.<br>"
                   "2. Tính xác suất $P(1 &lt; X \\le 4)$ bằng hai cách: (a) Dùng bảng pmf; (b) Dùng hàm tích lũy $F(x)$.",
        "analysis": "Hàm cdf F(x) = P(X <= x) cộng dồn từng bậc nhảy. Tính xác suất khoảng P(a < X <= b) = F(b) - F(a).",
        "hints": [
            "F(x) chia làm 5 khoảng: x < 0; 0 <= x < 1; 1 <= x < 3; 3 <= x < 5; x >= 5.",
            "Giá trị tích lũy: 0, 0.2, 0.5, 0.9, 1.0.",
            "P(1 < X <= 4) = P(X = 3) = 0.4. Hoặc F(4) - F(1) = 0.9 - 0.5 = 0.4."
        ],
        "steps": [
            "<b>Bước 1: Viết công thức hàm cdf bậc thang F(x) `[+0,50đ]`</b><br>"
            "Cộng dồn xác suất $F(x) = P(X \\le x)$:<br>"
            "$$F_X(x) = \\begin{cases}"
            "0, &amp; x &lt; 0 \\\\"
            "0{,}2, &amp; 0 \\le x &lt; 1 \\\\"
            "0{,}5, &amp; 1 \\le x &lt; 3 \\\\"
            "0{,}9, &amp; 3 \\le x &lt; 5 \\\\"
            "1{,}0, &amp; x \\ge 5"
            "\\end{cases}$$",
            "<b>Bước 2: Tính P(1 < X ≤ 4) bằng hai cách `[+0,50đ]`</b><br>"
            "- <i>Cách a (dùng pmf):</i> Trong khoảng $(1, 4]$, biến ngẫu nhiên chỉ nhận giá trị $x = 3$.<br>"
            "$$P(1 &lt; X \\le 4) = P(X = 3) = 0{,}40$$<br>"
            "- <i>Cách b (dùng cdf):</i> Áp dụng công thức $P(a &lt; X \\le b) = F(b) - F(a)$ với $a = 1, b = 4$:<br>"
            "$$P(1 &lt; X \\le 4) = F(4) - F(1) = 0{,}90 - 0{,}50 = 0{,}40$$<br>"
            "Hai cách cho kết quả hoàn toàn trùng khớp."
        ],
        "pro_tips": "Lưu ý dấu ngoặc trong F(x): 'dưới lấy dấu bằng, trên không lấy dấu bằng' (hàm liên tục phải).",
        "pitfalls": "Tính nhầm F(4) = 0,5 vì không để ý 4 nằm trong khoảng [3, 5)."
    })

    exercises.append({
        "id": "TL3_4", "topicId": 3, "level": "Trung bình",
        "title": "Biến đổi tuyến tính của kỳ vọng, phương sai và độ lệch chuẩn",
        "problem": "Cho biến ngẫu nhiên $X$ có kỳ vọng $E(X) = 5$ và phương sai $\\operatorname{Var}(X) = 4$. Đặt $Y = 2X - 3$. Hãy tính:<br>"
                   "1. Kỳ vọng $E(Y)$.<br>"
                   "2. Phương sai $\\operatorname{Var}(Y)$ và độ lệch chuẩn $\\operatorname{SD}(Y)$.<br>"
                   "3. Mômen bậc hai $E(X^2)$ và $E(Y^2)$.",
        "analysis": "Áp dụng E(aX+b) = aE(X)+b; Var(aX+b) = a^2*Var(X); SD(aX+b) = |a|*SD(X). Mômen bậc hai tính từ E(X^2) = Var(X) + [E(X)]^2.",
        "hints": [
            "E(2X - 3) = 2*5 - 3 = 7.",
            "Var(2X - 3) = 2^2 * Var(X) = 4 * 4 = 16. SD = sqrt(16) = 4.",
            "E(X^2) = Var(X) + [E(X)]^2 = 4 + 25 = 29."
        ],
        "steps": [
            "<b>Bước 1: Tính E(Y) `[+0,30đ]`</b><br>"
            "Áp dụng tính chất tuyến tính của kỳ vọng:<br>"
            "$$E(Y) = E(2X - 3) = 2 \\cdot E(X) - 3 = 2(5) - 3 = 10 - 3 = 7{,}0$$",
            "<b>Bước 2: Tính Var(Y) và SD(Y) `[+0,40đ]`</b><br>"
            "Áp dụng tính chất biến đổi tuyến tính của phương sai (hằng số $-3$ bị triệt tiêu):<br>"
            "$$\\operatorname{Var}(Y) = \\operatorname{Var}(2X - 3) = 2^2 \\cdot \\operatorname{Var}(X) = 4 \\times 4 = 16{,}0$$<br>"
            "Độ lệch chuẩn:<br>"
            "$$\\operatorname{SD}(Y) = \\sqrt{\\operatorname{Var}(Y)} = \\sqrt{16} = 4{,}0$$<br>"
            "(Hoặc dùng $\\operatorname{SD}(2X - 3) = |2| \\cdot \\operatorname{SD}(X) = 2 \\times 2 = 4{,}0$).",
            "<b>Bước 3: Tính các mômen bậc hai `[+0,30đ]`</b><br>"
            "- $E(X^2) = \\operatorname{Var}(X) + [E(X)]^2 = 4 + 5^2 = 4 + 25 = 29{,}0$.<br>"
            "- $E(Y^2) = \\operatorname{Var}(Y) + [E(Y)]^2 = 16 + 7^2 = 16 + 49 = 65{,}0$."
        ],
        "pro_tips": "Nhớ công thức chuyển vế: E(X^2) = Var(X) + [E(X)]^2 xuất phát từ Var = E(X^2) - [E(X)]^2.",
        "pitfalls": "Trừ 3 vào phương sai: Var = 4*4 - 3 = 13 (SAI HOÀN TOÀN)."
    })

    exercises.append({
        "id": "TL3_5", "topicId": 3, "level": "Trung bình",
        "title": "Mô hình chi phí kiểm định chất lượng (Slide Week 07 tr. 8–9, 15)",
        "problem": "Một cơ sở kiểm tra hai sản phẩm độc lập. Mỗi sản phẩm đạt chuẩn với xác suất $0{,}8$. Gọi $X$ là số sản phẩm đạt chuẩn ($X \\in \\{0, 1, 2\\}$). Chi phí xử lý lô hàng tính bằng nghìn đồng là $C = 50 + 20X$.<br>"
                   "1. Lập bảng phân phối xác suất của $X$.<br>"
                   "2. Tính chi phí kỳ vọng $E(C)$.<br>"
                   "3. Tính phương sai $\\operatorname{Var}(C)$ và độ lệch chuẩn $\\operatorname{SD}(C)$ kèm đơn vị.",
        "analysis": "X tuân theo phân phối nhị thức B(2, 0.8). Lập pmf, tính E(X) = 1.6, Var(X) = 0.32, sau đó dùng biến đổi tuyến tính tính cho C.",
        "hints": [
            "P(X=0) = 0.2^2 = 0.04; P(X=1) = 2*0.8*0.2 = 0.32; P(X=2) = 0.8^2 = 0.64.",
            "E(X) = 1.6 sản phẩm. E(C) = 50 + 20*1.6 = 82 nghìn đồng.",
            "Var(X) = 2*0.8*0.2 = 0.32. Var(C) = 20^2 * 0.32 = 400 * 0.32 = 128 (nghìn đồng)^2."
        ],
        "steps": [
            "<b>Bước 1: Lập bảng phân phối xác suất của X `[+0,35đ]`</b><br>"
            "Vì kiểm tra 2 sản phẩm độc lập cùng xác suất đạt chuẩn $0{,}8$:<br>"
            "- $P(X = 0) = (1 - 0{,}8)^2 = 0{,}04$.<br>"
            "- $P(X = 1) = C_2^1 (0{,}8)^1 (0{,}2)^1 = 0{,}32$.<br>"
            "- $P(X = 2) = (0{,}8)^2 = 0{,}64$.<br>"
            "<table class='data-table'><tr><th>x</th><td>0</td><td>1</td><td>2</td><td>Tổng</td></tr>"
            "<tr><th>p(x)</th><td>0,04</td><td>0,32</td><td>0,64</td><td>1,00</td></tr></table>",
            "<b>Bước 2: Tính chi phí kỳ vọng E(C) `[+0,30đ]`</b><br>"
            "$E(X) = n \\cdot p = 2 \\times 0{,}8 = 1{,}6$ (sản phẩm đạt chuẩn).<br>"
            "$$E(C) = E(50 + 20X) = 50 + 20 \\cdot E(X) = 50 + 20(1{,}6) = 50 + 32 = 82{,}0\\text{ (nghìn đồng)}$$",
            "<b>Bước 3: Tính Var(C) và SD(C) `[+0,35đ]`</b><br>"
            "Phương sai của $X$: $\\operatorname{Var}(X) = n p (1 - p) = 2(0{,}8)(0{,}2) = 0{,}32$ (sản phẩm$^2$).<br>"
            "Phương sai chi phí:<br>"
            "$$\\operatorname{Var}(C) = \\operatorname{Var}(50 + 20X) = 20^2 \\cdot \\operatorname{Var}(X) = 400 \\times 0{,}32 = 128{,}0\\text{ (nghìn đồng)}^2$$<br>"
            "Độ lệch chuẩn chi phí:<br>"
            "$$\\operatorname{SD}(C) = \\sqrt{128} = 8\\sqrt{2} \\approx 11{,}3137\\text{ (nghìn đồng)}$$"
        ],
        "pro_tips": "Ghi đúng đơn vị: (nghìn đồng)^2 cho phương sai và nghìn đồng cho độ lệch chuẩn.",
        "pitfalls": "Quên nhân 2 trong số trường hợp X = 1 (chỉ tính 0.8 * 0.2 = 0.16)."
    })

    exercises.append({
        "id": "TL3_6", "topicId": 3, "level": "Trung bình",
        "title": "Kỳ vọng và Phương sai của hàm hai biến độc lập",
        "problem": "Cho hai biến ngẫu nhiên độc lập $X$ và $Y$ có các thông số: $E(X) = 3$, $\\operatorname{Var}(X) = 2$; $E(Y) = 4$, $\\operatorname{Var}(Y) = 5$. Hãy tính:<br>"
                   "1. Kỳ vọng tích $E(X Y)$.<br>"
                   "2. Kỳ vọng tổ hợp $E(2X - 3Y + 5)$.<br>"
                   "3. Phương sai $\\operatorname{Var}(X - 3Y)$ và $\\operatorname{Var}(2X + 4Y)$.",
        "analysis": "Vì X, Y độc lập nên E(XY) = E(X)*E(Y). Tuyến tính E(aX+bY) = aE(X)+bE(Y). Độc lập nên Var(aX+bY) = a^2*Var(X) + b^2*Var(Y) (lưu ý dấu trừ cũng thành bình phương dấu cộng!).",
        "hints": [
            "E(XY) = 3 * 4 = 12.",
            "E(2X - 3Y + 5) = 2(3) - 3(4) + 5 = 6 - 12 + 5 = -1.",
            "Var(X - 3Y) = 1^2 * Var(X) + (-3)^2 * Var(Y) = 1(2) + 9(5) = 2 + 45 = 47."
        ],
        "steps": [
            "<b>Bước 1: Tính E(XY) `[+0,30đ]`</b><br>"
            "Vì $X$ và $Y$ độc lập:<br>"
            "$$E(XY) = E(X) \\cdot E(Y) = 3 \\times 4 = 12{,}0$$",
            "<b>Bước 2: Tính E(2X - 3Y + 5) `[+0,30đ]`</b><br>"
            "$$E(2X - 3Y + 5) = 2 \\cdot E(X) - 3 \\cdot E(Y) + 5 = 2(3) - 3(4) + 5 = 6 - 12 + 5 = -1{,}0$$",
            "<b>Bước 3: Tính các phương sai `[+0,40đ]`</b><br>"
            "- $\\operatorname{Var}(X - 3Y)$: Vì $X, Y$ độc lập:<br>"
            "$$\\operatorname{Var}(X - 3Y) = 1^2 \\cdot \\operatorname{Var}(X) + (-3)^2 \\cdot \\operatorname{Var}(Y) = 1(2) + 9(5) = 2 + 45 = 47{,}0$$<br>"
            "- $\\operatorname{Var}(2X + 4Y)$:<br>"
            "$$\\operatorname{Var}(2X + 4Y) = 2^2 \\cdot \\operatorname{Var}(X) + 4^2 \\cdot \\operatorname{Var}(Y) = 4(2) + 16(5) = 8 + 80 = 88{,}0$$"
        ],
        "pro_tips": "LƯU Ý CỰC KỲ QUAN TRỌNG: Phương sai của HIỆU Var(X - Y) vẫn là DẤU CỘNG: Var(X) + Var(Y), không bao giờ lấy trừ!",
        "pitfalls": "Lấy Var(X - 3Y) = Var(X) - 9*Var(Y) = 2 - 45 = -43 (phương sai không bao giờ được âm!)."
    })

    exercises.append({
        "id": "TL3_7", "topicId": 3, "level": "Nâng cao",
        "title": "Khôi phục bảng pmf từ hàm phân phối tích lũy cdf",
        "problem": "Cho hàm phân phối tích lũy của biến ngẫu nhiên $X$:<br>"
                   "$$F_X(x) = \\begin{cases}"
                   "0, &amp; x &lt; -1 \\\\"
                   "0{,}15, &amp; -1 \\le x &lt; 0 \\\\"
                   "0{,}45, &amp; 0 \\le x &lt; 2 \\\\"
                   "0{,}80, &amp; 2 \\le x &lt; 3 \\\\"
                   "1{,}00, &amp; x \\ge 3"
                   "\\end{cases}$$"
                   "1. Xác định tập các giá trị mà $X$ có thể nhận và tính xác suất tại từng giá trị.<br>"
                   "2. Tính kỳ vọng $E(X)$ và phương sai $\\operatorname{Var}(X)$.<br>"
                   "3. Tính xác suất $P(-0{,}5 \\le X &lt; 3)$.",
        "analysis": "Mỗi bước nhảy của F(x) tại điểm x_0 tương ứng với một giá trị có xác suất dương p(x_0) = F(x_0) - lim_{x->x_0^-} F(x). Sau đó tính kỳ vọng và xác suất khoảng nửa đóng nửa mở.",
        "hints": [
            "Các điểm nhảy: x = -1, 0, 2, 3.",
            "p(-1) = 0.15 - 0 = 0.15; p(0) = 0.45 - 0.15 = 0.30; p(2) = 0.80 - 0.45 = 0.35; p(3) = 1.0 - 0.80 = 0.20.",
            "Xác suất P(-0.5 <= X < 3) gồm các giá trị x = 0 và x = 2: p(0) + p(2) = 0.30 + 0.35 = 0.65."
        ],
        "steps": [
            "<b>Bước 1: Khôi phục bảng phân phối xác suất pmf `[+0,40đ]`</b><br>"
            "Độ cao các bước nhảy của $F(x)$ tại các điểm gián đoạn:<br>"
            "- Tại $x = -1$: $P(X = -1) = 0{,}15 - 0 = 0{,}15$.<br>"
            "- Tại $x = 0$: $P(X = 0) = 0{,}45 - 0{,}15 = 0{,}30$.<br>"
            "- Tại $x = 2$: $P(X = 2) = 0{,}80 - 0{,}45 = 0{,}35$.<br>"
            "- Tại $x = 3$: $P(X = 3) = 1{,}00 - 0{,}80 = 0{,}20$.<br>"
            "<table class='data-table'><tr><th>x</th><td>-1</td><td>0</td><td>2</td><td>3</td><td>Tổng</td></tr>"
            "<tr><th>p(x)</th><td>0,15</td><td>0,30</td><td>0,35</td><td>0,20</td><td>1,00</td></tr></table>",
            "<b>Bước 2: Tính E(X) và Var(X) `[+0,35đ]`</b><br>"
            "- $E(X) = -1(0{,}15) + 0(0{,}30) + 2(0{,}35) + 3(0{,}20) = -0{,}15 + 0 + 0{,}70 + 0{,}60 = 1{,}15$.<br>"
            "- $E(X^2) = (-1)^2(0{,}15) + 0^2(0{,}30) + 2^2(0{,}35) + 3^2(0{,}20) = 0{,}15 + 0 + 1{,}40 + 1{,}80 = 3{,}35$.<br>"
            "- $\\operatorname{Var}(X) = E(X^2) - [E(X)]^2 = 3{,}35 - (1{,}15)^2 = 3{,}35 - 1{,}3225 = 2{,}0275$.",
            "<b>Bước 3: Tính P(-0,5 ≤ X < 3) `[+0,25đ]`</b><br>"
            "Trong khoảng $[-0{,}5; 3)$, các giá trị $X$ thỏa mãn là $x = 0$ và $x = 2$ (không lấy $x = 3$ vì dấu &lt; 3):<br>"
            "$$P(-0{,}5 \\le X &lt; 3) = P(X = 0) + P(X = 2) = 0{,}30 + 0{,}35 = 0{,}65\\text{ (65\\%)}$$"
        ],
        "pro_tips": "Kiểm tra tổng các bước nhảy: 0,15 + 0,30 + 0,35 + 0,20 = 1,00.",
        "pitfalls": "Đếm nhầm x = 3 vào câu 3 dẫn đến kết quả 0,85 thay vì 0,65."
    })

    exercises.append({
        "id": "TL3_8", "topicId": 3, "level": "Nâng cao",
        "title": "Bài toán người bán báo: Tối ưu hóa lợi nhuận kỳ vọng",
        "problem": "Một người bán báo mua mỗi tờ báo giá 3 nghìn đồng và bán ra giá 8 nghìn đồng (lãi 5 nghìn đồng/tờ nếu bán được). Những tờ báo không bán được trong ngày phải bỏ đi (mất trắng 3 nghìn đồng/tờ). Số lượng báo khách hàng hỏi mua mỗi ngày là biến ngẫu nhiên $D$ có phân phối:<br>"
                   "<table class='data-table'><tr><th>Nhu cầu d (tờ)</th><td>10</td><td>11</td><td>12</td><td>13</td></tr>"
                   "<tr><th>P(D = d)</th><td>0,1</td><td>0,3</td><td>0,4</td><td>0,2</td></tr></table>"
                   "Nếu người bán báo quyết định nhập về $12$ tờ mỗi ngày, hãy lập bảng phân phối xác suất của lợi nhuận $Y$ và tính lợi nhuận kỳ vọng $E(Y)$.",
        "analysis": "Gọi q = 12 là số báo nhập. Chi phí cố định = 12 * 3 = 36 nghìn. Doanh thu = 8 * min(d, 12). Lợi nhuận Y = 8*min(d, 12) - 36.",
        "hints": [
            "Nếu d = 10: bán được 10 tờ -> Doanh thu = 80 -> Lợi nhuận = 80 - 36 = 44 nghìn.",
            "Nếu d = 11: bán được 11 tờ -> Doanh thu = 88 -> Lợi nhuận = 88 - 36 = 52 nghìn.",
            "Nếu d = 12 hoặc d = 13: đều bán hết 12 tờ -> Doanh thu = 96 -> Lợi nhuận = 96 - 36 = 60 nghìn."
        ],
        "steps": [
            "<b>Bước 1: Thiết lập công thức lợi nhuận Y `[+0,30đ]`</b><br>"
            "Người bán nhập $q = 12$ tờ báo. Tổng chi phí bỏ ra: $12 \\times 3 = 36$ nghìn đồng.<br>"
            "Số báo bán được thực tế là $\\min(D, 12)$. Lợi nhuận:<br>"
            "$$Y = 8 \\cdot \\min(D, 12) - 36\\text{ (nghìn đồng)}$$",
            "<b>Bước 2: Tính giá trị lợi nhuận theo từng mức nhu cầu `[+0,35đ]`</b><br>"
            "- Khi $D = 10$ (xác suất 0,1): $Y = 8(10) - 36 = 80 - 36 = 44$ nghìn đồng.<br>"
            "- Khi $D = 11$ (xác suất 0,3): $Y = 8(11) - 36 = 88 - 36 = 52$ nghìn đồng.<br>"
            "- Khi $D = 12$ (xác suất 0,4): $Y = 8(12) - 36 = 96 - 36 = 60$ nghìn đồng.<br>"
            "- Khi $D = 13$ (xác suất 0,2): Nhu cầu là 13 nhưng chỉ có 12 tờ để bán $\\implies Y = 8(12) - 36 = 60$ nghìn đồng.",
            "<b>Bước 3: Lập bảng pmf của lợi nhuận và tính kỳ vọng E(Y) `[+0,35đ]`</b><br>"
            "Gộp hai trường hợp cùng cho mức lợi nhuận 60 nghìn: $P(Y = 60) = 0{,}4 + 0{,}2 = 0{,}6$.<br>"
            "<table class='data-table'><tr><th>Lợi nhuận y (nghìn)</th><td>44</td><td>52</td><td>60</td><td>Tổng</td></tr>"
            "<tr><th>P(Y = y)</th><td>0,10</td><td>0,30</td><td>0,60</td><td>1,00</td></tr></table><br>"
            "Lợi nhuận kỳ vọng mỗi ngày:<br>"
            "$$E(Y) = 44(0{,}10) + 52(0{,}30) + 60(0{,}60) = 4{,}4 + 15{,}6 + 36{,}0 = 56{,}0\\text{ (nghìn đồng)}$$"
        ],
        "pro_tips": "Điểm mấu chốt của bài toán này là gộp xác suất tại mức lợi nhuận tối đa khi nhu cầu vượt quá số lượng hàng nhập.",
        "pitfalls": "Quên tính chi phí của những tờ báo bị ế bỏ đi."
    })

    return exercises

if __name__ == "__main__":
    t3 = get_topic_3()
    print(f"Generated Topic 3: {len(t3)} exercises.")
