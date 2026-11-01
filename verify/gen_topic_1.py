# Topic 1: Thống kê mô tả, Bảng liên hợp & Hồi quy tuyến tính (TL1_1 -> TL1_8)
import sys

def get_topic_1():
    exercises = []

    # TL1_1 (Cơ bản)
    exercises.append({
        "id": "TL1_1", "topicId": 1, "level": "Cơ bản",
        "title": "Tóm tắt dữ liệu số: Trung bình, Trung vị, Tứ phân vị và Điểm ngoại lai (Outlier)",
        "problem": "Khảo sát thời gian tự học mỗi tuần (đơn vị: giờ) của một nhóm gồm 10 sinh viên, thu được mẫu số liệu sau:<br>"
                   "$$\\{3,\\; 5,\\; 6,\\; 7,\\; 7,\\; 8,\\; 8,\\; 9,\\; 10,\\; 16\\}$$"
                   "1. Tính số trung bình (Mean) và trung vị (Median) của mẫu số liệu.<br>"
                   "2. Xác định các tứ phân vị $Q_1$, $Q_2$, $Q_3$ và khoảng tứ phân vị (IQR).<br>"
                   "3. Dùng tiêu chuẩn hàng rào $1{,}5 \\times \\text{IQR}$ để kiểm tra xem mẫu có điểm ngoại lai (outlier) hay không.",
        "analysis": "Dữ liệu đã được sắp xếp tăng dần ($n=10$). Áp dụng các định nghĩa về trung bình, trung vị, chia nửa tìm Q1, Q3, tính IQR = Q3 - Q1 và xác định hàng rào ngoài [Q1 - 1.5*IQR, Q3 + 1.5*IQR].",
        "hints": [
            "Số trung bình là tổng chia cho n. Trung vị là trung bình cộng của phần tử thứ 5 và thứ 6.",
            "Nửa dưới gồm 5 số đầu {3, 5, 6, 7, 7} -> Q1 là trung vị nửa dưới. Nửa trên gồm {8, 8, 9, 10, 16} -> Q3.",
            "IQR = Q3 - Q1. Hàng rào trên: Q3 + 1,5 * IQR. Hàng rào dưới: Q1 - 1,5 * IQR."
        ],
        "steps": [
            "<b>Bước 1: Tính số trung bình (Mean) `[+0,25đ]`</b><br>"
            "Tổng các giá trị: $\\sum x_i = 3 + 5 + 6 + 7 + 7 + 8 + 8 + 9 + 10 + 16 = 79$.<br>"
            "Số quan sát $n = 10$.<br>"
            "$$\\bar{x} = \\frac{\\sum x_i}{n} = \\frac{79}{10} = 7{,}9\\text{ (giờ)}$$",
            "<b>Bước 2: Xác định trung vị và các tứ phân vị `[+0,35đ]`</b><br>"
            "- Vì $n = 10$ chẵn, trung vị $Q_2$ (Median) là trung bình cộng của 2 giá trị chính giữa (vị trí 5 và 6):<br>"
            "$$Q_2 = \\frac{x_{(5)} + x_{(6)}}{2} = \\frac{7 + 8}{2} = 7{,}5\\text{ (giờ)}$$"
            "- Nửa dưới dữ liệu gồm 5 giá trị: $\\{3, 5, 6, 7, 7\\}$. Tứ phân vị thứ nhất là giá trị ở chính giữa nửa dưới:<br>"
            "$$Q_1 = 6\\text{ (giờ)}$$"
            "- Nửa trên dữ liệu gồm 5 giá trị: $\\{8, 8, 9, 10, 16\\}$. Tứ phân vị thứ ba là giá trị ở chính giữa nửa trên:<br>"
            "$$Q_3 = 9\\text{ (giờ)}$$"
            "- Khoảng tứ phân vị (Interquartile Range):<br>"
            "$$\\text{IQR} = Q_3 - Q_1 = 9 - 6 = 3\\text{ (giờ)}$$",
            "<b>Bước 3: Xác định hàng rào và tìm điểm ngoại lai `[+0,40đ]`</b><br>"
            "- Hàng rào dưới (Lower Fence):<br>"
            "$$\\text{LF} = Q_1 - 1{,}5 \\times \\text{IQR} = 6 - 1{,}5 \\times 3 = 6 - 4{,}5 = 1{,}5$$"
            "- Hàng rào trên (Upper Fence):<br>"
            "$$\\text{UF} = Q_3 + 1{,}5 \\times \\text{IQR} = 9 + 1{,}5 \\times 3 = 9 + 4{,}5 = 13{,}5$$"
            "So sánh các giá trị trong mẫu với khoảng $[1{,}5;\\; 13{,}5]$:<br>"
            "Giá trị $x = 16 > 13{,}5$ nằm ngoài hàng rào trên.<br>"
            "<b>Kết luận:</b> Mẫu có duy nhất một điểm ngoại lai là $16$ giờ. Nhận xét: Do có điểm ngoại lai lớn kéo trung bình lên nên $\\bar{x} = 7{,}9 > Q_2 = 7{,}5$ (phân phối lệch phải)."
        ],
        "pro_tips": "Khi dữ liệu có điểm ngoại lai, luôn nhận xét thêm rằng Trung vị và IQR có tính 'bền vững' (robust), ít bị ảnh hưởng hơn Số trung bình.",
        "pitfalls": "Quên sắp xếp dãy số trước khi tìm trung vị hoặc tính sai vị trí nửa trên/nửa dưới."
    })

    # TL1_2 (Cơ bản)
    exercises.append({
        "id": "TL1_2", "topicId": 1, "level": "Cơ bản",
        "title": "Bảng liên hợp (Contingency Table): Tần số, Tần suất biên và Xác suất có điều kiện",
        "problem": "Khảo sát 60 sinh viên về kỹ năng Tiếng Anh và năm học, thu được bảng liên hợp sau:<br>"
                   "<table class='data-table'><tr><th>Năm học \\ Tiếng Anh</th><th>Đạt loại Giỏi</th><th>Chưa Giỏi</th><th>Tổng</th></tr>"
                   "<tr><td>Năm thứ nhất</td><td>12</td><td>28</td><td>40</td></tr>"
                   "<tr><td>Năm thứ hai</td><td>15</td><td>5</td><td>20</td></tr>"
                   "<tr><td>Tổng</td><td>27</td><td>33</td><td>60</td></tr></table>"
                   "1. Chọn ngẫu nhiên 1 sinh viên, tính xác suất sinh viên đó là 'Sinh viên năm 2 VÀ Đạt Giỏi'.<br>"
                   "2. Biết sinh viên được chọn là sinh viên năm 2, tính xác suất sinh viên đó Đạt loại Giỏi.<br>"
                   "3. Biết sinh viên được chọn Đạt loại Giỏi, tính xác suất sinh viên đó là sinh viên năm 2.",
        "analysis": "Đọc bảng liên hợp: ô giao là xác suất đồng thời, tổng hàng/cột là phân phối biên. Xác suất có điều kiện là tỉ lệ của ô giao trên tổng hàng hoặc tổng cột tương ứng.",
        "hints": [
            "Câu 1: Ô giao giữa dòng 'Năm 2' và cột 'Giỏi' chia cho tổng thể N=60.",
            "Câu 2: Không gian mẫu thu hẹp vào dòng 'Năm 2' (tổng 20 sinh viên).",
            "Câu 3: Không gian mẫu thu hẹp vào cột 'Giỏi' (tổng 27 sinh viên)."
        ],
        "steps": [
            "<b>Bước 1: Tính xác suất đồng thời (Câu 1) `[+0,30đ]`</b><br>"
            "Số sinh viên năm 2 và đạt loại Giỏi là 15 sinh viên trên tổng số 60 sinh viên:<br>"
            "$$P(\\text{Năm 2} \\cap \\text{Giỏi}) = \\frac{15}{60} = 0{,}25\\text{ (25\\%)}$$",
            "<b>Bước 2: Tính xác suất có điều kiện theo hàng (Câu 2) `[+0,35đ]`</b><br>"
            "Điều kiện đã biết: Sinh viên học năm thứ hai. Số sinh viên năm hai là 20:<br>"
            "$$P(\\text{Giỏi} \\mid \\text{Năm 2}) = \\frac{P(\\text{Năm 2} \\cap \\text{Giỏi})}{P(\\text{Năm 2})} = \\frac{15/60}{20/60} = \\frac{15}{20} = 0{,}75\\text{ (75\\%)}$$",
            "<b>Bước 3: Tính xác suất có điều kiện theo cột (Câu 3) `[+0,35đ]`</b><br>"
            "Điều kiện đã biết: Sinh viên đạt loại Giỏi. Tổng số sinh viên đạt Giỏi là 27:<br>"
            "$$P(\\text{Năm 2} \\mid \\text{Giỏi}) = \\frac{P(\\text{Năm 2} \\cap \\text{Giỏi})}{P(\\text{Giỏi})} = \\frac{15/60}{27/60} = \\frac{15}{27} = \\frac{5}{9} \\approx 0{,}5556\\text{ (55{,}56\\%)}$$"
        ],
        "pro_tips": "Phân biệt rõ P(A|B) và P(B|A). Cái nằm sau dấu gạch đứng '|' chính là điều kiện đã xảy ra và là mẫu số của phân số.",
        "pitfalls": "Nhầm lẫn mẫu số: dùng tổng 60 thay vì tổng hàng hoặc tổng cột khi tính xác suất có điều kiện."
    })

    # TL1_3 (Cơ bản)
    exercises.append({
        "id": "TL1_3", "topicId": 1, "level": "Cơ bản",
        "title": "Hồi quy tuyến tính đơn: Dự đoán giá trị và Tính phần dư (Residual)",
        "problem": "Một mô hình hồi quy tuyến tính đơn mô tả mối quan hệ giữa số giờ ôn tập ($x$) và điểm thi ($y$) của sinh viên có phương trình:<br>"
                   "$$\\hat{y} = 15 + 2{,}5x$$"
                   "1. Nêu ý nghĩa thực tế của hệ số góc (slope) $b_1 = 2{,}5$ và hệ số chặn (intercept) $b_0 = 15$.<br>"
                   "2. Một sinh viên ôn tập $x = 8$ giờ, hãy tính điểm thi dự đoán $\\hat{y}$ của sinh viên này.<br>"
                   "3. Điểm thi thực tế của sinh viên này ghi nhận được là $y = 38$ điểm. Hãy tính phần dư (residual) $e$ và giải thích ý nghĩa.",
        "analysis": "Hệ số b1 biểu thị mức thay đổi trung bình của y khi x tăng 1 đơn vị. Điểm dự đoán thu được bằng cách thay x=8 vào phương trình. Phần dư e = y - y_hat.",
        "hints": [
            "b1 = 2.5: khi ôn thêm 1 giờ thì điểm thi tăng trung bình bao nhiêu?",
            "Thay x = 8 vào: y_hat = 15 + 2.5 * 8.",
            "Phần dư e = Quan sát thực tế - Dự đoán mô hình (y - y_hat)."
        ],
        "steps": [
            "<b>Bước 1: Giải thích ý nghĩa hệ số hồi quy `[+0,30đ]`</b><br>"
            "- <b>Hệ số chặn $b_0 = 15$:</b> Khi một sinh viên không ôn tập giờ nào ($x = 0$), điểm thi dự đoán trung bình là 15 điểm.<br>"
            "- <b>Hệ số góc $b_1 = 2{,}5$:</b> Cứ mỗi khi sinh viên dành thêm 1 giờ ôn tập, điểm thi dự đoán trung bình sẽ tăng thêm $2{,}5$ điểm.",
            "<b>Bước 2: Tính điểm thi dự đoán khi x = 8 `[+0,30đ]`</b><br>"
            "Thay $x = 8$ vào phương trình đường hồi quy:<br>"
            "$$\\hat{y} = 15 + 2{,}5 \\times 8 = 15 + 20 = 35\\text{ (điểm)}$$",
            "<b>Bước 3: Tính phần dư và nêu ý nghĩa `[+0,40đ]`</b><br>"
            "Công thức tính phần dư (Residual):<br>"
            "$$e = y - \\hat{y} = 38 - 35 = +3\\text{ (điểm)}$$<br>"
            "<b>Ý nghĩa:</b> Phần dư mang dấu dương ($e = +3$) cho thấy sinh viên này đạt kết quả thực tế cao hơn $3$ điểm so với mức mà mô hình hồi quy dự đoán dựa trên số giờ ôn tập của bạn ấy (mô hình đã đánh giá thấp hơn thực tế 3 điểm)."
        ],
        "pro_tips": "Luôn nhớ quy tắc phần dư: $e = y - \\hat{y}$ (Thực tế trừ Mô hình), không bao giờ lấy Mô hình trừ Thực tế.",
        "pitfalls": "Tính ngược dấu $e = \\hat{y} - y = 35 - 38 = -3$ dẫn đến giải thích sai lệch."
    })

    # TL1_4 (Trung bình)
    exercises.append({
        "id": "TL1_4", "topicId": 1, "level": "Trung bình",
        "title": "Ước lượng OLS: Hệ số tương quan Pearson r, Phương trình hồi quy và Tính chất phần dư",
        "problem": "Cho 5 cặp quan sát $(x_i, y_i)$ như sau: $(1, 3);\\; (2, 5);\\; (3, 6);\\; (4, 8);\\; (5, 10)$.<br>"
                   "1. Tính hệ số tương quan tuyến tính mẫu Pearson $r$ và nhận xét mối quan hệ giữa $X$ và $Y$.<br>"
                   "2. Tìm phương trình hồi quy mẫu bình phương nhỏ nhất (OLS) $\\hat{y} = b_0 + b_1 x$.<br>"
                   "3. Lập bảng tính phần dư $e_i$ tại cả 5 điểm và kiểm chứng tính chất $\\sum_{i=1}^5 e_i = 0$.",
        "analysis": "Tính sum x, sum y, sum x^2, sum y^2, sum xy. Dùng công thức OLS: b1 = [n*sum(xy) - sum(x)*sum(y)] / [n*sum(x^2) - (sum x)^2], b0 = y_bar - b1*x_bar. r = Cov(x,y)/(sx * sy).",
        "hints": [
            "Lập bảng tính 5 cột: x, y, x^2, y^2, xy.",
            "x_bar = 15/5 = 3, y_bar = 32/5 = 6.4.",
            "b1 = sum[(x - x_bar)(y - y_bar)] / sum[(x - x_bar)^2] = 17 / 10 = 1.7."
        ],
        "steps": [
            "<b>Bước 1: Lập bảng tính toán các tổng thống kê `[+0,30đ]`</b><br>"
            "<table class='data-table'><tr><th>i</th><th>$x_i$</th><th>$y_i$</th><th>$x_i^2$</th><th>$y_i^2$</th><th>$x_i y_i$</th></tr>"
            "<tr><td>1</td><td>1</td><td>3</td><td>1</td><td>9</td><td>3</td></tr>"
            "<tr><td>2</td><td>2</td><td>5</td><td>4</td><td>25</td><td>10</td></tr>"
            "<tr><td>3</td><td>3</td><td>6</td><td>9</td><td>36</td><td>18</td></tr>"
            "<tr><td>4</td><td>4</td><td>8</td><td>16</td><td>64</td><td>32</td></tr>"
            "<tr><td>5</td><td>5</td><td>10</td><td>25</td><td>100</td><td>50</td></tr>"
            "<tr><th>Tổng</th><th>15</th><th>32</th><th>55</th><th>234</th><th>113</th></tr></table><br>"
            "- $\\bar{x} = \\frac{15}{5} = 3{,}0$; $\\bar{y} = \\frac{32}{5} = 6{,}4$.",
            "<b>Bước 2: Tính hệ số tương quan r `[+0,25đ]`</b><br>"
            "$$r = \\frac{n\\sum x_i y_i - (\\sum x_i)(\\sum y_i)}{\\sqrt{[n\\sum x_i^2 - (\\sum x_i)^2][n\\sum y_i^2 - (\\sum y_i)^2]}} = \\frac{5(113) - 15(32)}{\\sqrt{[5(55) - 15^2][5(234) - 32^2]}}$$"
            "$$r = \\frac{565 - 480}{\\sqrt{(275 - 225)(1170 - 1024)}} = \\frac{85}{\\sqrt{50 \\times 146}} = \\frac{85}{\\sqrt{7300}} = \\frac{85}{85{,}44} \\approx 0{,}9948$$"
            "<b>Nhận xét:</b> $r \\approx 0{,}9948 > 0$ rất sát 1, chứng tỏ có mối quan hệ tương quan tuyến tính thuận chiều cực kỳ mạnh.",
            "<b>Bước 3: Tìm phương trình hồi quy OLS `[+0,25đ]`</b><br>"
            "- Hệ số góc: $b_1 = \\frac{n\\sum x_i y_i - (\\sum x_i)(\\sum y_i)}{n\\sum x_i^2 - (\\sum x_i)^2} = \\frac{85}{50} = 1{,}70$.<br>"
            "- Hệ số chặn: $b_0 = \\bar{y} - b_1 \\bar{x} = 6{,}4 - 1{,}70 \\times 3{,}0 = 6{,}4 - 5{,}1 = 1{,}30$.<br>"
            "Phương trình hồi quy là: $$\\hat{y} = 1{,}30 + 1{,}70x$$",
            "<b>Bước 4: Kiểm chứng tính chất tổng phần dư bằng 0 `[+0,20đ]`</b><br>"
            "- $x=1 \\implies \\hat{y}_1 = 3{,}00 \\implies e_1 = 3 - 3{,}00 = 0{,}00$.<br>"
            "- $x=2 \\implies \\hat{y}_2 = 4{,}70 \\implies e_2 = 5 - 4{,}70 = +0{,}30$.<br>"
            "- $x=3 \\implies \\hat{y}_3 = 6{,}40 \\implies e_3 = 6 - 6{,}40 = -0{,}40$.<br>"
            "- $x=4 \\implies \\hat{y}_4 = 8{,}10 \\implies e_4 = 8 - 8{,}10 = -0{,}10$.<br>"
            "- $x=5 \\implies \\hat{y}_5 = 9{,}80 \\implies e_5 = 10 - 9{,}80 = +0{,}20$.<br>"
            "Tổng các phần dư: $$\\sum_{i=1}^5 e_i = 0{,}00 + 0{,}30 - 0{,}40 - 0{,}10 + 0{,}20 = 0{,}00\\text{ (đúng với lý thuyết OLS)}$$"
        ],
        "pro_tips": "Đường thẳng hồi quy OLS luôn luôn đi qua điểm trọng tâm $(\\bar{x}, \\bar{y})$. Trong bài này, thay $x=3$ vào ra $\\hat{y} = 6{,}4 = \\bar{y}$!",
        "pitfalls": "Lẫn lộn giữa $(\\sum x)^2$ và $\\sum (x^2)$. Trong bài: $(\\sum x)^2 = 15^2 = 225$, còn $\\sum x^2 = 55$."
    })

    # TL1_5 (Trung bình)
    exercises.append({
        "id": "TL1_5", "topicId": 1, "level": "Trung bình",
        "title": "Phân loại biến số, Lập bảng phân phối tần số - tần suất và Nhận diện thang đo",
        "problem": "Một nghiên cứu ghi nhận thông tin của 40 khách hàng gồm: Giới tính, Đánh giá mức độ hài lòng (1 sao đến 5 sao), Số lượng sản phẩm đã mua (món), và Tổng số tiền chi tiêu (nghìn đồng).<br>"
                   "1. Hãy phân loại 4 biến số trên theo phân loại dữ liệu (Định tính danh nghĩa, Định tính thứ bậc, Định lượng rời rạc, Định lượng liên tục).<br>"
                   "2. Thống kê về mức độ hài lòng (thang 1-5 sao) thu được số khách tương ứng: 1 sao: 2 khách, 2 sao: 6 khách, 3 sao: 12 khách, 4 sao: 14 khách, 5 sao: 6 khách. Lập bảng phân phối tần số, tần suất (%) và tần suất tích lũy (%).",
        "analysis": "Định tính danh nghĩa (không có thứ tự), thứ bậc (có thứ tự nhưng khoảng cách không đo lường bằng số), định lượng rời rạc (đếm), liên tục (đo lường trên trục số thực). Tần suất = tần số / N * 100%.",
        "hints": [
            "Giới tính không có thứ tự hơn kém -> Danh nghĩa (Nominal).",
            "Mức độ sao có thứ tự 1 < 2 < 3 < 4 < 5 nhưng phép trừ không có nghĩa đo lường -> Thứ bậc (Ordinal).",
            "Số món đếm được là số nguyên không âm -> Định lượng rời rạc (Discrete).",
            "Tiền bạc đo lường liên tục trên miền giá trị thực -> Định lượng liên tục (Continuous)."
        ],
        "steps": [
            "<b>Bước 1: Phân loại 4 biến số `[+0,40đ]`</b><br>"
            "- <b>Giới tính (Nam/Nữ):</b> Biến định tính danh nghĩa (Nominal categorical variable) vì các nhóm không có thứ bậc ưu tiên.<br>"
            "- <b>Mức độ hài lòng (1-5 sao):</b> Biến định tính thứ bậc (Ordinal categorical variable) vì các mức có trật tự tăng dần nhưng khoảng cách giữa các sao không đồng nhất.<br>"
            "- <b>Số lượng sản phẩm đã mua:</b> Biến định lượng rời rạc (Discrete numerical variable) vì nhận các giá trị đếm nguyên $0, 1, 2, \\dots$<br>"
            "- <b>Tổng số tiền chi tiêu:</b> Biến định lượng liên tục (Continuous numerical variable) vì có thể nhận bất kỳ giá trị thực nào trong một khoảng.",
            "<b>Bước 2: Lập bảng phân phối tần số, tần suất và tích lũy `[+0,60đ]`</b><br>"
            "Tổng số khách hàng $N = 40$.<br>"
            "<table class='data-table'><tr><th>Mức sao</th><th>Tần số ($f_i$)</th><th>Tần suất ($p_i = f_i/N$)</th><th>Tần suất tích lũy ($F_i$)</th></tr>"
            "<tr><td>1 sao</td><td>2</td><td>2/40 = 5%</td><td>5%</td></tr>"
            "<tr><td>2 sao</td><td>6</td><td>6/40 = 15%</td><td>20%</td></tr>"
            "<tr><td>3 sao</td><td>12</td><td>12/40 = 30%</td><td>50%</td></tr>"
            "<tr><td>4 sao</td><td>14</td><td>14/40 = 35%</td><td>85%</td></tr>"
            "<tr><td>5 sao</td><td>6</td><td>6/40 = 15%</td><td>100%</td></tr>"
            "<tr><th>Tổng</th><th>40</th><th>100%</th><th>-</th></tr></table><br>"
            "<b>Nhận xét:</b> Có đến 80% khách hàng hài lòng từ 3 sao trở lên ($30\\% + 35\\% + 15\\% = 80\\%$). Điểm trung vị rơi vào mức 3 sao (tích lũy đạt 50%)."
        ],
        "pro_tips": "Khi làm bảng tần suất, luôn kiểm tra dòng Tổng cộng xem tổng tần số có đúng bằng $N$ và tổng tần suất có đúng bằng $100\\%$ hay không.",
        "pitfalls": "Nhầm lẫn giữa biến định tính thứ bậc (mức sao, trình độ học vấn) và biến định lượng rời rạc."
    })

    # TL1_6 (Trung bình)
    exercises.append({
        "id": "TL1_6", "topicId": 1, "level": "Trung bình",
        "title": "Hình dạng phân phối (Skewness): Lệch phải, Lệch trái, Đối xứng và So sánh Mean vs Median",
        "problem": "Quan sát biểu đồ tần số (Histogram) của ba tập dữ liệu kinh tế - xã hội sau:<br>"
                   "- Tập 1: Thu nhập hàng tháng của người lao động trong một tỉnh.<br>"
                   "- Tập 2: Điểm thi của một bài kiểm tra quá dễ (hầu hết làm điểm tối đa 10, chỉ ít người điểm thấp).<br>"
                   "- Tập 3: Chiều cao của 1000 nam thanh niên trưởng thành cùng độ tuổi.<br>"
                   "1. Hãy xác định hình dạng phân phối của từng tập dữ liệu (Lệch phải / Lệch trái / Đối xứng hình chuông).<br>"
                   "2. So sánh mối quan hệ giữa Số trung bình (Mean) và Trung vị (Median) trong từng trường hợp và giải thích nguyên nhân.",
        "analysis": "Lệch phải (Right-skewed): đuôi dài sang phải, có các giá trị cực lớn kéo Mean > Median. Lệch trái (Left-skewed): đuôi dài sang trái, có các giá trị cực nhỏ kéo Mean < Median. Đối xứng (Symmetric): Mean approx Median.",
        "hints": [
            "Thu nhập có các tỷ phú, triệu phú tạo đuôi dài sang bên phải.",
            "Đề thi dễ đa số điểm 9, 10 ở bên phải, vài bạn điểm 1, 2 kéo đuôi dài sang bên trái.",
            "Chiều cao tuân theo phân phối chuẩn đối xứng quanh giá trị trung bình."
        ],
        "steps": [
            "<b>Bước 1: Phân tích Tập 1 (Thu nhập người lao động) `[+0,35đ]`</b><br>"
            "- <b>Hình dạng:</b> Lệch phải (Right-skewed / Phân phối dương). Phần lớn người lao động có mức thu nhập trung bình hoặc thấp dồn ở bên trái, trong khi có một số ít người có thu nhập cực cao tạo thành một chiếc đuôi dài kéo sang bên phải.<br>"
            "- <b>Mối quan hệ:</b> $\\text{Mean} > \\text{Median}$. Do số trung bình bị các mức thu nhập khổng lồ (điểm ngoại lai lớn) kéo lệch mạnh về bên phải, trong khi trung vị phản ánh chính xác mức thu nhập của người ở chính giữa xã hội.",
            "<b>Bước 2: Phân tích Tập 2 (Điểm thi đề quá dễ) `[+0,35đ]`</b><br>"
            "- <b>Hình dạng:</b> Lệch trái (Left-skewed / Phân phối âm). Đỉnh dữ liệu dồn về phía điểm cao (bên phải), một số ít điểm kém tạo thành đuôi dài kéo dài về phía điểm thấp (bên trái).<br>"
            "- <b>Mối quan hệ:</b> $\\text{Mean} < \\text{Median}$. Các điểm số quá thấp kéo số trung bình tụt xuống dưới trung vị.",
            "<b>Bước 3: Phân tích Tập 3 (Chiều cao nam thanh niên) `[+0,30đ]`</b><br>"
            "- <b>Hình dạng:</b> Đối xứng hình chuông (Symmetric bell-shaped). Dữ liệu phân bố đều đặn hai bên giá trị trung tâm.<br>"
            "- <b>Mối quan hệ:</b> $\\text{Mean} \\approx \\text{Median} \\approx \\text{Mode}$."
        ],
        "pro_tips": "Mẹo ghi nhớ trực quan: Đuôi kéo dài về phía nào thì phân phối lệch về phía đó, và Mean luôn bị đuôi kéo về phía mình nhiều hơn Median!",
        "pitfalls": "Nói ngược: nhầm đỉnh cao ở bên trái là 'lệch trái' (sai, đỉnh ở bên trái thì đuôi dài sang phải nên gọi là 'lệch phải')."
    })

    # TL1_7 (Nâng cao)
    exercises.append({
        "id": "TL1_7", "topicId": 1, "level": "Nâng cao",
        "title": "Nghịch lý Simpson (Simpson's Paradox): Phân tích bảng dữ liệu ba chiều và Biến ẩn (Lurking Variable)",
        "problem": "Một trường đại học xét tuyển vào hai khoa: Khoa Tự nhiên (Khoa A) và Khoa Xã hội (Khoa B). Số liệu tuyển sinh theo giới tính được ghi nhận như sau:<br>"
                   "- <b>Tại Khoa A:</b> Nam có 80/100 người trúng tuyển; Nữ có 18/20 người trúng tuyển.<br>"
                   "- <b>Tại Khoa B:</b> Nam có 10/20 người trúng tuyển; Nữ có 60/100 người trúng tuyển.<br>"
                   "1. Tính tỉ lệ trúng tuyển của Nam và Nữ trong từng khoa riêng biệt. Trong từng khoa, giới tính nào có tỉ lệ đỗ cao hơn?<br>"
                   "2. Gộp số liệu cả hai khoa, tính tỉ lệ trúng tuyển chung của toàn trường cho Nam và cho Nữ.<br>"
                   "3. Nêu hiện tượng nghịch lý xảy ra và giải thích nguyên nhân sâu xa (chỉ rõ biến ẩn / biến can thiệp - lurking variable).",
        "analysis": "Tính tỉ lệ riêng từng khoa: pA(Nam) = 80%, pA(Nu) = 90%; pB(Nam) = 50%, pB(Nu) = 60%. Khi gộp: Nam = 90/120 = 75%, Nu = 78/120 = 65%. Nam lại cao hơn! Biến ẩn là 'Khoa ứng tuyển' có độ khó khác nhau và số lượng đăng ký giữa hai giới rất chênh lệch.",
        "hints": [
            "Khoa A: 80/100 so với 18/20. Khoa B: 10/20 so với 60/100.",
            "Gộp chung: Tổng nam trúng tuyển = 80 + 10 = 90, tổng nộp = 100 + 20 = 120.",
            "Tổng nữ trúng tuyển = 18 + 60 = 78, tổng nộp = 20 + 100 = 120.",
            "Khoa nào có tỉ lệ đỗ cao hơn nói chung? Giới tính nào nộp nhiều vào khoa dễ đó?"
        ],
        "steps": [
            "<b>Bước 1: Tính tỉ lệ trúng tuyển trong từng khoa `[+0,35đ]`</b><br>"
            "- <b>Tại Khoa A (Khoa dễ đỗ):</b><br>"
            "  + Nam: $\\frac{80}{100} = 80\\%$<br>"
            "  + Nữ: $\\frac{18}{20} = 90\\%$<br>"
            "  $\\implies$ Ở Khoa A, tỉ lệ trúng tuyển của Nữ cao hơn Nam ($90\\% > 80\\%$).<br>"
            "- <b>Tại Khoa B (Khoa khó đỗ):</b><br>"
            "  + Nam: $\\frac{10}{20} = 50\\%$<br>"
            "  + Nữ: $\\frac{60}{100} = 60\\%$<br>"
            "  $\\implies$ Ở Khoa B, tỉ lệ trúng tuyển của Nữ vẫn cao hơn Nam ($60\\% > 50\\%$).",
            "<b>Bước 2: Tính tỉ lệ trúng tuyển chung toàn trường khi gộp dữ liệu `[+0,35đ]`</b><br>"
            "- Tổng số thí sinh Nam: $100 + 20 = 120$ thí sinh. Số đỗ: $80 + 10 = 90$.<br>"
            "$$P(\\text{Đỗ} \\mid \\text{Nam}) = \\frac{90}{120} = 0{,}75 = 75{,}0\\%$$"
            "- Tổng số thí sinh Nữ: $20 + 100 = 120$ thí sinh. Số đỗ: $18 + 60 = 78$.<br>"
            "$$P(\\text{Đỗ} \\mid \\text{Nữ}) = \\frac{78}{120} = 0{,}65 = 65{,}0\\%$$"
            "$\\implies$ Khi gộp chung, tỉ lệ trúng tuyển của Nam lại cao hơn Nữ ($75\\% > 65\\%$).",
            "<b>Bước 3: Giải thích nghịch lý Simpson `[+0,30đ]`</b><br>"
            "Đây là biểu hiện điển hình của <b>Nghịch lý Simpson (Simpson's Paradox)</b>: Một xu hướng xuất hiện trong tất cả các nhóm nhỏ nhưng lại bị đảo ngược hoàn toàn khi gộp dữ liệu lại.<br>"
            "<b>Nguyên nhân (Biến ẩn):</b> Do <i>khoa ứng tuyển</i> đóng vai trò là biến ẩn (confounding / lurking variable):<br>"
            "- Khoa A dễ đỗ hơn rất nhiều (tỉ lệ trúng tuyển trung bình $\\approx 81{,}7\\%$), và có tới $83{,}3\\%$ số thí sinh Nam nộp vào khoa này (100/120 bạn).<br>"
            "- Khoa B khắt khe hơn (tỉ lệ trúng tuyển trung bình $\\approx 58{,}3\\%$), nhưng có tới $83{,}3\\%$ thí sinh Nữ nộp vào khoa này (100/120 bạn).<br>"
            "Vì phần lớn Nam nộp vào nơi dễ đỗ còn phần lớn Nữ nộp vào nơi khó đỗ, tỉ lệ gộp chung của Nam bị kéo vọt lên cao hơn Nữ dù trong từng khoa Nữ đều có kết quả vượt trội!"
        ],
        "pro_tips": "Để nhận diện nghịch lý Simpson: Luôn nhìn vào tỉ trọng nộp đơn của các nhóm vào các phân khúc khác nhau (weights).",
        "pitfalls": "Chỉ nhìn vào kết luận tổng gộp 75% > 65% rồi vội vàng kết luận trường phân biệt đối xử với nữ giới."
    })

    # TL1_8 (Nâng cao)
    exercises.append({
        "id": "TL1_8", "topicId": 1, "level": "Nâng cao",
        "title": "Hồi quy bội (Multiple Regression): Ý nghĩa hệ số Ceteris Paribus và Hệ số xác định R²",
        "problem": "Một công ty công nghệ xây dựng mô hình hồi quy bội dự đoán mức lương hàng tháng ($y$, triệu đồng) theo số năm kinh nghiệm ($x_1$, năm) và điểm đánh giá hiệu suất công việc ($x_2$, thang 100 điểm) từ dữ liệu của 150 kỹ sư phần mềm:<br>"
                   "$$\\hat{y} = 12{,}0 + 2{,}4 x_1 + 0{,}15 x_2$$"
                   "Mô hình có tổng bình phương toàn phần $SST = 2500$ và tổng bình phương phần dư $SSE = 450$.<br>"
                   "1. Giải thích ý nghĩa của hệ số hồi quy riêng phần $b_1 = 2{,}4$ và $b_2 = 0{,}15$ theo nguyên tắc <i>ceteris paribus</i> (các điều kiện khác không đổi).<br>"
                   "2. Một kỹ sư có 5 năm kinh nghiệm và đạt 80 điểm hiệu suất thì mức lương dự đoán là bao nhiêu?<br>"
                   "3. Tính hệ số xác định $R^2$ của mô hình và nêu ý nghĩa thực tế của con số này.",
        "analysis": "Hệ số b1 trong hồi quy bội là mức thay đổi của y khi x1 tăng 1 đơn vị VỚI ĐIỀU KIỆN x2 GIỮ NGUYÊN. R^2 = 1 - SSE/SST = SSR/SST.",
        "hints": [
            "Bắt buộc phải có cụm từ 'khi điểm hiệu suất x2 không đổi' khi giải thích b1.",
            "Thay x1 = 5 và x2 = 80 vào phương trình để tính y_hat.",
            "R^2 = 1 - SSE/SST = 1 - 450/2500 = 1 - 0.18 = 0.82 (82%)."
        ],
        "steps": [
            "<b>Bước 1: Giải thích ý nghĩa các hệ số hồi quy riêng phần `[+0,35đ]`</b><br>"
            "- <b>Hệ số $b_1 = 2{,}4$:</b> Trong điều kiện <i>điểm đánh giá hiệu suất $x_2$ không đổi</i>, cứ mỗi năm kinh nghiệm làm việc tăng thêm, mức lương dự đoán trung bình của kỹ sư tăng thêm $2{,}4$ triệu đồng/tháng.<br>"
            "- <b>Hệ số $b_2 = 0{,}15$:</b> Trong điều kiện <i>số năm kinh nghiệm $x_1$ không đổi</i>, cứ mỗi điểm hiệu suất công việc tăng thêm, mức lương dự đoán trung bình của kỹ sư tăng thêm $0{,}15$ triệu đồng/tháng (tức 150.000 đồng/tháng).<br>"
            "- <b>Hệ số chặn $b_0 = 12{,}0$:</b> Kỹ sư mới vào nghề chưa có kinh nghiệm ($x_1 = 0$) và điểm hiệu suất bằng 0 ($x_2 = 0$) có mức lương cơ sở dự đoán là 12 triệu đồng/tháng.",
            "<b>Bước 2: Dự đoán mức lương kỹ sư cụ thể `[+0,30đ]`</b><br>"
            "Thay $x_1 = 5$ và $x_2 = 80$ vào phương trình mô hình:<br>"
            "$$\\hat{y} = 12{,}0 + 2{,}4 \\times 5 + 0{,}15 \\times 80 = 12{,}0 + 12{,}0 + 12{,}0 = 36{,}0\\text{ (triệu đồng/tháng)}$$",
            "<b>Bước 3: Tính hệ số xác định R² và nêu ý nghĩa `[+0,35đ]`</b><br>"
            "Hệ số xác định (Coefficient of Determination) $R^2$ được tính bằng:<br>"
            "$$R^2 = 1 - \\frac{SSE}{SST} = 1 - \\frac{450}{2500} = 1 - 0{,}18 = 0{,}82\\text{ (hoặc 82\\%)}$$"
            "<b>Ý nghĩa:</b> Mô hình hồi quy bội này giải thích được $82\\%$ sự biến thiên (sự dao động) của mức lương kỹ sư thông qua hai biến độc lập là số năm kinh nghiệm và điểm hiệu suất công việc; $18\\%$ sự biến thiên còn lại do các yếu tố khác chưa được đưa vào mô hình hoặc do sai số ngẫu nhiên."
        ],
        "pro_tips": "Trong bài thi tự luận hồi quy bội, nếu quên viết điều kiện 'giữ nguyên các biến còn lại' (ceteris paribus) thì sẽ bị trừ 50% số điểm của câu giải thích!",
        "pitfalls": "Quên điều kiện giữ nguyên biến còn lại khi giải thích hệ số hồi quy riêng phần."
    })

    return exercises

if __name__ == "__main__":
    t1 = get_topic_1()
    print(f"Generated Topic 1: {len(t1)} exercises.")
