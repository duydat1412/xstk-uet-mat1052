import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('verify/run_full_qa_suite.py', 'r', encoding='utf-8') as f:
    text = f.read()

suite_7 = """# ----------------------------------------------------------------------
# SUITE 7: Lesson References & Slide Lecture Cross-Referencing
# ----------------------------------------------------------------------
print("\\n[SUITE 7] Lesson References & Slide Lecture Cross-Referencing (26 Lessons)")
ref_path = os.path.join(CONTENT_DIR, "lesson_references.json")
test_assert(os.path.isfile(ref_path), "Reference database exists: content/lesson_references.json")
with open(ref_path, "r", encoding="utf-8") as f:
    refs_db = json.load(f)

test_assert(len(refs_db) == 26, f"All 26 lessons have slide reference entries (Found: {len(refs_db)})")

import fitz
for lid, r in refs_db.items():
    sfile = r.get("slide_file")
    sfile_path = os.path.join(ROOT_DIR, sfile)
    test_assert(os.path.isfile(sfile_path), f"Slide file exists for {lid}: {sfile}")
    doc = fitz.open(sfile_path)
    p_start = r.get("page_start", 0)
    test_assert(1 <= p_start <= len(doc), f"Lesson {lid} start page {p_start} is valid for {sfile} ({len(doc)} pages)")
    test_assert(len(r.get("section", "")) > 10, f"Lesson {lid} has descriptive section reference")
    test_assert(len(r.get("remind", "")) > 20, f"Lesson {lid} has study guidance when confused")
    test_assert(len(r.get("stat20", "")) > 5, f"Lesson {lid} has Stat20 textbook cross-reference")

# Check hoc.html UI integration for references
test_assert(".lesson-ref-box" in hoc_html, "Reference box CSS defined in hoc.html")
test_assert(".theory-ref-pill" in hoc_html, "Theory inline reference pill CSS defined in hoc.html")
test_assert('<div id="lessonRefBox">' in hoc_html, "HTML #lessonRefBox container present in hoc.html")
test_assert("function renderRefBox(" in hoc_html, "renderRefBox function defined in hoc.html")
test_assert("renderRefBox(l);" in hoc_html, "renderRefBox(l) called in renderCurrentLesson")

"""

target = """# ----------------------------------------------------------------------
# FINAL SUMMARY"""

if target in text:
    text = text.replace(target, suite_7 + target)
    print("Injected Suite 7 into run_full_qa_suite.py (LF)")
elif target.replace('\n', '\r\n') in text:
    text = text.replace(target.replace('\n', '\r\n'), suite_7.replace('\n', '\r\n') + target.replace('\n', '\r\n'))
    print("Injected Suite 7 into run_full_qa_suite.py (CRLF)")
else:
    print("Target not found!")

with open('verify/run_full_qa_suite.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated verify/run_full_qa_suite.py successfully.")
