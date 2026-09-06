# சோதனை-008 · இரு பா — the two-family claim, tested and failed

**Run 2026-09-06.** Pre-registered in `vithai.md` வி-022 on 2026-08-23, before any of these measures
were taken. **Result: the declared failure condition triggered on all three measures.** வி-022 is
downgraded accordingly.

## கருதுகோள் | The hypothesis under test

தொல்காப்பியம் செய்யுளியல் நூ. 103–104 collapse the four பா into two families by **நடை**, gait:

> ஆசிரிய நடைத்தே வஞ்சி ஏனை
> **வெண்பா நடைத்தே கலி** என மொழிப. (104)

வி-022 observed that கலித்தொகை's எதுகை density (48.4 %, 8.4× chance) lands inside the வெண்பா band
(7.8–9.7×) and far from the four ஆசிரியப்பா corpora (2.6–4.8×), and proposed that a two-thousand-year-old
classification had **predicted out-of-sample**.

## நெறிமுறை | Protocol, as pre-registered

> *"Test the two-family claim on independent measures — not the எதுகை figure that suggested it.
> Declared failure condition: **if கலித்தொகை clusters with the akaval corpora on two of three
> independent measures, the two-family reading is not doing the work claimed here.**"*

**Instrument.** An **அசை scanner** written for this test — Unicode grapheme segmentation into
உயிர் / உயிர்மெய் / மெய் / ஆய்தம், then Tolkāppiyam's greedy நேர்/நிரை rule (a நெடில், or a குறில்
not followed by another syllable, plus any trailing ஒற்று → **நேர்**; a குறில் followed by another
syllable → **நிரை**). Validated against seven textbook cases before use, including the வாய்பாடு
names themselves: **தேமா → நேர் நேர், புளிமா → நிரை நேர்.** Those names are their own scansion, so
they are a real test rather than a circular one.

**Measures**, all independent of எதுகை:
1. **opening அசை** — % of அடி beginning on நேர்
2. **overall நேர்** — % of all அசை in the corpus that are நேர்
3. **மோனை σ1↔σ3** — first-letter agreement between சீர் 1 and 3 within a line

**Corpora**, from `_src/txt/`, with பரிபாடல் (mixed metre) as an uncommitted control.

## முடிவு | Result

| corpus | பா | lines | opening நேர் | overall நேர் | மோனை σ1↔σ3 | words/line |
|---|---|---|---|---|---|---|
| திருக்குறள் | வெண்பா | 2689 | 25.0 % | 47.9 % | 16.0 % | 3.52 |
| நாலடியார் | வெண்பா | 1628 | 23.4 % | 48.0 % | 34.1 % | 3.75 |
| **கலித்தொகை** | **கலி** | 4264 | **38.3 %** | **51.1 %** | **20.0 %** | **5.75** |
| *பரிபாடல்* | *mixed* | 2353 | *37.8 %* | *49.4 %* | *22.7 %* | *5.00* |
| ஐங்குறுநூறு | ஆசிரியம் | 2214 | 22.9 % | 47.6 % | 20.8 % | 3.77 |
| குறுந்தொகை | ஆசிரியம் | 1880 | 25.0 % | 51.6 % | 23.9 % | 3.82 |
| நற்றிணை | ஆசிரியம் | 5241 | 34.4 % | 48.9 % | 16.7 % | 4.77 |
| பதிற்றுப்பத்து | ஆசிரியம் | 2243 | 29.5 % | 48.6 % | 22.8 % | 4.10 |

| measure | வெண்பா mean | ஆசிரியம் mean | கலி | clusters with |
|---|---|---|---|---|
| opening அசை | 24.2 | 28.0 | 38.3 | **ஆசிரியம்** |
| overall நேர் | 47.9 | 49.2 | 51.1 | **ஆசிரியம்** |
| மோனை σ1↔σ3 | 25.1 | 21.0 | 20.0 | **ஆசிரியம்** |

**Three of three. The failure condition triggered.**

## விளக்கம் | What this means, narrowly

**[முடிவு | CONCLUSION]** The two-family reading is **not doing the work வி-022 claimed for it.**
கலித்தொகை's high எதுகை density is real and remains unexplained, but it is **one measure**, and it
does not generalise: on every independent rhythmic measure taken here, கலி sits with the akaval
corpora or beyond them, not with வெண்பா. The claim that Tolkāppiyam's classification "predicted
out-of-sample" is **withdrawn**.

**[விளக்கம் | INTERPRETATION] And the more interesting reading is the one the control supplies.**
On opening அசை, கலி (38.3) is not merely nearer ஆசிரியம் than வெண்பா — it is far from *both*
(24.2 and 28.0), and its nearest neighbour in the whole table is **பரிபாடல்** (37.8), the mixed and
musical one, which was included as a control and committed to nothing. On words-per-line the same
pair separates: கலி 5.75 and பரிபாடல் 5.00 against 3.5–4.8 everywhere else. **கலி may simply be its
own thing** — which is, after all, what having a பா of its own means.

**[கருதுகோள் | HYPOTHESIS] What நூ. 104 might actually be claiming.** If கலி does not resemble
வெண்பா on syllable rhythm, line length, or alliteration, then **நடை** in நூ. 104 is probably not any
of those. வெண்பா's gait is defined in நூ. 78 only negatively — `அதாஅன்று`, *it is not that* — and
what "gait" names may be a property of **performance** rather than of text: tempo, delivery, the
ஓசை. If so it is not measurable from an e-text at all, and this experiment tested the wrong thing
in a way no amount of care would have caught. **காதுக்காக:** read a கலித்தொகை passage aloud, then a
வெண்பா, then a Sangam akaval. Does கலி *move* like வெண்பா to you, whatever the numbers say?

## எல்லை | Limits — read before citing any number above

- **Word ≠ சீர்.** Project Madurai's spacing only approximates foot division, so "σ1↔σ3" is
  first-word-to-third-word, not first-foot-to-third-foot. This is the same limitation the எதுகை
  measurement carried and it has not improved.
- **Line extraction is heuristic** — any line of 2–9 Tamil-dominant words. Commentary prose that
  happens to be short will slip in; verse lines longer than nine words will drop out. கலித்தொகை and
  பரிபாடல் have the longest lines and therefore lose the most, which cuts *against* the difference
  observed, not for it.
- **Line length is a confound for measure 3.** கலி lines average 5.75 words against 3.5–3.8 for the
  வெண்பா corpora; σ1↔σ3 in a long line is a different span than in a short one.
- **Two வெண்பா corpora and four ஆசிரியம் corpora, one கலி corpus.** கலித்தொகை is the *only* surviving
  கலி anthology, so n=1 for the class under test and no within-class variance can be estimated.
- **The அசை scanner is new and unreviewed.** It passes seven textbook cases; it has not been checked
  against a published scansion of a full poem. That check is the obvious next step and would put
  every number here at risk.

## முடிவின் நிலை | Standing

**வி-022 is downgraded from a seed to a failed prediction**, with the எதுகை observation that
prompted it kept as an unexplained fact. The experiment did what it was built to do: a claim that
felt good was put at risk on measures chosen before the data was seen, and it did not survive.
Recorded per `../murai.md` §9 — *reserve "validated" for a claim with a visible protocol,
observations, failure conditions and limits* — and §10, which asks that the losing arc be kept.
