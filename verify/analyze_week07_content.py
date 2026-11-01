import fitz, re, sys

sys.stdout.reconfigure(encoding='utf-8')

# Analyze differences in notation, topics, formulas
print("Checking slide week07 notation...")
doc7 = fitz.open("week07.pdf")
text7 = ""
for page in doc7:
    text7 += page.get_text() + "\n"

# Look for specific keywords in week07:
keywords = [
    "Chebyshev", "luật số lớn", "yếu", "chiếc hộp", "i.i.d", "độc lập", 
    "kỳ vọng", "phương sai", "độ lệch chuẩn", "liên tục", "mật độ", 
    "tích lũy", "phân phối đều", "chuẩn", "mũ", "chi-bình phương", 
    "t-Student", "giới hạn trung tâm", "Markov", "LOTUS", "hệ số biến thiên"
]

print("Found keywords occurrences in week07:")
for kw in keywords:
    cnt = len(re.findall(re.escape(kw), text7, re.IGNORECASE))
    print(f"  - {kw}: {cnt}")
