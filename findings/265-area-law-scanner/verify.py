"""Check the stated parameter choices for the local skew bound."""
from fractions import Fraction

choices = [
    (Fraction(3, 8), Fraction(1, 5), Fraction(1, 40)),
    (Fraction(49, 100), Fraction(1, 100), Fraction(1, 200)),
]
for q, xi, slack in choices:
    assert q < Fraction(1, 2), q
    v = (1 - xi) / 2
    assert v > q, (q, xi)
    assert v - q == slack, (q, xi, v - q)

print("265 PASS: q<1/2, (1-xi)/2>q with slacks 1/40 and 1/200")
