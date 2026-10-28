"""Recompute the arithmetic quoted in the README. Does not re-derive the proof."""
from math import sqrt

def close(x, y, rel=1e-9):
    assert abs(x - y) <= rel * max(1.0, abs(y)), (x, y)

A = 48 * (1 + sqrt(162)) ** 2
B = 28.0
C_displayed = sqrt(A + B)
C_opt = sqrt(3) / 2 ** (1 / 3) * A ** (1 / 6) * B ** (1 / 3)
h_multiplier = (2 * A / B) ** (1 / 3)

close(C_displayed, 95.25691847782163)
close(C_opt, 19.05512405146923)
close(1 - C_opt / C_displayed, 0.7999607340236838)
close(h_multiplier, 8.645184586116219)

# Joint centered-kernel constants for the square source / unit-ball target.
d, R2, PK, absK, L2 = 2, 2.0, 4.0, 4.0, 1.0
kappa = (4 * sqrt(2) - 5) / 3
alpha = 4 + 4 * kappa
beta = 4 * kappa
lam = (beta + sqrt(beta * beta + 8 * alpha * beta)) / (2 * alpha)
C0 = (2 + sqrt(1.5)) ** 2
Aj = 4 * d * (1 + lam) * R2 * (1 + sqrt(C0)) ** 2
Bj = (alpha + beta / lam) * L2 * PK / absK
C_joint = sqrt(3) / 2 ** (1 / 3) * Aj ** (1 / 6) * Bj ** (1 / 3)

close(kappa, 0.21895141649746006507)
close(lam, 0.69587375404716932)
close(Aj, 484.3000, 1e-4)
close(Bj, 6.134375, 1e-6)
close(C_joint, 7.052230, 1e-5)
assert C_joint < 7.1, "quoted rational upper bound C <= 71/10"

print("374 PASS: 95.2569184778 -> 19.0551240515 (-79.9961%), joint 7.05223039")
