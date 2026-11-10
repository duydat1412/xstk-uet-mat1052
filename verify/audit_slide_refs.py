import json, os

for course_file, course_id in [('data/courses/xstk.json', 'xstk'), ('data/courses/csdl.json', 'csdl')]:
    with open(course_file, encoding='utf-8') as f:
        lessons = json.load(f)
    print(f"=== {course_id.upper()} ({len(lessons)} lessons) ===")
    for l in lessons:
        ref = l.get('ref', {})
        slide_file = ref.get('slide_file')
        if not slide_file:
            print(f"{l['id']}: NO slide_file defined!")
            continue
        
        direct_path = os.path.join('public', slide_file)
        csdl_path = os.path.join('public', 'tailieu_csdl', slide_file)
        xstk_path = os.path.join('public', 'tailieu_xstk', slide_file)
        
        status = []
        if os.path.exists(direct_path): status.append('public/' + slide_file)
        if os.path.exists(csdl_path): status.append('public/tailieu_csdl/' + slide_file)
        if os.path.exists(xstk_path): status.append('public/tailieu_xstk/' + slide_file)
        
        print(f"{l['id']}: slide_file={repr(slide_file)} -> found in: {status if status else 'MISSING!'}")
