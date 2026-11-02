import os
import re
import fitz
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("content/lesson_references.json", "r", encoding="utf-8") as f:
    refs = json.load(f)

print(f"Auditing {len(refs)} lesson references...")

total_ok = 0
for lid, ref in sorted(refs.items()):
    slide_file = ref.get("slide_file")
    page_start = ref.get("page_start")
    pages_str = ref.get("pages")
    section = ref.get("section")
    remind = ref.get("remind")
    stat20 = ref.get("stat20")

    # 1. Check file exists
    assert os.path.isfile(slide_file), f"File {slide_file} does not exist for lesson {lid}"
    
    # 2. Check PDF total pages
    doc = fitz.open(slide_file)
    total_pages = len(doc)
    assert 1 <= page_start <= total_pages, f"page_start {page_start} out of bounds (1..{total_pages}) for {lid}"

    # 3. Check fields validity
    assert len(pages_str) > 3, f"pages string too short for {lid}"
    assert len(section) > 10, f"section too short for {lid}"
    assert len(remind) > 20, f"remind too short for {lid}"
    assert len(stat20) > 5, f"stat20 too short for {lid}"

    total_ok += 1
    print(f"  [OK] {lid}: {slide_file} ({page_start}/{total_pages} pages) | {pages_str}")

print(f"\nAll {total_ok}/26 lesson references are 100% physically valid against actual PDF files!")
