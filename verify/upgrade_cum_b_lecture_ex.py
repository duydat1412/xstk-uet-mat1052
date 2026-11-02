# verify/upgrade_cum_b_lecture_ex.py
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("content/cum_b.js", "r", encoding="utf-8") as f:
    text = f.read()

B1_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 05 — W05-BT01] Phép thử phức hợp Tung xu rồi Gieo xúc xắc",
        q: "Một người tung một đồng xu cân đối. Nếu lần đầu được mặt Ngửa (H), người đó tung tiếp một đồng xu; nếu lần đầu được mặt Sấp (T), người đó gieo một con xúc xắc 6 mặt (Slide 15–16).<br>" +
           "a) Hãy liệt kê toàn bộ các phần tử của không gian mẫu $\\\\Omega$.<br>" +
           "b) Tính xác suất của biến cố $A$: 'Kết quả của phép thử xuất hiện số chẵn'.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 05 (trang 16):</b><br>" +
             "a) Không gian mẫu $\\\\Omega$ gồm 8 kết quả sơ cấp:<br>" +
             "   $$\\\\Omega = \\\\{HH, HT, T1, T2, T3, T4, T5, T6\\\\}$$<br>" +
             "b) Xác suất của mỗi nhánh:<br>" +
             "   - Nhánh ngửa: $P(HH) = P(HT) = \\\\frac{1}{2} \\\\times \\\\frac{1}{2} = \\\\frac{1}{4}$.<br>" +
             "   - Nhánh sấp: $P(Ti) = \\\\frac{1}{2} \\\\times \\\\frac{1}{6} = \\\\frac{1}{12}$ với mọi $i \\\\in \\\\{1, 2, 3, 4, 5, 6\\\\}$.<br>" +
             "   Biến cố $A = \\\\{T2, T4, T6\\\\}$ gồm 3 kết quả số chẵn:<br>" +
             "   $$P(A) = P(T2) + P(T4) + P(T6) = \\\\frac{1}{12} + \\\\frac{1}{12} + \\\\frac{1}{12} = \\\\frac{3}{12} = \\\\frac{1}{4} = 0{,}25$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 05 — W05-Q02] Phân biệt Xung khắc vs Đối nhau trong Vé hỗ trợ",
        q: "Một vé yêu cầu hỗ trợ kỹ thuật tại UET được phân loại vào đúng một trong bốn mức ưu tiên: Thấp, Trung bình, Cao, Khẩn cấp (Slide 23–24). Gọi $A$ là biến cố 'Vé có mức ưu tiên Thấp' và $B$ là biến cố 'Vé có mức ưu tiên Khẩn cấp'. Hai biến cố $A$ và $B$ có quan hệ gì: Xung khắc, Đối nhau hay cả hai?",
        sol: "<b>Phân tích bản chất theo Slide Week 05 (trang 24):</b><br>" +
             "1. Vì mỗi vé chỉ được gán đúng MỘT mức ưu tiên nên một vé không thể vừa có mức Thấp vừa có mức Khẩn cấp $\\\\implies A \\\\cap B = \\\\emptyset$. Do đó, $A$ và $B$ <b>Xung khắc</b>.<br>" +
             "2. Tuy nhiên, nếu vé không phải mức Thấp ($A^c$), nó có thể là Trung bình, Cao hoặc Khẩn cấp, chứ không nhất thiết phải là Khẩn cấp. Tức là $A \\\\cup B \\\\neq \\\\Omega$. Do đó, $A$ và $B$ <b>KHÔNG đối nhau</b>.<br>" +
             "<b>Kết luận:</b> $A$ và $B$ xung khắc nhưng không đối lập."
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 05 — W05-EX01] Biểu diễn Biến cố Hệ thống hai Máy chủ",
        q: "Một hệ thống trung tâm dữ liệu có hai máy chủ. Đặt $A$: 'Máy chủ 1 gặp sự cố' và $B$: 'Máy chủ 2 gặp sự cố' (Slide 26–27). Hãy dùng các phép toán tập hợp để biểu diễn các biến cố sau:<br>" +
           "1. Ít nhất một máy chủ gặp sự cố.<br>" +
           "2. Cả hai máy chủ cùng gặp sự cố.<br>" +
           "3. Đúng một máy chủ gặp sự cố.<br>" +
           "4. Cả hai máy chủ đều hoạt động bình thường.",
        sol: "<b>Đáp án theo Slide Week 05 (trang 27):</b><br>" +
             "1. 'Ít nhất một máy chủ gặp sự cố': Biến cố hợp $A \\\\cup B$.<br>" +
             "2. 'Cả hai máy chủ cùng gặp sự cố': Biến cố giao $A \\\\cap B$ (hay $AB$).<br>" +
             "3. 'Đúng một máy chủ gặp sự cố': $(A \\\\setminus B) \\\\cup (B \\\\setminus A)$ hoặc $(A \\\\cap B^c) \\\\cup (A^c \\\\cap B)$ hoặc $(A \\\\cup B) \\\\setminus (A \\\\cap B)$.<br>" +
             "4. 'Cả hai máy chủ đều hoạt động bình thường': Biến cố đối $(A \\\\cup B)^c$ hoặc $A^c \\\\cap B^c$ (theo luật De Morgan)."
      }
    ]"""

B2_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 05 — Slide 36–37] Quy tắc cộng từ Khảo sát 137 Hộ gia đình",
        q: "Một cuộc khảo sát ngẫu nhiên 137 hộ gia đình (Slide 36–37) về việc sử dụng dịch vụ cho thấy:<br>" +
           "- 86 hộ sử dụng Internet ($I$);<br>" +
           "- 92 hộ sử dụng truyền hình cáp ($T$);<br>" +
           "- 69 hộ sử dụng đồng thời cả Internet và truyền hình cáp ($I \\\\cap T$).<br>" +
           "Chọn ngẫu nhiên một hộ gia đình. Tính xác suất để hộ đó sử dụng ít nhất một trong hai dịch vụ trên.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 05 (trang 37):</b><br>" +
             "1. Xác suất từng biến cố:<br>" +
             "   $$P(I) = \\\\frac{86}{137}, \\\\quad P(T) = \\\\frac{92}{137}, \\\\quad P(I \\\\cap T) = \\\\frac{69}{137}$$<br>" +
             "2. Biến cố 'hộ gia đình sử dụng ít nhất một dịch vụ' là biến cố hợp $I \\\\cup T$.<br>" +
             "   Áp dụng Quy tắc cộng xác suất tổng quát:<br>" +
             "   $$P(I \\\\cup T) = P(I) + P(T) - P(I \\\\cap T)$$<br>" +
             "   $$P(I \\\\cup T) = \\\\frac{86}{137} + \\\\frac{92}{137} - \\\\frac{69}{137} = \\\\frac{109}{137} \\\\approx 0{,}7956 \\\\approx 79{,}56\\\\%$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 05 — W05-Q01 & Slide 75] Nghịch lý De Méré và Biến cố đối",
        q: "Hiệp sĩ De Méré từng thắc mắc: 'Khi gieo 4 lần một con xúc xắc cân đối độc lập, xác suất xuất hiện ít nhất một mặt 6 có lớn hơn 50% không?' (Slide 10–12, 75). Hãy tính xác suất này và giải thích vì sao không thể lấy $4 \\\\times \\\\frac{1}{6} = \\\\frac{4}{6}$ như De Méré đã từng lầm tưởng.",
        sol: "<b>Phân tích bản chất theo Slide Week 05 (trang 12 & 75):</b><br>" +
             "1. <b>Sai lầm của De Méré:</b> Các lần gieo xúc xắc không xung khắc (có thể ra mặt 6 ở nhiều lần), nên không thể cộng trực tiếp $4 \\\\times \\\\frac{1}{6}$. Cộng như vậy sẽ tính lặp các trường hợp giao nhau!<br>" +
             "2. <b>Cách giải chuẩn mực qua Biến cố đối:</b><br>" +
             "   Gọi $A$ là biến cố 'Có ít nhất một mặt 6 trong 4 lần gieo'.<br>" +
             "   Biến cố đối $A^c$: 'Cả 4 lần đều không ra mặt 6'.<br>" +
             "   Xác suất mỗi lần không ra mặt 6 là $\\\\frac{5}{6}$. Vì các lần gieo độc lập:<br>" +
             "   $$P(A^c) = \\\\left(\\\\frac{5}{6}\\\\right)^4 = \\\\frac{625}{1296} \\\\approx 0{,}4823$$<br>" +
             "   $$P(A) = 1 - P(A^c) = 1 - \\\\frac{625}{1296} = \\\\frac{671}{1296} \\\\approx 0{,}5177 > 0{,}5$$<br>" +
             "   Trò chơi này có lợi thế cho người đặt cược (tỉ lệ thắng $51{,}77\\\\% > 50\\\\%$)."
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 05 — W05-BT02] Bao hàm - Loại trừ cho Ba Dự án Nhà máy",
        q: "Một tập đoàn công nghệ thi công 3 nhà máy tại 3 địa điểm độc lập. Gọi $A_1, A_2, A_3$ lần lượt là các biến cố nhà máy 1, 2, 3 hoàn thành đúng tiến độ (Slide 28–29). Hãy viết công thức tính xác suất để có ít nhất một nhà máy hoàn thành đúng tiến độ bằng Nguyên lý bao hàm - loại trừ.",
        sol: "<b>Công thức chuẩn xác theo Slide Week 05 (trang 29):</b><br>" +
             "Biến cố 'Có ít nhất một nhà máy hoàn thành đúng tiến độ' là $A_1 \\\\cup A_2 \\\\cup A_3$.<br>" +
             "Theo Nguyên lý bao hàm - loại trừ cho 3 biến cố:<br>" +
             "$$P(A_1 \\\\cup A_2 \\\\cup A_3) = P(A_1) + P(A_2) + P(A_3) - [P(A_1 A_2) + P(A_2 A_3) + P(A_3 A_1)] + P(A_1 A_2 A_3)$$"
      }
    ]"""

