"""
run_full_qa_suite.py - Comprehensive Quality Assurance & Mathematical Sanity Test Suite
Target: UET.MAT1052 Probability and Statistics Interactive Self-Study Learning Kit
"""

import sys
import os
import json
import re
import math
import subprocess

# Ensure UTF-8 output on Windows console
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE_DIR = os.path.join(ROOT_DIR, "site")
CONTENT_DIR = os.path.join(ROOT_DIR, "content")
DOCS_DIR = os.path.join(ROOT_DIR, "docs")

PASSED = 0
FAILED = 0
WARNINGS = 0

def test_assert(condition, test_name, error_msg=""):
    global PASSED, FAILED
    if condition:
        PASSED += 1
        print(f"  [PASS] {test_name}")
    else:
        FAILED += 1
        print(f"  [FAIL] {test_name}: {error_msg}")

def test_warn(condition, test_name, warn_msg=""):
    global WARNINGS
    if not condition:
        WARNINGS += 1
        print(f"  [WARN] {test_name}: {warn_msg}")
    else:
        print(f"  [PASS] {test_name}")

print("=" * 80)
print("  UET.MAT1052 QA AUDIT & VERIFICATION SUITE - PHASE 7")
print("=" * 80)

# ----------------------------------------------------------------------
# SUITE 1: HTML Files Structure, Navigation & KaTeX Integrity
# ----------------------------------------------------------------------
print("\n[SUITE 1] HTML Files Structure, Navigation & KaTeX Integrity")
html_files = [
    "index.html",
    "hoc.html",
    "tuluan.html",
    "tracnghiem.html",
    "congthuc.html"
]

expected_nav_hrefs = {
    "index.html": ["hoc.html", "tuluan.html", "tracnghiem.html", "congthuc.html"],
    "hoc.html": ["index.html", "tuluan.html", "tracnghiem.html", "congthuc.html"],
    "tuluan.html": ["index.html", "hoc.html", "tracnghiem.html", "congthuc.html"],
    "tracnghiem.html": ["index.html", "hoc.html", "tuluan.html", "congthuc.html"],
    "congthuc.html": ["index.html", "hoc.html", "tuluan.html", "tracnghiem.html"]
}

for fname in html_files:
    fpath = os.path.join(SITE_DIR, fname)
    exists = os.path.isfile(fpath)
    test_assert(exists, f"File existence: site/{fname}")
    if not exists:
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check non-empty
    test_assert(len(content) > 10000, f"File size site/{fname} > 10KB ({len(content)} bytes)")
    
    # Check essential tags
    test_assert("<!DOCTYPE html>" in content or "<!doctype html>" in content.lower(), f"Doctype present: site/{fname}")
    test_assert("<html" in content and "</html>" in content, f"HTML tags paired: site/{fname}")
    test_assert("<head>" in content and "</head>" in content, f"Head tags paired: site/{fname}")
    test_assert("<body" in content and "</body>" in content, f"Body tags paired: site/{fname}")
    test_assert("charset=\"UTF-8\"" in content or "charset=\"utf-8\"" in content.lower(), f"UTF-8 meta declared: site/{fname}")
    
    # Check KaTeX inclusion
    test_assert("katex.min.css" in content, f"KaTeX CSS included: site/{fname}")
    test_assert("katex.min.js" in content, f"KaTeX JS included: site/{fname}")
    test_assert("auto-render.min.js" in content, f"KaTeX auto-render JS included: site/{fname}")
    
    # Check Nav Links
    for expected_href in expected_nav_hrefs[fname]:
        test_assert(f'href="{expected_href}"' in content, f"Nav link to {expected_href} in site/{fname}")

