with open('verify/run_full_qa_suite.py', 'r', encoding='utf-8') as f:
    text = f.read()

old_code = """    sfile = r.get("slide_file")
    sfile_path = os.path.join(ROOT_DIR, sfile)
    test_assert(os.path.isfile(sfile_path), f"Slide file exists for {lid}: {sfile}")"""

new_code = """    sfile = r.get("slide_file")
    sfile_path = os.path.join(ROOT_DIR, sfile)
    if not os.path.isfile(sfile_path):
        sfile_path = os.path.join(ROOT_DIR, "tailieu_xstk", sfile)
    test_assert(os.path.isfile(sfile_path), f"Slide file exists for {lid}: {sfile}")"""

text = text.replace(old_code.replace('\r\n', '\n'), new_code.replace('\r\n', '\n'))
text = text.replace(old_code, new_code)

with open('verify/run_full_qa_suite.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Patched run_full_qa_suite.py!")
