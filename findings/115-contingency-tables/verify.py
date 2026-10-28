"""Recompute the quoted inverse-gap bound. Does not re-derive the proof."""
def certificate(d):
    U = d ** 20
    R = U                      # worst case R = U
    A0 = 2 + 2 * d * (U + 1) ** 2
    return 128 * d * d * ((1 + 2 * d * d) * d * R * (R + 1) * A0 + 2)

for d in range(14, 201):
    K = certificate(d)
    assert K <= 24832 * d ** 86, d
print("115 PASS: K' <= 24832 d^86 for every d in 14..200")
