import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Import previously defined exercises for topic 1
with open("content/tuluan_data.json", "r", encoding="utf-8") as f:
    exercises = json.load(f)

# ==============================================================================
# DẠNG 2: LÝ THUYẾT XÁC SUẤT, CÓ ĐIỀU KIỆN & BAYES (TL2_1 -> TL2_8)
# ==============================================================================
exercises.append({
    "id": "TL2_1", "topicId": 2, "level": "Cơ bản",
    "title": "Xác suất cổ điển: Gieo hai con xúc xắc cân đối",
    "problem": "Gieo đồng thời hai con xúc xắc 6 mặt cân đối và đồng chất. Hãy tính xác suất của các biến cố sau:<br>"
               "1. Biến cố $A$: 'Tổng số chấm xuất hiện trên hai con xúc xắc lớn hơn hoặc bằng 9'.<br>"
               "2. Biến cố $B$: 'Tổng số chấm xuất hiện là một số nguyên tố'.",
    "analysis": "Không gian mẫu gồm 36 cặp kết quả đồng khả năng (i, j) với 1 <= i, j <= 6. Liệt kê các cặp thỏa mãn điều kiện và áp dụng công thức xác suất cổ điển P = |A| / |Omega|.",
    "hints": [
        "Không gian mẫu |Omega| = 6 * 6 = 36.",
        "Tổng >= 9 gồm các tổng: 9, 10, 11, 12. Liệt kê các cặp (i, j).",
        "Các số nguyên tố có thể xuất hiện từ 2 đến 12 là: 2, 3, 5, 7, 11."
    ],
    "steps": [
        "<b>Bước 1: Xác định không gian mẫu `[+0,25đ]`</b><br>"
        "Mỗi con xúc xắc có 6 mặt, gieo 2 con xúc xắc độc lập:<br>"
        "$$|\\Omega| = 6 \\times 6 = 36\\text{ (kết quả đồng khả năng)}$$",
        "<b>Bước 2: Tính xác suất biến cố A (Tổng ≥ 9) `[+0,35đ]`</b><br>"
        "Các cặp $(i, j)$ có tổng $\\ge 9$:<br>"
        "- Tổng = 9: $(3,6), (4,5), (5,4), (6,3)$ (4 cặp).<br>"
        "- Tổng = 10: $(4,6), (5,5), (6,4)$ (3 cặp).<br>"
        "- Tổng = 11: $(5,6), (6,5)$ (2 cặp).<br>"
        "- Tổng = 12: $(6,6)$ (1 cặp).<br>"
        "Số kết quả thuận lợi: $|A| = 4 + 3 + 2 + 1 = 10$.<br>"
        "$$P(A) = \\frac{|A|}{|\\Omega|} = \\frac{10}{36} = \\frac{5}{18} \\approx 0{,}2778\\text{ (27{,}78\\%)}$$",
        "<b>Bước 3: Tính xác suất biến cố B (Tổng là số nguyên tố) `[+0,40đ]`</b><br>"
        "Các số nguyên tố từ 2 đến 12 là $\\{2, 3, 5, 7, 11\\}$:<br>"
        "- Tổng = 2: $(1,1)$ (1 cặp).<br>"
        "- Tổng = 3: $(1,2), (2,1)$ (2 cặp).<br>"
        "- Tổng = 5: $(1,4), (2,3), (3,2), (4,1)$ (4 cặp).<br>"
        "- Tổng = 7: $(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)$ (6 cặp).<br>"
        "- Tổng = 11: $(5,6), (6,5)$ (2 cặp).<br>"
        "Số kết quả thuận lợi: $|B| = 1 + 2 + 4 + 6 + 2 = 15$.<br>"
        "$$P(B) = \\frac{|B|}{|\\Omega|} = \\frac{15}{36} = \\frac{5}{12} \\approx 0{,}4167\\text{ (41{,}67\\%)}$$"
    ],
    "pro_tips": "Lập bảng lưới 6x6 trong giấy nháp để đếm số cặp cực nhanh và không bao giờ bị đếm sót.",
    "pitfalls": "Đếm thiếu cặp đối xứng (ví dụ tính (3,6) nhưng quên tính (6,3))."
})

