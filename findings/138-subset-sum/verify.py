"""Recompute the quoted arithmetic. Does not re-derive the proof."""
from fractions import Fraction

# 45-term rational lower bound for 2^0.5156, using the truncated ln 2 constant
term = Fraction(5156, 10000) * Fraction(693147180559, 10 ** 12)
partial = Fraction(0)
fact = 1
for i in range(46):
    if i:
        fact *= i
    partial += term ** i / fact
assert Fraction(1429584295, 10 ** 9) < partial          # 1.429584295 < sum
assert 1429584295 / 10 ** 9 < 2 ** 0.5156              # moment bound < 2^0.5156

eta, eps = 0.51772, 1e-8
old = -eta + 0.5169 + 48 * eps
new = -eta + 0.5157 + 48 * eps
assert abs(old - (-0.00081952)) < 1e-12, old
assert abs(new - (-0.00201952)) < 1e-12, new

print("138 PASS: moment lower bound, exponents -0.00081952 -> -0.00201952")
