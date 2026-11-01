# KHUNG VÀ CHUẨN CHẤT LƯỢNG HỌC LIỆU (TEMPLATES & STANDARDS)
## Môn học: UET.MAT1052 — Xác suất Thống kê

Tài liệu này quy định cấu trúc bắt buộc và chuẩn mực chất lượng cho mọi bài giảng, bài tập tự luận, và câu hỏi trắc nghiệm trong toàn bộ hệ thống học liệu.

---

# PHẦN 1: KHUNG CHUẨN MỘT BÀI GIẢNG (LESSON TEMPLATE)
Mỗi bài học được chia nhỏ theo nguyên tử kiến thức (micro-learning), tối đa 3–5 bước đọc ngắn, không viết tường chữ, luôn kèm ví dụ số ngay lập tức. Cấu trúc bài giảng tuân thủ nghiêm ngặt **7 thành phần bắt buộc (a – g)**:

### 1. Tiêu đề & Mục tiêu đầu ra
- **Tên bài học**: Rõ ràng, gắn liền với khái niệm cốt lõi.
- **Bạn sẽ làm được gì sau bài này**: 1–2 gạch đầu dòng hành động cụ thể (ví dụ: *"Tính được kỳ vọng và phương sai từ bảng phân phối; giải thích được ý nghĩa đơn vị đo; không bị lừa bởi biến đổi tuyến tính"*).

### (a) Trực giác bằng lời (Intuition)
- Trả lời 3 câu hỏi trước khi đưa công thức:
  1. *Nó là cái gì trong đời thực?* (Ẩn dụ thực tế: chiếc bập bênh, tâm khối lượng, độ rung lắc, thước đo rủi ro...).
  2. *Vì sao người ta phải nghĩ ra nó?* (Nếu chỉ có trung bình thì thiếu thông tin gì? Vì sao phải bình phương sai số?).
  3. *Khi nào dùng nó?* (Nhận diện ngữ cảnh bài toán thực tế).
- Tuyệt đối không dùng thuật ngữ toán trừu tượng để giải thích một khái niệm trừu tượng.

### (b) Định nghĩa & Công thức toán học chuẩn xác
- Trình bày công thức bằng ký hiệu toán học chuẩn mực (LaTeX), đồng bộ với Slide UET MAT1052.
- Giải thích rõ từng ký hiệu trong công thức và thứ nguyên đơn vị.
- Đóng khung công thức then chốt (Highlight box).

### (c) Ví dụ giải mẫu từng bước (Step-by-step Worked Example)
- Bài toán số liệu cụ thể (lấy từ slide bài giảng hoặc bài thi thực tế).
- Lời giải chia nhỏ thành các bước rõ ràng:
  - *Bước 1: Tóm tắt đề & Gọi tên biến ngẫu nhiên*
  - *Bước 2: Viết công thức tổng quát trước khi thay số*
  - *Bước 3: Thay số và thực hiện phép tính trung gian*
  - *Bước 4: Kết luận kèm đơn vị đo rõ ràng*
- Mọi phép tính phải có đoạn script kiểm chứng đi kèm (Python / R).

### (d) Cạm bẫy & Lỗi thường gặp (Common Pitfalls)
- Nêu rõ 2–3 sai lầm mà 80% sinh viên năm đầu hay mắc phải (ví dụ: quên bình phương $a$ trong $\operatorname{Var}(aX+b)$, nhầm đơn vị giữa phương sai và độ lệch chuẩn, nhầm độc lập với xung khắc).
- So sánh song song: **CÁCH NGHĨ SAI ❌** vs **CÁCH NGHĨ ĐÚNG ✔️**.

### (e) Tự thử sức (Quick Check / Practice)
- Một bài toán tương tự để người học tự tính trong 1–2 phút.
- Có nút bấm hoặc cơ chế ẩn/hiện "Gợi ý" và "Đáp số chi tiết" để người học chủ động suy nghĩ trước khi nhìn đáp án.

### (f) Câu kiểm tra hiểu bài tương tác (Interactive Concept Quiz)
- 1 câu trắc nghiệm chốt bài.
- 4 phương án lựa chọn: 1 đáp án đúng + 3 đáp án nhiễu phản ánh chính xác 3 lỗi sai phổ biến.
- Phản hồi tức thì (Instant Feedback):
  - Khi chọn đúng: Chúc mừng + Khẳng định lại nguyên lý cốt lõi.
  - Khi chọn sai: Chỉ rõ bạn vừa mắc phải bẫy nào (ví dụ: *"Bạn ra 38 vì bạn cộng thẳng 2 vào phương sai. Hãy nhớ: cộng hằng số chỉ tịnh tiến đồ thị, không làm dữ liệu phân tán thêm!"*).

