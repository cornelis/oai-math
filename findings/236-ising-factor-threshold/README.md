# 236: Factor-of-IID threshold for the free Ising model on regular trees

Paper: *The sharp factor-of-IID threshold for the free Ising model on regular
trees*.

## Improvement

| Quantity | Paper | Here |
|---|---|---|
| Information-loss coefficient | `1/4` | **`1/3`** |
| Bound implied by the fusion identity | `2 sqrt(q_0(t))` | **`sqrt(3 q_0(t))`** |
| Same, with `q_0 <= t+t^2` | `2 sqrt(t+t^2)` | **`sqrt(3(t+t^2))`** (−13.3975%) |
| Asymptotic lower coefficient | `1/2 sqrt(t)` | **`sqrt(2) sqrt(t)`** |
| Width of the derived interval at `t=0.001` | n/a | **−75.7047%** |
| Width of the derived interval at `t=0.01` | n/a | **−69.3496%** |

The paper states only `M(t) <= C sqrt(t)` with `C` unspecified; the explicit
`2 sqrt(t+t^2)` is our substitution of its fusion identity, so those two rows
compare two derivations, not a paper constant. The `1/4` coefficient is
displayed.

Model unchanged: binary branching `b=2` (`d`-regular tree with `d = b+1 = 3`),
critical `theta^2 = 1/2`, threshold `theta <= (d-1)^(-1/2)`, exponent `sqrt(t)`.

## Upper refinement

The paper proves `M(t) >= t k/(1 + t k^2)` and its fusion argument gives

```
M(t) <= M(t) - (1/4) M(t)^2 + q_0(t),     q_0(t) <= t + t^2,
```

i.e. `M^2/4 <= q_0` and hence `2 sqrt(t+t^2)`. Retain the denominator in the
exact fusion identity: for `x = U^2, y = V^2` in `[0,1/2]`,

```
(2 - x - y)/(1 - xy) >= 4/3,
```

since both partial derivatives are nonpositive. The coefficient becomes `1/3`,
so `M(t) <= sqrt(3 q_0(t)) <= sqrt(3(t+t^2))`.

## Lower refinement

With geometric level weights `c_k = (1-r) r^k`, the critical covariance of
level spin sums is `1 + (1/2)min(k,l)` and observation noise adds `t sum c_k^2`.
The signal-to-variance bound gives

```
M(t) >= t / [ (1-r)/(1+r) + t (1 + (1/2) r^2/(1-r^2)) ].
```

Choosing the smaller root `r` of `(1-r)^2 = (t/2) r` makes the denominator
`t + 1 - r`, i.e. `M(t) >= t/(t+1-r)`.

## Numeric comparison

| `t` | Original lower | Original upper | Refined lower | Refined upper | Width reduction |
|---:|---:|---:|---:|---:|---:|
| `0.0001` | `0.00500000` | `0.0200010` | `0.0139936` | `0.0173214` | `77.8165%` |
| `0.001` | `0.0158103` | `0.0632772` | `0.0432674` | `0.0547996` | **`75.7047%`** |
| `0.01` | `0.0500000` | `0.2009975` | `0.1277876` | `0.1740690` | **`69.3496%`** |
| `0.1` | `0.1578947` | `0.6633250` | `0.3333333` | `0.5744563` | `52.2935%` |

The original lower bound is the paper's formula optimized over integer `k`.

## Checks

`python3 verify.py` recomputes the four table rows, the width reductions and
the `sqrt(3)/2` upper-coefficient ratio.

## Scope and limits

- Auxiliary analytic bounds, not simulation intervals; the factor-of-IID
  threshold and the `sqrt(t)` exponent are unchanged.
- Earlier `84.4%` / `80.5%` width reductions used looser baselines and are
  superseded by the fair `75.7047%` / `69.3496%` values.
- The quantization lemma `h^2/4` for discretized Gaussian observations is a
  separate added lemma, not a reduction of a paper constant.
