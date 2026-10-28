# 138: Subset sum: sharper checksum decay, deficiency variance and collision bound

Paper: *Subset Sum in Time `2^0.49n`* (and its low-space companion).

## Improvement

| Quantity | Paper | Here |
|---|---|---|
| Deficiency variance | `Var d(V) <= q` | **`Var d(V) <= min(q, n-q)/4`** (sharp at `q=1`) |
| Checksum second-moment rate | `-0.00081952` | **`-0.00201952`** at the same sample/list exponent |
| Prime-collision prefactor | `K B L 2^-L` | **`B/(c_0 2^L)`** (one factor `L` removed) |
| Preliminary search | transformed lists, `nN0+1` target scans | **original-weight lists, one exact two-sum scan**, never later |

## Derivation

**Variance.** Both manuscripts prove `Var d(V) <= q` from a conditional
martingale whose increments lie in an interval of length one. Such a variable
has variance at most `1/4`; applying this conditionally gives `Var <= q/4`, and
exposing the complement of size `n-q` gives `Var <= (n-q)/4`. Hence
`Var d(V) <= min(q,n-q)/4`, with Hoeffding tails
`Pr(|d - E d| >= t) <= 2 exp(-2t^2/r)`, `r = min(q,n-q)`. Sharp at `q=1` with
half the weights zero.

**Checksum.** The appendix bounds both continuous moments by
`1.4295*1.00001 + 0.00007 = 1.429584295` and compares the bound with
`2^0.5168`; the source's finite-circle comparison uses `2^0.5169`. Exact
rational arithmetic gives

```
1.429584295 < sum_{i=0}^{45} (0.5156 ln 2)^i / i! < 2^0.5156,
```

so moments below `2^0.5157` follow for a sufficiently large cutoff. With
`eta = 0.51772` and `epsilon = 10^-8`, the rate in the exponential before the
`O(1)` prefactor is `-eta + 0.5157 + 48 epsilon = -0.00201952`, against the
source's `-eta + 0.5169 + 48 epsilon = -0.00081952`.

**Collisions.** Counting prime divisors with `kL < B` gives
`k <= floor((B-1)/L)`, so the collision probability is at most `B/(c_0 2^L)`
instead of `K B L 2^-L`.

**Preflight.** Tie weights satisfy `z = C a + s` with `C = 1 + nN0`
(`12n <= N0 < 24n`) and `0 <= s <= nN0`, so `floor(z/C)` is the original subset
sum and `|Sigma_a(V)| <= |Sigma_c(V)|`. Searching the original weights finishes
whenever the transformed preliminary search does, with one target scan instead
of `nN0+1`.

## Checks

`python3 verify.py` checks the rational moment lower bound, the `2^0.5156`
comparison and both checksum rates.

## Scope and limits

- The variance, collision and preflight results are proved here. The checksum
  improvement uses the source's numerical node enclosures and its finite-circle
  cutoff transfer; neither was regenerated, so it holds only if both are valid.
- No improvement to the `2^0.49n` total time, no reduction below the
  preliminary bottleneck, and no new total-time exponent.
