# LỘ TRÌNH ÔN THI GIỮA KỲ XÁC SUẤT THỐNG KÊ (UET.MAT1052)
## Hướng Dẫn Tự Học Tương Tác: Từ Mất Gốc Đến Điểm Tuyệt Đối
### Tác giả: Bộ tài liệu Ôn thi Chuẩn UET MAT1052 | Cập nhật theo Slide Tuần 01 – Tuần 07

---

## 1. TỔNG QUAN VÀ ĐỊNH VỊ MỤC TIÊU

### 1.1. Cấu trúc bài thi Giữa kỳ UET MAT1052
Theo quy định giảng dạy và cấu trúc đề thi chính thức của Trường Đại học Công nghệ (ĐHQGHN):
- **Thời lượng làm bài**: **90 phút**.
- **Hình thức thi**: Kết hợp **50% Trắc nghiệm khách quan** và **50% Tự luận giải tích**.
  - **Phần Trắc nghiệm (5.0 điểm)**: Khoảng 20 – 25 câu hỏi (0.2 – 0.25 điểm/câu), quét qua toàn bộ 7 chủ đề. Kiểm tra lý thuyết định tính, nhận diện mô hình, diễn giải chỉ số thống kê, và các bài toán tính toán nhanh 1 – 2 bước.
  - **Phần Tự luận (5.0 điểm)**: Thường gồm 3 – 4 bài toán lớn (chia thành 2 – 3 ý nhỏ mỗi bài), tập trung sâu vào:
    1. *Thống kê mô tả & Hồi quy tuyến tính (OLS)*: Tìm phương trình hồi quy mẫu $\hat{y} = b_0 + b_1 x$, giải thích ý nghĩa hệ số, tính hệ số xác định $R^2$, dự báo.
    2. *Xác suất cổ điển & Công thức Bayes*: Bài toán chọn ngẫu nhiên, xác suất có điều kiện, kiểm định y tế / sàng lọc sản phẩm lỗi.
    3. *Biến ngẫu nhiên rời rạc / Phân phối thông dụng*: Bảng phân phối xác suất (pmf), hàm tích lũy (cdf), tính kỳ vọng $E(X)$, phương sai $\operatorname{Var}(X)$, áp dụng mô hình Nhị thức $B(n, p)$ hoặc Poisson $Po(\lambda)$.
    4. *Phân phối Chuẩn & Định lý giới hạn trung tâm (CLT)*: Chuẩn hóa $Z$, tra bảng $\Phi(z)$, tính xác suất tổng $S_n$ hoặc trung bình mẫu $\bar{X}_n$, giải phương trình tìm cỡ mẫu $n$ hoặc số linh kiện dự phòng.

### 1.2. Đối tượng và Khởi điểm học tập
Bộ tài liệu này được thiết kế dành riêng cho bạn nếu bạn thuộc một trong các tình huống sau:
- **Tình huống 1 (Mất gốc / Bắt đầu từ số 0)**: Đã bỏ lỡ nhiều buổi học trên lớp, chưa nắm vững từ Mục 2.4 (Thống kê mô tả phân tán) đến Tuần 07 (CLT). Cần một kế hoạch cấp tốc để qua môn với điểm khá/giỏi.
- **Tình huống 2 (Đã học nhưng hay nhầm công thức và rơi vào bẫy)**: Hiểu khái niệm mơ hồ nhưng khi làm bài thường xuyên nhầm giữa *độc lập* và *xung khắc*, quên hiệu chỉnh liên tục $\pm 0.5$, chia nhầm $n$ thay vì $\sqrt{n}$ trong CLT.
- **Tình huống 3 (Mục tiêu A / A+)**: Muốn tối ưu hóa tốc độ làm trắc nghiệm, trình bày tự luận chuẩn từng barem điểm để không bị trừ dù chỉ 0.25 điểm.

---