### (g) Nguồn đối chiếu (Citations)
- Ghi rõ nguồn gốc học liệu ở cuối mỗi bài: số trang trong Slide UET MAT1052 và số mục tương ứng trong giáo trình Stat20.

---

# PHẦN 2: KHUNG CHUẨN MỘT BÀI TẬP TỰ LUẬN (FREE RESPONSE TEMPLATE)
Bài tự luận được thiết kế để rèn luyện kỹ năng trình bày chuẩn mực thi học kỳ, giúp sinh viên ăn trọn vẹn điểm số từng bước.

```markdown
### [DẠNG BÀI] — Tên bài toán (Mức độ: Cơ bản / Trung bình / Nâng cao)

#### 1. ĐỀ BÀI
[Bối cảnh bài toán thực tế, số liệu rõ ràng, câu hỏi chia theo các ý a, b, c]

#### 2. PHÂN TÍCH ĐỀ & ĐỊNH HƯỚNG GIẢI
- Dữ kiện đã cho: ...
- Yêu cầu cần tìm: ...
- Nhận diện mô hình toán: Biến ngẫu nhiên nào? Phân phối gì? Vì sao chọn mô hình này?

#### 3. BẬT / TẮT GỢI Ý TỪNG BƯỚC (Interactive Progressive Hints)
- [Gợi ý 1]: Công thức cần dùng là gì?
- [Gợi ý 2]: Thay số bước đầu như thế nào?
- [Gợi ý 3]: Lưu ý biến đổi đại số / tra bảng số.

#### 4. LỜI GIẢI CHI TIẾT CHUẨN BAREM ĐIỂM
- **Bước 1**: Gọi biến ngẫu nhiên, xác định không gian giá trị và điều kiện (nêu rõ giả thiết i.i.d., $n \ge 30$ nếu dùng CLT).  `[+0.25đ]`
- **Bước 2**: Viết công thức tổng quát bằng chữ và ký hiệu.  `[+0.25đ]`
- **Bước 3**: Thay số chi tiết, trình bày phép tính trung gian.  `[+0.25đ]`
- **Bước 4**: Kết luận rõ ràng, ghi đúng đơn vị thực tế (kg, phút, $\text{GB}^2$...).  `[+0.25đ]`

#### 5. CÁCH TRÌNH BÀY ĐỂ ĐẠT ĐIỂM TỐI ĐA (Pro Tips for Max Score)
- Những câu chữ giám khảo UET bắt buộc phải nhìn thấy trong bài thi.
- Quy chuẩn làm tròn (ví dụ: giữ 4 chữ số thập phân cho xác suất).

#### 6. BẪY THƯỜNG GẶP & NƠI DỄ BỊ TRỪ ĐIỂM (Where Students Lose Points)
- Liệt kê các lỗi khiến sinh viên mất từ 0.25đ đến 0.5đ một cách oan uổng.

#### 7. MÃ NGUỒN KIỂM CHỨNG (Verification Script)
- Khối code Python / R tính toán độc lập ra kết quả chính xác 100%.
```

---

# PHẦN 3: KHUNG CHUẨN MỘT CÂU TRẮC NGHIỆM (MULTIPLE CHOICE TEMPLATE)
Mỗi câu hỏi trắc nghiệm không chỉ để kiểm tra đáp số mà là một **công cụ chẩn đoán lỗ hổng kiến thức**.

```markdown
### [MÃ CÂU] — [CHỦ ĐỀ] — Mức độ: [Nhận biết / Thông hiểu / Vận dụng]

**Câu hỏi**: [Đề bài ngắn gọn, chuẩn xác]

**Các phương án lựa chọn**:
- A. [Đáp án Đúng]
- B. [Đáp án Nhiễu 1]
- C. [Đáp án Nhiễu 2]
- D. [Đáp án Nhiễu 3]

**Giải thích chi tiết & Phân tích đáp án**:
- **Đáp án đúng là A**: 
  - Giải thích bản chất toán học.
  - Các bước tính toán ra kết quả.
- **Vì sao B sai**: Phản ánh lỗi sai tư duy gì (ví dụ: dùng nhầm công thức của biến liên tục cho biến rời rạc).
- **Vì sao C sai**: Phản ánh lỗi sai tính toán gì (ví dụ: quên bình phương hệ số $a$).
- **Vì sao D sai**: Phản ánh bẫy khái niệm gì (ví dụ: nhầm lẫn giữa độc lập và xung khắc).
```
