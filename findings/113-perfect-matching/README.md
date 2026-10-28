# 113: Perfect-matching FPRAS: fewer annealing stages from a certified count bound

Paper: *A Fully Polynomial Randomized Approximation Scheme for Perfect
Matchings in General Graphs* (annealing schedule and padding bias).

## Improvement

The paper chooses the stage count `K >= 1` from `n^(n/2) b^(-K) <= epsilon/32`
with `b = 1+1/n`. For a graph with `q` nonedges, `Z_0 = (n-1)!!` and a certified
lower bound `L <= Z`, the condition

```
A = min(Z_0 - L, q (n-3)!!),        A b^(-K) <= epsilon L / 32
```

suffices for the first such `K`, independently of the paper's mixing arguments.

| Case | Paper `K` | Here |
|---|---:|---:|
| `n=64, q=32, epsilon=.1` with `L = Z_0 - q(n-3)!!` | `8956` | **`375`** (−95.8%) |
| same, enlarged-graph size `N` | `144,458,560` | **`6,064,192`** |
| `n=64, q=64, L=1` | `8956` | **`6915`** (−22.8%) |
| `q <= rho(n-1)`, fixed `rho < 1` | `O(n^2 log n + n log(1/epsilon))` | **`O(n log(1/epsilon))`** |

`N = n + 4p C(n,2)` with `p = 2K+2` is the size of the enlarged graph built by
replacing each logical edge with a path (the paper's equation for `N`). The
`375` stage count relies on the certified dense bound; it is not a general
statement for sparse graphs.

## Derivation

At most `Z_0 - L` complete-graph matchings are absent from `G`, and each
specified nonedge lies in exactly `(n-3)!!` complete-graph perfect matchings, so
a union bound gives `A` absent matchings. Every absent matching has at least one
nonedge and hence activity at most `b^(-j)`, so

```
0 <= Z_a - Z <= A a,        (Z_a - Z)/Z <= A a / L,
```

and `A b^(-K) <= epsilon L/32` controls the padding bias with the same error
budget. The chain still uses `K >= 1`, at most `K` scale updates and budgets
proportional to `1/K`, so the replaced cutoff is no larger.

On the dense class the union bound `Z >= Z_0 - q(n-3)!!` is certified and
positive for `q < n-1`; using it as `L` gives `A/L <= q/(n-1-q)`.

## Checks

`python3 verify.py` recomputes the paper's `K = 8956`, our `K = 375`, the lifted
`N = 6,064,192` and the `q=64` case `K = 6915`.

## Scope and limits

- Propagation to the paper's algorithm uses its balance, bag, operator and
  bounded-sampler lemmas; those were not independently proved.
- No new unrestricted exponent, no improvement to the paper's polynomial
  worst-case runtime, and no measured FPRAS improvement.
- The dense-class bound is special to few nonedges; sparse complements can be
  counted exactly instead.
