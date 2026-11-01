# BẢN ĐỒ BAO PHỦ NỘI DUNG (COVERAGE MAP)
## Môn học: UET.MAT1052 — Xác suất Thống kê (Giữa kỳ)
### Đối chiếu: Slide Giảng dạy UET (Week 01 – Week 07) ↔ Giáo trình Stat20 ↔ 5 Cụm Bài học Thiết kế (A – E)

---

## 1. TỔNG QUAN PHẠM VI ÔN TẬP GIỮA KỲ

Theo thông báo tại slide cuối của **Tuần 07 (trang 94)**:
> *"Buổi 8: kiểm tra giữa kỳ và giải đáp câu hỏi về đề thi.*
> *Nội dung cần ôn: dữ liệu, thống kê mô tả, xác suất và biến ngẫu nhiên; cách nhận diện mô hình, tính xác suất, kỳ vọng, phương sai, độ lệch chuẩn."*

Bộ tài liệu tự học tương tác được tổ chức thành **5 Cụm kiến thức chuẩn hóa (A, B, C, D, E)** bao phủ 100% nội dung từ Week 01 đến hết Week 07, bảo đảm người học từ con số 0 (hoặc mất gốc từ mục 2.4) có thể nắm trọn vẹn cả **Nửa Trắc Nghiệm** và **Nửa Tự Luận**.

---

## 2. MA TRẬN ĐỐI CHIẾU CHI TIẾT (STAT20 ↔ SLIDE UET ↔ CỤM BÀI HỌC)

