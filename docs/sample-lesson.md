# BÀI GIẢNG MẪU HOÀN CHỈNH (PHASE 1)
## Chuyên đề: Kỳ vọng, Phương sai và Biến đổi tuyến tính của Biến ngẫu nhiên rời rạc
### Mã bài: Lesson C5-C6 | Vị trí: Cụm C | Nguồn: Slide Week 07 (tr. 4–20, 79–81) & Stat20 (Mục 4.7, 4.8, 4.10)

---

## 🎯 MỤC TIÊU BÀI HỌC
Sau khi hoàn thành bài này, bạn sẽ:
1. Hiểu bản chất thực tế của Kỳ vọng (tâm cân bằng dài hạn) và Phương sai/Độ lệch chuẩn (độ rung lắc, rủi ro quanh tâm).
2. Tính toán thành thạo $E(X)$, $E(X^2)$, $\operatorname{Var}(X)$, $\operatorname{SD}(X)$ từ bảng phân phối xác suất bằng cả 2 cách (định nghĩa và công thức rút gọn).
3. Không bao giờ bị lừa bởi công thức biến đổi tuyến tính $aX + b$.
4. Trình bày bài tự luận ăn trọn điểm barem của giảng viên UET (đúng thứ nguyên đơn vị, đủ 4 bước lập luận).

---

## 💡 (a) TRỰC GIÁC BẰNG LỜI (INTUITION)

### 1. Kỳ vọng $E(X)$ là gì?
- **Hình dung đời thường**: Hãy tưởng tượng một chiếc bập bênh hoặc một chiếc thước kẻ đặt trên một điểm tựa. Trên thước, bạn đặt các quả cân ở các vị trí giá trị $x$ với độ nặng tương ứng là xác suất $p(x)$. **Kỳ vọng $E(X)$ chính là "điểm tựa hoàn hảo" (tâm khối lượng)** giữ cho chiếc thước nằm cân bằng tuyệt đối.
- **Trong dài hạn**: Nếu bạn lặp lại phép thử này hàng triệu lần và tính trung bình cộng tất cả các kết quả nhận được, con số trung bình cộng đó sẽ tiến sát về $E(X)$.
- **Cảnh báo**: Kỳ vọng **không nhất thiết** phải là một giá trị mà biến ngẫu nhiên có thể nhận được! (Ví dụ: số con trung bình của một gia đình là 2,3 con; tung xúc xắc có kỳ vọng 3,5 chấm — không có mặt nào là 3,5 chấm cả).

### 2. Vì sao cần Phương sai $\operatorname{Var}(X)$ và Độ lệch chuẩn $\operatorname{SD}(X)$?
- Hãy so sánh hai trò chơi may rủi:
  - *Trò A*: Tung đồng xu, ngửa nhận 100 nghìn, sấp nhận 100 nghìn $\implies$ Kỳ vọng = 100 nghìn. (Rủi ro bằng 0).
  - *Trò B*: Tung đồng xu, ngửa nhận 200 nghìn, sấp mất trắng (0 đồng) $\implies$ Kỳ vọng = 100 nghìn. (Rủi ro cực cao).
- Cả hai trò chơi đều có kỳ vọng giống hệt nhau là 100 nghìn! Nếu chỉ nhìn vào kỳ vọng, bạn không thể thấy được mức độ rủi ro.
- **Phương sai và Độ lệch chuẩn sinh ra để đo "độ rung lắc / mức độ phân tán"** của các kết quả xung quanh tâm kỳ vọng. Giá trị càng lớn, kết quả càng phân tán mạnh và rủi ro càng cao.
- **Vì sao phải bình phương sai số $(X - \mu)^2$?** Vì nếu chỉ lấy $(X - \mu)$ rồi nhân xác suất, các độ lệch âm (bên trái tâm) và độ lệch dương (bên phải tâm) sẽ tự triệt tiêu lẫn nhau ra đúng bằng 0! Việc bình phương giúp biến mọi khoảng cách thành số dương. Sau đó, ta lấy căn bậc hai $\sqrt{\operatorname{Var}}$ để đưa độ lệch chuẩn quay về **cùng đơn vị đo** với biến gốc.

---

## 📐 (b) ĐỊNH NGHĨA & CÔNG THỨC TOÁN HỌC CHUẨN XÁC

Cho biến ngẫu nhiên rời rạc $X$ có hàm khối xác suất $p_X(x) = P(X = x)$. Đặt $\mu = E(X)$.

