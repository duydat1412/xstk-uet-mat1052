# verify/build_references.py
import json

LESSON_REFS = {
    "A1": {
        "slide_file": "week01.pdf",
        "slide_name": "Tuần 01 — Dữ liệu và Thu thập",
        "pages": "Slide 23 – 50",
        "page_start": 23,
        "section": "Phần 2: Từ đối tượng đến biến (Slide 23–30) & Phần 3: Từ biến đến khung dữ liệu (Slide 31–50)",
        "stat20": "Stat20 Mục 1.1, 1.2, 1.3 (Data Frames & Variable Types)",
        "key_points": [
            "Đơn vị quan sát (Observation) ở mỗi hàng và Biến số (Variable) ở mỗi cột",
            "Phân loại 4 họ biến: Định danh (Nominal), Thứ bậc (Ordinal), Rời rạc (Discrete), Liên tục (Continuous)",
            "Cạm bẫy mã số: MSSV, SĐT, Mã chuyến bay là biến phân loại định danh, không phải biến số"
        ],
        "remind": "Nếu bạn chưa phân biệt được biến định danh vs thứ bậc, hoặc hay nhầm mã số là biến số, hãy mở lại Slide Week 01 từ trang 23 đến 45 để xem các ví dụ trực quan về bảng Palmer Penguins và phim Marvel."
    },
    "A2": {
        "slide_file": "week02.pdf",
        "slide_name": "Tuần 02 — Tóm tắt dữ liệu (Phần 1)",
        "pages": "Slide 6 – 35",
        "page_start": 6,
        "section": "Phần 1: Dữ liệu phân loại — Bảng liên hợp, Bảng tần số & Tỉ lệ (Slide 6–35)",
        "stat20": "Stat20 Mục 2.2 (Categorical Summaries & Contingency Tables)",
        "key_points": [
            "Bảng liên hợp 2 chiều (Contingency Table) tóm tắt mối quan hệ giữa 2 biến phân loại",
            "Xác định đúng mẫu số: Tỉ lệ trên tổng hàng, tổng cột hay tổng toàn bảng",
            "Bài tập mẫu UET W02-EX03 và phân tích tiêu đề W02-WP01"
        ],
        "remind": "Nếu bạn hay tính nhầm tỉ lệ phần trăm hoặc chọn sai mẫu số trong bảng 2 chiều, hãy đọc lại Slide Week 02 từ trang 15 đến 25 về quy tắc 'Đọc trước khi tính'."
    },
    "A3": {
        "slide_file": "week02.pdf",
        "slide_name": "Tuần 02 — Tóm tắt dữ liệu (Phần 2 & 3)",
        "pages": "Slide 36 – 114",
        "page_start": 36,
        "section": "Phần 2: Dữ liệu số (Slide 36–56), Phần 3: Đo lường phân tán (Slide 57–69) & Phần 4: Giá trị bất thường (Slide 70–95)",
        "stat20": "Stat20 Mục 2.4 (Numerical Summaries, IQR & Robustness)",
        "key_points": [
            "Đo độ tập trung: Trung bình (Mean) nhạy cảm ngoại lai vs Trung vị (Median) bền vững (Robust)",
            "Đo độ phân tán: Khoảng biến thiên (Range), Phương sai mẫu, Độ lệch chuẩn (SD), Tứ phân vị (IQR = Q3 - Q1)",
            "Quy tắc hàng rào Tukey xác định ngoại lai: [Q1 - 1.5*IQR, Q3 + 1.5*IQR]"
        ],
        "remind": "Nếu bạn chưa nắm chắc cách tìm Q1, Q3 hoặc công thức xác định ngoại lai 1.5*IQR, hãy mở lại Slide Week 02 các trang 44, 70–75 và 91 (bài mẫu W02-EX11)."
    },
    "A4": {
        "slide_file": "week04.pdf",
        "slide_name": "Tuần 04 — Mối quan hệ giữa các biến & Hồi quy OLS",
        "pages": "Slide 1 – 75",
        "page_start": 1,
        "section": "Phần 1: Hệ số tương quan Pearson r (Slide 1–40) & Phần 2: Hồi quy tuyến tính bình phương tối thiểu OLS (Slide 41–75)",
        "stat20": "Stat20 Mục 2.10 & Mục 7.2 (Correlation & Simple Linear Regression)",
        "key_points": [
            "Hệ số tương quan r ∈ [-1, 1], đo mức độ tuyến tính, bất biến với phép đổi thang đo tuyến tính",
            "Đường hồi quy mẫu: y^ = b0 + b1*x với b1 = r * (sy / sx) và b0 = y_bar - b1 * x_bar",
            "Phần dư e = y - y^, tổng phần dư luôn bằng 0, hệ số xác định R^2 = r^2"
        ],
        "remind": "Nếu bạn chưa thành thạo bấm máy Casio tính b0, b1 hoặc diễn giải ý nghĩa kinh tế của hệ số góc b1, hãy ôn lại Slide Week 04 từ trang 45 đến trang 65."
    },
    "A5": {
        "slide_file": "week04.pdf",
        "slide_name": "Tuần 04 — Hồi quy tuyến tính nâng cao",
        "pages": "Slide 76 – 99",
        "page_start": 76,
        "section": "Phần 3: Hồi quy với biến phân loại & Biến chỉ báo (Dummy Variables) (Slide 76–99)",
        "stat20": "Stat20 Mục 2.12 (Regression with Categorical Predictors)",
        "key_points": [
            "Biến chỉ báo Dummy: Nhận giá trị 1 nếu đối tượng thuộc nhóm, và 0 nếu ngược lại",
            "Mức tham chiếu (Baseline / Reference level): Nhóm bị khuyết hệ số, đóng vai trò mốc so sánh",
            "Ý nghĩa hệ số góc: Chênh lệch trung bình của nhóm chỉ báo so với nhóm tham chiếu"
        ],
        "remind": "Nếu bạn còn lúng túng khi viết phương trình hồi quy có biến Dummy hoặc đọc bảng output, hãy xem lại Slide Week 04 các trang 78–92."
    },
    "B1": {
        "slide_file": "week05.pdf",
        "slide_name": "Tuần 05 — Không gian mẫu & Tiên đề xác suất",
        "pages": "Slide 1 – 30",
        "page_start": 1,
        "section": "Phần 1 & 2: Không gian mẫu Ω, Biến cố và 3 Tiên đề xác suất Kolmogorov (Slide 1–30)",
        "stat20": "Stat20 Mục 3.1; OpenIntro Statistics Chương 3",
        "key_points": [
            "Không gian mẫu Ω: Tập hợp toàn bộ các kết quả sơ cấp có thể xảy ra của phép thử",
            "Biến cố A ⊆ Ω; Xác suất cổ điển P(A) = |A| / |Ω| khi các kết quả đồng khả năng",
            "3 Tiên đề Kolmogorov: P(A) ≥ 0, P(Ω) = 1, và P(∪Ai) = ∑P(Ai) khi các Ai xung khắc"
        ],
        "remind": "Nếu bạn cảm thấy khái niệm không gian mẫu và tiên đề xác suất trừu tượng, hãy đọc lại Slide Week 05 từ trang 10 đến 25 với các ví dụ tung đồng xu, xúc xắc."
    },
    "B2": {
        "slide_file": "week05.pdf",
        "slide_name": "Tuần 05 — Quy tắc cộng & Biến cố đối",
        "pages": "Slide 31 – 50",
        "page_start": 31,
        "section": "Phần 3: Quy tắc cộng, Biến cố đối và Nguyên lý bao hàm - loại trừ (Slide 31–50)",
        "stat20": "Stat20 Mục 3.1 & Mục 3.3.9 (Addition Rule & Inclusion-Exclusion)",
        "key_points": [
            "Biến cố đối lập: P(A^c) = 1 - P(A); Quy tắc vàng 'Ít nhất một' = 1 - P('Không có cái nào')",
            "Quy tắc cộng tổng quát: P(A ∪ B) = P(A) + P(B) - P(A ∩ B)",
            "Nguyên lý bao hàm - loại trừ cho 3 biến cố: P(A ∪ B ∪ C)"
        ],
        "remind": "Nếu bạn hay quên trừ phần giao P(A ∩ B) khi hai biến cố không xung khắc, hãy xem lại sơ đồ Venn ở Slide Week 05 trang 33–42."
    },
    "B3": {
        "slide_file": "week05.pdf",
        "slide_name": "Tuần 05 — Xác suất điều kiện & Định lý Bayes",
        "pages": "Slide 51 – 68",
        "page_start": 51,
        "section": "Phần 4: Xác suất có điều kiện, Quy tắc nhân, Sơ đồ cây & Định lý Bayes (Slide 51–68)",
        "stat20": "Stat20 Mục 3.3.3 & 3.3.4 (Conditional Probability & Bayes' Rule)",
        "key_points": [
            "Xác suất có điều kiện: P(A|B) = P(AB) / P(B) (với P(B) > 0), không gian mẫu thu hẹp về B",
            "Quy tắc nhân: P(AB) = P(B) * P(A|B) = P(A) * P(B|A)",
            "Định lý Bayes: P(Ai|B) = P(Ai)P(B|Ai) / ∑P(Aj)P(B|Aj); Mô hình dịch bệnh SIR (Slide 67–69)"
        ],
        "remind": "Nếu bạn gặp khó khăn khi vẽ sơ đồ cây hoặc tính xác suất xét nghiệm dương tính giả (Base Rate Fallacy), hãy đọc kỹ Slide Week 05 từ trang 55 đến 69."
    },
    "B4": {
        "slide_file": "week05.pdf",
        "slide_name": "Tuần 05 — Độc lập vs Xung khắc",
        "pages": "Slide 69 – 80",
        "page_start": 69,
        "section": "Phần 4: Phân biệt Độc lập vs Xung khắc (Slide 69–80; Câu hỏi kiểm tra W05-Q03)",
        "stat20": "Stat20 Mục 3.3.5 & 3.3.8 (Independence vs Mutually Exclusive)",
        "key_points": [
            "Hai biến cố độc lập khi P(AB) = P(A)P(B) hoặc P(A|B) = P(A)",
            "Hai biến cố xung khắc khi A ∩ B = ∅, tức P(AB) = 0",
            "Bẫy chí tử: Nếu P(A) > 0 và P(B) > 0, xung khắc thì KHÔNG THỂ độc lập!"
        ],
        "remind": "Đây là câu hỏi lừa kinh điển trong đề thi UET. Hãy xem kỹ Slide Week 05 trang 70–72 với lời cảnh báo: 'Xung khắc không phải độc lập'."
    },
    "B5": {
        "slide_file": "week05.pdf",
        "slide_name": "Tuần 05 — Giải tích kết hợp & Nghịch lý De Méré",
        "pages": "Slide 81 – 93",
        "page_start": 81,
        "section": "Phần 5: Giải nghịch lý De Méré (Slide 73–80) & Phần 6: Bài tập tổng hợp và Kỹ thuật đếm (Slide 81–93)",
        "stat20": "Stat20 Mục 3.4.2 (Combinatorics & Counting Principles)",
        "key_points": [
            "Quy tắc cộng (chia trường hợp rời nhau) và Quy tắc nhân (thực hiện liên tiếp các công đoạn)",
            "Hoán vị P_n = n!, Chỉnh hợp A_n^k = n!/(n-k)!, Tổ hợp C_n^k = n! / [k!(n-k)!]",
            "Nghịch lý De Méré: So sánh xác suất xuất hiện mặt 6 trong 4 lần tung vs cặp 6 trong 24 lần tung"
        ],
        "remind": "Nếu bạn hay nhầm lẫn giữa Chỉnh hợp (có thứ tự) và Tổ hợp (không thứ tự), hãy ôn lại Slide Week 05 trang 73–85 và bài toán tình huống W05-CASE01."
    },
    "C1": {
        "slide_file": "week06.pdf",
        "slide_name": "Tuần 06 — Biến ngẫu nhiên rời rạc & Hàm phân phối",
        "pages": "Slide 16 – 36",
        "page_start": 16,
        "section": "Phần 2: Biến ngẫu nhiên và Phân phối xác suất (Slide 16–24) & Phần 3: Hàm phân phối tích lũy cdf (Slide 25–36)",
        "stat20": "Stat20 Mục 4.1, 4.2, 4.3.1, 4.4 (Discrete Random Variables & CDF)",
        "key_points": [
            "Biến ngẫu nhiên rời rạc X: Ánh xạ từ không gian mẫu Ω vào tập con đếm được của R",
            "Hàm khối xác suất pmf p_X(x) = P(X = x) với điều kiện chuẩn hóa ∑p(x) = 1",
            "Hàm tích lũy cdf F(x) = P(X ≤ x): Hàm đơn điệu tăng, dạng bậc thang, liên tục bên phải"
        ],
        "remind": "Nếu bạn chưa biết cách lập bảng pmf tìm hằng số c hoặc vẽ đồ thị bậc thang của F(x), hãy đọc lại Slide Week 06 từ trang 18 đến 35."
    },
    "C2": {
        "slide_file": "week06.pdf",
        "slide_name": "Tuần 06 — Phân phối Bernoulli & Nhị thức",
        "pages": "Slide 37 – 52",
        "page_start": 37,
        "section": "Phần 4: Các phân phối rời rạc thông dụng — Phân phối Bernoulli & Nhị thức B(n, p) (Slide 37–52)",
        "stat20": "Stat20 Mục 4.3.2.2 & 4.3.2.3 (Bernoulli & Binomial Distributions)",
        "key_points": [
            "Dãy phép thử Bernoulli: n phép thử độc lập, mỗi phép thử chỉ có 2 kết quả (Thành công p, Thất bại 1-p)",
            "Công thức xác suất Nhị thức: P(X = k) = C_n^k * p^k * (1 - p)^(n - k)",
            "Bẫy ít nhất 1 lần thành công: P(X ≥ 1) = 1 - P(X = 0) = 1 - (1 - p)^n"
        ],
        "remind": "Nếu bạn chưa tự tin nhận diện các điều kiện của mô hình Nhị thức, hãy mở Slide Week 06 từ trang 39 đến 51."
    },
    "C3": {
        "slide_file": "week06.pdf",
        "slide_name": "Tuần 06 — Phân phối Siêu bội HG(N, M, n)",
        "pages": "Slide 53 – 65",
        "page_start": 53,
        "section": "Phần 4: Phân phối Siêu bội — Lấy mẫu không hoàn lại từ tổng thể hữu hạn (Slide 53–65)",
        "stat20": "Stat20 Mục 4.3.2.4 (Hypergeometric Distribution)",
        "key_points": [
            "Mô hình rút KHÔNG hoàn lại n phần tử từ hộp N phần tử có M phần tử đặc biệt",
            "Công thức xác suất Siêu bội: P(X = k) = [C_M^k * C_(N-M)^(n-k)] / C_N^n",
            "Liên hệ với Nhị thức: Khi N rất lớn so với n (n/N < 0.05), Siêu bội xấp xỉ Nhị thức với p = M/N"
        ],
        "remind": "Nếu bạn còn phân vân khi nào dùng Nhị thức (rút có hoàn lại), khi nào dùng Siêu bội (rút không hoàn lại), hãy xem lại bảng so sánh ở Slide Week 06 trang 55–62."
    },
    "C4": {
        "slide_file": "week06.pdf",
        "slide_name": "Tuần 06 — Phân phối Poisson & Cây quyết định mô hình",
        "pages": "Slide 66 – 80",
        "page_start": 66,
        "section": "Phần 4: Phân phối Poisson (Slide 66–69) & Phần 5: Cây quyết định lựa chọn mô hình rời rạc (Slide 70–80)",
        "stat20": "Stat20 Mục 4.3.2.5 & 4.3.2.6 (Poisson Distribution & Model Selection)",
        "key_points": [
            "Phân phối Poisson Po(λ): Mô hình hóa số biến cố hiếm xảy ra trong một khoảng thời gian/không gian liên tục",
            "Công thức xác suất: P(X = k) = (λ^k * e^(-λ)) / k!",
            "Quy tắc đổi tham số theo khoảng thời gian: λ' = λ * t; Xấp xỉ Poisson cho Nhị thức khi n ≥ 20, p ≤ 0.05"
        ],
        "remind": "Nếu bạn muốn nắm chắc sơ đồ chọn nhanh mô hình (Nhị thức, Siêu bội hay Poisson) khi đọc đề thi, hãy xem ngay Slide Week 06 trang 70–78."
    },
    "C5": {
        "slide_file": "week07.pdf",
        "slide_name": "Tuần 07 — Kỳ vọng & Tính chất tuyến tính",
        "pages": "Slide 4 – 13",
        "page_start": 4,
        "section": "Phần 1: Kỳ vọng và phương sai — Định nghĩa và Tính chất của Kỳ vọng (Slide 4–13)",
        "stat20": "Stat20 Mục 4.7 & 4.8 (Expected Value & LOTUS)",
        "key_points": [
            "Kỳ vọng E(X) = ∑ x*p(x): Trọng tâm khối lượng của phân phối xác suất",
            "Định lý LOTUS: E[g(X)] = ∑ g(x)*p(x) (không cần tìm phân phối của g(X))",
            "Tính chất tuyến tính vô điều kiện: E(aX + b) = a*E(X) + b và E(X + Y) = E(X) + E(Y) (kể cả khi không độc lập)"
        ],
        "remind": "Nếu bạn chưa nắm được bản chất trực giác của kỳ vọng như một điểm tựa cân bằng trên bập bênh, hãy xem hình minh họa trực quan ở Slide Week 07 trang 5–9."
    },
    "C6": {
        "slide_file": "week07.pdf",
        "slide_name": "Tuần 07 — Phương sai & Độ lệch chuẩn",
        "pages": "Slide 14 – 20, 79 – 81",
        "page_start": 14,
        "section": "Phần 1: Phương sai và độ lệch chuẩn (Slide 14–20) & Phần 7: Bài tập vận dụng 1 (Slide 79–81)",
        "stat20": "Stat20 Mục 4.10 (Variance & Standard Deviation)",
        "key_points": [
            "Định nghĩa: Var(X) = E[(X - μ)^2] = E(X^2) - [E(X)]^2; Độ lệch chuẩn SD(X) = √Var(X)",
            "Tính chất biến đổi: Var(aX + b) = a^2 * Var(X) và SD(aX + b) = |a| * SD(X)",
            "Khi X, Y độc lập: Var(X ± Y) = Var(X) + Var(Y) (luôn cộng phương sai, không bao giờ trừ)"
        ],
        "remind": "Nếu bạn hay làm sai bài tập tính Var(2X - 3Y) hoặc quên bình phương hệ số a^2, hãy đọc kỹ Slide Week 07 trang 16–19 và lời giải bài mẫu số 1 ở Slide 79–81."
    },
    "D1": {
        "slide_file": "week07.pdf",
        "slide_name": "Tuần 07 — Biến ngẫu nhiên i.i.d. & Mô hình chiếc hộp",
        "pages": "Slide 21 – 24",
        "page_start": 21,
        "section": "Phần 2: Các biến ngẫu nhiên độc lập cùng phân phối (i.i.d.) & Mô hình chiếc hộp (Slide 21–24)",
        "stat20": "Stat20 Mục 4.13 (Independent and Identically Distributed & Box Models)",
        "key_points": [
            "Biến ngẫu nhiên i.i.d. (independent and identically distributed): Độc lập và cùng tuân theo một quy luật xác suất",
            "Mô hình chiếc hộp (Box model): Rút thăm n lần CÓ hoàn lại từ một hộp vé ghi các con số",
            "Chuyển dịch tư duy: Xem mọi bài toán lấy mẫu ngẫu nhiên như việc rút thẻ từ một chiếc hộp trừu tượng"
        ],
        "remind": "Nếu bạn chưa hình dung được mô hình chiếc hộp liên hệ thế nào với các biến ngẫu nhiên trong bài thi, hãy mở lại Slide Week 07 trang 21–24."
    },
    "D2": {
        "slide_file": "week07.pdf",
        "slide_name": "Tuần 07 — Tổng & Trung bình mẫu: Quy tắc căn bậc hai",
        "pages": "Slide 25 – 32",
        "page_start": 25,
        "section": "Phần 2: Tổng và trung bình của các biến i.i.d. — Square Root Law (Slide 25–32)",
        "stat20": "Stat20 Mục 4.14 (Sum and Average of i.i.d. Variables)",
        "key_points": [
            "Tổng Sn = X1 + ... + Xn: E(Sn) = n*μ, SD(Sn) = σ*√n (quy tắc nhân căn n)",
            "Trung bình mẫu X_bar = Sn / n: E(X_bar) = μ, SD(X_bar) = σ / √n (sai số giảm theo 1/√n)",
            "Quy tắc căn bậc hai (Square Root Law): Muốn giảm sai số đo lường đi k lần, phải tăng cỡ mẫu gấp k^2 lần"
        ],
        "remind": "Đây là dạng bài trắc nghiệm tính nhanh rất phổ biến. Hãy mở Slide Week 07 trang 26–30 để ghi nhớ sự khác biệt giữa σ*√n và σ/√n."
    },
    "D3": {
        "slide_file": "week07.pdf",
        "slide_name": "Tuần 07 — Bất đẳng thức Chebyshev",
        "pages": "Slide 33 – 37",
        "page_start": 33,
        "section": "Phần 3: Bất đẳng thức Chebyshev và cận trên sai lệch [CHUYÊN ĐỀ ĐỘC QUYỀN SLIDE UET] (Slide 33–37)",
        "stat20": "Nội dung nâng cao riêng biệt của Slide UET (không có trong Stat20)",
        "key_points": [
            "Bất đẳng thức Chebyshev: P(|X - μ| ≥ k*σ) ≤ 1 / k^2 (với mọi k > 0)",
            "Dạng sai số tuyệt đối ε: P(|X - μ| ≥ ε) ≤ Var(X) / ε^2",
            "Ưu điểm tối cao: Đúng cho MỌI phân phối xác suất bất kỳ (kể cả phân phối lệch, rời rạc hay liên tục)"
        ],
        "remind": "Nếu gặp bài toán yêu cầu 'đánh giá xác suất mà không biết dạng phân phối', hãy mở ngay Slide Week 07 trang 34–37 về Bất đẳng thức Chebyshev."
    },
    "D4": {
        "slide_file": "week07.pdf",
        "slide_name": "Tuần 07 — Luật số lớn yếu (WLLN)",
        "pages": "Slide 38 – 40",
        "page_start": 38,
        "section": "Phần 3: Luật số lớn yếu — Weak Law of Large Numbers [ĐỘC QUYỀN SLIDE UET] (Slide 38–40)",
        "stat20": "Nội dung giải tích xác suất nâng cao của Slide UET",
        "key_points": [
            "Phát biểu WLLN: lim (n→∞) P(|X_bar_n - μ| ≥ ε) = 0 với mọi sai số ε > 0 tùy ý",
            "Ý nghĩa toán học: Trung bình mẫu hội tụ theo xác suất về kỳ vọng thực của tổng thể",
            "Ứng dụng thực tế: Cơ sở toán học nền tảng cho ngành bảo hiểm, casino và thống kê suy diễn"
        ],
        "remind": "Nếu bạn muốn hiểu bản chất chứng minh WLLN từ BĐT Chebyshev (Var(X_bar) = σ^2/n → 0), hãy xem Slide Week 07 trang 38–40."
    },
    "E1": {
        "slide_file": "week07.pdf",
        "slide_name": "Tuần 07 — Biến liên tục, Hàm mật độ (pdf) & Hàm cdf",
        "pages": "Slide 41 – 47, 82 – 83",
        "page_start": 41,
        "section": "Phần 4: Biến ngẫu nhiên liên tục, Hàm mật độ pdf & Hàm tích lũy cdf (Slide 41–47) & Bài tập vận dụng 2 (Slide 82–83)",
        "stat20": "Stat20 Mục 4.15 (Continuous Random Variables & Probability Density)",
        "key_points": [
            "Hàm mật độ f(x) ≥ 0, điều kiện chuẩn hóa: ∫(-∞→∞) f(x)dx = 1",
            "Xác suất tại một điểm luôn bằng 0: P(X = c) = 0 ⇒ P(a ≤ X ≤ b) = P(a < X < b) = ∫(a→b) f(x)dx",
            "Hàm tích lũy F(x) = ∫(-∞→x) f(t)dt, liên tục trên R và f(x) = F'(x) tại các điểm khả vi"
        ],
        "remind": "Nếu bạn chưa vững kỹ năng tích phân tìm tham số k để hàm là mật độ hợp lệ, hãy đọc Slide Week 07 trang 42–46 và lời giải mẫu Bài tập 2 ở Slide 82–83."
    },
    "E2": {
        "slide_file": "week07.pdf",
        "slide_name": "Tuần 07 — Kỳ vọng & Phương sai của biến liên tục",
        "pages": "Slide 48 – 49",
        "page_start": 48,
        "section": "Phần 4: Kỳ vọng và phương sai của biến ngẫu nhiên liên tục (Slide 48–49)",
        "stat20": "Stat20 Mục 4.15 (Expectation & Variance for Continuous Variables)",
        "key_points": [
            "Kỳ vọng liên tục: E(X) = ∫(-∞→∞) x*f(x)dx; E[g(X)] = ∫(-∞→∞) g(x)*f(x)dx",
            "Phương sai: Var(X) = ∫(-∞→∞) x^2*f(x)dx - [E(X)]^2",
            "Kỹ năng giải tích: Tích phân từng phần ∫u dv = uv - ∫v du là công cụ bắt buộc trong bài thi tự luận UET"
        ],
        "remind": "Nếu bạn hay tính nhầm tích phân từng phần khi tìm E(X) hoặc Var(X), hãy mở Slide Week 07 trang 48–49 để xem kỹ các bước biến đổi mẫu."
    },
    "E3": {
        "slide_file": "week07.pdf",
        "slide_name": "Tuần 07 — Phân phối Đều U(a, b)",
        "pages": "Slide 50 – 53",
        "page_start": 50,
        "section": "Phần 5: Các phân phối liên tục đặc biệt — Phân phối Đều U(a, b) (Slide 50–53)",
        "stat20": "Stat20 Mục 4.16.1 (Uniform Distribution)",
        "key_points": [
            "Hàm mật độ không đổi: f(x) = 1 / (b - a) trên đoạn [a, b]",
            "Xác suất tỉ lệ thuận với độ dài khoảng con: P(c ≤ X ≤ d) = (d - c) / (b - a)",
            "Đặc trưng số học: Kỳ vọng E(X) = (a + b)/2 (trung điểm); Phương sai Var(X) = (b - a)^2 / 12"
        ],
        "remind": "Nếu bạn gặp bài toán thời gian chờ xe buýt hoặc đồng hồ ngẫu nhiên, hãy mở Slide Week 07 trang 50–53 về mô hình phân phối Đều."
    },
    "E4": {
        "slide_file": "week07.pdf",
        "slide_name": "Tuần 07 — Phân phối Chuẩn N(μ, σ²)",
        "pages": "Slide 54 – 62, 84 – 85",
        "page_start": 54,
        "section": "Phần 5: Phân phối Chuẩn Gauss, Chuẩn hóa Z & Tra bảng Laplace (Slide 54–62) & Bài tập vận dụng 3 (Slide 84–85)",
        "stat20": "Stat20 Mục 4.16.2 (Normal Distribution & Z-scores)",
        "key_points": [
            "Đồ thị hình chuông Gauss đối xứng quanh kỳ vọng μ; Điểm uốn tại μ ± σ",
            "Biến đổi chuẩn hóa Z = (X - μ) / σ ~ N(0, 1); Quy tắc tra bảng Φ(z) và tính chất đối xứng Φ(-z) = 1 - Φ(z)",
            "Quy tắc thực nghiệm: 68% trong khoảng μ±1σ, 95% trong khoảng μ±2σ, 99.7% trong khoảng μ±3σ",
            "Bài toán ngược tìm phân vị x_p = μ + z_p * σ và bài toán tải trọng thang máy (Slide 84–85)"
        ],
        "remind": "Phân phối chuẩn chiếm tới 2–3 điểm trong bài thi. Hãy ôn kỹ Slide Week 07 từ trang 54 đến 62 và bài tập thang máy ở Slide 84–85."
    },
    "E5": {
        "slide_file": "week07.pdf",
        "slide_name": "Tuần 07 — Phân phối Mũ, Chi-bình phương & t-Student",
        "pages": "Slide 63 – 67, 86 – 88",
        "page_start": 63,
        "section": "Phần 5: Phân phối Mũ Exp(λ), Chi-bình phương & t-Student [ĐỘC QUYỀN SLIDE UET] (Slide 63–67) & Bài tập vận dụng 4 (Slide 86–88)",
        "stat20": "Chuyên đề phân phối liên tục mở rộng của Slide UET Week 07",
        "key_points": [
            "Phân phối Mũ Exp(λ): Hàm mật độ f(x) = λ*e^(-λx) (x ≥ 0); Hàm cdf F(x) = 1 - e^(-λx); Xác suất đuôi P(X > x) = e^(-λx)",
            "Đặc trưng: Kỳ vọng E(X) = 1/λ, Phương sai Var(X) = 1/λ^2; Tính chất không nhớ (Memoryless): P(X > s+t | X > s) = P(X > t)",
            "Nhận diện đồ thị phân phối Chi-bình phương (lệch phải, k bậc tự do) và t-Student (hình chuông, đuôi dày hơn chuẩn)"
        ],
        "remind": "Đề thi UET thường có câu hỏi về tính chất không nhớ hoặc kết hợp phân phối Mũ với CLT. Hãy xem Slide Week 07 trang 63–65 và Bài tập 4 ở Slide 86–88."
    },
    "E6": {
        "slide_file": "week07.pdf",
        "slide_name": "Tuần 07 — Định lý Giới hạn Trung tâm (CLT)",
        "pages": "Slide 68 – 77, 89 – 91",
        "page_start": 68,
        "section": "Phần 6: Định lý giới hạn trung tâm (CLT) (Slide 68–77) & Phần 7: Bài tập vận dụng 5 — Bóng đèn dự phòng / Cỡ mẫu (Slide 89–91)",
        "stat20": "Stat20 Mục 4.17 (Central Limit Theorem)",
        "key_points": [
            "Phát biểu CLT: Với mẫu i.i.d. có kỳ vọng μ và phương sai σ^2 hữu hạn, khi n đủ lớn (n ≥ 30):",
            "Tổng mẫu Sn ≈ N(n*μ, n*σ^2) ⇒ Z = (Sn - n*μ) / (σ*√n) ~ N(0, 1)",
            "Trung bình mẫu X_bar ≈ N(μ, σ^2/n) ⇒ Z = (X_bar - μ) / (σ/√n) ~ N(0, 1)",
            "Bài toán tìm số lượng linh kiện dự phòng n: Đặt ẩn phụ u = √n, giải bất phương trình bậc hai (Bài tập 5, Slide 89–91)"
        ],
        "remind": "Đây là bài toán 'chốt hạ' phân loại điểm 9–10 của UET. Hãy xem thật kỹ lời giải phương trình bậc hai tìm n = 23 bóng đèn ở Slide Week 07 trang 89–91."
    }
}

print(f"Total reference items created: {len(LESSON_REFS)}")
# Save as JSON for verification
with open("content/lesson_references.json", "w", encoding="utf-8") as f:
    json.dump(LESSON_REFS, f, ensure_ascii=False, indent=2)
print("Saved to content/lesson_references.json successfully.")