exercises.append({
    "id": "TL2_2", "topicId": 2, "level": "Cơ bản",
    "title": "Rút thăm không hoàn lại và quy tắc cộng xác suất",
    "problem": "Một hộp kín chứa 12 quả cầu cùng kích thước, trong đó có 5 quả màu đỏ và 7 quả màu xanh. Rút ngẫu nhiên lần lượt 2 quả cầu không hoàn lại.<br>"
               "1. Tính xác suất để cả hai quả cầu rút ra đều có màu đỏ.<br>"
               "2. Tính xác suất để cả hai quả cầu rút ra đều có màu xanh.<br>"
               "3. Tính xác suất để hai quả cầu rút ra có cùng màu.",
    "analysis": "Áp dụng quy tắc nhân cho việc lấy mẫu không hoàn lại P(A cap B) = P(A) * P(B|A). Hai biến cố 'cùng đỏ' và 'cùng xanh' là xung khắc nên áp dụng quy tắc cộng.",
    "hints": [
        "Lần 1 rút đỏ xác suất 5/12. Lần 2 chỉ còn 4 đỏ trên 11 quả.",
        "Lần 1 rút xanh xác suất 7/12. Lần 2 chỉ còn 6 xanh trên 11 quả.",
        "Cùng màu = Cả 2 đỏ HOẶC Cả 2 xanh (hai trường hợp xung khắc, cộng lại)."
    ],
    "steps": [
        "<b>Bước 1: Tính xác suất cả 2 quả màu đỏ `[+0,35đ]`</b><br>"
        "Gọi $R_1, R_2$ là lần 1, lần 2 rút được quả đỏ.<br>"
        "$$P(\\text{Cả 2 đỏ}) = P(R_1) \\cdot P(R_2 \\mid R_1) = \\frac{5}{12} \\times \\frac{4}{11} = \\frac{20}{132} = \\frac{5}{33} \\approx 0{,}1515\\text{ (15{,}15\\%)}$$",
        "<b>Bước 2: Tính xác suất cả 2 quả màu xanh `[+0,35đ]`</b><br>"
        "Gọi $X_1, X_2$ là lần 1, lần 2 rút được quả xanh.<br>"
        "$$P(\\text{Cả 2 xanh}) = P(X_1) \\cdot P(X_2 \\mid X_1) = \\frac{7}{12} \\times \\frac{6}{11} = \\frac{42}{132} = \\frac{7}{22} \\approx 0{,}3182\\text{ (31{,}82\\%)}$$",
        "<b>Bước 3: Tính xác suất rút được 2 quả cùng màu `[+0,30đ]`</b><br>"
        "Vì hai biến cố 'cả 2 đỏ' và 'cả 2 xanh' là xung khắc từng đôi một ($A \\cap B = \\emptyset$), theo Tiên đề 3 Kolmogorov:<br>"
        "$$P(\\text{Cùng màu}) = P(\\text{Cả 2 đỏ}) + P(\\text{Cả 2 xanh}) = \\frac{20}{132} + \\frac{42}{132} = \\frac{62}{132} = \\frac{31}{66} \\approx 0{,}4697\\text{ (46{,}97\\%)}$$"
    ],
    "pro_tips": "Có thể giải bằng tổ hợp: P(Cùng màu) = [C(5, 2) + C(7, 2)] / C(12, 2) = (10 + 21) / 66 = 31/66, cho kết quả tương đương 100%.",
    "pitfalls": "Quên giảm mẫu số ở lần thứ hai (vẫn chia cho 12 thay vì 11)."
})