| STT | Cụm bài học | Mã bài đề xuất | Tên bài học chi tiết | Slide UET tương ứng | Mục Stat20 tương ứng | Ghi chú & Nguồn độc quyền |
|:---:|:---:|:---:|:---|:---|:---|:---|
| **I** | **CỤM A: DỮ LIỆU & THỐNG KÊ MÔ TẢ** | **A1** | Khung dữ liệu & Phân loại biến (Định danh, Thứ bậc, Rời rạc, Liên tục) | `week01.pdf` (tr. 1–75) | Mục 1.1, 1.2, 1.3 | Cả 2 nguồn đều có. Stat20 nhấn mạnh Data frame. |
| | | **A2** | Tóm tắt biến phân loại: Tần số, Tỉ lệ, Bảng liên hợp 2 chiều | `week02.pdf` (tr. 1–35) | Mục 2.2 | Cả 2 nguồn đều có. Quan trọng: chọn đúng mẫu số (tổng hàng, tổng cột, tổng chung). |
| | | **A3** | Tóm tắt biến số: Tâm (Mean, Median), Phân tán (SD, IQR, Range), Hình dạng phân phối | `week02.pdf` (tr. 36–114) | Mục 2.4 | UET slide nhấn mạnh tiêu chuẩn xác định ngoại lai $1.5 \times \text{IQR}$. |
| | | **A4** | Ngữ pháp đồ họa & Trực quan hóa dữ liệu (Histogram, Boxplot, Scatter plot) | `week03_plotnine.pdf` (tr. 1–94) | Mục 2.6, 2.7 | Stat20 dùng `ggplot2` (R); Slide UET dùng `plotnine` (Python). |
| | | **A5** | Tương quan tuyến tính (Hệ số Pearson $r$) & Nhận định quan hệ | `week04.pdf` (tr. 1–40) | Mục 2.10 | Công thức $r \in [-1, 1]$, tính chất bất biến tỉ lệ, lưu ý tương quan $\neq$ nhân quả. |
| | | **A6** | Hồi quy tuyến tính đơn (OLS): Đường hồi quy $\hat{y} = b_0 + b_1 x$, Phần dư $e = y - \hat{y}$ | `week04.pdf` (tr. 41–75) | Mục 2.10, 7.2 | Phương pháp bình phương tối thiểu, ý nghĩa hệ số góc $b_1$, hệ số chặn $b_0$. |
| | | **A7** | Hồi quy tuyến tính bội cơ bản: Biến chỉ báo (Dummy variable) & Mức tham chiếu | `week04.pdf` (tr. 76–99) | Mục 2.12 | Cách đọc hệ số khi có biến phân loại (so với baseline). |
| **II** | **CỤM B: LÝ THUYẾT XÁC SUẤT** | **B1** | Không gian mẫu $\Omega$, Biến cố, 3 Tiên đề xác suất Kolmogorov | `week05.pdf` (tr. 1–30) | Mục 3.1 | Slide UET kết hợp giáo trình OpenIntro Statistics Ch.3. |
| | | **B2** | Quy tắc cộng, Biến cố đối, Nguyên lý bao hàm – loại trừ | `week05.pdf` (tr. 31–50) | Mục 3.1, 3.3.9 | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$; phân biệt xung khắc vs đối lập. |
| | | **B3** | Xác suất có điều kiện $P(A\|B)$ & Quy tắc nhân | `week05.pdf` (tr. 51–68) | Mục 3.3.3, 3.3.4 | Liên hệ mật thiết với bảng liên hợp ở Cụm A. |
| | | **B4** | Tính độc lập của biến cố vs Tính xung khắc | `week05.pdf` (tr. 69–80) | Mục 3.3.5, 3.3.8 | Sai lầm chí mạng: nhầm lẫn giữa độc lập ($P(AB)=P(A)P(B)$) và xung khắc ($AB=\emptyset$). |
| | | **B5** | Giải tích kết hợp & Quy tắc đếm (Nhân, Hoán vị, Chỉnh hợp, Tổ hợp $C_n^k$) | `week05.pdf` (tr. 81–93) | Mục 3.4.2 | Nền tảng để xây dựng phân phối nhị thức và siêu bội. |
| **III** | **CỤM C: BIẾN NGẪU NHIÊN RỜI RẠC** | **C1** | Biến ngẫu nhiên rời rạc, Hàm khối xác suất (pmf) $p_X(x)$ & Hàm tích lũy (cdf) $F(x)$ | `week06.pdf` (tr. 1–35) | Mục 4.1, 4.2, 4.3.1, 4.4 | Bảng phân phối xác suất, điều kiện $\sum p(x) = 1$, tính chất bậc thang của $F(x)$. |
| | | **C2** | Phân phối Bernoulli & Phân phối Nhị thức $B(n, p)$ | `week06.pdf` (tr. 36–52) | Mục 4.3.2.2, 4.3.2.3 | Lấy mẫu có hoàn lại, điều kiện các phép thử độc lập Bernoulli. |
| | | **C3** | Phân phối Siêu bội $HG(N, M, n)$ | `week06.pdf` (tr. 53–65) | Mục 4.3.2.4 | Lấy mẫu KHÔNG hoàn lại từ tổng thể hữu hạn $N$. |
| | | **C4** | Phân phối Poisson $(\lambda)$ & Nhận diện mô hình rời rạc | `week06.pdf` (tr. 66–80) | Mục 4.3.2.5, 4.3.2.6 | Biến cố hiếm trong khoảng liên tục, so sánh 3 mô hình chọn lựa. |
| | | **C5** | Kỳ vọng $E(X)$: Định nghĩa, Ý nghĩa tâm khối lượng & Kỳ vọng của hàm $E(g(X))$ | `week07.pdf` (tr. 4–13) | Mục 4.7, 4.8 | Tính chất tuyến tính $E(aX+b) = aE(X)+b$, $E(X+Y) = E(X)+E(Y)$. |
| | | **C6** | Phương sai $\operatorname{Var}(X)$ & Độ lệch chuẩn $\operatorname{SD}(X)$ | `week07.pdf` (tr. 14–20) | Mục 4.10 | Công thức rút gọn $E(X^2) - [E(X)]^2$, $\operatorname{Var}(aX+b) = a^2\operatorname{Var}(X)$, bảo toàn thứ nguyên đơn vị. |
| **IV** | **CỤM D: TỔNG, TRUNG BÌNH & ĐỊNH LÝ HỘI TỤ** | **D1** | Biến ngẫu nhiên độc lập cùng phân phối (i.i.d.) & Mô hình chiếc hộp (Box Model) | `week07.pdf` (tr. 21–24) | Mục 4.13 | Rút thăm có hoàn lại từ hộp vé, mô hình hóa phép thử phức hợp. |
| | | **D2** | Kỳ vọng & Độ lệch chuẩn của Tổng $S_n$ và Trung bình mẫu $\bar{X}_n$ | `week07.pdf` (tr. 25–32) | Mục 4.14 | Quy tắc $\sigma\sqrt{n}$ và $\sigma/\sqrt{n}$, quy tắc căn bậc hai (Square Root Law). |
| | | **D3** | Bất đẳng thức Chebyshev & Cận trên xác suất sai lệch | `week07.pdf` (tr. 33–37) | **CHỈ CÓ TRONG SLIDE** | $P(\|X - \mu\| \ge k\sigma) \le 1/k^2$; đánh giá không phụ thuộc dạng phân phối. |
| | | **D4** | Luật số lớn yếu (WLLN): Bản chất toán học & Ứng dụng thực tế | `week07.pdf` (tr. 38–40) | **CHỈ CÓ TRONG SLIDE** | Chứng minh hội tụ xác suất từ Chebyshev; ý nghĩa đối với bảo hiểm và sòng bạc. |
| **V** | **CỤM E: BIẾN LIÊN TỤC & ĐỊNH LÝ GIỚI HẠN TRUNG TÂM (CLT)** | **E1** | Biến ngẫu nhiên liên tục: Hàm mật độ xác suất (pdf) $f(x)$ & Hàm tích lũy (cdf) $F(x)$ | `week07.pdf` (tr. 41–47) | Mục 4.15 | Xác suất tại 1 điểm bằng 0 ($P(X=c)=0$), diện tích tích phân, liên hệ $f(x) = F'(x)$. |
| | | **E2** | Kỳ vọng & Phương sai của biến liên tục | `week07.pdf` (tr. 48–49) | Mục 4.15 | Tích phân $\int x f(x) dx$ và $\int x^2 f(x) dx - [E(X)]^2$. |
| | | **E3** | Phân phối Đều $U(a, b)$ | `week07.pdf` (tr. 50–53) | Mục 4.16.1 | Mật độ hằng số $1/(b-a)$, $E = (a+b)/2$, $\operatorname{Var} = (b-a)^2/12$. |
| | | **E4** | Phân phối Chuẩn $N(\mu, \sigma^2)$: Chuẩn hóa $Z$, Quy tắc 68–95–99.7 & Tra bảng $\Phi(z)$ | `week07.pdf` (tr. 54–62) | Mục 4.16.2 | Quy tắc thực nghiệm 1-2-3 SD, tính phân vị $q_p$, đối xứng hình chuông Gauss. |
| | | **E5** | Các phân phối liên tục bổ sung: Mũ $Exp(\lambda)$, Chi-bình phương $\chi^2$, $t$-Student | `week07.pdf` (tr. 63–67) | **CHỈ CÓ TRONG SLIDE** | Mũ: tính không nhớ, $E=1/\lambda, \operatorname{Var}=1/\lambda^2$; $\chi^2$ và $t$: nhận diện định tính. |
| | | **E6** | Định lý giới hạn trung tâm (CLT): Phát biểu, Điều kiện & Ứng dụng tính xác suất mẫu lớn | `week07.pdf` (tr. 68–77, 84–91) | Mục 4.17 | Xấp xỉ $S_n \sim N(n\mu, n\sigma^2)$ và $\bar{X}_n \sim N(\mu, \sigma^2/n)$; bài toán tìm cỡ mẫu $n$. |

