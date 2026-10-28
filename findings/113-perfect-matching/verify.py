"""Recompute the quoted stage counts. Does not re-derive the proof."""
from math import comb, log, ceil

def odd_double_factorial(m):
    r = 1
    for i in range(m, 0, -2):
        r *= i
    return r

n, eps = 64, 0.1
Z0 = odd_double_factorial(n - 1)      # 63!!
D = odd_double_factorial(n - 3)       # 61!!
b = 1 + 1 / n

def stages(q, L):
    A = min(Z0 - L, q * D)
    return ceil(log(A * 32 / (eps * L)) / log(b)), A

from math import log as _log
src = ceil(_log(n ** (n / 2) * 32 / eps) / _log(b))
assert src == 8956, src
K, A = stages(32, Z0 - 32 * D)
assert A == 32 * D
assert K == 375, K
assert n + 4 * (2 * K + 2) * comb(n, 2) == 6_064_192

K64, _ = stages(64, 1)
assert K64 == 6915, K64

print("113 PASS: K=375 (from 8956), N=6,064,192; K=6915 for q=64,L=1")
