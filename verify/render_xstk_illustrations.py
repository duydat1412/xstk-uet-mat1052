import fitz
import os

xstk_renders = [
    # A2: Histogram & Distribution shapes
    ("week02.pdf", 7, "public/illustrations/xstk/xstk_a2_distribution_shapes.png", "Hình dạng phân phối: Đối xứng, Lệch phải, Lệch trái"),
    # A3: Boxplot & Tukey Outlier fences
    ("week02.pdf", 37, "public/illustrations/xstk/xstk_a3_boxplot_tukey.png", "Biểu đồ Hộp Boxplot và Hàng rào ngoại lai 1.5 IQR của Tukey"),
    # A4: Scatter Plot & OLS Line
    ("week04.pdf", 12, "public/illustrations/xstk/xstk_a4_scatter_ols_line.png", "Biểu đồ phân tán Scatter Plot và Đường hồi quy OLS"),
    ("week04.pdf", 45, "public/illustrations/xstk/xstk_a4_residuals_plot.png", "Đồ thị Phần dư (Residuals) và sai số quan sát"),
    # B1-B3: Venn Diagram & Probability Rules
    ("week05.pdf", 12, "public/illustrations/xstk/xstk_b1_venn_diagram.png", "Sơ đồ Venn: Biến cố Giao, Hợp, Phần bù"),
    # B5: Probability Tree & Bayes
    ("week05.pdf", 72, "public/illustrations/xstk/xstk_b5_bayes_tree_diagram.png", "Sơ đồ Cây xác suất (Tree Diagram) và Công thức Bayes"),
    # D1-D3: Normal Distribution Bell Curve
    ("week07.pdf", 22, "public/illustrations/xstk/xstk_d1_normal_distribution_curve.png", "Đường cong Phân phối Chuẩn hình chuông Gauss và Quy tắc 68-95-99.7"),
]

print("Rendering XSTK illustrations...")
for fname, pno, out_path, title in xstk_renders:
    pdf_path = os.path.join("public", fname)
    if not os.path.exists(pdf_path):
        pdf_path = os.path.join("public", "tailieu_xstk", fname)
    if not os.path.exists(pdf_path):
        print(f"Missing PDF: {fname}")
        continue
    doc = fitz.open(pdf_path)
    if pno > len(doc):
        print(f"Page {pno} > {len(doc)} in {fname}")
        continue
    page = doc[pno - 1]
    pix = page.get_pixmap(dpi=150)
    pix.save(out_path)
    print(f"Rendered: {out_path} ({pix.width}x{pix.height}) - {title}")

print("\nDone rendering XSTK illustrations!")