### 1. Kỳ vọng toán học (Expected Value)
$$E(X) = \sum_{x} x \cdot p_X(x)$$

- **Kỳ vọng của hàm $g(X)$ (Luật thống kê vô thức - LOTUS)**:
$$E[g(X)] = \sum_{x} g(x) \cdot p_X(x)$$
*(Đặc biệt: $E(X^2) = \sum x^2 \cdot p_X(x)$)*

- **Tính chất tuyến tính**: Với mọi hằng số $a, b$:
$$E(aX + b) = a \cdot E(X) + b$$
$$E(X + Y) = E(X) + E(Y) \quad \text{(luôn đúng, kể cả khi } X, Y \text{ không độc lập)}$$

### 2. Phương sai (Variance) & Độ lệch chuẩn (Standard Deviation)
- **Định nghĩa gốc của phương sai**:
$$\operatorname{Var}(X) = E\left[(X - \mu)^2\right] = \sum_{x} (x - \mu)^2 \cdot p_X(x)$$

- **Công thức rút gọn (dùng để tính toán thực tế)**:
$$\operatorname{Var}(X) = E(X^2) - [E(X)]^2$$

- **Độ lệch chuẩn**:
$$\operatorname{SD}(X) = \sqrt{\operatorname{Var}(X)}$$

- **Tính chất biến đổi tuyến tính**: Với mọi hằng số $a, b$:
$$\operatorname{Var}(aX + b) = a^2 \cdot \operatorname{Var}(X)$$
$$\operatorname{SD}(aX + b) = |a| \cdot \operatorname{SD}(X)$$
*(Hằng số $+b$ chỉ làm dịch chuyển đồ thị sang phải/trái, không làm thay đổi độ phân tán nên hoàn toàn biến mất khỏi công thức phương sai!)*

---

## 📝 (c) VÍ DỤ GIẢI MẪU TỪNG BƯỚC (STEP-BY-STEP)

> [!NOTE]
> **Bài toán thực tế (Slide Week 07, trang 79–81 — Bài tập 1):**
> Dung lượng của một chiếc USB được khách hàng mua tại một cửa hàng công nghệ là biến ngẫu nhiên rời rạc $X$ (đơn vị: GB). Bảng phân phối xác suất như sau:
> 
> | Dung lượng $x$ (GB) | 1 | 2 | 4 | 8 | 16 |
> |:---|:---:|:---:|:---:|:---:|:---:|
> | **Xác suất $p_X(x)$** | 0,05 | 0,10 | 0,35 | 0,40 | 0,10 |
> 
> 1. Tính kỳ vọng $E(X)$ và $E(X^2)$.
> 2. Tính phương sai $\operatorname{Var}(X)$ trực tiếp từ định nghĩa.
> 3. Kiểm tra lại bằng công thức rút gọn $\operatorname{Var}(X) = E(X^2) - [E(X)]^2$.
> 4. Tính độ lệch chuẩn $\operatorname{SD}(X)$ và ghi đúng đơn vị đo.

### Lời giải chi tiết:

#### Ý 1: Tính $E(X)$ và $E(X^2)$
- **Bước 1**: Áp dụng công thức kỳ vọng $E(X) = \sum x \cdot p_X(x)$:
  $$E(X) = 1(0{,}05) + 2(0{,}10) + 4(0{,}35) + 8(0{,}40) + 16(0{,}10)$$
  $$E(X) = 0{,}05 + 0{,}20 + 1{,}40 + 3{,}20 + 1{,}60 = 6{,}45\text{ GB}$$
  
- **Bước 2**: Áp dụng công thức $E(X^2) = \sum x^2 \cdot p_X(x)$:
  $$E(X^2) = 1^2(0{,}05) + 2^2(0{,}10) + 4^2(0{,}35) + 8^2(0{,}40) + 16^2(0{,}10)$$
  $$E(X^2) = 1(0{,}05) + 4(0{,}10) + 16(0{,}35) + 64(0{,}40) + 256(0{,}10)$$
  $$E(X^2) = 0{,}05 + 0{,}40 + 5{,}60 + 25{,}60 + 25{,}60 = 57{,}25\text{ GB}^2$$

