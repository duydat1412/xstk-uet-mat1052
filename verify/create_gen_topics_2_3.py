import sys

sys.stdout.reconfigure(encoding='utf-8')

def indent_block(text, spaces=4):
    pad = " " * spaces
    return "\n".join(pad + line if line.strip() else line for line in text.split("\n"))

# Convert generate_tuluan_full.py to gen_topic_2.py
with open('verify/generate_tuluan_full.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx_start = text.find('exercises.append({\n    "id": "TL2_1"')
idx_end = text.rfind('print(f"Added Topic 2')
topic2_body = text[idx_start:idx_end].strip()

topic2_content = f"""# Topic 2: Xác suất cơ bản, Có điều kiện & Bayes (TL2_1 -> TL2_8)
import sys

def get_topic_2():
    exercises = []

{indent_block(topic2_body, 4)}

    return exercises

if __name__ == "__main__":
    t2 = get_topic_2()
    print(f"Generated Topic 2: {{len(t2)}} exercises.")
"""

with open('verify/gen_topic_2.py', 'w', encoding='utf-8') as f:
    f.write(topic2_content)

print("gen_topic_2.py written.")

# Convert append_topics_3_4.py to gen_topic_3.py
with open('verify/append_topics_3_4.py', 'r', encoding='utf-8') as f:
    text3 = f.read()

idx_start3 = text3.find('exercises.append({\n    "id": "TL3_1"')
idx_end3 = text3.rfind('print(f"Added Topic 3')
topic3_body = text3[idx_start3:idx_end3].strip()

topic3_content = f"""# Topic 3: Biến rời rạc, pmf, cdf, Kỳ vọng & Phương sai (TL3_1 -> TL3_8)
import sys

def get_topic_3():
    exercises = []

{indent_block(topic3_body, 4)}

    return exercises

if __name__ == "__main__":
    t3 = get_topic_3()
    print(f"Generated Topic 3: {{len(t3)}} exercises.")
"""

with open('verify/gen_topic_3.py', 'w', encoding='utf-8') as f:
    f.write(topic3_content)

print("gen_topic_3.py written.")
