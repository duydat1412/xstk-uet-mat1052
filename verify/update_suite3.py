with open('verify/run_csdl_qa_suite.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = '''redirect_sources = [r["source"] for r in vercel_cfg.get("redirects", [])]
test_assert("/csdl" in redirect_sources, "Vercel route /csdl declared")
test_assert("/csdl/hoc" in redirect_sources, "Vercel route /csdl/hoc declared")
test_assert("/xstk/hoc" in redirect_sources, "Vercel route /xstk/hoc declared")
test_assert("/hoc" in redirect_sources, "Vercel route /hoc maintained for backward compatibility")'''

replacement = '''redirect_sources = [r["source"] for r in vercel_cfg.get("redirects", [])]
next_cfg_path = os.path.join(ROOT_DIR, "next.config.mjs")
has_next = os.path.isfile(next_cfg_path)
next_cfg_text = ""
if has_next:
    with open(next_cfg_path, "r", encoding="utf-8") as nf:
        next_cfg_text = nf.read()

test_assert("/csdl" in redirect_sources or "source: '/csdl'" in next_cfg_text, "Vercel route /csdl declared")
test_assert("/csdl/hoc" in redirect_sources or os.path.isdir(os.path.join(ROOT_DIR, "app", "csdl", "hoc")), "Vercel route /csdl/hoc declared")
test_assert("/xstk/hoc" in redirect_sources or os.path.isdir(os.path.join(ROOT_DIR, "app", "xstk", "hoc")), "Vercel route /xstk/hoc declared")
test_assert("/hoc" in redirect_sources or "source: '/hoc'" in next_cfg_text, "Vercel route /hoc maintained for backward compatibility")'''

if target in text:
    text = text.replace(target, replacement, 1)
    with open('verify/run_csdl_qa_suite.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated run_csdl_qa_suite.py for Next.js routing compatibility")
else:
    print("Target not found in run_csdl_qa_suite.py")
