import numpy as np
import math
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== VERIFY CỤM E CALCULATIONS ===")

# --- 1. Continuous RV, pdf and cdf (Bài E1, E2) ---
# Slide 82-83 (Bài tập 2):
# F(x) = x^2 / 9 on [0, b], F(b) = 1 => b^2 / 9 = 1 => b = 3
# f(x) = F'(x) = 2x / 9 on (0, 3)
# E(X) = integral_0^3 x * (2x/9) dx = 2/9 * [x^3 / 3]_0^3 = 2/9 * 9 = 2.0
# E(X^2) = integral_0^3 x^2 * (2x/9) dx = 2/9 * [x^4 / 4]_0^3 = 2/9 * 81/4 = 4.5
# Var(X) = 4.5 - 2^2 = 0.5
b_val = math.sqrt(9)
e_x_e1 = (2/9) * (3**3 / 3)
e_x2_e1 = (2/9) * (3**4 / 4)
var_x_e1 = e_x2_e1 - e_x_e1**2
sd_x_e1 = math.sqrt(var_x_e1)
print(f"Bài tập 2: b = {b_val}, E(X) = {e_x_e1:.4f}, E(X^2) = {e_x2_e1:.4f}, Var(X) = {var_x_e1:.4f}, SD = {sd_x_e1:.4f}")
assert b_val == 3.0
assert e_x_e1 == 2.0
assert var_x_e1 == 0.5

# Slide 49 (Ví dụ 13): f(x) = 2x on (0, 1)
# E(X) = integral 2x^2 dx = 2/3
# E(X^2) = integral 2x^3 dx = 2/4 = 0.5
# Var(X) = 0.5 - (2/3)^2 = 1/2 - 4/9 = 1/18 approx 0.05556
e_v13 = 2/3
var_v13 = 0.5 - (2/3)**2
sd_v13 = math.sqrt(1/18)
print(f"Ví dụ 13: E(X) = {e_v13:.4f}, Var(X) = {var_v13:.5f} (1/18), SD = {sd_v13:.4f}")
assert np.isclose(var_v13, 1/18)

# --- 2. Uniform Distribution (Bài E3) ---
# U(0, 10): f(x) = 1/10
# P(X < 3) = 3 / 10 = 0.3
# E(X) = (0 + 10) / 2 = 5.0
# Var(X) = (10 - 0)^2 / 12 = 100 / 12 = 8.3333
var_unif = 100 / 12
print(f"U(0, 10): P(X < 3) = 0.3, E = 5.0, Var = {var_unif:.4f}")
assert np.isclose(var_unif, 25/3)

# --- 3. Normal Distribution (Bài E4) ---
# Slide 84-85 (Bài tập 3: Thang máy 10 người):
# X_i ~ N(65, 5^2), S_10 = sum_{i=1}^10 X_i ~ N(650, 10 * 25) = N(650, 250)
# SD(S_10) = 5 * sqrt(10) = 15.811388
# P(S_10 <= 700): Z = (700 - 650) / (5 * sqrt(10)) = 50 / 15.811388 = 3.162277
# Standard normal cdf at Z = 3.1623:
# Phi(3.1623) approx 0.999216
z_elevator = (700 - 650) / (5 * math.sqrt(10))
# Using pure python error function: Phi(z) = 0.5 * (1 + erf(z / sqrt(2)))
phi_elevator = 0.5 * (1 + math.erf(z_elevator / math.sqrt(2)))
print(f"Thang máy: Z = {z_elevator:.4f}, Phi(Z) = {phi_elevator:.4f}")
assert np.isclose(z_elevator, 3.162277, atol=1e-4)
assert np.isclose(phi_elevator, 0.9992, atol=1e-3)

# Slide 57 (Ví dụ 15: Điểm thi N(70, 10^2)):
# P(X >= 85): Z = (85 - 70) / 10 = 1.5 => 1 - Phi(1.5) = 1 - 0.93319 = 0.0668
# P(60 <= X <= 80): Z in [-1, 1] => Phi(1) - Phi(-1) = 2*Phi(1) - 1 approx 0.6827
phi_1 = 0.5 * (1 + math.erf(1 / math.sqrt(2)))
phi_15 = 0.5 * (1 + math.erf(1.5 / math.sqrt(2)))
print(f"Ví dụ 15: P(X >= 85) = {1 - phi_15:.4f}, P(60 <= X <= 80) = {2*phi_1 - 1:.4f}")
assert np.isclose(phi_1, 0.84134, atol=1e-4)
assert np.isclose(phi_15, 0.93319, atol=1e-4)

