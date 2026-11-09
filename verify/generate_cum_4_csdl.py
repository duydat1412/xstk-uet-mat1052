import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

cum_4_code = """// ==========================================================================
// CỤM 4 (CSDL): PHỤ THUỘC HÀM & CHUẨN HÓA CƠ SỞ DỮ LIỆU
// Bao gồm: Bài CSDL_10, CSDL_11, CSDL_12, CSDL_13, CSDL_14
// Nguồn: Slide UET.IS2099 C4_1.pptx (96 slides)
// ==========================================================================

const CUM_4_CSDL = [
  {
    id: "CSDL_10",
    cluster: "4",
    title: "Dư thừa dữ liệu, Dị thường & Định nghĩa Phụ thuộc hàm (FD)",
    sources: "Slide UET.IS2099 Chương 4 (Slide 1–25)",
    ref: {
      slide_file: "C4_1.pptx",
      slide_name: "Chương 4 — Phụ thuộc hàm và Chuẩn hóa CSDL",
      pages: "Slide 1 – 25",
      page_start: 1,
      page_end: 25,
      section: "Mục 4.1: Sự dư thừa và dị thường dữ liệu; Mục 4.2: Khái niệm Phụ thuộc hàm (FD)",
      key_points: [
        "3 loại dị thường dữ liệu kinh điển: Dị thường thêm (Insertion Anomaly), Dị thường xóa (Deletion Anomaly), Dị thường cập nhật (Update Anomaly)",
        "Định nghĩa toán học của Phụ thuộc hàm: X -> Y (X xác định hàm Y, hoặc Y phụ thuộc hàm vào X)",
        "Điều kiện thỏa mãn: Với mọi cặp bộ t1, t2 trong quan hệ, nếu t1[X] = t2[X] thì bắt buộc t1[Y] = t2[Y]",
        "Phụ thuộc hàm tầm thường (Trivial FD): X -> Y trong đó Y là tập con của X (Y ⊆ X)"
      ],
      remind: "Dị thường dữ liệu là câu hỏi lý thuyết mở đầu của mọi đề thi CSDL. Mở Slide C4_1 trang 4–10 để xem bảng ví dụ về dị thường trong quản lý nhân viên và đề án."
    },
    desc: "Hiểu rõ nguyên nhân sâu xa của dư thừa dữ liệu, 3 loại dị thường nguy hiểm và định nghĩa toán học nền tảng của Phụ thuộc hàm.",
    steps: [
      {
        t: "Ba Dị thường dữ liệu (Anomalies) khi thiết kế CSDL tồi",
        c: `<p>Khi gom quá nhiều thông tin không liên quan vào cùng một bảng, CSDL sẽ xuất hiện <b>dư thừa dữ liệu</b> và dẫn tới 3 loại dị thường nghiêm trọng:</p>
            <ul>
              <li><b>Dị thường cập nhật (Update Anomaly)</b>: Khi thông tin của một đối tượng bị lặp lại ở hàng chục hàng khác nhau (ví dụ: Tên phòng ban 'Kế toán' lặp lại ở 100 nhân viên). Nếu phòng ban đổi tên thành 'Tài chính - Kế toán', ta phải cập nhật 100 lần. Nếu sót 1 dòng, dữ liệu sẽ bị mâu thuẫn, mất tính nhất quán!</li>
              <li><b>Dị thường xóa (Deletion Anomaly)</b>: Khi xóa một thực thể, ta <i>vô tình làm mất luôn thông tin của một thực thể hoàn toàn khác</i>! (Ví dụ: Nếu phòng ban số 4 chỉ có 1 nhân viên duy nhất. Khi nhân viên này nghỉ việc và bị xóa, toàn bộ thông tin về phòng ban số 4 cũng biến mất khỏi hệ thống).</li>
              <li><b>Dị thường thêm (Insertion Anomaly)</b>: Khi muốn thêm thông tin của một đối tượng mới, ta không thể thực hiện được nếu chưa có thông tin của đối tượng đi kèm (vì vướng ràng buộc khóa chính không được NULL). (Ví dụ: Thành lập phòng ban mới nhưng chưa tuyển được nhân viên nào, ta không thể thêm phòng ban vào bảng vì chưa có Mã nhân viên để làm khóa chính).</li>
            </ul>`
      },
      {
        t: "Định nghĩa Toán học của Phụ thuộc hàm (Functional Dependency)",
        c: `<p>Phụ thuộc hàm là công cụ toán học hình thức dùng để phát hiện và loại bỏ dư thừa dữ liệu:</p>
            <div class="tip-box">
              <b>Định nghĩa chính xác (Slide C4_1 tr. 11):</b><br>
              Cho lược đồ quan hệ $R(A_1, A_2, \\dots, A_n)$ và hai tập thuộc tính $X, Y \\subseteq R$.<br>
              Ta nói rằng <b>$X$ xác định hàm $Y$</b> (hoặc <b>$Y$ phụ thuộc hàm vào $X$</b>), ký hiệu là:
              $$X \\to Y$$
              nếu với <b>mọi thể hiện hợp lệ $r(R)$</b>, với bất kỳ hai bộ $t_1, t_2 \\in r(R)$ nào, hễ giá trị trên $X$ giống nhau thì giá trị trên $Y$ cũng bắt buộc phải giống nhau:
              $$\\forall t_1, t_2 \\in r(R): t_1[X] = t_2[X] \\implies t_1[Y] = t_2[Y]$$
            </div>
            <ul>
              <li>$X$ được gọi là <b>Vế trái (Determinant / Tập xác định)</b>.</li>
              <li>$Y$ được gọi là <b>Vế phải (Dependent / Tập phụ thuộc)</b>.</li>
              <li><b>Phụ thuộc hàm tầm thường (Trivial FD)</b>: Nếu $Y \\subseteq X$ (ví dụ: $AB \\to A$), thì phụ thuộc hàm này luôn luôn đúng trong mọi trường hợp và không mang giá trị ngữ nghĩa mới.</li>
              <li><b>Phụ thuộc hàm không tầm thường (Non-trivial FD)</b>: Khi $Y \\not\\subseteq X$.</li>
            </ul>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide C4_1 — Slide 10–12] Nhận diện Phụ thuộc hàm từ Ngữ cảnh Thực tế",
        q: "Trong CSDL Sinh viên UET: 'Mỗi sinh viên có một Mã sinh viên duy nhất (`MaSV`), ứng với một `HoTen`, một `NgaySinh` và thuộc một `Khoa`. Mỗi Khoa có một `TruongKhoa` duy nhất'. Hãy viết các phụ thuộc hàm xuất hiện trong bài toán này.",
        sol: "<b>Phân tích ngữ nghĩa nghiệp vụ:</b><br>" +
             "1. Biết <code>MaSV</code> thì xác định duy nhất Họ tên, Ngày sinh và Khoa:<br>" +
             "   $$MaSV \\to HoTen, \\quad MaSV \\to NgaySinh, \\quad MaSV \\to Khoa$$<br>" +
             "   (hoặc viết gộp: $MaSV \\to HoTen, NgaySinh, Khoa$).<br>" +
             "2. Biết tên <code>Khoa</code> thì xác định duy nhất Trưởng khoa:<br>" +
             "   $$Khoa \\to TruongKhoa$$"
      },
      {
        level: "Trung bình",
        t: "[Slide C4_1 — Slide 12–13] Kiểm tra Dữ liệu Thực tế có Thỏa mãn Phụ thuộc hàm không",
        q: "Cho bảng dữ liệu $r(R)$ với các bộ sau: `t1 = (A: 1, B: 2, C: 3)`, `t2 = (A: 1, B: 2, C: 4)`, `t3 = (A: 2, B: 5, C: 3)`. Bảng $r(R)$ này có thỏa mãn phụ thuộc hàm $A \\to B$ không? Có thỏa mãn $A \\to C$ không?",
        sol: "<b>Kiểm tra theo định nghĩa:</b><br>" +
             "1. Xét $A \\to B$:<br>" +
             "   - So sánh $t_1$ và $t_2$: $t_1[A] = t_2[A] = 1 \\implies t_1[B] = t_2[B] = 2$ (thỏa mãn).<br>" +
             "   - Bộ $t_3$ có $A = 2$ không trùng với bộ nào khác.<br>" +
             "   $\\rightarrow$ Bảng $r(R)$ <b>THỎA MÃN</b> phụ thuộc hàm $A \\to B$.<br>" +
             "2. Xét $A \\to C$:<br>" +
             "   - So sánh $t_1$ và $t_2$: $t_1[A] = t_2[A] = 1$, nhưng $t_1[C] = 3 \\neq t_2[C] = 4$.<br>" +
             "   $\\rightarrow$ Bảng $r(R)$ <b>VI PHẠM</b> phụ thuộc hàm $A \\to C$!"
      },
      {
        level: "Vận dụng",
        t: "[Slide C4_1 — Slide 5–9] Phân tích 3 Dị thường trong Bảng Quản lý Nhân viên - Đề án",
        q: "Xét bảng gom chung: `NV_DA(`<u>`MaNV, MaDA`</u>`, TenNV, Luong, TenDA, DiaDiemDA, SoGio)`. Hãy chỉ rõ 3 dị thường (Thêm, Xóa, Cập nhật) xảy ra trong bảng này.",
        sol: "<b>Phân tích chi tiết 3 dị thường:</b><br>" +
             "1. <b>Dị thường thêm (Insertion Anomaly)</b>: Không thể thêm một đề án mới (ví dụ Đề án số 10) nếu chưa phân công nhân viên nào làm việc cho đề án đó, vì khóa chính có chứa <code>MaNV</code> (vi phạm quy tắc toàn vẹn thực thể không được NULL).<br>" +
             "2. <b>Dị thường xóa (Deletion Anomaly)</b>: Nếu nhân viên duy nhất đang phụ trách đề án số 5 xin nghỉ việc và bị xóa, thì mọi thông tin về <code>TenDA</code> và <code>DiaDiemDA</code> của đề án số 5 cũng bị xóa sạch khỏi CSDL.<br>" +
             "3. <b>Dị thường cập nhật (Update Anomaly)</b>: Tên nhân viên và Mức lương bị lặp lại ở tất cả các đề án mà nhân viên đó tham gia. Nếu nhân viên được tăng lương, phải sửa trên hàng chục dòng; nếu sót 1 dòng, dữ liệu lương của cùng một người sẽ bị mâu thuẫn."
      }
    ],
    pitfalls: [
      {
        bad: "Nhìn vào vài hàng dữ liệu cụ thể trong bảng để khẳng định một phụ thuộc hàm luôn đúng.",
        good: "Phụ thuộc hàm là ràng buộc ngữ nghĩa thực tế phải đúng trên MỌI thể hiện có thể có trong tương lai, không chỉ đúng trên một vài dòng dữ liệu tạm thời."
      },
      {
        bad: "Nghĩ rằng nếu X -> Y thì chắc chắn Y -> X (tính đối xứng).",
        good: "Phụ thuộc hàm hoàn toàn KHÔNG có tính đối xứng! Ví dụ: MaSV -> NgaySinh là đúng, nhưng NgaySinh -> MaSV là sai (nhiều sinh viên có thể cùng ngày sinh)."
      }
    ],
    quizzes: [
      {
        level: "Nhận biết",
        badge: "🟢 Cấp độ 1: Nhận biết",
        q: "Phụ thuộc hàm nào sau đây là một Phụ thuộc hàm tầm thường (Trivial Functional Dependency)?",
        opts: [
          "$A \\to B$",
          "$AB \\to A$",
          "$A \\to BC$",
          "$B \\to C$"
        ],
        ans: 1,
        fb: "Chính xác! Phụ thuộc hàm tầm thường là phụ thuộc hàm có vế phải là tập con của vế trái ($A \\subseteq AB$). Nó luôn đúng với mọi quan hệ."
      },
      {
        level: "Thông hiểu",
        badge: "🟡 Cấp độ 2: Thông hiểu",
        q: "Hiện tượng khi xóa một sinh viên khỏi CSDL mà vô tình làm mất luôn thông tin về lớp học chuyên ngành duy nhất của sinh viên đó được gọi là:",
        opts: [
          "Dị thường cập nhật (Update anomaly)",
          "Dị thường thêm (Insertion anomaly)",
          "Dị thường xóa (Deletion anomaly)",
          "Vi phạm tính nguyên tố"
        ],
        ans: 2,
        fb: "Đúng! Dị thường xóa xảy ra khi việc xóa một đối tượng kéo theo sự mất mát ngoài ý muốn của một đối tượng độc lập khác."
      },
      {
        level: "Vận dụng",
        badge: "🔴 Cấp độ 3: Vận dụng & Bẫy",
        q: "Cho quan hệ $R(A, B, C)$. Bảng dữ liệu hiện tại có 2 bộ: `(1, 2, 3)` và `(1, 2, 4)`. Phụ thuộc hàm nào sau đây BỊ VI PHẠM bởi bảng dữ liệu này?",
        opts: [
          "$A \\to B$",
          "$B \\to A$",
          "$AB \\to C$",
          "$C \\to A$"
        ],
        ans: 2,
        fb: "Rất chuẩn! Với cả hai bộ, vế trái $AB = (1, 2)$ giống nhau, nhưng vế phải $C$ lại khác nhau (3 và 4), do đó $AB \\to C$ bị vi phạm nghiêm trọng."
      }
    ]
  },

  {
    id: "CSDL_11",
    cluster: "4",
    title: "Hệ tiên đề Armstrong & Thuật toán tìm Bao đóng thuộc tính X+",
    sources: "Slide UET.IS2099 Chương 4 (Slide 26–45)",
    ref: {
      slide_file: "C4_1.pptx",
      slide_name: "Chương 4 — Phụ thuộc hàm và Chuẩn hóa CSDL",
      pages: "Slide 26 – 45",
      page_start: 26,
      page_end: 45,
      section: "Mục 4.4: Hệ suy diễn Armstrong; Mục 4.6: Thuật toán tìm Bao đóng của tập thuộc tính (X+)",
      key_points: [
        "3 Tiên đề Armstrong cốt lõi: Luật Phản xạ (Reflexivity), Luật Tăng trưởng (Augmentation), Luật Bắc cầu (Transitivity)",
        "3 Quy tắc dẫn xuất: Luật Phân rã (Decomposition), Luật Hợp (Union), Luật Tựa bắc cầu (Pseudotransitivity)",
        "Bao đóng của tập thuộc tính X+ dưới tập F: Tập hợp tất cả các thuộc tính A sao cho X -> A được suy diễn từ F",
        "Thuật toán lặp tìm X+ (O(n^2)): Khởi tạo X+ = X, liên tục bổ sung vế phải của các FD có vế trái nằm trong X+"
      ],
      remind: "Thuật toán tìm bao đóng X+ là nền tảng của 100% các câu hỏi về tìm khóa và kiểm tra dạng chuẩn. Xem kỹ Slide C4_1 trang 28–32."
    },
    desc: "Nắm vững Hệ tiên đề Armstrong và làm chủ thuật toán tìm Bao đóng thuộc tính X+ — chìa khóa vạn năng cho bài thi Chuẩn hóa CSDL.",
    steps: [
      {
        t: "Hệ tiên đề Armstrong & Các quy tắc dẫn xuất",
        c: `<p>Năm 1974, William W. Armstrong đề xuất hệ 3 tiên đề đúng đắn (Sound) và đầy đủ (Complete) để suy diễn mọi phụ thuộc hàm hợp lý:</p>
            <ol>
              <li><b>Luật Phản xạ (Reflexivity)</b>: Nếu $Y \\subseteq X$ thì $X \\to Y$. (Ví dụ: $AB \\to A$).</li>
              <li><b>Luật Tăng trưởng (Augmentation)</b>: Nếu $X \\to Y$ thì $XZ \\to YZ$ với mọi tập thuộc tính $Z$.</li>
              <li><b>Luật Bắc cầu (Transitivity)</b>: Nếu $X \\to Y$ và $Y \\to Z$ thì $X \\to Z$.</li>
            </ol>
            <div class="tip-box">
              <b>3 Quy tắc dẫn xuất thực chiến hay dùng nhất:</b><br>
              • <b>Luật Hợp (Union)</b>: $\\{ X \\to Y, \\; X \\to Z \\} \\implies X \\to YZ$.<br>
              • <b>Luật Phân rã (Decomposition)</b>: $X \\to YZ \\implies \\{ X \\to Y, \\; X \\to Z \\}$.<br>
              • <b>Luật Tựa bắc cầu (Pseudotransitivity)</b>: $\\{ X \\to Y, \\; WY \\to Z \\} \\implies WX \\to Z$.
            </div>`
      },
      {
        t: "Thuật toán Tìm Bao đóng của Tập thuộc tính (X+)",
        c: `<p><b>Bao đóng của tập thuộc tính $X$</b> dưới tập phụ thuộc hàm $F$, ký hiệu là $X^+_F$ (hoặc $X^+$), là tập hợp tất cả các thuộc tính $A$ có thể được suy diễn từ $X$ nhờ $F$ (tức là $X \\to A$).</p>
            <div class="warn-box">
              <b>Thuật toán chuẩn mực (Slide C4_1 tr. 28):</b><br>
              <b>Đầu vào:</b> Tập thuộc tính $X$ và tập phụ thuộc hàm $F$.<br>
              <b>Đầu ra:</b> Bao đóng $X^+$.<br>
              1. <b>Khởi tạo:</b> $X^+ = X$.<br>
              2. <b>Lặp:</b> Duyệt qua từng phụ thuộc hàm $Y \\to Z$ trong $F$:<br>
                 - Nếu $Y \\subseteq X^+$ thì bổ sung thêm $Z$ vào: $X^+ = X^+ \\cup Z$.<br>
              3. Lặp lại bước 2 cho đến khi $X^+$ không thay đổi thêm thuộc tính nào nữa (điểm bất động).<br>
              4. <b>Trả về kết quả $X^+$.</b>
            </div>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide C4_1 — Slide 29] Tìm Bao đóng của Tập {ABC}+ cơ bản",
        q: "Ví dụ 1 Slide C4_1 trang 29: Cho tập phụ thuộc hàm $F = \\{ A \\to D, \\; E \\to H, \\; AB \\to DE, \\; CE \\to G \\}$. Hãy tính bao đóng $\\{ABC\\}^+$.",
        sol: "<b>Thực hiện thuật toán tìm bao đóng từng bước:</b><br>" +
             "- <b>Khởi tạo:</b> $X_0 = \\\\{A, B, C\\\\}$.<br>" +
             "- <b>Vòng lặp 1:</b><br>" +
             "  + Xét $A \\to D$: Vì $A \\in X_0 \\implies X_1 = X_0 \\cup \\\\{D\\\\} = \\\\{A, B, C, D\\\\}$.<br>" +
             "  + Xét $E \\to H$: $E \\notin X_1$ (bỏ qua).<br>" +
             "  + Xét $AB \\to DE$: Vì $AB \\subseteq X_1 \\implies X_2 = X_1 \\cup \\\\{D, E\\\\} = \\\\{A, B, C, D, E\\\\}$.<br>" +
             "  + Xét $CE \\to G$: Vì $CE \\subseteq X_2 \\implies X_3 = X_2 \\cup \\\\{G\\\\} = \\\\{A, B, C, D, E, G\\\\}$.<br>" +
             "- <b>Vòng lặp 2:</b><br>" +
             "  + Xét lại $E \\to H$: Bây giờ $E \\in X_3 \\implies X_4 = X_3 \\cup \\\\{H\\\\} = \\\\{A, B, C, D, E, G, H\\\\}$.<br>" +
             "- <b>Vòng lặp 3:</b> Không bổ sung thêm thuộc tính nào nữa $\\\\rightarrow$ Dừng lại.<br>" +
             "$$\\\\mathbf{\\\\{ABC\\\\}^+ = \\\\{A, B, C, D, E, G, H\\\\}}$$"
      },
      {
        level: "Trung bình",
        t: "[Slide C4_1 — Slide 31] Chứng minh một Phụ thuộc hàm có được suy diễn từ F không",
        q: "Ví dụ 3 Slide C4_1 trang 31: Cho tập phụ thuộc hàm $F = \\{ AG \\to I, \\; BE \\to I, \\; E \\to G, \\; AB \\to E, \\; GI \\to H \\}$. Hãy chứng minh xem $AB \\to H$ có được suy diễn từ $F$ hay không (nghĩa là kiểm tra $F \\models AB \\to H$).",
        sol: "<b>Quy tắc vàng: Để kiểm tra $X \\to Y$ có thuộc $F^+$ không, ta chỉ cần tính $X^+$ và xem $Y$ có nằm trong $X^+$ không!</b><br>" +
             "- Tính bao đóng $\\{AB\\}^+$:<br>" +
             "  + Khởi tạo: $X = \\\\{A, B\\\\}$.<br>" +
             "  + Áp dụng $AB \\to E$: $X = \\\\{A, B, E\\\\}$.<br>" +
             "  + Áp dụng $E \\to G$: $X = \\\\{A, B, E, G\\\\}$.<br>" +
             "  + Áp dụng $AG \\to I$ (vì $A, G \\in X$): $X = \\\\{A, B, E, G, I\\\\}$.<br>" +
             "  + Áp dụng $GI \\to H$ (vì $G, I \\in X$): $X = \\\\{A, B, E, G, I, H\\\\}$.<br>" +
             "- Ta thấy $H \\in \\\\{AB\\\\}^+$.<br>" +
             "$$\\\\implies \\\\mathbf{F \\\\models AB \\to H} \\\\quad (\\\\text{Chứng minh hoàn tất!})$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide C4_1 — Slide 39–43] Kiểm tra Hai Tập Phụ thuộc hàm Tương đương (F ≡ E)",
        q: "Slide C4_1 trang 39: Cho hai tập phụ thuộc hàm:<br>" +
           "- $F = \\{ A \\to C, \\; AC \\to D, \\; E \\to AD, \\; E \\to H \\}$<br>" +
           "- $E = \\{ A \\to CD, \\; E \\to AH \\}$<br>" +
           "Hai tập phụ thuộc hàm $F$ và $E$ có tương đương nhau không ($F \\equiv E$)?",
        sol: "<b>Để chứng minh $F \\equiv E$, ta cần chứng minh cả hai chiều: $F \\models E$ và $E \\models F$:</b><br>" +
             "1. <b>Chiều 1 (Kiểm tra $F \\models E$):</b><br>" +
             "   - Tính $A^+_F$: $A^+_F = \\\\{A, C, D\\\\} \\implies A \\to CD$ thỏa mãn.<br>" +
             "   - Tính $E^+_F$: $E^+_F = \\\\{E, A, D, H, C\\\\} \\implies E \\to AH$ thỏa mãn.<br>" +
             "   $\\rightarrow F \\models E$.<br>" +
             "2. <b>Chiều 2 (Kiểm tra $E \\models F$):</b><br>" +
             "   - Tính $A^+_E$: $A^+_E = \\\\{A, C, D\\\\} \\implies A \\to C$ thỏa mãn.<br>" +
             "   - Tính $(AC)^+_E$: $(AC)^+_E = \\\\{A, C, D\\\\} \\implies AC \\to D$ thỏa mãn.<br>" +
             "   - Tính $E^+_E$: $E^+_E = \\\\{E, A, H, C, D\\\\} \\implies E \\to AD$ và $E \\to H$ đều thỏa mãn.<br>" +
             "   $\\rightarrow E \\models F$.<br>" +
             "$$\\\\mathbf{\\\\text{Kết luận: } F \\\\equiv E} \\\\quad (\\\\text{Hai tập tương đương hoàn toàn}).$$"
      }
    ],
    pitfalls: [
      {
        bad: "Dừng thuật toán tìm bao đóng ngay sau khi duyệt qua hết danh sách phụ thuộc hàm ở vòng lặp đầu tiên.",
        good: "Bắt buộc phải lặp lại duyệt danh sách nhiều lần cho tới khi tập bao đóng không thể mở rộng thêm nữa, vì việc bổ sung thuộc tính ở bước sau có thể kích hoạt các phụ thuộc hàm bị bỏ qua ở bước trước!"
      },
      {
        bad: "Nghĩ rằng muốn kiểm tra F ≡ E phải tính tất cả bao đóng phụ thuộc hàm F+ và E+.",
        good: "Tính F+ cực kỳ phức tạp (kích thước hàm mũ). Cách làm chuẩn và nhanh nhất là chỉ cần tính bao đóng tập thuộc tính của các vế trái."
      }
    ],
    quizzes: [
      {
        level: "Nhận biết",
        badge: "🟢 Cấp độ 1: Nhận biết",
        q: "Theo Hệ tiên đề Armstrong, nếu $X \\to Y$ và $Y \\to Z$ thì ta suy diễn được $X \\to Z$. Đây là quy tắc gì?",
        opts: [
          "Quy tắc phản xạ (Reflexivity)",
          "Quy tắc tăng trưởng (Augmentation)",
          "Quy tắc bắc cầu (Transitivity)",
          "Quy tắc phân rã (Decomposition)"
        ],
        ans: 2,
        fb: "Chính xác! Đây là Quy tắc bắc cầu (Transitivity rule) trong 3 tiên đề cốt lõi của Armstrong."
      },
      {
        level: "Thông hiểu",
        badge: "🟡 Cấp độ 2: Thông hiểu",
        q: "Cho lược đồ $R(A, B, C, D)$ với $F = \\{ A \\to B, \\; B \\to C, \\; C \\to D \\}$. Bao đóng của tập thuộc tính $\\{A\\}^+$ là:",
        opts: [
          "$\\{A, B\\}$",
          "$\\{A, B, C\\}$",
          "$\\{A, B, C, D\\}$",
          "Chỉ có $\\{A\\}$"
        ],
        ans: 2,
        fb: "Đúng! Áp dụng bắc cầu liên tục: A -> B -> C -> D, suy ra A+ = {A, B, C, D}."
      },
      {
        level: "Vận dụng",
        badge: "🔴 Cấp độ 3: Vận dụng & Bẫy",
        q: "Cho $F = \\{ AB \\to C, \\; C \\to D, \\; D \\to B \\}$. Bao đóng $\\{A, D\\}^+$ bằng:",
        opts: [
          "$\\{A, D\\}$",
          "$\\{A, B, D\\}$",
          "$\\{A, B, C, D\\}$",
          "$\\{A, C, D\\}$"
        ],
        ans: 2,
        fb: "Rất chuẩn! Bắt đầu: {A, D}. Áp dụng D -> B => {A, B, D}. Vì có AB, áp dụng AB -> C => {A, B, C, D}. Toàn bộ thuộc tính đều được suy ra!"
      }
    ]
  },

  {
    id: "CSDL_12",
    cluster: "4",
    title: "Thuật toán xác định tất cả Khóa tối thiểu của Lược đồ",
    sources: "Slide UET.IS2099 Chương 4 (Slide 46–60)",
    ref: {
      slide_file: "C4_1.pptx",
      slide_name: "Chương 4 — Phụ thuộc hàm và Chuẩn hóa CSDL",
      pages: "Slide 46 – 60",
      page_start: 46,
      page_end: 60,
      section: "Mục 4.9: Bao đóng và khóa; Thuật toán phân loại thuộc tính L, R, B, N và thuật toán tìm khóa tối thiểu",
      key_points: [
        "Định nghĩa toán học của Khóa: K là khóa nếu K+ = R và không có tập con thực sự nào của K có bao đóng bằng R",
        "Kỹ thuật phân loại 4 nhóm thuộc tính: L (chỉ xuất hiện bên Trái), R (chỉ xuất hiện bên Phải), B (xuất hiện cả hai bên), N (không xuất hiện ở vế nào)",
        "Nguyên tắc vàng: Nhóm (L ∪ N) BẮT BUỘC PHẢI CÓ MẶT trong mọi khóa tối thiểu; Nhóm R KHÔNG BAO GIỜ có mặt trong bất kỳ khóa tối thiểu nào",
        "Thuật toán duyệt tổ hợp để tìm TẤT CẢ các khóa ứng viên mà không bị sót"
      ],
      remind: "Đây là câu hỏi tự luận chiếm 2 điểm trong đề thi UET. Hãy xem kỹ Slide C4_1 trang 54–56 về bảng phân loại L, R, B, N."
    },
    desc: "Làm chủ thuật toán phân loại thuộc tính L, R, B, N để tìm chính xác và đầy đủ tất cả các khóa tối thiểu của lược đồ quan hệ trong vài phút.",
    steps: [
      {
        t: "Định nghĩa Siêu khóa và Khóa tối thiểu",
        c: `<p>Cho lược đồ quan hệ $R(A_1, A_2, \\dots, A_n)$ và tập phụ thuộc hàm $F$:</p>
            <ul>
              <li><b>Siêu khóa (Superkey - $K$)</b>: Là tập thuộc tính $K \\subseteq R$ có bao đóng phủ kín toàn bộ thuộc tính của lược đồ:
                $$K^+_F = R$$
              </li>
              <li><b>Khóa tối thiểu / Khóa ứng viên (Candidate Key - $K$)</b>: Là một siêu khóa mà không chứa bất kỳ tập con thực sự nào cũng là siêu khóa:
                $$K^+ = R \\quad \\text{và} \\quad \\forall X \\subset K: X^+ \\neq R$$
              </li>
            </ul>`
      },
      {
        t: "Kỹ thuật Phân loại 4 nhóm thuộc tính L, R, B, N",
        c: `<p>Để không phải duyệt thử vu vơ $2^n$ tập con, ta chia tập thuộc tính của $R$ thành <b>4 nhóm chiến lược</b> dựa vào vị trí xuất hiện trong các phụ thuộc hàm của $F$:</p>
            <table class="data-table">
              <thead><tr><th>Nhóm</th><th>Định nghĩa vị trí</th><th>Quy tắc đối với Khóa tối thiểu</th></tr></thead>
              <tbody>
                <tr><td><b>Nhóm L (Left)</b></td><td>Thuộc tính <b>chỉ xuất hiện ở vế Trái</b> của các FD trong $F$.</td><td><b>BẮT BUỘC PHẢI CÓ MẶT</b> trong MỌI khóa tối thiểu.</td></tr>
                <tr><td><b>Nhóm N (None)</b></td><td>Thuộc tính <b>hoàn toàn không xuất hiện</b> ở vế nào trong $F$.</td><td><b>BẮT BUỘC PHẢI CÓ MẶT</b> trong MỌI khóa tối thiểu.</td></tr>
                <tr><td><b>Nhóm R (Right)</b></td><td>Thuộc tính <b>chỉ xuất hiện ở vế Phải</b> của các FD trong $F$.</td><td><b>KHÔNG BAO GIỜ</b> xuất hiện trong bất kỳ khóa tối thiểu nào. (Loại bỏ ngay!).</td></tr>
                <tr><td><b>Nhóm B (Both)</b></td><td>Thuộc tính <b>xuất hiện ở cả hai vế</b> trong $F$.</td><td>Có thể có mặt hoặc không có mặt trong khóa (Cần thử nghiệm kết hợp).</td></tr>
              </tbody>
            </table>
            <div class="tip-box">
              <b>Quy trình tìm khóa 3 bước thần tốc:</b><br>
              1. <b>Bước 1:</b> Đặt $X_0 = L \\cup N$. Tính bao đóng $X_0^+$.<br>
                 - Nếu $X_0^+ = R$, thì $X_0$ chính là <b>Khóa tối thiểu duy nhất</b> của lược đồ (Dừng lại ngay, không cần xét thêm gì nữa!).<br>
              2. <b>Bước 2:</b> Nếu $X_0^+ \\neq R$, ta lần lượt kết hợp $X_0$ với các tập con của nhóm $B$ theo thứ tự tăng dần về số lượng phần tử (tập 1 phần tử, 2 phần tử...).<br>
              3. <b>Bước 3:</b> Với mỗi tổ hợp $K = X_0 \\cup B_i$, nếu $K^+ = R$ và không chứa bất kỳ khóa nào đã tìm thấy trước đó, thì $K$ là một Khóa tối thiểu mới.
            </div>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide C4_1 — Slide 54] Tìm Khóa Duy nhất khi (L ∪ N)+ = R",
        q: "Cho lược đồ quan hệ $R(A, B, C, D, E)$ với tập phụ thuộc hàm $F = \\{ A \\to B, \\; B \\to C, \\; C \\to D, \\; D \\to E \\}$. Hãy tìm tất cả các khóa tối thiểu của $R$.",
        sol: "<b>Áp dụng kỹ thuật phân loại L, R, B, N:</b><br>" +
             "- Vế trái: $\\\\{A, B, C, D\\\\}$; Vế phải: $\\\\{B, C, D, E\\\\}$.<br>" +
             "- Phân loại:<br>" +
             "  + Nhóm $L$ (chỉ ở vế trái): $\\\\{A\\\\}$.<br>" +
             "  + Nhóm $R$ (chỉ ở vế phải): $\\\\{E\\\\}$.<br>" +
             "  + Nhóm $B$ (ở cả hai vế): $\\\\{B, C, D\\\\}$.<br>" +
             "  + Nhóm $N$ (không có mặt): $\\\\emptyset$.<br>" +
             "- Xét $X_0 = L \\cup N = \\\\{A\\\\}$:<br>" +
             "  + Tính $A^+$: $A^+ = \\\\{A, B, C, D, E\\\\} = R$.<br>" +
             "$$\\\\mathbf{\\\\implies R \\\\text{ có đúng 1 khóa tối thiểu duy nhất là: } K = \\\\{A\\\\}}$$"
      },
      {
        level: "Trung bình",
        t: "[Slide C4_1 — Slide 55] Tìm Nhiều Khóa Ứng viên khi kết hợp với nhóm B",
        q: "Cho lược đồ $R(A, B, C, D, E, G)$ với tập phụ thuộc hàm $F = \\{ AB \\to C, \\; C \\to D, \\; D \\to B, \\; D \\to E, \\; E \\to G \\}$. Hãy tìm tất cả các khóa tối thiểu của $R$.",
        sol: "<b>Phân tích từng bước:</b><br>" +
             "1. Phân loại thuộc tính:<br>" +
             "   - Vế trái: $\\\\{A, B, C, D, E\\\\}$; Vế phải: $\\\\{B, C, D, E, G\\\\}$.<br>" +
             "   - $L = \\\\{A\\\\}$; $R = \\\\{G\\\\}$; $B = \\\\{B, C, D, E\\\\}$; $N = \\\\emptyset$.<br>" +
             "   - $X_0 = L \\cup N = \\\\{A\\\\}$. Tính $A^+ = \\\\{A\\\\} \\neq R$.<br>" +
             "2. Lần lượt kết hợp $A$ với từng thuộc tính của $B = \\\\{B, C, D, E\\\\}$:<br>" +
             "   - Thử $K_1 = \\\\{A, B\\\\}$: $\\\\{AB\\\\}^+ = \\\\{A, B, C, D, E, G\\\\} = R \\implies \\\\mathbf{K_1 = \\\\{AB\\\\}}$ là khóa.<br>" +
             "   - Thử $K_2 = \\\\{A, C\\\\}$: $\\\\{AC\\\\}^+ = \\\\{A, C, D, B, E, G\\\\} = R \\implies \\\\mathbf{K_2 = \\\\{AC\\\\}}$ là khóa.<br>" +
             "   - Thử $K_3 = \\\\{A, D\\\\}$: $\\\\{AD\\\\}^+ = \\\\{A, D, B, E, G, C\\\\} = R \\implies \\\\mathbf{K_3 = \\\\{AD\\\\}}$ là khóa.<br>" +
             "   - Thử $K_4 = \\\\{A, E\\\\}$: $\\\\{AE\\\\}^+ = \\\\{A, E, G\\\\} \\neq R$ (chưa đủ).<br>" +
             "3. Thử kết hợp 2 thuộc tính từ $B$ đi kèm $A$ (loại trừ các tập chứa $K_1, K_2, K_3$): Chỉ còn xét $\\\\{A, E, B\\\\}$ (chứa AB), $\\\\{A, E, C\\\\}$ (chứa AC), $\\\\{A, E, D\\\\}$ (chứa AD). Không còn tập nào độc lập.<br>" +
             "$$\\\\mathbf{\\\\text{Kết luận: Lược đồ có đúng 3 khóa tối thiểu là: } K_1 = \\\\{AB\\\\}, \\; K_2 = \\\\{AC\\\\}, \\; K_3 = \\\\{AD\\\\}}$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide C4_1 — Slide 93] Đề thi UET: Xác định Khóa và Thuộc tính Khóa của Lược đồ 10 Thuộc tính",
        q: "Bài tập đề thi UET (Slide C4_1 trang 93): Cho lược đồ $R(A, B, C, D, E, F, G, H, I, J)$ với tập phụ thuộc hàm:<br>" +
           "$$F = \\{ AB \\to C, \\; BD \\to EF, \\; AD \\to GH, \\; A \\to I, \\; H \\to J \\}$$<br>" +
           "Hãy tìm tất cả các khóa tối thiểu của $R$ và liệt kê tập thuộc tính khóa, thuộc tính không khóa.",
        sol: "<b>Giải bài toán thi bằng phương pháp phân loại chuẩn:</b><br>" +
             "1. Phân loại thuộc tính trong $R$:<br>" +
             "   - Xuất hiện vế trái: $\\\\{A, B, D, H\\\\}$.<br>" +
             "   - Xuất hiện vế phải: $\\\\{C, E, F, G, H, I, J\\\\}$.<br>" +
             "   - Nhóm $L$ (chỉ xuất hiện bên trái): $\\\\{A, B, D\\\\}$.<br>" +
             "   - Nhóm $R$ (chỉ xuất hiện bên phải): $\\\\{C, E, F, G, I, J\\\\}$.<br>" +
             "   - Nhóm $B$ (xuất hiện cả 2 bên): $\\\\{H\\\\}$.<br>" +
             "   - Nhóm $N$ (không xuất hiện vế nào): $\\\\emptyset$.<br>" +
             "2. Xét tập bắt buộc $X_0 = L \\cup N = \\\\{A, B, D\\\\}$:<br>" +
             "   - Tính $\\\\{ABD\\\\}^+$:<br>" +
             "     + Bắt đầu: $\\\\{A, B, D\\\\}$.<br>" +
             "     + $AB \\to C \\implies \\\\{A, B, D, C\\\\}$.<br>" +
             "     + $BD \\to EF \\implies \\\\{A, B, D, C, E, F\\\\}$.<br>" +
             "     + $AD \\to GH \\implies \\\\{A, B, D, C, E, F, G, H\\\\}$.<br>" +
             "     + $A \\to I \\implies \\\\{A, B, D, C, E, F, G, H, I\\\\}$.<br>" +
             "     + $H \\to J \\implies \\\\{A, B, D, C, E, F, G, H, I, J\\\\} = R$.<br>" +
             "3. <b>Kết luận:</b><br>" +
             "   - Vì $X_0^+ = R$ nên $R$ có <b>đúng 1 khóa tối thiểu duy nhất là: $K = \\\\{A, B, D\\\\}$</b>.<br>" +
             "   - <b>Tập thuộc tính khóa (Prime):</b> $\\\\{A, B, D\\\\}$.<br>" +
             "   - <b>Tập thuộc tính không khóa (Non-prime):</b> $\\\\{C, E, F, G, H, I, J\\\\}$."
      }
    ],
    pitfalls: [
      {
        bad: "Bỏ quên nhóm N (các thuộc tính không xuất hiện ở vế nào của các phụ thuộc hàm) khi tìm khóa.",
        good: "Các thuộc tính thuộc nhóm N không bao giờ được sinh ra bởi bất kỳ thuộc tính nào khác, do đó chúng BẮT BUỘC PHẢI CÓ MẶT trong tất cả các khóa tối thiểu!"
      },
      {
        bad: "Thấy K+ = R thì vội vàng kết luận ngay K là khóa tối thiểu.",
        good: "K+ = R mới chỉ chứng minh K là Siêu khóa. Bạn phải kiểm tra thêm điều kiện tối thiểu: Không có tập con thực sự nào của K có bao đóng bằng R."
      }
    ],
    quizzes: [
      {
        level: "Nhận biết",
        badge: "🟢 Cấp độ 1: Nhận biết",
        q: "Thuộc tính chỉ xuất hiện ở vế PHẢI của các phụ thuộc hàm (nhóm R) có đặc điểm gì đối với khóa tối thiểu?",
        opts: [
          "Bắt buộc phải có mặt trong mọi khóa tối thiểu",
          "Không bao giờ xuất hiện trong bất kỳ khóa tối thiểu nào",
          "Chỉ xuất hiện khi khóa có từ 3 thuộc tính trở lên",
          "Luôn là khóa chính"
        ],
        ans: 1,
        fb: "Chính xác! Thuộc tính thuộc nhóm R luôn được suy ra từ các thuộc tính khác, nên việc đưa nó vào khóa sẽ làm mất tính tối thiểu. Vì vậy nhóm R không bao giờ thuộc khóa."
      },
      {
        level: "Thông hiểu",
        badge: "🟡 Cấp độ 2: Thông hiểu",
        q: "Cho lược đồ $R(A, B, C, D)$ với $F = \\{ A \\to B, \\; B \\to C \\}$. Thuộc tính $D$ không xuất hiện trong bất kỳ phụ thuộc hàm nào của $F$. Nhận định nào sau đây là ĐÚNG?",
        opts: [
          "$D$ không thể tham gia vào khóa",
          "$D$ bắt buộc phải có mặt trong tất cả các khóa tối thiểu của $R$",
          "Khóa của $R$ chỉ có thể là $\\{A\\}$",
          "Lược đồ $R$ không có khóa"
        ],
        ans: 1,
        fb: "Đúng! Thuộc tính $D$ thuộc nhóm $N$ (None), không thể được sinh ra từ bất kỳ thuộc tính nào, do đó mọi khóa của $R$ đều bắt buộc phải chứa $D$."
      },
      {
        level: "Vận dụng",
        badge: "🔴 Cấp độ 3: Vận dụng & Bẫy",
        q: "Cho lược đồ $R(A, B, C, D)$ với $F = \\{ AB \\to CD, \\; C \\to A, \\; D \\to B \\}$. Số lượng khóa ứng viên (tối thiểu) của $R$ là:",
        opts: [
          "1 khóa",
          "2 khóa",
          "3 khóa",
          "4 khóa"
        ],
        ans: 3,
        fb: "Rất xuất sắc! Lược đồ này có đúng 4 khóa tối thiểu là: {AB}, {BC}, {CD}, {AD}."
      }
    ]
  },

  {
    id: "CSDL_13",
    cluster: "4",
    title: "Các Dạng chuẩn dữ liệu: 1NF, 2NF, 3NF và BCNF",
    sources: "Slide UET.IS2099 Chương 4 (Slide 61–78)",
    ref: {
      slide_file: "C4_1.pptx",
      slide_name: "Chương 4 — Phụ thuộc hàm và Chuẩn hóa CSDL",
      pages: "Slide 61 – 78",
      page_start: 61,
      page_end: 78,
      section: "Mục 4.10: Các dạng chuẩn dựa trên khóa chính; 1NF, 2NF, 3NF và Dạng chuẩn Boyce-Codd (BCNF)",
      key_points: [
        "Phụ thuộc hàm đầy đủ (Full FD) vs Phụ thuộc bộ phận (Partial FD)",
        "Phụ thuộc bắc cầu (Transitive FD): X -> Y và Y -> A (với Y không phải siêu khóa)",
        "Dạng chuẩn 1 (1NF): Mọi giá trị thuộc tính phải là nguyên tử (Atomic), không có thuộc tính đa trị/phức hợp",
        "Dạng chuẩn 2 (2NF): Đạt 1NF và KHÔNG CÓ thuộc tính không khóa nào phụ thuộc bộ phận vào một phần của khóa",
        "Dạng chuẩn 3 (3NF): Đạt 2NF và KHÔNG CÓ thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa chính (mọi X -> A thì X là siêu khóa hoặc A là thuộc tính khóa)",
        "Dạng chuẩn Boyce-Codd (BCNF): Đạt 1NF và với mọi FD không tầm thường X -> A thì X BẮT BUỘC PHẢI LÀ SIÊU KHÓA"
      ],
      remind: "Kiểm tra dạng chuẩn là câu hỏi cốt lõi của đề thi. Hãy mở Slide C4_1 trang 68–78 để đối chiếu định nghĩa 2NF, 3NF và BCNF."
    },
    desc: "Nắm vững tiêu chuẩn phân loại và thuật toán kiểm tra từng dạng chuẩn: 1NF, 2NF, 3NF và BCNF để xử lý trọn vẹn câu hỏi lý thuyết lẫn bài tập tính toán.",
    steps: [
      {
        t: "Khái niệm Phụ thuộc Đầy đủ, Bộ phận & Bắc cầu",
        c: `<p>Để hiểu các dạng chuẩn, trước hết ta phải phân loại mối quan hệ giữa thuộc tính không khóa và khóa chính:</p>
            <ul>
              <li><b>Phụ thuộc hàm đầy đủ (Full Functional Dependency)</b>: Thuộc tính $Y$ phụ thuộc đầy đủ vào $X$ nếu $X \\to Y$ và việc loại bỏ bất kỳ thuộc tính nào khỏi $X$ đều làm phụ thuộc hàm không còn đúng nữa (nghĩa là không có $Z \\subset X$ sao cho $Z \\to Y$).</li>
              <li><b>Phụ thuộc hàm bộ phận (Partial Dependency)</b>: Thuộc tính $Y$ phụ thuộc bộ phận vào $X$ nếu tồn tại một tập con thực sự $Z \\subset X$ sao cho $Z \\to Y$. (Nghĩa là $Y$ chỉ cần một phần của khóa là đã xác định được rồi!).</li>
              <li><b>Phụ thuộc bắc cầu (Transitive Dependency)</b>: Một thuộc tính không khóa $Z$ phụ thuộc bắc cầu vào khóa chính $X$ nếu tồn tại tập thuộc tính $Y$ sao cho $X \\to Y$, $Y \\to Z$, nhưng $Y$ không phải là siêu khóa và $Z$ không thuộc $Y$.</li>
            </ul>`
      },
      {
        t: "Bảng Đối chiếu Tiêu chuẩn 4 Dạng chuẩn (1NF -> BCNF)",
        c: `<table class="data-table">
              <thead><tr><th>Dạng chuẩn</th><th>Điều kiện bắt buộc</th><th>Dấu hiệu vi phạm phổ biến</th></tr></thead>
              <tbody>
                <tr>
                  <td><b>1NF (Dạng chuẩn 1)</b></td>
                  <td>Tất cả các giá trị thuộc tính đều phải là <b>nguyên tử (Atomic)</b>; không chứa thuộc tính đa trị, thuộc tính phức hợp hay lặp nhóm.</td>
                  <td>Một ô chứa danh sách nhiều số điện thoại ngăn cách bằng dấu phẩy; hoặc cột Địa chỉ gộp chung số nhà, đường, quận.</td>
                </tr>
                <tr>
                  <td><b>2NF (Dạng chuẩn 2)</b></td>
                  <td>Đạt 1NF <b>VÀ</b> mọi thuộc tính không khóa phải <b>phụ thuộc đầy đủ vào khóa chính</b> (không phụ thuộc bộ phận).<br><i>(Lưu ý: Nếu mọi khóa của quan hệ chỉ gồm đúng 1 thuộc tính đơn thì bảng tự động đạt 2NF!).</i></td>
                  <td>Khóa chính là $\\{A, B\\}$ nhưng lại có phụ thuộc hàm $A \\to C$ (với $C$ là thuộc tính không khóa).</td>
                </tr>
                <tr>
                  <td><b>3NF (Dạng chuẩn 3)</b></td>
                  <td>Đạt 2NF <b>VÀ</b> không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa chính.<br><b>Quy tắc kiểm tra nhanh:</b> Với mọi phụ thuộc hàm không tầm thường $X \\to A$, bắt buộc phải thỏa mãn ít nhất một trong 2 điều kiện:
                    <ol>
                      <li>$X$ là một <b>Siêu khóa</b>, HOẶC</li>
                      <li>$A$ là một <b>Thuộc tính khóa (Prime attribute)</b>.</li>
                    </ol>
                  </td>
                  <td>Tồn tại $X \\to A$ trong đó $X$ không phải siêu khóa và $A$ là thuộc tính không khóa (ví dụ: $MaPB \\to TenPB$ trong bảng Nhân viên).</td>
                </tr>
                <tr>
                  <td><b>BCNF (Boyce-Codd)</b></td>
                  <td>Đạt 1NF <b>VÀ</b> với <b>mọi</b> phụ thuộc hàm không tầm thường $X \\to A$, $X$ <b>BẮT BUỘC PHẢI LÀ MỘT SIÊU KHÓA</b>.</td>
                  <td>Tồn tại phụ thuộc hàm $X \\to A$ trong đó $X$ không phải siêu khóa, kể cả khi $A$ là thuộc tính khóa! (BCNF nghiêm ngặt hơn 3NF).</td>
                </tr>
              </tbody>
            </table>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide C4_1 — Slide 70–73] Kiểm tra Dạng chuẩn 2 (2NF)",
        q: "Cho lược đồ `PHANCONG(`<u>`MaNV, MaDA`</u>`, SoGio, TenNV, TenDA)` có khóa chính là `(MaNV, MaDA)` với tập phụ thuộc hàm: $F = \\{ \\{MaNV, MaDA\\} \\to SoGio, \\; MaNV \\to TenNV, \\; MaDA \\to TenDA \\}$. Lược đồ này có đạt 2NF không? Tại sao?",
        sol: "<b>Phân tích kiểm tra 2NF:</b><br>" +
             "- Khóa chính: $\\\\{MaNV, MaDA\\\\}$.<br>" +
             "- Thuộc tính không khóa: $\\\\{SoGio, TenNV, TenDA\\\\}$.<br>" +
             "- Xét các phụ thuộc hàm:<br>" +
             "  + $MaNV \\to TenNV$: Thuộc tính không khóa <code>TenNV</code> chỉ phụ thuộc vào một phần của khóa chính (<code>MaNV</code>) $\\\\rightarrow$ <b>Phụ thuộc bộ phận</b>.<br>" +
             "  + $MaDA \\to TenDA$: Thuộc tính không khóa <code>TenDA</code> chỉ phụ thuộc vào <code>MaDA</code> $\\\\rightarrow$ <b>Phụ thuộc bộ phận</b>.<br>" +
             "$$\\\\mathbf{\\\\implies PHANCONG \\\\text{ VI PHẠM 2NF (chỉ đạt 1NF)!}}$$"
      },
      {
        level: "Trung bình",
        t: "[Slide C4_1 — Slide 77–80] Kiểm tra Dạng chuẩn 3 (3NF)",
        q: "Cho lược đồ `NHANVIEN(`<u>`MaNV`</u>`, HoTen, MaPB, TenPB, TruongPhong)` có khóa chính là `MaNV`. Tập phụ thuộc hàm là $F = \\{ MaNV \\to \\{HoTen, MaPB\\}, \\; MaPB \\to \\{TenPB, TruongPhong\\} \\}$. Lược đồ đạt dạng chuẩn mấy?",
        sol: "<b>Kiểm tra từng dạng chuẩn:</b><br>" +
             "1. Khóa chính là thuộc tính đơn <code>MaNV</code> $\\\\implies$ Không thể có phụ thuộc bộ phận $\\\\implies$ <b>Đạt 2NF</b>.<br>" +
             "2. Xét phụ thuộc hàm $MaPB \\to TenPB$:<br>" +
             "   - Vế trái $MaPB$ có phải siêu khóa không? $(MaPB)^+ = \\\\{MaPB, TenPB, TruongPhong\\\\} \\neq R \\implies$ <b>KHÔNG phải siêu khóa</b>.<br>" +
             "   - Vế phải $TenPB$ có phải thuộc tính khóa không? Khóa chỉ có $MaNV$, nên $TenPB$ là <b>thuộc tính không khóa</b>.<br>" +
             "   $\\rightarrow$ Cả hai điều kiện của 3NF đều bị vi phạm (đây là phụ thuộc bắc cầu qua $MaPB$).<br>" +
             "$$\\\\mathbf{\\\\implies NHANVIEN \\\\text{ VI PHẠM 3NF (chỉ đạt dạng chuẩn 2NF)!}}$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide C4_1 — Slide 86–88] Phân biệt 3NF và BCNF qua Ví dụ Kinh điển",
        q: "Ví dụ Slide C4_1 trang 87: Cho lược đồ $R(A, B, C)$ với tập phụ thuộc hàm $F = \\{ AB \\to C, \\; C \\to B \\}$.<br>" +
           "a) Tìm tất cả các khóa tối thiểu của $R$.<br>" +
           "b) Lược đồ $R$ đạt dạng chuẩn 3NF không? Có đạt BCNF không? Tại sao?",
        sol: "<b>Phân tích chi tiết:</b><br>" +
             "a) Tìm khóa:<br>" +
             "   - $(AB)^+ = \\\\{A, B, C\\\\} \\implies K_1 = \\\\{AB\\\\}$.<br>" +
             "   - Vì $C \\to B \\implies (AC)^+ = \\\\{A, C, B\\\\} \\implies K_2 = \\\\{AC\\\\}$.<br>" +
             "   - Thuộc tính khóa: $\\\\{A, B, C\\\\}$ (mọi thuộc tính đều là thuộc tính khóa!). Không có thuộc tính không khóa nào.<br>" +
             "b) Kiểm tra dạng chuẩn:<br>" +
             "   - <b>Kiểm tra 3NF:</b> Xét $C \\to B$. Vế phải $B$ là một <b>thuộc tính khóa</b> $\\\\implies$ Thỏa mãn điều kiện 2 của 3NF. Do đó $R$ <b>ĐẠT DẠNG CHUẨN 3NF</b>.<br>" +
             "   - <b>Kiểm tra BCNF:</b> Xét $C \\to B$. BCNF bắt buộc vế trái $C$ phải là siêu khóa. Nhưng $C^+ = \\\\{B, C\\\\} \\neq R$ ($C$ không phải siêu khóa!).<br>" +
             "$$\\\\mathbf{\\\\implies R \\\\text{ ĐẠT 3NF NHƯNG VI PHẠM BCNF!}}$$"
      }
    ],
    pitfalls: [
      {
        bad: "Nghĩ rằng nếu bảng đạt 3NF thì chắc chắn cũng đạt BCNF.",
        good: "BCNF khắt khe hơn 3NF. Khi một bảng có nhiều khóa ứng viên chồng chéo nhau (như AB và AC), bảng có thể đạt 3NF nhờ vế phải là thuộc tính khóa, nhưng vẫn vi phạm BCNF vì vế trái không phải siêu khóa!"
      },
      {
        bad: "Kiểm tra 2NF khi khóa chính chỉ có 1 thuộc tính đơn lẻ.",
        good: "Nếu mọi khóa ứng viên của bảng đều là thuộc tính đơn lẻ (như MaSV, MaNV), thì bảng đó KHÔNG THỂ CÓ phụ thuộc bộ phận, do đó tự động đạt 2NF ngay lập tức mà không cần kiểm tra!"
      }
    ],
    quizzes: [
      {
        level: "Nhận biết",
        badge: "🟢 Cấp độ 1: Nhận biết",
        q: "Điều kiện cần và đủ để một lược đồ quan hệ đạt Dạng chuẩn 2 (2NF) là:",
        opts: [
          "Không có bất kỳ giá trị NULL nào trong bảng",
          "Đạt 1NF và mọi thuộc tính không khóa phải phụ thuộc hàm đầy đủ vào khóa chính",
          "Tất cả các thuộc tính đều phải là khóa",
          "Phải có ít nhất hai khóa ngoại"
        ],
        ans: 1,
        fb: "Chính xác! 2NF nghiêm cấm phụ thuộc bộ phận: mọi thuộc tính không khóa bắt buộc phải phụ thuộc đầy đủ vào toàn bộ khóa chính."
      },
      {
        level: "Thông hiểu",
        badge: "🟡 Cấp độ 2: Thông hiểu",
        q: "Trong lược đồ $R(A, B, C, D)$ có khóa duy nhất là $A$. Có phụ thuộc hàm $B \\to C$ (với $B, C$ là thuộc tính không khóa). Lược đồ này vi phạm dạng chuẩn nào?",
        opts: [
          "Vi phạm 1NF",
          "Vi phạm 2NF",
          "Đạt 2NF nhưng vi phạm 3NF (do có phụ thuộc bắc cầu)",
          "Đạt chuẩn BCNF"
        ],
        ans: 2,
        fb: "Đúng! Khóa là thuộc tính đơn $A$ nên tự động đạt 2NF. Tuy nhiên có $A \\to B$ và $B \\to C$ nên $C$ phụ thuộc bắc cầu vào khóa, do đó vi phạm 3NF."
      },
      {
        level: "Vận dụng",
        badge: "🔴 Cấp độ 3: Vận dụng & Bẫy",
        q: "Một lược đồ quan hệ có 100% các thuộc tính đều là Thuộc tính khóa (Prime attributes). Lược đồ này CHẮC CHẮN đạt dạng chuẩn nào sau đây?",
        opts: [
          "Chắc chắn đạt BCNF",
          "Chắc chắn đạt 3NF (và 2NF, 1NF)",
          "Chỉ chắc chắn đạt 1NF",
          "Không thể xác định được nếu không biết dữ liệu"
        ],
        ans: 1,
        fb: "Rất xuất sắc! Vì mọi thuộc tính đều là thuộc tính khóa, nên trong mọi phụ thuộc hàm $X \\to A$, vế phải $A$ luôn là thuộc tính khóa (thỏa mãn điều kiện thứ 2 của 3NF). Do đó bảng tự động đạt 3NF!"
      }
    ]
  },

  {
    id: "CSDL_14",
    cluster: "4",
    title: "Lý thuyết Phân rã: Bảo toàn thông tin, Bảo toàn phụ thuộc hàm",
    sources: "Slide UET.IS2099 Chương 4 (Slide 79–96)",
    ref: {
      slide_file: "C4_1.pptx",
      slide_name: "Chương 4 — Phụ thuộc hàm và Chuẩn hóa CSDL",
      pages: "Slide 79 – 96",
      page_start: 79,
      page_end: 96,
      section: "Mục 4.11: Phân rã bảo toàn thông tin (Lossless-join); Mục 4.12: Bảo toàn phụ thuộc hàm; Thuật toán phân rã về 3NF và BCNF",
      key_points: [
        "Mục tiêu của Phân rã (Decomposition): Tách bảng vi phạm chuẩn thành các bảng nhỏ hơn đạt chuẩn cao hơn",
        "Định lý Phân rã Bảo toàn thông tin cho 2 quan hệ (R1, R2): (R1 ∩ R2 -> R1) hoặc (R1 ∩ R2 -> R2) phải thuộc F+",
        "Bảo toàn phụ thuộc hàm (Dependency Preservation): (F1 ∪ F2)+ = F+",
        "Thuật toán phân rã về 3NF: Vừa bảo toàn thông tin, vừa bảo toàn phụ thuộc hàm",
        "Thuật toán phân rã về BCNF: Bảo toàn thông tin nhưng CÓ THỂ KHÔNG bảo toàn phụ thuộc hàm"
      ],
      remind: "Đây là câu hỏi phân loại 9–10 điểm trong đề thi UET. Hãy xem kỹ Slide C4_1 trang 80–85 về định lý kiểm tra bảo toàn thông tin cho 2 quan hệ."
    },
    desc: "Làm chủ 2 tính chất sống còn của phân rã: Bảo toàn thông tin và Bảo toàn phụ thuộc hàm, thực hành trọn vẹn thuật toán chuẩn hóa về 3NF và BCNF.",
    steps: [
      {
        t: "Tại sao Phân rã phải Bảo toàn Thông tin (Lossless Join)?",
        c: `<p>Khi một bảng quan hệ $R$ vi phạm dạng chuẩn, giải pháp là <b>Phân rã (Decompose)</b> $R$ thành các lược đồ con $R_1, R_2, \\dots, R_k$ sao cho $R = R_1 \\cup R_2 \\cup \\dots \\cup R_k$.</p>
            <div class="warn-box">
              <b>CẠM BẪY CHÍ MẠNG: Kết nối Mất mát (Lossy Join)!</b><br>
              Nếu phân rã tùy tiện không đúng khoa học, khi ta kết nối tự nhiên các bảng con lại ($R_1 \\bowtie R_2 \\dots$), kết quả sẽ <b>sinh ra các bản ghi giả (Spurious Tuples)</b> không hề có trong thực tế! Dữ liệu bị sai lệch hoàn toàn.<br>
              Vì vậy, phép phân rã bắt buộc phải là <b>Phân rã Kết nối Không mất thông tin (Lossless-Join Decomposition)</b>:
              $$R = R_1 \\bowtie R_2 \\bowtie \\dots \\bowtie R_k$$
            </div>`
      },
      {
        t: "Định lý Kiểm tra Bảo toàn Thông tin cho 2 Quan hệ",
        c: `<p>Trong bài thi UET, trường hợp phân rã $R$ thành hai quan hệ $R_1$ và $R_2$ được kiểm tra cực nhanh bằng định lý sau:</p>
            <div class="tip-box">
              <b>Định lý (Slide C4_1 tr. 81):</b><br>
              Phép phân rã $\\rho = \\{R_1, R_2\\}$ của lược đồ $R$ với tập phụ thuộc hàm $F$ là <b>bảo toàn thông tin</b> khi và chỉ khi phần giao của hai quan hệ xác định hàm ít nhất một trong hai quan hệ:
              $$(R_1 \\cap R_2) \\to R_1 \\in F^+ \\quad \\text{HOẶC} \\quad (R_1 \\cap R_2) \\to R_2 \\in F^+$$
              <i>(Nghĩa là: Thuộc tính chung giữa hai bảng bắt buộc phải là một Siêu khóa của ít nhất một trong hai bảng con!).</i>
            </div>`
      },
      {
        t: "Thuật toán Phân rã về 3NF & BCNF",
        c: `<p>Sự khác biệt cốt lõi giữa 3NF và BCNF khi chuẩn hóa:</p>
            <table class="data-table">
              <thead><tr><th>Tiêu chí so sánh</th><th>Chuẩn hóa về 3NF</th><th>Chuẩn hóa về BCNF</th></tr></thead>
              <tbody>
                <tr><td><b>Bảo toàn thông tin (Lossless)</b></td><td><b>LUÔN LUÔN</b> đạt được.</td><td><b>LUÔN LUÔN</b> đạt được.</td></tr>
                <tr><td><b>Bảo toàn phụ thuộc hàm (Preservation)</b></td><td><b>LUÔN LUÔN</b> bảo toàn được 100% phụ thuộc hàm.</td><td><b>CÓ THỂ BỊ MẤT</b> phụ thuộc hàm!</td></tr>
                <tr><td><b>Độ dư thừa dữ liệu</b></td><td>Còn một lượng nhỏ dư thừa (khi có phụ thuộc hàm giữa các khóa).</td><td>Loại bỏ sạch sẽ 100% dư thừa dữ liệu.</td></tr>
              </tbody>
            </table>`
      }
    ],
    examples: [
      {
        level: "Cơ bản",
        t: "[Slide C4_1 — Slide 81–83] Kiểm tra Phân rã Bảo toàn Thông tin cho 2 Bảng",
        q: "Cho $R(A, B, C)$ với $F = \\{ A \\to B \\}$. Xét phép phân rã $R$ thành $R_1(A, B)$ và $R_2(A, C)$. Phép phân rã này có bảo toàn thông tin (Lossless) không? Tại sao?",
        sol: "<b>Áp dụng định lý kiểm tra nhanh:</b><br>" +
             "1. Tìm phần giao thuộc tính: $R_1 \\cap R_2 = \\\\{A, B\\\\} \\cap \\\\{A, C\\\\} = \\\\{A\\\\}$.<br>" +
             "2. Kiểm tra xem giao có xác định hàm $R_1$ hoặc $R_2$ không:<br>" +
             "   - Ta có $A \\to B \\in F \\implies A \\to AB \\implies (R_1 \\cap R_2) \\to R_1$ thỏa mãn!<br>" +
             "$$\\\\mathbf{\\\\implies \\\\text{Phép phân rã này BẢO TOÀN THÔNG TIN (Lossless-join)!}}$$"
      },
      {
        level: "Trung bình",
        t: "[Slide C4_1 — Slide 84–85] Phát hiện Phân rã Mất mát Thông tin (Lossy)",
        q: "Cho $R(A, B, C)$ với $F = \\{ B \\to C \\}$. Xét phép phân rã $R$ thành $R_1(A, B)$ và $R_2(A, C)$. Phép phân rã này có bảo toàn thông tin không?",
        sol: "<b>Phân tích:</b><br>" +
             "1. Giao của hai quan hệ: $R_1 \\cap R_2 = \\\\{A\\\\}$.<br>" +
             "2. Kiểm tra bao đóng của giao: $A^+ = \\\\{A\\\\}$.<br>" +
             "   - $A^+ \\neq R_1$ (không xác định được B).<br>" +
             "   - $A^+ \\neq R_2$ (không xác định được C).<br>" +
             "$$\\\\mathbf{\\\\implies \\\\text{Phép phân rã BỊ MẤT MÁT THÔNG TIN (Lossy)! Khi JOIN lại sẽ sinh ra bản ghi giả!}}$$"
      },
      {
        level: "Vận dụng",
        t: "[Slide C4_1 — Slide 87–91] Thuật toán Phân rã BCNF cho Lược đồ R(A, B, C, D, E)",
        q: "Ví dụ Slide C4_1 trang 87: Cho $R(A, B, C, D, E)$ với $F = \\{ A \\to B, \\; BC \\to D \\}$. Khóa của $R$ là $\\{A, C, E\\}$. Hãy phân rã $R$ về dạng chuẩn BCNF bảo toàn thông tin.",
        sol: "<b>Thực hiện thuật toán phân rã BCNF:</b><br>" +
             "1. Xét phụ thuộc hàm $A \\to B$:<br>" +
             "   - Vế trái $A$ không phải siêu khóa của $R$ ($A^+ = \\\\{A, B\\\\} \\neq R$) $\\\\implies$ Vi phạm BCNF.<br>" +
             "   - Tách $R$ thành 2 bảng:<br>" +
             "     + $R_1 = A^+ = \\\\{A, B\\\\}$ (có khóa là $A$, đạt chuẩn BCNF).<br>" +
             "     + $R_2 = R - (A^+ - A) = \\\\{A, C, D, E\\\\}$.<br>" +
             "2. Xét tiếp $R_2(A, C, D, E)$ với phụ thuộc hàm chiếu trên $R_2$:<br>" +
             "   - Vì $A \\to B$ và $BC \\to D \\implies AC \\to D$.<br>" +
             "   - Phụ thuộc hàm $AC \\to D$ vi phạm BCNF trên $R_2$ (vì $(AC)^+ = \\\\{A, C, D\\\\} \\neq R_2$).<br>" +
             "   - Tách $R_2$ thành 2 bảng:<br>" +
             "     + $R_{21} = (AC)^+ = \\\\{A, C, D\\\\}$ (có khóa là $AC$, đạt chuẩn BCNF).<br>" +
             "     + $R_{22} = R_2 - (AC^+ - AC) = \\\\{A, C, E\\\\}$ (có khóa là $ACE$, đạt chuẩn BCNF).<br>" +
             "3. <b>Kết quả phân rã BCNF cuối cùng:</b><br>" +
             "$$\\\\mathbf{\\\\rho = \\\\{ R_1(\\underline{A}, B), \\; R_{21}(\\underline{A, C}, D), \\; R_{22}(\\underline{A, C, E}) \\}}$$<br>" +
             "Tất cả các bảng con đều đạt chuẩn BCNF và phép phân rã bảo toàn thông tin 100%!"
      }
    ],
    pitfalls: [
      {
        bad: "Nghĩ rằng thuật toán phân rã BCNF luôn luôn bảo toàn được mọi phụ thuộc hàm ban đầu.",
        good: "Đây là cái giá phải trả của BCNF! Đôi khi để triệt tiêu hoàn toàn dư thừa dữ liệu về BCNF, ta bắt buộc phải đánh đổi việc mất mát một số phụ thuộc hàm (trong khi chuẩn hóa về 3NF thì luôn bảo toàn được phụ thuộc hàm)."
      },
      {
        bad: "Sau khi phân rã, quên không kiểm tra xem bảng con còn lại có còn vi phạm dạng chuẩn nữa không.",
        good: "Thuật toán phân rã là một quy trình đệ quy: Sau khi tách bảng, phải tiếp tục kiểm tra từng bảng con cho tới khi tất cả các bảng con đều đạt chuẩn mới được dừng lại."
      }
    ],
    quizzes: [
      {
        level: "Nhận biết",
        badge: "🟢 Cấp độ 1: Nhận biết",
        q: "Thuật toán chuẩn hóa lược đồ quan hệ về dạng chuẩn 3NF có ưu điểm vượt trội nào so với BCNF?",
        opts: [
          "Loại bỏ được nhiều dữ liệu dư thừa hơn BCNF",
          "Luôn luôn vừa bảo toàn thông tin, vừa bảo toàn được 100% các phụ thuộc hàm ban đầu",
          "Không cần sử dụng đến phép chiếu",
          "Chỉ tạo ra tối đa 2 bảng con"
        ],
        ans: 1,
        fb: "Chính xác! Ưu thế cốt tử của 3NF là luôn luôn tồn tại thuật toán phân rã vừa bảo toàn thông tin (Lossless), vừa bảo toàn phụ thuộc hàm (Dependency Preservation)."
      },
      {
        level: "Thông hiểu",
        badge: "🟡 Cấp độ 2: Thông hiểu",
        q: "Cho lược đồ $R(A, B, C, D)$ phân rã thành hai bảng $R_1(A, B, C)$ và $R_2(C, D)$. Để phép phân rã này là bảo toàn thông tin (Lossless-join), điều kiện cần và đủ là:",
        opts: [
          "$C \\to A$ hoặc $C \\to B$",
          "$C \\to ABC$ hoặc $C \\to CD$ (nghĩa là $C$ là siêu khóa của ít nhất một trong hai bảng con)",
          "Bảng $R_1$ và $R_2$ phải có cùng số lượng hàng",
          "$C$ phải là khóa ngoại tham chiếu đến $D$"
        ],
        ans: 1,
        fb: "Đúng! Phần giao của hai bảng là {C}. Định lý yêu cầu giao {C} phải là siêu khóa của ít nhất một trong hai bảng (C -> ABC hoặc C -> CD)."
      },
      {
        level: "Vận dụng",
        badge: "🔴 Cấp độ 3: Vận dụng & Bẫy",
        q: "Hậu quả nghiêm trọng nhất của một phép phân rã 'Mất mát thông tin' (Lossy Join Decomposition) là gì?",
        opts: [
          "Làm mất bớt các dòng dữ liệu thật trong bảng",
          "Khi thực hiện kết nối tự nhiên các bảng con lại với nhau, kết quả sẽ sinh ra các bộ dữ liệu giả (Spurious tuples) làm sai lệch bản chất dữ liệu ban đầu",
          "Làm cho cơ sở dữ liệu bị đầy ổ cứng",
          "Không thể viết được câu lệnh SELECT"
        ],
        ans: 1,
        fb: "Rất chuẩn xác! Từ 'Lossy' không có nghĩa là mất dòng, mà là mất đi tính chính xác của thông tin do sinh ra thêm các bản ghi giả (Spurious tuples) khi kết nối lại!"
      }
    ]
  }
];

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { CUM_4_CSDL };
}
"""

with open('content_csdl/cum_4.js', 'w', encoding='utf-8') as f:
    f.write(cum_4_code)

print("Created content_csdl/cum_4.js successfully! Length:", len(cum_4_code))
