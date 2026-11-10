import json, fitz, os

for path, name in [('data/courses/xstk.json', 'xstk'), ('data/courses/csdl.json', 'csdl')]:
    with open(path, encoding='utf-8') as f:
        lessons = json.load(f)
    print(f"Checking {name}...")
    for l in lessons:
        ref = l.get('ref', {})
        sfile = ref.get('slide_file', '')
        if sfile.endswith('.pptx'):
            pdf_name = sfile.replace(' ', '').replace('.pptx', '.pdf')
        else:
            pdf_name = sfile
        pub_path = os.path.join('public', pdf_name)
        if not os.path.exists(pub_path):
            print(f"  [FAIL] {l['id']}: {pub_path} does not exist!")
        else:
            doc = fitz.open(pub_path)
            pstart = ref.get('page_start', 1)
            if pstart > len(doc):
                print(f"  [FAIL] {l['id']}: page_start {pstart} > total {len(doc)} in {pdf_name}")
            else:
                print(f"  [OK] {l['id']}: {pdf_name} p.{pstart}/{len(doc)}")
