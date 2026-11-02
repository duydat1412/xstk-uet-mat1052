import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('site/hoc.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = """      <div class="clt-info" id="cltInfo">Đang vẽ phân phối của biến ngẫu nhiên gốc X...</div>
    </div>`;
  }

  return html;
}"""

replacement = """      <div class="clt-info" id="cltInfo">Đang vẽ phân phối của biến ngẫu nhiên gốc X...</div>
    </div>`;
  }

  // Inline Reference Pill at the end of Theory
  if (l.ref) {
    html += `<div class="theory-ref-pill">
      <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;">
        <span>📌 <b>Tra cứu Slide bài giảng:</b> ${l.ref.slide_name} (<b>${l.ref.pages}</b>) — <i>${l.ref.section}</i></span>
      </div>
      <a href="/${l.ref.slide_file}#page=${l.ref.page_start}" target="_blank" class="mini-pdf-link" title="Mở trang ${l.ref.page_start} trong file ${l.ref.slide_file}">
        📄 Mở Slide PDF (${l.ref.slide_file}) ↗
      </a>
    </div>`;
  }

  return html;
}"""

# Normalize \r\n to match
if target in text:
    text = text.replace(target, replacement)
    print("Replaced with LF!")
elif target.replace('\n', '\r\n') in text:
    text = text.replace(target.replace('\n', '\r\n'), replacement.replace('\n', '\r\n'))
    print("Replaced with CRLF!")
else:
    print("Could not find target!")

# Also add ref hint to congrats box in renderQuiz
congrats_target = """      ${curLessonIdx < ALL_LESSONS.length - 1 ? `
        <button class="btn btn-primary" onclick="nextSection()" style="font-size:1rem;padding:10px 22px;">
          Tiếp tục sang bài tiếp theo (${ALL_LESSONS[curLessonIdx + 1].id}) →
        </button>
      ` : `
        <div style="display:inline-block;background:var(--ok);color:#fff;font-weight:700;padding:8px 18px;border-radius:999px;">
          🏆 Bạn đã hoàn thành toàn bộ 26 bài học trong chương trình!
        </div>
      `}
    </div>`;"""

congrats_replacement = """      ${l.ref ? `
        <div style="margin: 14px 0 16px; padding: 10px 14px; background: rgba(255,255,255,0.6); border: 1px dashed rgba(0,0,0,0.15); border-radius: 8px; font-size: .86rem; color: var(--text); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px;">
          <span>📌 <b>Muốn ôn luyện sâu hơn?</b> Tra cứu tại: <b>${l.ref.slide_name} (${l.ref.pages})</b></span>
          <a href="/${l.ref.slide_file}#page=${l.ref.page_start}" target="_blank" class="mini-pdf-link">
            📄 Mở Slide (${l.ref.slide_file}) ↗
          </a>
        </div>
      ` : ''}
      ${curLessonIdx < ALL_LESSONS.length - 1 ? `
        <button class="btn btn-primary" onclick="nextSection()" style="font-size:1rem;padding:10px 22px;">
          Tiếp tục sang bài tiếp theo (${ALL_LESSONS[curLessonIdx + 1].id}) →
        </button>
      ` : `
        <div style="display:inline-block;background:var(--ok);color:#fff;font-weight:700;padding:8px 18px;border-radius:999px;">
          🏆 Bạn đã hoàn thành toàn bộ 26 bài học trong chương trình!
        </div>
      `}
    </div>`;"""

if congrats_target in text:
    text = text.replace(congrats_target, congrats_replacement)
    print("Replaced congrats with LF!")
elif congrats_target.replace('\n', '\r\n') in text:
    text = text.replace(congrats_target.replace('\n', '\r\n'), congrats_replacement.replace('\n', '\r\n'))
    print("Replaced congrats with CRLF!")
else:
    print("Could not find congrats target!")

with open('site/hoc.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Finished updating site/hoc.html.")