exercises.append({
    "id": "TL2_3", "topicId": 2, "level": "Cơ bản",
    "title": "Vận dụng các công thức xác suất cơ bản và biểu đồ Venn",
    "problem": "Cho hai biến cố $A$ và $B$ thỏa mãn: $P(A) = 0{,}6$; $P(B) = 0{,}5$ và $P(A \\cap B) = 0{,}3$. Hãy tính:<br>"
               "1. Xác suất của hợp $P(A \\cup B)$.<br>"
               "2. Các xác suất có điều kiện $P(A \\mid B)$ và $P(B \\mid A)$.<br>"
               "3. Xác suất biến cố $A$ không xảy ra nhưng biến cố $B$ xảy ra: $P(A^c \\cap B)$.",
    "analysis": "Áp dụng trực tiếp quy tắc cộng tổng quát, định nghĩa xác suất có điều kiện và công thức hiệu hai biến cố.",
    "hints": [
        "P(A cup B) = P(A) + P(B) - P(A cap B).",
        "P(A|B) = P(A cap B) / P(B); P(B|A) = P(A cap B) / P(A).",
        "P(A^c cap B) = P(B) - P(A cap B)."
    ],
    "steps": [
        "<b>Bước 1: Tính xác suất của hợp P(A ∪ B) `[+0,30đ]`</b><br>"
        "Áp dụng nguyên lý bao hàm - loại trừ:<br>"
        "$$P(A \\cup B) = P(A) + P(B) - P(A \\cap B) = 0{,}6 + 0{,}5 - 0{,}3 = 0{,}80\\text{ (80\\%)}$$",
        "<b>Bước 2: Tính các xác suất có điều kiện `[+0,40đ]`</b><br>"
        "- $P(A \\mid B) = \\frac{P(A \\cap B)}{P(B)} = \\frac{0{,}3}{0{,}5} = 0{,}60$.<br>"
        "- $P(B \\mid A) = \\frac{P(A \\cap B)}{P(A)} = \\frac{0{,}3}{0{,}6} = 0{,}50$.",
        "<b>Bước 3: Tính P(Aᶜ ∩ B) `[+0,30đ]`</b><br>"
        "Biến cố $A^c \\cap B$ chính là phần diện tích của $B$ sau khi bỏ đi phần giao với $A$:<br>"
        "$$P(A^c \\cap B) = P(B) - P(A \\cap B) = 0{,}5 - 0{,}3 = 0{,}20\\text{ (20\\%)}$$"
    ],
    "pro_tips": "Nhận xét thêm: P(A|B) = 0,6 = P(A) và P(B|A) = 0,5 = P(B), điều này chứng minh A và B là hai biến cố độc lập!",
    "pitfalls": "Tính P(A^c cap B) bằng P(A^c) * P(B) khi chưa chứng minh độc lập."
})

exercises.append({
    "id": "TL2_4", "topicId": 2, "level": "Trung bình",
    "title": "Kiểm tra tính độc lập và xung khắc của hai biến cố",
    "problem": "Khảo sát 100 sinh viên thu được kết quả: 40 sinh viên đăng ký học thêm Tiếng Nhật (biến cố $A$), 30 sinh viên đăng ký học thêm Kỹ năng mềm (biến cố $B$), và có 12 sinh viên đăng ký cả hai khóa học.<br>"
               "1. Tính $P(A), P(B), P(A \\cap B)$ và $P(A \\cup B)$.<br>"
               "2. Hai biến cố $A$ và $B$ có xung khắc với nhau không? Vì sao?<br>"
               "3. Hai biến cố $A$ và $B$ có độc lập với nhau không? Giải thích bằng định nghĩa toán học.",
    "analysis": "Xung khắc kiểm tra P(AB) = 0. Độc lập kiểm tra P(AB) = P(A) * P(B).",
    "hints": [
        "P(A) = 40/100, P(B) = 30/100, P(AB) = 12/100.",
        "Xung khắc nếu P(AB) = 0. Ở đây P(AB) = 0.12 > 0.",
        "So sánh P(AB) với tích P(A)*P(B) = 0.4 * 0.3 = 0.12."
    ],
    "steps": [
        "<b>Bước 1: Tính các xác suất cơ bản `[+0,30đ]`</b><br>"
        "- $P(A) = \\frac{40}{100} = 0{,}40$.<br>"
        "- $P(B) = \\frac{30}{100} = 0{,}30$.<br>"
        "- $P(A \\cap B) = \\frac{12}{100} = 0{,}12$.<br>"
        "- $P(A \\cup B) = P(A) + P(B) - P(A \\cap B) = 0{,}40 + 0{,}30 - 0{,}12 = 0{,}58$.",
        "<b>Bước 2: Kiểm tra tính xung khắc `[+0,35đ]`</b><br>"
        "Hai biến cố xung khắc khi và chỉ khi chúng không thể đồng thời xảy ra, tức $P(A \\cap B) = 0$.<br>"
        "Ở đây, $P(A \\cap B) = 0{,}12 &gt; 0$ (có 12 sinh viên học cả hai khóa).<br>"
        "$\\implies A$ và $B$ <b>KHÔNG xung khắc</b>.",
        "<b>Bước 3: Kiểm tra tính độc lập `[+0,35đ]`</b><br>"
        "Ta xét tích xác suất:<br>"
        "$$P(A) \\cdot P(B) = 0{,}40 \\times 0{,}30 = 0{,}12$$<br>"
        "So sánh với $P(A \\cap B) = 0{,}12$, ta thấy đẳng thức nghiệm đúng:<br>"
        "$$P(A \\cap B) = P(A) \\cdot P(B) = 0{,}12$$<br>"
        "$\\implies A$ và $B$ là hai biến cố <b>HOÀN TOÀN ĐỘC LẬP</b>."
    ],
    "pro_tips": "Bài này cho thấy rất rõ: Hai biến cố ĐỘC LẬP thì KHÔNG THỂ XUNG KHẮC (vì nếu xung khắc thì P(AB) = 0 khác 0,12).",
    "pitfalls": "Nhầm lẫn giữa 2 khái niệm, cho rằng xung khắc là độc lập."
})

