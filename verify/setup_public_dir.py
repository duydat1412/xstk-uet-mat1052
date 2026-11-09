import os, shutil

os.makedirs('public', exist_ok=True)

# 1. Copy site folder to public/site
if os.path.exists('site'):
    if os.path.exists('public/site'):
        shutil.rmtree('public/site')
    shutil.copytree('site', 'public/site')
    print("Copied site/ to public/site/")

# 2. Copy root pdfs to public/
for f in os.listdir('.'):
    if f.endswith('.pdf') or f.endswith('.html') or f.endswith('.png'):
        shutil.copy2(f, os.path.join('public', f))
print("Copied root files to public/")

# 3. Copy tailieu_csdl & tailieu_xstk if exist
for d in ['tailieu_csdl', 'tailieu_xstk', 'content_csdl']:
    if os.path.exists(d):
        dest = os.path.join('public', d)
        if os.path.exists(dest):
            shutil.rmtree(dest)
        shutil.copytree(d, dest)
        print(f"Copied {d}/ to public/{d}/")

print("Public directory setup complete!")
