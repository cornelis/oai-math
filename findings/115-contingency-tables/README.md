# 115: Contingency tables: sharper child transport and inverse-gap certificate

Paper: *Exact Uniform Sampling of Contingency Tables with Arbitrary Margins*
(conditional transport and the child-log-concavity lemma); the cell-bounded
counting companion is context only.

**Scope note.** The gain is against the paper's **internal** `O(d^126)`
calculation, **not** its `O(d^160)` headline statement, and both bounds are
astronomically large: this sharpens a certificate, it does not yield a usable
algorithm.

## Improvement

| Quantity | Paper | Here |
|---|---|---|
| Between-child variance | every endpoint pair charged separately | **`V <= R(R+1) sum_j min(z_j,z_{j+1})(h_j - h_{j+1})^2`** |
| Transversal coefficient | `4 d^2 (U+1)^6` | **`K_t = d R (R+1) A_0`** |
| Inverse-gap certificate | `O(d^126)` internal (`d^160` headline) | **`K' <= 24,832 d^86`** for `d >= 14` (hence `<= d^90`) |

with `d = 10 + (m+1)(n+1)`, `U = d^20`, `A_0 = 2 + 2d(U+1)^2`, and `R` the
integer span of a child support (`R < U` on feasible small states).

## Derivation

**Child mass.** With child masses `z_j`, means `h_j` and total `Z`, the
between-child variance is
`V = (1/Z) sum_{a<b} z_a z_b (h_a - h_b)^2`. Child masses are log-concave with
interval support. For each adjacent cut, log-concavity makes the smaller side at
most `(R+1) min(z_j,z_{j+1})`; telescoping and Cauchy-Schwarz give

```
V <= R(R+1) sum_j min(z_j,z_{j+1})(h_j - h_{j+1})^2,
```

including zero boundary masses, instead of charging every endpoint pair.

**Edge ownership.** The source gives
`min(z_j,z_{j+1})(h_j-h_{j+1})^2 <= A_0 E_sigma` per adjacent pair. In its
signed-flow construction at level `l`, every used edge belongs to at most one
level, so the same inequality holds with the level energy `E_sigma,l` and
`sum_l E_sigma,l <= E_sigma`; summing over adjacent pairs therefore pays `A_0`
once, giving `V <= R(R+1) A_0 E_sigma` and `K_t = dR(R+1)A_0`. With the ideal-kernel factor `128 d^2`:

```
K' = 128 d^2 [ (1+2d^2) d R (R+1)(2 + 2d(U+1)^2) + 2 ].
```

## Checks

`python3 verify.py` evaluates `K'` at `d = 14, 15, 20, 50, 100` and checks
`K' <= 24,832 d^86`. The README's `d >= 14` claim is illustrated, not proved, by
these samples.

## Scope and limits

- Global consequences use the source's child signature/log-concavity,
  resistance construction, repair, reversibility and dense-draw accuracy
  statements; those were not re-proved.
- The signed flow itself was not constructed in the checks.
- This is a local certificate sharpening, not a full sampler implementation; it
  does not transfer to the bounded counting manuscript.