exercises.append({
    "id": "TL2_5", "topicId": 2, "level": "Trung bình",
    "title": "Công thức xác suất đầy đủ và Công thức Bayes trong chẩn đoán y tế",
    "problem": "Một căn bệnh hiểm nghèo có tỉ lệ mắc trong dân số là 1% ($P(D) = 0{,}01$). Một xét nghiệm y khoa có độ nhạy là 95% (người có bệnh xét nghiệm dương tính với xác suất 0,95) và độ đặc hiệu là 90% (người không có bệnh xét nghiệm âm tính với xác suất 0,90).<br>"
               "1. Tính xác suất một người dân ngẫu nhiên có kết quả xét nghiệm dương tính $P(T^+)$.<br>"
               "2. Một người đi xét nghiệm và nhận được kết quả Dương tính. Hãy tính xác suất người đó thực sự mắc bệnh: $P(D \\mid T^+)$. Nêu nhận xét về kết quả này.",
    "analysis": "Hệ đầy đủ gồm: Có bệnh D (0.01) và Không có bệnh D^c (0.99). Áp dụng công thức xác suất đầy đủ để tính P(T+), sau đó dùng công thức Bayes đảo ngược điều kiện.",
    "hints": [
        "P(D) = 0.01 => P(D^c) = 0.99.",
        "P(T+|D) = 0.95. P(T-|D^c) = 0.90 => P(T+|D^c) = 1 - 0.90 = 0.10 (dương tính giả).",
        "P(T+) = P(D)*P(T+|D) + P(D^c)*P(T+|D^c).",
        "Bayes: P(D|T+) = [P(D)*P(T+|D)] / P(T+)."
    ],
    "steps": [
        "<b>Bước 1: Thiết lập hệ đầy đủ và các xác suất thành phần `[+0,30đ]`</b><br>"
        "- Tỉ lệ có bệnh: $P(D) = 0{,}01 \\implies P(D^c) = 1 - 0{,}01 = 0{,}99$.<br>"
        "- Xác suất dương tính khi có bệnh: $P(T^+ \\mid D) = 0{,}95$.<br>"
        "- Xác suất dương tính giả khi không có bệnh: $P(T^+ \\mid D^c) = 1 - 0{,}90 = 0{,}10$.",
        "<b>Bước 2: Tính xác suất dương tính toàn cục P(T⁺) `[+0,35đ]`</b><br>"
        "Theo công thức xác suất đầy đủ:<br>"
        "$$P(T^+) = P(D) \\cdot P(T^+ \\mid D) + P(D^c) \\cdot P(T^+ \\mid D^c)$$<br>"
        "$$P(T^+) = 0{,}01(0{,}95) + 0{,}99(0{,}10) = 0{,}0095 + 0{,}0990 = 0{,}1085\\text{ (10{,}85\\%)}$$",
        "<b>Bước 3: Áp dụng công thức Bayes tính P(D | T⁺) `[+0,35đ]`</b><br>"
        "$$P(D \\mid T^+) = \\frac{P(D) \\cdot P(T^+ \\mid D)}{P(T^+)} = \\frac{0{,}0095}{0{,}1085} = \\frac{19}{217} \\approx 0{,}0876\\text{ (hay } 8{,}76\\%\\text{)}$$<br>"
        "<b>Nhận xét:</b> Dù xét nghiệm có độ nhạy rất cao (95%), nhưng vì bệnh rất hiếm (1%), phần lớn các ca dương tính là dương tính giả từ nhóm không bệnh (9,9% so với 0,95%). Do đó, một người dương tính chỉ có khoảng 8,76% cơ hội thực sự mắc bệnh và cần làm thêm xét nghiệm khẳng định lần 2!"
    ],
    "pro_tips": "Đây là bài toán kinh điển của Stat20 và đề thi UET, hãy luôn viết rõ hai nhánh: dương tính thật và dương tính giả.",
    "pitfalls": "Quên lấy biến cố đối của độ đặc hiệu: P(T+|D^c) = 1 - 0.90 = 0.10, nhiều bạn nhầm lẫn thay thẳng 0.90 vào công thức."
})