## 2. KẾ HOẠCH 1: LỘ TRÌNH CẤP TỐC 72 GIỜ (3 NGÀY TRƯỚC GIỜ G)
> **Mục tiêu**: Lấy chắc **7.5 – 8.5 điểm** chỉ trong 3 ngày cuối cùng.  
> **Nguyên tắc vàng**: *"Tập trung 80% sức lực vào 20% dạng toán chiếm 80% điểm số (Pareto Principle)"*. Tuyệt đối không sa đà vào các chứng minh lý thuyết phức tạp, ưu tiên làm chủ các bài toán tự luận kinh điển và tra cứu sổ tay công thức.

### Lịch trình chi tiết từng ngày (Chiến dịch 72 giờ)

```
[Ngày 1: Ăn chắc Điểm Tự luận Cơ sở]
├── Sáng (8h - 11h30) : Chủ đề 1 (Thống kê mô tả + OLS) -> Làm bài TL1_1, TL1_2, TL1_3
├── Chiều (13h30 - 17h): Chủ đề 2 (Xác suất điều kiện + Bayes) -> Làm bài TL2_1, TL2_3, TL2_4
└── Tối (19h30 - 22h30): Quét 40 câu trắc nghiệm nhanh Topic 1 & 2 trên site/tracnghiem.html

[Ngày 2: Chinh phục Biến ngẫu nhiên & Định lý Giới hạn]
├── Sáng (8h - 11h30) : Chủ đề 3 & 4 (pmf, E(X), Var(X), Nhị thức, Poisson) -> Làm TL3_1, TL3_2, TL4_1, TL4_3
├── Chiều (13h30 - 17h): Chủ đề 6 & 7 (Phân phối chuẩn, Chuẩn hóa Z, CLT bóng đèn/thang máy) -> Làm TL6_1, TL6_2, TL7_1, TL7_7
└── Tối (19h30 - 22h30): Quét 50 câu trắc nghiệm Topic 3, 4, 6, 7; ghi nhận câu sai vào Sổ tay lỗi sai

[Ngày 3: Tổng lực Thi thử, Sửa lỗi & Phòng thi]
├── Sáng (8h - 10h)   : Bật Chế độ Thi thử 30 câu ngẫu nhiên trong 45 phút trên site/tracnghiem.html
├── Sáng (10h15 - 12h): Giải 2 đề tự luận mẫu bấm giờ 45 phút
├── Chiều (13h30 - 16h): Rà soát toàn bộ "Sổ tay lỗi sai" + Ôn lại Sổ tay công thức site/congthuc.html
└── Tối (19h30 - 21h30): Kiểm tra lại Máy tính Casio fx-580/880, in bảng tra Z, ngủ sớm giữ tinh thần minh mẫn
```

### Danh sách "Must-Do" (7 Bài Tự luận Bắt buộc Phải Giải Bằng Được)
1. **Bài `TL1_1` (OLS)**: Tính $b_1, b_0, r, R^2$, viết phương trình hồi quy mẫu $\hat{y} = b_0 + b_1 x$ và giải thích ý nghĩa kinh tế/kỹ thuật của $b_1$.
2. **Bài `TL2_3` (Bayes y tế / kiểm tra sản phẩm)**: Lập bảng hoặc sơ đồ cây, tính xác suất bệnh nhân thực sự mắc bệnh khi có kết quả dương tính $P(D \mid +)$.
3. **Bài `TL3_1` (Bảng phân phối pmf & cdf)**: Tìm hằng số $c$, tính $E(X), \operatorname{Var}(X), E(3X-5), \operatorname{Var}(2X+1)$.
4. **Bài `TL4_1` (Phân phối Nhị thức $B(n, p)$)**: Tính xác suất đúng $k$ lần, ít nhất 1 lần $1 - (1-p)^n$.
5. **Bài `TL4_3` (Phân phối Poisson)**: Tính xác suất cuộc gọi đến trong khoảng thời gian $t$, đổi tham số $\lambda' = \lambda \cdot t$.
6. **Bài `TL6_2` (Chuẩn hóa Z & Bài toán phân vị ngược)**: Cho $X \sim N(\mu, \sigma^2)$, tìm ngưỡng điểm $x_0$ để lọt vào top 5% sinh viên xuất sắc nhất ($z_{0.95} = 1.645$).
7. **Bài `TL7_7` (CLT Bóng đèn dự phòng - Signature UET Slide 90)**: Đặt $u = \sqrt{n}$, giải phương trình bậc hai $100u^2 - 49.35u - 2000 \ge 0 \implies n = 23$. Đây là bài phân loại 9 – 10 điểm của UET!