#### Ý 2: Tính $\operatorname{Var}(X)$ trực tiếp từ định nghĩa
Với $\mu = E(X) = 6{,}45\text{ GB}$, áp dụng $\operatorname{Var}(X) = \sum (x - \mu)^2 p_X(x)$:
- Tại $x=1$: $(1 - 6{,}45)^2 \cdot 0{,}05 = (-5{,}45)^2 \cdot 0{,}05 = 29{,}7025 \cdot 0{,}05 = 1{,}485125$
- Tại $x=2$: $(2 - 6{,}45)^2 \cdot 0{,}10 = (-4{,}45)^2 \cdot 0{,}10 = 19{,}8025 \cdot 0{,}10 = 1{,}980250$
- Tại $x=4$: $(4 - 6{,}45)^2 \cdot 0{,}35 = (-2{,}45)^2 \cdot 0{,}35 = 6{,}0025 \cdot 0{,}35 = 2{,}100875$
- Tại $x=8$: $(8 - 6{,}45)^2 \cdot 0{,}40 = (1{,}55)^2 \cdot 0{,}40 = 2{,}4025 \cdot 0{,}40 = 0{,}961000$
- Tại $x=16$: $(16 - 6{,}45)^2 \cdot 0{,}10 = (9{,}55)^2 \cdot 0{,}10 = 91{,}2025 \cdot 0{,}10 = 9{,}120250$

Cộng tổng 5 giá trị:
$$\operatorname{Var}(X) = 1{,}485125 + 1{,}980250 + 2{,}100875 + 0{,}961000 + 9{,}120250 = 15{,}6475\text{ GB}^2$$

#### Ý 3: Kiểm tra bằng công thức rút gọn
$$\operatorname{Var}(X) = E(X^2) - [E(X)]^2 = 57{,}25 - (6{,}45)^2 = 57{,}25 - 41{,}6025 = 15{,}6475\text{ GB}^2$$
Hai kết quả hoàn toàn trùng khớp!

#### Ý 4: Tính độ lệch chuẩn $\operatorname{SD}(X)$
$$\operatorname{SD}(X) = \sqrt{\operatorname{Var}(X)} = \sqrt{15{,}6475} \approx 3{,}9557\text{ GB}$$

- **Kết luận**: Khách hàng mua USB có dung lượng trung bình là $6{,}45\text{ GB}$, và độ biến thiên điển hình xung quanh mức trung bình này là khoảng $3{,}96\text{ GB}$.

---

## ⚠️ (d) CẠM BẪY & LỖI THƯỜNG GẶP (COMMON PITFALLS)

| Cạm bẫy | CÁCH HIỂU SAI ❌ | CÁCH HIỂU ĐÚNG ✔️ |
|:---|:---|:---|
| **Bẫy 1: Biến đổi tuyến tính của Phương sai** | $\operatorname{Var}(3X + 2) = 3\operatorname{Var}(X) + 2$ hoặc $3^2\operatorname{Var}(X) + 2$ | $\operatorname{Var}(3X + 2) = 3^2 \cdot \operatorname{Var}(X) = 9\operatorname{Var}(X)$. Hằng số $+2$ bị triệt tiêu hoàn toàn vì cộng hằng số không làm dãn dữ liệu! |
| **Bẫy 2: Thứ nguyên đơn vị đo** | Ghi $\operatorname{Var}(X) = 15{,}65\text{ GB}$ (nhầm đơn vị với độ lệch chuẩn) | Phương sai có đơn vị bình phương: $\text{GB}^2$. Độ lệch chuẩn mới có đơn vị $\text{GB}$. Quên ghi mũ 2 ở phương sai sẽ bị trừ 0.25đ! |
| **Bẫy 3: Đẳng thức sai lầm $E(X^2) = [E(X)]^2$** | Cho rằng $E(X^2)$ bằng bình phương của $E(X)$ | $[E(X)]^2$ là bình phương của một số thực, còn $E(X^2)$ là kỳ vọng của biến ngẫu nhiên $X^2$. Luôn có $E(X^2) \ge [E(X)]^2$, hiệu của chúng chính là $\operatorname{Var}(X) \ge 0$. |

---

## 🏋️ (e) BÀI TẬP TỰ THỬ SỨC (QUICK PRACTICE)

