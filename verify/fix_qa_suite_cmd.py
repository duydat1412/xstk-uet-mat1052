with open('verify/run_csdl_qa_suite.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = 'const { ALL_CSDL_LESSONS } = require(\'./content_csdl/lessons_all.js\'); console.log(JSON.stringify(ALL_CSDL_LESSONS));'
replacement = 'import(\'./content_csdl/lessons_all.js\').then(m => console.log(JSON.stringify(m.ALL_CSDL_LESSONS)));'

if target in text:
    text = text.replace(target, replacement, 1)
    with open('verify/run_csdl_qa_suite.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed run_csdl_qa_suite.py successfully")
else:
    print("Target not found in run_csdl_qa_suite.py")