exercises.append({
    "id": "TL2_6", "topicId": 2, "level": "Trung bình",
    "title": "Độ tin cậy của hệ thống linh kiện nối tiếp và song song",
    "problem": "Một mạch điện điều khiển gồm 3 linh kiện $L_1, L_2, L_3$ hoạt động độc lập. Mạch hoạt động bình thường nếu linh kiện $L_1$ hoạt động VÀ ít nhất một trong hai linh kiện $L_2, L_3$ hoạt động (tức $L_1$ mắc nối tiếp với cụm song song $[L_2 // L_3]$).<br>"
               "Biết xác suất hoạt động tốt của từng linh kiện là: $P(L_1) = 0{,}90$; $P(L_2) = 0{,}80$; $P(L_3) = 0{,}80$.<br>"
               "Hãy tính xác suất để toàn bộ hệ thống hoạt động bình thường.",
    "analysis": "Xác định biến cố hệ thống: H = L1 cap (L2 cup L3). Do các linh kiện độc lập, P(H) = P(L1) * P(L2 cup L3). Cụm song song tính qua biến cố đối.",
    "hints": [
        "Tính xác suất cụm song song [L2 // L3] hoạt động: P(L2 cup L3) = 1 - P(cả 2 cùng hỏng).",
        "P(L2 hỏng) = 1 - 0.8 = 0.2. P(L3 hỏng) = 0.2.",
        "Nhân với P(L1) vì L1 mắc nối tiếp độc lập."
    ],
    "steps": [
        "<b>Bước 1: Tính độ tin cậy của cụm song song [L₂ // L₃] `[+0,40đ]`</b><br>"
        "Cụm song song ngừng hoạt động khi CẢ HAI linh kiện $L_2$ và $L_3$ cùng hỏng.<br>"
        "Vì $L_2, L_3$ độc lập:<br>"
        "- $P(L_2^c) = 1 - 0{,}80 = 0{,}20$.<br>"
        "- $P(L_3^c) = 1 - 0{,}80 = 0{,}20$.<br>"
        "Xác suất cả hai cùng hỏng: $P(L_2^c \\cap L_3^c) = 0{,}20 \\times 0{,}20 = 0{,}04$.<br>"
        "Xác suất cụm song song hoạt động tốt:<br>"
        "$$P(L_2 \\cup L_3) = 1 - P(L_2^c \\cap L_3^c) = 1 - 0{,}04 = 0{,}96\\text{ (96\\%)}$$",
        "<b>Bước 2: Tính độ tin cậy của toàn hệ thống `[+0,60đ]`</b><br>"
        "Hệ thống hoạt động khi $L_1$ hoạt động VÀ cụm song song hoạt động.<br>"
        "Vì $L_1$ độc lập với cụm $[L_2, L_3]$:<br>"
        "$$P(\\text{Hệ thống}) = P(L_1) \\cdot P(L_2 \\cup L_3) = 0{,}90 \\times 0{,}96 = 0{,}8640\\text{ (hay } 86{,}40\\%\\text{)}$$<br>"
        "<b>Kết luận:</b> Xác suất hệ thống hoạt động là 86,40%."
    ],
    "pro_tips": "Nguyên tắc nhớ nhanh: Mắc nối tiếp thì NHÂN xác suất hoạt động; Mắc song song thì NHÂN xác suất hỏng (rồi lấy 1 trừ đi).",
    "pitfalls": "Cộng xác suất của L2 và L3 (0.8 + 0.8 = 1.6 > 1) là sai hoàn toàn."
})