**Đề bài (Slide Week 07, trang 18–19):**
Nhiệt độ phòng $X$ đo bằng độ Celsius ($^\circ\text{C}$) có kỳ vọng $E(X) = 25^\circ\text{C}$ và độ lệch chuẩn $\operatorname{SD}(X) = 3^\circ\text{C}$. Nhiệt độ đo bằng độ Fahrenheit ($^\circ\text{F}$) được đổi theo công thức:
$$Y = 1{,}8 \cdot X + 32$$
Hãy tính kỳ vọng $E(Y)$, phương sai $\operatorname{Var}(Y)$ và độ lệch chuẩn $\operatorname{SD}(Y)$ kèm đơn vị đo.

<details>
<summary><b>👉 Bấm vào đây để xem Gợi ý và Lời giải chi tiết</b></summary>

- **Gợi ý**: 
  - Áp dụng $E(aX+b) = aE(X)+b$ với $a=1{,}8; b=32$.
  - Tính $\operatorname{Var}(X) = [\operatorname{SD}(X)]^2$.
  - Áp dụng $\operatorname{SD}(aX+b) = |a|\operatorname{SD}(X)$.
- **Lời giải**:
  - $E(Y) = 1{,}8 \cdot E(X) + 32 = 1{,}8(25) + 32 = 45 + 32 = 77^\circ\text{F}$.
  - $\operatorname{SD}(Y) = 1{,}8 \cdot \operatorname{SD}(X) = 1{,}8 \cdot 3 = 5{,}4^\circ\text{F}$.
  - $\operatorname{Var}(Y) = [\operatorname{SD}(Y)]^2 = (5{,}4)^2 = 29{,}16\text{ }(^\circ\text{F})^2$ (hoặc tính bằng $1{,}8^2 \cdot \operatorname{Var}(X) = 3{,}24 \cdot 9 = 29{,}16$).
</details>

---

## ❓ (f) CÂU KIỂM TRA HIỂU BÀI (CONCEPT QUIZ)

**Câu hỏi**: Cho biến ngẫu nhiên $X$ có phương sai $\operatorname{Var}(X) = 4$. Hãy tính phương sai của biến ngẫu nhiên $Y = 3X + 2$.

- A. $36$
- B. $38$
- C. $14$
- D. $12$

### Phân tích đáp án & Phản hồi chẩn đoán:
- **Đáp án đúng là A ($36$)**:
  - *Giải thích*: Áp dụng công thức biến đổi tuyến tính: $\operatorname{Var}(aX + b) = a^2 \operatorname{Var}(X)$.
  - Thay số: $\operatorname{Var}(3X + 2) = 3^2 \cdot \operatorname{Var}(X) = 9 \cdot 4 = 36$.
- **Nếu bạn chọn B ($38$) — Sai**: Bạn đã nhớ phải bình phương hệ số $3$ thành $9$, nhưng lại cộng thêm $2$ vào kết quả ($9 \cdot 4 + 2 = 38$). *Hãy ghi nhớ*: cộng thêm hằng số chỉ làm dịch chuyển vị trí trung tâm, hoàn toàn không làm thay đổi độ phân tán nên số $+2$ phải bị triệt tiêu!
- **Nếu bạn chọn C ($14$) — Sai**: Bạn đã nhầm công thức phương sai sang công thức kỳ vọng: $3 \cdot 4 + 2 = 14$. Đối với phương sai, hệ số phải bình phương và hằng số tự do phải bỏ đi.
- **Nếu bạn chọn D ($12$) — Sai**: Bạn đã nhân $3 \cdot 4 = 12$ nhưng quên không bình phương hệ số $a$ (phải là $3^2 = 9$).

---

## 📚 (g) BÀI TẬP TỰ LUẬN MẪU CHUẨN THI GIỮA KỲ UET (KÈM BAREM CHẤM)

### Đề bài (Slide Week 07, trang 6, 8, 9, 15)
Một cơ sở kiểm tra hai sản phẩm độc lập. Mỗi sản phẩm đạt chuẩn với xác suất $0{,}8$. Gọi $X$ là số sản phẩm đạt chuẩn trong 2 sản phẩm được kiểm tra. Chi phí kiểm định và xử lý lô hàng (tính bằng nghìn đồng) được xác định theo mô hình:
$$C = 50 + 20X$$
1. Lập bảng phân phối xác suất của $X$.
2. Tính chi phí xử lý kỳ vọng $E(C)$.
3. Tính phương sai $\operatorname{Var}(C)$ và độ lệch chuẩn $\operatorname{SD}(C)$ của chi phí xử lý.

---

### Lời giải chuẩn Barem điểm UET:

