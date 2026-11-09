import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASSED = 0
FAILED = 0
WARNINGS = 0

def test_assert(condition, desc):
    global PASSED, FAILED
    if condition:
        PASSED += 1
        print(f"  [PASS] {desc}")
    else:
        FAILED += 1
        print(f"  [FAIL] {desc}")

print("=" * 80)
print("  UET.IS2099 (CƠ SỞ DỮ LIỆU) QA AUDIT & VERIFICATION SUITE")
print("=" * 80)

# ----------------------------------------------------------------------
# SUITE 1: HTML Structure & Hub Integration
# ----------------------------------------------------------------------
print("\n[SUITE 1] HTML Files & UET Study Hub Integration")
csdl_hoc_path = os.path.join(ROOT_DIR, "site", "csdl", "hoc.html")
test_assert(os.path.isfile(csdl_hoc_path), "File exists: site/csdl/hoc.html")
hoc_size = os.path.getsize(csdl_hoc_path)
test_assert(hoc_size > 50000, f"site/csdl/hoc.html is substantive ({hoc_size} bytes)")

with open(csdl_hoc_path, "r", encoding="utf-8") as f:
    hoc_html = f.read()

test_assert("<!DOCTYPE html>" in hoc_html, "Doctype declared in site/csdl/hoc.html")
test_assert("<html" in hoc_html and "</html>" in hoc_html, "HTML tags paired in site/csdl/hoc.html")
test_assert("<head" in hoc_html and "</head>" in hoc_html, "Head tags paired in site/csdl/hoc.html")
test_assert("<body" in hoc_html and "</body>" in hoc_html, "Body tags paired in site/csdl/hoc.html")
test_assert("charset" in hoc_html.lower() and "utf-8" in hoc_html.lower(), "UTF-8 declared")
test_assert("katex.min.css" in hoc_html, "KaTeX CSS linked")
test_assert("katex.min.js" in hoc_html, "KaTeX JS included")
test_assert("course-switcher" in hoc_html, "Course Switcher present in site/csdl/hoc.html")
test_assert("csdl_active_lesson" in hoc_html or "csdl_progress" in hoc_html or "csdl_completed_lessons" in hoc_html, "CSDL specific localStorage key used")

# ----------------------------------------------------------------------
# SUITE 2: CSDL Lessons Data Integrity (14 Lessons)
# ----------------------------------------------------------------------
print("\n[SUITE 2] CSDL Lessons Data Integrity (14 Lessons)")
lessons_js_path = os.path.join(ROOT_DIR, "content_csdl", "lessons_all.js")
test_assert(os.path.isfile(lessons_js_path), "File exists: content_csdl/lessons_all.js")

# Extract ALL_CSDL_LESSONS using node with utf-8 encoding
import subprocess
node_cmd = ["node", "-e", "import('./content_csdl/lessons_all.js').then(m => console.log(JSON.stringify(m.ALL_CSDL_LESSONS)));"]
res = subprocess.run(node_cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=ROOT_DIR)
test_assert(res.returncode == 0, "Node.js successfully loads content_csdl/lessons_all.js")

lessons = json.loads(res.stdout.strip())
test_assert(len(lessons) == 14, f"Exactly 14 lessons defined (Found: {len(lessons)})")

clusters = {"1": 0, "2": 0, "3": 0, "4": 0}
total_steps = 0
total_exs = 0
total_traps = 0
total_quizzes = 0

for l in lessons:
    lid = l["id"]
    c = l.get("cluster")
    clusters[c] = clusters.get(c, 0) + 1
    
    steps = l.get("steps", [])
    exs = l.get("examples", [])
    traps = l.get("pitfalls", [])
    quizzes = l.get("quizzes", [])
    
    total_steps += len(steps)
    total_exs += len(exs)
    total_traps += len(traps)
    total_quizzes += len(quizzes)
    
    test_assert(len(steps) >= 2, f"Lesson {lid} has >= 2 theory steps (Found: {len(steps)})")
    test_assert(len(exs) == 3, f"Lesson {lid} has exactly 3 examples (Found: {len(exs)})")
    test_assert(len(traps) >= 2, f"Lesson {lid} has >= 2 pitfalls (Found: {len(traps)})")
    test_assert(len(quizzes) == 3, f"Lesson {lid} has exactly 3 gatekeeper quizzes (Found: {len(quizzes)})")
    
    # Check Ref
    ref = l.get("ref", {})
    sfile = ref.get("slide_file")
    sfile_path = os.path.join(ROOT_DIR, "tailieu_csdl", sfile)
    test_assert(os.path.isfile(sfile_path), f"Slide file exists for {lid}: {sfile}")
    test_assert(len(ref.get("section", "")) > 5, f"Lesson {lid} has section info")
    test_assert(len(ref.get("remind", "")) > 10, f"Lesson {lid} has remind guidance")
    
    # Check Quiz options & answers
    for q_idx, q in enumerate(quizzes):
        test_assert(len(q.get("opts", [])) == 4, f"Quiz {q_idx+1} of {lid} has 4 options")
        test_assert(0 <= q.get("ans", -1) <= 3, f"Quiz {q_idx+1} of {lid} has valid answer index")
        test_assert(len(q.get("fb", "")) > 10, f"Quiz {q_idx+1} of {lid} has feedback")

print(f"\n[SUMMARY STATS]")
print(f"  Clusters: {clusters}")
print(f"  Total Steps: {total_steps}")
print(f"  Total Examples: {total_exs}")
print(f"  Total Pitfalls: {total_traps}")
print(f"  Total Gatekeeper Quizzes: {total_quizzes}")

# ----------------------------------------------------------------------
# SUITE 3: Global Routing & Vercel Configuration
# ----------------------------------------------------------------------
print("\n[SUITE 3] Global Routing & Vercel Configuration")
vercel_path = os.path.join(ROOT_DIR, "vercel.json")
with open(vercel_path, "r", encoding="utf-8") as f:
    vercel_cfg = json.load(f)

redirect_sources = [r["source"] for r in vercel_cfg.get("redirects", [])]
test_assert("/csdl" in redirect_sources, "Vercel route /csdl declared")
test_assert("/csdl/hoc" in redirect_sources, "Vercel route /csdl/hoc declared")
test_assert("/xstk/hoc" in redirect_sources, "Vercel route /xstk/hoc declared")
test_assert("/hoc" in redirect_sources, "Vercel route /hoc maintained for backward compatibility")

# Check index.html Hub
index_path = os.path.join(ROOT_DIR, "site", "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

test_assert("UET STUDY HUB" in index_html, "UET Study Hub banner in site/index.html")
test_assert("card-sub-xstk" in index_html, "XSTK card present in site/index.html")
test_assert("card-sub-csdl" in index_html, "CSDL card present in site/index.html")
test_assert("/csdl/hoc" in index_html, "Link to /csdl/hoc in site/index.html")

print("\n" + "=" * 80)
print(f"  CSDL QA SUITE SUMMARY: {PASSED} PASSED | {FAILED} FAILED | {WARNINGS} WARNINGS")
print("=" * 80)

if FAILED > 0:
    print(f"\n❌ CSDL QA SUITE FAILED with {FAILED} errors.")
    sys.exit(1)
else:
    print(f"\n✅ 100% CSDL QA TESTS PASSED! System is production-ready.")
