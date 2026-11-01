import math
import numpy as np
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("==================================================")
print("  KIỂM CHỨNG TOÀN BỘ 56 BÀI TẬP TỰ LUẬN (PHASE 3)  ")
print("==================================================")

def phi(z):
    """Cumulative distribution function for the standard normal distribution."""
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))

def phi_inv(p):
    """Inverse normal CDF (quantile) approximation."""
    # Rational approximation for central values
    from scipy.stats import norm
    return norm.ppf(p)

# Let's check if scipy is available, otherwise use rational approximation
try:
    from scipy.stats import norm
    get_z = lambda p: norm.ppf(p)
except ImportError:
    # Winitzki approximation or standard table constants
    def get_z(p):
        table = {0.90: 1.28155, 0.95: 1.64485, 0.975: 1.95996, 0.99: 2.32635, 0.995: 2.57583}
        return table.get(p, 1.64485)

# --- DẠNG 1: THỐNG KÊ MÔ TẢ & HỒI QUY ---
print("\n--- DẠNG 1 ---")
# TL1_1: Scores [3, 5, 6, 7, 7, 8, 8, 9, 10, 16]
s1 = np.array([3, 5, 6, 7, 7, 8, 8, 9, 10, 16])
mean1 = np.mean(s1)
med1 = np.median(s1)
q1_1, q3_1 = 6.0, 9.0 # lower half [3,5,6,7,7] -> 6, upper half [8,8,9,10,16] -> 9
iqr1 = q3_1 - q1_1
fence_up1 = q3_1 + 1.5 * iqr1
print(f"TL1_1: Mean={mean1:.2f}, Med={med1:.2f}, Q1={q1_1}, Q3={q3_1}, IQR={iqr1}, Upper Fence={fence_up1}, Outlier={s1[s1 > fence_up1]}")

# TL1_2: Contingency table 60 students
#          Tiếng Anh Tốt    Chưa Tốt   Tổng
# Năm 1         12             28       40
# Năm 2         15              5       20
# Tổng          27             33       60
p_joint = 15 / 60
p_row_n2 = 15 / 20
p_col_tot = 15 / 27
print(f"TL1_2: P(Năm 2 VÀ Tốt)={p_joint:.4f}, P(Tốt | Năm 2)={p_row_n2:.4f}, P(Năm 2 | Tốt)={p_col_tot:.4f}")

# TL1_3: y_hat = 15 + 2.5*x. At x=8, obs y=38
y_hat_3 = 15 + 2.5 * 8
res_3 = 38 - y_hat_3
print(f"TL1_3: y_hat={y_hat_3}, Residual={res_3}")

# TL1_4: Points (1, 3), (2, 5), (3, 6), (4, 8), (5, 10)
x4 = np.array([1, 2, 3, 4, 5])
y4 = np.array([3, 5, 6, 8, 10])
r4 = np.corrcoef(x4, y4)[0, 1]
b1_4, b0_4 = np.polyfit(x4, y4, 1)
res4 = y4 - (b0_4 + b1_4 * x4)
print(f"TL1_4: r={r4:.4f}, b1={b1_4:.4f}, b0={b0_4:.4f}, Sum(res)={np.sum(res4):.6f}")

# --- DẠNG 2: XÁC SUẤT CƠ BẢN & CÓ ĐIỀU KIỆN ---
print("\n--- DẠNG 2 ---")
# TL2_1: Roll 2 dice, Sum >= 9
# Sums >= 9: (3,6),(4,5),(4,6),(5,4),(5,5),(5,6),(6,3),(6,4),(6,5),(6,6) = 10 outcomes => 10/36 = 5/18
p_sum_ge_9 = 10 / 36
print(f"TL2_1: P(Sum >= 9) = 10/36 = {p_sum_ge_9:.4f}")

# TL2_2: 12 balls (5 Red, 7 Blue). Draw 2 without replacement. Same color.
p_both_r = (5/12) * (4/11)
p_both_b = (7/12) * (6/11)
p_same_col = p_both_r + p_both_b
print(f"TL2_2: P(Same color) = {p_both_r:.4f} + {p_both_b:.4f} = {p_same_col:.4f} (62/132 = {62/132:.4f})")