---

## 3. KẾ HOẠCH 2: LỘ TRÌNH CHUẨN 7 NGÀY (1 TUẦN - VỮNG VÀNG ĐIỂM A/A+)
> **Mục tiêu**: Đạt từ **8.5 đến 10.0 điểm**.  
> **Nguyên tắc**: *1 Ngày – 1 Chủ đề khép kín*. Áp dụng quy trình học 4 bước khép kín:
> 1. Đọc tóm tắt lý thuyết tại `site/hoc.html` (30 phút).
> 2. Giải trọn vẹn 8 bài tự luận tại `site/tuluan.html` (90 phút).
> 3. Luyện 22 – 25 câu trắc nghiệm tại `site/tracnghiem.html` ở Chế độ Luyện tập (45 phút).
> 4. Rà soát bẫy và ghi nhớ công thức tại `site/congthuc.html` (15 phút).

### Ma trận lộ trình 7 ngày

| Ngày | Chủ đề trọng tâm | Mục tiêu kiến thức cốt lõi | Tự luận trọng tâm | Số câu Trắc nghiệm |
|:---:|:---|:---|:---|:---:|
| **Ngày 1** | **Chủ đề 1: Thống kê mô tả & Hồi quy OLS** | Phân loại biến, tứ phân vị, ngoại lai $1.5 \times \text{IQR}$, hiệp phương sai, OLS $b_1 = r \frac{s_y}{s_x}$, biến chỉ báo Dummy | `TL1_1` đến `TL1_8` | 23 câu (`TN1_01` – `TN1_23`) |
| **Ngày 2** | **Chủ đề 2: Lý thuyết Xác suất & Bayes** | Tiên đề xác suất, De Morgan, công thức cộng/nhân, phân biệt độc lập vs xung khắc, Bayes, Base Rate Fallacy | `TL2_1` đến `TL2_8` | 23 câu (`TN2_01` – `TN2_23`) |
| **Ngày 3** | **Chủ đề 3: Biến ngẫu nhiên rời rạc, Kỳ vọng & Phương sai** | Hàm khối pmf, hàm tích lũy cdf, tính tuyến tính $E(aX+b)$, $\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$, $\operatorname{Var}(X \pm Y)$ khi độc lập, Bất đẳng thức Jensen | `TL3_1` đến `TL3_8` | 22 câu (`TN3_01` – `TN3_22`) |
| **Ngày 4** | **Chủ đề 4: Các phân phối xác suất rời rạc** | Bernoulli, Nhị thức $B(n, p)$, Siêu bội $HG(N, M, n)$, Poisson $Po(\lambda)$, quy tắc xấp xỉ Poisson ($n \ge 20, p \le 0.05$) | `TL4_1` đến `TL4_8` | 23 câu (`TN4_01` – `TN4_23`) |
| **Ngày 5** | **Chủ đề 5: Mô hình chiếc hộp, Chebyshev & Luật số lớn** | Box model, rút có/không hoàn lại, Square Root Law ($n\mu, \sigma\sqrt{n}$), BĐT Chebyshev $P(\|X-\mu\| \ge k\sigma) \le \frac{1}{k^2}$, WLLN | `TL5_1` đến `TL5_8` | 22 câu (`TN5_01` – `TN5_22`) |
| **Ngày 6** | **Chủ đề 6: Biến ngẫu nhiên liên tục & Phân phối Chuẩn** | Hàm mật độ $f(x)$, $P(X=c)=0$, Phân phối Đều $U(a,b)$, Phân phối Chuẩn $N(\mu, \sigma^2)$, Z-scores, Phân phối Mũ $Exp(\lambda)$ không nhớ | `TL6_1` đến `TL6_8` | 25 câu (`TN6_01` – `TN6_25`) |
| **Ngày 7** | **Chủ đề 7: Định lý giới hạn trung tâm (CLT) & Tổng ôn** | CLT cho tổng và trung bình mẫu, hiệu chỉnh liên tục $\pm 0.5$, bài toán tải trọng thang máy, bóng đèn dự phòng, cỡ mẫu khảo sát | `TL7_1` đến `TL7_8` | 23 câu (`TN7_01` – `TN7_23`) |