exercises.append({
    "id": "TL2_7", "topicId": 2, "level": "Nâng cao",
    "title": "Nghịch lý Monty Hall và phân tích cây xác suất",
    "problem": "Trong một gameshow, có 3 cánh cửa đóng kín giống hệt nhau: sau một cánh cửa là một chiếc ô tô, sau hai cánh cửa còn lại là hai con dê. Bạn chọn ngẫu nhiên cửa số 1. Người dẫn chương trình (biết rõ sau mỗi cửa có gì) mở cửa số 3 ra và cho thấy một con dê. Sau đó, MC cho bạn cơ hội: 'Bạn có muốn đổi sang cửa số 2 không?'.<br>"
               "Hãy dùng công thức xác suất có điều kiện chứng minh rằng bạn NÊN ĐỔI CỬA, và tính xác suất trúng ô tô nếu đổi cửa.",
    "analysis": "Gọi C_i là biến cố ô tô ở cửa i (P(C_i) = 1/3). Gọi M_3 là biến cố MC mở cửa 3. Tính P(C_2 | M_3) bằng định lý Bayes.",
    "hints": [
        "Ban đầu P(C1) = P(C2) = P(C3) = 1/3.",
        "Nếu ô tô ở cửa 1 (bạn đã chọn đúng), MC có thể mở cửa 2 hoặc 3: P(M3 | C1) = 1/2.",
        "Nếu ô tô ở cửa 2, MC BẮT BUỘC phải mở cửa 3 (vì bạn chọn cửa 1 và cửa 2 có xe): P(M3 | C2) = 1.",
        "Nếu ô tô ở cửa 3, MC không bao giờ mở cửa 3: P(M3 | C3) = 0."
    ],
    "steps": [
        "<b>Bước 1: Thiết lập các biến cố và xác suất ban đầu `[+0,30đ]`</b><br>"
        "Gọi $C_i$ là biến cố ô tô nằm sau cửa $i$ ($i \\in \\{1, 2, 3\\}$). Ban đầu: $P(C_1) = P(C_2) = P(C_3) = 1/3$.<br>"
        "Bạn chọn cửa 1. Gọi $M_3$ là biến cố MC mở cửa 3 có con dê.",
        "<b>Bước 2: Xác định các xác suất có điều kiện của MC `[+0,30đ]`</b><br>"
        "- Nếu ô tô ở cửa 1: MC có thể chọn mở cửa 2 hoặc 3 ngẫu nhiên $\\implies P(M_3 \\mid C_1) = 1/2$.<br>"
        "- Nếu ô tô ở cửa 2: MC không thể mở cửa 1 (bạn đang chọn) và không thể mở cửa 2 (có xe) $\\implies$ MC bắt buộc mở cửa 3: $P(M_3 \\mid C_2) = 1$.<br>"
        "- Nếu ô tô ở cửa 3: MC không thể làm lộ xe $\\implies P(M_3 \\mid C_3) = 0$.",
        "<b>Bước 3: Tính xác suất MC mở cửa 3 theo công thức đầy đủ `[+0,20đ]`</b><br>"
        "$$P(M_3) = \\frac{1}{3}\\left(\\frac{1}{2}\\right) + \\frac{1}{3}(1) + \\frac{1}{3}(0) = \\frac{1}{6} + \\frac{1}{3} = \\frac{1}{2}$$",
        "<b>Bước 4: Áp dụng công thức Bayes tính xác suất trúng xe khi đổi sang cửa 2 `[+0,20đ]`</b><br>"
        "$$P(C_2 \\mid M_3) = \\frac{P(C_2) \\cdot P(M_3 \\mid C_2)}{P(M_3)} = \\frac{\\frac{1}{3} \\times 1}{\\frac{1}{2}} = \\frac{2}{3} \\approx 0{,}6667\\text{ (66{,}67\\%)}$$<br>"
        "Trong khi đó, nếu giữ nguyên cửa 1: $P(C_1 \\mid M_3) = \\frac{\\frac{1}{3} \\times \\frac{1}{2}}{\\frac{1}{2}} = \\frac{1}{3} \\approx 33{,}33\\%$.<br>"
        "<b>Kết luận:</b> Đổi sang cửa 2 làm tăng gấp đôi cơ hội trúng ô tô (từ 1/3 lên 2/3), do đó người chơi chắc chắn NÊN ĐỔI."
    ],
    "pro_tips": "Trực giác đơn giản: Cửa 1 ban đầu chỉ có 1/3 cơ hội đúng (2/3 cơ hội xe nằm ở 2 cửa còn lại). Khi MC loại 1 cửa dê, toàn bộ 2/3 cơ hội dồn hết sang cánh cửa còn lại!",
    "pitfalls": "Nghĩ rằng chỉ còn 2 cánh cửa thì mỗi cửa có xác suất 50-50 (đây là ảo tưởng phổ biến)."
})

