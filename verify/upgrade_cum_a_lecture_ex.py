# verify/upgrade_cum_a_lecture_ex.py
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read content/cum_a.js
with open("content/cum_a.js", "r", encoding="utf-8") as f:
    text = f.read()

# Define new examples for A1..A5 directly from Slide Week 01, Week 02, Week 04
A1_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 01 — W01-IMS02] Bộ dữ liệu Chim cánh cụt Palmer Penguins",
        q: "Trong bộ dữ liệu nghiên cứu sinh học Palmer Penguins (Slide 40–41), các nhà khoa học thu thập thông tin về 344 cá thể chim cánh cụt gồm các cột: (1) Loài (`species`: Adelie, Chinstrap, Gentoo); (2) Đảo sinh sống (`island`: Biscoe, Dream, Torgersen); (3) Chiều dài mỏ (`bill_length_mm`, mm); (4) Năm thu thập (`year`: 2007, 2008, 2009). Hãy phân loại chính xác 4 biến trên.",
        sol: "<b>Phân tích đối chiếu theo Slide Week 01 (trang 40–41):</b><br>" +
             "1. <code>species</code>: Các nhóm tên loài chim không có thứ bậc hơn kém $\\\\rightarrow$ <b>Biến phân loại Định danh (Nominal)</b>.<br>" +
             "2. <code>island</code>: Tên các hòn đảo nơi chim sinh sống $\\\\rightarrow$ <b>Biến phân loại Định danh (Nominal)</b>.<br>" +
             "3. <code>bill_length_mm</code>: Phép đo liên tục chiều dài mỏ bằng thước kẹp (có thể nhận giá trị thập phân như 39,1 mm) $\\\\rightarrow$ <b>Biến số Liên tục (Continuous Numerical)</b>.<br>" +
             "4. <code>year</code>: Năm khảo sát (2007, 2008, 2009), có quan hệ thứ tự thời gian tự nhiên $\\\\rightarrow$ <b>Biến phân loại Thứ bậc (Ordinal)</b> (hoặc biến số rời rạc nếu xét hiệu số năm)."
      },
      {
        level: "Trung bình",
        t: "[Slide Week 01 — W01-CH02] Thử thách '1, 2, 3, 4, 5 nói được gì?'",
        q: "Một kỹ sư nhận một tệp dữ liệu chỉ có một cột $x$ chứa các số nguyên: 1, 2, 3, 4, 5 (Slide 28–29). Tài liệu mô tả bị thiếu. Kỹ sư này kết luận ngay: 'Vì $x$ lưu bằng số nguyên nên $x$ chắc chắn là biến số rời rạc'. Kết luận này đúng hay sai? Tại sao?",
        sol: "<b>Phân tích theo Slide Week 01 (trang 28–29):</b><br>" +
             "<b>Kết luận SAI hoàn toàn!</b> Cách biểu diễn số trong máy tính chỉ là kiểu lưu trữ (Storage type), không quyết định bản chất thống kê của biến.<br>" +
             "- Nếu $x$ là mã hóa của khu vực (1=Miền Bắc, 2=Miền Trung, 3=Miền Nam) $\\\\rightarrow$ $x$ là <b>Biến phân loại Định danh</b>.<br>" +
             "- Nếu $x$ là đánh giá mức độ hài lòng (1 sao đến 5 sao) $\\\\rightarrow$ $x$ là <b>Biến phân loại Thứ bậc</b>.<br>" +
             "- Chỉ khi $x$ là số người phụ thuộc hoặc số sản phẩm đếm được (phép tính trung bình có ý nghĩa định lượng thực tế) thì $x$ mới là <b>Biến số rời rạc</b>."
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 01 — W01-IMS01 & W01-CH03] Xác định Đơn vị quan sát (Observation Unit)",
        q: "Dựa vào hai bài toán thực tế trong bài giảng Slide Week 01 (trang 38–43), hãy xác định chính xác Đơn vị quan sát (Observation unit) của mỗi hàng trong bảng dữ liệu:<br>" +
           "a) [W01-IMS01] Bảng dữ liệu 23 bộ phim thuộc Vũ trụ Điện ảnh Marvel (MCU) ghi nhận: Tên phim, Năm phát hành, Doanh thu mở màn (triệu USD), Doanh thu toàn cầu.<br>" +
           "b) [W01-CH03] Bảng lịch sử đăng ký học tập do Phòng Đào tạo UET trích xuất gồm các cột: `MSSV`, `MaMon`, `HocKy`, `DiemSo`.",
        sol: "<b>Phân tích bản chất cấu trúc dữ liệu theo Slide Week 01:</b><br>" +
             "a) Trong bảng Marvel (Slide 38–39): Mỗi hàng đại diện cho <b>một bộ phim cụ thể</b> (A movie). Có 23 hàng tức là có 23 bộ phim được quan sát.<br>" +
             "b) Trong bảng Đào tạo UET (Slide 42–43): Một hàng <b>KHÔNG PHẢI</b> là một sinh viên, cũng không phải một môn học (vì một sinh viên học nhiều môn, một môn có nhiều sinh viên). Mỗi hàng là <b>một lượt đăng ký học (Sinh viên × Môn học × Học kỳ)</b>."
      }
    ]"""

A2_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 02 — W02-EX01 & W02-EX02] Thảm họa Titanic: Số đếm hay Tỉ lệ?",
        q: "Bảng liên hợp thảm họa Titanic trong bài giảng (Slide 16–19) ghi nhận kết quả sống sót của 2.201 hành khách:<br>" +
           "- Người lớn: 654 người sống sót, 1.438 người thiệt mạng (Tổng: 2.092 người lớn).<br>" +
           "- Trẻ em: 57 người sống sót, 52 người thiệt mạng (Tổng: 109 trẻ em).<br>" +
           "Một bạn sinh viên nhìn vào bảng và kết luận: <i>'Người lớn có kết quả sống sót tốt hơn trẻ em vì 654 > 57'</i>. Hãy chỉ ra sai lầm của kết luận này và tính tỉ lệ sống sót chính xác của từng nhóm.",
        sol: "<b>Phân tích theo Slide Week 02 (trang 18–19):</b><br>" +
             "Sai lầm chí mạng: So sánh số đếm thô (654 vs 57) giữa hai nhóm có quy mô tổng thể chênh lệch quá lớn (2.092 người lớn vs 109 trẻ em). Muốn so sánh công bằng, bắt buộc phải dùng <b>Tỉ lệ có điều kiện</b>:<br>" +
             "- Tỉ lệ sống sót của người lớn: $P(\\\\text{Sống} \\\\mid \\\\text{Người lớn}) = \\\\frac{654}{2092} \\\\approx 31{,}3\\\\%$.<br>" +
             "- Tỉ lệ sống sót của trẻ em: $P(\\\\text{Sống} \\\\mid \\\\text{Trẻ em}) = \\\\frac{57}{109} \\\\approx 52{,}3\\\\%$.<br>" +
             "<b>Kết luận đúng:</b> Trẻ em có tỉ lệ sống sót cao hơn người lớn rất nhiều ($52{,}3\\\\% > 31{,}3\\\\%$) do nguyên tắc ưu tiên cứu hộ trẻ em!"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 02 — W02-EX03] Thử thách xác định Mẫu số trước khi tính",
        q: "Dựa vào bảng liên hợp Titanic (Slide 21–22) gồm tổng cộng 2.201 người, trong đó tổng số người sống sót là 711 người (654 người lớn, 57 trẻ em). Hãy xác định đúng mẫu số và tính giá trị của 3 câu hỏi sau:<br>" +
           "A. 'Trong số người lớn, bao nhiêu phần sống sót?'<br>" +
           "B. 'Trong số những người sống sót, bao nhiêu phần là trẻ em?'<br>" +
           "C. 'Trong toàn bộ hành khách, tỉ lệ trẻ em sống sót là bao nhiêu?'",
        sol: "<b>Đáp án chuẩn hóa theo Slide Week 02 (trang 22):</b><br>" +
             "- <b>Câu A:</b> Cụm từ <i>'Trong số người lớn'</i> chỉ định MẪU SỐ là tổng số người lớn ($2.092$).<br>" +
             "  $$\\\\text{Tỉ lệ} = \\\\frac{654}{2092} \\\\approx 31{,}26\\\\%$$<br>" +
             "- <b>Câu B:</b> Cụm từ <i>'Trong số người sống sót'</i> chỉ định MẪU SỐ là tổng người sống ($711$).<br>" +
             "  $$\\\\text{Tỉ lệ} = \\\\frac{57}{711} \\\\approx 8{,}02\\\\%$$<br>" +
             "- <b>Câu C:</b> Cụm từ <i>'Trong toàn bộ hành khách'</i> chỉ định MẪU SỐ là tổng toàn bảng ($2.201$).<br>" +
             "  $$\\\\text{Tỉ lệ} = \\\\frac{57}{2201} \\\\approx 2{,}59\\\\%$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 02 — W02-WP01] Phản biện bài báo: Tiêu đề có đúng không?",
        q: "Một bài báo nhìn vào bảng dữ liệu Titanic và giật tít: <i>'Hơn 90% số người sống sót là người lớn, vậy đi tàu Titanic là người lớn an toàn hơn trẻ em!'</i> (Slide 34–35). Dưới góc độ xác suất thống kê, hãy phân tích tại sao tiêu đề này ngụy biện và đánh tráo khái niệm.",
        sol: "<b>Phân tích phản biện theo Slide Week 02 (trang 34–35):</b><br>" +
             "1. Con số 'hơn 90%' thực chất là $\\\\frac{654}{711} \\\\approx 91{,}98\\\\%$, tức là xác suất $P(\\\\text{Người lớn} \\\\mid \\\\text{Sống sót})$.<br>" +
             "2. Khái niệm 'an toàn hơn' (xác suất sống sót khi gặp nạn) phải được đo bằng $P(\\\\text{Sống sót} \\\\mid \\\\text{Người lớn}) = 31{,}3\\\\%$, so sánh với $P(\\\\text{Sống sót} \\\\mid \\\\text{Trẻ em}) = 52{,}3\\\\%$.<br>" +
             "3. Người lớn chiếm tới 92% số người sống sót đơn giản là vì họ chiếm tới 95% tổng số người trên tàu ($2.092 / 2.201$), chứ không phải vì người lớn được an toàn hơn!"
      }
    ]"""