---

## 4. KẾ HOẠCH 3: LỘ TRÌNH NÂNG CAO 14 NGÀY (2 TUẦN - MASTERY 10/10)
> **Mục tiêu**: Thành thạo bản chất toán học, làm chủ mọi góc khuất bài thi, đạt điểm tối đa 10/10 và giành học bổng xuất sắc môn học.

### Phân kỳ chiến lược 14 ngày

```
[TUẦN 1: NỀN TẢNG TOÀN DIỆN & TỰ LUẬN ĐỈNH CAO]
├── Ngày 01 & 02: Hoàn thành Cụm A (Thống kê mô tả, Tidy data, Grammar of Graphics, OLS, Dummy)
├── Ngày 03 & 04: Hoàn thành Cụm B (Không gian mẫu, Tổ hợp, Xác suất điều kiện, Công thức Bayes nâng cao)
├── Ngày 05 & 06: Hoàn thành Cụm C (Biến rời rạc, Các phân phối thông dụng, Kỳ vọng điều kiện)
└── Ngày 07    : Rà soát nửa chặng đường -> Kiểm tra lại 28 bài tự luận đầu tiên

[TUẦN 2: ĐỊNH LÝ HỘI TỤ, PHÂN PHỐI LIÊN TỤC & TỔNG ÔN CHUYÊN SÂU]
├── Ngày 08 & 09: Cụm D (Mô hình chiếc hộp, BĐT Chebyshev, Luật số lớn WLLN, Cỡ mẫu Chebyshev)
├── Ngày 10 & 11: Cụm E (Hàm mật độ, Phân phối Chuẩn, Mũ, Chi-bình phương, t-Student, CLT)
├── Ngày 12     : Quét sạch 161 câu trắc nghiệm ở Chế độ Timed Exam (bấm giờ 40 câu/lần)
├── Ngày 13     : Thao luyện "Sổ tay lỗi sai" (Spaced Repetition: Làm lại tất cả các câu từng sai)
└── Ngày 14     : Mô phỏng thi thật 90 phút (Đề tổng hợp 25 câu TN + 4 câu TL) và nghỉ ngơi
```

---

## 5. CẨM NANG CHIẾN THUẬT PHÒNG THI GIỮA KỲ UET (EXAM STRATEGY)

### 5.1. Phân bổ thời gian 90 phút tối ưu

```
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                         TỔNG THỜI GIAN LÀM BÀI: 90 PHÚT                                  ║
╠══════════════════════════════════════════════════════════════════════════════════════════╣
║ 00' ────────────────── 40' ─────────────── 45' ────────────────────── 85' ──────── 90'   ║
║   [PHẦN TRẮC NGHIỆM]        [KIỂM TRA TN]         [PHẦN TỰ LUẬN]         [SOÁT TỔNG THỂ] ║
║      40 phút (25 câu)          5 phút             40 phút (3-4 bài)          5 phút       ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝
```

1. **Chiến thuật 3 lượt (Three-Pass Strategy) cho phần Trắc nghiệm (40 phút)**:
   - **Lượt 1 (Phút 0 – 20)**: Quét từ câu 1 đến câu cuối. Chỉ làm các câu lý thuyết định tính và bài tính toán cơ bản bấm máy ra ngay (< 1 phút/câu). Câu nào đọc thấy phức tạp hoặc chưa rõ hướng giải: **đánh dấu `?` và bỏ qua ngay lập tức**.
   - **Lượt 2 (Phút 20 – 35)**: Quay lại giải quyết các câu đánh dấu `?` (các bài toán cần vẽ bảng liên hợp, tính Bayes 2 bước, chuẩn hóa $Z$).
   - **Lượt 3 (Phút 35 – 40)**: Giải quyết các câu phân loại cao hoặc câu suy luận logic. Nếu hết thời gian, dùng phương pháp loại trừ distractor phi lý và chọn đáp án có xác suất đúng cao nhất. Tuyệt đối không để trống bất kỳ câu trắc nghiệm nào!
