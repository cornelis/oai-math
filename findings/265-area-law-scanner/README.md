# 265: Area-law scanner: a sub-endpoint skew power

Paper: *A two-dimensional area law from a global spectral gap* (conditional skew
lemma).

## Improvement

| Quantity | Paper | Here |
|---|---|---|
| Local skew power in `eta` | `eta^(1/8)` (after an intermediate `eta^(1/4)`) | **`eta^q`** for every fixed `0<q<1/2` |

Because `0 < eta < 1`, a larger `q` makes `eta^q` smaller: the gain is a stronger
remainder bound as `q` approaches the endpoint `1/2`, which is not reached.

No claim is made about the paper's final scanner exponent. The paper fixes
`epsilon > 0` and its theorem holds for every such `epsilon`; the values in its
own scanner table (largest `0.999952`) are already below `1 - epsilon`. With the
paper's parameter choices the local gain does not change its final exponent, so
any numerical exponent obtained by re-choosing parameters is an instance, not a
stronger theorem.

## Derivation

The manuscript interpolates on the half strip with a circle of radius `b/2`,
giving a remainder essentially `eta^(1/4)` up to a logarithm, weakened to
`eta^(1/8)`. With `ell_h = log(e d_h)` and `eta = I(x:F|U)_theta`, three-lines
gives `|F(z)| <= C m^(1-|Re z|/b)`. A smaller circle `|z| = xi b` keeps
`|f(z)-p| <= C m^(1-xi)`, and a Cauchy bound on the second-order remainder gives,
for every fixed `0<q<1/2`,

```
0 < a ell_h <= c_q   ==>   |f(a/2)| - Re f(a/2) <= C_q a^2 ell_h^4 eta^q.
```

Parameters: `q = 3/8` with `xi = 1/5`; `q = 49/100` with `xi = 1/100` and
smallness `a ell_h <= 1/6400`. In both cases the exponent budget has slack
`v - q > 0`, where `v = (1-xi)/2`: `1/40` and `1/200` respectively.

## Checks

`python3 verify.py` checks those parameter choices: `q < 1/2`, `v = (1-xi)/2 > q`,
and the two stated slacks `1/40` and `1/200`.

## Scope and limits

- Uses the source marginal-phase comparison lemma, the replica product
  calculus, physical truncation and spectral estimates, the entropy bootstrap,
  the earlier movement refinement, and the source's clearance and `L <= s_0`
  hypotheses. None of these was formalized or externally reviewed here.
- The local lemma was checked on small floating-point examples by the internal
  run; those are sanity checks, not error-certified inequalities.
- No claim about the paper's final exponent, PEPS bond dimension, or novelty.
