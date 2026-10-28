"""Recompute the quoted arithmetic. Does not re-derive the proof."""
from fractions import Fraction
from math import log

# entropy term: ln(256) -> ln(4) for 64 equal-mass four-state blocks
assert abs((1 - log(4) / log(256)) - 0.75) < 1e-12

# log primitive: K = 16B+8 terms, error at most (50B+2) 3^(-2K)
for B in range(1, 60):
    K = 16 * B + 8
    err = Fraction(50 * B + 2, 3 ** (2 * K))
    assert err <= Fraction(1, 2 ** (31 * B + 10)), B
    assert err < Fraction(1, 2 ** (20 * B)), B
print("121 PASS: 75% entropy-term cut; 2^-31B-10 < G^-20 for B=1..59")