2. **Kiểm tra và tô phiếu trắc nghiệm (Phút 40 – 45)**:
   - Dành trọn vẹn 5 phút để so khớp đáp án nháp và tô đen dứt khoát trên phiếu trả lời trắc nghiệm, tránh lệch dòng hoặc tô mờ máy quét không nhận diện được.
3. **Chiến thuật giải phần Tự luận (Phút 45 – 85)**:
   - **Chọn bài dễ làm trước**: Thông thường bài Hồi quy OLS hoặc bài tính $E(X), \operatorname{Var}(X)$ từ bảng phân phối rời rạc là dạng dễ ăn trọn điểm nhất. Làm ngay bài này để tạo tâm lý tự tin và "bỏ túi" trước 1.5 – 2.0 điểm.
   - Tiếp theo làm bài Xác suất / Bayes và bài Phân phối Chuẩn / CLT.
   - Giữ bài tìm cỡ mẫu $n$ hoặc giải phương trình bậc hai CLT làm sau cùng.
4. **Soát tổng thể (Phút 85 – 90)**:
   - Kiểm tra đơn vị kết luận (USD, sản phẩm, giờ, người...).
   - Kiểm tra xem có để quên giá trị làm tròn ở bước trung gian hay không.

---

### 5.2. Tiêu chuẩn Trình bày Tự luận Ăn trọn Barem Điểm UET
Giảng viên chấm thi tự luận UET chấm theo barem từng 0.25 điểm. Để không bị trừ điểm oan, bài làm của bạn phải tuân thủ nghiêm ngặt 4 nguyên tắc vàng sau:

> [!IMPORTANT]
> **4 NGUYÊN TẮC VÀNG KHI TRÌNH BÀY BÀI THI TỰ LUẬN**
> 1. **Khai báo biến và biến cố rõ ràng ngay từ dòng đầu tiên**:
>    - Ví dụ: *"Gọi $A$ là biến cố sản phẩm lấy ra là phế phẩm", "Gọi $X$ là biến ngẫu nhiên chỉ...*.
>    - Tuyệt đối không nhảy vào viết ngay đẳng thức số mà không có chủ ngữ toán học.
> 2. **Luôn viết công thức chữ (Formula) trước khi thay số cụ thể**:
>    - Viết: $P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{0.12}{0.30} = 0.4000$.
>    - Nếu chỉ viết: $\frac{0.12}{0.30} = 0.4$, giám khảo có quyền trừ từ 0.25 đến 0.5 điểm vì thiếu căn cứ lý thuyết.
> 3. **Quy tắc làm tròn số**:
>    - Giá trị xác suất: Giữ ít nhất **4 chữ số thập phân** (ví dụ: $0.0436$, không làm tròn thô thành $0.04$).
>    - Giá trị $Z$-score: Giữ **2 chữ số thập phân** để khớp với bảng tra $\Phi(z)$ (ví dụ: $z = 1.64$ hoặc $1.65$).
>    - Trong các bước tính trung gian: Tuyệt đối không làm tròn sớm; lưu biến vào bộ nhớ máy tính (phím `STO` `A`, `B`, `C`) để tránh sai số lũy tiến.
> 4. **Câu kết luận gắn liền với thực tế và đơn vị bài toán**:
>    - *"Vậy xác suất để thang máy không bị quá tải là xấp xỉ 97.72%"*.

---

## 6. HƯỚNG DẪN BẤM MÁY TÍNH CẦM TAY (CASIO FX-580VNX & FX-880BTG)

Máy tính cầm tay là vũ khí tối thượng giúp bạn tiết kiệm 50% thời gian làm trắc nghiệm và kiểm tra chéo đáp án tự luận với độ tin cậy 100%.

### 6.1. Thống kê 1 biến (Tính Mean $\bar{x}$, Phương sai $s^2$, Độ lệch chuẩn $s$)
Dùng để kiểm tra nhanh các bài toán tóm tắt dữ liệu (Chủ đề 1 & Chủ đề 3).

