# 125: Metric k-median: sharper anchoring and strictness constants

Paper: *The Approximation Threshold for Metric k-Median* and its companion
*Single-Exponential Recovery and Bounded-Price Strictness for Metric k-Median*.

**Scope note.** The improved constants remain **impractical**: the assembled
margin is still below `2^-1300`, and the source already cites a stronger external
strictness proof. This sharpens the companion's constants; it does not change
the approximation factor or yield a deployable algorithm.

## Improvement

| Quantity | Companion | Here |
|---|---|---|
| Anchoring constant at tolerance `mu = 1/100` | `4,015` bits | **`659` bits** (gain `> 2^3355`) |
| Elementary strictness gap coefficient at price bound `T` | companion's value | **`84x` larger** (quoted; derivation not reproduced here) |
| Assembled margin to factor 2 | companion's bound | `> 2^6719` larger, but still `< 2^-1300` |

Both use the same scale condition `b(q0 + ell) <= 10P` and the same replay
model; no hypothesis or facility count changes. The `2^6719` assembled gain is a
consequence of the `84x` factor (it requires `84 > 60.6`), so the two stand or
fall together. `q0` is the short count,
`ell = |S| - h` the surplus of the width-five local optimum, `P` the cost, and
`b` the companion's price parameter.

## Derivation

**Retain `22/5`.** The companion's all-bad weighted swap lemma yields
`cost(S) <= 17P/5`, hence `sum_i V_i <= K P` with `K = 22/5`; the anchoring
argument uses `6P`. Retaining `22/5` is a pure constant improvement.

**Continuous threshold averaging.** For rational `0 < mu <= 1` set
`t_max = mu^2/60`, `A = K[2t_max + t_max/(1-t_max)]`, `a = mu - A > 0`,
`J = ceil[(K+10t_max)/((693/1000)a)]`, `t_min = t_max/2^J`, and declare a
center good at threshold `t` when it is not short and `V_i <= t b`. Integrating
over `[t_min,t_max]` with measure `dt/t` charges each center once instead of the
source's factor-two geometric tail:

```
integral t b [m(t)+ell] dt/t <= (10 t_max + K) P,
```

and `J log 2 > (693/1000) J` follows from a rational lower bound on `log 2`, so
some threshold satisfies `t b(m+ell) <= a P`.

**Half-separation balls.** Open balls of radius `sep_i/2` stay disjoint, the
nearest proxy lies inside its own ball, and singleton-ball excesses halve,
giving `D_g - P_g <= mu P`.

## Checks

`python3 verify.py` reads `values.json` (the numbers only, no provenance) and
checks: `C_new` has exactly 659 bits, the ratio to the 4015-bit original exceeds
`2^3355`, `assembled_sigma_new < 2^-1300`, and the assembled gap grows by more
than `2^6719`. The `84x` factor is quoted, not recomputed.

## Scope and limits

- Uses the companion's width-five swap lemma, replay model and
  anchoring/recovery foundations; those are not closed here.
- The approximation factor is unchanged and the constants remain impractical
  (`< 2^-1300`). The source already cites a stronger external strictness proof;
  this is not the best known strictness constant.
- Measured speedups exist only against our own cached prototype and are not part
  of this claim.
