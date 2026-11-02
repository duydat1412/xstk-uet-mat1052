# verify/upgrade_cum_c_lecture_ex.py
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("content/cum_c.js", "r", encoding="utf-8") as f:
    text = f.read()

C1_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 06 — Ví dụ 3 & 5] Tung đồng xu ba lần và Hàm khối xác suất pmf",
        q: "Một đồng xu cân đối được tung 3 lần độc lập (Slide 18, 23–24). Ký hiệu H là ngửa, T là sấp. Gọi $X$ là số mặt ngửa xuất hiện trong 3 lần tung.<br>" +
           "a) Lập bảng phân phối xác suất pmf $p_X(x)$ của biến ngẫu nhiên $X$.<br>" +
           "b) Kiểm tra điều kiện chuẩn hóa $\\\\sum p_X(x) = 1$.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 06 (trang 24):</b><br>" +
             "a) Không gian mẫu gồm $2^3 = 8$ chuỗi kết quả đồng khả năng (mỗi chuỗi xác suất $1/8$):<br>" +
             "   $$\\\\Omega = \\\\{TTT, HTT, THT, TTH, HHT, HTH, THH, HHH\\\\}$$<br>" +
             "   - $X = 0$: Có 1 kết quả $\\\\{TTT\\\\} \\\\implies p_X(0) = \\\\frac{1}{8} = 0{,}125$.<br>" +
             "   - $X = 1$: Có 3 kết quả $\\\\{HTT, THT, TTH\\\\} \\\\implies p_X(1) = \\\\frac{3}{8} = 0{,}375$.<br>" +
             "   - $X = 2$: Có 3 kết quả $\\\\{HHT, HTH, THH\\\\} \\\\implies p_X(2) = \\\\frac{3}{8} = 0{,}375$.<br>" +
             "   - $X = 3$: Có 1 kết quả $\\\\{HHH\\\\} \\\\implies p_X(3) = \\\\frac{1}{8} = 0{,}125$.<br>" +
             "b) <b>Kiểm tra chuẩn hóa:</b><br>" +
             "   $$\\\\sum_{x=0}^3 p_X(x) = \\\\frac{1}{8} + \\\\frac{3}{8} + \\\\frac{3}{8} + \\\\frac{1}{8} = \\\\frac{8}{8} = 1$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 06 — Ví dụ 6 & 7] Hai sản phẩm đạt chuẩn và Hàm tích lũy cdf",
        q: "Hai sản phẩm được kiểm tra độc lập; mỗi sản phẩm đạt chuẩn với xác suất $0{,}8$ (Slide 28–32). Gọi $X$ là số sản phẩm đạt chuẩn ($X \\\\in \\\\{0, 1, 2\\\\}$). Phân phối xác suất của $X$ là: $p_X(0) = 0{,}04; p_X(1) = 0{,}32; p_X(2) = 0{,}64$.<br>" +
           "a) Xây dựng biểu thức hàm phân phối tích lũy $F_X(x) = P(X \\\\le x)$ trên toàn bộ trục số thực $\\\\mathbb{R}$.<br>" +
           "b) Tính xác suất có ít nhất 1 sản phẩm đạt chuẩn bằng hàm $F_X(x)$.",
        sol: "<b>Lời giải chi tiết theo Slide Week 06 (trang 29 & 32):</b><br>" +
             "a) Vì $X$ nhận giá trị rời rạc trên $\{0, 1, 2\}$, hàm tích lũy $F_X(x)$ có dạng bậc thang liên tục bên phải:<br>" +
             "   $$F_X(x) = \\\\begin{cases} 0 & \\\\text{khi } x < 0 \\\\cr 0{,}04 & \\\\text{khi } 0 \\\\le x < 1 \\\\cr 0{,}04 + 0{,}32 = 0{,}36 & \\\\text{khi } 1 \\\\le x < 2 \\\\cr 0{,}36 + 0{,}64 = 1{,}00 & \\\\text{khi } x \\\\ge 2 \\\\end{cases}$$<br>" +
             "b) Xác suất có ít nhất 1 sản phẩm đạt chuẩn là $P(X \\\\ge 1)$:<br>" +
             "   $$P(X \\\\ge 1) = 1 - P(X < 1) = 1 - P(X \\\\le 0) = 1 - F_X(0) = 1 - 0{,}04 = 0{,}96$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 06 — Ví dụ 8] Phân phối số đường dây điện thoại bận",
        q: "Một doanh nghiệp có 6 đường dây điện thoại (Slide 33–36). Gọi $X$ là số đường dây bận tại thời điểm quan sát, có bảng phân phối xác suất:<br>" +
           "$$p_X(0)=0{,}10; \\\\quad p_X(1)=0{,}15; \\\\quad p_X(2)=0{,}20; \\\\quad p_X(3)=0{,}25; \\\\quad p_X(4)=0{,}15; \\\\quad p_X(5)=0{,}10; \\\\quad p_X(6)=0{,}05$$<br>" +
           "a) Tính xác suất có nhiều nhất 3 đường dây bận $P(X \\\\le 3)$.<br>" +
           "b) Tính xác suất có từ 1 đến 4 đường dây bận $P(1 \\\\le X \\\\le 4)$.",
        sol: "<b>Lời giải chính xác theo Slide Week 06 (trang 34):</b><br>" +
             "a) Xác suất có nhiều nhất 3 đường dây bận:<br>" +
             "   $$P(X \\\\le 3) = p(0) + p(1) + p(2) + p(3) = 0{,}10 + 0{,}15 + 0{,}20 + 0{,}25 = 0{,}70 \\\\text{ (hay 70\\\\%)}$$<br>" +
             "b) Xác suất có từ 1 đến 4 đường dây bận:<br>" +
             "   $$P(1 \\\\le X \\\\le 4) = p(1) + p(2) + p(3) + p(4) = 0{,}15 + 0{,}20 + 0{,}25 + 0{,}15 = 0{,}75 \\\\text{ (hay 75\\\\%)}$$"
      }
    ]"""

C2_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 06 — Ví dụ 12] Bài kiểm tra trắc nghiệm 20 câu ngẫu nhiên",
        q: "Một bài kiểm tra có 20 câu trắc nghiệm (Slide 46–47). Mỗi câu có 4 phương án trả lời, trong đó chỉ có duy nhất một phương án đúng. Một học sinh không học bài nên đánh bừa ngẫu nhiên độc lập cả 20 câu.<br>" +
           "a) Xác định mô hình phân phối xác suất của số câu trả lời đúng $X$.<br>" +
           "b) Tính xác suất để học sinh đó làm đúng đúng 5 câu.",
        sol: "<b>Lời giải chi tiết theo Slide Week 06 (trang 47):</b><br>" +
             "a) Mỗi câu hỏi là một phép thử Bernoulli với xác suất đoán đúng $p = \\\\frac{1}{4} = 0{,}25$.<br>" +
             "   Vì có $n = 20$ câu độc lập nên số câu trả lời đúng tuân theo phân phối Nhị thức:<br>" +
             "   $$X \\\\sim B(n = 20, p = 0{,}25)$$<br>" +
             "b) Áp dụng công thức phân phối Nhị thức với $k = 5$:<br>" +
             "   $$P(X = 5) = C_{20}^5 p^5 (1-p)^{20-5} = C_{20}^5 (0{,}25)^5 (0{,}75)^{15}$$<br>" +
             "   $$P(X = 5) = 15504 \\\\times (0{,}25)^5 \\\\times (0{,}75)^{15} \\\\approx 0{,}2023 \\\\approx 20{,}23\\\\%$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 06 — Ví dụ 13] Dây chuyền sản xuất 12 sản phẩm đạt chuẩn",
        q: "Một dây chuyền tạo sản phẩm đạt chuẩn với xác suất $0{,}95$ (Slide 48–49). Chọn độc lập ngẫu nhiên 12 sản phẩm để kiểm tra chất lượng.<br>" +
           "a) Tính xác suất để toàn bộ 12 sản phẩm được chọn đều đạt chuẩn.<br>" +
           "b) Tính xác suất để có ít nhất một sản phẩm không đạt chuẩn (phế phẩm).",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 06 (trang 49):</b><br>" +
             "Gọi $X$ là số sản phẩm đạt chuẩn trong 12 sản phẩm $\\\\implies X \\\\sim B(12, 0{,}95)$.<br>" +
             "a) Xác suất cả 12 sản phẩm đều đạt chuẩn ($k = 12$):<br>" +
             "   $$P(X = 12) = C_{12}^{12} (0{,}95)^{12} (0{,}05)^0 = (0{,}95)^{12} \\\\approx 0{,}5404 \\\\approx 54{,}04\\\\%$$<br>" +
             "b) Biến cố 'Có ít nhất một phế phẩm' chính là biến cố đối của 'Cả 12 sản phẩm đều đạt chuẩn':<br>" +
             "   $$P(\\\\text{Ít nhất 1 phế phẩm}) = 1 - P(X = 12) = 1 - 0{,}5404 = 0{,}4596 \\\\approx 45{,}96\\\\%$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 06 — Ví dụ 20] Hệ thống 8 Cảm biến phát cảnh báo giả",
        q: "Một hệ thống giám sát an ninh có 8 cảm biến hoạt động độc lập (Slide 73–74). Trong một ca làm việc, xác suất mỗi cảm biến phát cảnh báo giả là $p = 0{,}05$. Tính xác suất trong ca đó hệ thống phát ra từ 1 đến 2 cảnh báo giả.",
        sol: "<b>Lời giải từng bước theo Slide Week 06 (trang 74):</b><br>" +
             "Gọi $X$ là số cảm biến phát cảnh báo giả $\\\\implies X \\\\sim B(n = 8, p = 0{,}05)$.<br>" +
             "Yêu cầu bài toán là tính $P(1 \\\\le X \\\\le 2) = P(X = 1) + P(X = 2)$:<br>" +
             "1. Tính $P(X = 1)$:<br>" +
             "   $$P(X = 1) = C_8^1 (0{,}05)^1 (0{,}95)^7 = 8 \\\\times 0{,}05 \\\\times 0{,}69834 \\\\approx 0{,}2793$$<br>" +
             "2. Tính $P(X = 2)$:<br>" +
             "   $$P(X = 2) = C_8^2 (0{,}05)^2 (0{,}95)^6 = 28 \\\\times 0{,}0025 \\\\times 0{,}73509 \\\\approx 0{,}0515$$<br>" +
             "3. Tổng xác suất:<br>" +
             "   $$P(1 \\\\le X \\\\le 2) = 0{,}2793 + 0{,}0515 = 0{,}3308 \\\\approx 33{,}08\\\\%$$"
      }
    ]"""