exercises.append({
    "id": "TL2_8", "topicId": 2, "level": "Nâng cao",
    "title": "Tính công bằng của bốc thăm không hoàn lại",
    "problem": "Một hộp có 10 lá thăm, trong đó chỉ có đúng 1 lá thăm trúng thưởng. Có 3 người A, B, C lần lượt rút ngẫu nhiên mỗi người 1 lá thăm (không hoàn lại).<br>"
               "1. Tính xác suất người A (rút đầu tiên) trúng thưởng.<br>"
               "2. Tính xác suất người B (rút thứ hai) trúng thưởng.<br>"
               "3. Tính xác suất người C (rút thứ ba) trúng thưởng. Việc rút trước hay rút sau có ảnh hưởng đến cơ hội trúng không?",
    "analysis": "Dùng quy tắc nhân chuỗi xác suất có điều kiện: Người thứ 2 trúng khi người thứ 1 trượt VÀ người thứ 2 trúng. Người thứ 3 trúng khi người 1 trượt VÀ người 2 trượt VÀ người 3 trúng.",
    "hints": [
        "P(A) = 1/10.",
        "P(B) = P(A trượt) * P(B trúng | A trượt) = (9/10) * (1/9).",
        "P(C) = P(A trượt) * P(B trượt | A trượt) * P(C trúng | A trượt, B trượt)."
    ],
    "steps": [
        "<b>Bước 1: Xác suất người A trúng thưởng `[+0,30đ]`</b><br>"
        "Người A rút đầu tiên từ 10 lá thăm có 1 lá trúng:<br>"
        "$$P(A) = \\frac{1}{10} = 0{,}10\\text{ (10\\%)}$$",
        "<b>Bước 2: Xác suất người B trúng thưởng `[+0,35đ]`</b><br>"
        "Người B trúng thưởng khi và chỉ khi người A rút trượt (xác suất 9/10), sau đó người B rút được lá trúng từ 9 lá còn lại (xác suất 1/9):<br>"
        "$$P(B) = P(A^c) \\cdot P(B \\mid A^c) = \\frac{9}{10} \\times \\frac{1}{9} = \\frac{1}{10} = 0{,}10\\text{ (10\\%)}$$",
        "<b>Bước 3: Xác suất người C trúng thưởng và Kết luận `[+0,35đ]`</b><br>"
        "Người C trúng khi cả A và B đều trượt, lúc này còn lại 8 lá thăm trong đó có 1 lá trúng:<br>"
        "$$P(C) = P(A^c) \\cdot P(B^c \\mid A^c) \\cdot P(C \\mid A^c \\cap B^c) = \\frac{9}{10} \\times \\frac{8}{9} \\times \\frac{1}{8} = \\frac{1}{10} = 0{,}10\\text{ (10\\%)}$$<br>"
        "<b>Kết luận:</b> Cả 3 người đều có xác suất trúng thưởng bằng nhau tuyệt đối ($P = 1/10 = 10\\%$). Thứ tự bốc thăm hoàn toàn không ảnh hưởng đến cơ hội công bằng của mỗi người!"
    ],
    "pro_tips": "Đây là nguyên lý toán học bảo đảm tính công bằng tuyệt đối của các trò chơi bốc thăm trúng thưởng trong đời thực.",
    "pitfalls": "Tưởng rằng người rút sau bị thiệt thòi vì người trước có thể đã lấy mất lá trúng."
})

print(f"Added Topic 2 exercises. Total so far: {len(exercises)}.")

with open("content/tuluan_data.json", "w", encoding="utf-8") as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)