# ----------------------------------------------------------------------
# SUITE 2: Embedded JavaScript Syntax Check via Node.js
# ----------------------------------------------------------------------
print("\n[SUITE 2] Embedded JavaScript Syntax Check (Node.js engine)")
for fname in html_files:
    fpath = os.path.join(SITE_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract scripts that are inline (not external src)
    script_blocks = re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', content, re.DOTALL)
    test_assert(len(script_blocks) > 0, f"Inline script found in site/{fname}")
    
    for idx, script in enumerate(script_blocks):
        # Validate syntax via node stdin to avoid Windows CLI length limit
        node_code = f"new Function({json.dumps(script)});"
        try:
            res = subprocess.run(["node", "-"], input=node_code, capture_output=True, text=True, encoding="utf-8", timeout=15)
            test_assert(res.returncode == 0, f"JavaScript syntax valid: site/{fname} (script block #{idx+1})", res.stderr.strip()[:100])
        except Exception as e:
            test_assert(False, f"JavaScript syntax execution: site/{fname}", str(e))

# ----------------------------------------------------------------------
# SUITE 3: Content Databases Integrity & Schema
# ----------------------------------------------------------------------
print("\n[SUITE 3] Content Databases Integrity & Schema Validation")

# Check tracnghiem_data.json
tn_path = os.path.join(CONTENT_DIR, "tracnghiem_data.json")
test_assert(os.path.isfile(tn_path), "File exists: content/tracnghiem_data.json")
with open(tn_path, "r", encoding="utf-8") as f:
    tn_data = json.load(f)

test_assert(isinstance(tn_data, list), "tracnghiem_data.json is a JSON list")
test_assert(len(tn_data) == 161, f"Total MCQs count is 161 (Found: {len(tn_data)})")

# Check schema and uniqueness of MCQs
tn_ids = set()
topic_mcq_counts = {}
ans_dist = {0: 0, 1: 0, 2: 0, 3: 0}
diff_dist = {}

valid_levels = {"Cơ bản", "Trung bình", "Nâng cao", "Nhận biết", "Thông hiểu", "Vận dụng", "Vận dụng cao"}

for q in tn_data:
    q_id = q.get("id")
    test_assert(q_id is not None and q_id not in tn_ids, f"MCQ ID unique and valid: {q_id}")
    tn_ids.add(q_id)
    
    topic_id = q.get("topicId")
    topic_mcq_counts[topic_id] = topic_mcq_counts.get(topic_id, 0) + 1
    
    options = q.get("options", [])
    test_assert(len(options) == 4, f"MCQ {q_id} has exactly 4 options")
    
    corr = q.get("correctIndex")
    test_assert(corr in [0, 1, 2, 3], f"MCQ {q_id} correctIndex in 0..3 (Found {corr})")
    if corr in ans_dist:
        ans_dist[corr] += 1
        
    lvl = q.get("level")
    diff_dist[lvl] = diff_dist.get(lvl, 0) + 1
    test_assert(lvl in valid_levels, f"MCQ {q_id} valid level: {lvl}")
    
    test_assert(len(q.get("explanation", "")) > 10, f"MCQ {q_id} has substantial explanation")

# Check tuluan_data.json
tl_path = os.path.join(CONTENT_DIR, "tuluan_data.json")
test_assert(os.path.isfile(tl_path), "File exists: content/tuluan_data.json")
with open(tl_path, "r", encoding="utf-8") as f:
    tl_raw = json.load(f)

test_assert(isinstance(tl_raw, dict), "tuluan_data.json is a JSON object with exercises and topics")
tl_exercises = tl_raw.get("exercises", [])
test_assert(len(tl_exercises) == 56, f"Total free response count is 56 (Found: {len(tl_exercises)})")

tl_ids = set()
topic_tl_counts = {}
for p in tl_exercises:
    p_id = p.get("id")
    test_assert(p_id is not None and p_id not in tl_ids, f"Free response ID unique: {p_id}")
    tl_ids.add(p_id)
    
    top_id = p.get("topicId")
    topic_tl_counts[top_id] = topic_tl_counts.get(top_id, 0) + 1
    
    steps = p.get("steps", [])
    test_assert(len(steps) >= 1, f"Free response {p_id} has step-by-step breakdown (Found {len(steps)})")
    
    for s_idx, step in enumerate(steps):
        test_assert(isinstance(step, str) and len(step) > 20, f"Step #{s_idx+1} valid content in {p_id}")
        test_assert("Bước" in step or "bước" in step.lower() or "[+" in step, f"Step #{s_idx+1} barem marker in {p_id}")

# Check 7 topics distribution in free-response: each topic has 8 questions
for t in range(1, 8):
    cnt = topic_tl_counts.get(t, 0)
    test_assert(cnt == 8, f"Topic {t} has exactly 8 free response exercises (Found: {cnt})")

# Check lessons in content/lessons_all.js
lessons_path = os.path.join(CONTENT_DIR, "lessons_all.js")
test_assert(os.path.isfile(lessons_path), "File exists: content/lessons_all.js")
with open(lessons_path, "r", encoding="utf-8") as f:
    lessons_js = f.read()

lesson_ids_raw = re.findall(r'(?:["\']id["\']|\bid)\s*:\s*["\']([^"\']+)["\']', lessons_js)
lesson_ids = [lid for lid in lesson_ids_raw if re.match(r'^[A-E]\d+$', lid)]
test_assert(len(lesson_ids) == 26, f"Total lessons is 26 across 5 clusters (Found: {len(lesson_ids)})")
test_assert(len(set(lesson_ids)) == 26, "All 26 lesson IDs are unique")

# Check formulas in site/congthuc.html
with open(os.path.join(SITE_DIR, "congthuc.html"), "r", encoding="utf-8") as f:
    ct_content = f.read()

ct_ids = re.findall(r'"id":\s*"(CT\d+_\d+)"', ct_content)
test_assert(len(ct_ids) == 35, f"Total formula cards is 35 (Found: {len(ct_ids)})")
test_assert(len(set(ct_ids)) == 35, "All 35 formula IDs are unique")

# ----------------------------------------------------------------------
# SUITE 4: MCQ Balance & Quality Verification
# ----------------------------------------------------------------------
print("\n[SUITE 4] MCQ Option Balance & Difficulty Distribution")
print(f"  Distribution of correct answers: A={ans_dist[0]} ({ans_dist[0]/161*100:.1f}%), "
      f"B={ans_dist[1]} ({ans_dist[1]/161*100:.1f}%), "
      f"C={ans_dist[2]} ({ans_dist[2]/161*100:.1f}%), "
      f"D={ans_dist[3]} ({ans_dist[3]/161*100:.1f}%)")

for opt_idx, opt_letter in enumerate(["A", "B", "C", "D"]):
    pct = ans_dist[opt_idx] / 161 * 100
    test_assert(18.0 <= pct <= 32.0, f"Option {opt_letter} percentage balanced (18% - 32%): {pct:.1f}%")

print(f"  Level distribution: {diff_dist}")
test_assert(len(diff_dist) >= 3, "Multi-level question distribution present")

# ----------------------------------------------------------------------
# SUITE 5: Rigorous Mathematical Sanity Checks
# ----------------------------------------------------------------------
print("\n[SUITE 5] Rigorous Mathematical Sanity & Formula Exactness Checks")

# 1. CLT Spare Bulbs Quadratic Sanity Check
# Week 07 Slide 90 & Exercise TL7_7:
# Mu = 100, Sigma = 20 (Var = 400), T = 2000, Conf = 99%
# Solving 100u^2 - 20*z*u - 2000 >= 0
def solve_clt_spare_bulbs(z_val):
    a = 100.0
    b = -20.0 * z_val
    c = -2000.0
    delta = b**2 - 4*a*c
    u = (-b + math.sqrt(delta)) / (2*a)
    n = math.ceil(u**2)
    return u, n

u_std, n_std = solve_clt_spare_bulbs(2.3263)
u_slide, n_slide = solve_clt_spare_bulbs(2.4675)
test_assert(n_std == 23 and n_slide == 23, f"CLT Spare bulb root yields n = 23 (u_std={u_std:.3f}, u_slide={u_slide:.3f})")

# 2. OLS Regression Sanity Check
# Sample points: (1, 2), (2, 3), (3, 5), (4, 4), (5, 6)
xs = [1.0, 2.0, 3.0, 4.0, 5.0]
ys = [2.0, 3.0, 5.0, 4.0, 6.0]
n_pts = len(xs)
sum_x = sum(xs)
sum_y = sum(ys)
sum_x2 = sum(x**2 for x in xs)
sum_y2 = sum(y**2 for y in ys)
sum_xy = sum(x*y for x, y in zip(xs, ys))
b1 = (n_pts * sum_xy - sum_x * sum_y) / (n_pts * sum_x2 - sum_x**2)
b0 = (sum_y - b1 * sum_x) / n_pts
r_num = (n_pts * sum_xy - sum_x * sum_y)
r_den = math.sqrt((n_pts * sum_x2 - sum_x**2) * (n_pts * sum_y2 - sum_y**2))
r = r_num / r_den
r2 = r**2

test_assert(b1 == 0.9, f"OLS slope b1 exactness (Expected 0.9, Got {b1:.4f})")
test_assert(b0 == 1.3, f"OLS intercept b0 exactness (Expected 1.3, Got {b0:.4f})")
test_assert(0.0 <= r2 <= 1.0, f"OLS R^2 in valid [0, 1] interval: {r2:.4f}")
test_assert(-1.0 <= r <= 1.0, f"Correlation coefficient r in [-1, 1]: {r:.4f}")

# 3. Bayes' Theorem Sanity Check
# P(D) = 0.01, P(Pos|D) = 0.95, P(Pos|not D) = 0.02
# P(D|Pos) = (0.01 * 0.95) / (0.01 * 0.95 + 0.99 * 0.02)
p_d = 0.01
p_pos_d = 0.95
p_pos_not_d = 0.02
p_pos = p_d * p_pos_d + (1 - p_d) * p_pos_not_d
p_d_pos = (p_d * p_pos_d) / p_pos
test_assert(0.323 <= p_d_pos <= 0.325, f"Bayes theorem exact calculation: {p_d_pos:.5f} (~32.42%)")

# 4. Binomial & Poisson Distribution Boundary Check
# Binomial n=10, p=0.3 -> sum of probabilities for k=0..10 equals 1
binom_sum = sum(math.comb(10, k) * (0.3**k) * (0.7**(10-k)) for k in range(11))
test_assert(abs(binom_sum - 1.0) < 1e-9, f"Binomial PMF total mass equals 1.0 (Sum: {binom_sum:.9f})")

# Poisson lambda = 4.5 -> sum of k=0..30 equals ~1.0
poiss_sum = sum((4.5**k * math.exp(-4.5)) / math.factorial(k) for k in range(35))
test_assert(abs(poiss_sum - 1.0) < 1e-7, f"Poisson PMF total mass equals 1.0 (Sum: {poiss_sum:.9f})")

# 5. Normal CDF Symmetry & Standard Values Check
def phi(z):
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))

test_assert(abs(phi(0.0) - 0.5) < 1e-9, "Phi(0) == 0.5")
test_assert(abs(phi(1.96) - 0.975002) < 1e-4, f"Phi(1.96) approx 0.9750 (Got {phi(1.96):.5f})")
test_assert(abs(phi(1.645) - 0.9500) < 1e-3, f"Phi(1.645) approx 0.9500 (Got {phi(1.645):.5f})")
test_assert(abs(phi(-1.96) - (1.0 - phi(1.96))) < 1e-9, "Phi(-z) == 1 - Phi(z) symmetry holds")

# ----------------------------------------------------------------------
# FINAL SUMMARY
# ----------------------------------------------------------------------
print("\n" + "=" * 80)
print(f"  QA SUITE SUMMARY: {PASSED} PASSED | {FAILED} FAILED | {WARNINGS} WARNINGS")
print("=" * 80)

if FAILED > 0:
    print(f"\n❌ QA SUITE FAILED with {FAILED} errors.")
    sys.exit(1)
else:
    print(f"\n✅ ALL {PASSED} QA AND MATHEMATICAL SANITY TESTS PASSED WITH 100% SUCCESS!")
    sys.exit(0)