* **Trên Casio fx-580VNX**:
  1. Bật cột tần số: `SHIFT` $\rightarrow$ `MENU` $\rightarrow$ bấm phím mũi tên xuống $\rightarrow$ chọn `3: Thống kê (Statistics)` $\rightarrow$ chọn `1: Mở (Frequency ON)`.
  2. Vào chế độ thống kê: `MENU` $\rightarrow$ `6: Thống kê` $\rightarrow$ chọn `1: 1-Biến (1-Variable)`.
  3. Nhập giá trị $x_i$ vào cột $X$, nhập tần số hoặc xác suất tương ứng vào cột `FREQ`.
  4. Bấm `AC` $\rightarrow$ bấm `OPTN` $\rightarrow$ chọn `3: Dữ liệu tính 1-biến (1-Variable Calc)`.
  5. Màn hình hiện toàn bộ:
     - $\bar{x}$: Trung bình mẫu (hoặc kỳ vọng $E(X)$ nếu nhập xác suất).
     - $\sigma_x$: Độ lệch chuẩn tổng thể.
     - $s_x$: Độ lệch chuẩn mẫu hiệu chỉnh (mẫu số $n-1$).
     - $\operatorname{Min}(x), Q_1, \operatorname{Med}, Q_3, \operatorname{Max}(x)$: 5 số tóm tắt của Boxplot!

* **Trên Casio fx-880BTG**:
  1. Bấm `HOME` $\rightarrow$ chọn biểu tượng `Thống kê (Statistics)` $\rightarrow$ bấm `OK`.
  2. Bấm phím `TOOLS` $\rightarrow$ mục `Tần số (Frequency)` $\rightarrow$ chọn `Bật (ON)`.
  3. Nhập dữ liệu vào 2 cột $x$ và `FREQ`.
  4. Bấm `AC` $\rightarrow$ bấm `OK` $\rightarrow$ chọn `Tính toán 1-biến`.

---

### 6.2. Hồi quy tuyến tính OLS (Tìm $b_0, b_1, r, R^2$)
Dùng cho bài toán Hồi quy tuyến tính (Chủ đề 1).

* **Trên Casio fx-580VNX**:
  1. `MENU` $\rightarrow$ `6: Thống kê` $\rightarrow$ chọn `2: $y = a + bx$`.
  2. Nhập các cặp $(x_i, y_i)$ vào 2 cột tương ứng.
  3. Bấm `AC` $\rightarrow$ bấm `OPTN` $\rightarrow$ chọn `4: Tính toán hồi quy (Regression Calc)`.
  4. Kết quả hiển thị:
     - $a$: Hệ số chặn ($b_0$).
     - $b$: Hệ số góc ($b_1$).
     - $r$: Hệ số tương quan Pearson. Muốn tìm $R^2$, chỉ cần lấy $r^2$.

---

### 6.3. Tính Phân phối Rời rạc (Nhị thức & Poisson)
Dùng cho bài toán kiểm tra xác suất tức thời (Chủ đề 4).

* **Trên Casio fx-580VNX**:
  - Vào chế độ phân phối: `MENU` $\rightarrow$ `7: Phân phối (Distribution)`.
  - **Phân phối Nhị thức**:
    - Tính tại đúng 1 điểm $P(X = k)$: Bấm mũi tên xuống $\rightarrow$ chọn `1: Binomial PD` $\rightarrow$ chọn `2: Biến (Variable)` $\rightarrow$ Nhập $x = k, N = n, p = p$.
    - Tính tích lũy $P(X \le k)$: Chọn `1: Binomial CD` $\rightarrow$ chọn `2: Biến` $\rightarrow$ Nhập $x = k, N = n, p = p$.
  - **Phân phối Poisson**:
    - Tính tại đúng 1 điểm $P(X = k)$: Chọn `2: Poisson PD` $\rightarrow$ chọn `2: Biến` $\rightarrow$ Nhập $x = k, \lambda = \lambda$.
    - Tính tích lũy $P(X \le k)$: Chọn `3: Poisson CD` $\rightarrow$ chọn `2: Biến` $\rightarrow$ Nhập $x = k, \lambda = \lambda$.

---