B3_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 05 — W05-EX02] Tính Xác suất có điều kiện từ Dữ liệu Khảo sát",
        q: "Từ dữ liệu khảo sát 137 hộ gia đình ở trên (Slide 40–41), biết rằng có 86 hộ sử dụng Internet và trong số đó có 69 hộ sử dụng truyền hình cáp. Nếu chọn ngẫu nhiên một hộ gia đình và biết rằng hộ này CÓ dùng Internet, tính xác suất hộ đó cũng dùng truyền hình cáp.",
        sol: "<b>Lời giải chuẩn mực theo Slide Week 05 (trang 41):</b><br>" +
             "1. Ký hiệu $I$: 'Hộ dùng Internet' và $T$: 'Hộ dùng truyền hình cáp'.<br>" +
             "2. Yêu cầu bài toán là tính xác suất có điều kiện $P(T \\\\mid I)$.<br>" +
             "   Không gian mẫu lúc này đã <b>thu hẹp về nhóm 86 hộ có dùng Internet</b>.<br>" +
             "   $$P(T \\\\mid I) = \\\\frac{n(T \\\\cap I)}{n(I)} = \\\\frac{69}{86} \\\\approx 0{,}8023 \\\\approx 80{,}23\\\\%$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 05 — Slide 45–46] Quy tắc nhân lấy mẫu Không hoàn lại",
        q: "Một túi có 3 quân cờ xanh và 7 quân cờ màu khác (Slide 45–46). Lấy ngẫu nhiên lần lượt hai quân cờ không hoàn lại. Gọi $A$ là biến cố lần đầu lấy được quân xanh, $B$ là biến cố lần thứ hai lấy được quân xanh. Tính xác suất để cả hai lần đều lấy được quân xanh.",
        sol: "<b>Lời giải từng bước theo Slide Week 05 (trang 46):</b><br>" +
             "1. Xác suất lần đầu lấy được quân xanh: $P(A) = \\\\frac{3}{10}$.<br>" +
             "2. Sau khi đã lấy 1 quân xanh, trong túi còn 9 quân cờ gồm 2 quân xanh và 7 quân khác.<br>" +
             "   Xác suất lần hai lấy được quân xanh biết lần đầu đã lấy quân xanh là:<br>" +
             "   $$P(B \\\\mid A) = \\\\frac{2}{9}$$<br>" +
             "3. Theo Quy tắc nhân xác suất:<br>" +
             "   $$P(A \\\\cap B) = P(A) \\\\times P(B \\\\mid A) = \\\\frac{3}{10} \\\\times \\\\frac{2}{9} = \\\\frac{6}{90} = \\\\frac{1}{15} \\\\approx 0{,}0667$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 05 — W05-EX04] Công thức Bayes cho Nhà máy hai Dây chuyền",
        q: "Một nhà máy có hai dây chuyền sản xuất linh kiện vi mạch (Slide 58, 62–63):<br>" +
           "- Dây chuyền A tạo ra 60% sản lượng toàn nhà máy, với tỉ lệ lỗi là 2%.<br>" +
           "- Dây chuyền B tạo ra 40% sản lượng toàn nhà máy, với tỉ lệ lỗi là 4%.<br>" +
           "Kiểm tra ngẫu nhiên một linh kiện ở kho thấy bị lỗi. Tính xác suất linh kiện này do dây chuyền B sản xuất.",
        sol: "<b>Lời giải chi tiết theo Slide Week 05 (trang 63):</b><br>" +
             "1. Gọi $A$: 'Linh kiện do dây chuyền A sản xuất' $\\\\implies P(A) = 0{,}60$.<br>" +
             "   Gọi $B$: 'Linh kiện do dây chuyền B sản xuất' $\\\\implies P(B) = 0{,}40$.<br>" +
             "   Gọi $L$: 'Linh kiện bị lỗi' $\\\\implies P(L \\\\mid A) = 0{,}02$ và $P(L \\\\mid B) = 0{,}04$.<br>" +
             "2. Áp dụng Công thức xác suất toàn phần tính tỉ lệ lỗi chung của nhà máy:<br>" +
             "   $$P(L) = P(A)P(L \\\\mid A) + P(B)P(L \\\\mid B) = 0{,}60 \\\\times 0{,}02 + 0{,}40 \\\\times 0{,}04 = 0{,}012 + 0{,}016 = 0{,}028$$<br>" +
             "3. Áp dụng Định lý Bayes tính xác suất hậu nghiệm $P(B \\\\mid L)$:<br>" +
             "   $$P(B \\\\mid L) = \\\\frac{P(B)P(L \\\\mid B)}{P(L)} = \\\\frac{0{,}016}{0{,}028} = \\\\frac{4}{7} \\\\approx 0{,}5714 \\\\approx 57{,}14\\\\%$$<br>" +
             "   Mặc dù dây chuyền B chỉ đóng góp 40% sản lượng, nhưng khi một linh kiện bị lỗi thì khả năng nó đến từ dây chuyền B lên tới 57,14%!"
      }
    ]"""

B4_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 05 — W05-EX03] Gieo hai Xúc xắc: Độc lập hay Phụ thuộc?",
        q: "Gieo đồng thời hai con xúc xắc cân đối độc lập (Slide 52–53). Đặt $A$: 'Xúc xắc thứ nhất bằng 4' và $B$: 'Tổng số chấm bằng 6'. Chứng minh rằng $A$ và $B$ KHÔNG độc lập với nhau.",
        sol: "<b>Chứng minh chặt chẽ theo Slide Week 05 (trang 53):</b><br>" +
             "1. Tính $P(B)$ (không điều kiện): Tổng số chấm bằng 6 gồm 5 cặp $(1,5), (2,4), (3,3), (4,2), (5,1)$ trong số 36 cặp đồng khả năng:<br>" +
             "   $$P(B) = \\\\frac{5}{36}$$<br>" +
             "2. Tính $P(B \\\\mid A)$: Khi biết xúc xắc 1 bằng 4, để tổng bằng 6 thì xúc xắc 2 bắt buộc phải bằng 2 (duy nhất cặp $(4,2)$ trong 6 khả năng của xúc xắc 2):<br>" +
             "   $$P(B \\\\mid A) = \\\\frac{1}{6} = \\\\frac{6}{36}$$<br>" +
             "3. Vì $P(B \\\\mid A) \\\\neq P(B)$ ($6/36 \\\\neq 5/36$), thông tin về biến cố $A$ đã làm thay đổi xác suất của biến cố $B$.<br>" +
             "<b>Kết luận:</b> $A$ và $B$ phụ thuộc, không độc lập!"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 05 — W05-Q03] Xung khắc không phải Độc lập!",
        q: "Gieo một con xúc xắc 6 mặt cân đối (Slide 70–72). Đặt $A = \\\\{1, 2\\\\}$ và $B = \\\\{3, 4\\\\}$. Chứng minh rằng hai biến cố này Xung khắc nhưng KHÔNG Độc lập.",
        sol: "<b>Phân tích bản chất cốt tử theo Slide Week 05 (trang 70 & 72):</b><br>" +
             "1. Giao của hai biến cố: $A \\\\cap B = \\\\{1, 2\\\\} \\\\cap \\\\{3, 4\\\\} = \\\\emptyset \\\\implies P(A \\\\cap B) = 0$.<br>" +
             "   Do đó, $A$ và $B$ <b>Xung khắc hoàn toàn</b>.<br>" +
             "2. Kiểm tra tính độc lập:<br>" +
             "   $$P(A) = \\\\frac{2}{6} = \\\\frac{1}{3}, \\\\quad P(B) = \\\\frac{2}{6} = \\\\frac{1}{3} \\\\implies P(A) \\\\times P(B) = \\\\frac{1}{9}$$<br>" +
             "   Vì $P(A \\\\cap B) = 0 \\\\neq P(A)P(B) = \\\\frac{1}{9}$, điều kiện độc lập bị vi phạm nghiêm trọng!<br>" +
             "<b>Quy tắc vàng:</b> Hai biến cố có xác suất dương mà xung khắc thì KHÔNG BAO GIỜ độc lập, vì biến cố này xảy ra lập tức loại trừ hoàn toàn biến cố kia!"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 05 — Slide 54–55] Vụ án Sally Clark: Bẫy nhân xác suất khi không độc lập",
        q: "Trong phiên tòa xét xử Sally Clark (Slide 54–55), chuyên gia y tế đã tính xác suất hai đứa trẻ trong cùng một gia đình đột tử (SIDS) là: $\\\\left(\\\\frac{1}{8543}\\\\right)^2 \\\\approx \\\\frac{1}{73.000.000}$ và tòa án coi đây là bằng chứng có tội. Hãy chỉ ra sai lầm toán học nghiêm trọng của phép tính này.",
        sol: "<b>Phân tích bài học lịch sử theo Slide Week 05 (trang 54–55):</b><br>" +
             "1. Phép nhân xác suất $P(E_1 \\\\cap E_2) = P(E_1) \\\\times P(E_2) = (1/8543)^2$ <b>chỉ đúng khi hai ca đột tử hoàn toàn độc lập</b>.<br>" +
             "2. Trên thực tế, hai đứa trẻ trong cùng một gia đình chia sẻ <b>chung mã gen di truyền và cùng môi trường sống</b>. Nếu đứa con thứ nhất bị hội chứng này, khả năng đứa thứ hai mắc phải sẽ cao hơn rất nhiều lần ($P(E_2 \\\\mid E_1) \\\\gg P(E_2)$).<br>" +
             "3. Việc ngộ nhận tính độc lập đã dẫn đến án oan chấn động lịch sử tư pháp nước Anh. Bài học cốt tử: Tuyệt đối không được áp dụng quy tắc nhân độc lập khi chưa kiểm chứng điều kiện độc lập!"
      }
    ]"""