---

## 3. BẢNG PHÂN LOẠI CÁC DẠNG BÀI TẬP VÀ MÔ HÌNH TOÁN HỌC

| Cụm | Dạng bài tập trọng tâm | Bản chất công thức / Thuật toán giải | Nguồn xuất hiện trong đề/slide | Mức độ thi |
|:---:|:---|:---|:---|:---:|
| **A** | 1. Xác định loại biến từ bài toán thực tế | Kiểm tra bản chất biến: định danh, thứ bậc, rời rạc, liên tục; bẫy mã số | Week 01, Stat20 Ch.1 | Trắc nghiệm |
| **A** | 2. Tính tỉ lệ từ bảng liên hợp 2 chiều | Xác định mẫu số theo từ khóa: "trong số...", "biết rằng..." | Week 02, Stat20 2.2 | Trắc nghiệm & Tự luận ngắn |
| **A** | 3. Tính bộ 5 số tóm tắt (Five-number summary), IQR, xác định ngoại lai | $\text{IQR} = Q_3 - Q_1$; Cận dưới: $Q_1 - 1.5\text{IQR}$, Cận trên: $Q_3 + 1.5\text{IQR}$ | Week 02 (tr. 70-85), Stat20 2.4 | Tự luận & Trắc nghiệm |
| **A** | 4. Phân tích hình dạng phân phối (Skewness) | So sánh Mean vs Median: Lệch phải ($\text{Mean} > \text{Median}$), Lệch trái ($\text{Mean} < \text{Median}$) | Week 02, Stat20 2.4 | Trắc nghiệm |
| **A** | 5. Tính và diễn giải hệ số hồi quy, phần dư | Đường hồi quy $\hat{y} = b_0 + b_1 x$; Phần dư $e_i = y_i - \hat{y}_i$; Ý nghĩa hệ số góc | Week 04, Stat20 2.10, 7.2 | Tự luận & Trắc nghiệm |
| **B** | 6. Tính xác suất bằng quy tắc cộng & Biến cố đối | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$; $P(A) = 1 - P(A^c)$ | Week 05, Stat20 Ch.3 | Trắc nghiệm |
| **B** | 7. Xác suất có điều kiện & Quy tắc nhân | $P(A\|B) = \frac{P(A \cap B)}{P(B)}$; $P(A \cap B) = P(B)P(A\|B)$ | Week 05, Stat20 Ch.3 | Tự luận & Trắc nghiệm |
| **B** | 8. Kiểm tra tính độc lập của hai biến cố | Kiểm tra đẳng thức: $P(A \cap B) \stackrel{?}{=} P(A) \cdot P(B)$ | Week 05, Stat20 Ch.3 | Trắc nghiệm |
| **B** | 9. Bài toán đếm & Xác suất cổ điển | Sử dụng tổ hợp $C_n^k$, chỉnh hợp $A_n^k$, quy tắc nhân số cách chọn | Week 05, Stat20 Ch.3 | Tự luận |
| **C** | 10. Lập bảng phân phối xác suất rời rạc (pmf), tìm tham số chưa biết | Điều kiện chuẩn hóa $\sum p(x) = 1$; Tính $F(x) = P(X \le x)$ | Week 06, Week 07 Bài 1 | Tự luận |
| **C** | 11. Nhận diện và tính xác suất mô hình rời rạc (Bernoulli, Nhị thức, Siêu bội, Poisson) | Nhị thức: có hoàn lại $C_n^k p^k (1-p)^{n-k}$; Siêu bội: không hoàn lại $\frac{C_M^k C_{N-M}^{n-k}}{C_N^n}$; Poisson: hiếm $\frac{\lambda^k e^{-\lambda}}{k!}$ | Week 06, Stat20 Ch.4 | Tự luận & Trắc nghiệm |
| **C** | 12. Tính kỳ vọng $E(X)$, $E(X^2)$, phương sai $\operatorname{Var}(X)$, $\operatorname{SD}(X)$ rời rạc | $E(X) = \sum x p(x)$; $\operatorname{Var}(X) = E(X^2) - [E(X)]^2$; $\operatorname{SD} = \sqrt{\operatorname{Var}}$ | Week 07 (tr. 5-20, Bài tập 1) | Tự luận bắt buộc |
| **C** | 13. Tính kỳ vọng và phương sai của biến đổi tuyến tính | $E(aX + b) = aE(X) + b$; $\operatorname{Var}(aX + b) = a^2\operatorname{Var}(X)$; $\operatorname{SD}(aX + b) = \|a\|\operatorname{SD}(X)$ | Week 07 (tr. 7, 17, 18) | Trắc nghiệm & Tự luận |
| **D** | 14. Tổng và trung bình của mẫu i.i.d. (Mô hình chiếc hộp) | $E(S_n) = n\mu, \operatorname{SD}(S_n) = \sigma\sqrt{n}$; $E(\bar{X}_n) = \mu, \operatorname{SD}(\bar{X}_n) = \sigma/\sqrt{n}$ | Week 07 (tr. 21-32) | Tự luận & Trắc nghiệm |
| **D** | 15. Áp dụng bất đẳng thức Chebyshev đánh giá cận xác suất | $P(\|X - \mu\| \ge k\sigma) \le 1/k^2$; $P(\|X - \mu\| < k\sigma) \ge 1 - 1/k^2$ | Week 07 (tr. 33-40) | Tự luận & Trắc nghiệm |
| **D** | 16. Bài toán suy giảm sai số trung bình mẫu (Quy tắc căn bậc hai) | Muốn $\operatorname{SD}(\bar{X})$ giảm $m$ lần thì $n$ phải tăng $m^2$ lần | Week 07 (tr. 26) | Trắc nghiệm |
| **E** | 17. Xác định tham số của hàm mật độ/tích lũy liên tục | Điều kiện liên tục tại biên $F(b) = 1$ hoặc $\int f(x) dx = 1$ | Week 07 (tr. 42, 82 - Bài tập 2) | Tự luận |
| **E** | 18. Tính xác suất, kỳ vọng, phương sai của biến liên tục | $P(a \le X \le b) = \int_a^b f(x)dx$; $E(X) = \int x f(x)dx$ | Week 07 (tr. 44, 48 - Bài tập 2) | Tự luận |
| **E** | 19. Bài toán phân phối Đều $U(a, b)$ | Xác suất theo tỉ lệ chiều dài đoạn: $P(c \le X \le d) = \frac{d - c}{b - a}$ | Week 07 (tr. 51-53) | Trắc nghiệm & Tự luận |
| **E** | 20. Chuẩn hóa & Tính xác suất phân phối Chuẩn | $Z = \frac{X - \mu}{\sigma}$; Tra bảng $\Phi(z)$; Quy tắc 68–95–99.7 | Week 07 (tr. 54-62) | Tự luận & Trắc nghiệm |
| **E** | 21. Bài toán phân vị phân phối Chuẩn (Bài toán ngược) | Cho $P(X \le x_p) = p$, tìm $Z_p = \Phi^{-1}(p) \implies x_p = \mu + Z_p \sigma$ | Week 07 (tr. 60-62) | Tự luận & Trắc nghiệm |
| **E** | 22. Tính xác suất với phân phối Mũ $Exp(\lambda)$ | $P(X > x) = e^{-\lambda x}$; $P(a < X < b) = e^{-\lambda a} - e^{-\lambda b}$; $\mu = 1/\lambda$ | Week 07 (tr. 63-65, 86 - Bài tập 4) | Tự luận & Trắc nghiệm |
| **E** | 23. Áp dụng Định lý giới hạn trung tâm (CLT) tính xác suất tổng và trung bình | $S_n \approx N(n\mu, n\sigma^2) \implies Z = \frac{S_n - n\mu}{\sigma\sqrt{n}}$; $\bar{X}_n \approx N(\mu, \frac{\sigma^2}{n}) \implies Z = \frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}}$ | Week 07 (tr. 68-77, 84, 86) | Tự luận trọng tâm |
| **E** | 24. Bài toán tìm cỡ mẫu $n$ đạt độ tin cậy bằng CLT | Thiết lập bất phương trình $\frac{a \cdot n - c}{b\sqrt{n}} \ge z_\alpha$; Đặt $u = \sqrt{n}$, giải tam thức bậc 2 | Week 07 (tr. 89-91 - Bài tập 5) | Tự luận phân loại cao |