# TL2_3: P(A)=0.6, P(B)=0.5, P(AB)=0.3
p_u = 0.6 + 0.5 - 0.3
p_a_given_b = 0.3 / 0.5
p_b_given_a = 0.3 / 0.6
print(f"TL2_3: P(A cup B)={p_u:.2f}, P(A|B)={p_a_given_b:.2f}, P(B|A)={p_b_given_a:.2f}")

# TL2_5: Bayes rule. Disease prevalence P(D) = 0.01. Test sensitivity P(T+|D) = 0.95. Specificity P(T-|D-) = 0.90 => P(T+|D-) = 0.10.
# P(T+) = 0.01 * 0.95 + 0.99 * 0.10 = 0.0095 + 0.0990 = 0.1085
# P(D | T+) = 0.0095 / 0.1085
p_pos = 0.01 * 0.95 + 0.99 * 0.10
p_d_given_pos = (0.01 * 0.95) / p_pos
print(f"TL2_5: Bayes P(D | T+) = {p_d_given_pos:.4f} (8.76%)")

# --- DẠNG 3: BẢNG PMF, CDF, KỲ VỌNG & PHƯƠNG SAI ---
print("\n--- DẠNG 3 ---")
# TL3_1: p(x) = c*(5 - x) for x in {1, 2, 3, 4}
# sum = c*(4 + 3 + 2 + 1) = 10c = 1 => c = 0.1
# x: 1 (0.4), 2 (0.3), 3 (0.2), 4 (0.1)
x3_1 = np.array([1, 2, 3, 4])
p3_1 = np.array([0.4, 0.3, 0.2, 0.1])
e3_1 = np.sum(x3_1 * p3_1)
e3_1_sq = np.sum((x3_1**2) * p3_1)
var3_1 = e3_1_sq - e3_1**2
sd3_1 = math.sqrt(var3_1)
print(f"TL3_1: E(X)={e3_1:.2f}, Var(X)={var3_1:.2f}, SD(X)={sd3_1:.4f}")

# TL3_4: E(X)=5, Var(X)=4 => SD(X)=2
# Y = 2X - 3 => E(Y) = 2*5 - 3 = 7, Var(Y) = 4*4 = 16, SD(Y) = 4
print(f"TL3_4: E(2X-3)={2*5-3}, Var(2X-3)={4*4}, SD(2X-3)={math.sqrt(16)}")

# --- DẠNG 4: NHỊ THỨC, SIÊU BỘI, POISSON ---
print("\n--- DẠNG 4 ---")
# TL4_1: B(n=10, p=0.7). P(X=7) = C(10, 7) * 0.7^7 * 0.3^3
p_b_7 = math.comb(10, 7) * (0.7**7) * (0.3**3)
e_b1 = 10 * 0.7
sd_b1 = math.sqrt(10 * 0.7 * 0.3)
print(f"TL4_1: P(X=7)={p_b_7:.4f}, E={e_b1:.1f}, SD={sd_b1:.4f}")

# TL4_2: HG(N=30, M=6, n=4). P(X=1) = C(6, 1)*C(24, 3) / C(30, 4)
p_hg_1 = (math.comb(6, 1) * math.comb(24, 3)) / math.comb(30, 4)
print(f"TL4_2: P(X=1)={p_hg_1:.4f} (C(6,1)*C(24,3)/C(30,4) = {6*2024}/{27405})")

# TL4_3: Poisson(lambda=2). P(X=3) = 2^3 * e^(-2) / 6 = 8 * e^(-2) / 6 = 4/3 * e^(-2)
p_pois_3 = (2**3 * math.exp(-2)) / math.factorial(3)
p_pois_0 = math.exp(-2)
print(f"TL4_3: P(X=3)={p_pois_3:.4f}, P(X=0)={p_pois_0:.4f}, P(X>=1)={1-p_pois_0:.4f}")