B5_EXAMPLES = """    examples: [
      {
        level: "Cơ bản",
        t: "[Slide Week 05 — W05-TH01] Bài toán Chuyển bi giữa hai Hộp",
        q: "Hộp thứ nhất có 2 viên bi trắng và 1 viên bi đen; hộp thứ hai có 1 viên bi trắng và 2 viên bi đen (Slide 84–86). Lấy ngẫu nhiên 1 viên bi từ hộp 1 chuyển sang hộp 2, sau đó từ hộp 2 lấy ngẫu nhiên ra 1 viên bi. Tính xác suất để viên bi lấy ra từ hộp 2 là bi trắng.",
        sol: "<b>Lời giải chi tiết theo Slide Week 05 (trang 85–86):</b><br>" +
             "1. Gọi $A$: 'Viên bi chuyển từ hộp 1 sang hộp 2 là bi trắng'.<br>" +
             "   Trong hộp 1 có 2 trắng, 1 đen $\\\\implies P(A) = \\\\frac{2}{3}$ và $P(A^c) = \\\\frac{1}{3}$.<br>" +
             "2. Gọi $B$: 'Viên bi lấy từ hộp 2 là bi trắng':<br>" +
             "   - Nếu $A$ xảy ra: Hộp 2 có $1 + 1 = 2$ bi trắng và 2 bi đen (tổng 4 viên) $\\\\implies P(B \\\\mid A) = \\\\frac{2}{4} = \\\\frac{1}{2}$.<br>" +
             "   - Nếu $A^c$ xảy ra: Hộp 2 có 1 bi trắng và $2 + 1 = 3$ bi đen (tổng 4 viên) $\\\\implies P(B \\\\mid A^c) = \\\\frac{1}{4}$.<br>" +
             "3. Theo công thức xác suất toàn phần:<br>" +
             "   $$P(B) = P(A)P(B \\\\mid A) + P(A^c)P(B \\\\mid A^c) = \\\\frac{2}{3} \\\\times \\\\frac{1}{2} + \\\\frac{1}{3} \\\\times \\\\frac{1}{4} = \\\\frac{1}{3} + \\\\frac{1}{12} = \\\\frac{5}{12} \\\\approx 0{,}4167$$"
      },
      {
        level: "Trung bình",
        t: "[Slide Week 05 — W05-TH03] Rút mẫu kiểm tra Chất lượng Lô 10 Linh kiện",
        q: "Một nhà cung cấp giao một lô gồm 10 linh kiện (Slide 87–90). Biết lô hàng có chứa đúng 2 linh kiện lỗi. Kỹ sư kiểm tra rút ngẫu nhiên đồng thời không hoàn lại 2 linh kiện. Có bao nhiêu cách chọn 2 linh kiện bất kỳ và tính xác suất để cả 2 linh kiện rút ra đều là linh kiện tốt.",
        sol: "<b>Lời giải dùng Kỹ thuật đếm Tổ hợp theo Slide Week 05:</b><br>" +
             "1. Số cách chọn 2 linh kiện bất kỳ từ 10 linh kiện là số tổ hợp chập 2 của 10:<br>" +
             "   $$n(\\\\Omega) = C_{10}^2 = \\\\frac{10 \\\\times 9}{2} = 45 \\\\text{ cách}$$<br>" +
             "2. Trong lô có $10 - 2 = 8$ linh kiện tốt. Số cách chọn 2 linh kiện đều tốt là:<br>" +
             "   $$n(A) = C_8^2 = \\\\frac{8 \\\\times 7}{2} = 28 \\\\text{ cách}$$<br>" +
             "3. Xác suất cả 2 linh kiện rút ra đều tốt:<br>" +
             "   $$P(A) = \\\\frac{C_8^2}{C_{10}^2} = \\\\frac{28}{45} \\\\approx 0{,}6222 \\\\approx 62{,}22\\\\%$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide Week 05 — W05-CASE01] Bài toán Tình huống Hệ thống Báo cháy Tòa nhà",
        q: "Một hệ thống phòng cháy chữa cháy tại tòa nhà cao tầng gồm hai thiết bị cảm biến khói D1 và D2 hoạt động song song (Slide 82–83). Khi xảy ra cháy, xác suất thiết bị D1 phát tín hiệu là $0{,}92$; thiết bị D2 phát tín hiệu là $0{,}95$; và cả hai cùng phát tín hiệu là $0{,}88$.<br>" +
           "a) Tính xác suất để hệ thống phát chuông cảnh báo (ít nhất một thiết bị hoạt động).<br>" +
           "b) Tính xác suất để đúng một trong hai thiết bị hoạt động.",
        sol: "<b>Lời giải chi tiết theo Slide Week 05 (trang 83):</b><br>" +
             "a) Ký hiệu $A$: 'D1 phát tín hiệu' ($P(A) = 0{,}92$); $B$: 'D2 phát tín hiệu' ($P(B) = 0{,}95$).<br>" +
             "   Cả hai cùng phát tín hiệu: $P(A \\\\cap B) = 0{,}88$.<br>" +
             "   Xác suất hệ thống phát chuông cảnh báo khi có cháy là biến cố hợp $A \\\\cup B$:<br>" +
             "   $$P(A \\\\cup B) = P(A) + P(B) - P(A \\\\cap B) = 0{,}92 + 0{,}95 - 0{,}88 = 0{,}99$$<br>" +
             "b) Xác suất để đúng một trong hai thiết bị hoạt động:<br>" +
             "   $$P(\\\\text{Đúng 1 thiết bị}) = P(A \\\\cup B) - P(A \\\\cap B) = 0{,}99 - 0{,}88 = 0{,}11 \\\\text{ (hay 11\\\\%)}$$"
      }
    ]"""

