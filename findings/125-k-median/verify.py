"""Check the quoted constants against the small numbers file."""
import json
from fractions import Fraction
from pathlib import Path

values = json.loads((Path(__file__).with_name("values.json")).read_text())

C_new = int(values["C_new"])
assert C_new.bit_length() == values["C_new_bits"] == 659
assert 2 ** 658 <= C_new < 2 ** 659

# C_original >= 2^4014 because it has 4015 bits, so the ratio exceeds 2^4014/C_new.
assert values["C_original_bits"] - C_new.bit_length() == 3356
assert Fraction(2 ** 4014, C_new) > 2 ** values["C_gain_lower_power_of_two"]

sigma_new = Fraction(values["assembled_sigma_new"])
sigma_original = Fraction(values["assembled_sigma_original"])
assert sigma_new < Fraction(1, 2 ** 1300)
assert sigma_new / sigma_original > 2 ** values["assembled_gap_gain_lower_power_of_two"]

# The strictness factor is quoted, not recomputed here.
assert values["same_T_strictness_gap_gain"] == 84

print("125 PASS: 659-bit C_new (gain >2^3355), sigma_new <2^-1300, assembled gain >2^6719")
