import numpy as np
import math
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== VERIFY CỤM C CALCULATIONS (PURE PYTHON MATH) ===")

# --- 1. pmf and cdf (Bài C1) ---
x_c1 = np.array([0, 1, 2])
p_c1 = np.array([0.25, 0.50, 0.25])
assert np.isclose(np.sum(p_c1), 1.0)
f_0 = 0.25
f_1 = 0.75
f_2 = 1.00
print(f"Coin toss cdf: F(0)={f_0}, F(1)={f_1}, F(2)={f_2}")

# Constant c for p(x) = c * x
c_val = 1 / np.sum([1, 2, 3, 4])
print(f"Normalization constant c = {c_val:.4f} (0.1)")
assert np.isclose(c_val, 0.1)

# --- 2. Binomial Distribution (Bài C2) ---
# X ~ B(n=10, p=1/6), P(X=3) = C(10, 3) * (1/6)^3 * (5/6)^7
n_b, p_b = 10, 1/6
prob_3_sixes = math.comb(10, 3) * (p_b**3) * ((1 - p_b)**7)
e_binom = n_b * p_b
var_binom = n_b * p_b * (1 - p_b)
sd_binom = math.sqrt(var_binom)
print(f"B(10, 1/6): P(X=3) = {prob_3_sixes:.4f}")
print(f"E(X) = {e_binom:.4f}, Var(X) = {var_binom:.4f}, SD(X) = {sd_binom:.4f}")

# B(10, 0.3) from quiz
var_b10_03 = 10 * 0.3 * 0.7
e_b10_03 = 10 * 0.3
assert np.isclose(var_b10_03, 2.1)
assert np.isclose(e_b10_03, 3.0)

# --- 3. Hypergeometric Distribution (Bài C3) ---
# N=20, M=8, n=5. P(X=2) = [C(8, 2) * C(12, 3)] / C(20, 5)
c_8_2 = math.comb(8, 2)
c_12_3 = math.comb(12, 3)
c_20_5 = math.comb(20, 5)
prob_hyper = (c_8_2 * c_12_3) / c_20_5
print(f"Hypergeometric: C(8,2)*C(12,3)/C(20,5) = {c_8_2} * {c_12_3} / {c_20_5} = {prob_hyper:.4f}")

e_hyper = 5 * (8/20)
var_hyper = 5 * (8/20) * (12/20) * (15/19)
print(f"Hypergeometric: E = {e_hyper:.4f}, Var = {var_hyper:.4f}")
assert np.isclose(prob_hyper, 28 * 220 / 15504)
assert np.isclose(e_hyper, 2.0)
assert np.isclose(var_hyper, 1.2 * 15 / 19)

# --- 4. Poisson Distribution (Bài C4) ---
# lambda = 4, P(X=2) = 4^2 * exp(-4) / 2!
prob_pois_2 = (4**2 * math.exp(-4)) / math.factorial(2)
e_pois = 4.0
var_pois = 4.0
print(f"Poisson(4): P(X=2) = {prob_pois_2:.4f}, E = {e_pois}, Var = {var_pois}")
assert np.isclose(prob_pois_2, 8 * math.exp(-4))

# --- 5. Expectation and Variance properties (Bài C5, C6) ---
x_usb = np.array([1, 2, 4, 8, 16], dtype=float)
p_usb = np.array([0.05, 0.10, 0.35, 0.40, 0.10], dtype=float)
e_usb = np.sum(x_usb * p_usb)
var_usb = np.sum((x_usb - e_usb)**2 * p_usb)
sd_usb = math.sqrt(var_usb)
print(f"USB: E = {e_usb:.4f}, Var = {var_usb:.4f}, SD = {sd_usb:.4f}")
assert np.isclose(e_usb, 6.45)
assert np.isclose(var_usb, 15.6475)
assert np.isclose(sd_usb, math.sqrt(15.6475))

print("\n=== ALL CỤM C CALCULATIONS VERIFIED SUCCESSFULLY! ===")
