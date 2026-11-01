/* Ngân hàng câu hỏi trắc nghiệm XSTK UET MAT1052 - Phase 4 */
window.TRAC_NGHIEM_DATA = [
  {
    "id": "TN1_01",
    "topicId": 1,
    "topicName": "Dữ liệu & Thống kê mô tả",
    "level": "Cơ bản",
    "question": "Trong một nghiên cứu về sinh viên đại học, các biến số sau được thu thập: (1) Mã số sinh viên, (2) Điểm rèn luyện xếp loại (Xuất sắc, Tốt, Khá, Trung bình), (3) Số tín chỉ đã tích lũy, (4) Thời gian tự học mỗi tuần (giờ). Các biến này lần lượt thuộc loại nào?",
    "options": [
      "Định tính danh nghĩa (Nominal), Định tính thứ bậc (Ordinal), Định lượng rời rạc, Định lượng liên tục",
      "Định lượng rời rạc, Định tính thứ bậc, Định lượng rời rạc, Định lượng liên tục",
      "Định tính danh nghĩa, Định tính danh nghĩa, Định lượng liên tục, Định lượng rời rạc",
      "Định tính thứ bậc, Định tính thứ bậc, Định lượng rời rạc, Định lượng liên tục"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì:\n- (1) Mã số sinh viên là nhãn định danh, các con số không dùng để cộng trừ nhân chia hay so sánh lớn bé -> Định tính danh nghĩa (Nominal).\n- (2) Điểm rèn luyện có thứ tự tự nhiên (Xuất sắc > Tốt > Khá > Trung bình) nhưng khoảng cách giữa các mức không đo đếm bằng số -> Định tính thứ bậc (Ordinal).\n- (3) Số tín chỉ tích lũy chỉ nhận các giá trị nguyên không âm 0, 1, 2, 3... đếm được -> Định lượng rời rạc (Discrete numeric).\n- (4) Thời gian tự học có thể nhận bất kỳ giá trị thực nào trên một khoảng (ví dụ 12,35 giờ) -> Định lượng liên tục (Continuous numeric).\n\nPhân tích bẫy sai:\n- Phương án B: Sai vì nhầm Mã số sinh viên là định lượng do nó ghi bằng các chữ số.\n- Phương án C: Sai vì xếp loại rèn luyện có quan hệ thứ bậc rõ ràng, không thể là danh nghĩa thuần túy.\n- Phương án D: Sai vì mã số sinh viên không có thứ bậc ưu tiên nào.",
    "source": "Stat20 Mục 1.1 - 1.2"
  },
  {
    "id": "TN1_02",
    "topicId": 1,
    "topicName": "Dữ liệu & Thống kê mô tả",
    "level": "Cơ bản",
    "question": "Một bảng dữ liệu ghi lại thông tin tiêm chủng của 500 trẻ em tại một trung tâm y tế, mỗi dòng tương ứng với một trẻ, các cột gồm: Họ tên, Ngày sinh, Cân nặng, Chiều cao, Tình trạng tiêm chủng. Theo chuẩn cấu trúc dữ liệu gọn gàng (tidy data frame), phát biểu nào sau đây là ĐÚNG?",
    "options": [
      "Đơn vị quan sát là toàn bộ trung tâm y tế, và số quan sát là 5",
      "Đơn vị quan sát (observational unit) là từng trẻ em, và mỗi cột là một biến số (variable)",
      "Mỗi dòng là một biến số và mỗi cột là một đơn vị quan sát",
      "Đơn vị quan sát là các lần tiêm chủng và kích thước mẫu là 5 x 500 = 2500"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì theo định nghĩa bảng dữ liệu tidy (Stat20 Ch.1): mỗi dòng đại diện cho một đơn vị quan sát cá thể (ở đây là một trẻ em), mỗi cột đại diện cho một đặc trưng đo lường (biến số), và mỗi ô là một giá trị duy nhất.\n\nPhân tích bẫy sai:\n- Phương án A: Sai vì trung tâm y tế là bối cảnh thu thập, không phải đơn vị đo lường cơ sở.\n- Phương án C: Nhầm lẫn ngược hoàn toàn giữa khái niệm dòng (quan sát) và cột (biến số).\n- Phương án D: Dữ liệu ghi thông tin từng trẻ chứ không phải từng mũi tiêm lặp lại.",
    "source": "Stat20 Mục 1.2"
  },
  {
    "id": "TN1_03",
    "topicId": 1,
    "topicName": "Dữ liệu & Thống kê mô tả",
    "level": "Cơ bản",
    "question": "Một công ty công nghệ có 100 nhân viên. Thu nhập bình quân (mean) là 35 triệu đồng/tháng, nhưng trung vị (median) chỉ là 18 triệu đồng/tháng. Nhận định nào sau đây là CHÍNH XÁC NHẤT về hình dạng phân phối thu nhập của công ty?",
    "options": [
      "Phân phối lệch trái (Left-skewed) do phần lớn nhân viên có mức lương cao hơn trung bình",
      "Phân phối hoàn toàn đối xứng hình chuông vì số lượng nhân viên đủ lớn (n = 100)",
      "Phân phối lệch phải (Right-skewed) do có một số ít nhân viên cấp cao hoặc chuyên gia nhận mức lương cực cao kéo giá trị trung bình lên",
      "Dữ liệu bị lỗi thu thập vì trung bình luôn luôn phải xấp xỉ bằng trung vị"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì khi $\\text{Mean} (35) > \\text{Median} (18)$, phân phối có đuôi dài kéo về phía giá trị lớn (phía bên phải), gọi là phân phối lệch phải (right-skewed). Các giá trị cực lớn (như lương của ban giám đốc vài trăm triệu) kéo mạnh giá trị Mean lên cao, trong khi Median không bị ảnh hưởng (bền vững).\n\nPhân tích bẫy sai:\n- Phương án A: Sai vì phân phối lệch trái có $\\text{Mean} < \\text{Median}$ (đuôi dài bên trái kéo Mean xuống).\n- Phương án B: Sai vì số lượng $n=100$ không đảm bảo dữ liệu gốc có dạng hình chuông đối xứng (nhất là biến thu nhập luôn lệch phải).\n- Phương án D: Sai vì Mean và Median chỉ bằng nhau khi phân phối đối xứng hoàn hảo.",
    "source": "Stat20 Mục 2.4; Slide Week 07 tr. 5"
  },
  {
    "id": "TN1_04",
    "topicId": 1,
    "topicName": "Dữ liệu & Thống kê mô tả",
    "level": "Trung bình",
    "question": "Cho mẫu số liệu đã sắp xếp: 3, 5, 7, 8, 9, 11, 15, 16, 20. Khoảng tứ phân vị (IQR) của mẫu dữ liệu này bằng bao nhiêu (theo phương pháp tách trung vị phổ biến trong giáo trình)?",
    "options": [
      "15,5",
      "6",
      "17",
      "9,5"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì:\n- Số quan sát $n=9$ (lẻ), giá trị chính giữa ở vị trí thứ 5 là $\\text{Median} = Q_2 = 9$.\n- Nửa dưới gồm 4 số: [3, 5, 7, 8] $\\implies Q_1 = \\frac{5 + 7}{2} = 6,0$.\n- Nửa trên gồm 4 số: [11, 15, 16, 20] $\\implies Q_3 = \\frac{15 + 16}{2} = 15,5$.\n- Khoảng tứ phân vị $\\text{IQR} = Q_3 - Q_1 = 15,5 - 6,0 = 9,5$.\n\nPhân tích bẫy sai:\n- Phương án A: Sai do nhầm $\\text{IQR}$ chính là $Q_3 = 15,5$.\n- Phương án B: Sai do nhầm $\\text{IQR}$ là $Q_1 = 6,0$.\n- Phương án C: 17 là khoảng biến thiên toàn phần $\\text{Range} = 20 - 3 = 17$, không phải khoảng tứ phân vị.",
    "source": "Stat20 Mục 2.4"
  },
  {
    "id": "TN1_05",
    "topicId": 1,
    "topicName": "Dữ liệu & Thống kê mô tả",
    "level": "Cơ bản",
    "question": "Một mẫu dữ liệu có tứ phân vị thứ nhất $Q_1 = 10$ và tứ phân vị thứ ba $Q_3 = 22$. Theo tiêu chuẩn 1,5×IQR của Tukey, một giá trị $x$ được coi là ngoại lai (outlier) nếu nằm ngoài khoảng nào?",
    "options": [
      "[-8; 40]",
      "[4; 28]",
      "[10; 22]",
      "[-2; 34]"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì:\n- Khoảng tứ phân vị: $\\text{IQR} = Q_3 - Q_1 = 22 - 10 = 12$.\n- Hàng rào dưới (Lower Fence): $Q_1 - 1,5 \\cdot \\text{IQR} = 10 - 1,5 \\cdot 12 = 10 - 18 = -8$.\n- Hàng rào trên (Upper Fence): $Q_3 + 1,5 \\cdot \\text{IQR} = 22 + 1,5 \\cdot 12 = 22 + 18 = 40$.\n- Do đó, giá trị $x$ nằm ngoài khoảng $[-8; 40]$ ($x < -8$ hoặc $x > 40$) là ngoại lai.\n\nPhân tích bẫy sai:\n- Phương án B: Nhầm công thức thành $[Q_1 - 0,5 \\cdot \\text{IQR}; Q_3 + 0,5 \\cdot \\text{IQR}] = [4; 28]$.\n- Phương án C: Đây chỉ là hộp $[Q_1; Q_3]$, chứa 50% dữ liệu trung tâm chứ không phải rào ngoại lai.\n- Phương án D: Tính nhầm $1 \\cdot \\text{IQR}$ thay vì $1,5 \\cdot \\text{IQR}$ ($10 - 12 = -2; 22 + 12 = 34$).",
    "source": "Stat20 Mục 2.4; Slide Week 07 tr. 5"
  },
  {
    "id": "TN1_06",
    "topicId": 1,
    "topicName": "Dữ liệu & Thống kê mô tả",
    "level": "Cơ bản",
    "question": "Khi trong tập dữ liệu xuất hiện một vài điểm ngoại lai cực kỳ lớn (do sai sót gõ nhầm thêm hai chữ số 0 vào cuối), cặp đại lượng thống kê nào sau đây ít bị ảnh hưởng nhất (có tính bền vững - robust)?",
    "options": [
      "Trung bình (Mean) và Độ lệch chuẩn (SD)",
      "Trung vị (Median) và Khoảng tứ phân vị (IQR)",
      "Trung bình (Mean) và Trung vị (Median)",
      "Khoảng biến thiên (Range) và Phương sai (Variance)"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì Trung vị và IQR dựa trên thứ tự xếp hạng vị trí của dữ liệu nên không bị kéo bởi giá trị số học của các điểm cực trị (tính bền vững cao). Ngược lại, Mean, Phương sai, Độ lệch chuẩn và Range đều phụ thuộc trực tiếp vào từng giá trị số học, do đó bị bóp méo dữ dội khi có ngoại lai.\n\nPhân tích bẫy sai:\n- Phương án A: Mean và SD là các đại lượng cực kỳ nhạy cảm (non-robust).\n- Phương án C: Chứa Mean là đại lượng không bền vững.\n- Phương án D: Range lấy $(\\max - \\min)$ nên bị ảnh hưởng trực tiếp 100% bởi ngoại lai.",
    "source": "Stat20 Mục 2.4"
  },
  {
    "id": "TN1_07",
    "topicId": 1,
    "topicName": "Dữ liệu & Thống kê mô tả",
    "level": "Cơ bản",
    "question": "Một mẫu số liệu $X$ có độ lệch chuẩn mẫu bằng $s_X = 4$. Nếu ta biến đổi từng quan sát theo công thức $Y = -3X + 5$, thì độ lệch chuẩn mẫu $s_Y$ của biến mới $Y$ bằng bao nhiêu?",
    "options": [
      "-12",
      "-7",
      "12",
      "36"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì theo tính chất biến đổi tuyến tính của độ lệch chuẩn mẫu: $s_{aX+b} = |a| \\cdot s_X$.\nỞ đây $a = -3$ và $b = 5$, suy ra: $s_Y = |-3| \\cdot 4 = 3 \\cdot 4 = 12$.\n\nPhân tích bẫy sai:\n- Phương án A: Độ lệch chuẩn luôn là đại lượng không âm ($s \\ge 0$), không bao giờ nhận giá trị âm -12.\n- Phương án B: Nhầm lẫn tính toán $-3 \\cdot 4 + 5 = -7$ (áp dụng quy tắc kỳ vọng cho độ lệch chuẩn).\n- Phương án D: 36 là phương sai mẫu $s_Y^2 = a^2 s_X^2 = 9 \\cdot 16 = 144$ (hoặc nhầm $a^2 s_X = 9 \\cdot 4 = 36$).",
    "source": "Stat20 Mục 2.4; Slide Week 07 tr. 9"
  },
  {
    "id": "TN1_08",
    "topicId": 1,
    "topicName": "Dữ liệu & Thống kê mô tả",
    "level": "Trung bình",
    "question": "Khảo sát 200 sinh viên về việc tham gia CLB học thuật và kết quả môn học: Trong 100 sinh viên có tham gia CLB, có 80 bạn đạt điểm A/B và 20 bạn đạt điểm dưới B. Trong 100 sinh viên không tham gia CLB, có 60 bạn đạt điểm A/B và 40 bạn đạt điểm dưới B. Tỷ lệ sinh viên đạt điểm A/B trong nhóm có tham gia CLB và tỷ lệ sinh viên có tham gia CLB trong nhóm đạt điểm A/B lần lượt là:",
    "options": [
      "80% và 40%",
      "40% và 80%",
      "57,14% và 80%",
      "80% và 57,14%"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì:\n- Tỷ lệ đạt điểm A/B trong nhóm có tham gia CLB là xác suất có điều kiện: $P(A/B \\mid CLB) = \\frac{80}{100} = 80\\%$.\n- Tỷ lệ tham gia CLB trong nhóm đạt điểm A/B: Nhóm đạt A/B có tổng cộng $80 + 60 = 140$ sinh viên. Do đó: $P(CLB \\mid A/B) = \\frac{80}{140} = \\frac{4}{7} \\approx 57,14\\%$.\n\nPhân tích bẫy sai:\n- Phương án A: Sai do tính $P(CLB \\mid A/B) = 80/200 = 40\\%$ (chia cho toàn thể thay vì chia cho nhóm A/B).\n- Phương án B: Đảo ngược hai thứ tự câu hỏi và nhầm mẫu số.\n- Phương án C: Đảo ngược thứ tự của hai câu hỏi.",
    "source": "Stat20 Mục 2.2"
  },
  {
    "id": "TN1_09",
    "topicId": 1,
    "topicName": "Dữ liệu & Thống kê mô tả",
    "level": "Cơ bản",
    "question": "Phát biểu nào sau đây về hệ số tương quan tuyến tính Pearson $r$ là ĐÚNG?",
    "options": [
      "$-1 \\le r \\le 1$; nếu đổi đơn vị đo của $X$ từ mét sang xentimét thì giá trị của $r$ không hề thay đổi",
      "Nếu $r = 0$, ta có thể khẳng định chắc chắn giữa $X$ và $Y$ không có bất kỳ mối quan hệ nào",
      "Hệ số tương quan mang đơn vị đo bằng tích đơn vị của $X$ và đơn vị của $Y$",
      "Hệ số $r = 0,8$ chứng tỏ $X$ là nguyên nhân dẫn tới 80% sự thay đổi của $Y$"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì hệ số tương quan Pearson $r$ luôn nằm trong đoạn $[-1; 1]$, được chuẩn hóa qua Z-score nên là một đại lượng không thứ nguyên (không có đơn vị), độc lập hoàn toàn với đơn vị đo lường của cả $X$ và $Y$.\n\nPhân tích bẫy sai:\n- Phương án B: $r=0$ chỉ chứng tỏ không có quan hệ TUYẾN TÍNH. Giữa $X$ và $Y$ vẫn có thể có quan hệ phi tuyến hoàn hảo (ví dụ $Y = X^2$ với $X \\in [-2, 2]$ đối xứng thì $r = 0$).\n- Phương án C: $r$ không có đơn vị đo.\n- Phương án D: Sai vì tương quan không đồng nghĩa với quan hệ nhân quả (correlation does not imply causation).",
    "source": "Stat20 Mục 2.10"
  },
  {
    "id": "TN1_10",
    "topicId": 1,
    "topicName": "Dữ liệu & Thống kê mô tả",
    "level": "Trung bình",
    "question": "Cho dữ liệu hai biến $X$ và $Y$ có: $\\bar{x} = 10$, $s_x = 2$; $\\bar{y} = 50$, $s_y = 6$ và hệ số tương quan $r = 0,8$. Phương trình đường hồi quy tuyến tính OLS dự báo $Y$ theo $X$ có dạng $\\hat{y} = \\hat{\\beta}_0 + \\hat{\\beta}_1 x$. Giá trị của $\\hat{\\beta}_0$ và $\\hat{\\beta}_1$ lần lượt là:",
    "options": [
      "$\\hat{\\beta}_1 = 0,8$ và $\\hat{\\beta}_0 = 42$",
      "$\\hat{\\beta}_1 = 2,4$ và $\\hat{\\beta}_0 = 26$",
      "$\\hat{\\beta}_1 = 2,4$ và $\\hat{\\beta}_0 = 50$",
      "$\\hat{\\beta}_1 = 0,267$ và $\\hat{\\beta}_0 = 47,33$"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì theo công thức OLS:\n- Hệ số góc: $\\hat{\\beta}_1 = r \\cdot \\frac{s_y}{s_x} = 0,8 \\cdot \\frac{6}{2} = 2,4$.\n- Hệ số chặn: $\\hat{\\beta}_0 = \\bar{y} - \\hat{\\beta}_1 \\bar{x} = 50 - 2,4 \\cdot 10 = 50 - 24 = 26$.\nDo đó phương trình là $\\hat{y} = 26 + 2,4x$.\n\nPhân tích bẫy sai:\n- Phương án A: Nhầm lẫn trực tiếp lấy hệ số góc bằng hệ số tương quan $\\hat{\\beta}_1 = r = 0,8$, rồi tính $\\hat{\\beta}_0 = 50 - 0,8 \\cdot 10 = 42$.\n- Phương án C: Quên không trừ $\\hat{\\beta}_1 \\bar{x}$ khi tính hệ số chặn.\n- Phương án D: Nghịch đảo tỷ số độ lệch chuẩn thành $r \\cdot \\frac{s_x}{s_y} = 0,8 \\cdot \\frac{2}{6} \\approx 0,267$ (hồi quy $X$ theo $Y$ thay vì $Y$ theo $X$).",
    "source": "Stat20 Mục 2.10"
  },
  {
    "id": "TN1_11",
    "topicId": 1,
    "topicName": "Dữ liệu & Thống kê mô tả",
    "level": "Cơ bản",
    "question": "Mô hình hồi quy dự báo điểm thi môn XSTK ($Y$) theo số giờ tự học ($X$) thu được phương trình: $\\hat{y} = 3,5 + 0,15x$. Ý nghĩa của hệ số 0,15 là gì?",
    "options": [
      "Nếu sinh viên học thêm 1 giờ, chắc chắn điểm thi thực tế của sinh viên đó sẽ tăng chính xác 0,15 điểm",
      "Nếu một sinh viên không học giờ nào ($x=0$), điểm thi dự báo của bạn đó là 0,15 điểm",
      "Khi sinh viên dành thêm 1 giờ tự học, điểm thi môn XSTK trung bình được dự báo tăng thêm 0,15 điểm",
      "Có 15% sự biến thiên của điểm thi được giải thích bởi số giờ tự học"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì hệ số góc trong mô hình OLS phản ánh mức thay đổi trung bình kỳ vọng (hoặc dự báo) của biến phản hồi $Y$ khi biến giải thích $X$ tăng thêm 1 đơn vị.\n\nPhân tích bẫy sai:\n- Phương án A: Sai nghiêm trọng vì hồi quy thống kê chỉ dự báo xu hướng trung bình cho tổng thể, không khẳng định một quan hệ tất định cá nhân tuyệt đối 100%.\n- Phương án B: Khi $x=0$, điểm dự báo là hệ số chặn $\\hat{\\beta}_0 = 3,5$, không phải 0,15.\n- Phương án D: Tỷ lệ biến thiên được đo bằng $R^2$, không phải bằng hệ số góc $\\hat{\\beta}_1$.",
    "source": "Stat20 Mục 2.10"
  },
  {
    "id": "TN1_12",
    "topicId": 1,
    "topicName": "Dữ liệu & Thống kê mô tả",
    "level": "Cơ bản",
    "question": "Cho đường hồi quy $\\hat{y} = 20 + 1,5x$. Một quan sát thực tế trong mẫu có $x_i = 10$ và $y_i = 38$. Phần dư (residual) $e_i$ tương ứng với quan sát này là bao nhiêu?",
    "options": [
      "-3",
      "+35",
      "+16,5",
      "+3"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì:\n- Giá trị dự báo từ mô hình: $\\hat{y}_i = 20 + 1,5 \\cdot 10 = 35$.\n- Phần dư định nghĩa là hiệu giữa giá trị thực tế và giá trị dự báo: $e_i = y_i - \\hat{y}_i = 38 - 35 = +3$.\nGiá trị phần dư dương thể hiện điểm dữ liệu thực tế nằm cao hơn đường hồi quy 3 đơn vị.\n\nPhân tích bẫy sai:\n- Phương án A: Sai do tính ngược $\\hat{y}_i - y_i = 35 - 38 = -3$.\n- Phương án B: Nhầm phần dư chính là giá trị dự báo $\\hat{y}_i = 35$.\n- Phương án C: Tính nhầm $38 - 1,5 \\cdot 10 - 20/2$ linh tinh.",
    "source": "Stat20 Mục 2.10"
  },
  {
    "id": "TN1_13",
    "topicId": 1,
    "topicName": "Dữ liệu & Thống kê mô tả",
    "level": "Trung bình",
    "question": "Trong mô hình hồi quy tuyến tính OLS đơn biến có hệ số chặn (intercept), khẳng định nào sau đây luôn luôn ĐÚNG với tập các phần dư $e_i$ ($i = 1, \\dots, n$)?",
    "options": [
      "Tổng các phần dư bằng 0 ($\\sum_{i=1}^n e_i = 0$), do đó trung bình của phần dư luôn bằng 0",
      "Mọi phần dư $e_i$ đều phải bằng 0 nếu kích thước mẫu đủ lớn",
      "Tổng bình phương các phần dư luôn bằng 0 ($\\sum e_i^2 = 0$)",
      "Độ lệch chuẩn của phần dư luôn bằng độ lệch chuẩn của biến phản hồi $Y$"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo tính chất toán học của phương pháp bình phương bé nhất OLS (khi mô hình có hệ số chặn $\\beta_0$), phương trình chuẩn thứ nhất bắt buộc $\\sum_{i=1}^n (y_i - \\hat{y}_i) = 0$, nghĩa là tổng các phần dư triệt tiêu lẫn nhau và trung bình phần dư $\\bar{e} = 0$.\n\nPhân tích bẫy sai:\n- Phương án B: Phần dư của từng điểm chỉ bằng 0 khi tất cả các điểm dữ liệu nằm thẳng hàng tuyệt đối trên một đường thẳng (điều không tưởng trong dữ liệu thực tế).\n- Phương án C: Tổng bình phương $\\sum e_i^2$ là hàm mục tiêu tối thiểu hóa ($SSE$), nó chỉ bằng 0 khi dữ liệu thẳng hàng hoàn hảo.\n- Phương án D: Sai vì độ lệch chuẩn phần dư $s_e = s_y \\sqrt{1 - R^2} \\le s_y$.",
    "source": "Stat20 Mục 2.10"
  },
  {
    "id": "TN1_14",
    "topicId": 1,
    "topicName": "Dữ liệu & Thống kê mô tả",
    "level": "Cơ bản",
    "question": "Hệ số tương quan giữa tốc độ chạy xe ($X$) và mức tiêu hao năng lượng hiệu quả ($Y$) là $r = -0,7$. Hệ số xác định $R^2$ của mô hình hồi quy tuyến tính đơn biến giữa $Y$ và $X$ là bao nhiêu và mang ý nghĩa gì?",
    "options": [
      "$R^2 = -0,49$; nghĩa là có sự tương quan nghịch biến mạnh giữa $X$ và $Y$",
      "$R^2 = 0,49$; nghĩa là 49% sự biến thiên của $Y$ được giải thích bởi quan hệ tuyến tính với $X$",
      "$R^2 = 0,7$; nghĩa là 70% các điểm dữ liệu nằm chính xác trên đường hồi quy",
      "$R^2 = 0,3$; nghĩa là còn 30% sai số chưa được giải thích"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì trong hồi quy tuyến tính đơn biến, hệ số xác định $R^2$ chính bằng bình phương của hệ số tương quan Pearson: $R^2 = r^2 = (-0,7)^2 = 0,49$ (hay 49%). Nó đo lường tỷ lệ biến thiên của biến phản hồi $Y$ được giải thích bởi mô hình hồi quy tuyến tính theo $X$.\n\nPhân tích bẫy sai:\n- Phương án A: Sai nghiêm trọng vì bình phương của một số thực không bao giờ âm ($R^2 \\ge 0$).\n- Phương án C: Nhầm $R^2$ với $|r| = 0,7$ và hiểu sai ý nghĩa (không phải % số điểm nằm trên đường).\n- Phương án D: Sai phép tính $1 - 0,7 = 0,3$.",
    "source": "Stat20 Mục 2.10"
  },
  {
    "id": "TN1_15",
    "topicId": 1,
    "topicName": "Dữ liệu & Thống kê mô tả",
    "level": "Trung bình",
    "question": "Một trường đại học nhận thấy tỷ lệ trúng tuyển chung của thí sinh nữ thấp hơn thí sinh nam. Tuy nhiên, khi xét riêng từng khoa (Kỹ thuật, Kinh tế, Xã hội), tỷ lệ trúng tuyển của nữ ở TỪNG KHOA đều cao hơn hoặc bằng nam. Hiện tượng này được gọi là gì và nguyên nhân chính là do đâu?",
    "options": [
      "Hiệu ứng đòn bẩy (Leverage effect); do có nhiều quan sát ngoại lai làm bóp méo số liệu",
      "Quy tắc 1,5xIQR; do dữ liệu của thí sinh nữ bị lệch trái nghiêm trọng",
      "Nghịch lý Simpson; do biến gây nhiễu (confounding variable) là 'Khoa ứng tuyển' - nữ nộp đơn nhiều hơn vào các khoa có tính cạnh tranh rất cao và tỷ lệ chọi khốc liệt",
      "Hiện tượng quá khớp (Overfitting); do số lượng biến số nhiều hơn số lượng mẫu quan sát"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì đây là ví dụ kinh điển về Nghịch lý Simpson (Stat20 Ch.2, vụ kiện tuyển sinh UC Berkeley 1973). Xu hướng quan sát được ở từng nhóm nhỏ bị đảo ngược khi gộp chung dữ liệu lại, nguyên nhân là do tồn tại một biến ẩn/biến gây nhiễu phân bổ không đồng đều giữa hai nhóm (ở đây nữ nộp nhiều vào khoa khó đỗ, nam nộp nhiều vào khoa dễ đỗ).\n\nPhân tích bẫy sai:\n- Phương án A: Sai vì hiện tượng đòn bẩy là khái niệm trong hồi quy OLS khi điểm có giá trị $x$ cực đoan.\n- Phương án B: Sai vì 1,5xIQR là tiêu chuẩn lọc ngoại lai một chiều.\n- Phương án D: Sai vì overfitting là hiện tượng mô hình học máy học vẹt chi tiết nhiễu.",
    "source": "Stat20 Mục 2.2, 2.10"
  },
  {
    "id": "TN1_16",
    "topicId": 1,
    "topicName": "Dữ liệu & Thống kê mô tả",
    "level": "Trung bình",
    "question": "Một mô hình hồi quy bội dự báo giá nhà ($Y$, triệu đồng) theo diện tích ($X_1$, $m^2$) và khoảng cách tới trung tâm ($X_2$, km) có dạng: $\\hat{y} = 500 + 40 x_1 - 85 x_2$. Ý nghĩa của hệ số $-85$ là gì?",
    "options": [
      "Cứ xa trung tâm thêm 1 km thì giá nhà của mọi căn hộ đều giảm chính xác 85 triệu đồng",
      "Khoảng cách tới trung tâm và diện tích nhà có mối quan hệ nghịch biến với hệ số tương quan là -85",
      "Nếu diện tích nhà tăng thêm $1 m^2$ thì giá nhà giảm 85 triệu đồng",
      "Trong điều kiện diện tích nhà không đổi (ceteris paribus), cứ xa trung tâm thêm 1 km thì giá nhà trung bình được dự báo giảm 85 triệu đồng"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì trong hồi quy bội, mỗi hệ số góc $\\hat{\\beta}_j$ biểu diễn sự thay đổi dự báo của $Y$ khi biến giải thích $X_j$ tăng 1 đơn vị VỚI ĐIỀU KIỆN TẤT CẢ CÁC BIẾN CÒN LẠI ĐƯỢC GIỮ NGUYÊN (nguyên lý ceteris paribus / holding other variables constant).\n\nPhân tích bẫy sai:\n- Phương án A: Sai vì thiếu điều kiện giữ nguyên diện tích $X_1$, và dùng từ 'chắc chắn mọi căn hộ' thay vì trung bình dự báo.\n- Phương án B: Hệ số tương quan chỉ nằm từ -1 đến +1, không thể bằng -85.\n- Phương án C: Nhầm biến khoảng cách $X_2$ với biến diện tích $X_1$.",
    "source": "Stat20 Mục 2.12"
  },
  {
    "id": "TN1_17",
    "topicId": 1,
    "topicName": "Dữ liệu & Thống kê mô tả",
    "level": "Nâng cao",
    "question": "Trong phân tích hồi quy tuyến tính, một điểm quan sát có giá trị của biến độc lập $x_i$ rất xa so với giá trị trung bình $\\bar{x}$, nhưng lại nằm gần như hoàn hảo trên đường xu hướng chung của các điểm còn lại. Điểm này có đặc điểm gì?",
    "options": [
      "Có đòn bẩy cao (high leverage) nhưng có mức độ ảnh hưởng thấp (low influence) đến độ dốc của đường hồi quy",
      "Có đòn bẩy thấp nhưng có mức độ ảnh hưởng cực cao",
      "Là một điểm ngoại lai có phần dư cực lớn làm đảo ngược dấu của hệ số góc",
      "Làm cho hệ số xác định $R^2$ giảm mạnh về gần 0"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì:\n- Điểm có $x_i$ cách rất xa $\\bar{x}$ luôn có giá trị đòn bẩy (leverage) cao vì nó nằm ở vị trí tiềm năng có thể làm xoay đường hồi quy.\n- Tuy nhiên, vì nó lại nằm ngay trên đường xu hướng chung của toàn bộ mẫu, nên phần dư của nó rất nhỏ ($e_i \\approx 0$). Việc loại bỏ điểm này hay giữ lại điểm này hầu như không làm thay đổi hệ số góc $\\hat{\\beta}_1$, do đó nó có sức ảnh hưởng thấp (low influence).\n\nPhân tích bẫy sai:\n- Phương án B: Ngược hoàn toàn với bản chất toán học của leverage.\n- Phương án C: Sai vì phần dư của nó rất nhỏ do nằm ngay trên đường xu hướng.\n- Phương án D: Điểm đòn bẩy cao nằm thẳng hàng với xu hướng chung thực chất sẽ làm TĂNG $R^2$ chứ không làm giảm.",
    "source": "Stat20 Mục 2.10"
  },
  {
    "id": "TN1_18",
    "topicId": 1,
    "topicName": "Dữ liệu & Thống kê mô tả",
    "level": "Trung bình",
    "question": "Khi ta thêm một biến giải thích bất kỳ $X_k$ vào mô hình hồi quy OLS bội (ngay cả khi biến này là các số ngẫu nhiên không có ý nghĩa thực tế), hệ số xác định $R^2$ thông thường sẽ thay đổi như thế nào?",
    "options": [
      "Luôn luôn giảm đi vì mô hình bị phân tán",
      "Luôn luôn tăng hoặc giữ nguyên không đổi, không bao giờ giảm",
      "Giảm đi một lượng đúng bằng hệ số tương quan giữa biến mới và $Y$",
      "Không thể dự đoán được vì phụ thuộc vào kích thước mẫu $n$"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì về mặt đại số tuyến tính, thêm một biến mới đồng nghĩa với việc mở rộng không gian vector chiếu của các biến độc lập, làm cho tổng bình phương sai số phần dư ($SSE$) luôn giảm hoặc giữ nguyên ($SSE_{new} \\le SSE_{old}$). Do $R^2 = 1 - \\frac{SSE}{SST}$, nên $R^2$ chỉ có thể tăng hoặc cùng lắm giữ nguyên. Chính vì nhược điểm này, người ta mới cần dùng $R^2$ hiệu chỉnh ($Adjusted\\; R^2$) để phạt các biến vô bổ.\n\nPhân tích bẫy sai:\n- Phương án A, C, D: Đều sai với tính chất toán học của OLS.",
    "source": "Stat20 Mục 2.12"
  },
  {
    "id": "TN1_19",
    "topicId": 1,
    "topicName": "Dữ liệu & Thống kê mô tả",
    "level": "Cơ bản",
    "question": "Trong biểu đồ hộp (Boxplot), đường vạch ngang nằm bên trong hình hộp chữ nhật biểu diễn đại lượng nào của mẫu số liệu?",
    "options": [
      "Trung bình cộng (Mean)",
      "Độ lệch chuẩn (SD)",
      "Trung vị (Median)",
      "Yếu vị (Mode)"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì theo cấu trúc chuẩn của Boxplot (biểu đồ 5 số đặc trưng của Tukey):\n- Cạnh dưới hộp là $Q_1$, cạnh trên hộp là $Q_3$.\n- Vạch kẻ bên trong hộp luôn là Trung vị ($Median = Q_2$). Chiều cao hộp là $IQR = Q_3 - Q_1$.\n\nPhân tích bẫy sai:\n- Phương án A: Giá trị Mean thường không được vẽ trong boxplot tiêu chuẩn (hoặc nếu có chỉ là một dấu cộng/chấm riêng biệt).\n- Phương án B, D: SD và Mode không được thể hiện bằng vạch ngang trong hộp.",
    "source": "Stat20 Mục 2.4"
  },
  {
    "id": "TN1_20",
    "topicId": 1,
    "topicName": "Dữ liệu & Thống kê mô tả",
    "level": "Cơ bản",
    "question": "Cho mẫu số liệu gồm 5 giá trị: 2, 4, 6, 8, 10. Phương sai mẫu hiệu chỉnh ($s^2$, mẫu số $n-1$) của mẫu này bằng bao nhiêu?",
    "options": [
      "8",
      "\\(\\sqrt{10} \\approx 3,16\\)",
      "40",
      "10"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì:\n- Số quan sát $n = 5$.\n- Trung bình mẫu: $\\bar{x} = \\frac{2 + 4 + 6 + 8 + 10}{5} = 6$.\n- Các độ lệch bình phương: $(2-6)^2 = 16$, $(4-6)^2 = 4$, $(6-6)^2 = 0$, $(8-6)^2 = 4$, $(10-6)^2 = 16$.\n- Tổng các độ lệch bình phương: $16 + 4 + 0 + 4 + 16 = 40$.\n- Phương sai mẫu hiệu chỉnh (chia cho $n-1 = 4$): $s^2 = \\frac{40}{4} = 10$.\n\nPhân tích bẫy sai:\n- Phương án A: Sai do chia cho $n=5$ thay vì $n-1=4$ ($40/5 = 8$, đây là phương sai chưa hiệu chỉnh $\\sigma^2$ của tổng thể).\n- Phương án B: Đây là độ lệch chuẩn $s = \\sqrt{10}$, câu hỏi hỏi phương sai $s^2$.\n- Phương án C: 40 là tổng các bình phương độ lệch ($SS$), chưa chia cho bậc tự do $n-1$.",
    "source": "Stat20 Mục 2.4; Slide Week 07 tr. 8"
  },
  {
    "id": "TN1_21",
    "topicId": 1,
    "topicName": "Dữ liệu & Thống kê mô tả",
    "level": "Cơ bản",
    "question": "Một lớp học có 40 sinh viên, trong đó có 14 sinh viên đạt điểm Giỏi, 18 sinh viên đạt điểm Khá, còn lại là Trung bình. Tần số tương đối (tỷ lệ phần trăm) của sinh viên đạt loại Trung bình trong lớp là bao nhiêu?",
    "options": [
      "20%",
      "8%",
      "35%",
      "45%"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì:\n- Số sinh viên đạt loại Trung bình: $40 - (14 + 18) = 40 - 32 = 8$ sinh viên.\n- Tần số tương đối: $\\frac{8}{40} = 0,2 = 20\\%$.\n\nPhân tích bẫy sai:\n- Phương án B: Nhầm lẫn giữa số sinh viên (8 sinh viên) với số phần trăm (ghi nhầm thành 8%).\n- Phương án C: $14/40 = 35\\%$ là tỷ lệ sinh viên Giỏi.\n- Phương án D: $18/40 = 45\\%$ là tỷ lệ sinh viên Khá.",
    "source": "Stat20 Mục 2.2"
  },
  {
    "id": "TN1_22",
    "topicId": 1,
    "topicName": "Dữ liệu & Thống kê mô tả",
    "level": "Nâng cao",
    "question": "Một nhà nghiên cứu xây dựng mô hình hồi quy biểu diễn chiều cao trẻ em theo độ tuổi dựa trên mẫu gồm các bé từ 2 đến 10 tuổi: $\\hat{y} = 75 + 6x$ (cm). Sau đó, nhà nghiên cứu dùng mô hình này để dự báo chiều cao của một người khi 35 tuổi ($x=35$) và thu được $\\hat{y} = 75 + 6 \\cdot 35 = 285$ cm. Sai lầm nghiêm trọng ở đây là gì?",
    "options": [
      "Tính toán sai số học vì $6 \\cdot 35 + 75$ phải bằng 210 cm",
      "Ngoại suy (Extrapolation) quá xa ngoài miền dữ liệu quan sát gốc ($x \\in [2; 10]$), nơi quy luật sinh học không còn giữ nguyên dạng tuyến tính",
      "Mô hình thiếu biến giới tính nên hệ số chặn bị đội lên quá cao",
      "Hệ số góc phải là số âm vì tuổi càng cao thì người càng thấp đi"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì hiện tượng ngoại suy (extrapolation) là việc áp dụng phương trình hồi quy cho các giá trị nằm ngoài phạm vi quan sát của dữ liệu mẫu. Chiều cao trẻ em tăng tuyến tính từ 2 đến 10 tuổi, nhưng sau tuổi dậy thì chiều cao sẽ ngừng tăng. Ngoại suy đến tuổi 35 dẫn đến kết quả phi lý 285 cm.\n\nPhân tích bẫy sai:\n- Phương án A: Phép tính $75 + 210 = 285$ hoàn toàn đúng về mặt số học thuần túy, sai lầm nằm ở bản chất thống kê.\n- Phương án C, D: Không phải nguyên nhân gây ra kết quả phi lý này.",
    "source": "Stat20 Mục 2.10"
  },
  {
    "id": "TN1_23",
    "topicId": 1,
    "topicName": "Dữ liệu & Thống kê mô tả",
    "level": "Nâng cao",
    "question": "Khi so sánh hai mô hình hồi quy bội dự báo cùng một biến phản hồi $Y$: Mô hình 1 có 2 biến độc lập với $R^2 = 0,65$ và $R^2_{adj} = 0,63$; Mô hình 2 thêm vào 5 biến độc lập nữa có $R^2 = 0,66$ và $R^2_{adj} = 0,58$. Nhà phân tích nên lựa chọn mô hình nào và vì sao?",
    "options": [
      "Chọn Mô hình 2 vì $R^2$ của nó cao hơn (0,66 so với 0,65), mô hình luôn tốt hơn khi $R^2$ lớn hơn",
      "Cả hai mô hình tương đương nhau vì sai số chỉ chênh lệch 1%",
      "Chọn Mô hình 1 vì $R^2_{adj}$ cao hơn đáng kể (0,63 so với 0,58), chứng tỏ 5 biến thêm vào không đem lại giá trị thông tin bù đắp được sự phức tạp của mô hình",
      "Không thể kết luận được nếu chưa biết phương sai phần dư của Mô hình 1"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì trong hồi quy bội, $R^2$ thông thường luôn tăng khi thêm biến bất kể biến đó có vô nghĩa hay không. Để tránh overfitting, ta phải căn cứ vào $R^2$ hiệu chỉnh ($R^2_{adj}$). Việc $R^2_{adj}$ giảm từ 0,63 xuống 0,58 cho thấy 5 biến thêm vào là các biến gây nhiễu, làm mô hình cồng kềnh và giảm khả năng khái quát hóa.\n\nPhân tích bẫy sai:\n- Phương án A: Rơi vào bẫy cổ điển chỉ nhìn vào $R^2$ thông thường khi so sánh các mô hình có số lượng biến khác nhau.\n- Phương án B, D: Sai quy tắc chuẩn trong lựa chọn mô hình hồi quy.",
    "source": "Stat20 Mục 2.12"
  },
  {
    "id": "TN2_01",
    "topicId": 2,
    "topicName": "Xác suất cổ điển, Có điều kiện & Bayes",
    "level": "Cơ bản",
    "question": "Cho hai biến cố $A$ và $B$ có $P(A) = 0,6$; $P(B) = 0,5$ và $P(A \\cap B) = 0,3$. Xác suất biến cố hợp $P(A \\cup B)$ bằng bao nhiêu?",
    "options": [
      "1,1",
      "0,3",
      "0,4",
      "0,8"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì theo quy tắc cộng xác suất tổng quát:\n$P(A \\cup B) = P(A) + P(B) - P(A \\cap B) = 0,6 + 0,5 - 0,3 = 0,8$.\n\nPhân tích bẫy sai:\n- Phương án A: Sai do cộng trực tiếp $0,6 + 0,5 = 1,1$ mà quên trừ phần giao (xác suất không bao giờ vượt quá 1!).\n- Phương án B: Nhầm $P(A \\cup B)$ với $P(A \\cap B) = 0,3$.\n- Phương án C: Sai do tính $0,6 - 0,5 + 0,3 = 0,4$.",
    "source": "Slide Week 07; Stat20 Mục 3.1"
  },
  {
    "id": "TN2_02",
    "topicId": 2,
    "topicName": "Xác suất cổ điển, Có điều kiện & Bayes",
    "level": "Cơ bản",
    "question": "Tiếp tục với hai biến cố $A$ và $B$ ở câu trên ($P(A) = 0,6; P(B) = 0,5; P(A \\cap B) = 0,3 \\implies P(A \\cup B) = 0,8$). Xác suất để CẢ HAI biến cố $A$ và $B$ đều KHÔNG xảy ra ($P(\\bar{A} \\cap \\bar{B})$) bằng bao nhiêu?",
    "options": [
      "0,2",
      "0,1",
      "0,5",
      "0,7"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo định lý De Morgan: $\\bar{A} \\cap \\bar{B} = \\overline{A \\cup B}$.\nDo đó: $P(\\bar{A} \\cap \\bar{B}) = 1 - P(A \\cup B) = 1 - 0,8 = 0,2$.\n\nPhân tích bẫy sai:\n- Phương án B: Sai do tự ý nhân phần bù $P(\\bar{A}) \\cdot P(\\bar{B}) = (1-0,6)(1-0,5) = 0,4 \\cdot 0,5 = 0,2$ nhưng ngộ nhận công thức khác thành 0,1.\n- Phương án C: Sai do lấy $1 - P(B) = 0,5$.\n- Phương án D: Sai do lấy $1 - P(A \\cap B) = 1 - 0,3 = 0,7$ (đây là xác suất có ít nhất một biến cố không xảy ra $P(\\bar{A} \\cup \\bar{B})$).",
    "source": "Stat20 Mục 3.1"
  },
  {
    "id": "TN2_03",
    "topicId": 2,
    "topicName": "Xác suất cổ điển, Có điều kiện & Bayes",
    "level": "Cơ bản",
    "question": "Cho $P(A \\cap B) = 0,18$ và $P(B) = 0,4$. Xác suất có điều kiện $P(A \\mid B)$ bằng bao nhiêu?",
    "options": [
      "0,072",
      "0,45",
      "2,22",
      "0,22"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì theo định nghĩa xác suất có điều kiện:\n$P(A \\mid B) = \\frac{P(A \\cap B)}{P(B)} = \\frac{0,18}{0,4} = 0,45$.\n\nPhân tích bẫy sai:\n- Phương án A: Sai do lấy tích $0,18 \\cdot 0,4 = 0,072$.\n- Phương án C: Sai do lấy ngược $P(B) / P(A \\cap B) = 0,4 / 0,18 \\approx 2,22$ (xác suất không thể lớn hơn 1).\n- Phương án D: Sai do lấy hiệu $0,4 - 0,18 = 0,22$.",
    "source": "Slide Week 07; Stat20 Mục 3.2"
  },
  {
    "id": "TN2_04",
    "topicId": 2,
    "topicName": "Xác suất cổ điển, Có điều kiện & Bayes",
    "level": "Trung bình",
    "question": "Giả sử hai biến cố $A$ và $B$ có xác suất dương ($P(A) > 0, P(B) > 0$) và xung khắc nhau ($A \\cap B = \\emptyset$). Khẳng định nào sau đây là ĐÚNG?",
    "options": [
      "$A$ và $B$ chắc chắn độc lập với nhau vì chúng không liên quan tới nhau",
      "$P(A \\cup B) = P(A) \\cdot P(B)$",
      "$A$ và $B$ KHÔNG THỂ độc lập với nhau",
      "$P(A \\mid B) = P(A)$"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì:\n- Do $A$ và $B$ xung khắc nên $P(A \\cap B) = P(\\emptyset) = 0$.\n- Để $A$ và $B$ độc lập thì bắt buộc $P(A \\cap B) = P(A) \\cdot P(B)$.\n- Vì $P(A) > 0$ và $P(B) > 0$ nên $P(A) \\cdot P(B) > 0 \\neq 0$.\nDo đó hai biến cố có xác suất dương và xung khắc nhau thì KHÔNG BAO GIỜ độc lập (biết $B$ xảy ra thì $A$ chắc chắn không xảy ra, $P(A \\mid B) = 0 \\neq P(A)$).\n\nPhân tích bẫy sai:\n- Phương án A: Nhầm lẫn phổ biến giữa 'xung khắc' (không thể cùng xảy ra) và 'độc lập' (không làm thay đổi xác suất của nhau).\n- Phương án B: Viết sai công thức xác suất hợp.\n- Phương án D: Sai vì $P(A \\mid B) = 0 \\neq P(A)$.",
    "source": "Stat20 Mục 3.2; Slide Week 07"
  },
  {
    "id": "TN2_05",
    "topicId": 2,
    "topicName": "Xác suất cổ điển, Có điều kiện & Bayes",
    "level": "Cơ bản",
    "question": "Cho hai biến cố $A$ và $B$ độc lập với nhau, có $P(A) = 0,4$ và $P(B) = 0,5$. Xác suất của biến cố giao $P(A \\cap B)$ và biến cố hợp $P(A \\cup B)$ lần lượt là:",
    "options": [
      "0,20 và 0,90",
      "0,00 và 0,90",
      "0,10 và 0,80",
      "0,20 và 0,70"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì:\n- Do $A$ và $B$ độc lập: $P(A \\cap B) = P(A) \\cdot P(B) = 0,4 \\cdot 0,5 = 0,20$.\n- Quy tắc cộng: $P(A \\cup B) = P(A) + P(B) - P(A \\cap B) = 0,4 + 0,5 - 0,20 = 0,70$.\n\nPhân tích bẫy sai:\n- Phương án A: Sai do tính $P(A \\cap B) = 0,20$ nhưng lại quên trừ phần giao khi tính hợp ($0,4 + 0,5 = 0,90$).\n- Phương án B: Nhầm độc lập thành xung khắc ($P(A \\cap B) = 0$).\n- Phương án C: Sai số học.",
    "source": "Stat20 Mục 3.2"
  },
  {
    "id": "TN2_06",
    "topicId": 2,
    "topicName": "Xác suất cổ điển, Có điều kiện & Bayes",
    "level": "Cơ bản",
    "question": "Từ một bộ bài tây tiêu chuẩn gồm 52 lá, người ta rút ngẫu nhiên đồng thời 3 lá bài (không quan tâm thứ tự). Có bao nhiêu kết quả có thể xảy ra trong không gian mẫu?",
    "options": [
      "22100",
      "132600",
      "156",
      "140608"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì rút đồng thời 3 lá không xét thứ tự từ 52 lá là số tổ hợp chập 3 của 52 phần tử:\n$C_{52}^3 = \\frac{52!}{3! \\cdot 49!} = \\frac{52 \\cdot 51 \\cdot 50}{3 \\cdot 2 \\cdot 1} = 22.100$.\n\nPhân tích bẫy sai:\n- Phương án B: $52 \\cdot 51 \\cdot 50 = 132.600$ là số chỉnh hợp $A_{52}^3$ (có phân biệt thứ tự rút).\n- Phương án C: Sai do lấy $52 \\cdot 3 = 156$.\n- Phương án D: $52^3 = 140.608$ là trường hợp rút có hoàn lại từng lá.",
    "source": "Stat20 Mục 3.3"
  },
  {
    "id": "TN2_07",
    "topicId": 2,
    "topicName": "Xác suất cổ điển, Có điều kiện & Bayes",
    "level": "Cơ bản",
    "question": "Một chiếc hộp chứa 6 quả bóng màu đỏ và 4 quả bóng màu xanh. Rút ngẫu nhiên lần lượt 2 quả bóng không hoàn lại. Xác suất để cả 2 quả bóng rút được đều màu đỏ là:",
    "options": [
      "9/25 (36%)",
      "1/3 (khoảng 33,33%)",
      "3/5 (60%)",
      "1/5 (20%)"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì theo quy tắc nhân xác suất có điều kiện (rút không hoàn lại):\n- Lần 1 rút bóng đỏ: xác suất là $\\frac{6}{10}$.\n- Lần 2 rút tiếp bóng đỏ (trong hộp còn 5 bóng đỏ trên 9 quả): xác suất là $\\frac{5}{9}$.\n- Xác suất cả hai quả đỏ: $P = \\frac{6}{10} \\cdot \\frac{5}{9} = \\frac{30}{90} = \\frac{1}{3} \\approx 33,33\\%$.\n(Cách 2 dùng tổ hợp: $\\frac{C_6^2}{C_{10}^2} = \\frac{15}{45} = \\frac{1}{3}$).\n\nPhân tích bẫy sai:\n- Phương án A: Sai do coi là rút CÓ hoàn lại: $(\\frac{6}{10})^2 = \\frac{36}{100} = 36\\%$.\n- Phương án C: $\\frac{6}{10} = \\frac{3}{5}$ mới là xác suất rút 1 quả đỏ ở lần đầu.\n- Phương án D: Sai số học.",
    "source": "Stat20 Mục 3.3"
  },
  {
    "id": "TN2_08",
    "topicId": 2,
    "topicName": "Xác suất cổ điển, Có điều kiện & Bayes",
    "level": "Cơ bản",
    "question": "Cũng chiếc hộp trên (6 bóng đỏ, 4 bóng xanh), nhưng người ta rút lần 1, ghi lại màu, rồi TRẢ LẠI quả bóng vào hộp, khuấy đều rồi mới rút lần 2 (rút có hoàn lại). Xác suất để cả 2 quả bóng rút được đều màu đỏ là bao nhiêu?",
    "options": [
      "0,3333",
      "0,60",
      "0,36",
      "0,16"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì do có hoàn lại, hai lần rút là hoàn toàn độc lập với xác suất đỏ mỗi lần là $p = \\frac{6}{10} = 0,6$.\nDo đó: $P = 0,6 \\cdot 0,6 = 0,36$ (36%).\n\nPhân tích bẫy sai:\n- Phương án A: 0,3333 (1/3) là kết quả của bài toán rút KHÔNG hoàn lại.\n- Phương án B: 0,60 là xác suất của một lần rút đơn lẻ.\n- Phương án D: $0,4 \\cdot 0,4 = 0,16$ là xác suất cả hai quả đều xanh.",
    "source": "Stat20 Mục 3.3"
  },
  {
    "id": "TN2_09",
    "topicId": 2,
    "topicName": "Xác suất cổ điển, Có điều kiện & Bayes",
    "level": "Trung bình",
    "question": "Một nhà máy có 2 phân xưởng cùng sản xuất một loại linh kiện: Phân xưởng I sản xuất 60% tổng sản lượng với tỷ lệ phế phẩm là 2%; Phân xưởng II sản xuất 40% sản lượng còn lại với tỷ lệ phế phẩm là 3%. Chọn ngẫu nhiên một linh kiện từ kho của nhà máy. Xác suất để linh kiện này là phế phẩm bằng bao nhiêu?",
    "options": [
      "0,050 (tức 5%)",
      "0,025 (tức 2,5%)",
      "0,012 (tức 1,2%)",
      "0,024 (tức 2,4%)"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì áp dụng công thức xác suất toàn phần với hệ đầy đủ $\\{A_1, A_2\\}$ là linh kiện do xưởng I và II sản xuất:\n$P(B) = P(A_1) P(B \\mid A_1) + P(A_2) P(B \\mid A_2) = 0,60 \\cdot 0,02 + 0,40 \\cdot 0,03 = 0,012 + 0,012 = 0,024$ (2,4%).\n\nPhân tích bẫy sai:\n- Phương án A: Sai do cộng ngây thơ hai tỷ lệ phế phẩm: $2\\% + 3\\% = 5\\%$.\n- Phương án B: Sai do lấy trung bình cộng giản đơn: $\\frac{2\\% + 3\\%}{2} = 2,5\\%$ (bỏ qua trọng số sản lượng 60% và 40%).\n- Phương án C: Chỉ tính riêng phần phế phẩm của một phân xưởng.",
    "source": "Stat20 Mục 3.4; Slide Week 07"
  },
  {
    "id": "TN2_10",
    "topicId": 2,
    "topicName": "Xác suất cổ điển, Có điều kiện & Bayes",
    "level": "Trung bình",
    "question": "Tiếp tục với bài toán nhà máy ở trên: Người ta kiểm tra một linh kiện lấy ngẫu nhiên và thấy nó là phế phẩm. Xác suất để phế phẩm này do Phân xưởng I sản xuất là bao nhiêu?",
    "options": [
      "0,50 (tức 50%)",
      "0,60 (tức 60%)",
      "0,40 (tức 40%)",
      "0,012 (tức 1,2%)"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo công thức Bayes:\n$P(A_1 \\mid B) = \\frac{P(A_1) P(B \\mid A_1)}{P(B)} = \\frac{0,60 \\cdot 0,02}{0,024} = \\frac{0,012}{0,024} = 0,5$ (50%).\n\nPhân tích bẫy sai:\n- Phương án B: Sai do nhầm với xác suất tiên nghiệm (prior probability) $P(A_1) = 0,60$.\n- Phương án C: Sai do chọn tiên nghiệm của xưởng II.\n- Phương án D: 0,012 mới chỉ là tử số $P(A_1 \\cap B)$, chưa chia cho xác suất toàn phần $P(B)$.",
    "source": "Stat20 Mục 3.4; Slide Week 07"
  },
  {
    "id": "TN2_11",
    "topicId": 2,
    "topicName": "Xác suất cổ điển, Có điều kiện & Bayes",
    "level": "Nâng cao",
    "question": "Một căn bệnh hiếm gặp có tỷ lệ mắc trong cộng đồng là 1% ($P(D) = 0,01$). Một xét nghiệm chẩn đoán có độ nhạy 95% ($P(+ \\mid D) = 0,95$) và độ đặc hiệu 90% (tức tỷ lệ dương tính giả trong người khỏe là 10%, $P(+ \\mid \\bar{D}) = 0,10$). Một người đi xét nghiệm và nhận kết quả dương tính (+). Xác suất thực sự người này bị bệnh ($P(D \\mid +)$) xấp xỉ bằng bao nhiêu?",
    "options": [
      "Chính xác 95%",
      "Khoảng 8,76%",
      "Khoảng 85,5%",
      "Khoảng 50%"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì theo công thức Bayes:\n- Xác suất kết quả xét nghiệm dương tính toàn phần:\n$P(+) = P(D) P(+ \\mid D) + P(\\bar{D}) P(+ \\mid \\bar{D}) = 0,01 \\cdot 0,95 + 0,99 \\cdot 0,10 = 0,0095 + 0,0990 = 0,1085$.\n- Xác suất người dương tính thực sự mắc bệnh:\n$P(D \\mid +) = \\frac{0,01 \\cdot 0,95}{0,1085} = \\frac{0,0095}{0,1085} \\approx 0,08756$ (tức khoảng 8,76%).\nĐây là minh chứng kinh điển cho 'Ngụy biện tỷ lệ cơ sở' (Base Rate Fallacy): vì bệnh rất hiếm (chỉ 1%), số ca dương tính giả từ 99% người khỏe ($0,099$) áp đảo số ca dương tính thật ($0,0095$), khiến xác suất mắc bệnh khi dương tính chưa đến 9%!\n\nPhân tích bẫy sai:\n- Phương án A: Bẫy ngụy biện phổ biến nhất, nhầm độ nhạy $P(+ \\mid D) = 95\\%$ thành $P(D \\mid +)$.\n- Phương án C, D: Phép tính nhẩm sai lầm.",
    "source": "Stat20 Mục 3.4"
  },
  {
    "id": "TN2_12",
    "topicId": 2,
    "topicName": "Xác suất cổ điển, Có điều kiện & Bayes",
    "level": "Cơ bản",
    "question": "Một xạ thủ bắn 4 phát đạn độc lập vào bia, xác suất trúng bia ở mỗi phát đều bằng $0,7$. Xác suất để xạ thủ bắn TRÚNG BIA ÍT NHẤT MỘT PHÁT bằng bao nhiêu?",
    "options": [
      "0,7599",
      "2,8000",
      "0,9919",
      "0,2401"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì biến cố đối của 'bắn trúng ít nhất một phát' là 'cả 4 phát đều trượt'.\n- Xác suất trượt ở mỗi phát: $1 - 0,7 = 0,3$.\n- Do các phát bắn độc lập, xác suất cả 4 phát trượt: $0,3^4 = 0,0081$.\n- Xác suất trúng ít nhất một phát: $1 - 0,0081 = 0,9919$.\n\nPhân tích bẫy sai:\n- Phương án A: Sai do tính nhầm $1 - 0,7^4 = 1 - 0,2401 = 0,7599$.\n- Phương án B: Sai do cộng trực tiếp $4 \\cdot 0,7 = 2,8$ (xác suất không thể lớn hơn 1).\n- Phương án D: 0,2401 là xác suất cả 4 phát đều trúng ($0,7^4$), không phải ít nhất một.",
    "source": "Stat20 Mục 3.2"
  },
  {
    "id": "TN2_13",
    "topicId": 2,
    "topicName": "Xác suất cổ điển, Có điều kiện & Bayes",
    "level": "Trung bình",
    "question": "Một trò chơi quay số trúng thưởng có xác suất trúng ở mỗi lần quay độc lập là $p = 0,2$. Cần quay ít nhất bao nhiêu lần để xác suất trúng thưởng ít nhất một lần đạt tối thiểu 99%?",
    "options": [
      "5 lần",
      "20 lần",
      "15 lần",
      "21 lần"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì:\n- Ta cần: $P(\\text{ít nhất 1 lần trúng}) = 1 - (1 - 0,2)^n = 1 - 0,8^n \\ge 0,99$.\n- Tương đương: $0,8^n \\le 0,01$.\n- Lấy logarit tự nhiên hai vế (chú ý $\\ln(0,8) < 0$ nên đổi chiều bất đẳng thức):\n$n \\ge \\frac{\\ln(0,01)}{\\ln(0,8)} \\approx \\frac{-4,60517}{-0,22314} \\approx 20,64$.\n- Vì số lần quay phải là số nguyên nên ta làm tròn lên: $n = 21$ lần.\n\nPhân tích bẫy sai:\n- Phương án A: Lấy $1 / p = 1 / 0,2 = 5$ lần (đây chỉ là kỳ vọng số lần quay để trúng 1 lần, nhưng với $n=5$ thì xác suất trúng mới là $1 - 0,8^5 \\approx 67,23\\%$, cách rất xa 99%).\n- Phương án B: Làm tròn xuống $n=20$ thì xác suất mới chỉ đạt $1 - 0,8^{20} \\approx 98,85\\% < 99\\%$.\n- Phương án C: Đoán mò.",
    "source": "Stat20 Mục 3.2"
  },
  {
    "id": "TN2_14",
    "topicId": 2,
    "topicName": "Xác suất cổ điển, Có điều kiện & Bayes",
    "level": "Trung bình",
    "question": "Trong bài toán ngày sinh nổi tiếng (giả định 1 năm có 365 ngày và ngày sinh phân bổ đều): Cần một nhóm tối thiểu bao nhiêu người để xác suất có ít nhất 2 người có cùng ngày sinh (ngày và tháng) vượt quá 50%?",
    "options": [
      "23 người",
      "183 người",
      "366 người",
      "50 người"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo bài toán nghịch lý ngày sinh (Birthday Problem, Stat20 Ch.3):\n- Với $n=23$ người, số cặp ghép đôi là $C_{23}^2 = \\frac{23 \\cdot 22}{2} = 253$ cặp.\n- Xác suất để tất cả 23 người có ngày sinh hoàn toàn khác nhau là:\n$P(\\text{khác nhau}) = \\frac{365}{365} \\cdot \\frac{364}{365} \\cdot \\frac{363}{365} \\cdots \\frac{343}{365} \\approx 0,4927$.\n- Do đó, xác suất có ít nhất 2 người trùng ngày sinh là: $1 - 0,4927 = 0,5073 = 50,73\\% > 50\\%$.\n\nPhân tích bẫy sai:\n- Phương án B: 183 người (gần $365 / 2$) là suy luận trực giác ngây thơ so sánh số ngày trong năm.\n- Phương án C: 366 người là theo nguyên lý Dirichlet để CHẮC CHẮN 100% có trùng ngày sinh, không phải vượt quá 50%.\n- Phương án D: Ước lượng cảm tính.",
    "source": "Stat20 Mục 3.3"
  },
  {
    "id": "TN2_15",
    "topicId": 2,
    "topicName": "Xác suất cổ điển, Có điều kiện & Bayes",
    "level": "Cơ bản",
    "question": "Một người tung đồng xu cân đối đồng chất 6 lần liên tiếp và cả 6 lần đều xuất hiện mặt Ngửa. Ở lần tung thứ 7, xác suất xuất hiện mặt Sấp là bao nhiêu?",
    "options": [
      "Lớn hơn 0,5 vì theo quy luật bù trừ, mặt Sấp 'đã đến lúc' phải ra",
      "Chính xác 0,5",
      "Nhỏ hơn 0,5 vì đồng xu đang có đà xuất hiện mặt Ngửa",
      "Bằng \\(1 - (0,5)^6 \\approx 0,984\\)"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì mỗi lần tung đồng xu là một phép thử độc lập và đồng xu không có trí nhớ. Dù trước đó có ra 6 lần ngửa liên tiếp, xác suất mặt Sấp ở lần thứ 7 vẫn giữ nguyên bằng $0,5$. Suy nghĩ rằng mặt Sấp 'đã đến lúc phải ra' là một sai lầm nhận thức kinh điển mang tên 'Ngụy biện của con bạc' (Gambler's Fallacy).\n\nPhân tích bẫy sai:\n- Phương án A: Gambler's fallacy.\n- Phương án C: Hot-hand fallacy (ngụy biện bàn tay nóng).\n- Phương án D: Nhầm công thức xác suất biến cố hợp.",
    "source": "Stat20 Mục 3.2"
  },
  {
    "id": "TN2_16",
    "topicId": 2,
    "topicName": "Xác suất cổ điển, Có điều kiện & Bayes",
    "level": "Cơ bản",
    "question": "Gieo đồng thời hai con xúc xắc cân đối 6 mặt. Xác suất để tổng số chấm xuất hiện trên hai con xúc xắc bằng 7 là bao nhiêu?",
    "options": [
      "7/36",
      "1/12",
      "1/6 (khoảng 16,67%)",
      "1/36"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì:\n- Không gian mẫu gồm $|\\Omega| = 6 \\times 6 = 36$ kết quả đồng khả năng.\n- Các cặp có tổng bằng 7 là: $(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)$ gồm đúng 6 cặp thuận lợi.\n- Xác suất: $P = \\frac{6}{36} = \\frac{1}{6} \\approx 16,67\\%$.\n\nPhân tích bẫy sai:\n- Phương án A: Nhầm lẫn lấy tổng số chấm (7) chia cho không gian mẫu (36).\n- Phương án B: Sai do coi chỉ có 3 cặp vì quên không hoán vị thứ tự hai con xúc xắc ($3/36 = 1/12$).\n- Phương án D: 1/36 là xác suất của một cặp điểm cụ thể duy nhất (ví dụ đôi 1).",
    "source": "Stat20 Mục 3.1"
  },
  {
    "id": "TN2_17",
    "topicId": 2,
    "topicName": "Xác suất cổ điển, Có điều kiện & Bayes",
    "level": "Cơ bản",
    "question": "Một hệ các biến cố $\\{A_1, A_2, \\dots, A_n\\}$ được gọi là một hệ đầy đủ (hay phân hoạch của không gian mẫu $\\Omega$) khi và chỉ khi thỏa mãn hai điều kiện nào sau đây?",
    "options": [
      "Đôi một độc lập và có xác suất bằng nhau",
      "Có tổng xác suất bằng 1 nhưng có thể giao nhau",
      "Có ít nhất một biến cố chắc chắn",
      "Đôi một xung khắc ($A_i \\cap A_j = \\emptyset$ với mọi $i \\neq j$) và hợp của chúng phủ kín không gian mẫu ($\\bigcup_{i=1}^n A_i = \\Omega$)"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì theo định nghĩa toán học của hệ đầy đủ các biến cố: Tập hợp các biến cố phải không có phần tử chung đôi một ($A_i \\cap A_j = \\emptyset$) và khi hợp lại phải bao quát toàn bộ không gian mẫu ($\\sum P(A_i) = 1$).\n\nPhân tích bẫy sai:\n- Phương án A: Nhầm lẫn giữa 'xung khắc' và 'độc lập'.\n- Phương án B: Nếu giao nhau thì không phải là một phân hoạch.\n- Phương án C: Sai hoàn toàn.",
    "source": "Slide Week 07 tr. 4; Stat20 Mục 3.4"
  },
  {
    "id": "TN2_18",
    "topicId": 2,
    "topicName": "Xác suất cổ điển, Có điều kiện & Bayes",
    "level": "Cơ bản",
    "question": "Một khóa học có 60 sinh viên nam và 40 sinh viên nữ. Trong đó có 30 nam và 10 nữ theo học chuyên ngành CNTT. Chọn ngẫu nhiên một sinh viên trong khóa và biết rằng sinh viên này học chuyên ngành CNTT. Xác suất để sinh viên được chọn là NỮ bằng bao nhiêu?",
    "options": [
      "0,25 (tức 25%)",
      "0,10 (tức 10%)",
      "0,40 (tức 40%)",
      "0,33 (tức 33%)"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì:\n- Không gian mẫu thu hẹp của điều kiện 'học CNTT' gồm: $30 + 10 = 40$ sinh viên.\n- Trong nhóm này, số sinh viên nữ là 10 bạn.\n- Do đó: $P(\\text{Nữ} \\mid \\text{CNTT}) = \\frac{10}{40} = 0,25$ (25%).\n\nPhân tích bẫy sai:\n- Phương án B: $10 / 100 = 0,10$ là xác suất đồng thời vừa là nữ vừa học CNTT ($P(\\text{Nữ} \\cap \\text{CNTT})$ trên toàn khóa).\n- Phương án C: $40 / 100 = 0,40$ là tỷ lệ nữ toàn khóa.\n- Phương án D: $10 / 30 \\approx 0,33$ là tỷ số giữa nữ và nam học CNTT.",
    "source": "Stat20 Mục 3.2"
  },
  {
    "id": "TN2_19",
    "topicId": 2,
    "topicName": "Xác suất cổ điển, Có điều kiện & Bayes",
    "level": "Cơ bản",
    "question": "Cho 3 biến cố $A, B, C$ độc lập đôi một và độc lập toàn thể, với $P(A) = 0,5$; $P(B) = 0,4$; $P(C) = 0,2$. Xác suất để CẢ BA biến cố cùng xảy ra ($P(A \\cap B \\cap C)$) bằng bao nhiêu?",
    "options": [
      "1,10",
      "0,04",
      "0,20",
      "0,08"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì theo tính chất độc lập toàn thể:\n$P(A \\cap B \\cap C) = P(A) \\cdot P(B) \\cdot P(C) = 0,5 \\cdot 0,4 \\cdot 0,2 = 0,04$.\n\nPhân tích bẫy sai:\n- Phương án A: Cộng đại số $0,5 + 0,4 + 0,2 = 1,1$ (vô nghĩa vì xác suất > 1).\n- Phương án C: Sai do lấy giá trị của $P(C)$.\n- Phương án D: $0,4 \\cdot 0,2 = 0,08$ (quên nhân $P(A)$).",
    "source": "Stat20 Mục 3.2"
  },
  {
    "id": "TN2_20",
    "topicId": 2,
    "topicName": "Xác suất cổ điển, Có điều kiện & Bayes",
    "level": "Trung bình",
    "question": "Giả sử hai biến cố $A$ và $B$ độc lập với nhau, có $P(A) = 0,5$ và $P(B) = 0,2$. Xác suất có điều kiện $P(A \\mid \\bar{B})$ bằng bao nhiêu?",
    "options": [
      "0,8",
      "0,4",
      "0,5",
      "0,1"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì định lý quan trọng về tính độc lập: Nếu $A$ và $B$ độc lập thì $A$ và $\\bar{B}$ cũng hoàn toàn độc lập với nhau. Do đó, việc biến cố $\\bar{B}$ xảy ra không làm thay đổi xác suất của $A$:\n$P(A \\mid \\bar{B}) = P(A) = 0,5$.\n\nPhân tích bẫy sai:\n- Phương án A: $1 - P(B) = 0,8$ là xác suất của $\\bar{B}$.\n- Phương án B: $P(A \\cap \\bar{B}) = 0,5 \\cdot 0,8 = 0,4$ (nhầm xác suất giao với xác suất có điều kiện).\n- Phương án D: $P(A \\cap B) = 0,1$.",
    "source": "Stat20 Mục 3.2"
  },
  {
    "id": "TN2_21",
    "topicId": 2,
    "topicName": "Xác suất cổ điển, Có điều kiện & Bayes",
    "level": "Trung bình",
    "question": "Hai người cùng bắn độc lập vào một mục tiêu. Xác suất trúng của người thứ nhất là $0,6$ và người thứ hai là $0,4$. Xác suất để CÓ ĐÚNG MỘT người bắn trúng mục tiêu là:",
    "options": [
      "0,76",
      "0,24",
      "1,00",
      "0,52"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì biến cố 'đúng một người trúng' gồm hai trường hợp xung khắc:\n- Người 1 trúng, Người 2 trượt: $P(A \\cap \\bar{B}) = 0,6 \\cdot (1 - 0,4) = 0,6 \\cdot 0,6 = 0,36$.\n- Người 1 trượt, Người 2 trúng: $P(\\bar{A} \\cap B) = (1 - 0,6) \\cdot 0,4 = 0,4 \\cdot 0,4 = 0,16$.\nTổng xác suất: $0,36 + 0,16 = 0,52$.\n(Hoặc dùng công thức: $P(A) + P(B) - 2P(A \\cap B) = 0,6 + 0,4 - 2(0,24) = 0,52$).\n\nPhân tích bẫy sai:\n- Phương án A: 0,76 là xác suất CÓ ÍT NHẤT một người trúng ($1 - 0,4 \\cdot 0,6 = 0,76$).\n- Phương án B: 0,24 là xác suất CẢ HAI người cùng trúng ($0,6 \\cdot 0,4 = 0,24$).\n- Phương án C: Cộng ngây thơ $0,6 + 0,4 = 1,00$.",
    "source": "Stat20 Mục 3.2"
  },
  {
    "id": "TN2_22",
    "topicId": 2,
    "topicName": "Xác suất cổ điển, Có điều kiện & Bayes",
    "level": "Nâng cao",
    "question": "Trong trò chơi truyền hình Monty Hall kinh điển: Có 3 cánh cửa (1 xe hơi, 2 con dê). Người chơi chọn Cửa 1. Người dẫn chương trình (biết rõ sau mỗi cửa có gì) mở Cửa 3 để lộ ra một con dê, sau đó cho người chơi quyền đổi sang Cửa 2 hoặc giữ nguyên Cửa 1. Quyết định tối ưu về mặt xác suất là gì?",
    "options": [
      "Nên ĐỔI sang Cửa 2 vì xác suất trúng xe hơi tăng lên thành 2/3 (khoảng 66,7%)",
      "Đổi hay giữ nguyên đều có xác suất trúng như nhau là 1/2 (50%) vì chỉ còn lại 2 cánh cửa đóng",
      "Nên GIỮ NGUYÊN Cửa 1 vì xác suất ban đầu luôn được bảo toàn ở mức 2/3",
      "Không thể xác định được vì hành động của MC là hoàn toàn ngẫu nhiên"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì:\n- Xác suất chọn đúng xe hơi ngay lần đầu ở Cửa 1 là $1/3$. Xác suất xe hơi nằm ở 2 cửa còn lại là $2/3$.\n- Vì MC luôn cố tình mở một cửa có dê trong số các cửa bạn chưa chọn, nên toàn bộ xác suất $2/3$ của nhóm cửa còn lại được dồn hoàn toàn vào cánh cửa duy nhất chưa mở (Cửa 2).\n- Do đó, đổi cửa sẽ mang lại xác suất thắng là $2/3$, trong khi giữ nguyên chỉ là $1/3$.\n\nPhân tích bẫy sai:\n- Phương án B: Ảo tưởng 50-50 kinh điển do ngộ nhận rằng việc còn 2 cửa đóng đồng nghĩa với xác suất đồng khả năng (bỏ qua điều kiện MC mở cửa dựa trên thông tin biết trước).\n- Phương án C, D: Sai hoàn toàn.",
    "source": "Stat20 Mục 3.4"
  },
  {
    "id": "TN2_23",
    "topicId": 2,
    "topicName": "Xác suất cổ điển, Có điều kiện & Bayes",
    "level": "Nâng cao",
    "question": "Có 3 chiếc hộp giống hệt nhau: Hộp I chứa 2 bi đỏ và 3 bi xanh; Hộp II chứa 4 bi đỏ và 1 bi xanh; Hộp III chứa 1 bi đỏ và 4 bi xanh. Chọn ngẫu nhiên một chiếc hộp với xác suất như nhau, rồi từ hộp đó rút ngẫu nhiên một viên bi và thấy nó màu ĐỎ. Xác suất viên bi đỏ này được rút ra từ Hộp II là bao nhiêu?",
    "options": [
      "1/3 (khoảng 33,33%)",
      "4/7 (khoảng 57,14%)",
      "4/5 (80%)",
      "2/7 (khoảng 28,57%)"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì theo định lý Bayes:\n- Gọi $H_i$ là biến cố chọn được Hộp $i$ ($P(H_1) = P(H_2) = P(H_3) = 1/3$).\n- Gọi $R$ là biến cố rút được bi đỏ:\n  + $P(R \\mid H_1) = 2/5 = 0,4$.\n  + $P(R \\mid H_2) = 4/5 = 0,8$.\n  + $P(R \\mid H_3) = 1/5 = 0,2$.\n- Xác suất toàn phần rút được bi đỏ:\n  $P(R) = \\frac{1}{3}(0,4 + 0,8 + 0,2) = \\frac{1}{3} \\cdot 1,4 = \\frac{1,4}{3}$.\n- Áp dụng công thức Bayes cho Hộp II:\n  $P(H_2 \\mid R) = \\frac{P(H_2) P(R \\mid H_2)}{P(R)} = \\frac{\\frac{1}{3} \\cdot 0,8}{\\frac{1,4}{3}} = \\frac{0,8}{1,4} = \\frac{4}{7} \\approx 57,14\\%$.\n\nPhân tích bẫy sai:\n- Phương án A: $1/3$ là xác suất tiên nghiệm khi chưa biết thông tin màu bi.\n- Phương án C: $4/5 = 80\\%$ là xác suất rút bi đỏ nếu ĐÃ BIẾT ở hộp II ($P(R \\mid H_2)$).\n- Phương án D: $2/7$ là xác suất bi đến từ Hộp I ($P(H_1 \\mid R) = 0,4/1,4 = 2/7$).",
    "source": "Stat20 Mục 3.4; Slide Week 07"
  },
  {
    "id": "TN3_01",
    "topicId": 3,
    "topicName": "Biến ngẫu nhiên rời rạc, Kỳ vọng & Phương sai",
    "level": "Cơ bản",
    "question": "Biến ngẫu nhiên rời rạc $X$ nhận các giá trị $x \\in \\{1, 2, 3, 4\\}$ với bảng phân phối xác suất: $P(X = x) = c \\cdot x$ (với $c$ là một hằng số thực). Giá trị của $c$ bằng bao nhiêu để đây là một hàm khối xác suất (pmf) hợp lệ?",
    "options": [
      "1,00",
      "0,25",
      "0,10",
      "0,05"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì theo điều kiện chuẩn hóa của hàm khối xác suất (pmf):\n$\\sum_{x=1}^4 P(X = x) = 1 \\iff c(1 + 2 + 3 + 4) = 1 \\iff 10c = 1 \\iff c = 0,10$.\n\nPhân tích bẫy sai:\n- Phương án A: Nhầm tổng xác suất bằng 1 thì $c = 1$.\n- Phương án B: Sai do lấy $1 / 4 = 0,25$ (coi như 4 giá trị có xác suất đều nhau).\n- Phương án D: Sai số học.",
    "source": "Slide Week 07 tr. 5; Stat20 Mục 4.1"
  },
  {
    "id": "TN3_02",
    "topicId": 3,
    "topicName": "Biến ngẫu nhiên rời rạc, Kỳ vọng & Phương sai",
    "level": "Cơ bản",
    "question": "Cho biến ngẫu nhiên $X$ có bảng phân phối xác suất:\n$X$: 0, 1, 2, 3\n$P(X=x)$: 0,1; 0,4; 0,3; 0,2.\nKỳ vọng toán $E(X)$ bằng bao nhiêu?",
    "options": [
      "1,5",
      "2,0",
      "1,0",
      "1,6"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì áp dụng định nghĩa kỳ vọng của biến ngẫu nhiên rời rạc:\n$E(X) = \\sum x \\cdot P(X = x) = 0 \\cdot 0,1 + 1 \\cdot 0,4 + 2 \\cdot 0,3 + 3 \\cdot 0,2 = 0 + 0,4 + 0,6 + 0,6 = 1,6$.\n\nPhân tích bẫy sai:\n- Phương án A: Lấy trung bình cộng ngây thơ các giá trị: $\\frac{0 + 1 + 2 + 3}{4} = 1,5$ (bỏ qua trọng số xác suất).\n- Phương án B: Làm tròn lên 2.\n- Phương án C: Sai do quên nhân giá trị với xác suất.",
    "source": "Slide Week 07 tr. 6; Stat20 Mục 4.3"
  },
  {
    "id": "TN3_03",
    "topicId": 3,
    "topicName": "Biến ngẫu nhiên rời rạc, Kỳ vọng & Phương sai",
    "level": "Trung bình",
    "question": "Tiếp tục với biến ngẫu nhiên $X$ ở câu trên (có $E(X) = 1,6$). Phương sai $\\operatorname{Var}(X)$ bằng bao nhiêu?",
    "options": [
      "0,84",
      "3,40",
      "2,56",
      "0,9165"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo công thức phương sai $\\operatorname{Var}(X) = E(X^2) - [E(X)]^2$:\n- $E(X^2) = 0^2 \\cdot 0,1 + 1^2 \\cdot 0,4 + 2^2 \\cdot 0,3 + 3^2 \\cdot 0,2 = 0 + 0,4 + 1,2 + 1,8 = 3,4$.\n- $\\operatorname{Var}(X) = 3,4 - (1,6)^2 = 3,4 - 2,56 = 0,84$.\n\nPhân tích bẫy sai:\n- Phương án B: 3,40 mới chỉ là $E(X^2)$, chưa trừ $[E(X)]^2$.\n- Phương án C: 2,56 là $[E(X)]^2$.\n- Phương án D: $\\sqrt{0,84} \\approx 0,9165$ là độ lệch chuẩn $\\sigma(X)$, không phải phương sai.",
    "source": "Slide Week 07 tr. 8; Stat20 Mục 4.4"
  },
  {
    "id": "TN3_04",
    "topicId": 3,
    "topicName": "Biến ngẫu nhiên rời rạc, Kỳ vọng & Phương sai",
    "level": "Cơ bản",
    "question": "Cho biến ngẫu nhiên $X$ có $E(X) = 5$. Giá trị của $E(-3X + 8)$ là:",
    "options": [
      "23",
      "-7",
      "-15",
      "7"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì theo tính tuyến tính của kỳ vọng:\n$E(aX + b) = a \\cdot E(X) + b = (-3) \\cdot 5 + 8 = -15 + 8 = -7$.\n\nPhân tích bẫy sai:\n- Phương án A: Tính sai dấu: $3 \\cdot 5 + 8 = 23$.\n- Phương án C: Quên không cộng hằng số 8.\n- Phương án D: Sai dấu kết quả.",
    "source": "Slide Week 07 tr. 7; Stat20 Mục 4.3"
  },
  {
    "id": "TN3_05",
    "topicId": 3,
    "topicName": "Biến ngẫu nhiên rời rạc, Kỳ vọng & Phương sai",
    "level": "Cơ bản",
    "question": "Cho biến ngẫu nhiên $X$ có $\\operatorname{Var}(X) = 4$. Phương sai của biến ngẫu nhiên $Y = -3X + 8$ bằng bao nhiêu?",
    "options": [
      "-4",
      "44",
      "36",
      "-12"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì theo tính chất phương sai biến đổi tuyến tính:\n$\\operatorname{Var}(aX + b) = a^2 \\cdot \\operatorname{Var}(X)$.\nỞ đây $a = -3$ và $b = 8$, suy ra: $\\operatorname{Var}(-3X + 8) = (-3)^2 \\cdot 4 = 9 \\cdot 4 = 36$.\nHằng số $+8$ chỉ làm tịnh tiến toàn bộ phân phối, không ảnh hưởng đến độ phân tán quanh tâm.\n\nPhân tích bẫy sai:\n- Phương án A: Sai do tính $-3 \\cdot 4 + 8 = -4$ (áp dụng quy tắc kỳ vọng cho phương sai; hơn nữa phương sai không bao giờ âm!).\n- Phương án B: Sai do tính $9 \\cdot 4 + 8 = 44$ (vô tình cộng thêm hằng số 8).\n- Phương án D: Sai do tính $(-3) \\cdot 4 = -12$ (quên bình phương $a$).",
    "source": "Slide Week 07 tr. 9; Stat20 Mục 4.4"
  },
  {
    "id": "TN3_06",
    "topicId": 3,
    "topicName": "Biến ngẫu nhiên rời rạc, Kỳ vọng & Phương sai",
    "level": "Cơ bản",
    "question": "Cho hai biến ngẫu nhiên $X$ và $Y$ ĐỘC LẬP với nhau, biết $\\operatorname{Var}(X) = 5$ và $\\operatorname{Var}(Y) = 3$. Giá trị của $\\operatorname{Var}(X - Y)$ bằng bao nhiêu?",
    "options": [
      "2",
      "15",
      "\\(\\sqrt{8} \\approx 2,83\\)",
      "8"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì đối với hai biến ngẫu nhiên độc lập:\n$\\operatorname{Var}(X - Y) = \\operatorname{Var}(X + (-1)Y) = \\operatorname{Var}(X) + (-1)^2 \\operatorname{Var}(Y) = \\operatorname{Var}(X) + \\operatorname{Var}(Y) = 5 + 3 = 8$.\nĐộ bất định (phương sai) của hiệu hai nguồn biến thiên độc lập luôn CỘNG DỒN, không bao giờ triệt tiêu hay trừ lẫn nhau!\n\nPhân tích bẫy sai:\n- Phương án A: Bẫy sai kinh điển: lấy $5 - 3 = 2$ do nghĩ rằng hiệu thì phương sai cũng trừ đi.\n- Phương án B: Nhân $5 \\cdot 3 = 15$.\n- Phương án C: Độ lệch chuẩn $\\sqrt{8}$, không phải phương sai.",
    "source": "Slide Week 07 tr. 14; Stat20 Mục 4.4"
  },
  {
    "id": "TN3_07",
    "topicId": 3,
    "topicName": "Biến ngẫu nhiên rời rạc, Kỳ vọng & Phương sai",
    "level": "Cơ bản",
    "question": "Cho hai biến ngẫu nhiên $X$ và $Y$ có $E(X) = 10$ và $E(Y) = 15$. Chưa rõ $X$ và $Y$ có độc lập hay không. Giá trị của $E(2X + 3Y)$ bằng bao nhiêu?",
    "options": [
      "65",
      "Chưa đủ dữ kiện để tính vì chưa biết $X, Y$ có độc lập hay không",
      "50",
      "150"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì tính chất tuyến tính của kỳ vọng $E(aX + bY) = aE(X) + bE(Y)$ LUÔN LUÔN ĐÚNG trong mọi trường hợp, hoàn toàn KHÔNG CẦN điều kiện độc lập:\n$E(2X + 3Y) = 2 \\cdot 10 + 3 \\cdot 15 = 20 + 45 = 65$.\n(Điều kiện độc lập chỉ bắt buộc đối với phương sai hoặc tích $E(XY)$).\n\nPhân tích bẫy sai:\n- Phương án B: Nhầm lẫn điều kiện độc lập của phương sai sang kỳ vọng.\n- Phương án C, D: Sai số học.",
    "source": "Slide Week 07 tr. 12; Stat20 Mục 4.3"
  },
  {
    "id": "TN3_08",
    "topicId": 3,
    "topicName": "Biến ngẫu nhiên rời rạc, Kỳ vọng & Phương sai",
    "level": "Cơ bản",
    "question": "Nếu hai biến ngẫu nhiên $X$ và $Y$ độc lập với nhau, có $E(X) = 4$ và $E(Y) = 6$, thì $E(X \\cdot Y)$ bằng bao nhiêu?",
    "options": [
      "10",
      "24",
      "Chưa đủ dữ kiện vì cần biết phương sai",
      "0"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì theo định lý: Khi hai biến ngẫu nhiên độc lập thì kỳ vọng của tích bằng tích các kỳ vọng:\n$E(XY) = E(X) \\cdot E(Y) = 4 \\cdot 6 = 24$.\n\nPhân tích bẫy sai:\n- Phương án A: Lấy tổng $4 + 6 = 10$.\n- Phương án C: Không cần phương sai để tính $E(XY)$.\n- Phương án D: 0 là hiệp phương sai $\\operatorname{Cov}(X, Y) = 0$, không phải $E(XY)$.",
    "source": "Slide Week 07 tr. 13"
  },
  {
    "id": "TN3_09",
    "topicId": 3,
    "topicName": "Biến ngẫu nhiên rời rạc, Kỳ vọng & Phương sai",
    "level": "Cơ bản",
    "question": "Cho biến ngẫu nhiên rời rạc $X$ nhận các giá trị 1, 2, 3 với xác suất tương ứng là $0,3$; $0,5$; $0,2$. Giá trị của hàm phân phối tích lũy tại $x = 2,5$ (tức $F(2,5)$) bằng bao nhiêu?",
    "options": [
      "0,5",
      "0,3",
      "0,8",
      "1,0"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì theo định nghĩa hàm phân phối tích lũy:\n$F(2,5) = P(X \\le 2,5) = P(X = 1) + P(X = 2) = 0,3 + 0,5 = 0,8$.\n(Giá trị $X = 3$ lớn hơn 2,5 nên không được tính vào tích lũy).\n\nPhân tích bẫy sai:\n- Phương án A: 0,5 chỉ là $P(X=2)$.\n- Phương án B: 0,3 chỉ là $P(X=1)$.\n- Phương án D: 1,0 là $F(3)$ hoặc $F(x)$ khi $x \\ge 3$.",
    "source": "Slide Week 07 tr. 4; Stat20 Mục 4.2"
  },
  {
    "id": "TN3_10",
    "topicId": 3,
    "topicName": "Biến ngẫu nhiên rời rạc, Kỳ vọng & Phương sai",
    "level": "Trung bình",
    "question": "Cho hàm phân phối tích lũy $F(x)$ của biến ngẫu nhiên rời rạc $X$. Biết rằng $\\lim_{x \\to 3^-} F(x) = 0,40$ và $F(3) = 0,75$. Xác suất tại đúng điểm $x = 3$ ($P(X = 3)$) bằng bao nhiêu?",
    "options": [
      "0,75",
      "0,40",
      "1,15",
      "0,35"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì đối với biến ngẫu nhiên rời rạc, bước nhảy (độ gián đoạn) của hàm cdf tại điểm $x_0$ chính bằng xác suất tại điểm đó:\n$P(X = 3) = F(3) - \\lim_{x \\to 3^-} F(x) = 0,75 - 0,40 = 0,35$.\n\nPhân tích bẫy sai:\n- Phương án A: 0,75 là xác suất tích lũy $P(X \\le 3)$.\n- Phương án B: 0,40 là xác suất tích lũy nghiêm ngặt $P(X < 3)$.\n- Phương án C: Cộng hai giá trị $0,75 + 0,40 = 1,15$.",
    "source": "Slide Week 07 tr. 4; Stat20 Mục 4.2"
  },
  {
    "id": "TN3_11",
    "topicId": 3,
    "topicName": "Biến ngẫu nhiên rời rạc, Kỳ vọng & Phương sai",
    "level": "Trung bình",
    "question": "Cho biến ngẫu nhiên $X$ nhận giá trị 1 và 2 với xác suất bằng nhau ($P(X=1) = P(X=2) = 0,5$). So sánh giữa $E\\left(\\frac{1}{X}\\right)$ và $\\frac{1}{E(X)}$:",
    "options": [
      "\\(E\\left(\\frac{1}{X}\\right) = 0,75 > \\frac{1}{E(X)} \\approx 0,667\\)",
      "\\(E\\left(\\frac{1}{X}\\right) = \\frac{1}{E(X)} = 0,75\\)",
      "\\(E\\left(\\frac{1}{X}\\right) = 0,5 < \\frac{1}{E(X)} = 0,667\\)",
      "Không thể tính được vì hàm $1/X$ không có kỳ vọng"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo luật LOTUS và Bất đẳng thức Jensen (do hàm $g(x) = 1/x$ là hàm lồi nghiêm ngặt trên $(0, \\infty)$ nên $E(g(X)) > g(E(X))$):\n- $E(X) = 1 \\cdot 0,5 + 2 \\cdot 0,5 = 1,5 \\implies \\frac{1}{E(X)} = \\frac{1}{1,5} = \\frac{2}{3} \\approx 0,667$.\n- $E\\left(\\frac{1}{X}\\right) = \\frac{1}{1} \\cdot 0,5 + \\frac{1}{2} \\cdot 0,5 = 0,5 + 0,25 = 0,75$.\nDo đó $E\\left(\\frac{1}{X}\\right) > \\frac{1}{E(X)}$. Đây là bài học quan trọng: Kỳ vọng không được giao hoán qua các hàm phi tuyến!\n\nPhân tích bẫy sai:\n- Phương án B: Bẫy ngây thơ coi $E(g(X)) = g(E(X))$.\n- Phương án C, D: Sai kết quả tính toán.",
    "source": "Slide Week 07 tr. 7; Stat20 Mục 4.3"
  },
  {
    "id": "TN3_12",
    "topicId": 3,
    "topicName": "Biến ngẫu nhiên rời rạc, Kỳ vọng & Phương sai",
    "level": "Cơ bản",
    "question": "Gọi $I_A$ là biến ngẫu nhiên chỉ thị của biến cố $A$ ($I_A = 1$ nếu $A$ xảy ra, $I_A = 0$ nếu $A$ không xảy ra), với $P(A) = p$. Kỳ vọng và phương sai của $I_A$ lần lượt là:",
    "options": [
      "$E(I_A) = 1$ và $\\operatorname{Var}(I_A) = p$",
      "$E(I_A) = p$ và $\\operatorname{Var}(I_A) = p(1 - p)$",
      "$E(I_A) = p$ và $\\operatorname{Var}(I_A) = p^2$",
      "$E(I_A) = p^2$ và $\\operatorname{Var}(I_A) = p(1 - p)$"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì biến chỉ thị $I_A$ thực chất là biến Bernoulli($p$):\n- $E(I_A) = 1 \\cdot P(A) + 0 \\cdot P(\\bar{A}) = p$.\n- $E(I_A^2) = 1^2 \\cdot p + 0^2 \\cdot (1-p) = p$ (vì $I_A^2 = I_A$).\n- $\\operatorname{Var}(I_A) = E(I_A^2) - [E(I_A)]^2 = p - p^2 = p(1 - p)$.\n\nPhân tích bẫy sai:\n- Phương án A, C, D: Sai công thức toán học cơ bản của biến chỉ thị.",
    "source": "Slide Week 07 tr. 10; Stat20 Mục 4.8"
  },
  {
    "id": "TN3_13",
    "topicId": 3,
    "topicName": "Biến ngẫu nhiên rời rạc, Kỳ vọng & Phương sai",
    "level": "Trung bình",
    "question": "Cho $X$ và $Y$ là hai biến ngẫu nhiên độc lập có $\\operatorname{Var}(X) = 2$ và $\\operatorname{Var}(Y) = 3$. Phương sai của biến $Z = 2X - 3Y + 5$ bằng bao nhiêu?",
    "options": [
      "40",
      "-1",
      "35",
      "13"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì:\n$\\operatorname{Var}(2X - 3Y + 5) = 2^2 \\operatorname{Var}(X) + (-3)^2 \\operatorname{Var}(Y) = 4 \\cdot 2 + 9 \\cdot 3 = 8 + 27 = 35$.\nHằng số $+5$ không làm đổi phương sai.\n\nPhân tích bẫy sai:\n- Phương án A: Sai do cộng thêm hằng số 5 ($35 + 5 = 40$).\n- Phương án B: Sai do tính $4 \\cdot 2 - 9 \\cdot 3 = 8 - 27 = -19$ hoặc $2(2) - 3(3) + 5 = 0$.\n- Phương án D: Sai do quên không bình phương các hệ số: $2 \\cdot 2 + 3 \\cdot 3 = 13$.",
    "source": "Slide Week 07 tr. 9; Stat20 Mục 4.4"
  },
  {
    "id": "TN3_14",
    "topicId": 3,
    "topicName": "Biến ngẫu nhiên rời rạc, Kỳ vọng & Phương sai",
    "level": "Trung bình",
    "question": "Nếu $\\operatorname{Cov}(X, Y) = 0$, ta có thể rút ra kết luận nào sau đây?",
    "options": [
      "$X$ và $Y$ chắc chắn độc lập với nhau",
      "Phương sai của $X$ bằng phương sai của $Y$",
      "$P(X = x, Y = y) = P(X = x) \\cdot P(Y = y)$ với mọi $x, y$",
      "$X$ và $Y$ không có tương quan tuyến tính ($E(XY) = E(X)E(Y)$), nhưng chưa chắc độc lập"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì theo định lý: Độc lập kéo theo $\\operatorname{Cov}(X, Y) = 0$, nhưng điều ngược lại KHÔNG đúng. $\\operatorname{Cov}(X, Y) = 0$ chỉ khẳng định không có quan hệ tuyến tính; giữa $X$ và $Y$ hoàn toàn có thể tồn tại mối quan hệ phi tuyến hoàn hảo (ví dụ $X \\sim U(-1, 1)$ và $Y = X^2$ có $\\operatorname{Cov}(X, Y) = 0$ nhưng $Y$ phụ thuộc hoàn toàn vào $X$).\n\nPhân tích bẫy sai:\n- Phương án A: Bẫy suy luận đảo ngược sai lầm (không tương quan $\\neq$ độc lập).\n- Phương án B: Không liên quan.\n- Phương án C: Đây là định nghĩa độc lập toàn phần, điều mà $\\operatorname{Cov}=0$ chưa đủ đảm bảo.",
    "source": "Slide Week 07 tr. 13"
  },
  {
    "id": "TN3_15",
    "topicId": 3,
    "topicName": "Biến ngẫu nhiên rời rạc, Kỳ vọng & Phương sai",
    "level": "Trung bình",
    "question": "Bảng phân phối xác suất đồng thời của hai biến ngẫu nhiên $X$ và $Y$ như sau:\n$P(X=0, Y=1) = 0,2$; $P(X=0, Y=2) = 0,3$;\n$P(X=1, Y=1) = 0,1$; $P(X=1, Y=2) = 0,4$.\nKỳ vọng biên $E(X)$ bằng bao nhiêu?",
    "options": [
      "0,5",
      "0,7",
      "1,7",
      "0,4"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì để tính $E(X)$, trước hết ta tìm phân phối biên của $X$ bằng cách cộng theo hàng:\n- $P(X = 0) = P(X=0, Y=1) + P(X=0, Y=2) = 0,2 + 0,3 = 0,5$.\n- $P(X = 1) = P(X=1, Y=1) + P(X=1, Y=2) = 0,1 + 0,4 = 0,5$.\nKỳ vọng: $E(X) = 0 \\cdot 0,5 + 1 \\cdot 0,5 = 0,5$.\n\nPhân tích bẫy sai:\n- Phương án B: Sai do tính $E(XY) = 0 + 0 + 1 \\cdot 1 \\cdot 0,1 + 1 \\cdot 2 \\cdot 0,4 = 0,1 + 0,8 = 0,9$ rồi nhầm sang số khác.\n- Phương án C: 1,7 là kỳ vọng biên của $Y$ ($P(Y=1)=0,3, P(Y=2)=0,7 \\implies E(Y) = 1 \\cdot 0,3 + 2 \\cdot 0,7 = 1,7$).\n- Phương án D: Sai số học.",
    "source": "Slide Week 07 tr. 11"
  },
  {
    "id": "TN3_16",
    "topicId": 3,
    "topicName": "Biến ngẫu nhiên rời rạc, Kỳ vọng & Phương sai",
    "level": "Trung bình",
    "question": "Với bảng phân phối đồng thời ở câu trên ($P(X=0, Y=1) = 0,2$; $P(X=0) = 0,5$; $P(Y=1) = 0,3$), hai biến ngẫu nhiên $X$ và $Y$ có độc lập với nhau hay không?",
    "options": [
      "Độc lập vì tổng xác suất toàn bảng bằng 1",
      "Không độc lập vì $P(X=0, Y=1) = 0,2 \\neq P(X=0) \\cdot P(Y=1) = 0,15$",
      "Độc lập vì $E(X)$ và $E(Y)$ đều tính được",
      "Không thể xác định vì cần biết phương sai của $X$"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì theo định nghĩa độc lập của hai biến ngẫu nhiên rời rạc, đẳng thức $P(X=x, Y=y) = P(X=x) \\cdot P(Y=y)$ phải thỏa mãn với MỌI cặp $(x, y)$.\nTại cặp $(0, 1)$:\n- $P(X=0, Y=1) = 0,20$.\n- $P(X=0) \\cdot P(Y=1) = 0,5 \\cdot 0,3 = 0,15 \\neq 0,20$.\nDo vi phạm ngay tại cặp này nên $X$ và $Y$ không độc lập.\n\nPhân tích bẫy sai:\n- Phương án A, C: Bảng phân phối nào cũng có tổng bằng 1 và tính được kỳ vọng, không liên quan đến tính độc lập.\n- Phương án D: Không cần biết phương sai.",
    "source": "Slide Week 07 tr. 11"
  },
  {
    "id": "TN3_17",
    "topicId": 3,
    "topicName": "Biến ngẫu nhiên rời rạc, Kỳ vọng & Phương sai",
    "level": "Nâng cao",
    "question": "Một người bán báo nhập 20 tờ báo mỗi sáng với giá 5.000 đ/tờ và bán ra với giá 8.000 đ/tờ. Báo không bán hết trong ngày bị vứt bỏ (lỗ hoàn toàn). Nhu cầu mua báo trong ngày ($D$) có phân phối: $P(D = 10) = 0,2$; $P(D = 20) = 0,5$; $P(D = 30) = 0,3$. Lợi nhuận kỳ vọng của người bán báo mỗi sáng là bao nhiêu?",
    "options": [
      "60.000 đồng",
      "63.000 đồng",
      "44.000 đồng",
      "30.000 đồng"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì lợi nhuận tính theo số báo thực tế bán được $\\min(D, 20)$ trừ đi chi phí nhập 20 tờ ($20 \\times 5.000 = 100.000$ đ):\n- Nếu $D = 10$ (xác suất 0,2): bán được 10 tờ $\\implies \\text{Lợi nhuận} = 10 \\times 8.000 - 100.000 = -20.000$ đ.\n- Nếu $D = 20$ (xác suất 0,5): bán được 20 tờ $\\implies \\text{Lợi nhuận} = 20 \\times 8.000 - 100.000 = +60.000$ đ.\n- Nếu $D = 30$ (xác suất 0,3): do chỉ nhập 20 tờ nên chỉ bán được 20 tờ $\\implies \\text{Lợi nhuận} = 20 \\times 8.000 - 100.000 = +60.000$ đ.\nLợi nhuận kỳ vọng:\n$E(\\text{Lợi nhuận}) = (-20.000) \\cdot 0,2 + 60.000 \\cdot 0,5 + 60.000 \\cdot 0,3 = -4.000 + 30.000 + 18.000 = 44.000$ đồng.\n\nPhân tích bẫy sai:\n- Phương án A: Bẫy coi như luôn bán hết 20 tờ ($60.000$ đ).\n- Phương án B: Bẫy tính nhu cầu kỳ vọng $E(D) = 10 \\cdot 0,2 + 20 \\cdot 0,5 + 30 \\cdot 0,3 = 21$ tờ, rồi lấy $21 \\times 3.000 = 63.000$ đ (sai vì số bán bị giới hạn trần ở 20).\n- Phương án D: Sai số học.",
    "source": "Slide Week 07 tr. 7"
  },
  {
    "id": "TN3_18",
    "topicId": 3,
    "topicName": "Biến ngẫu nhiên rời rạc, Kỳ vọng & Phương sai",
    "level": "Trung bình",
    "question": "Cho biến ngẫu nhiên $X$ nhận các giá trị: $-2$ (xác suất 0,3), $0$ (xác suất 0,4), $+3$ (xác suất 0,3). Phương sai $\\operatorname{Var}(X)$ bằng bao nhiêu?",
    "options": [
      "3,90",
      "0,30",
      "2,19",
      "3,81"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì:\n- Kỳ vọng: $E(X) = (-2) \\cdot 0,3 + 0 \\cdot 0,4 + 3 \\cdot 0,3 = -0,6 + 0,9 = 0,3$.\n- Kỳ vọng bình phương: $E(X^2) = (-2)^2 \\cdot 0,3 + 0^2 \\cdot 0,4 + 3^2 \\cdot 0,3 = 4 \\cdot 0,3 + 0 + 9 \\cdot 0,3 = 1,2 + 2,7 = 3,9$.\n- Phương sai: $\\operatorname{Var}(X) = E(X^2) - [E(X)]^2 = 3,9 - 0,3^2 = 3,9 - 0,09 = 3,81$.\n\nPhân tích bẫy sai:\n- Phương án A: 3,90 mới chỉ là $E(X^2)$, chưa trừ $[E(X)]^2$.\n- Phương án B: 0,30 là $E(X)$.\n- Phương án C: Sai dấu bình phương $(-2)^2 = -4 \\implies E(X^2) = -1,2 + 2,7 = 1,5 \\implies 1,5 - 0,09 = 1,41$ hoặc sai phép tính.",
    "source": "Slide Week 07 tr. 8"
  },
  {
    "id": "TN3_19",
    "topicId": 3,
    "topicName": "Biến ngẫu nhiên rời rạc, Kỳ vọng & Phương sai",
    "level": "Trung bình",
    "question": "Trong trò chơi Cò quay Roulette kiểu Mỹ có 38 ô: 18 ô Đỏ, 18 ô Đen và 2 ô Xanh lá (0 và 00). Một người chơi đặt cược 100.000 đồng vào cửa Đỏ. Nếu bóng rơi vào ô Đỏ, người chơi nhận lại 100.000 đồng vốn và được thưởng thêm 100.000 đồng; nếu bóng rơi vào Đen hoặc Xanh, người chơi mất toàn bộ 100.000 đồng tiền cược. Kỳ vọng số tiền lãi/lỗ của người chơi sau mỗi lượt cược là bao nhiêu?",
    "options": [
      "-5.263 đồng (tức lỗ trung bình khoảng 5,26%)",
      "0 đồng (trò chơi công bằng)",
      "+5.263 đồng",
      "-50.000 đồng"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì:\n- Xác suất thắng (ra Đỏ): $P(\\text{thắng}) = \\frac{18}{38}$. Lợi nhuận: $+100.000$ đ.\n- Xác suất thua (ra Đen hoặc Xanh): $P(\\text{thua}) = \\frac{20}{38}$. Lợi nhuận: $-100.000$ đ.\nKỳ vọng lợi nhuận:\n$E(X) = (+100.000) \\cdot \\frac{18}{38} + (-100.000) \\cdot \\frac{20}{38} = 100.000 \\cdot \\frac{-2}{38} \\approx -5.263$ đồng.\n(Đây chính là lợi thế nhà cái house edge bằng $2/38 \\approx 5,26\\%$).\n\nPhân tích bẫy sai:\n- Phương án B: Ảo tưởng trò chơi công bằng do quên mất 2 ô xanh lá nhà cái (0 và 00).\n- Phương án C: Sai dấu (người chơi luôn có kỳ vọng âm).\n- Phương án D: Sai số học.",
    "source": "Stat20 Mục 4.3; Slide Week 07 tr. 7"
  },
  {
    "id": "TN3_20",
    "topicId": 3,
    "topicName": "Biến ngẫu nhiên rời rạc, Kỳ vọng & Phương sai",
    "level": "Cơ bản",
    "question": "Cho $X_1, X_2, \\dots, X_{16}$ là 16 biến ngẫu nhiên độc lập cùng phân phối (i.i.d.) có độ lệch chuẩn $\\sigma = 12$. Độ lệch chuẩn của biến trung bình mẫu $\\bar{X} = \\frac{1}{16} \\sum_{i=1}^{16} X_i$ bằng bao nhiêu?",
    "options": [
      "0,75",
      "3",
      "48",
      "12"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì theo quy luật căn bậc hai đối với trung bình mẫu của $n$ biến i.i.d.:\n$\\sigma(\\bar{X}) = \\frac{\\sigma}{\\sqrt{n}} = \\frac{12}{\\sqrt{16}} = \\frac{12}{4} = 3$.\n\nPhân tích bẫy sai:\n- Phương án A: Sai do chia cho $n=16$ thay vì $\\sqrt{n}$ ($12/16 = 0,75$).\n- Phương án C: Nhầm sang độ lệch chuẩn của TỔNG: $\\sigma(S_n) = \\sigma\\sqrt{n} = 12 \\cdot 4 = 48$.\n- Phương án D: Giữ nguyên $\\sigma = 12$ là sai vì trung bình mẫu phải có độ phân tán nhỏ hơn từng quan sát đơn lẻ.",
    "source": "Slide Week 07 tr. 25; Stat20 Mục 4.13"
  },
  {
    "id": "TN3_21",
    "topicId": 3,
    "topicName": "Biến ngẫu nhiên rời rạc, Kỳ vọng & Phương sai",
    "level": "Cơ bản",
    "question": "Với mọi biến ngẫu nhiên $X$ có phương sai hữu hạn, bất đẳng thức nào sau đây luôn luôn ĐÚNG?",
    "options": [
      "\\(E(X^2) < [E(X)]^2\\)",
      "\\(E(X^2) = [E(X)]^2\\) với mọi biến ngẫu nhiên",
      "\\(E(X^2) \\ge [E(X)]^2\\), dấu bằng xảy ra khi và chỉ khi $X$ là một hằng số chắc chắn",
      "\\(E(X^2) \\le E(X)\\)"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì phương sai định nghĩa là trung bình của bình phương độ lệch nên không bao giờ âm:\n$\\operatorname{Var}(X) = E(X^2) - [E(X)]^2 \\ge 0 \\implies E(X^2) \\ge [E(X)]^2$.\nDấu bằng xảy ra khi và chỉ khi $\\operatorname{Var}(X) = 0$, nghĩa là $X$ không hề có tính ngẫu nhiên mà là một hằng số chắc chắn ($P(X = c) = 1$).\n\nPhân tích bẫy sai:\n- Phương án A, B, D: Đều trái ngược với định lý cơ bản về phương sai.",
    "source": "Slide Week 07 tr. 8"
  },
  {
    "id": "TN3_22",
    "topicId": 3,
    "topicName": "Biến ngẫu nhiên rời rạc, Kỳ vọng & Phương sai",
    "level": "Nâng cao",
    "question": "Cho hai biến ngẫu nhiên $X$ và $Y$ có hiệp phương sai $\\operatorname{Cov}(X, Y) = 2$. Giá trị của $\\operatorname{Cov}(-2X, 3Y)$ bằng bao nhiêu?",
    "options": [
      "12",
      "-6",
      "2",
      "-12"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì theo tính song tuyến tính (bilinearity) của hiệp phương sai:\n$\\operatorname{Cov}(aX, bY) = a \\cdot b \\cdot \\operatorname{Cov}(X, Y)$.\nỞ đây $a = -2$ và $b = 3$, do đó: $\\operatorname{Cov}(-2X, 3Y) = (-2) \\cdot 3 \\cdot 2 = -12$.\n\nPhân tích bẫy sai:\n- Phương án A: Quên dấu âm của hệ số $a=-2$.\n- Phương án B: Sai do lấy tích hai hệ số $(-2) \\cdot 3 = -6$ mà quên nhân hiệp phương sai gốc là 2.\n- Phương án C: Giữ nguyên giá trị cũ.",
    "source": "Slide Week 07 tr. 13"
  },
  {
    "id": "TN4_01",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Cơ bản",
    "question": "Một kiện hàng có 30 sản phẩm, trong đó có 6 phế phẩm. Người kiểm tra rút ngẫu nhiên lần lượt 5 sản phẩm KHÔNG HOÀN LẠI để kiểm tra. Gọi $X$ là số phế phẩm tìm thấy trong 5 sản phẩm đó. Biến ngẫu nhiên $X$ tuân theo phân phối nào?",
    "options": [
      "Phân phối Siêu bội (Hypergeometric)",
      "Phân phối Nhị thức (Binomial)",
      "Phân phối Poisson",
      "Phân phối Chuẩn (Normal)"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì phép thử rút không hoàn lại từ một tập hợp hữu hạn ($N=30$, có $M=6$ phế phẩm, lấy mẫu kích thước $n=5$) khiến xác suất rút được phế phẩm thay đổi sau mỗi lần rút (các lần rút phụ thuộc). Do đó số phế phẩm $X$ tuân theo phân phối Siêu bội $X \\sim HG(N=30, M=6, n=5)$.\n\nPhân tích bẫy sai:\n- Phương án B: Nhị thức chỉ áp dụng khi rút CÓ HOÀN LẠI (xác suất $p$ không đổi qua các lần rút).\n- Phương án C: Poisson dùng để đếm số biến cố xảy ra trong một khoảng thời gian/không gian liên tục.\n- Phương án D: $X$ là biến rời rạc đếm được, không thể là phân phối liên tục Chuẩn.",
    "source": "Slide Week 07 tr. 15; Stat20 Mục 4.9"
  },
  {
    "id": "TN4_02",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Cơ bản",
    "question": "Số lượng tin nhắn rác gửi đến một hòm thư điện tử trong khoảng thời gian từ 8h00 đến 9h00 sáng mỗi ngày thường được mô hình hóa phù hợp nhất bằng phân phối xác suất nào sau đây?",
    "options": [
      "Phân phối Siêu bội",
      "Phân phối Poisson",
      "Phân phối Đều rời rạc",
      "Phân phối Bernoulli"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì biến số đếm số lần xảy ra của một sự kiện ngẫu nhiên độc lập trong một khoảng thời gian liên tục cố định với tốc độ xuất hiện trung bình không đổi là định nghĩa tiêu chuẩn của Phân phối Poisson $Po(\\lambda)$.\n\nPhân tích bẫy sai:\n- Phương án A: Siêu bội chỉ dùng cho rút không hoàn lại từ tập hữu hạn.\n- Phương án C: Đều rời rạc đòi hỏi các số lượng tin nhắn khác nhau phải có cùng xác suất (vô lý trong thực tế).\n- Phương án D: Bernoulli chỉ nhận 2 giá trị 0 hoặc 1.",
    "source": "Slide Week 07 tr. 16; Stat20 Mục 4.10"
  },
  {
    "id": "TN4_03",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Cơ bản",
    "question": "Một bài thi trắc nghiệm gồm 20 câu hỏi độc lập, mỗi câu có 4 phương án trả lời và chỉ có 1 phương án đúng. Một thí sinh chọn ngẫu nhiên hoàn toàn cả 20 câu. Gọi $X$ là số câu trả lời đúng. Kỳ vọng và phương sai của $X$ lần lượt là:",
    "options": [
      "E(X) = 5 và Var(X) = 5",
      "E(X) = 5 và Var(X) = 1,9365",
      "E(X) = 5 và Var(X) = 3,75",
      "E(X) = 4 và Var(X) = 3"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì $X \\sim B(n=20, p=0,25)$:\n- Kỳ vọng: $E(X) = np = 20 \\cdot 0,25 = 5$.\n- Phương sai: $\\operatorname{Var}(X) = np(1-p) = 20 \\cdot 0,25 \\cdot 0,75 = 3,75$.\n\nPhân tích bẫy sai:\n- Phương án A: Nhầm sang tính chất của phân phối Poisson (Var = E = 5).\n- Phương án B: $\\sqrt{3,75} \\approx 1,9365$ là độ lệch chuẩn $\\sigma$, không phải phương sai.\n- Phương án D: Sai phép tính.",
    "source": "Slide Week 07 tr. 15; Stat20 Mục 4.8"
  },
  {
    "id": "TN4_04",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Cơ bản",
    "question": "Cho biến ngẫu nhiên $X \\sim B(n = 5, p = 0,4)$. Xác suất $P(X = 2)$ bằng bao nhiêu?",
    "options": [
      "0,03456",
      "0,2304",
      "0,0864",
      "0,3456"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì áp dụng công thức hàm xác suất nhị thức:\n$P(X = 2) = C_5^2 \\cdot (0,4)^2 \\cdot (1 - 0,4)^{5-2} = 10 \\cdot 0,16 \\cdot (0,6)^3 = 10 \\cdot 0,16 \\cdot 0,216 = 0,3456$.\n\nPhân tích bẫy sai:\n- Phương án A: Sai do dịch dấu phẩy thập phân.\n- Phương án B: $0,2304$ là $P(X=1)$.\n- Phương án C: $0,0864$ là kết quả khi quên nhân hệ số tổ hợp $C_5^2 = 10$ ($0,16 \\cdot 0,216 = 0,03456$).",
    "source": "Slide Week 07 tr. 15; Stat20 Mục 4.8"
  },
  {
    "id": "TN4_05",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Cơ bản",
    "question": "Biến ngẫu nhiên $X \\sim Po(\\lambda = 4)$. Độ lệch chuẩn $\\sigma(X)$ của $X$ bằng bao nhiêu?",
    "options": [
      "2",
      "4",
      "16",
      "0,25"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì đối với phân phối Poisson $Po(\\lambda)$:\n- Kỳ vọng $E(X) = \\lambda = 4$.\n- Phương sai $\\operatorname{Var}(X) = \\lambda = 4$.\n- Do đó độ lệch chuẩn là căn bậc hai của phương sai: $\\sigma(X) = \\sqrt{\\operatorname{Var}(X)} = \\sqrt{4} = 2$.\n\nPhân tích bẫy sai:\n- Phương án B: 4 là phương sai $\\operatorname{Var}(X)$, câu hỏi hỏi độ lệch chuẩn $\\sigma$.\n- Phương án C: Bình phương nhầm phương sai $4^2 = 16$.\n- Phương án D: Nghịch đảo $1/4 = 0,25$.",
    "source": "Slide Week 07 tr. 16; Stat20 Mục 4.10"
  },
  {
    "id": "TN4_06",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Cơ bản",
    "question": "Trung bình mỗi phút có 3 cuộc gọi đến một tổng đài ($X \\sim Po(3)$). Xác suất để trong một phút bất kỳ KHÔNG CÓ cuộc gọi nào đến tổng đài ($P(X = 0)$) là:",
    "options": [
      "0",
      "\\(e^{-3} \\approx 0,0498\\)",
      "\\(1 - e^{-3} \\approx 0,9502\\)",
      "\\(3 \\cdot e^{-3} \\approx 0,1494\\)"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì theo công thức Poisson với $k = 0$:\n$P(X = 0) = \\frac{\\lambda^0 e^{-\\lambda}}{0!} = \\frac{1 \\cdot e^{-3}}{1} = e^{-3} \\approx 0,0498$ (khoảng 4,98%).\n\nPhân tích bẫy sai:\n- Phương án A: Ngộ nhận rằng trung bình có 3 cuộc gọi thì xác suất 0 cuộc gọi phải bằng 0.\n- Phương án C: $1 - e^{-3}$ là xác suất CÓ ÍT NHẤT một cuộc gọi ($P(X \\ge 1)$).\n- Phương án D: $3 e^{-3}$ là xác suất có ĐÚNG 1 cuộc gọi ($P(X = 1)$).",
    "source": "Slide Week 07 tr. 16; Stat20 Mục 4.10"
  },
  {
    "id": "TN4_07",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Cơ bản",
    "question": "Phân phối Nhị thức $B(n, p)$ có thể được xấp xỉ tốt bởi phân phối Poisson $Po(\\lambda = np)$ trong điều kiện nào sau đây?",
    "options": [
      "Số phép thử $n$ rất nhỏ và $p$ rất gần 0,5",
      "Cả $n$ và $p$ đều rất lớn",
      "Số phép thử $n$ rất lớn ($n \\ge 20$ hoặc $n \\ge 100$) và xác suất thành công $p$ rất nhỏ ($p \\le 0,05$), sao cho tích $\\lambda = np$ ở mức vừa phải ($np \\le 10$)",
      "Khi $p = 0,5$ và $n \\ge 30$"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì theo Luật các biến cố hiếm (Law of Rare Events), phân phối Nhị thức hội tụ về Poisson khi $n \\to \\infty$ và $p \\to 0$ sao cho tích $np = \\lambda$ là một hằng số hữu hạn. Quy tắc thực hành là $n$ lớn ($n \\ge 20$ hoặc $100$) và $p$ nhỏ ($p \\le 0,05$), tích $np \\le 10$.\n\nPhân tích bẫy sai:\n- Phương án A, B: Sai điều kiện lý thuyết.\n- Phương án D: Khi $p = 0,5$ và $n \\ge 30$, ta phải dùng xấp xỉ CHUẨN (Normal approximation / CLT), không dùng Poisson vì $p$ không hề nhỏ.",
    "source": "Slide Week 07 tr. 16; Stat20 Mục 4.10"
  },
  {
    "id": "TN4_08",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Trung bình",
    "question": "Tỷ lệ một người bị dị ứng nghiêm trọng sau khi tiêm một loại vắc-xin là $p = 0,002$. Tiêm vắc-xin này cho $n = 1.000$ người độc lập. Sử dụng xấp xỉ Poisson, xác suất có đúng 3 người bị dị ứng xấp xỉ bằng bao nhiêu?",
    "options": [
      "0,2707",
      "0,1353",
      "0,0613",
      "0,1804"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì:\n- Ta có $n = 1.000$ rất lớn và $p = 0,002$ rất nhỏ $\\implies \\lambda = n \\cdot p = 1.000 \\cdot 0,002 = 2$.\n- Dùng xấp xỉ Poisson $Po(\\lambda = 2)$ để tính xác suất tại $k = 3$:\n$P(X = 3) \\approx \\frac{2^3 \\cdot e^{-2}}{3!} = \\frac{8 \\cdot e^{-2}}{6} = \\frac{4}{3} \\cdot e^{-2} \\approx \\frac{4}{3} \\cdot 0,135335 \\approx 0,1804$ (tức 18,04%).\n\nPhân tích bẫy sai:\n- Phương án A: 0,2707 là xác suất tại $k=1$ hoặc $k=2$ ($2^2 e^{-2} / 2 = 2 e^{-2} \\approx 0,2707$).\n- Phương án B: 0,1353 là xác suất tại $k=0$ ($e^{-2} \\approx 0,1353$).\n- Phương án C: Sai số học.",
    "source": "Slide Week 07 tr. 16; Stat20 Mục 4.10"
  },
  {
    "id": "TN4_09",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Trung bình",
    "question": "Giả sử một lô hàng có $N$ sản phẩm, trong đó có $M$ phế phẩm ($p = M/N$). Rút ngẫu nhiên $n$ sản phẩm. So sánh phương sai của số phế phẩm khi rút KHÔNG HOÀN LẠI (Siêu bội) so với khi rút CÓ HOÀN LẠI (Nhị thức):",
    "options": [
      "Phương sai của Siêu bội luôn NHỎ HƠN phương sai của Nhị thức do có hệ số hiệu chỉnh tổng thể hữu hạn \\(\\frac{N-n}{N-1} < 1\\)",
      "Phương sai của Siêu bội luôn LỚN HƠN phương sai của Nhị thức",
      "Phương sai của hai phân phối luôn bằng nhau và cùng bằng $np(1-p)$",
      "Kỳ vọng của Siêu bội nhỏ hơn kỳ vọng của Nhị thức"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo công thức phương sai siêu bội:\n$\\operatorname{Var}_{HG}(X) = n p (1 - p) \\cdot \\frac{N - n}{N - 1} = \\operatorname{Var}_{Binomial}(X) \\cdot \\frac{N - n}{N - 1}$.\nVới $n > 1$, hệ số hiệu chỉnh tổng thể hữu hạn $\\frac{N-n}{N-1} < 1$. Ý nghĩa thực tế: việc rút không hoàn lại loại bỏ dần các phần tử đã lấy, làm giảm độ bất định của các lần rút sau so với việc rút có hoàn lại!\nChú ý: Cả hai đều có CÙNG kỳ vọng $E(X) = n \\frac{M}{N} = np$.\n\nPhân tích bẫy sai:\n- Phương án B: Ngược với bản chất toán học.\n- Phương án C: Bẫy ngộ nhận hai phương sai bằng nhau.\n- Phương án D: Sai vì kỳ vọng của chúng hoàn toàn bằng nhau.",
    "source": "Slide Week 07 tr. 15; Stat20 Mục 4.9"
  },
  {
    "id": "TN4_10",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Cơ bản",
    "question": "Một tổ có 50 sinh viên, trong đó có 10 sinh viên giỏi. Chọn ngẫu nhiên không hoàn lại 5 sinh viên đi dự đại hội. Số sinh viên giỏi kỳ vọng có mặt trong đoàn đại biểu là:",
    "options": [
      "0,5 sinh viên",
      "1,0 sinh viên",
      "2,0 sinh viên",
      "0,2 sinh viên"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì áp dụng công thức kỳ vọng của phân phối Siêu bội $X \\sim HG(N=50, M=10, n=5)$:\n$E(X) = n \\cdot \\frac{M}{N} = 5 \\cdot \\frac{10}{50} = 5 \\cdot 0,2 = 1,0$ sinh viên.\n\nPhân tích bẫy sai:\n- Phương án A: Sai do tính $5 \\cdot 10 / 100 = 0,5$.\n- Phương án C: Sai phép tính.\n- Phương án D: 0,2 mới chỉ là tỷ lệ sinh viên giỏi trong tổ ($M/N$), chưa nhân kích thước mẫu $n=5$.",
    "source": "Slide Week 07 tr. 15; Stat20 Mục 4.9"
  },
  {
    "id": "TN4_11",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Trung bình",
    "question": "Khách hàng đến một cây ATM với tốc độ trung bình 2 người/phút theo phân phối Poisson. Tốc độ trung bình số khách đến cây ATM trong một khoảng thời gian 3 phút là bao nhiêu và xác suất có đúng 5 khách đến trong 3 phút đó là bao nhiêu?",
    "options": [
      "\\(\\lambda' = 2\\) khách và \\(P(X = 5) \\approx 0,0361\\)",
      "\\(\\lambda' = 6\\) khách và \\(P(X = 5) \\approx 0,0803\\)",
      "\\(\\lambda' = 6\\) khách và \\(P(X = 5) \\approx 0,1606\\)",
      "\\(\\lambda' = 5\\) khách và \\(P(X = 5) \\approx 0,1755\\)"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì theo tính chất tỷ lệ của quá trình Poisson:\n- Khi khoảng thời gian tăng lên $t = 3$ phút, tham số Poisson mới tỷ lệ thuận theo thời gian: $\\lambda' = \\lambda \\cdot t = 2 \\times 3 = 6$ khách.\n- Xác suất có đúng 5 khách trong 3 phút này:\n$P(X = 5) = \\frac{(\\lambda')^5 \\cdot e^{-\\lambda'}}{5!} = \\frac{6^5 \\cdot e^{-6}}{120} = \\frac{7.776 \\cdot e^{-6}}{120} = 64,8 \\cdot e^{-6} \\approx 0,1606$ (tức 16,06%).\n\nPhân tích bẫy sai:\n- Phương án A: Sai do giữ nguyên $\\lambda = 2$ của 1 phút thay vì nhân với 3 phút.\n- Phương án B: Sai số học khi chia cho $5!$.\n- Phương án D: Nhầm tham số $\\lambda$ thành số khách cần tính.",
    "source": "Slide Week 07 tr. 16; Stat20 Mục 4.10"
  },
  {
    "id": "TN4_12",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Trung bình",
    "question": "Một hộp có 8 viên bi đỏ và 4 viên bi xanh (tổng cộng 12 viên bi). Rút ngẫu nhiên đồng thời 3 viên bi. Xác suất để rút được đúng 2 viên bi đỏ bằng bao nhiêu?",
    "options": [
      "14/55 (khoảng 25,45%)",
      "4/11 (khoảng 36,36%)",
      "2/3 (khoảng 66,67%)",
      "28/55 (khoảng 50,91%)"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì áp dụng công thức phân phối Siêu bội $HG(N=12, M=8, n=3)$:\n- Số cách chọn 2 bi đỏ từ 8 bi đỏ: $C_8^2 = \\frac{8 \\cdot 7}{2} = 28$.\n- Số cách chọn 1 bi xanh từ 4 bi xanh: $C_4^1 = 4$.\n- Số cách chọn 3 bi bất kỳ từ 12 bi: $C_{12}^3 = \\frac{12 \\cdot 11 \\cdot 10}{6} = 220$.\n- Xác suất: $P(X = 2) = \\frac{C_8^2 \\cdot C_4^1}{C_{12}^3} = \\frac{28 \\cdot 4}{220} = \\frac{112}{220} = \\frac{28}{55} \\approx 0,5091$ (50,91%).\n\nPhân tích bẫy sai:\n- Phương án A: 14/55 là xác suất rút được đúng 1 bi đỏ ($C_8^1 C_4^2 / 220 = 8 \\cdot 6 / 220 = 48/220 = 12/55$).\n- Phương án B, C: Phép tính sai tổ hợp.",
    "source": "Slide Week 07 tr. 15; Stat20 Mục 4.9"
  },
  {
    "id": "TN4_13",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Nâng cao",
    "question": "Cho biến ngẫu nhiên $X \\sim B(n = 10, p = 0,3)$. Giá trị $k$ nào của $X$ có xác suất xuất hiện lớn nhất ($P(X = k)$ đạt cực đại - hay mốt/mode của phân phối)?",
    "options": [
      "k = 3",
      "k = 2",
      "k = 4",
      "k = 5"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì mốt (mode) của phân phối Nhị thức $B(n, p)$ là số nguyên $k$ thỏa mãn bất đẳng thức:\n$(n + 1)p - 1 \\le k \\le (n + 1)p$.\nỞ đây: $(10 + 1) \\cdot 0,3 - 1 = 3,3 - 1 = 2,3 \\le k \\le 3,3$.\nSố nguyên duy nhất nằm trong đoạn $[2,3; 3,3]$ là $k = 3$.\n(Kiểm tra xác suất: $P(X=3) \\approx 0,2668$ là lớn nhất so với $P(X=2) \\approx 0,2335$ và $P(X=4) \\approx 0,2001$).\n\nPhân tích bẫy sai:\n- Phương án B, C, D: Đều có xác suất nhỏ hơn giá trị tại $k=3$.",
    "source": "Slide Week 07 tr. 15"
  },
  {
    "id": "TN4_14",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Cơ bản",
    "question": "Biến ngẫu nhiên $X \\sim Bernoulli(p)$ đạt phương sai lớn nhất khi tham số $p$ bằng bao nhiêu và giá trị phương sai cực đại đó là bao nhiêu?",
    "options": [
      "$p = 1,0$ và $\\operatorname{Var}(X) = 1,00$",
      "$p = 0,5$ và $\\operatorname{Var}(X) = 0,25$",
      "$p = 0,0$ và $\\operatorname{Var}(X) = 0,00$",
      "$p = 0,5$ và $\\operatorname{Var}(X) = 0,50$"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì hàm phương sai của Bernoulli là $f(p) = p(1 - p) = p - p^2$.\nLấy đạo hàm: $f'(p) = 1 - 2p = 0 \\iff p = 0,5$.\nTại $p = 0,5$, phương sai cực đại là: $\\operatorname{Var}_{\\max} = 0,5 \\cdot (1 - 0,5) = 0,25$.\nÝ nghĩa trực giác: Khi $p = 0,5$, kết quả là khó đoán định và bất định nhất (tung đồng xu cân đối), do đó phương sai (độ bất định) đạt đỉnh cao nhất.\n\nPhân tích bẫy sai:\n- Phương án A, C: Tại $p = 1$ hoặc $p = 0$, biến ngẫu nhiên trở thành hằng số chắc chắn, phương sai bằng 0 (cực tiểu chứ không phải cực đại!).\n- Phương án D: Nhầm $p(1-p)$ bằng 0,5 thay vì 0,25.",
    "source": "Slide Week 07 tr. 10; Stat20 Mục 4.8"
  },
  {
    "id": "TN4_15",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Nâng cao",
    "question": "Một lô hàng gồm 100 sản phẩm, trong đó có 10 sản phẩm lỗi. Quy trình nghiệm thu quy định: lấy ngẫu nhiên không hoàn lại 4 sản phẩm để kiểm tra, nếu không có bất kỳ sản phẩm lỗi nào trong 4 sản phẩm đó thì lô hàng được chấp nhận. Xác suất để lô hàng này được chấp nhận xấp xỉ bằng bao nhiêu?",
    "options": [
      "Khoảng 90,00%",
      "Khoảng 65,61%",
      "Khoảng 65,16%",
      "Khoảng 34,84%"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì áp dụng mô hình Siêu bội $HG(N=100, M=10, n=4)$:\n- Số sản phẩm tốt trong lô: $100 - 10 = 90$ sản phẩm.\n- Biến cố lô hàng được chấp nhận là lấy được cả 4 sản phẩm tốt từ 90 sản phẩm tốt:\n$P(X = 0) = \\frac{C_{90}^4 \\cdot C_{10}^0}{C_{100}^4} = \\frac{\\frac{90 \\cdot 89 \\cdot 88 \\cdot 87}{24}}{\\frac{100 \\cdot 99 \\cdot 98 \\cdot 97}{24}} = \\frac{2.555.190}{3.921.225} \\approx 0,6516$ (tức 65,16%).\n(Nếu tính theo xác suất có điều kiện: $\\frac{90}{100} \\times \\frac{89}{99} \\times \\frac{88}{98} \\times \\frac{87}{97} \\approx 0,6516$).\n\nPhân tích bẫy sai:\n- Phương án A: 90% là tỷ lệ sản phẩm tốt ban đầu ($90/100$).\n- Phương án B: $0,9^4 = 0,6561$ là kết quả nếu coi là rút CÓ HOÀN LẠI (Nhị thức).\n- Phương án D: $1 - 0,6516 = 0,3484$ là xác suất lô hàng BỊ TỪ CHỐI.",
    "source": "Slide Week 07 tr. 15; Stat20 Mục 4.9"
  },
  {
    "id": "TN4_16",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Trung bình",
    "question": "Một người chơi bóng rổ ném bóng vào rổ với xác suất thành công ở mỗi lần ném độc lập là $p = 0,2$. Người này ném liên tục cho đến khi bóng vào rổ lần đầu tiên thì dừng lại. Gọi $X$ là số lần ném cho đến khi thành công lần đầu. Xác suất người này phải ném đúng 3 lần ($P(X = 3)$) bằng bao nhiêu?",
    "options": [
      "0,008",
      "0,048",
      "0,512",
      "0,128"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì để ném thành công lần đầu ở lần thứ 3, hai lần đầu tiên phải ném trượt và lần thứ 3 ném trúng:\n- Xác suất trượt mỗi lần: $1 - 0,2 = 0,8$.\n- Xác suất theo phân phối Hình học: $P(X = 3) = (1 - p)^{3-1} \\cdot p = (0,8)^2 \\cdot 0,2 = 0,64 \\cdot 0,2 = 0,128$ (tức 12,8%).\n\nPhân tích bẫy sai:\n- Phương án A: $0,2^3 = 0,008$ là xác suất cả 3 lần đều trúng.\n- Phương án B: Sai do nhân $3 \\cdot 0,8 \\cdot 0,2 = 0,48$.\n- Phương án C: $0,8^3 = 0,512$ là xác suất cả 3 lần đều trượt.",
    "source": "Stat20 Mục 4.8"
  },
  {
    "id": "TN4_17",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Cơ bản",
    "question": "Cho hai biến ngẫu nhiên độc lập $X_1 \\sim Po(\\lambda_1 = 2)$ và $X_2 \\sim Po(\\lambda_2 = 3)$. Tổng $Y = X_1 + X_2$ tuân theo phân phối nào?",
    "options": [
      "Phân phối Poisson với tham số \\(\\lambda = 5\\)",
      "Phân phối Poisson với tham số \\(\\lambda = 6\\)",
      "Phân phối Nhị thức với $n = 5$",
      "Phân phối Chuẩn với trung bình 5 và phương sai 25"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo tính chất tự nhiên (tính ổn định / reproductive property) của phân phối Poisson: Tổng của hai biến ngẫu nhiên Poisson độc lập là một biến ngẫu nhiên Poisson có tham số bằng tổng các tham số:\n$X_1 + X_2 \\sim Po(\\lambda_1 + \\lambda_2) = Po(2 + 3) = Po(5)$.\n\nPhân tích bẫy sai:\n- Phương án B: Sai do nhân các tham số $2 \\cdot 3 = 6$.\n- Phương án C, D: Sai phân phối.",
    "source": "Slide Week 07 tr. 16"
  },
  {
    "id": "TN4_18",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Cơ bản",
    "question": "Tung một đồng xu cân đối đồng chất 4 lần. Xác suất để xuất hiện MẶT NGỬA ÍT NHẤT MỘT LẦN bằng bao nhiêu?",
    "options": [
      "1/16 (6,25%)",
      "15/16 (93,75%)",
      "1/2 (50%)",
      "3/4 (75%)"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì biến cố đối của 'ít nhất một mặt ngửa' là 'không có mặt ngửa nào' (cả 4 lần đều sấp):\n$P(X = 0) = (0,5)^4 = \\frac{1}{16} = 0,0625$.\nDo đó: $P(X \\ge 1) = 1 - P(X = 0) = 1 - \\frac{1}{16} = \\frac{15}{16} = 0,9375$ (93,75%).\n\nPhân tích bẫy sai:\n- Phương án A: 1/16 là xác suất của biến cố đối (không có lần nào ngửa).\n- Phương án C: 1/2 là xác suất của 1 lần tung đơn lẻ.\n- Phương án D: Ước lượng cảm tính.",
    "source": "Slide Week 07 tr. 15; Stat20 Mục 4.8"
  },
  {
    "id": "TN4_19",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Trung bình",
    "question": "Trong thực tế điều tra xã hội học và chọn mẫu, phân phối Siêu bội $HG(N, M, n)$ (rút không hoàn lại) có thể được xấp xỉ an toàn bằng phân phối Nhị thức $B(n, p = M/N)$ khi thỏa mãn điều kiện kinh nghiệm nào?",
    "options": [
      "Khi kích thước mẫu $n$ bằng đúng kích thước tổng thể $N$",
      "Khi số lượng đặc trưng $M$ phải lớn hơn một nửa tổng thể ($M > N/2$)",
      "Kích thước mẫu $n$ chiếm tỷ lệ rất nhỏ so với tổng thể $N$ (thường là \\(n/N \\le 0,05\\) hoặc \\(n/N \\le 0,10\\))",
      "Khi kích thước mẫu $n > 100$ bất kể tổng thể $N$ là bao nhiêu"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì khi tỷ lệ lấy mẫu $n/N \\le 0,05$ (mẫu chiếm dưới 5% tổng thể), hệ số hiệu chỉnh tổng thể hữu hạn $\\frac{N-n}{N-1} \\approx 1$. Việc rút một vài cá thể từ một tổng thể khổng lồ làm thay đổi xác suất của các cá thể còn lại không đáng kể, do đó bài toán rút không hoàn lại xấp xỉ như rút có hoàn lại (Nhị thức).\n\nPhân tích bẫy sai:\n- Phương án A: Khi $n = N$, ta lấy hết toàn bộ tổng thể, không còn tính ngẫu nhiên.\n- Phương án B, D: Đều sai quy tắc xấp xỉ thống kê chuẩn.",
    "source": "Slide Week 07 tr. 15; Stat20 Mục 4.9"
  },
  {
    "id": "TN4_20",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Trung bình",
    "question": "Một tổng đài nhận trung bình 1 cuộc gọi báo hỏng mỗi giờ ($X \\sim Po(\\lambda = 1)$). Xác suất để trong một giờ tổng đài nhận ĐƯỢC TỐI ĐA 1 CUỘC GỌI ($P(X \\le 1)$) bằng bao nhiêu?",
    "options": [
      "\\(e^{-1} \\approx 0,3679\\)",
      "\\(1 - 2e^{-1} \\approx 0,2642\\)",
      "0,5000",
      "\\(2e^{-1} \\approx 0,7358\\)"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì 'tối đa 1 cuộc gọi' nghĩa là có 0 cuộc gọi hoặc đúng 1 cuộc gọi:\n$P(X \\le 1) = P(X = 0) + P(X = 1) = \\frac{1^0 e^{-1}}{0!} + \\frac{1^1 e^{-1}}{1!} = e^{-1} + e^{-1} = 2e^{-1} \\approx 2 \\cdot 0,367879 \\approx 0,7358$ (73,58%).\n\nPhân tích bẫy sai:\n- Phương án A: $e^{-1} \\approx 0,3679$ chỉ tính riêng trường hợp đúng 0 hoặc đúng 1 cuộc gọi.\n- Phương án B: $1 - 2e^{-1} \\approx 0,2642$ là xác suất có TỪ 2 CUỘC GỌI TRỞ LÊN ($P(X \\ge 2)$).\n- Phương án C: Đoán mò.",
    "source": "Slide Week 07 tr. 16; Stat20 Mục 4.10"
  },
  {
    "id": "TN4_21",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Nâng cao",
    "question": "Một nhóm có 10 thành viên, gồm 4 nữ và 6 nam. Chọn ngẫu nhiên không hoàn lại 3 thành viên để lập ban cán sự. Gọi $X$ là số thành viên nữ được chọn ($X \\sim HG(N=10, M=4, n=3)$). Phương sai $\\operatorname{Var}(X)$ bằng bao nhiêu?",
    "options": [
      "0,56",
      "0,72",
      "1,20",
      "0,748"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì áp dụng công thức phương sai của phân phối Siêu bội:\n$\\operatorname{Var}(X) = n \\cdot \\frac{M}{N} \\cdot \\left(1 - \\frac{M}{N}\\right) \\cdot \\frac{N - n}{N - 1}$.\nỞ đây: $n = 3, N = 10, M = 4 \\implies p = 4/10 = 0,4$.\n- Phương sai nếu là Nhị thức: $n p (1 - p) = 3 \\cdot 0,4 \\cdot 0,6 = 0,72$.\n- Hệ số hiệu chỉnh FPC: $\\frac{N - n}{N - 1} = \\frac{10 - 3}{10 - 1} = \\frac{7}{9}$.\n- Phương sai Siêu bội: $\\operatorname{Var}(X) = 0,72 \\cdot \\frac{7}{9} = 0,56$.\n\nPhân tích bẫy sai:\n- Phương án B: 0,72 là phương sai khi coi là rút CÓ HOÀN LẠI (quên nhân hệ số hiệu chỉnh FPC 7/9).\n- Phương án C: 1,20 là kỳ vọng $E(X) = 3 \\cdot 0,4 = 1,20$.\n- Phương án D: $\\sqrt{0,56} \\approx 0,7483$ là độ lệch chuẩn $\\sigma(X)$, không phải phương sai.",
    "source": "Slide Week 07 tr. 15; Stat20 Mục 4.9"
  },
  {
    "id": "TN4_22",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Trung bình",
    "question": "Một cuốn sách có 500 trang. Xác suất một trang bất kỳ có lỗi in là $p = 0,004$, các trang độc lập nhau. Dùng xấp xỉ Poisson, xác suất để trong toàn bộ cuốn sách có ÍT NHẤT MỘT TRANG BỊ LỖI IN là bao nhiêu?",
    "options": [
      "Khoảng 13,53%",
      "Khoảng 86,47%",
      "Khoảng 27,07%",
      "Khoảng 99,99%"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì:\n- Tham số Poisson: $\\lambda = n \\cdot p = 500 \\cdot 0,004 = 2$.\n- Biến cố đối của 'ít nhất một trang bị lỗi' là 'không có trang nào bị lỗi' ($X = 0$):\n$P(X = 0) = e^{-\\lambda} = e^{-2} \\approx 0,135335$.\n- Xác suất có ít nhất một trang bị lỗi:\n$P(X \\ge 1) = 1 - P(X = 0) = 1 - e^{-2} \\approx 1 - 0,135335 = 0,864665 \\approx 86,47\\%$.\n\nPhân tích bẫy sai:\n- Phương án A: 13,53% là xác suất KHÔNG CÓ trang nào lỗi ($P(X=0)$).\n- Phương án C: 27,07% là xác suất có đúng 1 trang lỗi ($2 e^{-2}$).\n- Phương án D: Ước lượng cảm tính sai.",
    "source": "Slide Week 07 tr. 16; Stat20 Mục 4.10"
  },
  {
    "id": "TN4_23",
    "topicId": 4,
    "topicName": "Các mô hình rời rạc kinh điển",
    "level": "Cơ bản",
    "question": "Bảng tóm tắt nào sau đây về các mô hình xác suất rời rạc là HOÀN TOÀN CHÍNH XÁC?",
    "options": [
      "Nhị thức: Rút không hoàn lại; Siêu bội: Rút có hoàn lại; Poisson: Biến liên tục",
      "Nhị thức: Có kỳ vọng bằng phương sai; Poisson: Có phương sai luôn nhỏ hơn kỳ vọng",
      "Nhị thức: Rút có hoàn lại, các lần rút độc lập; Siêu bội: Rút không hoàn lại từ tổng thể hữu hạn, các lần rút phụ thuộc; Poisson: Đếm biến cố hiếm trong khoảng liên tục",
      "Siêu bội: Các lần thử độc lập nhau; Nhị thức: Các lần thử phụ thuộc nhau"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì đây là phân biệt cốt lõi nhất giữa 3 mô hình rời rạc kinh điển (Slide Week 07 và Stat20 Ch.4):\n- Nhị thức: số phép thử $n$ cố định, xác suất $p$ không đổi (rút có hoàn lại), các phép thử độc lập.\n- Siêu bội: kích thước tổng thể $N$ và mẫu $n$ cố định, rút không hoàn lại nên xác suất thay đổi (phụ thuộc).\n- Poisson: đếm số lần xuất hiện của biến cố trong khoảng liên tục, kỳ vọng và phương sai luôn bằng nhau ($\\lambda$).\n\nPhân tích bẫy sai:\n- Phương án A, B, D: Đều đảo ngược hoặc sai lệch các đặc tính căn bản.",
    "source": "Slide Week 07 tr. 15-16; Stat20 Mục 4.8 - 4.10"
  },
  {
    "id": "TN5_01",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Một chiếc hộp chứa các tấm vé có độ lệch chuẩn $\\sigma = 3$. Rút ngẫu nhiên có hoàn lại $n = 100$ lần. Độ lệch chuẩn của TỔNG các số rút được ($S_n$) bằng bao nhiêu?",
    "options": [
      "300",
      "3",
      "0,3",
      "30"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì theo Quy luật căn bậc hai (Square Root Law) của mô hình chiếc hộp:\n$\\sigma(S_n) = \\sigma \\cdot \\sqrt{n} = 3 \\cdot \\sqrt{100} = 3 \\cdot 10 = 30$.\n\nPhân tích bẫy sai:\n- Phương án A: Sai do nhân $n \\cdot \\sigma = 100 \\cdot 3 = 300$ (ngộ nhận rằng độ lệch chuẩn của tổng tăng tỷ lệ thuận với $n$; thực chất chỉ kỳ vọng mới nhân $n$, còn độ lệch chuẩn chỉ nhân $\\sqrt{n}$ do có sự triệt tiêu ngẫu nhiên giữa các lần rút).\n- Phương án B: Giữ nguyên $\\sigma = 3$.\n- Phương án C: 0,3 là độ lệch chuẩn của TRUNG BÌNH MẪU $\\sigma(\\bar{X}_n) = \\sigma / \\sqrt{n} = 3 / 10 = 0,3$.",
    "source": "Slide Week 07 tr. 23; Stat20 Mục 4.12"
  },
  {
    "id": "TN5_02",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Thu nhập của cư dân một khu đô thị có độ lệch chuẩn $\\sigma = 20$ triệu đồng. Khảo sát một mẫu ngẫu nhiên độc lập gồm $n = 400$ người. Sai số chuẩn (độ lệch chuẩn của thu nhập trung bình mẫu $\\bar{X}_n$) bằng bao nhiêu?",
    "options": [
      "1,0 triệu đồng",
      "0,05 triệu đồng",
      "400 triệu đồng",
      "20 triệu đồng"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì sai số chuẩn của trung bình mẫu từ $n$ biến i.i.d. là:\n$\\sigma(\\bar{X}_n) = \\frac{\\sigma}{\\sqrt{n}} = \\frac{20}{\\sqrt{400}} = \\frac{20}{20} = 1,0$ triệu đồng.\n\nPhân tích bẫy sai:\n- Phương án B: Sai do chia cho $n=400$ thay vì $\\sqrt{n}$ ($20/400 = 0,05$).\n- Phương án C: Nhầm sang độ lệch chuẩn của TỔNG thu nhập: $\\sigma(S_n) = 20 \\cdot 20 = 400$.\n- Phương án D: Giữ nguyên $\\sigma = 20$ là sai vì trung bình của 400 người phải có độ biến động nhỏ hơn nhiều so với từng cá nhân.",
    "source": "Slide Week 07 tr. 25; Stat20 Mục 4.13"
  },
  {
    "id": "TN5_03",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Khi tăng kích thước mẫu $n$ lên gấp 4 lần ($n' = 4n$), độ lệch chuẩn của Tổng rút được $\\sigma(S_n)$ và độ lệch chuẩn của Trung bình mẫu $\\sigma(\\bar{X}_n)$ thay đổi như thế nào?",
    "options": [
      "\\(\\sigma(S_n)\\) tăng gấp 4 lần, còn \\(\\sigma(\\bar{X}_n)\\) giảm đi 4 lần",
      "\\(\\sigma(S_n)\\) tăng gấp 2 lần, còn \\(\\sigma(\\bar{X}_n)\\) giảm đi 2 lần",
      "Cả hai đại lượng đều tăng gấp 2 lần",
      "Cả hai đại lượng đều không đổi vì độ lệch chuẩn của tổng thể không đổi"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì:\n- Đối với tổng: $\\sigma(S_{4n}) = \\sigma \\sqrt{4n} = 2 \\cdot \\sigma \\sqrt{n} = 2 \\cdot \\sigma(S_n)$ (tăng gấp $\\sqrt{4} = 2$ lần).\n- Đối với trung bình: $\\sigma(\\bar{X}_{4n}) = \\frac{\\sigma}{\\sqrt{4n}} = \\frac{1}{2} \\cdot \\frac{\\sigma}{\\sqrt{n}} = \\frac{1}{2} \\sigma(\\bar{X}_n)$ (giảm đi $\\sqrt{4} = 2$ lần).\n\nPhân tích bẫy sai:\n- Phương án A: Sai do quên căn bậc hai (nhầm theo hệ số 4 thay vì 2).\n- Phương án C: Nhầm chiều biến thiên của trung bình mẫu.\n- Phương án D: Độ lệch chuẩn của mẫu thay đổi theo kích thước mẫu $n$ dù $\\sigma$ tổng thể không đổi.",
    "source": "Slide Week 07 tr. 26; Stat20 Mục 4.13"
  },
  {
    "id": "TN5_04",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Một chiếc hộp chứa 3 tấm vé ghi số [1] và 7 tấm vé ghi số [0]. Trung bình của hộp ($\\mu$) và độ lệch chuẩn của hộp ($\\sigma$) lần lượt là:",
    "options": [
      "\\(\\mu = 0,3\\) và \\(\\sigma = 0,21\\)",
      "\\(\\mu = 0,5\\) và \\(\\sigma = 0,5\\)",
      "\\(\\mu = 0,3\\) và \\(\\sigma = \\sqrt{0,21} \\approx 0,4583\\)",
      "\\(\\mu = 3\\) và \\(\\sigma = 7\\)"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì đối với hộp nhị phân chỉ gồm các vé [0] và [1]:\n- Tỷ lệ vé [1] là $p = \\frac{3}{3 + 7} = 0,3$.\n- Trung bình của hộp: $\\mu = p = 0,3$.\n- Phương sai của hộp: $\\sigma^2 = p(1 - p) = 0,3 \\cdot 0,7 = 0,21$.\n- Độ lệch chuẩn của hộp: $\\sigma = \\sqrt{0,21} \\approx 0,4583$.\n\nPhân tích bẫy sai:\n- Phương án A: 0,21 là phương sai $\\sigma^2$, chưa khai căn bậc hai để ra độ lệch chuẩn.\n- Phương án B: 0,5 là trường hợp số vé 0 và 1 bằng nhau.\n- Phương án D: Nhầm số lượng vé với giá trị trung bình.",
    "source": "Slide Week 07 tr. 22; Stat20 Mục 4.11"
  },
  {
    "id": "TN5_05",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Cho biến ngẫu nhiên $X$ bất kỳ có kỳ vọng $\\mu$ và phương sai $\\sigma^2$. Theo bất đẳng thức Chebyshev, xác suất để $X$ nhận giá trị nằm trong khoảng $(\\mu - 2\\sigma; \\mu + 2\\sigma)$ luôn đạt ÍT NHẤT là bao nhiêu?",
    "options": [
      "95% (tức 0,95)",
      "50% (tức 0,50)",
      "88,89% (tức 8/9)",
      "75% (tức 0,75)"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì theo bất đẳng thức Chebyshev dạng phần bù với $k = 2$:\n$P(|X - \\mu| < 2\\sigma) \\ge 1 - \\frac{1}{k^2} = 1 - \\frac{1}{2^2} = 1 - 0,25 = 0,75$ (75%).\nBất đẳng thức này đúng cho MỌI phân phối xác suất.\n\nPhân tích bẫy sai:\n- Phương án A: 95% là quy tắc kinh nghiệm của phân phối CHUẨN ($N(\\mu, \\sigma^2)$), không phải bất đẳng thức Chebyshev tổng quát.\n- Phương án B: Sai phép tính.\n- Phương án C: $8/9 \\approx 88,89\\%$ là kết quả khi $k = 3$ ($1 - 1/9 = 8/9$).",
    "source": "Slide Week 07 tr. 34-35"
  },
  {
    "id": "TN5_06",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Với biến ngẫu nhiên $X$ có kỳ vọng $\\mu = 50$ và độ lệch chuẩn $\\sigma = 4$, cận trên Chebyshev cho xác suất $P(|X - 50| \\ge 12)$ là:",
    "options": [
      "1/9 (khoảng 11,11%)",
      "1/3",
      "1/16",
      "8/9"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì khoảng cách lệch là $12 = 3 \\cdot 4 = 3\\sigma \\implies k = 3$.\nTheo bất đẳng thức Chebyshev:\n$P(|X - 50| \\ge 12) = P(|X - \\mu| \\ge 3\\sigma) \\le \\frac{1}{k^2} = \\frac{1}{3^2} = \\frac{1}{9} \\approx 0,1111$ (11,11%).\n\nPhân tích bẫy sai:\n- Phương án B: Sai do quên bình phương: $1/k = 1/3$.\n- Phương án C: Sai do lấy $1/12$ hoặc $1/4^2 = 1/16$.\n- Phương án D: 8/9 là cận dưới của biến cố ngược lại $P(|X - 50| < 12) \\ge 8/9$.",
    "source": "Slide Week 07 tr. 34-35"
  },
  {
    "id": "TN5_07",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Ưu điểm vượt trội lớn nhất của Bất đẳng thức Chebyshev so với các phương pháp tính xác suất khác là gì?",
    "options": [
      "Nó luôn cho kết quả xác suất chính xác 100% không có sai số",
      "Nó áp dụng được cho MỌI biến ngẫu nhiên (bất kể phân phối rời rạc, liên tục, lệch mạnh hay nhiều đỉnh), chỉ cần biết kỳ vọng $\\mu$ và phương sai $\\sigma^2$ hữu hạn",
      "Nó chỉ áp dụng được riêng cho phân phối Chuẩn",
      "Nó không cần biết phương sai của biến ngẫu nhiên"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì Chebyshev là bất đẳng thức phi tham số (non-parametric), áp dụng phổ quát cho bất kỳ phân phối nào mà không cần giả định về hình dạng của phân phối đó, chỉ cần tồn tại $\\mu$ và $\\sigma^2$.\n\nPhân tích bẫy sai:\n- Phương án A: Chebyshev chỉ cung cấp CẬN TRÊN hoặc CẬN DƯỚI (bounds), không phải xác suất chính xác, và cận này thường khá lỏng.\n- Phương án C: Phân phối chuẩn dùng bảng tra Z-score, không cần đến Chebyshev.\n- Phương án D: Chebyshev bắt buộc phải biết phương sai $\\sigma^2$ hữu hạn.",
    "source": "Slide Week 07 tr. 33"
  },
  {
    "id": "TN5_08",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Trung bình",
    "question": "Cho $X_1, \\dots, X_{100}$ là mẫu ngẫu nhiên gồm 100 biến i.i.d. có kỳ vọng $\\mu = 10$ và độ lệch chuẩn $\\sigma = 2$. Đánh giá xác suất để trung bình mẫu $\\bar{X}_{100}$ sai lệch so với $\\mu$ từ 0,6 trở lên ($P(|\\bar{X}_{100} - 10| \\ge 0,6)$) theo Chebyshev:",
    "options": [
      "\\(P(|\\bar{X}_{100} - 10| \\ge 0,6) \\le 1/3\\)",
      "\\(P(|\\bar{X}_{100} - 10| \\ge 0,6) \\le 4/0,36 \\approx 11,11\\)",
      "\\(P(|\\bar{X}_{100} - 10| \\ge 0,6) \\le 1/9 \\approx 0,1111\\)",
      "\\(P(|\\bar{X}_{100} - 10| \\ge 0,6) \\ge 8/9\\)"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì đối với trung bình mẫu $\\bar{X}_{100}$:\n- Độ lệch chuẩn của trung bình mẫu: $\\sigma(\\bar{X}_{100}) = \\frac{\\sigma}{\\sqrt{n}} = \\frac{2}{\\sqrt{100}} = \\frac{2}{10} = 0,2$.\n- Khoảng sai số $\\varepsilon = 0,6 = 3 \\cdot 0,2 = 3 \\sigma(\\bar{X}_{100}) \\implies k = 3$.\n- Theo Chebyshev: $P(|\\bar{X}_{100} - 10| \\ge 0,6) \\le \\frac{1}{k^2} = \\frac{1}{3^2} = \\frac{1}{9} \\approx 0,1111$.\n\nPhân tích bẫy sai:\n- Phương án A: Quên bình phương: $1/k = 1/3$.\n- Phương án B: Sai do lấy $\\sigma^2$ của tổng thể chia cho $\\varepsilon^2$ ($4 / 0,36$) mà quên chia cho mẫu số $n=100$ (xác suất > 1 là vô nghĩa).\n- Phương án D: Đảo ngược chiều bất đẳng thức.",
    "source": "Slide Week 07 tr. 36-37"
  },
  {
    "id": "TN5_09",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Phát biểu toán học nào sau đây biểu diễn ĐÚNG nội dung của Luật số lớn yếu (Weak Law of Large Numbers - WLLN) đối với dãy biến i.i.d. có kỳ vọng hữu hạn $\\mu$?",
    "options": [
      "Khi $n \\to \\infty$, tổng $S_n$ tiến dần về kỳ vọng $\\mu$",
      "Khi $n \\to \\infty$, phương sai của tổng $S_n$ tiến dần về 0",
      "Với mọi $n$, trung bình mẫu $\\bar{X}_n$ luôn bằng đúng $\\mu$",
      "Với mọi \\(\\varepsilon > 0\\), \\(\\lim_{n \\to \\infty} P(|\\bar{X}_n - \\mu| < \\varepsilon) = 1\\) (hoặc \\(\\lim_{n \\to \\infty} P(|\\bar{X}_n - \\mu| \\ge \\varepsilon) = 0\\))"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì Luật số lớn yếu khẳng định sự hội tụ theo xác suất: khi kích thước mẫu $n$ tiến ra vô cùng, xác suất để trung bình mẫu $\\bar{X}_n$ sai lệch so với kỳ vọng lý thuyết $\\mu$ một khoảng dù nhỏ tùy ý $\\varepsilon$ sẽ tiến dần về 0 (tức xác suất nằm sát $\\mu$ tiến về 1).\n\nPhân tích bẫy sai:\n- Phương án A: Sai vì TỔNG $S_n$ tiến ra vô cùng theo $n\\mu$, chỉ có TRUNG BÌNH MẪU mới hội tụ về $\\mu$.\n- Phương án B: Sai vì phương sai của tổng là $n\\sigma^2 \\to \\infty$.\n- Phương án C: $\\bar{X}_n$ là biến ngẫu nhiên, nó không cố định bằng $\\mu$ với mọi $n$.",
    "source": "Slide Week 07 tr. 38; Stat20 Mục 4.13"
  },
  {
    "id": "TN5_10",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Trung bình",
    "question": "Trong giáo trình và slide Week 07, Luật số lớn yếu được chứng minh một cách chặt chẽ dựa trên bất đẳng thức nào sau đây?",
    "options": [
      "Áp dụng Bất đẳng thức Chebyshev cho trung bình mẫu: \\(P(|\\bar{X}_n - \\mu| \\ge \\varepsilon) \\le \\frac{\\sigma^2}{n \\varepsilon^2}\\), vế phải tiến về 0 khi $n \\to \\infty$",
      "Áp dụng Bất đẳng thức Cauchy-Schwarz",
      "Áp dụng Bất đẳng thức Jensen",
      "Áp dụng Định lý Pythagoras"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo Week 07 (tr. 38-39):\nBiến trung bình mẫu $\\bar{X}_n$ có kỳ vọng $\\mu$ và phương sai $\\operatorname{Var}(\\bar{X}_n) = \\frac{\\sigma^2}{n}$.\nÁp dụng trực tiếp bất đẳng thức Chebyshev cho $\\bar{X}_n$ với sai số $\\varepsilon$:\n$P(|\\bar{X}_n - \\mu| \\ge \\varepsilon) \\le \\frac{\\operatorname{Var}(\\bar{X}_n)}{\\varepsilon^2} = \\frac{\\sigma^2}{n \\varepsilon^2}$.\nVới $\\varepsilon > 0$ và $\\sigma^2 < \\infty$ cố định, khi cho $n \\to \\infty$ thì $\\frac{\\sigma^2}{n \\varepsilon^2} \\to 0$. Định lý được chứng minh hoàn tất.\n\nPhân tích bẫy sai:\n- Phương án B, C, D: Đều là các bất đẳng thức toán học khác, không dùng để chứng minh trực tiếp WLLN.",
    "source": "Slide Week 07 tr. 38-39"
  },
  {
    "id": "TN5_11",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Nâng cao",
    "question": "Cần khảo sát một mẫu ngẫu nhiên độc lập tối thiểu bao nhiêu quan sát ($n$) từ tổng thể có độ lệch chuẩn $\\sigma = 4$ để theo Bất đẳng thức Chebyshev, ta có thể bảo đảm với độ tin cậy ít nhất 95% rằng trung bình mẫu $\\bar{X}_n$ sai lệch so với kỳ vọng $\\mu$ không quá 0,5 đơn vị ($P(|\\bar{X}_n - \\mu| < 0,5) \\ge 0,95$)?",
    "options": [
      "n = 246",
      "n = 1.280",
      "n = 320",
      "n = 64"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì theo hệ quả của bất đẳng thức Chebyshev cho trung bình mẫu:\n$P(|\\bar{X}_n - \\mu| \\ge \\varepsilon) \\le \\frac{\\sigma^2}{n \\varepsilon^2} \\le \\alpha$.\nỞ đây: $\\sigma = 4$, sai số $\\varepsilon = 0,5$, và mức rủi ro $\\alpha = 1 - 0,95 = 0,05$.\nSuy ra:\n$n \\ge \\frac{\\sigma^2}{\\alpha \\cdot \\varepsilon^2} = \\frac{4^2}{0,05 \\cdot (0,5)^2} = \\frac{16}{0,05 \\cdot 0,25} = \\frac{16}{0,0125} = 1.280$.\n\nPhân tích bẫy sai:\n- Phương án A: $n \\approx 246$ là kích thước mẫu tính theo xấp xỉ PHÂN PHỐI CHUẨN ($z_{0,025} = 1,96 \\implies n = \\frac{1,96^2 \\cdot 16}{0,25} \\approx 245,86$). Chebyshev không đòi hỏi phân phối chuẩn nên cho cận an toàn lớn hơn (1.280).\n- Phương án C, D: Sai số học do quên bình phương $\\varepsilon$ hoặc $\\sigma$.",
    "source": "Slide Week 07 tr. 40"
  },
  {
    "id": "TN5_12",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Trong một trò chơi cá cược, mỗi ván người chơi có kỳ vọng lợi nhuận là $-0,05$ đô-la (nhà cái có kỳ vọng $+0,05$ đô-la). Nếu một người chơi chơi 1.000.000 ván, theo Luật số lớn điều gì gần như chắc chắn sẽ xảy ra?",
    "options": [
      "Người chơi có thể lội ngược dòng thắng đậm vì 1.000.000 ván sẽ có lúc chuỗi may mắn xuất hiện",
      "Người chơi sẽ hòa vốn vì số ván thắng và thua sẽ cân bằng hoàn hảo bằng nhau",
      "Người chơi gần như chắc chắn phá sản và chịu lỗ bình quân khoảng 0,05 đô-la cho mỗi ván chơi",
      "Phương sai của tổng tiền thua sẽ giảm dần về 0"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì theo WLLN, khi số ván $n = 1.000.000$ rất lớn, trung bình số tiền thắng/thua mỗi ván $\\bar{X}_n$ sẽ hội tụ ngặt nghèo về kỳ vọng lý thuyết $\\mu = -0,05$ đô-la. Tổng số tiền người chơi mất sau 1 triệu ván xấp xỉ $1.000.000 \\times (-0,05) = -50.000$ đô-la. Đây là lý do các sòng bạc luôn kiếm được lợi nhuận khổng lồ và không bao giờ bị thua lỗ trong dài hạn.\n\nPhân tích bẫy sai:\n- Phương án A: Bẫy tâm lý ngụy biện con bạc (Gambler's fallacy).\n- Phương án B: Bẫy ngộ nhận luật bù trừ số ván.\n- Phương án D: Phương sai của TỔNG tiền luôn tăng theo $n\\sigma^2$, không giảm về 0.",
    "source": "Stat20 Mục 4.13; Slide Week 07 tr. 38"
  },
  {
    "id": "TN5_13",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Trung bình",
    "question": "Gieo một con xúc xắc cân đối 6 mặt 100 lần độc lập. Biết mỗi lần gieo có số chấm kỳ vọng $\\mu = 3,5$ và phương sai $\\sigma^2 = 35/12 \\approx 2,9167$. Kỳ vọng và độ lệch chuẩn của TỔNG số chấm sau 100 lần gieo lần lượt là:",
    "options": [
      "\\(E(S_{100}) = 350\\) và \\(\\sigma(S_{100}) \\approx 170,78\\)",
      "\\(E(S_{100}) = 3,5\\) và \\(\\sigma(S_{100}) \\approx 0,1708\\)",
      "\\(E(S_{100}) = 350\\) và \\(\\sigma(S_{100}) = 291,67\\)",
      "\\(E(S_{100}) = 350\\) và \\(\\sigma(S_{100}) \\approx 17,08\\)"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì theo công thức tổng của $n$ biến i.i.d.:\n- Kỳ vọng tổng: $E(S_n) = n \\cdot \\mu = 100 \\cdot 3,5 = 350$.\n- Phương sai tổng: $\\operatorname{Var}(S_n) = n \\cdot \\sigma^2 = 100 \\cdot \\frac{35}{12} \\approx 291,67$.\n- Độ lệch chuẩn tổng: $\\sigma(S_n) = \\sqrt{\\operatorname{Var}(S_n)} = \\sqrt{291,67} \\approx 17,08$.\n\nPhân tích bẫy sai:\n- Phương án A: Sai do tính $\\sigma(S_n) = n \\cdot \\sigma = 100 \\cdot 1,7078 = 170,78$ (nhân $n$ thay vì $\\sqrt{n}$).\n- Phương án B: Đây là kỳ vọng và SD của TRUNG BÌNH MẪU $\\bar{X}_{100}$, không phải của TỔNG.\n- Phương án C: 291,67 là phương sai của tổng, chưa lấy căn bậc hai.",
    "source": "Slide Week 07 tr. 23"
  },
  {
    "id": "TN5_14",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Thời gian giao hàng của một quán ăn có trung bình $\\mu = 30$ phút và độ lệch chuẩn $\\sigma = 5$ phút. Chưa biết quy luật phân phối cụ thể của thời gian giao hàng. Theo Bất đẳng thức Chebyshev, xác suất để một đơn hàng được giao trong khoảng từ 20 đến 40 phút tối thiểu bằng bao nhiêu?",
    "options": [
      "75%",
      "95%",
      "88,89%",
      "50%"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì khoảng từ 20 đến 40 phút tương ứng với khoảng sai lệch quanh trung bình:\n$|X - 30| < 10$.\nVì $\\sigma = 5$, khoảng cách sai lệch là $10 = 2 \\sigma \\implies k = 2$.\nTheo Chebyshev: $P(|X - 30| < 2 \\cdot 5) \\ge 1 - \\frac{1}{2^2} = 1 - 0,25 = 0,75$ (75%).\n\nPhân tích bẫy sai:\n- Phương án B: 95% là quy tắc phân phối chuẩn, không áp dụng được khi chưa biết phân phối cụ thể.\n- Phương án C: 88,89% ứng với $k=3$ (từ 15 đến 45 phút).\n- Phương án D: Sai số học.",
    "source": "Slide Week 07 tr. 35"
  },
  {
    "id": "TN5_15",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Trung bình",
    "question": "Khi áp dụng Bất đẳng thức Chebyshev $P(|X - \\mu| \\ge k\\sigma) \\le \\frac{1}{k^2}$, điều kiện bắt buộc đối với hằng số $k$ để bất đẳng thức mang lại thông tin có ý nghĩa thực tế là gì?",
    "options": [
      "\\(k > 0\\)",
      "\\(k > 1\\)",
      "\\(k\\) phải là số nguyên dương",
      "\\(k \\ge 3\\)"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì nếu $k \\le 1$ thì vế phải $\\frac{1}{k^2} \\ge 1$. Ta luôn biết xác suất của mọi biến cố luôn nhỏ hơn hoặc bằng 1, do đó kết luận $P(\\dots) \\le 1$ hoặc $P(\\dots) \\ge 0$ là một mệnh đề hiển nhiên (trivial), không đem lại bất kỳ thông tin hữu ích nào. Để chặn được cận trên $< 1$, bắt buộc $k > 1$.\n\nPhân tích bẫy sai:\n- Phương án A: Với $0 < k \\le 1$, bất đẳng thức vẫn đúng về mặt toán học nhưng vô nghĩa vì cận trên $\\ge 1$.\n- Phương án C: $k$ có thể là số thực bất kỳ lớn hơn 1 (ví dụ $k = 1,5$ hoặc $k = \\sqrt{5}$), không bắt buộc phải nguyên.\n- Phương án D: $k=2$ đã cho cận 75% rất hữu ích.",
    "source": "Slide Week 07 tr. 34"
  },
  {
    "id": "TN5_16",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Trung bình",
    "question": "Cho biến ngẫu nhiên $X$ có $\\mu = 100$ và $\\sigma = 10$. Khoảng đối xứng quanh trung bình $(\\mu - c; \\mu + c)$ nào sau đây được Chebyshev bảo đảm chắc chắn chứa ÍT NHẤT 80% giá trị của $X$?",
    "options": [
      "\\([80; 120]\\)",
      "\\([70; 130]\\)",
      "\\((100 - 10\\sqrt{5}; 100 + 10\\sqrt{5})\\) (khoảng [77,64; 122,36])",
      "\\([90; 110]\\)"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì ta cần xác suất chứa ít nhất $80\\% = 0,80$:\n$1 - \\frac{1}{k^2} = 0,80 \\iff \\frac{1}{k^2} = 0,20 = \\frac{1}{5} \\iff k^2 = 5 \\iff k = \\sqrt{5} \\approx 2,236$.\nĐộ rộng bán kính sai lệch: $c = k \\cdot \\sigma = \\sqrt{5} \\cdot 10 \\approx 22,36$.\nDo đó khoảng cần tìm là $(100 - 22,36; 100 + 22,36) = (77,64; 122,36)$.\n\nPhân tích bẫy sai:\n- Phương án A: $[80; 120]$ ứng với $k=2$, chỉ đảm bảo ít nhất $1 - 1/4 = 75\\% < 80\\%$.\n- Phương án B: $[70; 130]$ ứng với $k=3$, đảm bảo ít nhất $88,89\\%$ (rộng hơn mức tối thiểu cần thiết).\n- Phương án D: $[90; 110]$ ứng với $k=1$, Chebyshev cho cận $1 - 1 = 0\\%$.",
    "source": "Slide Week 07 tr. 35"
  },
  {
    "id": "TN5_17",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Trong mô hình chiếc hộp rút có hoàn lại $n$ lần, phát biểu nào sau đây là ĐÚNG khi nói về xu hướng biến thiên khi số lần rút $n$ tăng dần?",
    "options": [
      "Độ lệch chuẩn của cả Tổng và Trung bình đều tăng dần theo $n$",
      "Độ lệch chuẩn của cả Tổng và Trung bình đều giảm dần về 0",
      "Độ lệch chuẩn của Tổng không đổi, chỉ có độ lệch chuẩn của Trung bình giảm",
      "Độ lệch chuẩn của Tổng $S_n$ tăng dần theo $\\sqrt{n}$, trong khi độ lệch chuẩn của Trung bình $\\bar{X}_n$ giảm dần theo $1/\\sqrt{n}$"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì:\n- $\\sigma(S_n) = \\sigma \\sqrt{n} \\to \\infty$ khi $n \\to \\infty$ (tổng của càng nhiều số ngẫu nhiên thì khoảng giá trị tuyệt đối càng phân tán rộng ra).\n- $\\sigma(\\bar{X}_n) = \\frac{\\sigma}{\\sqrt{n}} \\to 0$ khi $n \\to \\infty$ (chia cho $n$ khiến các sai số ngẫu nhiên triệt tiêu lẫn nhau, giá trị trung bình gom tụ cực kỳ sát về tâm $\\mu$).\n\nPhân tích bẫy sai:\n- Phương án A, B, C: Đều mô tả sai quy luật căn bậc hai.",
    "source": "Slide Week 07 tr. 26; Stat20 Mục 4.13"
  },
  {
    "id": "TN5_18",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Trung bình",
    "question": "Một chiếc hộp chứa đúng 3 tấm vé mang số: [1, 2, 9]. Trung bình của hộp $\\mu$ và phương sai của hộp $\\sigma^2$ lần lượt là:",
    "options": [
      "\\(\\mu = 4\\) và \\(\\sigma^2 = 38/3 \\approx 12,67\\)",
      "\\(\\mu = 4\\) và \\(\\sigma^2 = 19\\)",
      "\\(\\mu = 4\\) và \\(\\sigma = 38/3\\)",
      "\\(\\mu = 3\\) và \\(\\sigma^2 = 12\\)"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì đối với chiếc hộp gồm $N=3$ vé mang số hữu hạn (xem như tổng thể):\n- Trung bình của hộp: $\\mu = \\frac{1 + 2 + 9}{3} = \\frac{12}{3} = 4$.\n- Phương sai của hộp (chia cho $N=3$): $\\sigma^2 = \\frac{(1-4)^2 + (2-4)^2 + (9-4)^2}{3} = \\frac{(-3)^2 + (-2)^2 + 5^2}{3} = \\frac{9 + 4 + 25}{3} = \\frac{38}{3} \\approx 12,67$.\n\nPhân tích bẫy sai:\n- Phương án B: Sai do chia cho $N-1 = 2$ ($38/2 = 19$, đây là phương sai mẫu, trong khi hộp đóng vai trò là tổng thể nên chia cho $N$).\n- Phương án C: Nhầm phương sai với độ lệch chuẩn.\n- Phương án D: Sai số học.",
    "source": "Slide Week 07 tr. 22; Stat20 Mục 4.11"
  },
  {
    "id": "TN5_19",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Nâng cao",
    "question": "Biến ngẫu nhiên không âm $X \\ge 0$ có kỳ vọng $\\mu = 20$ và độ lệch chuẩn $\\sigma = 5$. Đánh giá cận trên của xác suất $P(X \\ge 40)$ bằng Bất đẳng thức Chebyshev:",
    "options": [
      "\\(P(X \\ge 40) \\le 1/4 = 0,25\\)",
      "\\(P(X \\ge 40) \\le 1/16 = 0,0625\\)",
      "\\(P(X \\ge 40) \\le 0,50\\)",
      "\\(P(X \\ge 40) = 0\\)"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì:\n- Ta có biến cố $\\{X \\ge 40\\}$ tương đương $\\{X - 20 \\ge 20\\}$.\n- Biến cố này là tập con của biến cố hai phía: $\\{|X - 20| \\ge 20\\}$ (gồm $X \\ge 40$ hoặc $X \\le 0$).\n- Áp dụng Chebyshev với $\\varepsilon = 20 = 4\\sigma \\implies k = 4$:\n$P(X \\ge 40) \\le P(|X - 20| \\ge 20) \\le \\frac{\\sigma^2}{\\varepsilon^2} = \\frac{5^2}{20^2} = \\frac{25}{400} = \\frac{1}{16} = 0,0625$ (6,25%).\n\nPhân tích bẫy sai:\n- Phương án A: Sai do lấy $k = 40/20 = 2 \\implies 1/2^2 = 0,25$ (nhầm độ lệch là 10 thay vì 20).\n- Phương án C: Dùng bất đẳng thức Markov ($E(X)/a = 20/40 = 0,5$), nhưng Chebyshev cho cận chặt hơn nhiều (0,0625).\n- Phương án D: Sai hoàn toàn.",
    "source": "Slide Week 07 tr. 34"
  },
  {
    "id": "TN5_20",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Trung bình",
    "question": "Trong khoảng $(\\mu - 3\\sigma; \\mu + 3\\sigma)$, Bất đẳng thức Chebyshev bảo đảm chứa ít nhất bao nhiêu phần trăm dữ liệu, và nếu phân phối là Phân phối Chuẩn thì thực tế chứa bao nhiêu phần trăm dữ liệu?",
    "options": [
      "Chebyshev bảo đảm ít nhất 95%, còn Phân phối Chuẩn thực tế chứa 99%",
      "Cả hai đều cho kết quả giống hệt nhau là 99,73%",
      "Chebyshev bảo đảm ít nhất 88,89%, còn Phân phối Chuẩn thực tế chứa 99,73%",
      "Chebyshev bảo đảm 99,73%, còn Phân phối Chuẩn là 88,89%"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì:\n- Theo Chebyshev với $k=3$: $P(|X - \\mu| < 3\\sigma) \\ge 1 - \\frac{1}{3^2} = 1 - \\frac{1}{9} = \\frac{8}{9} \\approx 88,89\\%$.\n- Đối với Phân phối Chuẩn $N(\\mu, \\sigma^2)$, do có dạng hình chuông đặc thù với đuôi tiêu biến nhanh theo hàm mũ $e^{-z^2/2}$, diện tích trong khoảng $\\pm 3\\sigma$ đạt tới $99,73\\%$.\nĐiều này minh họa rõ nét tính chất 'an toàn nhưng lỏng' của Chebyshev đối với mọi phân phối so với trường hợp phân phối Chuẩn cụ thể.\n\nPhân tích bẫy sai:\n- Phương án A, B, D: Đều nhầm lẫn số liệu giữa hai định lý.",
    "source": "Slide Week 07 tr. 35 & tr. 54"
  },
  {
    "id": "TN5_21",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Hai đặc tính then chốt khẳng định trung bình mẫu $\\bar{X}_n$ là một ước lượng xuất sắc cho kỳ vọng tổng thể $\\mu$ là:",
    "options": [
      "Tính đối xứng và tính có phương sai cố định không đổi theo $n$",
      "Tính độc lập và tính luôn nhận giá trị nguyên",
      "Tính có phân phối đều và kỳ vọng luôn bằng 0",
      "Tính không chệch ($E(\\bar{X}_n) = \\mu$) và Tính nhất quán ($\\operatorname{Var}(\\bar{X}_n) = \\frac{\\sigma^2}{n} \\to 0$ khi $n \\to \\infty$ theo WLLN)"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì:\n- Tính không chệch (Unbiasedness): Kỳ vọng của trung bình mẫu luôn bằng đúng tham số thực $\\mu$ với mọi $n$.\n- Tính nhất quán (Consistency): Khi kích thước mẫu $n$ tăng vô hạn, phương sai giảm về 0, đảm bảo theo WLLN rằng trung bình mẫu hội tụ theo xác suất về giá trị thực $\\mu$.\n\nPhân tích bẫy sai:\n- Phương án A, B, C: Đều sai các định nghĩa lý thuyết thống kê cơ bản.",
    "source": "Slide Week 07 tr. 25, 38; Stat20 Mục 4.13"
  },
  {
    "id": "TN5_22",
    "topicId": 5,
    "topicName": "Mô hình chiếc hộp, Tổng & Trung bình, Chebyshev & WLLN",
    "level": "Cơ bản",
    "question": "Nếu chiếc hộp chỉ chứa các tấm vé [0] và [1] với tỷ lệ vé [1] là $p$, thì Tổng các số rút được sau $n$ lần rút có hoàn lại ($S_n = \\sum_{i=1}^n X_i$) chính là:",
    "options": [
      "Biến ngẫu nhiên có Phân phối Nhị thức $B(n, p)$, đếm số lần rút được vé [1]",
      "Biến ngẫu nhiên có Phân phối Siêu bội $HG(N, M, n)$",
      "Biến ngẫu nhiên có Phân phối Poisson $Po(np)$",
      "Biến ngẫu nhiên Bernoulli(p)"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì mỗi lần rút có hoàn lại là một phép thử Bernoulli($p$) độc lập với $X_i \\in \\{0, 1\\}$. Khi đó tổng $S_n = X_1 + \\dots + X_n$ chính là số lần thành công (số lần rút được vé 1) trong $n$ phép thử Bernoulli độc lập, đó là định nghĩa chính xác 100% của Phân phối Nhị thức $B(n, p)$.\n\nPhân tích bẫy sai:\n- Phương án B: Siêu bội chỉ xuất hiện khi rút KHÔNG hoàn lại.\n- Phương án C: Poisson chỉ là phân phối xấp xỉ khi $n$ lớn, $p$ nhỏ.\n- Phương án D: Bernoulli chỉ ứng với $n=1$.",
    "source": "Slide Week 07 tr. 22; Stat20 Mục 4.11"
  },
  {
    "id": "TN6_01",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Cơ bản",
    "question": "Cho $f(x)$ là hàm mật độ xác suất (pdf) của biến ngẫu nhiên liên tục $X$. Khẳng định nào sau đây là ĐÚNG?",
    "options": [
      "Giá trị $f(x)$ chính là xác suất tại điểm $x$, do đó luôn thỏa mãn $0 \\le f(x) \\le 1$",
      "\\(f(x) \\ge 0\\) với mọi $x$, tích phân toàn phần \\(\\int_{-\\infty}^{+\\infty} f(x) dx = 1\\), và giá trị $f(x)$ hoàn toàn có thể lớn hơn 1",
      "Với biến ngẫu nhiên liên tục, $P(X = c) > 0$ nếu $f(c) > 0$",
      "Tích phân toàn phần của hàm mật độ có thể bằng bất kỳ hằng số dương nào"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì theo định nghĩa toán học của hàm mật độ pdf:\n- $f(x) \\ge 0$ và $\\int_{-\\infty}^{+\\infty} f(x) dx = 1$.\n- $f(x)$ là MẬT ĐỘ xác suất (xác suất trên một đơn vị độ dài $P(x \\le X \\le x+dx) \\approx f(x)dx$), không phải là bản thân xác suất, nên giá trị $f(x)$ hoàn toàn CÓ THỂ lớn hơn 1 (ví dụ $X \\sim U(0; 0,5)$ có $f(x) = 1/(0,5 - 0) = 2 > 1$).\n\nPhân tích bẫy sai:\n- Phương án A: Bẫy sai kinh điển: nhầm lẫn mật độ $f(x)$ với xác suất $P(X=x)$.\n- Phương án C: Với mọi biến ngẫu nhiên liên tục, xác suất tại một điểm luôn bằng 0 ($P(X = c) = 0$).\n- Phương án D: Tích phân bắt buộc phải bằng đúng 1.",
    "source": "Slide Week 07 tr. 42; Stat20 Mục 4.14"
  },
  {
    "id": "TN6_02",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Cơ bản",
    "question": "Cho $X$ là biến ngẫu nhiên liên tục tuân theo phân phối Chuẩn $X \\sim N(\\mu = 50, \\sigma^2 = 25)$. Xác suất để $X$ nhận chính xác giá trị bằng 50 ($P(X = 50)$) là bao nhiêu?",
    "options": [
      "0,50",
      "\\(\\frac{1}{5\\sqrt{2\\pi}} \\approx 0,0798\\)",
      "Chính xác bằng 0",
      "0,68"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì đối với MỌI biến ngẫu nhiên liên tục, diện tích dưới đường cong tại một điểm duy nhất là một đoạn thẳng có độ rộng bằng 0:\n$P(X = c) = \\int_c^c f(x) dx = 0$.\nDo đó, xác suất tại điểm đúng bằng 50 chính xác bằng 0.\n\nPhân tích bẫy sai:\n- Phương án A: 0,50 là xác suất tích lũy $P(X \\le 50)$, không phải tại điểm.\n- Phương án B: $\\approx 0,0798$ là giá trị của HÀM MẬT ĐỘ $f(50) = \\frac{1}{\\sigma\\sqrt{2\\pi}}$, đây là chiều cao đỉnh chuông chứ không phải xác suất.\n- Phương án D: 0,68 là xác suất trong khoảng $\\pm 1\\sigma$.",
    "source": "Slide Week 07 tr. 43; Stat20 Mục 4.14"
  },
  {
    "id": "TN6_03",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Cơ bản",
    "question": "Với biến ngẫu nhiên liên tục $X$, phát biểu nào sau đây về các dấu bất đẳng thức là ĐÚNG?",
    "options": [
      "\\(P(a \\le X \\le b) > P(a < X < b)\\) vì có thêm hai đầu mút",
      "\\(P(a \\le X \\le b) = F(b) - F(a) + P(X = a) + P(X = b)\\)",
      "Dấu bằng chỉ có thể bỏ qua khi biến ngẫu nhiên là rời rạc",
      "\\(P(a \\le X \\le b) = P(a < X \\le b) = P(a \\le X < b) = P(a < X < b) = F(b) - F(a)\\)"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì do $P(X = a) = 0$ và $P(X = b) = 0$, việc lấy thêm hay bỏ đi hai điểm đầu mút không làm thay đổi tích phân (diện tích miền hình phẳng) của hàm mật độ.\n\nPhân tích bẫy sai:\n- Phương án A, B: Bẫy từ tư duy biến rời rạc, đối với biến rời rạc thì việc có dấu bằng làm tăng xác suất, nhưng biến liên tục thì không.\n- Phương án C: Ngược lại hoàn toàn, với biến rời rạc thì bắt buộc phải phân biệt chặt chẽ có dấu bằng hay không.",
    "source": "Slide Week 07 tr. 43; Stat20 Mục 4.14"
  },
  {
    "id": "TN6_04",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Trung bình",
    "question": "Cho hàm số $f(x) = k \\cdot x$ khi $0 \\le x \\le 2$ và $f(x) = 0$ với các giá trị khác. Giá trị của hằng số $k$ bằng bao nhiêu để $f(x)$ là một hàm mật độ xác suất hợp lệ?",
    "options": [
      "0,5",
      "1,0",
      "0,25",
      "2,0"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo điều kiện chuẩn hóa của hàm mật độ xác suất:\n$\\int_{-\\infty}^{+\\infty} f(x) dx = 1 \\iff \\int_0^2 k \\cdot x \\, dx = 1 \\iff k \\left[ \\frac{x^2}{2} \\right]_0^2 = 1 \\iff k \\cdot \\frac{4}{2} = 1 \\iff 2k = 1 \\iff k = 0,5$.\n\nPhân tích bẫy sai:\n- Phương án B: Nhầm tổng diện tích bằng 1 thì $k=1$.\n- Phương án C: Sai do tính $k \\cdot 4 = 1 \\implies k = 0,25$ (quên chia 2 khi lấy nguyên hàm).\n- Phương án D: Sai số học.",
    "source": "Slide Week 07 tr. 44"
  },
  {
    "id": "TN6_05",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Trung bình",
    "question": "Với hàm mật độ $f(x) = 0,5x$ trên đoạn $[0; 2]$ ở câu trên, kỳ vọng toán $E(X)$ bằng bao nhiêu?",
    "options": [
      "1,0",
      "4/3 (khoảng 1,333)",
      "2/3 (khoảng 0,667)",
      "2,0"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì theo định nghĩa kỳ vọng của biến ngẫu nhiên liên tục:\n$E(X) = \\int_{-\\infty}^{+\\infty} x \\cdot f(x) dx = \\int_0^2 x \\cdot (0,5x) dx = 0,5 \\int_0^2 x^2 dx = 0,5 \\left[ \\frac{x^3}{3} \\right]_0^2 = 0,5 \\cdot \\frac{8}{3} = \\frac{4}{3} \\approx 1,333$.\n(Do mật độ dồn về phía $x=2$ nhiều hơn nên trọng tâm kỳ vọng lệch về bên phải $4/3 > 1$).\n\nPhân tích bẫy sai:\n- Phương án A: 1,0 là trung điểm $(0+2)/2$, chỉ đúng nếu phân phối là phân phối Đều $U(0, 2)$.\n- Phương án C: Sai hệ số nguyên hàm.\n- Phương án D: 2,0 là cận trên.",
    "source": "Slide Week 07 tr. 45"
  },
  {
    "id": "TN6_06",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Cơ bản",
    "question": "Biến ngẫu nhiên $X$ tuân theo phân phối Đều trên khoảng $(10; 30)$, ký hiệu $X \\sim U(10, 30)$. Kỳ vọng $E(X)$ và phương sai $\\operatorname{Var}(X)$ lần lượt là:",
    "options": [
      "\\(E(X) = 20\\) và \\(\\operatorname{Var}(X) = 400\\)",
      "\\(E(X) = 20\\) và \\(\\operatorname{Var}(X) = 20\\)",
      "\\(E(X) = 20\\) và \\(\\operatorname{Var}(X) = 100/3 \\approx 33,33\\)",
      "\\(E(X) = 15\\) và \\(\\operatorname{Var}(X) = 33,33\\)"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì đối với phân phối Đều liên tục $U(a, b)$:\n- Kỳ vọng: $E(X) = \\frac{a + b}{2} = \\frac{10 + 30}{2} = 20$.\n- Phương sai: $\\operatorname{Var}(X) = \\frac{(b - a)^2}{12} = \\frac{(30 - 10)^2}{12} = \\frac{20^2}{12} = \\frac{400}{12} = \\frac{100}{3} \\approx 33,33$.\n\nPhân tích bẫy sai:\n- Phương án A: $400 = (b-a)^2$ (quên chia cho 12).\n- Phương án B: Nhầm phương sai bằng kỳ vọng.\n- Phương án D: Sai kỳ vọng.",
    "source": "Slide Week 07 tr. 50; Stat20 Mục 4.14"
  },
  {
    "id": "TN6_07",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Cơ bản",
    "question": "Cũng biến ngẫu nhiên $X \\sim U(10, 30)$ ở trên. Xác suất để $X$ nhận giá trị trong khoảng từ 15 đến 25 ($P(15 \\le X \\le 25)$) bằng bao nhiêu?",
    "options": [
      "0,25 (tức 25%)",
      "0,33 (tức 33,3%)",
      "0,10 (tức 10%)",
      "0,50 (tức 50%)"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì đối với phân phối Đều trên $[a, b]$, xác suất trên khoảng con $[c, d]$ đơn giản là tỷ số độ dài khoảng con trên độ dài toàn khoảng:\n$P(c \\le X \\le d) = \\frac{d - c}{b - a} = \\frac{25 - 15}{30 - 10} = \\frac{10}{20} = 0,50$ (50%).\n\nPhân tích bẫy sai:\n- Phương án A, B, C: Sai phép tính tỷ lệ độ dài.",
    "source": "Slide Week 07 tr. 50; Stat20 Mục 4.14"
  },
  {
    "id": "TN6_08",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Cơ bản",
    "question": "Cho biến ngẫu nhiên $X \\sim N(\\mu = 100, \\sigma^2 = 225)$. Giá trị chuẩn hóa (Z-score) tương ứng với giá trị quan sát $x = 130$ bằng bao nhiêu?",
    "options": [
      "+2,0",
      "+0,133",
      "+30",
      "+1,5"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì:\n- Phương sai $\\sigma^2 = 225 \\implies$ độ lệch chuẩn $\\sigma = \\sqrt{225} = 15$.\n- Công thức chuẩn hóa Z-score:\n$Z = \\frac{X - \\mu}{\\sigma} = \\frac{130 - 100}{15} = \\frac{30}{15} = +2,0$.\nÝ nghĩa: Giá trị 130 nằm cao hơn giá trị trung bình đúng 2 độ lệch chuẩn.\n\nPhân tích bẫy sai:\n- Phương án B: Sai do chia cho phương sai $\\sigma^2 = 225$ thay vì $\\sigma = 15$ ($30 / 225 \\approx 0,133$).\n- Phương án C: 30 là độ lệch tuyệt đối $x - \\mu$, chưa chuẩn hóa chia cho $\\sigma$.\n- Phương án D: Sai số học.",
    "source": "Slide Week 07 tr. 52; Stat20 Mục 4.15"
  },
  {
    "id": "TN6_09",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Cơ bản",
    "question": "Theo quy tắc thực nghiệm 68–95–99,7 của phân phối Chuẩn, tỷ lệ phần trăm dữ liệu nằm trong khoảng $(\\mu - \\sigma; \\mu + \\sigma)$ và trong khoảng $(\\mu - 2\\sigma; \\mu + 2\\sigma)$ xấp xỉ lần lượt là:",
    "options": [
      "Khoảng 50% và 90%",
      "Khoảng 68,3% và 95,5%",
      "Khoảng 75% và 88,9%",
      "Khoảng 68,3% và 99,7%"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì theo quy tắc hình chuông chuẩn 68–95–99,7:\n- Khoảng $\\pm 1\\sigma$ chứa khoảng $68,27\\% \\approx 68,3\\%$.\n- Khoảng $\\pm 2\\sigma$ chứa khoảng $95,45\\% \\approx 95,5\\%$.\n- Khoảng $\\pm 3\\sigma$ chứa khoảng $99,73\\% \\approx 99,7\\%$.\n\nPhân tích bẫy sai:\n- Phương án A: Sai số liệu.\n- Phương án C: 75% và 88,9% là các cận tối thiểu của Bất đẳng thức Chebyshev ($1 - 1/k^2$), không phải của phân phối Chuẩn.\n- Phương án D: 99,7% là của khoảng $\\pm 3\\sigma$.",
    "source": "Slide Week 07 tr. 54; Stat20 Mục 4.15"
  },
  {
    "id": "TN6_10",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Cơ bản",
    "question": "Cho biến ngẫu nhiên chuẩn tắc $Z \\sim N(0, 1)$, biết $\\Phi(1,96) = 0,9750$. Xác suất $P(Z > 1,96)$ bằng bao nhiêu?",
    "options": [
      "0,9750 (tức 97,5%)",
      "-0,9750",
      "0,0250 (tức 2,5%)",
      "0,0500 (tức 5%)"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì theo quy tắc biến cố đối:\n$P(Z > 1,96) = 1 - P(Z \\le 1,96) = 1 - \\Phi(1,96) = 1 - 0,9750 = 0,0250$ (2,5%).\n\nPhân tích bẫy sai:\n- Phương án A: 0,9750 là diện tích phía bên trái $P(Z \\le 1,96)$, câu hỏi hỏi phần đuôi bên phải ($Z > 1,96$).\n- Phương án B: Xác suất không bao giờ mang giá trị âm.\n- Phương án D: 0,0500 là tổng diện tích hai đuôi $P(|Z| > 1,96) = 2 \\times 0,0250 = 0,05$.",
    "source": "Slide Week 07 tr. 55; Stat20 Mục 4.15"
  },
  {
    "id": "TN6_11",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Cơ bản",
    "question": "Biết giá trị hàm phân phối tích lũy chuẩn tắc tại 1,5 là $\\Phi(1,5) = 0,9332$. Giá trị của $\\Phi(-1,5) = P(Z \\le -1,5)$ bằng bao nhiêu?",
    "options": [
      "-0,9332",
      "0,9332",
      "0,5000",
      "0,0668"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì đường cong mật độ chuẩn tắc đối xứng hoàn hảo qua trục tung ($z = 0$), do đó:\n$\\Phi(-z) = 1 - \\Phi(z)$.\nỞ đây: $\\Phi(-1,5) = 1 - \\Phi(1,5) = 1 - 0,9332 = 0,0668$.\n\nPhân tích bẫy sai:\n- Phương án A: Sai do đưa dấu âm ra ngoài $\\Phi(-z) = -\\Phi(z)$ (xác suất không âm!).\n- Phương án B: Sai do bỏ qua dấu âm của $z$.\n- Phương án C: 0,5000 là $\\Phi(0)$.",
    "source": "Slide Week 07 tr. 55; Stat20 Mục 4.15"
  },
  {
    "id": "TN6_12",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Trung bình",
    "question": "Điểm thi môn Xác suất thống kê của một trường đại học tuân theo phân phối Chuẩn với trung bình $\\mu = 70$ điểm và độ lệch chuẩn $\\sigma = 10$ điểm. Nhà trường muốn trao học bổng cho 5% sinh viên có điểm cao nhất (Top 5%). Biết rằng giá trị $z$ thỏa mãn $\\Phi(z) = 0,95$ là $z \\approx 1,645$. Điểm chuẩn tối thiểu để nhận học bổng xấp xỉ bằng bao nhiêu?",
    "options": [
      "86,45 điểm",
      "89,60 điểm",
      "71,65 điểm",
      "85,00 điểm"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì:\n- Sinh viên thuộc Top 5% điểm cao nhất đồng nghĩa với việc điểm số vượt qua 95% số sinh viên còn lại ($P(X \\le x_0) = 0,95$).\n- Điểm chuẩn hóa tương ứng là $z_{0,95} \\approx 1,645$.\n- Quy đổi ngược về thang điểm thực tế:\n$x_0 = \\mu + z \\cdot \\sigma = 70 + 1,645 \\cdot 10 = 70 + 16,45 = 86,45$ điểm.\n\nPhân tích bẫy sai:\n- Phương án B: $89,60$ điểm ứng với $z = 1,96$ (Top 2,5%).\n- Phương án C: Nhầm $z = 0,165$ hoặc cộng $70 + 1,645 = 71,645$ (quên nhân $\\sigma = 10$).\n- Phương án D: Làm tròn ước lượng.",
    "source": "Slide Week 07 tr. 56-57; Stat20 Mục 4.15"
  },
  {
    "id": "TN6_13",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Cơ bản",
    "question": "Thời gian hoạt động đến khi hỏng của một linh kiện điện tử tuân theo phân phối Mũ $Exp(\\lambda)$. Biết rằng linh kiện đã hoạt động bình thường suốt 100 giờ mà chưa hỏng. Xác suất để linh kiện này hoạt động thêm ít nhất 50 giờ nữa ($P(X > 150 \\mid X > 100)$) bằng bao nhiêu?",
    "options": [
      "Bằng $P(X > 150) = e^{-150\\lambda}$",
      "Bằng đúng \\(P(X > 50) = e^{-50\\lambda}\\) (Tính chất không nhớ - Memoryless)",
      "Bằng $P(X > 50) / P(X > 100)$",
      "Nhỏ hơn nhiều so với $P(X > 50)$ vì linh kiện đã bị hao mòn sau 100 giờ"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì phân phối Mũ là phân phối LIÊN TỤC DUY NHẤT sở hữu 'Tính chất không nhớ' (Memoryless Property):\n$P(X > s + t \\mid X > s) = P(X > t)$.\nỞ đây $s = 100$ và $t = 50$, do đó $P(X > 150 \\mid X > 100) = P(X > 50) = e^{-50\\lambda}$. Quá khứ đã sống 100 giờ không làm thay đổi tuổi thọ còn lại (coi như linh kiện 'không bị lão hóa' do chỉ hỏng bởi các xung điện ngẫu nhiên bên ngoài).\n\nPhân tích bẫy sai:\n- Phương án A: Nhầm lẫn bỏ qua điều kiện $X > 100$.\n- Phương án C: Chưa rút gọn biểu thức có điều kiện.\n- Phương án D: Bẫy trực giác đời thường về sự hao mòn cơ học (đối với hao mòn, người ta dùng phân phối Weibull, không phải phân phối Mũ).",
    "source": "Slide Week 07 tr. 63"
  },
  {
    "id": "TN6_14",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Cơ bản",
    "question": "Biến ngẫu nhiên $X$ có phân phối Mũ với tham số $\\lambda = 0,05$. Kỳ vọng $E(X)$ và độ lệch chuẩn $\\sigma(X)$ của $X$ lần lượt là:",
    "options": [
      "\\(E(X) = 0,05\\) và \\(\\sigma(X) = 0,05\\)",
      "\\(E(X) = 20\\) và \\(\\sigma(X) = 400\\)",
      "\\(E(X) = 20\\) và \\(\\sigma(X) = 20\\)",
      "\\(E(X) = 20\\) và \\(\\sigma(X) = \\sqrt{20}\\)"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì đối với phân phối Mũ $Exp(\\lambda)$:\n- Kỳ vọng: $E(X) = \\frac{1}{\\lambda} = \\frac{1}{0,05} = 20$.\n- Phương sai: $\\operatorname{Var}(X) = \\frac{1}{\\lambda^2} = \\frac{1}{0,0025} = 400$.\n- Độ lệch chuẩn: $\\sigma(X) = \\sqrt{\\operatorname{Var}(X)} = \\frac{1}{\\lambda} = 20$.\nĐặc trưng quan trọng: Phân phối Mũ luôn có Kỳ vọng và Độ lệch chuẩn BẰNG NHAU ($E(X) = \\sigma(X) = 1/\\lambda$).\n\nPhân tích bẫy sai:\n- Phương án A: Nhầm kỳ vọng chính là tham số $\\lambda$.\n- Phương án B: 400 là phương sai $\\operatorname{Var}(X)$, chưa khai căn để ra độ lệch chuẩn.\n- Phương án D: Sai số học.",
    "source": "Slide Week 07 tr. 63"
  },
  {
    "id": "TN6_15",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Trung bình",
    "question": "Thời gian chờ xe buýt (phút) tuân theo phân phối Mũ với tham số $\\lambda = 0,2$ ($X \\sim Exp(0,2)$). Xác suất một hành khách phải chờ KHÔNG QUÁ 5 PHÚT ($P(X \\le 5)$) bằng bao nhiêu?",
    "options": [
      "\\(e^{-1} \\approx 0,3679\\)",
      "\\(1 - e^{-0,2} \\approx 0,1813\\)",
      "0,5000",
      "\\(1 - e^{-1} \\approx 0,6321\\)"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì hàm phân phối tích lũy của $X \\sim Exp(\\lambda)$ là $F(x) = 1 - e^{-\\lambda x}$ với $x \\ge 0$.\nỞ đây $\\lambda = 0,2$ và $x = 5$, ta có:\n$P(X \\le 5) = 1 - e^{-0,2 \\cdot 5} = 1 - e^{-1} \\approx 1 - 0,367879 = 0,6321$ (tức 63,21%).\n\nPhân tích bẫy sai:\n- Phương án A: $e^{-1} \\approx 0,3679$ là xác suất phải chờ HƠN 5 PHÚT ($P(X > 5) = e^{-\\lambda x}$).\n- Phương án B: Sai do quên nhân $x=5$ vào số mũ.\n- Phương án C: Đoán mò.",
    "source": "Slide Week 07 tr. 63"
  },
  {
    "id": "TN6_16",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Trung bình",
    "question": "Phân phối Khi-bình phương với $k$ bậc tự do (ký hiệu $\\chi^2(k)$) được định nghĩa là phân phối của tổng nào sau đây?",
    "options": [
      "Tổng bình phương của $k$ biến ngẫu nhiên chuẩn tắc độc lập: \\(V = Z_1^2 + Z_2^2 + \\dots + Z_k^2\\) với $Z_i \\sim N(0, 1)$",
      "Tổng của $k$ biến ngẫu nhiên chuẩn tắc độc lập: $Z_1 + Z_2 + \\dots + Z_k$",
      "Tổng bình phương của $k$ biến ngẫu nhiên phân phối Đều trên $[0, 1]$",
      "Hiệu của hai biến ngẫu nhiên chuẩn tắc"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo định nghĩa toán học (Slide Week 07 tr. 64): Phân phối Khi-bình phương với $k$ bậc tự do là phân phối của tổng bình phương $k$ biến ngẫu nhiên chuẩn tắc độc lập $Z_i \\sim N(0, 1)$.\nDo là tổng của các bình phương nên biến $\\chi^2$ chỉ nhận giá trị không âm ($V \\ge 0$) và có phân phối lệch phải. Kỳ vọng $E(V) = k$ và phương sai $\\operatorname{Var}(V) = 2k$.\n\nPhân tích bẫy sai:\n- Phương án B: Tổng của $k$ biến chuẩn tắc $Z_1 + \\dots + Z_k$ có phân phối Chuẩn $N(0, k)$, không phải Khi-bình phương.\n- Phương án C, D: Sai định nghĩa.",
    "source": "Slide Week 07 tr. 64"
  },
  {
    "id": "TN6_17",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Cơ bản",
    "question": "Cho biến ngẫu nhiên $V$ tuân theo phân phối Khi-bình phương với 10 bậc tự do ($V \\sim \\chi^2(10)$). Kỳ vọng $E(V)$ và phương sai $\\operatorname{Var}(V)$ lần lượt là:",
    "options": [
      "\\(E(V) = 10\\) và \\(\\operatorname{Var}(V) = 10\\)",
      "\\(E(V) = 10\\) và \\(\\operatorname{Var}(V) = 20\\)",
      "\\(E(V) = 10\\) và \\(\\operatorname{Var}(V) = 100\\)",
      "\\(E(V) = 20\\) và \\(\\operatorname{Var}(V) = 40\\)"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì với phân phối Khi-bình phương $k$ bậc tự do:\n- Kỳ vọng: $E(V) = k = 10$.\n- Phương sai: $\\operatorname{Var}(V) = 2k = 2 \\times 10 = 20$.\n\nPhân tích bẫy sai:\n- Phương án A: Nhầm sang tính chất Poisson (Var = E).\n- Phương án C: $10^2 = 100$.\n- Phương án D: Nhầm $E = 2k$.",
    "source": "Slide Week 07 tr. 65"
  },
  {
    "id": "TN6_18",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Trung bình",
    "question": "Phát biểu nào sau đây so sánh ĐÚNG giữa Phân phối $t$-Student với $k$ bậc tự do và Phân phối Chuẩn tắc $N(0, 1)$?",
    "options": [
      "Phân phối $t$ chỉ nhận giá trị dương và bị lệch phải",
      "Phân phối $t$ có phương sai luôn nhỏ hơn 1",
      "Cả hai đều có đồ thị đối xứng hình chuông qua tâm 0, nhưng phân phối $t$ có đỉnh thấp hơn và phần đuôi dày hơn (heavy tails); khi $k \\to \\infty$, phân phối $t(k)$ hội tụ về $N(0, 1)$",
      "Phân phối $t$ và phân phối Chuẩn hoàn toàn trùng khớp nhau với mọi bậc tự do $k$"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì theo tính chất của phân phối $t$-Student (Slide Week 07 tr. 66-67):\n- $t(k)$ đối xứng qua 0 giống $N(0, 1)$, nhưng do mẫu số chứa độ lệch chuẩn mẫu ngẫu nhiên (chứa thêm độ bất định) nên phân phối $t$ tản rộng hơn, đỉnh thấp hơn, hai đuôi dày hơn (xác suất xảy ra các giá trị cực đoan cao hơn).\n- Phương sai của $t(k)$ là $\\frac{k}{k-2} > 1$ (với $k > 2$).\n- Khi bậc tự do $k \\to \\infty$, độ lệch chuẩn mẫu hội tụ về $\\sigma$ và phân phối $t(k)$ hội tụ hoàn toàn về Chuẩn tắc $N(0, 1)$.\n\nPhân tích bẫy sai:\n- Phương án A: Nhầm sang phân phối Khi-bình phương $\\chi^2$.\n- Phương án B: Phương sai của $t$ luôn LỚN HƠN 1 ($k/(k-2) > 1$).\n- Phương án D: Chúng chỉ trùng nhau ở giới hạn $k = \\infty$.",
    "source": "Slide Week 07 tr. 66-67"
  },
  {
    "id": "TN6_19",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Trung bình",
    "question": "Tuổi thọ của một loại bóng đèn led tuân theo phân phối Chuẩn với trung bình 1.200 giờ và độ lệch chuẩn 100 giờ. Nhà sản xuất đưa ra chính sách đổi mới miễn phí cho bóng đèn nào bị cháy trước 1.000 giờ. Biết $\\Phi(2,0) = 0,9772$. Tỷ lệ bóng đèn nhà sản xuất phải đổi mới xấp xỉ bằng bao nhiêu?",
    "options": [
      "97,72%",
      "5,00%",
      "0,27%",
      "2,28%"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì:\n- Chuẩn hóa Z-score tại mốc 1.000 giờ:\n$Z = \\frac{1.000 - 1.200}{100} = \\frac{-200}{100} = -2,0$.\n- Xác suất bóng đèn hỏng trước 1.000 giờ:\n$P(T < 1.000) = P(Z < -2,0) = \\Phi(-2,0) = 1 - \\Phi(2,0) = 1 - 0,9772 = 0,0228$ (tức 2,28%).\n\nPhân tích bẫy sai:\n- Phương án A: 97,72% là tỷ lệ bóng đèn KHÔNG bị hỏng và hoạt động tốt trên 1.000 giờ.\n- Phương án B: 5% là diện tích hai đuôi tại $z = \\pm 1,96$.\n- Phương án C: 0,27% là tỷ lệ tại $z = -3,0$.",
    "source": "Slide Week 07 tr. 55-56; Stat20 Mục 4.15"
  },
  {
    "id": "TN6_20",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Trung bình",
    "question": "Cho biến ngẫu nhiên $X$ có hàm mật độ $f(x) = 2x$ với $0 \\le x \\le 1$ (và $f(x) = 0$ ở các miền khác). Kỳ vọng của bình phương $E(X^2)$ bằng bao nhiêu?",
    "options": [
      "0,50",
      "0,67",
      "0,25",
      "1,00"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo quy tắc thống kê vô thức LOTUS cho biến ngẫu nhiên liên tục:\n$E(g(X)) = \\int_{-\\infty}^{+\\infty} g(x) f(x) dx$.\nÁp dụng cho $g(x) = x^2$:\n$E(X^2) = \\int_0^1 x^2 \\cdot (2x) dx = 2 \\int_0^1 x^3 dx = 2 \\left[ \\frac{x^4}{4} \\right]_0^1 = 2 \\cdot \\frac{1}{4} = 0,50$.\n\nPhân tích bẫy sai:\n- Phương án B: $2/3 \\approx 0,67$ là kỳ vọng $E(X) = \\int_0^1 x(2x)dx = 2/3$.\n- Phương án C: Sai số học khi tính nguyên hàm.\n- Phương án D: Sai tích phân.",
    "source": "Slide Week 07 tr. 45"
  },
  {
    "id": "TN6_21",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Nâng cao",
    "question": "Với biến ngẫu nhiên $X$ có hàm mật độ $f(x) = 2x$ trên $[0; 1]$ ở trên, Trung vị (Median $m$) của $X$ bằng bao nhiêu?",
    "options": [
      "0,5000",
      "\\(1/\\sqrt{2} \\approx 0,7071\\)",
      "2/3 (khoảng 0,6667)",
      "0,2500"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì Trung vị $m$ của biến liên tục là điểm chia đôi diện tích dưới hàm mật độ thành hai nửa bằng nhau (tức $F(m) = 0,50$):\n- Hàm cdf: $F(x) = \\int_0^x 2t dt = x^2$ với $x \\in [0, 1]$.\n- Giải phương trình: $F(m) = m^2 = 0,5 \\implies m = \\sqrt{0,5} = \\frac{1}{\\sqrt{2}} \\approx 0,7071$.\n(Do phân phối dồn nhiều diện tích về phía bên phải nên trung vị $0,7071$ lớn hơn $0,5$).\n\nPhân tích bẫy sai:\n- Phương án A: 0,5 là trung điểm hình học $[0, 1]$ (chỉ đúng khi hàm mật độ đều hoặc đối xứng).\n- Phương án C: $2/3 \\approx 0,6667$ là giá trị Trung bình (Mean $E(X)$), không phải Trung vị.\n- Phương án D: Sai số học.",
    "source": "Slide Week 07 tr. 44; Stat20 Mục 4.14"
  },
  {
    "id": "TN6_22",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Trung bình",
    "question": "Mối quan hệ bản chất giữa Phân phối Poisson và Phân phối Mũ trong một quá trình biến cố Poisson tốc độ $\\lambda$ là gì?",
    "options": [
      "Phân phối Poisson là biến liên tục còn phân phối Mũ là biến rời rạc",
      "Cả hai phân phối đều có cùng kỳ vọng bằng $\\lambda$",
      "Phân phối Poisson mô hình hóa SỐ LƯỢNG biến cố xảy ra trong một khoảng thời gian cố định, còn Phân phối Mũ mô hình hóa KHOẢNG THỜI GIAN CHỜ giữa hai biến cố liên tiếp",
      "Phân phối Mũ là giới hạn của phân phối Poisson khi $\\lambda \\to \\infty$"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì đây là cầu nối cốt lõi giữa hai phân phối quan trọng nhất của quá trình Poisson (Slide Week 07 tr. 63 và Stat20 Ch.4):\n- Đếm số sự kiện trong 1 đơn vị thời gian $\\implies N \\sim Po(\\lambda)$ (biến rời rạc).\n- Đo thời gian từ lúc này đến khi có sự kiện đầu tiên tiếp theo $\\implies T \\sim Exp(\\lambda)$ (biến liên tục).\nChứng minh: $P(T > t) = P(\\text{không có sự kiện nào trong khoảng } [0, t]) = e^{-\\lambda t} \\implies F(t) = 1 - e^{-\\lambda t}$, chính là cdf của phân phối Mũ.\n\nPhân tích bẫy sai:\n- Phương án A: Ngược lại (Poisson là rời rạc, Mũ là liên tục).\n- Phương án B: Kỳ vọng của Poisson là $\\lambda$, còn của Mũ là $1/\\lambda$.\n- Phương án D: Sai hoàn toàn.",
    "source": "Slide Week 07 tr. 63"
  },
  {
    "id": "TN6_23",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Cơ bản",
    "question": "Khi tăng độ lệch chuẩn $\\sigma$ của biến ngẫu nhiên phân phối Chuẩn $X \\sim N(\\mu, \\sigma^2)$ trong khi giữ nguyên giá trị trung bình $\\mu$, đồ thị hình chuông của hàm mật độ sẽ thay đổi như thế nào?",
    "options": [
      "Đồ thị co hẹp lại và đỉnh chuông nhô cao hơn",
      "Đồ thị tịnh tiến sang phía bên phải",
      "Hình dạng và chiều cao đỉnh đồ thị không thay đổi",
      "Đồ thị bị bè rộng sang hai bên và đỉnh chuông bị hạ thấp xuống (do tổng diện tích bên dưới luôn phải bằng 1)"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì chiều cao đỉnh chuông tại $x = \\mu$ bằng $\\frac{1}{\\sigma\\sqrt{2\\pi}}$. Khi $\\sigma$ tăng lên, mẫu số tăng nên chiều cao đỉnh giảm xuống; đồng thời để diện tích tích phân toàn phần luôn bảo toàn bằng đúng 1, hai sườn chuông bắt buộc phải trải rộng tản ra hai bên.\n\nPhân tích bẫy sai:\n- Phương án A: Đây là hiện tượng khi $\\sigma$ giảm đi (dữ liệu tập trung sát tâm hơn).\n- Phương án B: Đồ thị chỉ tịnh tiến sang phải khi $\\mu$ tăng lên.\n- Phương án C: Sai tính chất hình học của phân phối chuẩn.",
    "source": "Slide Week 07 tr. 52; Stat20 Mục 4.15"
  },
  {
    "id": "TN6_24",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Trung bình",
    "question": "Cho $X \\sim N(\\mu, \\sigma^2)$. Biết $\\Phi(1,5) = 0,9332$. Xác suất để $X$ nhận giá trị nằm trong khoảng $(\\mu - 1,5\\sigma; \\mu + 1,5\\sigma)$ bằng bao nhiêu?",
    "options": [
      "0,8664 (tức 86,64%)",
      "0,9332 (tức 93,32%)",
      "0,4332 (tức 43,32%)",
      "0,0668 (tức 6,68%)"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì khi chuẩn hóa khoảng đối xứng:\n$P(\\mu - 1,5\\sigma < X < \\mu + 1,5\\sigma) = P(-1,5 < Z < 1,5) = \\Phi(1,5) - \\Phi(-1,5)$.\nDo $\\Phi(-1,5) = 1 - \\Phi(1,5)$ nên:\n$P = \\Phi(1,5) - (1 - \\Phi(1,5)) = 2\\Phi(1,5) - 1 = 2 \\cdot 0,9332 - 1 = 1,8664 - 1 = 0,8664$ (86,64%).\n\nPhân tích bẫy sai:\n- Phương án B: 0,9332 là diện tích từ $-\\infty$ đến $1,5$ (quên trừ phần đuôi bên trái $\\Phi(-1,5)$).\n- Phương án C: $0,4332 = \\Phi(1,5) - 0,5$ chỉ là diện tích nửa khoảng từ 0 đến 1,5 (quên nhân 2).\n- Phương án D: 0,0668 là diện tích đuôi bên trái $\\Phi(-1,5)$.",
    "source": "Slide Week 07 tr. 55; Stat20 Mục 4.15"
  },
  {
    "id": "TN6_25",
    "topicId": 6,
    "topicName": "Biến ngẫu nhiên liên tục & Các phân phối liên tục",
    "level": "Cơ bản",
    "question": "Cho biến ngẫu nhiên $X \\sim N(\\mu = 20, \\sigma^2 = 16)$. Nếu đặt $Y = 3X - 10$, thì $Y$ tuân theo phân phối nào?",
    "options": [
      "Phân phối Chuẩn \\(N(50, 48)\\)",
      "Phân phối Chuẩn \\(N(50, 144)\\)",
      "Phân phối Chuẩn \\(N(50, 16)\\)",
      "Phân phối Đều \\(U(38, 62)\\)"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì một tính chất tuyệt đẹp của phân phối Chuẩn: Mọi tổ hợp tuyến tính của biến phân phối Chuẩn vẫn là một biến phân phối Chuẩn:\n- Kỳ vọng mới: $E(Y) = 3 E(X) - 10 = 3 \\cdot 20 - 10 = 50$.\n- Phương sai mới: $\\operatorname{Var}(Y) = 3^2 \\cdot \\operatorname{Var}(X) = 9 \\cdot 16 = 144$ (độ lệch chuẩn $\\sigma_Y = 3 \\cdot 4 = 12$).\nDo đó $Y \\sim N(50, 144)$.\n\nPhân tích bẫy sai:\n- Phương án A: Quên bình phương hệ số 3 khi tính phương sai: $3 \\cdot 16 = 48$.\n- Phương án C: Giữ nguyên phương sai 16.\n- Phương án D: Biến đổi tuyến tính của biến Chuẩn không thể chuyển thành biến Đều.",
    "source": "Slide Week 07 tr. 53; Stat20 Mục 4.15"
  },
  {
    "id": "TN7_01",
    "topicId": 7,
    "topicName": "Định lý giới hạn trung tâm (CLT) & Ứng dụng",
    "level": "Cơ bản",
    "question": "Cho $X_1, X_2, \\dots, X_n$ là các biến ngẫu nhiên độc lập cùng phân phối (i.i.d.) có kỳ vọng $\\mu$ và phương sai $\\sigma^2$ hữu hạn. Định lý Giới hạn Trung tâm (CLT) khẳng định điều gì khi kích thước mẫu $n$ đủ lớn?",
    "options": [
      "Bản thân từng biến $X_i$ sẽ tự động biến thành phân phối Chuẩn",
      "Tổng $S_n$ sẽ trở thành một hằng số chắc chắn bằng $n\\mu$",
      "Biến chuẩn hóa của tổng \\(Z_n = \\frac{S_n - n\\mu}{\\sigma\\sqrt{n}}\\) và của trung bình mẫu \\(Z_n = \\frac{\\bar{X}_n - \\mu}{\\sigma/\\sqrt{n}}\\) sẽ hội tụ về phân phối Chuẩn tắc $N(0, 1)$",
      "Phương sai của tổng $S_n$ sẽ tiến dần về 0"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì CLT khẳng định rằng khi $n$ lớn, phân phối của tổng $S_n$ và của trung bình mẫu $\\bar{X}_n$ sẽ có dạng hình chuông và tiến dần về phân phối Chuẩn, bất kể phân phối ban đầu của từng biến $X_i$ có hình dạng như thế nào (kể cả phân phối rời rạc, phân phối lệch mạnh hay phân phối đều).\n\nPhân tích bẫy sai:\n- Phương án A: Từng biến $X_i$ giữ nguyên phân phối gốc của nó, chỉ có TỔNG và TRUNG BÌNH của nhiều biến mới tiến về Chuẩn.\n- Phương án B: Tổng $S_n$ vẫn là biến ngẫu nhiên, không phải hằng số.\n- Phương án D: Phương sai của tổng $n\\sigma^2$ tiến ra vô cùng, không tiến về 0.",
    "source": "Slide Week 07 tr. 68-70; Stat20 Mục 4.17"
  },
  {
    "id": "TN7_02",
    "topicId": 7,
    "topicName": "Định lý giới hạn trung tâm (CLT) & Ứng dụng",
    "level": "Trung bình",
    "question": "Trọng lượng một người đi thang máy tuân theo phân phối Chuẩn $X \\sim N(\\mu = 65\\text{ kg}, \\sigma^2 = 100\\text{ kg}^2)$. Xét một nhóm gồm $n = 4$ người đi thang máy. Tổng trọng lượng $S_4 = X_1 + X_2 + X_3 + X_4$ tuân theo phân phối nào?",
    "options": [
      "Chỉ xấp xỉ Chuẩn theo CLT vì $n = 4 < 30$",
      "Không thể xác định được vì kích thước mẫu quá nhỏ ($n < 30$)",
      "Phân phối Chuẩn $N(260, 100)$",
      "Phân phối Chuẩn CHÍNH XÁC \\(N(260, 400)\\) với mọi $n$ mà KHÔNG CẦN điều kiện $n \\ge 30$"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì đây là một bẫy phân biệt lý thuyết cực kỳ quan trọng:\n- Nếu các biến thành phần $X_i$ BẢN THÂN NÓ ĐÃ CÓ PHÂN PHỐI CHUẨN, thì tổng của chúng có phân phối Chuẩn CHÍNH XÁC TUYỆT ĐỐI với BẤT KỲ $n \\ge 1$ nào (tính chất đóng kín tuyến tính của biến Chuẩn), không cần đến CLT và không cần điều kiện $n \\ge 30$.\n- Kỳ vọng tổng: $4 \\times 65 = 260$ kg.\n- Phương sai tổng: $4 \\times 100 = 400$ $\\text{kg}^2$ (độ lệch chuẩn $\\sigma = \\sqrt{400} = 20$ kg).\nDo đó $S_4 \\sim N(260, 400)$ chính xác 100%.\n\nPhân tích bẫy sai:\n- Phương án A, B: Bẫy máy móc đòi hỏi $n \\ge 30$ ngay cả khi biến gốc đã là phân phối Chuẩn (CLT chỉ cần thiết khi phân phối gốc KHÔNG PHẢI là chuẩn).\n- Phương án C: Quên nhân $n=4$ vào phương sai.",
    "source": "Slide Week 07 tr. 70; Stat20 Mục 4.17"
  },
  {
    "id": "TN7_03",
    "topicId": 7,
    "topicName": "Định lý giới hạn trung tâm (CLT) & Ứng dụng",
    "level": "Cơ bản",
    "question": "Khi phân phối của các biến thành phần $X_i$ không phải là phân phối Chuẩn (nhưng không bị lệch quá cực đoan), quy tắc ngón tay cái (rule of thumb) phổ biến trong thống kê yêu cầu kích thước mẫu $n$ tối thiểu bằng bao nhiêu để xấp xỉ CLT đủ tin cậy?",
    "options": [
      "\\(n \\ge 30\\)",
      "\\(n \\ge 10\\)",
      "\\(n \\ge 100\\)",
      "\\(n \\ge 1.000\\)"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì trong thực hành thống kê (Slide Week 07 và Stat20 Ch.4), mốc $n \\ge 30$ là quy ước ngón tay cái kinh điển. Với $n \\ge 30$, hình dạng phân phối của trung bình mẫu $\\bar{X}_n$ đã rất sát với đường cong hình chuông chuẩn, ngay cả khi phân phối gốc có dạng phân phối Đều hay phân phối Rời rạc.\n\nPhân tích bẫy sai:\n- Phương án B: $n \\ge 10$ thường chưa đủ để xấp xỉ tốt nếu phân phối gốc có độ lệch.\n- Phương án C, D: Kích thước mẫu quá lớn không cần thiết đối với hầu hết các phân phối thông thường.",
    "source": "Slide Week 07 tr. 71; Stat20 Mục 4.17"
  },
  {
    "id": "TN7_04",
    "topicId": 7,
    "topicName": "Định lý giới hạn trung tâm (CLT) & Ứng dụng",
    "level": "Cơ bản",
    "question": "Khi sử dụng phân phối Chuẩn liên tục $Y$ để xấp xỉ biến ngẫu nhiên nhận giá trị nguyên rời rạc $X$ (ví dụ số lần thành công trong phép thử Nhị thức), theo quy tắc hiệu chỉnh liên tục (continuity correction), xác suất tại đúng một điểm $P(X = k)$ được xấp xỉ bởi diện tích nào?",
    "options": [
      "\\(P(Y = k) = 0\\)",
      "\\(P(k - 0,5 \\le Y \\le k + 0,5)\\)",
      "\\(P(k \\le Y \\le k + 1)\\)",
      "\\(P(Y \\ge k)\\)"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì đối với biến liên tục $Y$, xác suất tại một điểm luôn bằng 0 ($P(Y=k)=0$). Để xấp xỉ cột xác suất rời rạc có đáy tại số nguyên $k$, ta mở rộng số nguyên $k$ thành một khoảng liên tục có độ rộng 1 đơn vị đối xứng quanh $k$, tức là đoạn $[k - 0,5; k + 0,5]$.\n\nPhân tích bẫy sai:\n- Phương án A: Bẫy không dùng hiệu chỉnh liên tục, khiến xác suất xấp xỉ bị triệt tiêu về 0 một cách vô lý.\n- Phương án C: Lệch sang phải nửa đơn vị.\n- Phương án D: Đây là diện tích của toàn bộ đuôi phải.",
    "source": "Slide Week 07 tr. 74"
  },
  {
    "id": "TN7_05",
    "topicId": 7,
    "topicName": "Định lý giới hạn trung tâm (CLT) & Ứng dụng",
    "level": "Trung bình",
    "question": "Với biến rời rạc nhận giá trị nguyên $X$, khi áp dụng hiệu chỉnh liên tục sang biến chuẩn $Y$, xác suất $P(X \\ge 25)$ và xác suất $P(X > 25)$ lần lượt được chuyển thành:",
    "options": [
      "\\(P(Y \\ge 25,5)\\) và \\(P(Y \\ge 24,5)\\)",
      "\\(P(Y \\ge 25,0)\\) cho cả hai trường hợp",
      "\\(P(Y \\ge 24,5)\\) và \\(P(Y \\ge 25,5)\\)",
      "\\(P(Y \\le 24,5)\\) và \\(P(Y \\le 25,5)\\)"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì:\n- $P(X \\ge 25)$ bao gồm các số nguyên $25, 26, 27, \\dots$. Điểm bắt đầu là cột 25, với mép trái là $25 - 0,5 = 24,5$. Do đó: $P(X \\ge 25) \\approx P(Y \\ge 24,5)$.\n- $P(X > 25)$ là biến cố không lấy 25, tương đương $X \\ge 26$, gồm các số $26, 27, 28, \\dots$. Điểm bắt đầu là cột 26, với mép trái là $26 - 0,5 = 25,5$. Do đó: $P(X > 25) \\approx P(Y \\ge 25,5)$.\n\nPhân tích bẫy sai:\n- Phương án A: Đảo ngược hai công thức.\n- Phương án B: Bỏ qua hiệu chỉnh liên tục, coi $X$ như biến liên tục.\n- Phương án D: Đảo ngược chiều bất đẳng thức.",
    "source": "Slide Week 07 tr. 74"
  },
  {
    "id": "TN7_06",
    "topicId": 7,
    "topicName": "Định lý giới hạn trung tâm (CLT) & Ứng dụng",
    "level": "Trung bình",
    "question": "Gieo một con xúc xắc cân đối 100 lần độc lập ($E(X) = 3,5; \\sigma = \\sqrt{35/12} \\approx 1,7078$). Tổng số chấm $S_{100}$ có kỳ vọng 350 và độ lệch chuẩn $\\sigma(S_{100}) \\approx 17,08$. Sử dụng CLT có hiệu chỉnh liên tục, biến đổi chuẩn hóa $Z$ để tính $P(S_{100} \\ge 380)$ là:",
    "options": [
      "\\(Z = \\frac{380 - 350}{17,08} \\approx 1,76\\)",
      "\\(Z = \\frac{380,5 - 350}{17,08} \\approx 1,79\\)",
      "\\(Z = \\frac{380 - 3,5}{1,7078} \\approx 220,5\\)",
      "\\(Z = \\frac{379,5 - 350}{17,08} \\approx 1,73\\)"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì theo quy tắc hiệu chỉnh liên tục cho $P(S_{100} \\ge 380)$, do là dấu $\\ge$ nên mép tích phân bắt đầu từ $380 - 0,5 = 379,5$.\nSau đó chuẩn hóa với trung bình $n\\mu = 350$ và độ lệch chuẩn $\\sigma\\sqrt{n} \\approx 17,08$:\n$Z = \\frac{379,5 - 350}{17,08} = \\frac{29,5}{17,08} \\approx 1,73$.\n\nPhân tích bẫy sai:\n- Phương án A: Quên hiệu chỉnh liên tục $\\pm 0,5$.\n- Phương án B: Hiệu chỉnh sai dấu $+0,5$ thay vì $-0,5$.\n- Phương án C: Nhầm công thức chuẩn hóa của 1 lần gieo thay vì của tổng 100 lần.",
    "source": "Slide Week 07 tr. 75"
  },
  {
    "id": "TN7_07",
    "topicId": 7,
    "topicName": "Định lý giới hạn trung tâm (CLT) & Ứng dụng",
    "level": "Trung bình",
    "question": "Trọng lượng của mỗi người vào thang máy có kỳ vọng $\\mu = 65$ kg và độ lệch chuẩn $\\sigma = 12$ kg. Một thang máy chở $n = 16$ người độc lập. Tải trọng an toàn tối đa của thang máy là 1.100 kg. Theo CLT, xác suất thang máy bị quá tải ($P(S_{16} > 1.100)$) xấp xỉ bằng bao nhiêu (biết $\\Phi(1,25) = 0,8944$)?",
    "options": [
      "10,56%",
      "89,44%",
      "1,25%",
      "21,12%"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo CLT cho tổng trọng lượng 16 người $S_{16}$ (do trọng lượng là biến liên tục nên không cần hiệu chỉnh liên tục $\\pm 0,5$):\n- Kỳ vọng tổng: $E(S_{16}) = 16 \\times 65 = 1.040$ kg.\n- Độ lệch chuẩn tổng: $\\sigma(S_{16}) = \\sigma \\sqrt{n} = 12 \\times \\sqrt{16} = 12 \\times 4 = 48$ kg.\n- Chuẩn hóa Z-score tại mức 1.100 kg:\n$Z = \\frac{1.100 - 1.040}{48} = \\frac{60}{48} = 1,25$.\n- Xác suất quá tải:\n$P(S_{16} > 1.100) = 1 - \\Phi(1,25) = 1 - 0,8944 = 0,1056$ (tức 10,56%).\n\nPhân tích bẫy sai:\n- Phương án B: 89,44% là xác suất thang máy AN TOÀN không bị quá tải ($P(S_{16} \\le 1.100)$).\n- Phương án C: Nhầm giá trị $Z = 1,25$ thành xác suất 1,25%.\n- Phương án D: Sai số học.",
    "source": "Slide Week 07 tr. 72"
  },
  {
    "id": "TN7_08",
    "topicId": 7,
    "topicName": "Định lý giới hạn trung tâm (CLT) & Ứng dụng",
    "level": "Nâng cao",
    "question": "Một viện nghiên cứu muốn thăm dò tỷ lệ cử tri ủng hộ một dự luật. Họ muốn tỷ lệ mẫu sai lệch so với tỷ lệ thực tế không quá 3% (tức $\\varepsilon = 0,03$) với độ tin cậy 95% (ứng với $z = 1,96$). Trong trường hợp chưa có bất kỳ thông tin nào về tỷ lệ ủng hộ trước đó (kịch bản xấu nhất), cỡ mẫu tối thiểu cần điều tra là bao nhiêu?",
    "options": [
      "385 cử tri",
      "1.068 cử tri",
      "2.401 cử tri",
      "500 cử tri"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì theo CLT cho tỷ lệ mẫu $\\hat{p} = \\bar{X}_n$:\n- Sai số biên: $\\varepsilon = z \\cdot \\sqrt{\\frac{p(1-p)}{n}}$.\n- Để bảo đảm với mọi $p$, ta lấy kịch bản phương sai lớn nhất (worst-case scenario) tại $p = 0,5 \\implies p(1-p) = 0,25$.\n- Suy ra cỡ mẫu tối thiểu:\n$n \\ge \\frac{z^2 \\cdot p(1-p)}{\\varepsilon^2} = \\frac{(1,96)^2 \\cdot 0,25}{(0,03)^2} = \\frac{3,8416 \\cdot 0,25}{0,0009} = \\frac{0,9604}{0,0009} \\approx 1.067,11$.\nLàm tròn lên số nguyên tiếp theo ta được $n = 1.068$ cử tri. Đây là con số tiêu chuẩn xuất hiện trên hầu hết các cuộc thăm dò dư luận uy tín trên thế giới (mẫu khoảng 1.000 - 1.100 người).\n\nPhân tích bẫy sai:\n- Phương án A: 385 là cỡ mẫu ứng với sai số rộng hơn $\\varepsilon = 0,05$ (5%).\n- Phương án C: Sai số học khi bình phương.\n- Phương án D: Ước lượng cảm tính.",
    "source": "Stat20 Mục 4.17; Slide Week 07 tr. 77"
  },
  {
    "id": "TN7_09",
    "topicId": 7,
    "topicName": "Định lý giới hạn trung tâm (CLT) & Ứng dụng",
    "level": "Nâng cao",
    "question": "Một trạm hải đăng cần duy trì chiếu sáng liên tục trong 2.000 giờ. Mỗi bóng đèn có tuổi thọ trung bình 100 giờ và độ lệch chuẩn 30 giờ. Khi một bóng đèn cháy, bóng tiếp theo được thay ngay lập tức (các tuổi thọ độc lập). Biết $\\Phi(1,645) = 0,95$. Cần chuẩn bị tối thiểu bao nhiêu bóng đèn ($n$) để xác suất hải đăng hoạt động liên tục không gián đoạn trong 2.000 giờ đạt ít nhất 95%?",
    "options": [
      "20 bóng đèn",
      "21 bóng đèn",
      "23 bóng đèn",
      "25 bóng đèn"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì theo Bài tập vận dụng 5 trong Slide Week 07 (tr. 90-91):\n- Tổng tuổi thọ của $n$ bóng đèn là $S_n \\sim N(100n, 30^2 n)$.\n- Yêu cầu: $P(S_n \\ge 2.000) \\ge 0,95 \\iff P\\left(Z \\ge \\frac{2.000 - 100n}{30\\sqrt{n}}\\right) \\ge 0,95$.\n- Do $\\Phi(1,645) = 0,95$ nên $P(Z \\ge -1,645) = 0,95$. Từ đó ta có bất phương trình:\n$\\frac{2.000 - 100n}{30\\sqrt{n}} \\le -1,645 \\iff 100n - 49,35\\sqrt{n} - 2.000 \\ge 0$.\n- Đặt $u = \\sqrt{n} > 0$, ta có phương trình bậc hai: $100u^2 - 49,35u - 2.000 \\ge 0$.\n- Giải ra: $u \\ge \\frac{49,35 + \\sqrt{49,35^2 + 800.000}}{200} \\approx \\frac{49,35 + 895,79}{200} \\approx 4,7257$.\n- Suy ra $n = u^2 \\ge (4,7257)^2 \\approx 22,33$.\n- Do số bóng đèn phải là số nguyên, ta cần tối thiểu $n = 23$ bóng đèn.\n\nPhân tích bẫy sai:\n- Phương án A: 20 bóng đèn là lấy $2.000 / 100 = 20$ (chỉ tính theo kỳ vọng trung bình, nhưng nếu lấy $n=20$ thì xác suất chỉ đạt đúng 50%, có tới 50% nguy cơ tắt điện giữa chừng!).\n- Phương án B: Làm tròn xuống $n = 21$ hoặc $22$ bóng thì xác suất chưa đạt $95\\%$.\n- Phương án D: Ước lượng dư thừa.",
    "source": "Slide Week 07 tr. 90-91 (Bài 5)"
  },
  {
    "id": "TN7_10",
    "topicId": 7,
    "topicName": "Định lý giới hạn trung tâm (CLT) & Ứng dụng",
    "level": "Nâng cao",
    "question": "Một công ty bảo hiểm bán 10.000 hợp đồng bảo hiểm xe máy độc lập. Xác suất mỗi hợp đồng gặp tai nạn phải bồi thường là 1% ($p = 0,01$). Khi có tai nạn, số tiền bồi thường cố định là 50 triệu đồng. Biết rằng giá trị $z$ ứng với tích lũy 99% là $z \\approx 2,33$. Để đảm bảo an toàn với xác suất 99% không bị vỡ quỹ bồi thường, công ty cần lập quỹ dự phòng bồi thường tối thiểu khoảng bao nhiêu?",
    "options": [
      "Đúng 5,00 tỷ đồng (bằng mức bồi thường kỳ vọng)",
      "Khoảng 10,00 tỷ đồng",
      "Khoảng 5,12 tỷ đồng",
      "Khoảng 6,16 tỷ đồng"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì:\n- Số vụ tai nạn $N \\sim B(n = 10.000, p = 0,01)$.\n- Kỳ vọng số vụ tai nạn: $E(N) = np = 10.000 \\times 0,01 = 100$ vụ.\n- Độ lệch chuẩn số vụ tai nạn: $\\sigma(N) = \\sqrt{np(1-p)} = \\sqrt{10.000 \\times 0,01 \\times 0,99} = \\sqrt{99} \\approx 9,95$ vụ.\n- Theo CLT, số vụ tai nạn tối đa ở mức tin cậy 99% ($z = 2,33$) là:\n$N_{0,99} = E(N) + z \\cdot \\sigma(N) = 100 + 2,33 \\times 9,95 \\approx 100 + 23,18 = 123,18$ vụ.\n- Số tiền bồi thường cần chuẩn bị:\n$\\text{Quỹ} = 123,18 \\times 50\\text{ triệu} \\approx 6.159\\text{ triệu} \\approx 6,16$ tỷ đồng.\n(Công ty cần dự phòng thêm $1,16$ tỷ đồng trên mức kỳ vọng 5 tỷ để hấp thụ rủi ro biến động ngẫu nhiên).\n\nPhân tích bẫy sai:\n- Phương án A: 5,00 tỷ đồng là chỉ tính theo kỳ vọng $100 \\times 50$, nếu để 5 tỷ thì xác suất vỡ quỹ lên tới 50%!\n- Phương án B: Ước lượng gấp đôi cảm tính.\n- Phương án C: Sai số học.",
    "source": "Slide Week 07 tr. 77"
  },
  {
    "id": "TN7_11",
    "topicId": 7,
    "topicName": "Định lý giới hạn trung tâm (CLT) & Ứng dụng",
    "level": "Trung bình",
    "question": "Quãng đường di chuyển mỗi ngày của một nhân viên giao hàng có trung bình $\\mu = 15$ km và độ lệch chuẩn $\\sigma = 3$ km. Theo dõi trong $n = 36$ ngày làm việc độc lập. Xác suất để quãng đường trung bình mỗi ngày trong 36 ngày đó vượt quá 16 km ($P(\\bar{X}_{36} > 16)$) bằng bao nhiêu (biết $\\Phi(2,0) = 0,9772$)?",
    "options": [
      "2,28%",
      "97,72%",
      "37,07%",
      "15,87%"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì theo CLT áp dụng cho biến trung bình mẫu $\\bar{X}_{36}$:\n- Kỳ vọng của trung bình mẫu: $E(\\bar{X}_{36}) = \\mu = 15$ km.\n- Độ lệch chuẩn của trung bình mẫu: $\\sigma(\\bar{X}_{36}) = \\frac{\\sigma}{\\sqrt{n}} = \\frac{3}{\\sqrt{36}} = \\frac{3}{6} = 0,5$ km.\n- Chuẩn hóa Z-score tại mốc 16 km:\n$Z = \\frac{16 - 15}{0,5} = \\frac{1}{0,5} = 2,0$.\n- Xác suất:\n$P(\\bar{X}_{36} > 16) = P(Z > 2,0) = 1 - \\Phi(2,0) = 1 - 0,9772 = 0,0228$ (tức 2,28%).\n\nPhân tích bẫy sai:\n- Phương án B: 97,72% là xác suất trung bình NHỎ HƠN HOẶC BẰNG 16 km ($P(\\bar{X} \\le 16)$).\n- Phương án C: $37,07\\%$ là kết quả nếu quên chia căn $n$ khi tính độ lệch chuẩn ($Z = (16-15)/3 = 0,33 \\implies 1 - 0,6293 = 0,3707$, đây là xác suất của MỘT NGÀY ĐƠN LẺ, không phải trung bình 36 ngày!).\n- Phương án D: Ứng với $Z = 1,0$.",
    "source": "Slide Week 07 tr. 73; Stat20 Mục 4.17"
  },
  {
    "id": "TN7_12",
    "topicId": 7,
    "topicName": "Định lý giới hạn trung tâm (CLT) & Ứng dụng",
    "level": "Cơ bản",
    "question": "Trường hợp nào sau đây KHÔNG THỂ áp dụng xấp xỉ phân phối Chuẩn (CLT) cho phân phối Nhị thức $B(n, p)$?",
    "options": [
      "Khi $n = 100$ và $p = 0,5$ ($np = 50 \\ge 10$)",
      "Khi $n = 100$ nhưng xác suất thành công cực nhỏ $p = 0,001$ ($np = 0,1 < 10$)",
      "Khi $n = 40$ và $p = 0,3$ ($np = 12 \\ge 10$ và $n(1-p) = 28 \\ge 10$)",
      "Khi $n = 200$ và $p = 0,1$ ($np = 20 \\ge 10$)"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì để xấp xỉ Chuẩn hoạt động tốt cho Nhị thức, phân phối không được quá lệch, đòi hỏi điều kiện kiểm tra:\n$np \\ge 10$ và $n(1 - p) \\ge 10$.\nỞ phương án A, $np = 100 \\times 0,001 = 0,1$ quá nhỏ, phân phối bị lệch cực độ về phía 0, không thể dùng phân phối Chuẩn đối xứng. Trong trường hợp này, bắt buộc phải dùng XẤP XỈ POISSON ($Po(\\lambda = 0,1)$).\n\nPhân tích bẫy sai:\n- Phương án A, C, D: Đều thỏa mãn mỹ mãn điều kiện $np \\ge 10$ và $n(1-p) \\ge 10$, xấp xỉ chuẩn rất chính xác.",
    "source": "Slide Week 07 tr. 71; Stat20 Mục 4.17"
  },
  {
    "id": "TN7_13",
    "topicId": 7,
    "topicName": "Định lý giới hạn trung tâm (CLT) & Ứng dụng",
    "level": "Trung bình",
    "question": "Khái niệm 'hội tụ' trong Định lý Giới hạn Trung tâm (CLT) chính xác là loại hội tụ nào trong lý thuyết xác suất?",
    "options": [
      "Hội tụ hầu chắc chắn (Almost sure convergence)",
      "Hội tụ theo trung bình bậc hai (Convergence in mean square)",
      "Hội tụ theo phân phối (Convergence in Distribution): Hàm phân phối tích lũy $F_{Z_n}(z)$ tiến dần về hàm phân phối tích lũy chuẩn tắc $\\Phi(z)$ tại mọi điểm $z$",
      "Hội tụ đều của hàm mật độ xác suất"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì Định lý Giới hạn Trung tâm khẳng định sự hội tụ theo phân phối (kí hiệu $Z_n \\xrightarrow{d} N(0, 1)$):\n$\\lim_{n \\to \\infty} P(Z_n \\le z) = \\Phi(z) = \\int_{-\\infty}^z \\frac{1}{\\sqrt{2\\pi}} e^{-t^2/2} dt$ với mọi số thực $z$.\nĐiều này không đồng nghĩa với việc từng giá trị biến ngẫu nhiên bằng nhau, mà chỉ là diện tích tích lũy xác suất tiệm cận về diện tích hình chuông chuẩn.\n\nPhân tích bẫy sai:\n- Phương án A, B, D: Đều là các dạng hội tụ mạnh hơn trong giải tích ngẫu nhiên, không phải phát biểu của CLT.",
    "source": "Slide Week 07 tr. 68"
  },
  {
    "id": "TN7_14",
    "topicId": 7,
    "topicName": "Định lý giới hạn trung tâm (CLT) & Ứng dụng",
    "level": "Trung bình",
    "question": "Cho $X_1, X_2, \\dots, X_{12}$ là 12 biến ngẫu nhiên độc lập cùng phân phối Đều trên $[0; 1]$ ($X_i \\sim U(0, 1)$ có $\\mu = 0,5$ và $\\sigma^2 = 1/12$). Biến ngẫu nhiên $Y = \\left(\\sum_{i=1}^{12} X_i\\right) - 6$ có đặc điểm gì nổi tiếng trong kỹ thuật mô phỏng máy tính?",
    "options": [
      "Có phân phối Đều trên khoảng $[-6; 6]$",
      "Có kỳ vọng bằng 6 và phương sai bằng 12",
      "Luôn nhận giá trị nguyên",
      "Có kỳ vọng bằng 0, phương sai bằng 1 và xấp xỉ rất sát với biến Chuẩn tắc $N(0, 1)$ (thuật toán cổ điển tạo số chuẩn tắc không cần tính hàm lượng giác)"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì:\n- Tổng 12 biến: $E(S_{12}) = 12 \\times 0,5 = 6$.\n- Phương sai tổng: $\\operatorname{Var}(S_{12}) = 12 \\times \\frac{1}{12} = 1 \\implies \\sigma(S_{12}) = 1$.\n- Khi trừ đi 6: $Y = S_{12} - 6$ có $E(Y) = 0$ và $\\operatorname{Var}(Y) = 1$.\nDo phân phối Đều có tính đối xứng rất cao, chỉ cần $n = 12$ biến là tổng của chúng đã triệt tiêu độ gồ ghề và khớp với đường cong Chuẩn tắc $N(0, 1)$ tới kinh ngạc. Đây chính là thuật toán phát sinh biến ngẫu nhiên chuẩn sơ khai kinh điển trong các máy tính thế hệ đầu!\n\nPhân tích bẫy sai:\n- Phương án A: Tổng của nhiều biến Đều không còn là biến Đều nữa (nó trở thành phân phối Irwin-Hall hình chuông mượt mà).\n- Phương án B, C: Sai các tính chất cơ bản.",
    "source": "Slide Week 07 tr. 69"
  },
  {
    "id": "TN7_15",
    "topicId": 7,
    "topicName": "Định lý giới hạn trung tâm (CLT) & Ứng dụng",
    "level": "Cơ bản",
    "question": "Khi áp dụng CLT cho biến nhận giá trị nguyên (ví dụ phân phối Nhị thức), tại sao việc dùng Hiệu chỉnh liên tục (Continuity Correction $\\pm 0,5$) lại đặc biệt quan trọng khi cỡ mẫu $n$ ở mức vừa phải ($n$ khoảng 20 đến 50)?",
    "options": [
      "Vì nếu không cộng/trừ 0,5, ta sẽ bỏ sót hoàn toàn hoặc tính dư cả một cột xác suất tại điểm biên (vốn có bề rộng bằng 1), dẫn đến sai số đáng kể",
      "Vì hiệu chỉnh liên tục giúp biến đổi phương sai mẫu thành phương sai tổng thể",
      "Vì bắt buộc phải có hiệu chỉnh liên tục thì định lý CLT mới được chứng minh",
      "Vì nếu không hiệu chỉnh thì kết quả xác suất luôn lớn hơn 1"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì trên biểu đồ histogram của biến rời rạc, mỗi số nguyên $k$ là một cột hình chữ nhật có độ rộng đáy từ $k - 0,5$ đến $k + 0,5$. Nếu tính tích phân của đường cong liên tục từ mốc $k$ thay vì $k - 0,5$, ta sẽ vô tình cắt xén mất một nửa diện tích của cột tại điểm $k$, gây ra sai số cố tật khá lớn khi $n$ chưa cực kỳ khổng lồ.\n\nPhân tích bẫy sai:\n- Phương án B, C, D: Đều là các giải thích sai bản chất hình học.",
    "source": "Slide Week 07 tr. 74"
  },
  {
    "id": "TN7_16",
    "topicId": 7,
    "topicName": "Định lý giới hạn trung tâm (CLT) & Ứng dụng",
    "level": "Trung bình",
    "question": "Một mẫu ngẫu nhiên gồm $n = 64$ quan sát độc lập được rút ra từ một tổng thể có $\\mu = 50$ và $\\sigma = 16$. Biết $\\Phi(1,0) = 0,8413$. Xác suất để trung bình mẫu $\\bar{X}_{64}$ nằm trong khoảng từ 48 đến 52 ($P(48 \\le \\bar{X}_{64} \\le 52)$) xấp xỉ bằng bao nhiêu?",
    "options": [
      "84,13%",
      "68,26%",
      "34,13%",
      "95,45%"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì:\n- Sai số chuẩn của trung bình mẫu: $\\sigma(\\bar{X}) = \\frac{\\sigma}{\\sqrt{n}} = \\frac{16}{\\sqrt{64}} = \\frac{16}{8} = 2$.\n- Chuẩn hóa hai cận:\n  + Cận dưới: $z_1 = \\frac{48 - 50}{2} = -1,0$.\n  + Cận trên: $z_2 = \\frac{52 - 50}{2} = +1,0$.\n- Xác suất:\n$P(-1,0 \\le Z \\le 1,0) = \\Phi(1,0) - \\Phi(-1,0) = 2\\Phi(1,0) - 1 = 2 \\times 0,8413 - 1 = 1,6826 - 1 = 0,6826$ (68,26%).\n(Đúng bằng quy tắc $1\\sigma$ chuẩn!).\n\nPhân tích bẫy sai:\n- Phương án A: 84,13% là diện tích từ $-\\infty$ đến $+1,0$.\n- Phương án C: 34,13% chỉ là nửa khoảng từ 50 đến 52.\n- Phương án D: 95,45% ứng với khoảng $\\pm 2\\sigma$ (từ 46 đến 54).",
    "source": "Slide Week 07 tr. 73; Stat20 Mục 4.17"
  },
  {
    "id": "TN7_17",
    "topicId": 7,
    "topicName": "Định lý giới hạn trung tâm (CLT) & Ứng dụng",
    "level": "Cơ bản",
    "question": "Số tiền chi tiêu của mỗi khách hàng tại siêu thị có trung bình 200.000 đồng và độ lệch chuẩn 50.000 đồng. Trong một buổi sáng có 100 khách hàng mua sắm độc lập. Xác suất để tổng doanh thu của siêu thị trong buổi sáng đó đạt ít nhất 21.000.000 đồng ($P(S_{100} \\ge 21.000.000)$) bằng bao nhiêu (biết $\\Phi(2,0) = 0,9772$)?",
    "options": [
      "97,72%",
      "50,00%",
      "2,28%",
      "10,00%"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì theo CLT cho tổng doanh thu 100 khách:\n- Kỳ vọng tổng: $E(S_{100}) = 100 \\times 200.000 = 20.000.000$ đồng.\n- Độ lệch chuẩn tổng: $\\sigma(S_{100}) = 50.000 \\times \\sqrt{100} = 500.000$ đồng.\n- Chuẩn hóa Z-score tại 21.000.000 đồng:\n$Z = \\frac{21.000.000 - 20.000.000}{500.000} = \\frac{1.000.000}{500.000} = 2,0$.\n- Xác suất:\n$P(S_{100} \\ge 21.000.000) = 1 - \\Phi(2,0) = 1 - 0,9772 = 0,0228$ (2,28%).\n\nPhân tích bẫy sai:\n- Phương án A: 97,72% là xác suất doanh thu DƯỚI 21 triệu đồng.\n- Phương án B: 50% là xác suất đạt mức kỳ vọng 20 triệu đồng.\n- Phương án D: Sai số học.",
    "source": "Slide Week 07 tr. 72"
  },
  {
    "id": "TN7_18",
    "topicId": 7,
    "topicName": "Định lý giới hạn trung tâm (CLT) & Ứng dụng",
    "level": "Trung bình",
    "question": "Sự khác biệt cốt lõi nhất giữa Luật số lớn (WLLN) và Định lý Giới hạn Trung tâm (CLT) là gì?",
    "options": [
      "WLLN áp dụng cho biến liên tục, còn CLT chỉ áp dụng cho biến rời rạc",
      "WLLN đòi hỏi $n \\ge 30$, còn CLT đúng với mọi $n$",
      "Hai định lý này là một, chỉ khác tên gọi",
      "WLLN trả lời câu hỏi: 'Trung bình mẫu đi về đâu?' (nó co cụm về kỳ vọng $\\mu$ như một điểm cố định); còn CLT trả lời câu hỏi: 'Sự dao động ngẫu nhiên quanh $\\mu$ có hình dạng như thế nào?' (nó có hình dạng chuông chuẩn với độ tản mát $\\sigma/\\sqrt{n}$)"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì đây là cách phân biệt kinh điển và sâu sắc nhất giữa hai trụ cột của lý thuyết xác suất hiện đại:\n- WLLN cho biết hành vi bậc một (First-order behavior): $\\bar{X}_n \\xrightarrow{P} \\mu$ (độ phân tán biến mất, trung bình mẫu hội tụ về một hằng số thực).\n- CLT cho biết hành vi bậc hai (Second-order fluctuation): khi phóng đại độ lệch đó lên $\\sqrt{n}$ lần (tức xem xét $\\sqrt{n}(\\bar{X}_n - \\mu)$), ta thấy quy luật dao động ngẫu nhiên quanh tâm có hình chuông chuẩn hoàn hảo $N(0, \\sigma^2)$.\n\nPhân tích bẫy sai:\n- Phương án A, B, C: Đều sai lệch hoàn toàn về mặt lý thuyết.",
    "source": "Slide Week 07 tr. 38, 68; Stat20 Mục 4.17"
  },
  {
    "id": "TN7_19",
    "topicId": 7,
    "topicName": "Định lý giới hạn trung tâm (CLT) & Ứng dụng",
    "level": "Cơ bản",
    "question": "Cho biến ngẫu nhiên nhận giá trị nguyên $X$. Khi xấp xỉ bằng biến Chuẩn $Y$, xác suất để $X$ nhận giá trị từ $a$ đến $b$ ($P(a \\le X \\le b)$, với $a < b$ là các số nguyên) được hiệu chỉnh liên tục thành:",
    "options": [
      "\\(P(a - 0,5 \\le Y \\le b + 0,5)\\)",
      "\\(P(a + 0,5 \\le Y \\le b - 0,5)\\)",
      "\\(P(a \\le Y \\le b)\\)",
      "\\(P(a - 1 \\le Y \\le b + 1)\\)"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì đoạn $[a, b]$ gồm các cột từ $a$ đến $b$. Mép trái của cột đầu tiên $a$ là $a - 0,5$, và mép phải của cột cuối cùng $b$ là $b + 0,5$. Do đó diện tích bao trọn vẹn toàn bộ các cột này là đoạn $[a - 0,5; b + 0,5]$.\n\nPhân tích bẫy sai:\n- Phương án B: Co hẹp khoảng, làm mất nửa cột tại $a$ và nửa cột tại $b$.\n- Phương án C: Bỏ qua hiệu chỉnh liên tục.\n- Phương án D: Mở rộng quá mức cần thiết.",
    "source": "Slide Week 07 tr. 74"
  },
  {
    "id": "TN7_20",
    "topicId": 7,
    "topicName": "Định lý giới hạn trung tâm (CLT) & Ứng dụng",
    "level": "Cơ bản",
    "question": "Để giảm sai số chuẩn (độ lệch chuẩn của trung bình mẫu $\\sigma(\\bar{X}_n)$) đi 10 lần, ta cần phải tăng kích thước mẫu $n$ lên bao nhiêu lần?",
    "options": [
      "10 lần",
      "100 lần",
      "\\(\\sqrt{10} \\approx 3,16\\) lần",
      "1.000 lần"
    ],
    "correctIndex": 1,
    "explanation": "Đáp án đúng là B vì sai số chuẩn tỷ lệ nghịch với căn bậc hai của kích thước mẫu: $\\sigma(\\bar{X}_n) = \\frac{\\sigma}{\\sqrt{n}}$.\nĐể mẫu số $\\sqrt{n}$ tăng gấp 10 lần, bắt buộc $n$ phải tăng gấp $10^2 = 100$ lần.\nĐây là 'Quy luật lợi ích giảm dần' trong lấy mẫu thống kê: muốn tăng độ chính xác lên gấp đôi thì phải tốn gấp 4 lần chi phí mẫu; muốn chính xác gấp 10 lần thì phải lấy mẫu gấp 100 lần!\n\nPhân tích bẫy sai:\n- Phương án A: Bẫy nhầm tỷ lệ thuận trực tiếp với $n$.\n- Phương án C, D: Sai số học.",
    "source": "Slide Week 07 tr. 26; Stat20 Mục 4.13"
  },
  {
    "id": "TN7_21",
    "topicId": 7,
    "topicName": "Định lý giới hạn trung tâm (CLT) & Ứng dụng",
    "level": "Trung bình",
    "question": "Tỷ lệ phế phẩm thực tế của một quy trình sản xuất là $p = 0,20$. Kiểm tra một mẫu ngẫu nhiên độc lập gồm $n = 400$ sản phẩm. Sai số chuẩn của tỷ lệ phế phẩm mẫu $\\sigma(\\hat{p})$ bằng bao nhiêu và xác suất để tỷ lệ phế phẩm trong mẫu vượt quá 24% ($P(\\hat{p} \\ge 0,24)$) bằng bao nhiêu (biết $\\Phi(2,0) = 0,9772$)?",
    "options": [
      "\\(\\sigma(\\hat{p}) = 0,04\\) và \\(P(\\hat{p} \\ge 0,24) \\approx 15,87\\%\\)",
      "\\(\\sigma(\\hat{p}) = 8\\) và \\(P(\\hat{p} \\ge 0,24) \\approx 50\\%\\)",
      "\\(\\sigma(\\hat{p}) = 0,02\\) và \\(P(\\hat{p} \\ge 0,24) \\approx 2,28\\%\\)",
      "\\(\\sigma(\\hat{p}) = 0,02\\) và \\(P(\\hat{p} \\ge 0,24) \\approx 97,72\\%\\)"
    ],
    "correctIndex": 2,
    "explanation": "Đáp án đúng là C vì theo CLT cho tỷ lệ mẫu $\\hat{p} = \\frac{S_n}{n}$:\n- Kỳ vọng của tỷ lệ mẫu: $E(\\hat{p}) = p = 0,20$.\n- Sai số chuẩn của tỷ lệ mẫu:\n$\\sigma(\\hat{p}) = \\sqrt{\\frac{p(1 - p)}{n}} = \\sqrt{\\frac{0,20 \\times 0,80}{400}} = \\sqrt{\\frac{0,16}{400}} = \\frac{0,4}{20} = 0,02$ (tức 2%).\n- Chuẩn hóa Z-score tại $\\hat{p} = 0,24$:\n$Z = \\frac{0,24 - 0,20}{0,02} = \\frac{0,04}{0,02} = 2,0$.\n- Xác suất:\n$P(\\hat{p} \\ge 0,24) = 1 - \\Phi(2,0) = 1 - 0,9772 = 0,0228$ (tức 2,28%).\n\nPhân tích bẫy sai:\n- Phương án A: Sai do tính $\\sqrt{0,16} / 10 = 0,04$.\n- Phương án B: 8 là độ lệch chuẩn của SỐ LƯỢNG phế phẩm $\\sigma(S_n) = \\sqrt{np(1-p)} = \\sqrt{64} = 8$, không phải của TỶ LỆ $\\hat{p}$.\n- Phương án D: 97,72% là diện tích đuôi bên trái ($P \\le 0,24$).",
    "source": "Slide Week 07 tr. 76; Stat20 Mục 4.17"
  },
  {
    "id": "TN7_22",
    "topicId": 7,
    "topicName": "Định lý giới hạn trung tâm (CLT) & Ứng dụng",
    "level": "Trung bình",
    "question": "Chi phí bảo trì hàng năm của mỗi máy móc trong phân xưởng có trung bình $\\mu = 10$ triệu đồng và độ lệch chuẩn $\\sigma = 2$ triệu đồng. Phân xưởng có $n = 25$ máy móc hoạt động độc lập. Ngân sách dự trù cho toàn bộ phân xưởng là 265 triệu đồng. Biết $\\Phi(1,5) = 0,9332$. Xác suất để tổng chi phí bảo trì không vượt quá ngân sách dự trù ($P(S_{25} \\le 265)$) bằng bao nhiêu?",
    "options": [
      "6,68%",
      "50,00%",
      "84,13%",
      "93,32%"
    ],
    "correctIndex": 3,
    "explanation": "Đáp án đúng là D vì:\n- Kỳ vọng tổng chi phí: $E(S_{25}) = 25 \\times 10 = 250$ triệu đồng.\n- Độ lệch chuẩn tổng chi phí: $\\sigma(S_{25}) = \\sigma \\sqrt{n} = 2 \\times \\sqrt{25} = 2 \\times 5 = 10$ triệu đồng.\n- Chuẩn hóa Z-score:\n$Z = \\frac{265 - 250}{10} = \\frac{15}{10} = 1,5$.\n- Xác suất chi phí không vượt ngân sách:\n$P(S_{25} \\le 265) = \\Phi(1,5) = 0,9332$ (tức 93,32%).\n\nPhân tích bẫy sai:\n- Phương án A: 6,68% là xác suất BỊ VƯỢT NGÂN SÁCH ($1 - 0,9332$).\n- Phương án B: 50% là xác suất không vượt 250 triệu.\n- Phương án C: Ứng với $Z = 1,0$.",
    "source": "Slide Week 07 tr. 72"
  },
  {
    "id": "TN7_23",
    "topicId": 7,
    "topicName": "Định lý giới hạn trung tâm (CLT) & Ứng dụng",
    "level": "Cơ bản",
    "question": "Vì sao Định lý Giới hạn Trung tâm (CLT) được tôn vinh là 'hòn đá tảng' của toàn bộ nền thống kê suy luận hiện đại?",
    "options": [
      "Vì nó giải thích tại sao phân phối Chuẩn xuất hiện phổ biến khắp nơi trong tự nhiên và khoa học, đồng thời cho phép ta xây dựng khoảng tin cậy và kiểm định giả thuyết cho trung bình tổng thể ngay cả khi hoàn toàn KHÔNG BIẾT phân phối gốc của dữ liệu",
      "Vì nó chứng minh rằng mọi hiện tượng trong vũ trụ đều là tất định",
      "Vì nó giúp tính toán xác suất mà không cần dùng đến bất kỳ phép tính tích phân nào",
      "Vì nó đảm bảo sai số thống kê luôn bằng 0 nếu mẫu đạt trên 30"
    ],
    "correctIndex": 0,
    "explanation": "Đáp án đúng là A vì trong thực tế, các nhà khoa học gần như không bao giờ biết được hình dạng phân phối thực sự của tổng thể. CLT trao cho chúng ta một sức mạnh phi thường: chỉ cần kích thước mẫu $n$ đủ lớn ($n \\ge 30$), ta được phép sử dụng phân phối Chuẩn với tất cả các công cụ suy luận mạnh mẽ (Z-test, khoảng tin cậy) để phân tích trung bình mẫu một cách hoàn toàn hợp lệ và chính xác.\n\nPhân tích bẫy sai:\n- Phương án B, C, D: Đều là các nhận định sai lệch và phản khoa học.",
    "source": "Slide Week 07 tr. 68-70; Stat20 Mục 4.17"
  }
];
