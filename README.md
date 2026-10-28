# Improvements to openai/math

Notes on constants from a few papers in the
[`openai/math`](https://github.com/openai/math) collection. Each note tightens
one, keeping the paper's assumptions.

They come from a side project of mine, a swarm-agent system for hard problems,
and were written with DeepSeek and GPT Sol 6.1.

Each finding has its own folder: a `README.md` with the claim, the reasoning
and the caveats, plus a small `verify.py` that redoes the arithmetic.

| #   | Paper                                                                                      | Improvement                                                                                                                                                               | Finding                                                 |
| --- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| 113 | A Fully Polynomial Randomized Approximation Scheme for Perfect Matchings in General Graphs | annealing stages `8956 -> 375` for a dense `n=64` instance; enlarged-graph size `N` `144,458,560 -> 6,064,192`                                                            | [README](findings/113-perfect-matching/README.md)       |
| 115 | Exact Uniform Sampling of Contingency Tables with Arbitrary Margins                        | inverse-gap `O(d^126)` (internal; headline is `d^160`) `-> K' <= 24,832 d^86`; constants astronomical                                                                     | [README](findings/115-contingency-tables/README.md)     |
| 121 | An Almost-Linear Approximation Scheme for Edit Distance                                    | entropy term `h_Sigma ln d/eta -> sum_i h_i ln k_i/eta` (75% less in that term for 64 four-state blocks); log summands `G^60 -> O(log G)`                                 | [README](findings/121-edit-distance/README.md)          |
| 125 | The Approximation Threshold for Metric k-Median (+ companion)                              | anchoring `4,015 -> 659` bits; strictness gap `84x` (quoted); assembled margin still `< 2^-1300`                                                                          | [README](findings/125-k-median/README.md)               |
| 131 | Polynomial Mixing of the Switch Chain for Every Graphical Degree Sequence                  | comparison `H <= 2 n^2 L -> H <= L`; mixing `2 n^8 -> n^6/2+1`                                                                                                            | [README](findings/131-switch-chain/README.md)           |
| 138 | Subset Sum in Time `2^0.49n`                                                               | variance `q -> min(q,n-q)/4`; checksum rate `-0.00081952 -> -0.00201952`; collision prefactor `K B L 2^-L -> B/(c_0 2^L)`                                                 | [README](findings/138-subset-sum/README.md)             |
| 236 | The sharp factor-of-IID threshold for the free Ising model on regular trees                | information-loss coefficient `1/4 -> 1/3`; implied bound `2 sqrt(t+t^2) -> sqrt(3(t+t^2))` (−13.3975%); derived-bound width −75.7047% at `t=0.001`, −69.3496% at `t=0.01` | [README](findings/236-ising-factor-threshold/README.md) |
| 374 | Sharp One-Third Stability of Brenier Maps                                                  | paper's formula at the stated fixture: `95.2569184778 -> 19.0551240515` (−79.9961%); joint-kernel extension `7.05223039`                                                  | [README](findings/374-transport-stability/README.md)    |


## Checking

Each finding ships a `verify.py`. Run them all:

```
for f in findings/*/verify.py; do python3 "$f" || exit 1; done
```

