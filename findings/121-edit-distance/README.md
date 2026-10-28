# 121: Almost-linear edit distance: tighter entropy term and rational logarithms

Paper: *An Almost-Linear Approximation Scheme for Edit Distance* (regret lemma
and numerics).

**Scope note.** These are **component-level** improvements: one additive entropy
term and one arithmetic primitive. The scheme's overall `N^(1+o(1))` behaviour,
its optimizer iterations, action lists and practical feasibility are unchanged,
and range reduction is a classical technique, so no new algorithm or exponent
follows.

## Improvement

| Quantity | Paper | Here |
|---|---|---|
| Scaled entropy contribution | `h_Sigma ln d / eta` | **`sum_i h_i ln k_i / eta`** |
| Entropy term, 64 equal-mass four-state blocks | `ln 256` | **`ln 4`** (75% less in this term alone) |
| Rational logarithm summands | `G^60` | **`O(log G)`** at the same `G^-20` tolerance |
| Large-input preflight | n/a | **`O(N)` exact preflight** replacing per-target transformed scans |

Here `G = H + d_dim + 2` is the source's precision parameter
(`sigma = G^-50`, gradient tolerance `G^-20`) and `B = bit_length(G)`.

## Derivation

**Entropy.** Blocks have the same masses `beta_i` for every vector in the
compact convex set; `k_i` counts coordinates in block `i`. The chain rule gives
`H(beta) <= H(rho) <= H(beta) + A` with `A = sum_i beta_i ln k_i` (no
independence assumption). Using `Psi(0) <= H(beta)+A` (with `A <= ln d`, equality only when block masses
are proportional to block sizes) and `H(rho*) >= H(beta)` in
the source's telescoping gives

```
sum_t <f_t + kappa Delta_t, rho_t> <= sum_t <f_t, rho*> + A/eta + 2 kappa,
```

with the same costs, increment range, `eta` and `kappa`. For conditioned child
tables `beta_i = h_i/h_Sigma`, so the entropy contribution is
`sum_i h_i ln k_i / eta`; for 64 equal-mass four-state blocks `ln 256` becomes
`ln 4`.

**Rational logarithm.** Replace the paper's `G^60`-term expansion around
`b = (r-1)/(r+1)` by range reduction `r = 2^e t`, `1 <= t < 2`, and `K = 16B+8`
terms of `2 sum_k b^(2k+1)/(2k+1)`, `b = (t-1)/(t+1) in [0,1/3)`. The tail is at
most `3^(-2K)` and `|e|+1 <= 50B+2`, so the error is at most
`2^(-31B-10) < G^-20`, with one cached `ln 2` series. The Frank-Wolfe
recurrence and sampler are unchanged.

## Checks

`python3 verify.py` checks the 75% entropy-term reduction and the tail bound
`(50B+2) 3^(-2K) < 2^(-20B)` for `B = 1..59`.

## Scope and limits

- The entropy refinement uses the source's fixed-block masses and regret
  inequality; the log primitive uses only its stated tolerance. Downstream
  regret/accuracy and the full scheme are not re-proved.
- One arithmetic component and one entropy term improve; the overall
  `N^(1+o(1))` exponent and practical feasibility are unchanged.
- No novelty claim for range reduction (classical) or randomized log
  estimation.