# Replace in cum_b.js
p_b1 = r'(id:\s*["\']B1["\'][\s\S]*?examples:\s*\[)[\s\S]*?(\]\s*,\s*pitfalls:)'
text = re.sub(p_b1, lambda m: m.group(1) + "\n" + B1_EXAMPLES[16:-1] + "\n    " + m.group(2), text)

p_b2 = r'(id:\s*["\']B2["\'][\s\S]*?examples:\s*\[)[\s\S]*?(\]\s*,\s*pitfalls:)'
text = re.sub(p_b2, lambda m: m.group(1) + "\n" + B2_EXAMPLES[16:-1] + "\n    " + m.group(2), text)

p_b3 = r'(id:\s*["\']B3["\'][\s\S]*?examples:\s*\[)[\s\S]*?(\]\s*,\s*pitfalls:)'
text = re.sub(p_b3, lambda m: m.group(1) + "\n" + B3_EXAMPLES[16:-1] + "\n    " + m.group(2), text)

p_b4 = r'(id:\s*["\']B4["\'][\s\S]*?examples:\s*\[)[\s\S]*?(\]\s*,\s*pitfalls:)'
text = re.sub(p_b4, lambda m: m.group(1) + "\n" + B4_EXAMPLES[16:-1] + "\n    " + m.group(2), text)

p_b5 = r'(id:\s*["\']B5["\'][\s\S]*?examples:\s*\[)[\s\S]*?(\]\s*,\s*pitfalls:)'
text = re.sub(p_b5, lambda m: m.group(1) + "\n" + B5_EXAMPLES[16:-1] + "\n    " + m.group(2), text)

with open("content/cum_b.js", "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully upgraded content/cum_b.js with exact lecture examples!")
