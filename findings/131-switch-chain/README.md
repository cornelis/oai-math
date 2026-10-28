# 131: Mixing of the switch chain: sharper comparison, gap and mixing time

Paper: *Polynomial Mixing of the Switch Chain for Every Graphical Degree
Sequence* (comparison lemma).

In the paper's complete-host, unweighted, labeled-degree model with the lazy
four-vertex proposal, `H = sum_a h_a` is the compared operator summed over pair
fibers, and `L` is the paper's normalization quantity,
`1 - P = L/[12 C(n,4)]`, with `sum_a J_a = 2L`.

## Improvement

| Quantity | Paper | Here |
|---|---|---|
| Comparison | `H <= 2 n^2 L` | **`H <= L`** |
| Spectral-gap certificate | `gamma >= 1/(24 n^2 C(n,4))` | **`gamma >= 1/(12 C(n,4))`**, better by `2 n^2` |
| Mixing time (TV `1/4`) | `2 n^8` | **`n^6/2 + 1 <= n^6`** |
| Exact-sampler chain steps | `O(n^8)` | **`O(n^6)`** |

## Derivation

Fix a pair fiber with `N` labels and `q` assigned to the first endpoint; the
conditional space is the `q`-subsets of `{1,...,N}`. With
`J = sum_{i<j}(I - tau_{ij})` and `h = I - E`, the identity

```
J f_A = k(N-k+1) f_A - (q-k+1) sum_{a in A} f_{A \ {a}}
```

shows `J` preserves the nested spans `V_k` and acts on `V_k/V_{k-1}` by
`k(N-k+1)`. Since `k(N-k+1) - N = (k-1)(N-k) >= 0`,

```
h <= J/N <= J/2
```

on nontrivial fibers; trivial fibers contribute zero. Averaging over fibers gives
`h_a <= J_a/2`, and `sum_a J_a = 2L` yields `H <= L`.

With the paper's normalization and Poincaré inequality `Var(f) <= <f,Hf>`, the
same chain gains the stated gap, mixing-time and step-count bounds.

## Checks

`python3 verify.py` checks the `2 n^2` gap ratio and the mixing bound
`ceil(12 C(n,4)(log2 + log2(M)/2)) <= n^6/2+1` for `n = 4..199`.

## Scope and limits

- The comparison `H <= L` is proved independently of the paper's three-row and
  disjoint-pair positivity lemmas. The subset-slice mechanism is standard and
  adjacent to the paper's own three-row/contingency-table method.
- The gap, mixing-time and sampler-step consequences use the paper's upstream
  Poincaré inequality and constant-kernel statements, which were not
  independently proved.
- The correction branch still enumerates exponentially many graphs; no total
  bit-runtime improvement is claimed.
