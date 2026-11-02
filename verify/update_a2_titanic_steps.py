import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("content/cum_a.js", "r", encoding="utf-8") as f:
    text = f.read()

titanic_steps = """      {
        t: "Hai biến phân loại: Bảng liên hợp 2 chiều (Contingency Table)",
        c: `<p>Muốn xem xét mối liên hệ giữa hai biến phân loại, bài giảng Slide Week 02 (trang 15–19) sử dụng <b>Bảng liên hợp thảm họa Titanic</b> (2.201 hành khách):</p>
            <table class="data-table">
              <thead><tr><th>Độ tuổi \\\\ Kết quả</th><th>Sống sót</th><th>Tử vong</th><th>Tổng hàng</th></tr></thead>
              <tbody>
                <tr><td><b>Người lớn</b></td><td>654</td><td>1.438</td><td><b>2.092</b></td></tr>
                <tr><td><b>Trẻ em</b></td><td>57</td><td>52</td><td><b>109</b></td></tr>
                <tr><td><b>Tổng cột</b></td><td><b>711</b></td><td><b>1.490</b></td><td><b>2.201</b></td></tr>
              </tbody>
            </table>
            <p>Trong bảng trên: Ô giao nhau cho biết tần số kết hợp (ví dụ: có $57$ hành khách là trẻ em và sống sót). Tổng hàng và tổng cột đều cộng ra tổng chung $n = 2.201$.</p>`
      },
      {
        t: "Kỹ năng sống còn: Chọn đúng MẪU SỐ khi tính tỉ lệ",
        c: `<p>Từ bảng liên hợp Titanic (Slide 21–22), bài thi thường yêu cầu tính 3 loại tỉ lệ khác nhau. Điểm mấu chốt là <b>xác định đúng MẪU SỐ</b>:</p>
            <ol>
              <li><b>Tỉ lệ trên toàn bộ (Joint Proportion)</b>: Mẫu số là <b>Tổng chung toàn bảng (2.201)</b>.<br>
                  Ví dụ: Tỉ lệ trẻ em sống sót trong toàn bộ hành khách = $\\\\frac{57}{2201} \\\\approx 2{,}59\\\\%$.
              </li>
              <li><b>Tỉ lệ có điều kiện theo hàng (Row Conditional)</b>: Mẫu số là <b>Tổng hàng</b>.<br>
                  Ví dụ: <i>Trong số trẻ em</i>, tỉ lệ sống sót = $\\\\frac{57}{109} \\\\approx 52{,}29\\\\%$.<br>
                  <i>Trong số người lớn</i>, tỉ lệ sống sót = $\\\\frac{654}{2092} \\\\approx 31{,}26\\\\%$.
              </li>
              <li><b>Tỉ lệ có điều kiện theo cột (Column Conditional)</b>: Mẫu số là <b>Tổng cột</b>.<br>
                  Ví dụ: <i>Trong số những người sống sót</i>, tỉ lệ trẻ em = $\\\\frac{57}{711} \\\\approx 8{,}02\\\\%$.
              </li>
            </ol>
            <div class="tip-box"><b>Mẹo tìm mẫu số trong câu hỏi:</b> Hãy tìm cụm từ <i>&quot;Trong số...&quot;</i> hoặc <i>&quot;Biết rằng...&quot;</i>. Đối tượng đứng ngay sau cụm từ đó chính là <b>MẪU SỐ</b>!</div>`
      },
      {
        t: "Làm thế nào để biết hai biến có liên hệ với nhau?",
        c: `<p>Hai biến phân loại được coi là <b>có mối liên hệ (associated)</b> nếu sự phân bố của biến này thay đổi khi ta biết thông tin về biến kia (Slide 23–26).</p>
            <p>Trong bảng Titanic, tỉ lệ sống sót của trẻ em ($52{,}29\\\\%$) cao hơn hẳn tỉ lệ sống sót của người lớn ($31{,}26\\\\%$). Sự khác biệt này cho thấy giữa <b>Độ tuổi</b> và <b>Kết quả sống sót</b> có mối liên hệ rõ rệt!</p>`
      }"""

p_steps = r'(\{\s*t:\s*["\']Hai biến phân loại: Bảng liên hợp 2 chiều \(Contingency Table\)["\'][\s\S]*?)(examples:\s*\[)'
text = re.sub(p_steps, lambda m: titanic_steps + "\n    ],\n    " + m.group(2), text)

with open("content/cum_a.js", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated A2 theory steps with Titanic dataset!")
