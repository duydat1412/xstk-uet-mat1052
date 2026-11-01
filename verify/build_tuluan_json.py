import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# We will generate a structured array of 56 free-response exercises (8 per topic across 7 topics).
# Let's write the comprehensive generator in python.

from verify.verify_tuluan import *

topics = [
    {"id": 1, "name": "Thống kê mô tả, Bảng liên hợp & Hồi quy tuyến tính", "short": "Mô tả & Hồi quy"},
    {"id": 2, "name": "Lý thuyết xác suất, Xác suất có điều kiện & Bayes", "short": "Xác suất & Điều kiện"},
    {"id": 3, "name": "Biến ngẫu nhiên rời rạc, Bảng pmf, Hàm cdf & Kỳ vọng, Phương sai", "short": "pmf, cdf & E/Var"},
    {"id": 4, "name": "Các phân phối rời rạc: Nhị thức, Siêu bội & Poisson", "short": "Nhị thức, Siêu bội, Poisson"},
    {"id": 5, "name": "Tổng, Trung bình mẫu i.i.d. & Bất đẳng thức Chebyshev", "short": "Tổng, TB & Chebyshev"},
    {"id": 6, "name": "Biến liên tục, Phân phối Đều, Mũ & Phân phối Chuẩn N(μ, σ²)", "short": "Liên tục, Đều & Chuẩn"},
    {"id": 7, "name": "Định lý giới hạn trung tâm (CLT) & Bài toán kích thước mẫu", "short": "Định lý CLT"}
]

print("Building 56 exercises...")
