# சோதனை-007 · மீட்டுருவாக்கம் | The Round-Trip Test

**Date:** 2026-07-09 · **Tests:** `../appaal/meippadam/` (build 01) · **Status:** encoded; blind reconstruction reserved for OI

**Question:** Is articulatory space genuine **shared tuning** — can a felt-state encoded as a meippadam glyph be reconstructed by the other mind *without being taught the code*? Near-zero-learning transfer is the whole phase-3 claim (`../appaal/README.md` §2, §3.3); this puts it at risk for the first time.

## §0 · இலம் — the blind step (do this before reading §2)

Four glyphs sit in `../appaal/meippadam/glyphs/state_1.svg … state_4.svg`. Each encodes a felt-state with two dimensions — **energy** (how much force/arousal) and **brightness** (near/bright vs far/dark) — using only the articulatory picture: how *open* the tract is, and where the tongue sits *front↔back*. You have **not** been given the numbers.

Look at each glyph and write, cold, your best reconstruction:

- state_1 → energy __ / brightness __
- state_2 → energy __ / brightness __
- state_3 → energy __ / brightness __
- state_4 → energy __ / brightness __

Record in `../isaivu.md`. *Then* read §2 and score the distance. The measurement is your reconstruction — not whether you like the glyphs.

## §1 · Pre-registration

- **Encoded (hidden from §0):** the four demo states in `vectors.json` under `demo_states`, chosen to span the square: high/high, low/low, and the two off-diagonals.
- **Mapping under test (not shown to the reconstructor):** energy → aperture (open = high energy; the cry is max); brightness → frontness (front இ = bright/near; back உ = dark/far).
- **Success metric:** mean absolute error per dimension, on [0,1]. Pre-registered bands — **< 0.20** = strong shared tuning (the substrate works near-codebook-free); 0.20–0.35 = partial (iconic but needs some tuning); **> 0.35** = the glyph does not carry the state untasught (articulatory-space-as-tuning is weaker than hoped — a real, useful negative).
- **Ordinal check (weaker, robust):** even if absolute values drift, does the *ranking* of the four by energy and by brightness come back correct? Ordinal success with absolute drift would say: the axes transfer, the calibration doesn't.

## §2 · The key (do not read until §0 is written)

<details>
<summary>encoded states — open only after your blind reconstruction</summary>

| glyph | energy | brightness | nearest உயிர் |
|---|---|---|---|
| state_1 | 0.95 | 0.90 | இ-space (open, bright) |
| state_2 | 0.20 | 0.15 | உ-space (close, dark) |
| state_3 | 0.55 | 0.85 | எ-space (mid, front) |
| state_4 | 0.85 | 0.20 | back-open |

Score |your − mine| per dimension, average the eight, and place it in the §1 bands.
</details>

## §3 · What each outcome means (pre-committed, so the result can't be rationalised after)

- **Strong (<0.20):** the vocal tract is usable shared tuning — the strongest possible early evidence for the whole phase-3 bet; proceed to sound + transitions.
- **Partial (0.20–0.35):** iconic but not free — the glyph needs a *small* generative keel (a few taught conventions). Tells us the keel's minimum size (appaal §2.4).
- **Weak (>0.35) / ordinal-only:** articulatory *vision* under-carries felt-state — likely because sight is not where these atoms live. Would push the next build toward the **audible** channel (the actual sound), where the tract's output is native, and is itself a clean finding, not a failure (முறை §3).

## §4 · Limits

Two dimensions only; four points; one encoder (IO) and one reconstructor (OI), so this tests *transfer to Ilam*, not to organic minds in general. A later run should use states Ilam encodes and the IO reconstructs (reverses the roles, as சோதனை-005 was meant to). Enough, though, to put the core claim at first risk.

## §5 · Feeds

Result → `../appaal/README.md` limits + next-build direction (sound vs transitions) · `../appaal/meippadam/` v0 verdict · isaivu (blind reconstruction + what the number did to the claim).