---

## 4. PHÂN TÍCH SO SÁNH: SỰ KHÁC BIỆT GIỮA HAI TÀI LIỆU NGUỒN

### 4.1. Nội dung CHỈ CÓ trong Slide UET (Không có trong giáo trình Stat20)
1. **Bất đẳng thức Chebyshev & Luật số lớn yếu (WLLN):**
   - Slide Week 07 dành trọn Phần 3 (trang 33–40) cho Bất đẳng thức Chebyshev ($P(|X - \mu| \ge k\sigma) \le 1/k^2$), mở đầu với BĐT Markov, và dẫn xuất định lý Luật số lớn yếu ($\lim_{n \to \infty} P(|\bar{X}_n - \mu| \ge \epsilon) = 0$).
   - Trong Stat20 hoàn toàn không xuất hiện từ khóa Chebyshev hay WLLN.
2. **Các phân phối liên tục mở rộng:**
   - **Phân phối Mũ ($Exp(\lambda)$):** Slide Week 07 giới thiệu chi tiết định nghĩa, hàm mật độ, hàm phân phối, kỳ vọng $1/\lambda$, phương sai $1/\lambda^2$, tính chất không nhớ, và có hẳn **Bài tập vận dụng số 4 (trang 86–88)** tính xác suất bằng CLT trên nền phân phối mũ. Stat20 chỉ tập trung vào phân phối Đều và Chuẩn.
   - **Phân phối $\chi^2$ (Chi-bình phương) & $t$-Student:** Slide Week 07 trang 66–67 giới thiệu định nghĩa hàm mật độ, bậc tự do $\nu$ và hình dáng đồ thị.