# --- 4. Exponential Distribution (Bài E5) ---
# Slide 86-88 (Bài tập 4: Khoảng cách sinh viên đến trường Exp(lambda = 1/5 = 0.2)):
# E(X) = 5 km, SD(X) = 5 km
# 1. P(X > 10) = exp(-10/5) = exp(-2) approx 0.135335
p_gt_10 = math.exp(-2)
print(f"Bài tập 4 Ý 1: P(X > 10) = exp(-2) = {p_gt_10:.4f}")
assert np.isclose(p_gt_10, 0.1353, atol=1e-3)

# 2. S_100 approx N(500, 2500), SD = 50. P(S_100 <= 300) = Phi((300-500)/50) = Phi(-4) approx 0.00003
z_s100 = (300 - 500) / 50
phi_neg4 = 0.5 * (1 + math.erf(-4 / math.sqrt(2)))
print(f"Bài tập 4 Ý 2: Phi(-4) = {phi_neg4:.6f}")
assert np.isclose(phi_neg4, 0.0000317, atol=1e-5)

# 3. X_bar_100: SD = 5 / sqrt(100) = 0.5. P(4.9 < X_bar_100 < 5.2):
# Z1 = (4.9 - 5) / 0.5 = -0.2, Z2 = (5.2 - 5) / 0.5 = 0.4
# Phi(0.4) - Phi(-0.2) = 0.6554 - 0.4207 = 0.2347
phi_04 = 0.5 * (1 + math.erf(0.4 / math.sqrt(2)))
phi_neg02 = 0.5 * (1 + math.erf(-0.2 / math.sqrt(2)))
prob_xbar100 = phi_04 - phi_neg02
print(f"Bài tập 4 Ý 3: Phi(0.4) - Phi(-0.2) = {phi_04:.4f} - {phi_neg02:.4f} = {prob_xbar100:.4f}")
assert np.isclose(prob_xbar100, 0.2347, atol=1e-3)

# 4. Single student: P(4.9 < X < 5.2) = exp(-4.9/5) - exp(-5.2/5) = exp(-0.98) - exp(-1.04)
p_single = math.exp(-0.98) - math.exp(-1.04)
print(f"Bài tập 4 Ý 4: exp(-0.98) - exp(-1.04) = {p_single:.4f}")
assert np.isclose(p_single, 0.0219, atol=1e-3)

# 5. X_bar_36: SD = 5 / 6 approx 0.8333. P(4.9 < X_bar_36 < 5.2):
# Z1 = -0.1 / (5/6) = -0.12, Z2 = 0.2 / (5/6) = 0.24
# Phi(0.24) - Phi(-0.12)
phi_024 = 0.5 * (1 + math.erf(0.24 / math.sqrt(2)))
phi_neg012 = 0.5 * (1 + math.erf(-0.12 / math.sqrt(2)))
prob_xbar36 = phi_024 - phi_neg012
print(f"Bài tập 4 Ý 5: Phi(0.24) - Phi(-0.12) = {phi_024:.4f} - {phi_neg012:.4f} = {prob_xbar36:.4f}")
assert np.isclose(prob_xbar36, 0.1426, atol=1e-3)

# --- 5. CLT Sample Size Determination (Bài E6, Bài tập 5 Slide 89-91) ---
# Components: mu = 100, sigma = 30.
# S_n >= 2000 with prob >= 0.95.
# (100n - 2000) / (30 * sqrt(n)) >= z_0.05 = 1.64485
# Let u = sqrt(n) > 0.
# 100 u^2 - 2000 >= 1.64485 * 30 * u = 49.3455 u
# 100 u^2 - 49.3455 u - 2000 >= 0
# Discriminant Delta = (-49.3455)^2 - 4 * 100 * (-2000) = 2434.978 + 800000 = 802434.978
# sqrt(Delta) = 895.787
# u >= (49.3455 + 895.787) / 200 = 945.1325 / 200 = 4.72566
# n = u^2 >= 4.72566^2 = 22.3319
# Test n = 22:
z_22 = (100 * 22 - 2000) / (30 * math.sqrt(22)) # 200 / 140.71 = 1.4213
phi_22 = 0.5 * (1 + math.erf(z_22 / math.sqrt(2)))
# Test n = 23:
z_23 = (100 * 23 - 2000) / (30 * math.sqrt(23)) # 300 / 143.87 = 2.0851
phi_23 = 0.5 * (1 + math.erf(z_23 / math.sqrt(2)))
print(f"Bài tập 5 Slide 91:")
print(f"  n = 22: Z = {z_22:.4f}, prob = {phi_22:.4f} (Slide: 0.9224)")
print(f"  n = 23: Z = {z_23:.4f}, prob = {phi_23:.4f} (Slide: 0.9815)")
assert phi_22 < 0.95
assert phi_23 >= 0.95
print(f"  => Chosen n = 23 components (1 active + 22 spare)!")

print("\n=== ALL CỤM E CALCULATIONS VERIFIED SUCCESSFULLY! ===")
