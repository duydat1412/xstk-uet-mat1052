with open('site/csdl/hoc.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'localStorage\.(?:getItem|setItem)\([\'"]([a-zA-Z0-9_\-]+)[\'"]', text)
print("Keys:", set(matches))
