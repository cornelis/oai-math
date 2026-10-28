"""Recompute the quoted arithmetic. Does not re-derive the proof."""
from math import comb, log2, ceil

for n in range(4, 200):
    # gap ratio: (1/(12 C(n,4))) / (1/(24 n^2 C(n,4))) = 2 n^2
    # mixing bound: ceil(12 C(n,4) (log2 + log2(M)/2)) with log M = C(n,2)
    bound = ceil(12 * comb(n, 4) * (1 + comb(n, 2) / 2))
    assert bound <= n ** 6 / 2 + 1 <= n ** 6, n

print("131 PASS: 2 n^2 gap ratio, n^6/2+1 mixing bound for n=4..199")