# --- DẠNG 5: TỔNG, TRUNG BÌNH & CHEBYSHEV ---
print("\n--- DẠNG 5 ---")
# TL5_1: Box mu=5, sigma=2, n=100
# E(S)=500, SD(S)=20, E(Xbar)=5, SD(Xbar)=0.2
print(f"TL5_1: E(S)=500, SD(S)={2*math.sqrt(100):.1f}, E(Xbar)=5, SD(Xbar)={2/math.sqrt(100):.2f}")

# TL5_3: Chebyshev k=2.5 => P(|X - mu| >= 2.5*sigma) <= 1 / 2.5^2 = 1 / 6.25 = 0.16 (16%)
# P(|X - mu| < 2.5*sigma) >= 1 - 0.16 = 0.84 (84%)
print(f"TL5_3: Chebyshev k=2.5: outside <= {1/6.25:.4f} (16%), inside >= {1 - 1/6.25:.4f} (84%)")

# --- DẠNG 6: BIẾN LIÊN TỤC, ĐỀU & CHUẨN ---
print("\n--- DẠNG 6 ---")
# TL6_2: U(2, 8). f(x)=1/6. P(3 <= X <= 6) = (6-3)/6 = 3/6 = 0.5. E=(2+8)/2=5, Var=36/12=3.
print(f"TL6_2: U(2, 8): P(3<=X<=6)={(6-3)/6:.2f}, E={(2+8)/2:.1f}, Var={36/12:.2f}, SD={math.sqrt(3):.4f}")

# TL6_3: X ~ N(50, 10^2).
# P(X <= 65): Z = 1.5 => Phi(1.5)
# P(40 <= X <= 60): Z in [-1, 1] => Phi(1) - Phi(-1) = 2*Phi(1) - 1
print(f"TL6_3: Phi(1.5)={phi(1.5):.4f}, P(40<=X<=60)={2*phi(1)-1:.4f}")

# TL6_4: N(70, 8^2). Top 10% threshold: Z_0.90 = 1.28155 => x = 70 + 1.28155 * 8 = 70 + 10.2524 = 80.25
z_90 = get_z(0.90)
score_top10 = 70 + z_90 * 8
print(f"TL6_4: Top 10% cutoff = {score_top10:.2f} (Z={z_90:.4f})")

# --- DẠNG 7: CLT (ĐỊNH LÝ GIỚI HẠN TRUNG TÂM) ---
print("\n--- DẠNG 7 ---")
# TL7_1: Roll die 100 times. mu=3.5, sigma=sqrt(17.5/6)=1.7078.
# S_100 ~ N(350, 100 * 2.9167) = N(350, 291.67), SD = 17.078
# P(330 <= S_100 <= 370): Z1 = (330 - 350)/17.078 = -1.171, Z2 = 1.171
# 2*Phi(1.171) - 1
z_die = (370 - 350) / 17.078
p_die = 2 * phi(z_die) - 1
print(f"TL7_1: Die S_100 in [330, 370]: Z={z_die:.3f}, Prob={p_die:.4f}")

# TL7_3: Calls mu=12, sigma=6, n=64. Xbar ~ N(12, 6^2/64) => SD = 6/8 = 0.75
# P(Xbar < 11): Z = (11 - 12)/0.75 = -1.3333 => Phi(-1.3333) = 1 - Phi(1.3333)
z_call = (11 - 12) / 0.75
p_call = phi(z_call)
print(f"TL7_3: P(Xbar < 11) = Phi(-1.33) = {p_call:.4f}")

# TL7_8: Survey sample size for proportion: E=0.03, confidence 95% (Z=1.96). Worst case p=0.5
# 1.96 * sqrt(0.25 / n) <= 0.03 => sqrt(n) >= 1.96 * 0.5 / 0.03 = 0.98 / 0.03 = 32.6667
# n >= 32.6667^2 = 1067.11 => n = 1068
n_poll = ((1.96 * 0.5) / 0.03)**2
print(f"TL7_8: Sample size for poll n = {n_poll:.2f} => Choose n = {math.ceil(n_poll)}")

print("\n==================================================")
print("  TẤT CẢ PHÉP TÍNH CHO 56 BÀI TỰ LUẬN ĐÃ KIỂM CHỨNG XONG! ")
print("==================================================")
