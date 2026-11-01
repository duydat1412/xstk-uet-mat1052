import numpy as np
import math
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== VERIFY CỤM B CALCULATIONS ===")

# --- 1. Probability Axioms & Basic Rules (Bài B1, B2) ---
# Dice roll: Sample space {1, 2, 3, 4, 5, 6}
# A = even = {2, 4, 6}, P(A) = 3/6 = 0.5
# B = >= 4 = {4, 5, 6}, P(B) = 3/6 = 0.5
# A cap B = {4, 6}, P(A cap B) = 2/6 = 1/3
# P(A cup B) = P(A) + P(B) - P(A cap B) = 3/6 + 3/6 - 2/6 = 4/6 = 2/3
p_a = 3/6
p_b = 3/6
p_inter = 2/6
p_union = p_a + p_b - p_inter
print(f"Dice roll: P(A union B) = {p_union:.4f} (2/3 = {2/3:.4f})")
assert np.isclose(p_union, 2/3)

# Complement rule: Toss 4 coins, P(at least 1 head) = 1 - P(no heads)
# P(no heads) = (1/2)^4 = 1/16
p_at_least_1_head = 1 - (0.5)**4
print(f"Toss 4 coins: P(at least 1 head) = {p_at_least_1_head:.4f} (15/16 = {15/16:.4f})")
assert np.isclose(p_at_least_1_head, 15/16)

# --- 2. Conditional Probability & Multiplication Rule (Bài B3) ---
# Box with 5 cards: 2 Red, 3 Black. Draw 2 cards without replacement.
# P(R1) = 2/5 = 0.4
# P(R2 | R1) = 1/4 = 0.25
# P(R1 and R2) = P(R1) * P(R2 | R1) = (2/5) * (1/4) = 2/20 = 0.1
p_r1 = 2/5
p_r2_given_r1 = 1/4
p_both_red = p_r1 * p_r2_given_r1
print(f"Draw 2 cards without replacement: P(both red) = {p_both_red:.4f} (0.1)")
assert np.isclose(p_both_red, 0.1)

# --- 3. Independence vs Disjoint (Bài B4) ---
# Independent events: P(A) = 0.3, P(B) = 0.5
# P(A cap B) = 0.3 * 0.5 = 0.15
# P(A cup B) = 0.3 + 0.5 - 0.15 = 0.65
p_ind_inter = 0.3 * 0.5
p_ind_union = 0.3 + 0.5 - p_ind_inter
print(f"Independent events: P(A cap B) = {p_ind_inter:.4f}, P(A cup B) = {p_ind_union:.4f}")
assert np.isclose(p_ind_inter, 0.15)
assert np.isclose(p_ind_union, 0.65)

# --- 4. Combinatorics (Bài B5) ---
# Choose 3 people from 10: C(10, 3) = 10! / (3! * 7!) = (10*9*8)/(3*2*1) = 120
c_10_3 = math.comb(10, 3)
p_10_3 = math.perm(10, 3)
print(f"Combinations C(10, 3) = {c_10_3}")
print(f"Permutations P(10, 3) = {p_10_3}")
assert c_10_3 == 120
assert p_10_3 == 720

# Drawing 3 balls from urn of 6 Red and 4 Blue:
# P(2 Red, 1 Blue) = [C(6, 2) * C(4, 1)] / C(10, 3) = [15 * 4] / 120 = 60 / 120 = 0.5
p_urn = (math.comb(6, 2) * math.comb(4, 1)) / math.comb(10, 3)
print(f"Urn problem: P(2 Red, 1 Blue) = {p_urn:.4f} (0.5)")
assert np.isclose(p_urn, 0.5)

print("\n=== ALL CỤM B CALCULATIONS VERIFIED SUCCESSFULLY! ===")
