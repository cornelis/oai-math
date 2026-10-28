# 374: Sharp one-third stability of optimal transport maps

Paper: *Sharp One-Third Stability of Brenier Maps*.

## Improvement

All numbers are the paper's formula evaluated at the fixture used throughout:
uniform source on `K = [-1,1]^2` (`d=2`, `R^2 = 2`, `|K| = 4`, `P_K = 4`) and
unit-ball targets (`L = 1`).

| Quantity | Value |
|---|---:|
| Paper's formula at this fixture | `95.2569184778` |
| Optimized coefficient | **`19.0551240515`** |
| Reduction | **`79.9960734%`** |
| Optimal `h` multiplier | `8.64518458612` (paper: `1`) |
| Exponent | `1/3` (unchanged) |

A combined derivation reaches `7.05223039` (−92.60% below the displayed
constant); see *Combined extension*.

## What the paper gives

```
C_* = ( 12 d R^2 (1+sqrt(C_0))^2 + 28 L^2 P_K/|K| )^{1/2},   C_0 = 162,
E <= A w^2/h^2 + B h,   w = W_2(mu,nu),  h > 0,
A = 12 d R^2 (1+sqrt(C_0))^2,   B = 28 L^2 P_K/|K|,
```

with the particular choice `h = w^{2/3}`, although the inequality is stated for
**every** `h > 0`. At the fixture `A = 48(1+sqrt(162))^2`, `B = 28`,
`C_* = 95.2569184778`.

## Derivation

Minimize the same inequality over `h`:

```
h_* = (2A/B)^(1/3) w^{2/3},
C_opt = (sqrt(3)/2^(1/3)) A^(1/6) B^(1/3) = 19.0551240515.
```

No hypothesis, target class or exponent changes.

## Combined extension

Same fixture as above. For the centered secant `S_h u`, the error against the derivative is
convolution with `k_h(t) = sign(t)(1/2 - |t|/h)` on `|t| < h/2`;
Cauchy-Schwarz gives `∫e_u^2 <= D^2h/12`. A joint two-sided bound gives

```
∫(e_0-e_1)^2 <= D^2 kappa h,     kappa = (4 sqrt(2) - 5)/3 ~ 0.21895142.
```

With moment constant `C_mom = (2+sqrt(3/2))^2` and split `lambda ~ 0.69587375`,

```
A_joint = 4d(1+lambda)R^2(1+sqrt(C_mom))^2,
B_joint = [alpha + beta/lambda] L^2 P_K/|K|,   alpha = 4+4kappa, beta = 4kappa,
C_joint = (sqrt(3)/2^(1/3)) A_joint^(1/6) B_joint^(1/3),
```

giving `A_joint ~ 484.3`, `B_joint ~ 6.134`, `C_joint ~ 7.05223039`.

| Sufficient coefficient | Value |
|---|---:|
| Displayed manuscript constant | `95.2569184778` |
| Optimized `h` above | `19.0551240515` |
| Moment + signed forward slices | `9.03496749` |
| Exact forward kernel | `8.33178350` |
| Centered slices, separate errors | `7.44198487` |
| Joint centered kernel + new moment | `7.05223039` |

Ablation: keeping the paper's moment `162` gives `C ~ 10.44547`; keeping its
gradient inequality and only changing the moment gives `C ~ 12.86502`.

## Exact restricted-class case

For targets on one affine line the common-source coupling is the increasing
quantile coupling, and `||T_mu - T_nu||^2_{L^2} = W_2(mu,nu)^2` exactly. For a
square source and a coordinate axis this yields the optimal max-affine map by a
linear merge, with no Newton mass-fitting step.

## Checks

`python3 verify.py` recomputes both direct baselines, the optimal `h`, the
quadratic constant `C_opt`, and the joint `kappa`, `lambda`, `A_joint`,
`B_joint`, `C_joint`.

## Scope and limits

- The `19.0551240515` result uses only the paper's inequality, valid for every
  `h > 0`.
- The `7.05223039` extension also propagates through the paper's midpoint
  domination, cell differentiability, moving-target path and
  finite-approximation lemmas; those were not re-proved here.
- The percentage is regime-dependent: `C_opt/C_*` tends to `1` as `B/A` tends to
  `2`; the fixture has `B/A ~ 0.003`.
- Not an optimal universal constant, not a new exponent, not a solver speedup.
