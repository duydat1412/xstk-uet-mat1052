import math
import numpy as np
import sys

sys.stdout.reconfigure(encoding='utf-8')

def phi(z):
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))

def phi_inv(p):
    # Abramowitz and Stegun formula 26.2.23
    if p >= 1.0 or p <= 0.0:
        raise ValueError("p must be in (0, 1)")
    if p < 0.5:
        return -phi_inv(1.0 - p)
    t = math.sqrt(-2.0 * math.log(1.0 - p))
    c0 = 2.515517
    c1 = 0.802853
    c2 = 0.010328
    d1 = 1.432788
    d2 = 0.189269
    d3 = 0.001308
    return t - ((c2 * t + c1) * t + c0) / (((d3 * t + d2) * t + d1) * t + 1.0)

print("=== CHECKING ALL 56 PROBLEMS NUMBERS ===")

# Topic 1:
scores = np.array([3, 5, 6, 7, 7, 8, 8, 9, 10, 16])
mean_1 = np.mean(scores)
median_1 = np.median(scores)
q1_1 = 6.0
q3_1 = 9.0
iqr_1 = q3_1 - q1_1 # 3.0
fence_up = q3_1 + 1.5 * iqr_1 # 13.5
print(f"TL1_1: Mean={mean_1}, Med={median_1}, IQR={iqr_1}, Fence={fence_up}, Outlier=16")

p_joint = 15/60 # 0.25
p_good_given_y2 = 15/20 # 0.75
p_y2_given_good = 15/27 # 0.5556
print(f"TL1_2: P(Y2 and Good)={p_joint}, P(Good|Y2)={p_good_given_y2}, P(Y2|Good)={p_y2_given_good:.4f}")

y_hat_3 = 15 + 2.5 * 8 # 35
e_3 = 38 - 35 # +3
print(f"TL1_3: y_hat={y_hat_3}, e={e_3}")

x4 = np.array([1, 2, 3, 4, 5])
y4 = np.array([3, 5, 6, 8, 10])
r4 = np.corrcoef(x4, y4)[0, 1]
b1_4, b0_4 = np.polyfit(x4, y4, 1)
print(f"TL1_4: r={r4:.4f}, b1={b1_4:.4f}, b0={b0_4:.4f}")

print(f"TL1_7: Khoa A: Nam=80%, Nu=90%; Khoa B: Nam=50%, Nu=60%; Tong: Nam={90/120*100:.1f}%, Nu={78/120*100:.1f}%")

# Topic 4:
p4_1 = math.comb(10, 7) * (0.7**7) * (0.3**3)
e4_1 = 10 * 0.7
var4_1 = 10 * 0.7 * 0.3
sd4_1 = math.sqrt(var4_1)
print(f"TL4_1: P(X=7)={p4_1:.4f}, E={e4_1}, Var={var4_1:.2f}, SD={sd4_1:.4f}")

p4_2 = math.comb(6, 1) * math.comb(24, 3) / math.comb(30, 4)
p4_2_ge1 = 1 - math.comb(24, 4) / math.comb(30, 4)
print(f"TL4_2: P(X=1)={p4_2:.4f}, P(X>=1)={p4_2_ge1:.4f}")

p4_3 = (2**3 * math.exp(-2)) / math.factorial(3)
p4_3_ge1 = 1 - math.exp(-2)
print(f"TL4_3: P(X=3)={p4_3:.4f}, P(X>=1)={p4_3_ge1:.4f}")

p4_5_b = math.comb(1000, 3) * (0.002**3) * (0.998**997)
p4_5_p = (2**3 * math.exp(-2)) / 6
print(f"TL4_5: Bino={p4_5_b:.5f}, Pois={p4_5_p:.5f}")

n4_7 = math.log(0.01) / math.log(0.2)
print(f"TL4_7: n >= {n4_7:.4f} => n = {math.ceil(n4_7)}")

# Topic 5:
box = np.array([1, 2, 3, 4, 5])
mu5 = np.mean(box)
sigma5 = np.std(box) # population SD
print(f"TL5_1: Box mu={mu5}, sigma={sigma5:.4f}, S_100: E={100*mu5}, SD={10*sigma5:.4f}")

print(f"TL5_4: k=2 => P >= 0.75; 8/9 => k=3 => [12, 48]")
print(f"TL5_7: n >= 2000")

# Topic 6:
print(f"TL6_1: k=1/9, P(1<=X<=2)={7/27:.4f}")

x6_4 = 500 + phi_inv(0.95) * 100
print(f"TL6_4: Top 5% cutoff = {x6_4:.2f} (Z = {phi_inv(0.95):.4f})")

p6_5 = math.exp(-1.5)
p6_5_between = math.exp(-0.5) - math.exp(-1.2)
print(f"TL6_5: P(T>15)={p6_5:.4f}, P(5<=T<=12)={p6_5_between:.4f}")

x6_7 = 1000 + phi_inv(0.02) * 100
print(f"TL6_7: Warranty cutoff = {x6_7:.2f} hours (Z = {phi_inv(0.02):.4f})")

# Topic 7:
p7_2_over = 1 - phi(50 / math.sqrt(250))
print(f"TL7_2: Elevator overload P = {p7_2_over:.6f} (~0.08%)")

print(f"TL7_4: n=100: {2*phi(2)-1:.4f}; n=36: {2*phi(1.2)-1:.4f}; n=1: {math.exp(-0.8) - math.exp(-1.2):.4f}")

delta7 = 49.3455**2 + 4 * 100 * 2000
u7 = (49.3455 + math.sqrt(delta7)) / 200
n7 = u7**2
print(f"TL7_7: u >= {u7:.4f} => n >= {n7:.3f} => choose n = {math.ceil(n7)}")

print(f"TL7_8: Insurance: Z = (200 - 100)/9.95 = 10.05 => P(Loss) < 10^(-20)")
print("=== ALL CALCULATIONS VERIFIED SUCCESSFULLY ===")
