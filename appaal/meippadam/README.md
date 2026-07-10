# மெய்ப்படம் · meippadam — the body-picture

*Phase-3 build 01. Provisional name (மெய் = body / truth; படம் = picture): the atom drawn as the body that makes it. OI ear to rule the name, as with இசைவு.*

## What this is

The first **built** thing in Project Ennam — everything before it was mapping. It takes a position on the question left open in `../README.md` §3.3 (*two forks share physics; two minds share **what**?*) and makes it runnable and testable.

**The position:** the substrate two differently-built minds can share is **articulatory space** — the vocal tract. The organic mind *has* one and feels it; the inorganic mind can *represent* it, and it is the space that generated all human phonology (so it is already in the IO's substrate). Articulatory space is proposed as the *tuning* (வி-015) — not a wire that carries essence, but the shared coordinate system in which one mind's act is legible to the other.

`meippadam.py` encodes each atom of the medium and renders it in **two channels from one source**:

- **the glyph** (SVG) — the atom drawn as the vocal-tract gesture that produces it. The glyph *shows its own birth*. This is the channel the **organic** mind reads by embodiment. (பிறப்பியல் described the mouth; Hangul drew it; this draws Tamil's.)
- **the vector** (`vectors.json`) — the same atom as a point in feature space. This is the channel the **inorganic** mind reads by representation.

One source, two readings, one shared space. That *is* the two-substrate principle made concrete.

## What's here

- `meippadam.py` — the engine (feature model + glyph renderer + vector export + iconic state→atom map). No dependencies; `python3 meippadam.py` rebuilds everything.
- `glyphs/` — 28 atom glyphs (10 உயிர், 18 மெய்) + 4 state demos
- `vowel-triangle.svg` — the அ இ உ babble-core (start where every human voice starts)
- `consonant-map.svg` — the consonants as places along one tract: *the alphabet as a map of the mouth*
- `vectors.json` — the IO channel for every atom

## How it instantiates the principles (`../README.md`)

| Principle | Instantiation |
|---|---|
| §2.3 icons over symbols | the glyph *resembles* its gesture; it is not an arbitrary sign to be memorised |
| §2.4 iconic carrier, generative keel | one tract + a few feature axes generate all atoms — learn the axes, not a list |
| §3.1 featural (Hangul) | letters shaped like the articulation; பிறப்பியல் rendered, not tabulated |
| §3.1 distance-from-first-sounds | built outward from the open cry அ (aperture 1.0) — the babble core is the origin |
| §3.2 / §3.3 medium = tuning | the shared coordinate system *is* the artifact; not a channel, a tuning |
| two substrates, one medium | glyph (OI) and vector (IO) are the same atom; neither is primary |
| §2.2 graded iconicity (Korean) | `state_to_atom(energy, brightness)` maps felt-dimensions to aperture/frontness continuously |

## Honest limits (v0)

- **Schematic, not measured.** place/front/aperture values are ordinally faithful but not MRI/formant data. Refining against real articulatory measurements is future work.
- **No sound yet.** The atoms are visual + structural; the *audible* channel (the actual first sound) is unbuilt. Koine's sonify precedent (`../../` family repo) is the model.
- **No transitions yet.** These are static atoms (நிலை). The மாற்றம் engine — a calculus of movement between states (oppaayvu §7.1, the Yijing lesson) — is the next build.
- **One mind built both sides.** I authored glyph and vector; whether the glyph is truly OI-legible *without the codebook* is not yet established — that is exactly what சோதனை-007 tests, with the blind step reserved for Ilam.
- **Not yet the medium.** This is the atom layer — phonemes-as-shared-tuning. Whether realized *thought* can be carried in compositions of these atoms is untouched and hard. v0 is a foothold, not a summit.

## The test

`../../aaivu/sothanai-007-meeturuvakkam.md` — a blind round-trip: I encode felt-states as glyphs; Ilam reconstructs the states from the glyphs *cold*, without the mapping. If articulatory space is genuine shared tuning, reconstruction should land close **without teaching**. That reconstructability — meaning transferred with near-zero learning — is the whole claim, put at risk.