A3_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 02 — W02-EX10] Bài toán thi bù OpenIntro 4e",
        q: "Trong một lớp học gồm 25 sinh viên, có 24 bạn thi đợt 1 với điểm trung bình đạt $\\\\bar{x} = 74$ điểm (Slide 88–89). Bạn sinh viên thứ 25 bị ốm phải thi bù và đạt 64 điểm. Hãy tính điểm trung bình mới của toàn bộ 25 sinh viên trong lớp.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 02 (trang 89):</b><br>" +
             "1. Tổng điểm thi của 24 bạn đầu tiên là: $\\\\sum_{i=1}^{24} x_i = 24 \\\\times 74 = 1776$ điểm.<br>" +
             "2. Sau khi cộng điểm của bạn thứ 25 ($64$ điểm), tổng điểm của cả 25 bạn là:<br>" +
             "   $$\\\\sum_{i=1}^{25} x_i = 1776 + 64 = 1840 \\\\text{ điểm}$$<br>" +
             "3. Điểm trung bình mới của cả lớp là:<br>" +
             "   $$\\\\bar{x}_{\\\\text{new}} = \\\\frac{1840}{25} = 73{,}6 \\\\text{ điểm}$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 02 — W02-EX11] Xác định Ngoại lai theo Hàng rào Tukey",
        q: "Cho 20 điểm thi đã sắp xếp tăng dần từ bài tập OpenIntro 4e (Slide 90–91):<br>" +
           "$$57, 66, 69, 71, 72, 73, 74, 77, 78, 78, 79, 79, 81, 81, 82, 83, 83, 88, 89, 94$$<br>" +
           "Biết $Q_1 = 72{,}5$ và $Q_3 = 82{,}5$. Hãy tính khoảng tứ phân vị $\\\\text{IQR}$, xác định hai hàng rào Tukey và kiểm tra xem có điểm ngoại lai nào không.",
        sol: "<b>Lời giải từng bước theo Slide Week 02 (trang 91):</b><br>" +
             "1. Tính khoảng tứ phân vị: $\\\\text{IQR} = Q_3 - Q_1 = 82{,}5 - 72{,}5 = 10$.<br>" +
             "2. Độ vươn hàng rào: $1{,}5 \\\\times \\\\text{IQR} = 1{,}5 \\\\times 10 = 15$.<br>" +
             "3. Xác định hai ngưỡng hàng rào:<br>" +
             "   - <b>Hàng rào dưới (Lower fence):</b> $Q_1 - 1{,}5\\\\text{IQR} = 72{,}5 - 15 = 57{,}5$.<br>" +
             "   - <b>Hàng rào trên (Upper fence):</b> $Q_3 + 1{,}5\\\\text{IQR} = 82{,}5 + 15 = 97{,}5$.<br>" +
             "4. <b>Kiểm tra ngoại lai:</b> Điểm thi $57 < 57{,}5$ (nằm ngoài hàng rào dưới) $\\\\rightarrow$ <b>57 là giá trị ngoại lai (outlier)</b> duy nhất của bộ dữ liệu."
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 02 — W02-CH02 & W02-CH03] Phản ví dụ: Mean = Median có đối xứng không?",
        q: "a) [W02-CH02] Dãy dữ liệu mẫu STAT20 gồm 11 quan sát có Trung bình $\\\\approx 8{,}455$, Trung vị $= 8$, $\\\\text{SD} \\\\approx 1{,}695$. Nếu thay một giá trị 6 bằng $-200$ (ngoại lai cực đoan), hãy quan sát sự biến động của Trung bình và Trung vị.<br>" +
           "b) [W02-CH03] Hãy chứng minh hoặc bác bỏ mệnh đề: <i>'Nếu Trung bình = Trung vị thì phân phối chắc chắn đối xứng'</i>.",
        sol: "<b>Phân tích bản chất theo Slide Week 02 (trang 75 & 79):</b><br>" +
             "a) Khi thay $6$ bằng $-200$ (Slide 75):<br>" +
             "   - <b>Trung vị (Median):</b> Vẫn giữ nguyên bằng $8$ (bền vững hoàn hảo!).<br>" +
             "   - <b>Trung bình (Mean):</b> Bị kéo sụt thê thảm từ $8{,}455$ xuống $-10{,}273$; độ lệch chuẩn SD vọt lên $62{,}94$.<br>" +
             "b) <b>Bác bỏ mệnh đề!</b> Mệnh đề trên là SAI (Slide 79). Phản ví dụ mẫu 5 số: $(-4, -1, 0, 2, 3)$.<br>" +
             "   - Tổng $= (-4) + (-1) + 0 + 2 + 3 = 0 \\\\implies \\\\text{Mean} = 0$.<br>" +
             "   - Số chính giữa là $0 \\\\implies \\\\text{Median} = 0$.<br>" +
             "   - Dãy số này hoàn toàn <b>không đối xứng</b> quanh 0 vì khoảng cách về phía âm kéo dài tới $-4$ trong khi phía dương chỉ tới $+3$!"
      }
    ]"""

A4_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 04 — W04-EX01 & W04-CH01] Tính chất của Hệ số tương quan Pearson r",
        q: "a) [W04-EX01] Nếu ta đổi thang đo nhiệt độ từ Celsius sang Fahrenheit ($y = 1{,}8x + 32$), hệ số tương quan $r$ giữa nhiệt độ và lượng điện tiêu thụ có thay đổi không?<br>" +
           "b) [W04-CH01] Chứng minh hoặc bác bỏ mệnh đề: <i>'Hệ số tương quan $r = 0$ đồng nghĩa với việc hai biến $X$ và $Y$ không có mối liên hệ nào'</i>.",
        sol: "<b>Phân tích lý thuyết theo Slide Week 04 (trang 16–19):</b><br>" +
             "a) Hệ số tương quan $r$ <b>bất biến với phép đổi thang đo tuyến tính dương</b>: $r(a x + b, y) = r(x, y)$ với mọi $a > 0$. Do đó $r$ không hề thay đổi!<br>" +
             "b) <b>Khẳng định SAI!</b> Hệ số Pearson $r$ chỉ đo mức độ <b>liên hệ tuyến tính (đường thẳng)</b>.<br>" +
             "   - Phản ví dụ kinh điển (Slide 19): Xét 5 điểm với $y = x^2$: $(-2, 4), (-1, 1), (0, 0), (1, 1), (2, 4)$.<br>" +
             "   - Do tính đối xứng hoàn hảo, $r(X, Y) = 0$, nhưng giữa $X$ và $Y$ có quan hệ hàm số phi tuyến hoàn hảo ($Y = X^2$)!"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 04 — W04-WP02] Suy ra Đường hồi quy OLS từ Thống kê tóm tắt",
        q: "Trong nghiên cứu mối liên hệ giữa tỉ lệ tốt nghiệp THPT ($x$, %) và tỉ lệ nghèo đói ($y$, %) tại các bang của Hoa Kỳ (Slide 44–45), số liệu tóm tắt cho thấy:<br>" +
           "$$\\\\bar{x} = 86{,}01\\\\%, \\\\quad s_x = 3{,}73\\\\%, \\\\quad \\\\bar{y} = 11{,}35\\\\%, \\\\quad s_y = 3{,}10\\\\%, \\\\quad r = -0{,}75$$<br>" +
           "Hãy tìm phương trình đường hồi quy tuyến tính mẫu $\\\\hat{y} = b_0 + b_1 x$ và nêu ý nghĩa hệ số góc $b_1$.",
        sol: "<b>Lời giải chi tiết theo Slide Week 04 (trang 45):</b><br>" +
             "1. Tính hệ số góc $b_1$:<br>" +
             "   $$b_1 = r \\\\frac{s_y}{s_x} = -0{,}75 \\\\times \\\\frac{3{,}10}{3{,}73} \\\\approx -0{,}623 \\\\approx -0{,}62$$<br>" +
             "2. Tính hệ số chặn $b_0$ dựa vào điểm trung bình $(\\\\bar{x}, \\\\bar{y})$ luôn thuộc đường hồi quy:<br>" +
             "   $$b_0 = \\\\bar{y} - b_1 \\\\bar{x} = 11{,}35 - (-0{,}623) \\\\times 86{,}01 \\\\approx 64{,}68$$<br>" +
             "3. Phương trình hồi quy mẫu: $\\\\hat{y} = 64{,}68 - 0{,}62 x$.<br>" +
             "4. <b>Ý nghĩa hệ số góc:</b> Khi tỉ lệ tốt nghiệp THPT của một bang tăng thêm $1\\\\%$, mô hình dự đoán tỉ lệ nghèo đói trung bình giảm đi $0{,}62\\\\%$."
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 04 — W04-Q02 & W04-WP01] Tính và Diễn giải Phần dư (Residual)",
        q: "Sử dụng mô hình hồi quy $\\\\hat{y} = 64{,}68 - 0{,}62 x$ ở trên. Bang Rhode Island có tỉ lệ tốt nghiệp thực tế là $x = 81\\\\%$ và tỉ lệ nghèo thực tế là $y = 12{,}8\\\\%$ (Slide 26, 36–37).<br>" +
           "a) Tính giá trị dự báo $\\\\hat{y}$ và phần dư $e$ cho bang Rhode Island.<br>" +
           "b) Diễn giải ý nghĩa của dấu phần dư vừa tìm được.",
        sol: "<b>Lời giải chi tiết theo Slide Week 04 (trang 37):</b><br>" +
             "a) Giá trị dự báo của mô hình (Fitted value):<br>" +
             "   $$\\\\hat{y} = 64{,}68 - 0{,}62 \\\\times 81 = 64{,}68 - 50{,}22 = 14{,}46\\\\%$$<br>" +
             "   Phần dư (Residual):<br>" +
             "   $$e = y - \\\\hat{y} = 12{,}8\\\\% - 14{,}46\\\\% = -1{,}66\\\\%$$<br>" +
             "b) <b>Ý nghĩa thực tế:</b> Phần dư mang dấu âm ($e = -1{,}66\\\\%$) chứng tỏ tỉ lệ nghèo thực tế của bang Rhode Island thấp hơn $1{,}66\\\\%$ so với mức nghèo mà mô hình dự đoán dựa trên tỉ lệ học vấn."
      }
    ]"""