#### Ý 1: Lập bảng phân phối xác suất của $X$ `[1,0 điểm]`
- Vì kiểm tra 2 sản phẩm độc lập, mỗi sản phẩm đạt chuẩn với xác suất $p = 0{,}8$, nên $X$ nhận các giá trị $x \in \{0, 1, 2\}$:
  - $P(X = 0) = (1 - 0{,}8)^2 = 0{,}2^2 = 0{,}04$  `[0.25đ]`
  - $P(X = 1) = 2 \cdot 0{,}8 \cdot (1 - 0{,}8) = 2 \cdot 0{,}8 \cdot 0{,}2 = 0{,}32$  `[0.25đ]`
  - $P(X = 2) = 0{,}8^2 = 0{,}64$  `[0.25đ]`
- Ta có bảng phân phối xác suất:
  
  | $x$ | 0 | 1 | 2 | Tổng |
  |:---|:---:|:---:|:---:|:---:|
  | $p_X(x)$ | 0,04 | 0,32 | 0,64 | 1,00 | `[0.25đ]`

#### Ý 2: Tính chi phí xử lý kỳ vọng $E(C)$ `[0,5 điểm]`
- Kỳ vọng số sản phẩm đạt chuẩn:
  $$E(X) = 0(0{,}04) + 1(0{,}32) + 2(0{,}64) = 0{,}32 + 1{,}28 = 1{,}6\text{ (sản phẩm)}$$  `[0.25đ]`
- Áp dụng tính chất tuyến tính của kỳ vọng:
  $$E(C) = E(50 + 20X) = 50 + 20 \cdot E(X) = 50 + 20(1{,}6) = 50 + 32 = 82\text{ (nghìn đồng)}$$  `[0.25đ]`

#### Ý 3: Tính $\operatorname{Var}(C)$ và $\operatorname{SD}(C)$ `[0,5 điểm]`
- Ta tính $E(X^2) = 0^2(0{,}04) + 1^2(0{,}32) + 2^2(0{,}64) = 0{,}32 + 2{,}56 = 2{,}88$.
- Phương sai của $X$:
  $$\operatorname{Var}(X) = E(X^2) - [E(X)]^2 = 2{,}88 - 1{,}6^2 = 2{,}88 - 2{,}56 = 0{,}32\text{ (sản phẩm}^2\text{)}$$  `[0.15đ]`
- Phương sai của chi phí $C$:
  $$\operatorname{Var}(C) = \operatorname{Var}(50 + 20X) = 20^2 \cdot \operatorname{Var}(X) = 400 \cdot 0{,}32 = 128\text{ (nghìn đồng)}^2$$  `[0.20đ]`
- Độ lệch chuẩn của chi phí $C$:
  $$\operatorname{SD}(C) = \sqrt{\operatorname{Var}(C)} = \sqrt{128} = 8\sqrt{2} \approx 11{,}31\text{ (nghìn đồng)}$$  `[0.15đ]`

---

### 📌 Mẹo trình bày để ăn trọn điểm (Pro Tips)
1. **Luôn kiểm tra tổng xác suất**: Sau khi lập bảng ở Ý 1, cộng nhẩm $0{,}04 + 0{,}32 + 0{,}64 = 1{,}00$. Giám khảo luôn nhìn dòng "Tổng = 1" để chấm bước này.
2. **Không bỏ quên đơn vị**: Ở Ý 3, ghi rõ $(nghìn\text{ }đồng)^2$ cho phương sai và $nghìn\text{ }đồng$ cho độ lệch chuẩn. Nếu chỉ ghi con số trần trụi $128$ và $11{,}31$, bạn rất dễ bị trừ 0.25đ điểm trình bày!

---

## 🔎 NGUỒN HỌC LIỆU
- **Slide UET.MAT1052 Week 07**: Trang 4, 5, 7, 8, 9, 14, 15, 16, 17, 79, 80, 81.
- **Giáo trình Stat20**: Chương 4, Mục 4.7 (Kỳ vọng và phương sai), Mục 4.8 (Kỳ vọng của một biến ngẫu nhiên), Mục 4.10 (Phương sai và độ lệch chuẩn).
- **Mã nguồn kiểm chứng**: Đã kiểm tra số học và chạy kiểm thử tự động tại [verify_sample_lesson.py](file:///d:/Projects/XSTK/verify/verify_sample_lesson.py).