### 6.4. Tính Phân phối Chuẩn $N(\mu, \sigma^2)$ & Phân vị ngược
Dùng cho bài toán Chuẩn hóa và CLT (Chủ đề 6 & 7).

* **Trên Casio fx-580VNX**:
  - `MENU` $\rightarrow$ `7: Phân phối (Distribution)`.
  - **Tính xác suất $P(a \le X \le b)$**:
    - Chọn `2: Normal CD`.
    - Nhập `Lower` $= a$, `Upper` $= b$, $\sigma = \sigma$, $\mu = \mu$.
    - *Lưu ý*: Nếu tính $P(X \le b)$, nhập `Lower` $= -10^{99}$ (bấm `-1` `x10^x` `99`). Nếu tính $P(X \ge a)$, nhập `Upper` $= 10^{99}$.
  - **Tính phân vị ngược (Inverse Normal - Tìm $x$ khi biết diện tích bên trái)**:
    - Chọn `3: Inverse Normal`.
    - Nhập `Area` (Diện tích tích lũy bên trái, ví dụ top 5% xuất sắc nhất thì Area $= 0.95$).
    - Nhập $\sigma$ và $\mu$. Máy tính trả về chính xác giá trị $x_0$ cần tìm!

---

## 7. BẢNG KIỂM 10 BẪY ĐIỂM SỐ CHẾT NGƯỜI (TOP 10 EXAM PITFALLS)

Trước khi bước vào phòng thi, hãy rà soát kỹ bảng kiểm 10 bẫy phổ biến nhất đã khiến hàng nghìn sinh viên UET mất điểm oan uổng:

| STT | Tên bẫy thường gặp | Sai lầm phổ biến của sinh viên | Bản chất đúng cần nhớ | Cách phòng tránh tức thì |
|:---:|:---|:---|:---|:---|
| **1** | **Nhầm lẫn Độc lập và Xung khắc** | Cho rằng $A, B$ độc lập thì $P(A \cap B) = 0$. | • Xung khắc: $A \cap B = \emptyset \implies P(AB) = 0$.<br>• Độc lập: $P(AB) = P(A)P(B)$.<br>Nếu $P(A), P(B) > 0$, hai biến cố độc lập **không bao giờ** xung khắc! | Nhớ khẩu quyết: *"Độc lập nhân xác suất, Xung khắc rỗng giao nhau"*. |
| **2** | **Quên bình phương khi tính phương sai tổ hợp** | Viết $\operatorname{Var}(3X - 5) = 3\operatorname{Var}(X) - 5$. | $\operatorname{Var}(aX + b) = a^2 \operatorname{Var}(X)$. Hằng số cộng $b$ không làm thay đổi độ phân tán! Dấu trừ biến thành cộng bình phương: $(-3)^2 = 9$. | Nhẩm ngay: Phương sai có thứ nguyên bình phương, nên hệ số phải bình phương ($a^2$). |
| **3** | **Phương sai của hiệu 2 biến độc lập** | Viết $\operatorname{Var}(X - Y) = \operatorname{Var}(X) - \operatorname{Var}(Y)$. | Khi $X, Y$ độc lập: $\operatorname{Var}(X - Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)$. Độ không chắc chắn luôn cộng dồn, không triệt tiêu! | Bất kể tổng hay hiệu, phương sai của các biến độc lập luôn **cộng lại**. |
| **4** | **Quên trừ 1 ở mẫu số phương sai hiệu chỉnh** | Tính $s_x^2 = \frac{1}{n} \sum (x_i - \bar{x})^2$. | Phương sai mẫu hiệu chỉnh (sample variance) bắt buộc chia cho **bậc tự do $n-1$** để là ước lượng không chệch! | Nhìn ký hiệu trên máy Casio: lấy $s_x$, không lấy $\sigma_x$. |
| **5** | **Nhầm lẫn xác suất tại 1 điểm của biến liên tục** | Cho rằng biến liên tục $X$ có $P(X = c) = f(c) > 0$. | Đối với mọi biến ngẫu nhiên liên tục, xác suất tại đúng 1 điểm luôn bằng $0$: $P(X = c) = 0$. $f(c)$ chỉ là độ cao mật độ, không phải xác suất! | Muốn có xác suất phải lấy tích phân trên một khoảng có độ rộng $> 0$. |
| **6** | **Quên hiệu chỉnh liên tục $\pm 0.5$ khi xấp xỉ Chuẩn** | Xấp xỉ biến rời rạc $X$ sang chuẩn mà tính thẳng $P(X \ge 10) \approx P(Y \ge 10)$. | Vì $X$ là rời rạc có bước nhảy 1 đơn vị, cột 10 trải từ $9.5$ đến $10.5$. Do đó $P(X \ge 10) \approx P(Y \ge 9.5)$ (mở rộng vùng lấy tích phân). | Vẽ trục số rời rạc: lấy $\ge 10$ thì lùi nửa bước về $9.5$; lấy $> 10$ (tức $\ge 11$) thì lùi về $10.5$. |
| **7** | **Nhầm lẫn giữa Tổng $S_n$ và Trung bình $\bar{X}_n$ trong CLT** | Dùng độ lệch chuẩn $\sigma/\sqrt{n}$ cho bài toán tổng tải trọng thang máy $S_n$. | • Đối với Tổng $S_n$: Độ lệch chuẩn là $\sigma \sqrt{n}$.<br>• Đối với Trung bình $\bar{X}_n$: Độ lệch chuẩn là $\sigma / \sqrt{n}$. | Tải trọng 20 người trong thang máy phải phân tán lớn hơn 1 người, do đó phải nhân $\sqrt{n}$. |
| **8** | **Bẫy điều kiện xấp xỉ Poisson thay cho Nhị thức** | Dùng Poisson cho mọi bài toán có $n$ lớn. | Chỉ xấp xỉ $B(n, p) \approx Po(\lambda = np)$ khi biến cố hiếm: $n \ge 20$ (hoặc $100$) và $p \le 0.05$. Nếu $p \approx 0.5$, phải xấp xỉ bằng Phân phối Chuẩn $N(np, np(1-p))$! | Kiểm tra giá trị của $p$: $p$ rất bé $\implies$ Poisson; $p$ trung bình $\implies$ Chuẩn. |
| **9** | **Nhầm lẫn giữa hệ số chặn $b_0$ và hệ số góc $b_1$** | Viết phương trình OLS ngược thành $\hat{y} = b_1 + b_0 x$. | Tiêu chuẩn thống kê trong slide UET: $\hat{y} = b_0 + b_1 x$, trong đó $b_0$ là Intercept (hệ số chặn) và $b_1$ là Slope (hệ số góc). | Luôn gắn hệ số góc $b_1$ đi kèm với biến giải thích $x$. |
| **10** | **Quên bình phương khi giải phương trình bậc hai CLT** | Với bài toán bóng đèn dự phòng UET slide 90, đặt $u = \sqrt{n}$, giải ra $u \ge 4.76$ nhưng quên bình phương $n = u^2$. | Nghiệm của phương trình bậc hai chỉ mới là $u = \sqrt{n}$. Cỡ mẫu thực tế phải là $n = \lceil u^2 \rceil = \lceil 4.76^2 \rceil = \lceil 22.65 \rceil = 23$. | Luôn kiểm tra lại đơn vị và ý nghĩa nghiệm: $n$ phải là số nguyên dương linh kiện! |

---

## 8. LỜI KẾT & TÂM THẾ VÀO PHÒNG THI

Kỳ thi giữa kỳ môn Xác suất Thống kê `UET.MAT1052` không nhằm mục đích đánh đố bằng những mẹo mực cao siêu, mà kiểm tra tư duy mô hình hóa dữ liệu và tính chính xác, cẩn trọng của một kỹ sư tương lai. 

Khi đã nắm vững các bài toán mẫu trong `site/tuluan.html`, luyện tập phản xạ trên `site/tracnghiem.html`, và trang bị sổ tay công thức `site/congthuc.html`, bạn hoàn toàn có đủ năng lực và sự tự tin để chinh phục điểm 9 – 10.

**Chúc bạn ôn tập thông minh, giữ vững tâm lý và đạt kết quả xuất sắc nhất!**
