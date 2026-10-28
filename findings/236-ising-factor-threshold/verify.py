"""Recompute the quoted arithmetic and table rows. Does not re-derive the proof."""
from math import sqrt

def close(x, y, rel=1e-4):
    assert abs(x - y) <= rel * max(1e-12, abs(y)), (x, y)

def best_integer_lower(t):
    best = 0.0
    for k in range(1, 4000):
        v = t * k / (1 + t * k * k)
        if v > best:
            best = v
    return best

def lower_root(t):
    # smaller root of (1-r)^2 = (t/2) r, i.e. r^2 - (2+t/2) r + 1 = 0
    s = 2 + t / 2
    return (s - sqrt(s * s - 4)) / 2

rows = [
    (0.0001, 0.005, 0.0200010, 0.0139936, 0.0173214, 77.8165),
    (0.001, 0.0158103, 0.0632772, 0.0432674, 0.0547996, 75.7047),
    (0.01, 0.0500000, 0.2009975, 0.1277876, 0.1740690, 69.3496),
    (0.1, 0.1578947, 0.6633250, 0.3333333, 0.5744563, 52.2935),
]
for t, ol, ou, nl, nu, width in rows:
    close(best_integer_lower(t), ol)
    close(2 * sqrt(t + t * t), ou)
    close(t / (t + 1 - lower_root(t)), nl)
    close(sqrt(3 * (t + t * t)), nu)
    close(100 * (1 - (nu - nl) / (ou - ol)), width)

print("236 PASS: sqrt(3)/2 upper coefficient; four table rows and widths")