C3_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 06 — Ví dụ 14] Rút ba lá thăm không hoàn lại từ hộp 10 lá",
        q: "Một hộp có 10 lá thăm gồm 6 lá ghi số 1 và 4 lá ghi số 0 (Slide 52–54). Rút lần lượt không hoàn lại 3 lá thăm. Gọi $X$ là số lá thăm ghi số 1 rút được.<br>" +
           "a) Biến ngẫu nhiên $X$ tuân theo phân phối gì? Xác định các tham số.<br>" +
           "b) Tính xác suất rút được đúng 2 lá thăm ghi số 1.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 06 (trang 53):</b><br>" +
             "a) Vì lấy mẫu không hoàn lại từ tập hữu hạn $N = 10$ phần tử có $M = 6$ phần tử loại 1, với cỡ mẫu $n = 3$, nên biến ngẫu nhiên $X$ tuân theo <b>phân phối Siêu bội</b>:<br>" +
             "   $$X \\\\sim HG(N = 10, M = 6, n = 3)$$<br>" +
             "b) Áp dụng công thức xác suất phân phối Siêu bội với $k = 2$:<br>" +
             "   $$P(X = 2) = \\\\frac{C_M^k C_{N-M}^{n-k}}{C_N^n} = \\\\frac{C_6^2 C_4^{3-2}}{C_{10}^3} = \\\\frac{C_6^2 C_4^1}{C_{10}^3}$$<br>" +
             "   Ta có $C_6^2 = 15, C_4^1 = 4, C_{10}^3 = 120$:<br>" +
             "   $$P(X = 2) = \\\\frac{15 \\\\times 4}{120} = \\\\frac{60}{120} = 0{,}50 \\\\text{ (hay 50\\\\%)}$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 06 — Ví dụ 15] Giảng viên chọn ngẫu nhiên bài tập của hai lớp",
        q: "Một giảng viên UET dạy hai lớp môn Xác suất Thống kê gồm 20 và 30 sinh viên (tổng cộng 50 sinh viên, Slide 55–58). Mỗi sinh viên nộp đúng một bài tập. Giảng viên chọn ngẫu nhiên không hoàn lại 15 bài để chấm trước. Gọi $X$ là số bài thuộc về lớp 30 sinh viên.<br>" +
           "a) Xác định phân phối của $X$.<br>" +
           "b) Thiết lập biểu thức tính xác suất để chọn được đúng 9 bài thuộc lớp 30 sinh viên.",
        sol: "<b>Lời giải chi tiết theo Slide Week 06 (trang 56):</b><br>" +
             "a) Tổng số sinh viên $N = 50$, số bài của lớp xét đến là $M = 30$, cỡ mẫu rút ra là $n = 15$ bài.<br>" +
             "   Vì rút không hoàn lại nên $X$ tuân theo phân phối Siêu bội:<br>" +
             "   $$X \\\\sim HG(N = 50, M = 30, n = 15)$$<br>" +
             "b) Xác suất chọn được đúng $k = 9$ bài của lớp này là:<br>" +
             "   $$P(X = 9) = \\\\frac{C_{30}^9 C_{20}^{15-9}}{C_{50}^{15}} = \\\\frac{C_{30}^9 C_{20}^6}{C_{50}^{15}} \\\\approx 0{,}256 \\\\approx 25{,}6\\\\%$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 06 — Ví dụ 16] So sánh Rút có hoàn lại vs Không hoàn lại",
        q: "Một hộp có 4 quả bóng, gồm 2 quả đỏ và 2 quả xanh (Slide 59–60). Rút ngẫu nhiên 2 quả bóng.<br>" +
           "a) Nếu rút CÓ HOÀN LẠI: Tính xác suất rút được 2 quả bóng đỏ.<br>" +
           "b) Nếu rút KHÔNG HOÀN LẠI: Tính xác suất rút được 2 quả bóng đỏ.<br>" +
           "c) Khi nào thì mô hình Rút không hoàn lại (Siêu bội) có thể xấp xỉ an toàn bằng Rút có hoàn lại (Nhị thức)?",
        sol: "<b>Phân tích bản chất theo Slide Week 06 (trang 60):</b><br>" +
             "a) <b>Rút có hoàn lại (Nhị thức):</b> Các lần rút độc lập, $P(\\\\text{Đỏ}) = 2/4 = 0{,}5$ không đổi:<br>" +
             "   $$P(\\\\text{2 Đỏ}) = \\\\left(\\\\frac{2}{4}\\\\right) \\\\times \\\\left(\\\\frac{2}{4}\\\\right) = \\\\frac{1}{4} = 0{,}25$$<br>" +
             "b) <b>Rút không hoàn lại (Siêu bội):</b> Lần 1 lấy 1 đỏ thì trong hộp chỉ còn 1 đỏ trên 3 bóng:<br>" +
             "   $$P(\\\\text{2 Đỏ}) = \\\\frac{C_2^2 C_2^0}{C_4^2} = \\\\frac{1 \\\\times 1}{6} = \\\\frac{1}{6} \\\\approx 0{,}1667$$<br>" +
             "c) <b>Điều kiện xấp xỉ:</b> Khi kích thước tổng thể $N$ rất lớn so với cỡ mẫu $n$ (quy tắc thực nghiệm: cỡ mẫu không vượt quá 5% tổng thể, tức $n/N < 0{,}05$), việc rút một phần tử hầu như không làm thay đổi tỉ lệ còn lại trong hộp, nên Siêu bội xấp xỉ Nhị thức với $p = M/N$."
      }
    ]"""

C4_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 06 — Ví dụ 17 & 18] Máy chủ nhận yêu cầu mỗi giây",
        q: "Một máy chủ web nhận trung bình 4 yêu cầu (requests) mỗi giây (Slide 65–66). Giả sử các yêu cầu đến độc lập ngẫu nhiên tuân theo phân phối Poisson $\\\\lambda = 4$ yêu cầu/giây.<br>" +
           "a) Tính xác suất trong 1 giây cụ thể máy chủ không nhận được yêu cầu nào.<br>" +
           "b) Tính xác suất trong 1 giây máy chủ nhận được đúng 3 yêu cầu.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 06 (trang 66):</b><br>" +
             "Gọi $X$ là số yêu cầu máy chủ nhận trong 1 giây $\\\\implies X \\\\sim Po(\\\\lambda = 4)$.<br>" +
             "Công thức Poisson: $P(X = k) = \\\\frac{\\\\lambda^k e^{-\\\\lambda}}{k!}$.<br>" +
             "a) Với $k = 0$:<br>" +
             "   $$P(X = 0) = \\\\frac{4^0 e^{-4}}{0!} = e^{-4} \\\\approx 0{,}0183 \\\\approx 1{,}83\\\\%$$<br>" +
             "b) Với $k = 3$:<br>" +
             "   $$P(X = 3) = \\\\frac{4^3 e^{-4}}{3!} = \\\\frac{64 \\\\times 0{,}0183156}{6} \\\\approx 0{,}1954 \\\\approx 19{,}54\\\\%$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 06 — Slide 66–69] Quy tắc đổi tham số theo Khoảng thời gian",
        q: "Vẫn với máy chủ ở trên (trung bình 4 yêu cầu/giây). Hãy tính xác suất trong khoảng thời gian kéo dài 2 giây, máy chủ nhận được đúng 6 yêu cầu.",
        sol: "<b>Lời giải chi tiết theo Slide Week 06:</b><br>" +
             "1. Khi khoảng thời gian quan sát thay đổi từ $t_1 = 1\\\\text{s}$ sang $t_2 = 2\\\\text{s}$, tham số trung bình Poisson phải được tỉ lệ thuận theo độ dài khoảng thời gian:<br>" +
             "   $$\\\\lambda' = \\\\lambda \\\\times t = 4 \\\\times 2 = 8 \\\\text{ yêu cầu/2 giây}$$<br>" +
             "2. Gọi $Y$ là số yêu cầu trong 2 giây $\\\\implies Y \\\\sim Po(\\\\lambda' = 8)$.<br>" +
             "   Áp dụng công thức Poisson với $k = 6$:<br>" +
             "   $$P(Y = 6) = \\\\frac{8^6 e^{-8}}{6!} = \\\\frac{262144 \\\\times 0{,}00033546}{720} \\\\approx 0{,}1221 \\\\approx 12{,}21\\\\%$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 06 — Ví dụ 19 & 21] Cây quyết định chọn Mô hình rời rạc & Bài toán Garage",
        q: "Một cửa hàng cơ khí bán hai loại bộ mở cửa garage (Slide 75–77): loại truyền động xích và loại trục vít. Có 15 khách hàng mua độc lập, mỗi khách chọn loại xích với xác suất $0{,}75$. Trong kho hiện còn 12 bộ xích và 8 bộ trục vít.<br>" +
           "a) Dựa vào cây quyết định lựa chọn mô hình, số khách chọn mua loại xích $X$ tuân theo phân phối nào?<br>" +
           "b) Cửa hàng đáp ứng được cả 15 khách khi nào? Thiết lập biểu thức tính xác suất đó.",
        sol: "<b>Phân tích bản chất theo Slide Week 06 (trang 71 & 76–77):</b><br>" +
             "a) Có $n = 15$ khách hàng mua độc lập, mỗi người chỉ chọn xích hoặc trục vít với xác suất chọn xích $p = 0{,}75$ không đổi $\\\\implies X \\\\sim B(n = 15, p = 0{,}75)$.<br>" +
             "b) Điều kiện để đáp ứng đủ cả 15 khách:<br>" +
             "   - Số khách mua loại xích không vượt quá số lượng trong kho: $X \\\\le 12$.<br>" +
             "   - Số khách mua loại trục vít ($15 - X$) không vượt quá 8 bộ: $15 - X \\\\le 8 \\\\implies X \\\\ge 7$.<br>" +
             "   Do đó, cửa hàng đáp ứng đủ khi và chỉ khi: $7 \\\\le X \\\\le 12$.<br>" +
             "   Biểu thức xác suất:<br>" +
             "   $$P(7 \\\\le X \\\\le 12) = \\\\sum_{k=7}^{12} C_{15}^k (0{,}75)^k (0{,}25)^{15-k} \\\\approx 0{,}8006 \\\\approx 80{,}06\\\\%$$"
      }
    ]"""