3. **Bài toán thực tế đặc thù của đề thi UET:**
   - Bài toán tải trọng thang máy (Tổng các biến chuẩn, Slide tr. 84).
   - Bài toán tìm số lượng linh kiện dự phòng $n$ bằng ẩn phụ $u = \sqrt{n}$ giải tam thức bậc hai (Slide tr. 89–91).

### 4.2. Nội dung CHỈ CÓ trong Giáo trình Stat20 (Không có hoặc lướt nhanh trong Slide UET)
1. **Ngữ cảnh tình huống và nghiên cứu thực tế sâu:**
   - Các vụ án và nghịch lý lịch sử: Vụ án Sally Clark (sai lầm do nhân xác suất khi không độc lập), Nghịch lý De Méré (xúc xắc cổ điển), Roulette tại Las Vegas.
2. **Kỹ thuật thống kê tính toán chuyên sâu (R code):**
   - Hướng dẫn chi tiết cú pháp R: `sample()`, `set.seed()`, `mutate()`, `filter()`, `lm()`, `resid()`, `pnorm()`, `dbinom()`.

### 4.3. Khác biệt về Ký hiệu và Công cụ Tính toán

| Hạng mục | Giáo trình Stat20 (Berkeley) | Slide Giảng dạy UET (MAT1052) | Chuẩn hóa trong Bộ Học liệu Tương tác |
|:---|:---|:---|:---|
| **Ngôn ngữ thực hành** | Ngôn ngữ R (`tidyverse`, `ggplot2`) | Ngôn ngữ Python (`numpy`, `scipy.stats`, `plotnine`) | **Cung cấp song song cả hai** (ưu tiên Python/Scipy bám sát đề thi UET, bổ sung đối chiếu R) |
| **Ký hiệu Hàm khối xác suất** | $P(X = x)$ hoặc $f(x)$ | $p_X(x)$ hoặc $P(X = x)$ | Dùng $p_X(x) = P(X = x)$ và chú thích rõ cả hai cách viết |
| **Ký hiệu Phân phối Chuẩn** | $\mathcal{N}(\mu, \sigma^2)$ | $\mathcal{N}(\mu, \sigma^2)$ | Thống nhất $\mathcal{N}(\mu, \sigma^2)$ |
| **Ký hiệu Hàm tích lũy Chuẩn tắc** | Thường gọi $P(Z \le z)$ hoặc `pnorm(z)` | Ký hiệu chuẩn giải tích $\Phi(z)$ | Thống nhất dùng ký hiệu quốc tế $\Phi(z)$ kèm bảng tra số liệu |
| **Tham số Phân phối Mũ** | $\lambda$ (rate parameter) | $\lambda > 0$, $E(X) = 1/\lambda$ | Thống nhất định nghĩa tham số tốc độ $\lambda$ với $E(X) = 1/\lambda$ (tránh nhầm với scale $\beta = 1/\lambda$) |
| **Dấu phân cách thập phân** | Dấu chấm kiểu Anh/Mỹ (`0.5`, `3.14`) | Slide dùng dấu chấm (`0.05`, `6.45`) | **Dùng dấu phẩy thập phân kiểu Việt** (`0,5`, `6,45`) trong lời giải tự luận theo quy chuẩn, code hiển thị dấu chấm |
| **Độ lệch chuẩn** | Thường viết tắt SD hoặc $\sigma$ | Ký hiệu rõ $\operatorname{SD}(X)$ hoặc $\sigma$ | Thống nhất $\operatorname{Var}(X)$ cho phương sai, $\operatorname{SD}(X)$ cho độ lệch chuẩn |

---

## 5. KẾT LUẬN & ĐỊNH HƯỚNG TRIỂN KHAI CHO CÁC PHASE TIẾP THEO

- **Trọng tâm tuyệt đối:** Mọi khái niệm, định lý, công thức và ví dụ giải mẫu từ Cụm A đến Cụm E đều bám chắc Slide UET Week 01–07, giải thích cặn kẽ bản chất theo cách diễn giải trực quan, dễ hiểu của Stat20.
- **Đánh dấu rõ ràng:** Các phần "Mở rộng / Có thể xuất hiện trong đề" (Chebyshev, WLLN, Mũ, $\chi^2$, $t$-Student) được dán nhãn phân loại minh bạch, bảo đảm học sinh không bị quá tải nhưng tuyệt đối không mất điểm nếu đề thi mở rộng.
- **Kiểm chứng 100% bằng code:** Toàn bộ đáp số tính toán trong ví dụ mẫu và bài tập đều được kiểm nghiệm qua script Python/R chạy thật.