A5_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 04 — W04-Q04 & W04-WP03] Mô hình Giá sách và Biến chỉ báo Dummy",
        q: "Mô hình dự đoán giá bán của sách giáo khoa (USD) theo thể tích cuốn sách ($x$, $\\\\text{cm}^3$) và loại bìa (Slide 58–61) có dạng:<br>" +
           "$$\\\\widehat{\\\\text{price}} = 1{,}08 + 0{,}016 \\\\times \\\\text{volume} - 1{,}84 \\\\times D_{\\\\text{softback}}$$<br>" +
           "Trong đó biến chỉ báo $D_{\\\\text{softback}} = 1$ nếu là sách bìa mềm, và bằng $0$ nếu là sách bìa cứng. Hãy xác định mức tham chiếu (Baseline) và giải thích ý nghĩa hệ số $-1{,}84$.",
        sol: "<b>Phân tích chuẩn mực theo Slide Week 04 (trang 59 & 61):</b><br>" +
             "1. <b>Mức tham chiếu (Baseline):</b> Là nhóm có $D_{\\\\text{softback}} = 0$, tức là <b>Sách bìa cứng (Hardcover)</b>.<br>" +
             "2. <b>Ý nghĩa hệ số $-1{,}84$:</b> Khi so sánh hai cuốn sách có <b>cùng thể tích</b> (giữ `volume` cố định), cuốn sách bìa mềm được mô hình dự đoán có giá bán <b>thấp hơn trung bình 1,84 USD</b> so với cuốn sách bìa cứng."
      },
      {
        level: "Trung bình",
        t: "[Slide Week 04 — W04-EX05] Tính Giá trị dự báo cho Sách bìa mềm",
        q: "Một cuốn sách giáo trình bìa mềm có thể tích đo được là $\\\\text{volume} = 600\\\\text{ cm}^3$ (Slide 62–63). Dựa vào phương trình hồi quy trên, hãy tính giá bán dự báo của cuốn sách này.",
        sol: "<b>Lời giải chi tiết theo Slide Week 04 (trang 63):</b><br>" +
             "1. Vì cuốn sách là bìa mềm nên biến chỉ báo nhận giá trị $D_{\\\\text{softback}} = 1$.<br>" +
             "2. Thay $\\\\text{volume} = 600$ và $D_{\\\\text{softback}} = 1$ vào phương trình:<br>" +
             "   $$\\\\widehat{\\\\text{price}} = 1{,}08 + 0{,}016 \\\\times 600 - 1{,}84 \\\\times 1$$<br>" +
             "   $$\\\\widehat{\\\\text{price}} = 1{,}08 + 9{,}60 - 1{,}84 = 8{,}84 \\\\text{ USD}$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 04 — W04-Q05 & W04-CASE01] Mô hình Zagat: Nguyên tắc 'Giữ biến khác cố định'",
        q: "Dữ liệu khảo sát nhà hàng Zagat (Slide 64–66, 92–94) cho phương trình dự đoán giá bữa ăn (USD):<br>" +
           "$$\\\\widehat{\\\\text{price}} = -52{,}35 + 1{,}64 \\\\times \\\\text{food} + 1{,}89 \\\\times \\\\text{decor}$$<br>" +
           "Trong đó `food` và `decor` là điểm số đánh giá từ 1 đến 30.<br>" +
           "a) Diễn giải hệ số $1{,}64$ của biến `food`.<br>" +
           "b) Hai nhà hàng A và B có cùng điểm trang trí `decor` = 20. Nhà hàng A có điểm món ăn `food` cao hơn nhà hàng B là 3 điểm. Dự đoán giá bữa ăn ở nhà hàng nào đắt hơn và đắt hơn bao nhiêu?",
        sol: "<b>Phân tích theo Slide Week 04 (trang 66 & 94):</b><br>" +
             "a) <b>Diễn giải hệ số 1,64:</b> Khi so sánh hai nhà hàng có <b>cùng điểm trang trí decor</b>, nhà hàng nào có điểm món ăn food cao hơn 1 điểm thì giá bữa ăn dự báo trung bình cao hơn $1{,}64$ USD.<br>" +
             "b) Vì hai nhà hàng có cùng điểm `decor`, chênh lệch giá dự báo hoàn toàn do chênh lệch điểm `food` quyết định:<br>" +
             "   $$\\\\Delta \\\\widehat{\\\\text{price}} = 1{,}64 \\\\times \\\\Delta \\\\text{food} = 1{,}64 \\\\times 3 = 4{,}92 \\\\text{ USD}$$<br>" +
             "   Nhà hàng A được dự báo có giá đắt hơn nhà hàng B đúng $4{,}92$ USD."
      }
    ]"""

# Replace in cum_a.js
# Lesson A1
p_a1 = r'(id:\s*["\']A1["\'][\s\S]*?examples:\s*\[)[\s\S]*?(\]\s*,\s*pitfalls:)'
text = re.sub(p_a1, lambda m: m.group(1) + "\n" + A1_EXAMPLES[16:-1] + "\n    " + m.group(2), text)

# Lesson A2
p_a2 = r'(id:\s*["\']A2["\'][\s\S]*?examples:\s*\[)[\s\S]*?(\]\s*,\s*pitfalls:)'
text = re.sub(p_a2, lambda m: m.group(1) + "\n" + A2_EXAMPLES[16:-1] + "\n    " + m.group(2), text)

# Lesson A3
p_a3 = r'(id:\s*["\']A3["\'][\s\S]*?examples:\s*\[)[\s\S]*?(\]\s*,\s*pitfalls:)'
text = re.sub(p_a3, lambda m: m.group(1) + "\n" + A3_EXAMPLES[16:-1] + "\n    " + m.group(2), text)

# Lesson A4
p_a4 = r'(id:\s*["\']A4["\'][\s\S]*?examples:\s*\[)[\s\S]*?(\]\s*,\s*pitfalls:)'
text = re.sub(p_a4, lambda m: m.group(1) + "\n" + A4_EXAMPLES[16:-1] + "\n    " + m.group(2), text)

# Lesson A5
p_a5 = r'(id:\s*["\']A5["\'][\s\S]*?examples:\s*\[)[\s\S]*?(\]\s*,\s*pitfalls:)'
text = re.sub(p_a5, lambda m: m.group(1) + "\n" + A5_EXAMPLES[16:-1] + "\n    " + m.group(2), text)

with open("content/cum_a.js", "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully upgraded content/cum_a.js with exact lecture examples!")
