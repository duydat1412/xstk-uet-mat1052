import numpy as np
import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== VERIFY CỤM A CALCULATIONS ===")

# --- 1. Five-number summary and Outlier Detection (Bài A3) ---
# Data sample: exam scores of 11 students: [4, 6, 7, 7, 8, 8, 8, 9, 9, 10, 18]
scores = np.array([4, 6, 7, 7, 8, 8, 8, 9, 9, 10, 18])
n = len(scores)
mean_val = np.mean(scores)
median_val = np.median(scores)

# Q1, Q3 (using standard textbook method / interpolation)
q1 = np.percentile(scores, 25, method='weibull') # or standard median of lower half
# Let's check median of lower half [4, 6, 7, 7, 8] -> 7
# median of upper half [8, 9, 9, 10, 18] -> 9
# In python standard:
q1_h = 7.0
q3_h = 9.0
iqr = q3_h - q1_h
lower_fence = q1_h - 1.5 * iqr
upper_fence = q3_h + 1.5 * iqr
outliers = scores[(scores < lower_fence) | (scores > upper_fence)]

print(f"Scores: {scores}")
print(f"Mean = {mean_val:.4f}, Median = {median_val:.4f}")
print(f"Q1 = {q1_h}, Q3 = {q3_h}, IQR = {iqr}")
print(f"Fences: [{lower_fence}, {upper_fence}]")
print(f"Outliers detected: {outliers}")
assert 18 in outliers, "18 must be detected as an outlier"

# Sample variance and sample standard deviation (ddof=1)
s2 = np.var(scores, ddof=1)
s = np.std(scores, ddof=1)
print(f"Sample variance s^2 = {s2:.4f}, Sample SD s = {s:.4f}")

# --- 2. Contingency Table Proportions (Bài A2) ---
# Table: Year 1 vs Year 2 on Working Part-time
#                Part-time (Yes)   No   Total
# Year 1 (Năm 1)        6          24     30
# Year 2 (Năm 2)       10          10     20
# Total                16          34     50
table = np.array([[6, 24], [10, 10]])
total = 50
p_joint_y2_work = 10 / 50 # 20%
p_row_work_given_y2 = 10 / 20 # 50%
p_col_y2_given_work = 10 / 16 # 62.5%
print(f"\nContingency Table:")
print(f"P(Year 2 AND Work) = {p_joint_y2_work:.4f} (20%)")
print(f"P(Work | Year 2)   = {p_row_work_given_y2:.4f} (50%)")
print(f"P(Year 2 | Work)   = {p_col_y2_given_work:.4f} (62.5%)")

# --- 3. Linear Regression and Residuals (Bài A4) ---
# Example: y_hat = 2 + 3*x
# At x = 4, observed y = 15
x_val = 4
y_obs = 15
y_pred = 2 + 3 * x_val
res = y_obs - y_pred
print(f"\nLinear Regression:")
print(f"Predicted y_hat = {y_pred}, Observed y = {y_obs}, Residual = {res}")
assert res == 1, "Residual must be 1"

# Worked Example 3: Dataset with 5 points
# x = [1, 2, 3, 4, 5], y = [2, 3, 5, 7, 8]
x_pts = np.array([1, 2, 3, 4, 5])
y_pts = np.array([2, 3, 5, 7, 8])
r_val = np.corrcoef(x_pts, y_pts)[0, 1]
# OLS slope b1 = Cov(x, y) / Var(x)
b1, b0 = np.polyfit(x_pts, y_pts, 1)
print(f"Points x={x_pts}, y={y_pts}")
print(f"Pearson r = {r_val:.4f}")
print(f"Regression line: y_hat = {b0:.4f} + {b1:.4f} * x")
residuals = y_pts - (b0 + b1 * x_pts)
print(f"Residuals: {np.round(residuals, 4)}")
print(f"Sum of residuals = {np.sum(residuals):.6f} (must be 0)")
assert np.isclose(np.sum(residuals), 0.0), "Sum of OLS residuals must equal 0"

# --- 4. Multiple Regression with Dummy Variable (Bài A5) ---
# Model: y_hat = 10 + 2.5 * x1 + 4.0 * d2
# where x1 is study hours, d2 is 1 if Major is IT, 0 if Major is Other (Baseline)
# Student A: x1 = 5, Major = Other (d2=0) -> y_hat = 10 + 2.5*5 + 0 = 22.5
# Student B: x1 = 5, Major = IT (d2=1) -> y_hat = 10 + 2.5*5 + 4 = 26.5
# Difference = 4.0
print(f"\nMultiple Regression with Dummy:")
pred_other = 10 + 2.5 * 5 + 4.0 * 0
pred_it = 10 + 2.5 * 5 + 4.0 * 1
print(f"Pred Other: {pred_other}, Pred IT: {pred_it}, Diff: {pred_it - pred_other}")
assert pred_it - pred_other == 4.0

print("\n=== ALL CỤM A CALCULATIONS VERIFIED SUCCESSFULLY! ===")