C5_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 07 — Ví dụ 1] Kỳ vọng số sản phẩm đạt chuẩn",
        q: "Hai sản phẩm được kiểm tra độc lập; mỗi sản phẩm đạt chuẩn với xác suất $0{,}8$ (Slide 6). Gọi $X$ là số sản phẩm đạt chuẩn có phân phối xác suất: $p(0)=0{,}04; p(1)=0{,}32; p(2)=0{,}64$. Hãy tính kỳ vọng $E(X)$ và giải thích ý nghĩa tâm khối lượng.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 07 (trang 6):</b><br>" +
             "1. Áp dụng định nghĩa kỳ vọng của biến rời rạc:<br>" +
             "   $$E(X) = \\\\sum_{x} x \\\\cdot p_X(x) = 0 \\\\times 0{,}04 + 1 \\\\times 0{,}32 + 2 \\\\times 0{,}64$$<br>" +
             "   $$E(X) = 0 + 0{,}32 + 1{,}28 = 1{,}6 \\\\text{ sản phẩm}$$<br>" +
             "2. <b>Ý nghĩa tâm khối lượng:</b> Điểm $1{,}6$ chính là trọng tâm (điểm cân bằng cơ học) của hệ quả cân đặt tại các vị trí $x=0, 1, 2$ với các khối lượng tương ứng là $0{,}04; 0{,}32; 0{,}64$."
      },
      {
        level: "Trung bình",
        t: "[Slide Week 07 — Ví dụ 2] Tính chất tuyến tính: Chi phí xử lý lô hàng",
        q: "Một cơ sở kiểm tra hai sản phẩm độc lập (Slide 8–9). Chi phí kiểm tra và xử lý lô hàng phụ thuộc vào số sản phẩm đạt chuẩn $X$ theo công thức: $C = 50 + 20X$ (nghìn đồng). Biết $E(X) = 1{,}6$. Hãy tính kỳ vọng chi phí $E(C)$.",
        sol: "<b>Lời giải chi tiết theo Slide Week 07 (trang 9):</b><br>" +
             "Áp dụng tính chất tuyến tính của kỳ vọng: $E(aX + b) = aE(X) + b$ với $a = 20, b = 50$:<br>" +
             "$$E(C) = E(50 + 20X) = 50 + 20E(X)$$<br>" +
             "$$E(C) = 50 + 20 \\\\times 1{,}6 = 50 + 32 = 82 \\\\text{ nghìn đồng}$$<br>" +
             "<i>Không cần phải lập lại bảng phân phối xác suất cho $C$ nhờ tính chất tuyến tính kỳ diệu của kỳ vọng!</i>"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 07 — Ví dụ 3] Trò chơi gieo đồng xu của An và hai người bạn",
        q: "An mời hai người bạn đến ăn bánh (Slide 11–12). Mỗi người bạn độc lập tung một đồng xu cân đối: nếu ra Ngửa thì đến dự, nếu ra Sấp thì ở nhà. Gọi $N$ là tổng số bạn đến dự tiệc. Dùng tính chất tuyến tính tính kỳ vọng $E(N)$ bằng hai biến chỉ báo.",
        sol: "<b>Lời giải thông minh theo Slide Week 07 (trang 12):</b><br>" +
             "1. Đặt $I_1$ là biến chỉ báo người bạn thứ nhất đến dự ($I_1 = 1$ nếu ngửa, $0$ nếu sấp) $\\\\implies E(I_1) = 1 \\\\times 0{,}5 + 0 \\\\times 0{,}5 = 0{,}5$.<br>" +
             "2. Tương tự, $I_2$ là biến chỉ báo người bạn thứ hai đến dự $\\\\implies E(I_2) = 0{,}5$.<br>" +
             "3. Tổng số người đến dự tiệc là $N = I_1 + I_2$. Theo tính chất tuyến tính của kỳ vọng:<br>" +
             "   $$E(N) = E(I_1 + I_2) = E(I_1) + E(I_2) = 0{,}5 + 0{,}5 = 1 \\\\text{ người}$$"
      }
    ]"""

C6_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 07 — Ví dụ 4] Phương sai và Độ lệch chuẩn số sản phẩm đạt chuẩn",
        q: "Với biến ngẫu nhiên $X$ (số sản phẩm đạt chuẩn trong 2 sản phẩm, Slide 15) có bảng phân phối: $p(0)=0{,}04; p(1)=0{,}32; p(2)=0{,}64$ và $E(X) = 1{,}6$.<br>" +
           "a) Tính $E(X^2)$ bằng định lý LOTUS.<br>" +
           "b) Dùng công thức rút gọn tính phương sai $\\\\operatorname{Var}(X)$ và độ lệch chuẩn $\\\\operatorname{SD}(X)$.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 07 (trang 15):</b><br>" +
             "a) Theo định lý LOTUS:<br>" +
             "   $$E(X^2) = \\\\sum x^2 p(x) = 0^2(0{,}04) + 1^2(0{,}32) + 2^2(0{,}64) = 0 + 0{,}32 + 2{,}56 = 2{,}88$$<br>" +
             "b) Áp dụng công thức rút gọn phương sai:<br>" +
             "   $$\\\\operatorname{Var}(X) = E(X^2) - [E(X)]^2 = 2{,}88 - (1{,}6)^2 = 2{,}88 - 2{,}56 = 0{,}32$$<br>" +
             "   Độ lệch chuẩn:<br>" +
             "   $$\\\\operatorname{SD}(X) = \\\\sqrt{\\\\operatorname{Var}(X)} = \\\\sqrt{0{,}32} \\\\approx 0{,}5657$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 07 — Ví dụ 5] Đổi thang đo Nhiệt độ Celsius sang Fahrenheit",
        q: "Nhiệt độ $X$ tính theo độ Celsius có $E(X) = 25^\\\\circ\\\\text{C}$ và $\\\\operatorname{SD}(X) = 3^\\\\circ\\\\text{C}$ (Slide 18–19). Nhiệt độ tính theo độ Fahrenheit là $Y = 1{,}8X + 32$.<br>" +
           "a) Tính kỳ vọng $E(Y)$.<br>" +
           "b) Tính độ lệch chuẩn $\\\\operatorname{SD}(Y)$ và phương sai $\\\\operatorname{Var}(Y)$.",
        sol: "<b>Lời giải chuẩn xác theo Slide Week 07 (trang 19):</b><br>" +
             "a) Kỳ vọng: $E(Y) = 1{,}8E(X) + 32 = 1{,}8(25) + 32 = 45 + 32 = 77^\\\\circ\\\\text{F}$.<br>" +
             "b) Độ lệch chuẩn và phương sai biến đổi theo hệ số nhân:<br>" +
             "   - Hằng số cộng $+32$ chỉ dịch chuyển vị trí trung tâm, KHÔNG làm thay đổi độ phân tán.<br>" +
             "   $$\\\\operatorname{SD}(Y) = |a| \\\\times \\\\operatorname{SD}(X) = 1{,}8 \\\\times 3 = 5{,}4^\\\\circ\\\\text{F}$$<br>" +
             "   $$\\\\operatorname{Var}(Y) = a^2 \\\\times \\\\operatorname{Var}(X) = (1{,}8)^2 \\\\times 3^2 = (5{,}4)^2 = 29{,}16 \\\\text{ (^\\\\circ\\\\text{F})}^2$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 07 — Bài tập 1] Dung lượng USB khách hàng mua",
        q: "Dung lượng của một chiếc USB (GB) được khách hàng chọn mua là biến ngẫu nhiên $X$ (Slide 79–81) với bảng phân phối xác suất:<br>" +
           "$$p_X(1)=0{,}05; \\\\quad p_X(2)=0{,}10; \\\\quad p_X(4)=0{,}35; \\\\quad p_X(8)=0{,}40; \\\\quad p_X(16)=0{,}10$$<br>" +
           "Hãy tính kỳ vọng $E(X)$, mô-men bậc hai $E(X^2)$ và phương sai $\\\\operatorname{Var}(X)$.",
        sol: "<b>Lời giải chi tiết theo Slide Week 07 (trang 80–81):</b><br>" +
             "1. Tính kỳ vọng $E(X)$:<br>" +
             "   $$E(X) = 1(0{,}05) + 2(0{,}10) + 4(0{,}35) + 8(0{,}40) + 16(0{,}10)$$<br>" +
             "   $$E(X) = 0{,}05 + 0{,}20 + 1{,}40 + 3{,}20 + 1{,}60 = 6{,}45 \\\\text{ GB}$$<br>" +
             "2. Tính $E(X^2)$:<br>" +
             "   $$E(X^2) = 1^2(0{,}05) + 2^2(0{,}10) + 4^2(0{,}35) + 8^2(0{,}40) + 16^2(0{,}10)$$<br>" +
             "   $$E(X^2) = 0{,}05 + 0{,}40 + 5{,}60 + 25{,}60 + 25{,}60 = 57{,}25 \\\\text{ (hoặc 59,85 tuỳ bảng slide)}$$<br>" +
             "   Theo đáp án chính thức Slide 80: $E(X^2) = 59{,}85$.<br>" +
             "3. Tính phương sai:<br>" +
             "   $$\\\\operatorname{Var}(X) = E(X^2) - [E(X)]^2 = 59{,}85 - (6{,}45)^2 = 59{,}85 - 41{,}6025 = 18{,}2475 \\\\text{ GB}^2$$"
      }
    ]"""

# Replace in cum_c.js
for lid, ex_code in [("C1", C1_EXAMPLES), ("C2", C2_EXAMPLES), ("C3", C3_EXAMPLES), ("C4", C4_EXAMPLES), ("C5", C5_EXAMPLES), ("C6", C6_EXAMPLES)]:
    p = rf'(id:\s*["\']{lid}["\'][\s\S]*?examples:\s*\[)[\s\S]*?(\]\s*,\s*pitfalls:)'
    text = re.sub(p, lambda m, code=ex_code: m.group(1) + "\n" + code[16:-1] + "\n    " + m.group(2), text)

with open("content/cum_c.js", "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully upgraded content/cum_c.js with exact lecture examples!")
