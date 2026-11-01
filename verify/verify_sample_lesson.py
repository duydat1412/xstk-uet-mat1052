import numpy as np

# Verify Worked Example 1 (USB Drive Capacity - Slide 79-81)
x = np.array([1, 2, 4, 8, 16], dtype=float)
p = np.array([0.05, 0.10, 0.35, 0.40, 0.10], dtype=float)

# Check sum of probabilities
assert np.isclose(np.sum(p), 1.0), "Sum of probabilities must equal 1"

# 1. Expectation E(X)
e_x = np.sum(x * p)
print(f"E(X) = {e_x:.4f} GB")

# 2. E(X^2)
e_x2 = np.sum((x**2) * p)
print(f"E(X^2) = {e_x2:.4f} GB^2")

# 3. Variance from definition: Var(X) = sum (x - mu)^2 * p
var_def = np.sum(((x - e_x)**2) * p)
print(f"Var(X) from definition = {var_def:.4f} GB^2")

# 4. Variance from shortcut: Var(X) = E(X^2) - [E(X)]^2
var_shortcut = e_x2 - (e_x**2)
print(f"Var(X) shortcut = {var_shortcut:.4f} GB^2")
assert np.isclose(var_def, var_shortcut), "Two variance formulas must match!"

# 5. Standard Deviation SD(X)
sd_x = np.sqrt(var_shortcut)
print(f"SD(X) = {sd_x:.4f} GB")

# Verify Linear Transformation Example (Slide 18-19: C to F)
# Y = 1.8 * X + 32, with E(X) = 25 deg C, SD(X) = 3 deg C, Var(X) = 9
e_y = 1.8 * 25 + 32
var_y = (1.8**2) * 9
sd_y = 1.8 * 3
print(f"\nLinear Transformation:")
print(f"E(Y) = {e_y:.2f} deg F")
print(f"Var(Y) = {var_y:.2f} deg F^2")
print(f"SD(Y) = {sd_y:.2f} deg F")

# Verify Multiple Choice Question calculations:
# X has Var(X) = 4, Y = 3X + 2.
# Correct Var(Y) = 3^2 * 4 = 36.
# Distractor 1 (forgot to square 3): 3 * 4 + 2 = 14
# Distractor 2 (added 2 after squaring): 9 * 4 + 2 = 38
# Distractor 3 (multiplied by 3 only): 3 * 4 = 12
print("\nMCQ Distractors verified:")
print(f"Correct: 3^2 * 4 = {3**2 * 4}")
print(f"Distractor 1: 3 * 4 + 2 = {3 * 4 + 2}")
print(f"Distractor 2: 9 * 4 + 2 = {9 * 4 + 2}")
print(f"Distractor 3: 3 * 4 = {3 * 4}")
