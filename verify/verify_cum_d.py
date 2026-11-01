import numpy as np
import math
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== VERIFY CỤM D CALCULATIONS ===")

# --- 1. Box Model (Bài D1) ---
# Slide 27-28: Box with 10 tickets: [0, 0, 1, 1, 1, 2, 3, 3, 4, 4]
box = np.array([0, 0, 1, 1, 1, 2, 3, 3, 4, 4], dtype=float)
n_box = len(box)
mu_box = np.mean(box)
# Note: In Slide 28, population variance of the box tickets:
# mu = (0*2 + 1*3 + 2*1 + 3*2 + 4*2) / 10 = (0 + 3 + 2 + 6 + 8) / 10 = 19 / 10 = 1.9
# sum (x - mu)^2 / 10:
# (0 - 1.9)^2 * 2 = 3.61 * 2 = 7.22
# (1 - 1.9)^2 * 3 = 0.81 * 3 = 2.43
# (2 - 1.9)^2 * 1 = 0.01 * 1 = 0.01
# (3 - 1.9)^2 * 2 = 1.21 * 2 = 2.42
# (4 - 1.9)^2 * 2 = 4.41 * 2 = 8.82
# sum = 7.22 + 2.43 + 0.01 + 2.42 + 8.82 = 20.90
# var = 20.90 / 10 = 2.09
# sigma = sqrt(2.09) = 1.44568
var_box = np.mean((box - mu_box)**2)
sigma_box = math.sqrt(var_box)
print(f"Box tickets: {box}")
print(f"mu = {mu_box:.4f} (1.9), var = {var_box:.4f} (2.09), sigma = {sigma_box:.5f} (1.44568)")
assert np.isclose(mu_box, 1.9)
assert np.isclose(var_box, 2.09)

# --- 2. Sum and Average (Bài D2) ---
# Slide 29-30: Draw n=25 with replacement:
# E(S_25) = 25 * 1.9 = 47.5
# SD(S_25) = sigma * sqrt(25) = 1.44568 * 5 = 7.2284
# E(X_bar_25) = 1.9
# SD(X_bar_25) = sigma / sqrt(25) = 1.44568 / 5 = 0.2891
n_draw = 25
e_s25 = n_draw * mu_box
sd_s25 = sigma_box * math.sqrt(n_draw)
e_xbar25 = mu_box
sd_xbar25 = sigma_box / math.sqrt(n_draw)
print(f"Draw n=25:")
print(f"  E(S_25) = {e_s25:.4f}, SD(S_25) = {sd_s25:.4f}")
print(f"  E(X_bar_25) = {e_xbar25:.4f}, SD(X_bar_25) = {sd_xbar25:.4f}")
assert np.isclose(e_s25, 47.5)
assert np.isclose(sd_s25, 7.228434, atol=1e-4)
assert np.isclose(sd_xbar25, 0.289136, atol=1e-4)

# Quiz: Box with sigma = 2, draw 100 times:
# SD(S_100) = 2 * sqrt(100) = 20
# SD(X_bar_100) = 2 / sqrt(100) = 0.2
assert np.isclose(2 * math.sqrt(100), 20.0)
assert np.isclose(2 / math.sqrt(100), 0.2)

# --- 3. Chebyshev Inequality (Bài D3) ---
# P(|X - mu| >= k * sigma) <= 1 / k^2
# k = 2 -> 1/4 = 0.25
# k = 3 -> 1/9 = 0.1111
assert np.isclose(1 / (2**2), 0.25)
assert np.isclose(1 / (3**2), 1/9)

# Chebyshev on sample mean:
# P(|X_bar_n - mu| >= epsilon) <= sigma^2 / (n * epsilon^2)
# Suppose sigma = 2, epsilon = 0.5. To have P <= 0.05:
# 4 / (n * 0.25) <= 0.05 => 16 / n <= 0.05 => n >= 16 / 0.05 = 320
n_cheby_sample = 4 / (0.25 * 0.05)
print(f"Sample size n required by Chebyshev (sigma=2, eps=0.5, alpha=0.05): {n_cheby_sample}")
assert np.isclose(n_cheby_sample, 320.0)

print("\n=== ALL CỤM D CALCULATIONS VERIFIED SUCCESSFULLY! ===")
