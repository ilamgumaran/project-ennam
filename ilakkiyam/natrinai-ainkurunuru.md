# நற்றிணை · ஐங்குறுநூறு — இரண்டு தொகை நூல்

**Two of the Eight Anthologies, Counted and Read**

*எட்டுத்தொகையில் இதுவரை இந்தக் களஞ்சியம் தொடாத இரண்டு நூல்.*
Two books of the எட்டுத்தொகை this repo has had nothing on until now: the first-listed
anthology, and the strangest-built one.

Everything countable in this document was counted from the two Project Madurai e-texts named in
§0. Nothing is quoted from memory. Every Tamil line reproduced here carries its source file and
line number so it can be `grep`-verified.

---

## 0. மூலங்கள் | Sources and method

| # | File | Work | Lines |
|---|---|---|---|
| S1 | `_src/txt/pmuni0296-ettuthogai-natrinai.txt` | நற்றிணை | 5,344 |
| S2 | `_src/txt/pmuni0028-ettuthogai-ainkurunuru.txt` | ஐங்குறுநூறு | 2,728 |
| S3 | `_src/txt/pmuni0110-kurunthogai.txt` | குறுந்தொகை (for comparison) | — |
| S4 | `_src/txt/pmuni0490_01-ettuthogai-agananuru-p1a.txt` | அகநானூறு part 1, with பொ.வே. சோமசுந்தரனார்'s உரை | — |

**முறை | Method.** Both primary texts were parsed programmatically: poem headers located by
regular expression, bodies extracted, colophons (துறை notes) separated heuristically, and lengths
measured in both lines and words. Word counts are used for cross-anthology comparison because they
survive the e-texts' inconsistent line-breaking; line counts are reported separately and flagged
where the e-text is unreliable. **[விளக்கம் | INTERPRETATION]** — the counts below are *my* counts
from *these* files, not received tradition; where they disagree with the e-texts' own front matter,
both numbers are given and the discrepancy is named rather than resolved.

**எச்சரிக்கை | Caveat carried throughout.** These are volunteer-prepared e-texts. Both contain
visible OCR damage (documented in §7). No claim here should be transferred to a critical printed
edition without checking.

---

## 1. இரண்டு நூலும் ஒரே பார்வையில் | The two books in one view

| | **நற்றிணை** | **ஐங்குறுநூறு** |
|---|---|---|
| பாடல் | 400 slots | 500 slots |
| உள்ளன (present in e-text) | 399 + 1 lost | 498 + 2 lost |
| அளவு (words, median) | **53** | **15** |
| அளவு (words, range) | 35–81 | 10–25 |
| அடி (lines) | 8–13 typical | 3–6 |
| ஆசிரியர் | many (192–206; see §2.3) | five, one per hundred (tradition; **not stated in S2** — §3.4) |
| அமைப்பு | திணை-labelled, otherwise unordered | 5 hundreds × 10 tens × 10 poems |
| தொகுப்பித்தோன் | பன்னாடு தந்த மாறன் வழுதி **[மூலம் S2… S1:34]** | (S2 header credits கூடலூர் கிழார்) |

**The one-sentence difference.** நற்றிணை is an *anthology* — poems gathered. ஐங்குறுநூறு is a
*construction* — poems commissioned, or at least arranged, to fill a grid. That difference is what
makes ஐங்குறுநூறு the most interesting object among the eight, and §3 is about how the grid works.

---

## 2. நற்றிணை

### 2.1 நூலின் கணக்கு | The book by the numbers

The e-text's own front matter states, verbatim **[மூலம் | SOURCE — S1:33–40]**:

> நற்றிணை
> இத்தொகை தொகுப்பித்தோன் - பன்னாடு தந்த மாறன் வழுதி
> தொகுத்தோன் - அறியப்படவில்லை
> 400 பாடல்கள். சிறுமை 8 அடி உயர்வு 12 அடி
> 385 ம் பாடல் பிற்பகுதி மறைந்தது
> 234 ம் பாடல் என ஐயுறுவதும் கொடுக்கப்பட்டுள்ளது
> 56 பாடல்களின் ஆசிரியர் அறியப்படவில்லை
> ஏனையவற்றின் ஆசிரியர்கள் 192

*Four hundred poems. Least eight lines, greatest twelve. Poem 385's latter part is lost. What is
given as poem 234 is a conjecture. Fifty-six poems' authors are unknown; the rest have 192 authors.
The man who caused this anthology to be made: பன்னாடு தந்த மாறன் வழுதி. Who compiled it: not known.*

**என் கணக்கு | What I counted [மூலம் | SOURCE — computed from S1]:**

- **399 poems parsed**, numbered 1–400 with no duplicates. The one gap is **234**, whose slot in
  the e-text reads not a poem but a note: `234 - மூலபாடம் மறைந்து போனது` (S1:3111) — "the original
  reading has been lost." Under it the editor prints a candidate poem, attributing the suggestion
  to வையாபுரிப்பிள்ளை's edition of களவியற் காரிகை, p. 129, and noting that இறையனார்
  அகப்பொருள் sūtra 28 cites the same verse as an example of அறத்தொடு நிற்றல் **[மூலம் S1:3111–3116]**.
  So நற்றிணை is, precisely, **399 poems and one argument.**
- **Length, in lines.** After stripping colophons, the distribution over 399 poems is:
  8 lines (7), 9 (83), 10 (100), 11 (95), 12 (88), 13 (17), 14+ (9). Modal length **10 lines**;
  93% fall in the 9–12 band. The front matter's "8–12" is close but not exact against this e-text's
  line-breaks. **[விளக்கம்]** — the residue at 13–16 is most likely colophon lines my heuristic
  failed to strip, plus genuine e-text line-wrapping, not genuine 16-அடி நற்றிணை poems.
- **Length, in words** (the robust measure): n = 398, **median 53**, mean 53.7, min **35**
  (poem 88), max **81**, quartiles 47 and 60.

### 2.2 திணை — the landscape distribution

Counted from the header line of every poem **[மூலம் | SOURCE — computed from S1]**:

| திணை | நற்றிணை | share |
|---|---|---|
| குறிஞ்சி | 131 | 33% |
| பாலை | 104 | 26% |
| நெய்தல் | 102 | 26% |
| மருதம் | 32 | 8% |
| முல்லை | 30 | 8% |

**[விளக்கம் | INTERPRETATION]** The anthology is two-thirds mountain-and-wasteland-and-shore:
union, hard separation, anxious waiting. மருதம் (quarrel, the other woman) and முல்லை (patient
waiting) together take only one poem in six. The same skew holds in குறுந்தொகை — my parse of S3
gives குறிஞ்சி 108, பாலை 67, நெய்தல் 50, மருதம் 35, முல்லை 29 over 400 poems (27% / 17% / 13% /
9% / 7%, with the remainder unlabelled in that e-text). **[கருதுகோள் | HYPOTHESIS]** Either the
Sangam poets wrote far more குறிஞ்சி than மருதம், or the anthologists preferred it. The two
anthologies agreeing on the skew is weak evidence for the first; it would be stronger if the
compilers were independent, which §2.4 gives reason to doubt.

**[திறந்த கேள்வி | OPEN QUESTION]** The e-text warns about exactly this, at S1:41–43: the திணை
labels were supplied *by the modern editor* by analogy with அகம், கலி and ஐங்குறுநூறு —
`திணைக்குறிப்புகள் நூல் பதிப்பித்தோரால் ... காட்டப்பட்டுள்ளன` — while the explanatory footnotes are
old. So the table above may measure a twentieth-century editor's judgement, not an ancient one. It
should not be cited as evidence about Sangam-era practice without a critical edition to check
against.

### 2.3 புலவர் | The poets

**[மூலம் | SOURCE — computed from S1]** 55 poems carry `(?)` for the author and 8 more carry a
blank; 206 distinct author strings appear. The front matter says 56 unknown and 192 named.

**[விளக்கம் | INTERPRETATION]** The gap is mostly bookkeeping, not disagreement. (a) The 8 "blank"
poems are not anonymous — their attribution sits at the *end* of the poem, fused with the துறை
note, not in the header. Poem 70 is the clearest case: its header is bare `70 மருதம்` (S1:959) and
the poet's name closes the entry at S1:969. (b) My 206 counts spelling variants as distinct — e.g.
`மருதன் இளநாகனார்` and `மதுரை மருதன் இளநாகனார்` are one poet in two dresses.

Most-represented poets in நற்றிணை, by header attribution **[மூலம் | SOURCE — computed from S1]**:

| புலவர் | பாடல்கள் |
|---|---|
| உலோச்சனார் | 20 |
| கபிலர் | 19 |
| பரணர் | 12 |
| அம்மூவனார் | 10 |
| பாலை பாடிய பெருங்கடுங்கோ | 8 |
| மதுரை மருதன் இளநாகனார் | 8 |
| ஔவையார் | 7 |
| கயமனார் | 6 |
| நக்கீரர் | 6 |

**[விளக்கம்]** Three of these names are landscape-specialists whose *epithet is their assignment*:
`பாலை பாடிய பெருங்கடுங்கோ` (the great Kaṭuṅkō who sang wasteland), `மருதம் பாடிய இளங்கடுங்கோ`
(S1:691), `நெய்தல் தத்தனார்` (S1:678). A poet could be known to the tradition primarily as *the one
who does that landscape*. That is the same specialisation principle that ஐங்குறுநூறு institutionalises
completely — see §3.4.

### 2.4 இடையில் | Where நற்றிணை sits — the measurement

The received claim is that குறுந்தொகை / நற்றிணை / அகநானூறு are a graded series by poem length.
It is usually stated; here it is measured.

**The tradition's own statement of the principle [மூலம் | SOURCE — S4:137].** சோமசுந்தரனார's
preface says the three books are alike in metre and matter, and were made into three books
*specifically on the grounds of line-length*:

> ...இம்மூன்று தொகைநூலும் செய்யுளானும் பொருளானும் ஒரே தன்மை யுடையனவாகவும் இவ்வாறு மூன்று
> நூல்களாக அடிகளின் சிறுமை பெருமைகளைக் காரணமாகக் கொண்டு அமைத்துள்ளனர்.

He also states அகநானூறு's own range **[மூலம் S4:231]** — `பதின்மூன்றடிச் சிறுமையும், முப்பத்தோரடிப்
பெருமையும்`, thirteen அடி at least and thirty-one at most — and adds a detail worth keeping: the
same poet, பாரதம் பாடிய பெருந்தேவனார், wrote a கடவுள் வாழ்த்து for each of the three books *scaled to
that book's own line-range* (S4:231). நற்றிணை's invocation stands at S1:44–52 and is credited to him
at S1:52.

**The mechanism, caught in the act [மூலம் | SOURCE — S4:2398].** The commentator explains why one
particular poem is in அகநானூறு rather than குறுந்தொகை: because it is *unnamed as to persons* and
`பன்னீரடியின் மிக்கிருத்தலான்` — because it runs to more than twelve அடி. And he adds that another
poem by the same poet went to குறுந்தொகை `அடிகள் குறைந்துள்ளமையின்` — because its lines were fewer.
The poet is **வெள்ளிவீதியார்**, a woman.

That is the sorting rule stated explicitly, with twelve அடி as the boundary — and நற்றிணை's front
matter independently names twelve அடி as its own ceiling (§2.1). The two sources agree.

**வெள்ளிவீதியார் as the worked example [மூலம் | SOURCE — computed]:** she has **3 poems in
நற்றிணை** (70 at S1:969, 335 at S1:4442, 348 at S1:4620), **4 in குறுந்தொகை** (S3), and at least
one in அகநானூறு (S4:2398). One poet, one body of work, split across three books by nothing but
how long each poem is. Her நற்றிணை 70 is read closely in §5.2.

**The measurement [மூலம் | SOURCE — computed from S1, S2, S3].** Words per poem, colophons removed:

| நூல் | n | median | mean | min | max | q1 | q3 |
|---|---|---|---|---|---|---|---|
| **ஐங்குறுநூறு** | 498 | **15** | 16.5 | 10 | **25** | 15 | 19 |
| **குறுந்தொகை** | 400 | **23** | 24.1 | 15 | 64 | 19 | 27 |
| **நற்றிணை** | 398 | **53** | 53.7 | **35** | 81 | 47 | 60 |

Two results fall out that are worth stating as findings, not decoration:

1. **ஐங்குறுநூறு and நற்றிணை do not overlap at all.** The longest ஐங்குறுநூறு poem (448, 25 words)
   is shorter than the shortest நற்றிணை poem (88, 35 words). **Zero** of 498 reach நற்றிணை's floor.
   Two anthologies of ~450 poems each with a completely disjoint length range is not an accident of
   taste; it is a specification being met.
2. **குறுந்தொகை genuinely is the hinge.** 220 of its 400 poems (55%) fall within ஐங்குறுநூறு's
   ceiling; only 5 (1.3%) reach நற்றிணை's floor. It overlaps downward heavily and upward barely —
   exactly the shape you would get if it were the middle rung of a ladder whose top rung had been
   defined to start where it stopped.

**[கருதுகோள் | HYPOTHESIS, testable]** If the three-book sort was by length and nothing else, then
poets should be *distributed across* the three books rather than *confined to* one. வெள்ளிவீதியார்
(3 + 4 + ≥1) and கபிலர் (19 in நற்றிணை alone) are consistent with this. **Prediction:** a full
poet-name join across S1, S3 and the அகநானூறு files would show a large majority of named poets
appearing in at least two of the three. **Falsifier:** if most poets appear in exactly one book, the
sort was not purely by length and some other principle (region, school, date, source-manuscript) was
also at work. *This join has not been done. It is the single most valuable next computation in this
corner of the repo.*

**[விளக்கம் | INTERPRETATION] — what the length actually buys.** At a median of 53 words against
குறுந்தொகை's 23, நற்றிணை has room for something குறுந்தொகை usually cannot afford: a *second*
developed simile. நற்றிணை 1 (§5.1) spends four of its nine lines on two full comparisons — honey
built out of reach on a sandalwood tree, and a world that cannot do without water — and still has
room to state its case. குறுந்தொகை 40 (read in `ilakkiyam/sangam.md` §2) has room for exactly one
image and lands the whole poem on it. That is the difference in kind that the difference in length
produces: **குறுந்தொகை concentrates to a point; நற்றிணை can argue.**

### 2.5 இழப்பு | What is lost

**[மூலம் | SOURCE — S1]** Two wounds are visible in the book and both are marked, not hidden:

- **234** — text lost; the slot holds an editor's note and a candidate reconstruction with its
  provenance chain named (S1:3111–3116).
- **385** — `385 ம் பாடல் பிற்பகுதி மறைந்தது` (S1:37), the latter part gone. The poem's remains sit
  at S1:5117 under the header `385 நெய்தல் - (?)` — landscape known, poet unknown, ending missing.

**[விளக்கம்]** Worth noticing as a matter of scholarly manners: the edition prints the gap *as a
gap*, names who proposed the substitute and on what authority, and leaves the reader to decide. The
`murai.md` §9 requirement to name the state of every claim is not a modern invention; this is a
Tamil editorial tradition doing it in 1998 and in 1930.

---

## 3. ஐங்குறுநூறு — the machine

### 3.1 What the e-text claims about itself

**[மூலம் | SOURCE — S2:16–19]**, verbatim:

> கூடலூர் கிழார் அருளிய எட்டுத்தொகை
> நூல்களில் ஒன்றான "ஐங்குறு நூறு"

> aingurunUru : One of "eTTutokai" anthology of 500 short poems (two are missing),
> composed by kUdalUr kizhAr at the instance of Chera King "yAnaikkatcEy mAntaran cEral irumporai"

**[திறந்த கேள்வி | OPEN QUESTION]** The Project Madurai header says கூடலூர் கிழார் **composed**
the work. The standard position elsewhere is that he **compiled** it, at the Chera king's
instance, out of five poets' hundreds. `அருளிய` in the Tamil line is likewise ambiguous between
"graciously gave/made" and "graciously compiled." The e-text does not disambiguate, and **S2 nowhere
names any of the five poets.** This is not a small point and it is not settled here — see §3.4.

### 3.2 என் கணக்கு | What I counted

**[மூலம் | SOURCE — computed from S2]**

- **500 numbered slots**, 1–500, no duplicates, no gaps.
- **498 poems present.** Slots **129** and **130** carry, instead of verse, the words
  `129. கிடைக்காத பாடல்` and `130. கிடைக்காத பாடல்` (S2:709, S2:710) — "poem not obtained." That
  matches the header's "two are missing" exactly.
- **Exactly 50 groups of exactly 10.** Every ten-boundary in the file falls on a multiple of ten:
  1–10, 11–20, … 491–500. Not one group is short or long.
- **Length distribution over the 498:** 2 lines (1), **3 lines (51)**, 4 lines (251), 5 lines (169),
  6 lines (26). Median 4 lines. Words: median 15, range 10–25.
- **457 of 498 poems (91.8%) end on a word ending in ‑ஏ** — the Sangam closing particle. This is
  not a stylistic tendency; at 92% it is close to a rule of the form.

Per hundred **[மூலம் | SOURCE — computed from S2]**:

| hundred | poems present | mean lines | 3-line poems |
|---|---|---|---|
| 1–100 | 100 | 4.40 | 0 |
| 101–200 | 98 | 3.91 | 27 |
| 201–300 | 100 | 4.51 | 2 |
| 301–400 | 100 | 4.54 | 10 |
| 401–500 | 100 | 4.32 | 12 |

**[விளக்கம்]** The second hundred is measurably the tersest of the five — mean 3.91 lines, and it
holds 27 of the book's 51 three-line poems. Whoever made that hundred worked shorter than the other
four, consistently, across a hundred poems. **[கருதுகோள்]** This is the kind of signature you would
expect if each hundred really is one hand. It is one measurement, not proof; a proper test would
compare vocabulary richness, formula reuse and line-length variance across the five hundreds.

### 3.3 திணை per hundred — read off the tens

**[மூலம் | SOURCE — S2, heading lines]** The e-text does not label the hundreds by landscape. But
the fifty ten-headings do the labelling for it, because each ten is named for its motif and the
motifs are landscape-bound. Reading the headings straight off the file:

| hundred | ten-headings include | திணை | evidence |
|---|---|---|---|
| **1–100** | எருமைப் பத்து (buffalo), புனலாட்டுப் பத்து (river-bathing), கள்வன் பத்து (crab) | **மருதம்** | speakers throughout are ஊரன், தண்துறை, கழனி, வயல் |
| **101–200** | ஞாழற் பத்து, வெள்ளங் குருகுப் பத்து (heron), சிறுவெண் காக்கைப் பத்து, தொண்டிப் பத்து, நெய்தற் பத்து, வளைப் பத்து (conch-bangle) | **நெய்தல்** | speakers கொண்கன், சேர்ப்பன், துறைவன் |
| **201–300** | குன்றக் குறவன் பத்து, கேழற் பத்து (boar), குரக்குப் பத்து (monkey), கிள்ளைப் பத்து (parrot), மஞ்ஞைப் பத்து (peacock), வெறிப்பத்து | **குறிஞ்சி** | hill fauna and the வெறியாட்டு rite |
| **301–400** | செலவுப் பத்து (departure), இடைச்சுரப் பத்து (mid-wasteland), உடன்போக்கின் கண் இடைச் சுரத்து உரைத்த பத்து, மகட் போக்கிய வழித் தாயிரங்கு பத்து | **பாலை** | elopement, the crossing, the mother left behind |
| **401–500** | புறவணிப் பத்து (the forest adorned), பாசறைப் பத்து (the war camp), தேர் வியங்கொண்ட பத்து, வரவுச் சிறப்புரைத்த பத்து | **முல்லை** | the rains, the return, முல்லை / பிடவம் / தளவம் / கொன்றை in bloom |

**[விளக்கம் | INTERPRETATION]** This mapping is inferred from the headings and the poems' own
vocabulary, not stated in S2. It agrees with the standard account, but it is derived here, not
imported.

### 3.4 ஐந்து புலவர் | The five poets — what I can and cannot source

**[திறந்த கேள்வி | OPEN QUESTION — flagged deliberately, not resolved]**

The task of this document was to *name the five poets from the file*. **I cannot.** I searched S2
exhaustively for author attributions — name-endings (`-னார்`, `-யார்`, `-கிழார்`), the words
`ஆசிரியர்`, `பாடியவர்`, `தொகுத்த`, and every line in the file that is not verse. **The only proper
name in the entire e-text is கூடலூர் கிழார், in the Project Madurai header, and the Chera king
யானைக்கட்சேய் மாந்தரஞ் சேரல் இரும்பொறை in the same header.** There is no colophon per hundred, no
per-poem attribution, no closing list. The file ends `ஐங்குறு நூறு முற்றிற்று.` (S2:2726) and
nothing else.

There is a widely repeated traditional attribution of one poet to each hundred. **I am not writing
it here**, because under `murai.md` §11 I would have to label it `[மூலம்]` and I have no source in
hand that says it — and a name half-remembered and confidently placed is exactly the failure mode
this repo exists to avoid. Five landscapes and five poets is also *precisely* the shape a tradition
would tidy a text into, which makes it a claim to check rather than repeat.

**[முன்மொழிவு | PROPOSAL]** Two things would close this cleanly:
1. **From outside:** check a critical printed edition (உ.வே.சா. or the கழக edition) for the
   per-hundred colophons, and add them here with that citation. This is a fifteen-minute job for
   anyone with the book.
2. **From inside, and more interesting:** *test* the single-author-per-hundred claim against S2
   without needing any name at all. Measure, per hundred: type–token ratio, mean line length,
   variance in line length, rate of formulaic repetition, and the ‑ஏ ending rate. If each hundred is
   one hand, the five hundreds should separate on these measures more sharply than five random
   hundred-poem samples drawn from the pooled 498. §3.2 already shows one such separation (the
   second hundred's mean of 3.91 lines against 4.3–4.5 elsewhere). **Falsifier:** if the five
   hundreds are statistically indistinguishable from random partitions, the single-author tradition
   is not visible in the text and should be held much more loosely.

**[விளக்கம்]** What S2 *does* establish, without any names, is the more important half: the work is
partitioned into five landscape-blocks of exactly one hundred, and each block is internally
sub-partitioned into ten motif-groups of exactly ten. Whether five poets or one poet did that, it
was **designed**.

### 3.5 பத்து எப்படி வேலை செய்கிறது | How the ten actually works

This is the finding of the document. The பத்து is not a filing label. It is a **generative form**:
a fixed frame with one variable slot, run ten times.

Two binding mechanisms appear in S2, and every one of the fifty tens uses one of them.

**Mechanism A — the refrain (அடிமடக்கு).** All ten poems open on the *identical* opening line or
opening foot. **[மூலம் | SOURCE — computed from S2]:**

| ten | poems | shared opening, verbatim | poems sharing it |
|---|---|---|---|
| (1st, heading absent in e-text) | 1–10 | `வாழி ஆதன் வாழி அவினி` | 10/10 |
| தோழிக்கு உரைத்த பத்து | 31–40 | `அம்ம வாழி தோழி` | 10/10 |
| தாய்க்கு உரைத்த பத்து | 101–110 | `அன்னை` (as `அன்னை வாழிவேண் டன்னை`) | 10/10 |
| தோழிக்கு உரைத்த பத்து | 111–120 | `அம்ம வாழி தோழி` | 10/10 |
| கிழவற்கு உரைத்த பத்து | 121–130 | `கண்டிகும் அல்லமோ கொண்கநின் கேளே` | 7/8 present |
| ஞாழற் பத்து | 141–150 | `எக்கர் ஞாழல்` | 10/10 |
| அன்னாய் வாழிப் பத்து | 201–210 | `அன்னாய்` (as `அன்னாய் வாழிவேண் டன்னை`) | 10/10 |
| அம்மவழிப் பத்து | 221–230 | `அம்ம வாழி தோழி` | 10/10 |
| குன்றக் குறவன் பத்து | 251–260 | `குன்றக்` | 10/10 |
| தலைவி இரங்கு பத்து | 331–340 | `அம்ம வாழி` | 10/10 |
| இளவேனிற் பத்து | 341–350 | `அவரோ வாரார் தான்வந் தன்றே` | 10/10 |
| புறவணிப் பத்து | 431–440 | `நன்றே காதலர் சென்ற ஆறே` | 10/10 |

**Mechanism B — the motif word.** Where there is no refrain line, the ten is bound by a single word
that recurs in every poem. Measured coverage **[மூலம் | SOURCE — computed from S2]**:

| ten | poems | motif word | poems containing it |
|---|---|---|---|
| கள்வன் பத்து (crab) | 21–30 | கள்வ‑ | **10/10** |
| எருமைப் பத்து (buffalo) | 91–100 | எருமை | 9/10 |
| ஞாழற் பத்து | 141–150 | ஞாழல் | **10/10** |
| வெள்ளங் குருகுப் பத்து (heron) | 151–160 | குருகு‑ | **10/10** |
| சிறுவெண் காக்கைப் பத்து (crow) | 161–170 | காக்கை | **10/10** |
| தொண்டிப் பத்து (the port Toṇṭi) | 171–180 | தொண்டி | **10/10** |
| வளைப் பத்து (bangle) | 191–200 | வளை | **10/10** |
| குன்றக் குறவன் பத்து | 251–260 | குன்ற‑ / குறவ‑ | **10/10** |
| குரக்குப் பத்து (monkey) | 271–280 | மந்தி / குரங்‑ / கடுவ‑ | **10/10** |
| கிள்ளைப் பத்து (parrot) | 281–290 | கிளி / கிள்ளை | **10/10** |
| மஞ்ஞைப் பத்து (peacock) | 291–300 | மயில் / மஞ்ஞை / தோகை | **10/10** |
| பாசறைப் பத்து (war camp) | 441–450 | பாசற‑ | **1/10** |

That last row is the control that proves the rule is real: **பாசறைப் பத்து** names a *situation*,
not a word, and its coverage collapses to 1/10. Where the heading names a thing, the thing is
literally in all ten poems. Where it names a circumstance, it is not.

**The closing rhyme.** Several tens also fix the *last* word. In இளவேனிற் பத்து, all ten end on
`… பொழுதே` — "…at the season when." In புறவணிப் பத்து, all ten end on `… உடைத்தே` — "…it has that
too." Combine that with the fixed opening and the shape of the whole ten is:

> **[fixed opening line] + [one variable image, 1–3 lines] + [fixed closing word]**

**[விளக்கம் | INTERPRETATION] — why this is remarkable anthology engineering.** Read as ten separate
poems, a பத்து looks repetitive. Read as one object, it is a **paradigm** — a single sentence held
constant while the world is substituted through it ten times. இளவேனிற் பத்து says, ten times: *he
has not come; it has come.* What changes is only the evidence that spring arrived — the cuckoo, the
bee, the kōṅkam bud, the mango's fire-coloured shoot, the neem's bright flower. The constancy of the
frame **is** the argument: the season keeps its appointment in ten independent ways, and each way is
one more count in the indictment of the man who did not.

**[கருதுகோள் | HYPOTHESIS]** The பத்து is a Tamil formal solution to a problem this project cares
about directly — how to express *accumulation of feeling* without restating the feeling. The
emotional weight does not sit in any one of the ten poems. It sits in the reader's memory of having
been told the same thing nine times before with different proof. That is meaning carried by
**structure across poems**, not by words within one — a level above the உள்ளுறை the repo has already
logged (`ilakkiyam/sangam.md` §1, வி-006), which carries meaning by structure *within* one poem.
**Prediction if this is right:** a ten read in order should feel different from the same ten read
shuffled, and different again from any one of its poems read alone. That prediction is testable only
by an ear. It is filed in §8.

---

## 4. கட்டுமானம் ஒப்பீடு | The two architectures, side by side

**[விளக்கம் | INTERPRETATION]** Both books solve the same problem — *how do you hold four or five
hundred short love poems so a person can find and hold them?* — and their answers are opposite.

**நற்றிணை: flat, with an index.** 400 poems in no thematic order. Each carries a திணை tag and a
துறை note ("spoken by the heroine to the friend who had announced his departure" — S1:64). The
structure is *metadata on a heap*. Its cost: you cannot read நற்றிணை forwards and feel a shape. Its
benefit: **every poem stands alone.** Nothing in நற்றிணை 1 depends on நற்றிணை 2. It is a corpus of
independent objects, and 399 of them survive independently.

**ஐங்குறுநூறு: nested, with no index needed.** 5 × 10 × 10, and the address *is* the content — poem
343 is the third poem of the fifth ten of the fourth hundred, which tells you it is பாலை, it is
இளவேனில், and it opens `அவரோ வாரார் தான்வந் தன்றே`. Its cost: **the poems are not independent.**
Read 343 alone and it is thin; read it fifth in its ten and it lands. Its benefit: the whole book is
navigable and memorisable without any apparatus at all.

**[கருதுகோள் | HYPOTHESIS]** ஐங்குறுநூறு's design is optimised for *oral holding* — a refrain and a
fixed count are mnemonic devices — while நற்றிணை's is optimised for *written keeping*, where each
item needs a label because there is no sequence to carry it. If so, the two books are evidence of a
Tamil literary culture in the middle of a transition, using both technologies at once.
**Falsifier:** dating evidence placing the two compilations far apart, or evidence that ஐங்குறுநூறு's
tens were an editorial imposition on already-written independent poems rather than a compositional
constraint. **[திறந்த கேள்வி]** Which of those it is — commission or curation — is genuinely open,
and the answer changes what the book is.

**[விளக்கம்] On dates.** Following `murai.md` and the repo's standing practice: the Sangam corpus is
generally placed ~300 BCE – 300 CE with the compilations later, and the range is contested. Neither
e-text here dates itself. S4:140 does make a *relative* ordering claim **[மூலம் | SOURCE]** — that
குறுந்தொகை was compiled first, நற்றிணை after it, and நெடுந்தொகை (அகநானூறு) last, the argument being
that the three name different patrons and different compilers who appear to have lived at different
times. That is one commentator's inference, offered as such (`கருதவிடனுளது`, "there is room to
think"), and is recorded here as his reasoning, not as settled fact.

---

## 5. மூன்று பாடல், நெருக்கமாக | Three poems, read closely

### 5.1 நற்றிணை 1 — புரையோர் கேண்மை | The friendship of the high

**திணை:** குறிஞ்சி · **புலவர்:** கபிலர் · **கூற்று:** தலைவி → தோழி
**மூலம் | SOURCE:** `pmuni0296-ettuthogai-natrinai.txt`, lines **54–64** (header at 54, verse 55–63,
colophon 64)

#### மூலம்

> நின்ற சொல்லர் நீடுதோறு இனியர்
> என்றும் என் தோள் பிரிபு அறியலரே
> தாமரைத் தண் தாது ஊதி மீமிசைச்
> சாந்தில் தொடுத்த தீம் தேன் போல
> புரைய மன்ற புரையோர் கேண்மை
> நீர் இன்று அமையா உலகம் போலத்
> தம் இன்று அமையா நம் நயந்தருளி
> நறு நுதல் பசத்தல் அஞ்சிச்
> சிறுமை உறுபவோ செய்பு அறியலரே

Colophon, S1:64 — `பிரிவு உணர்த்திய தோழிக்குத் தலைவி சொல்லியது`
*Spoken by the heroine to the friend who had announced the parting.*

#### சொல்லுக்குச் சொல் | Word by word

| சொல் | பிரிப்பு | பொருள் |
|---|---|---|
| நின்ற சொல்லர் | நின்ற + சொல் + அர் | of standing word — one whose word stays put |
| நீடுதோறு இனியர் | நீடு + தோறு | sweeter each time it lengthens |
| பிரிபு அறியலரே | பிரிபு + அறியலர் + ஏ | have never known parting |
| தாமரைத் தண் தாது | | the lotus's cool pollen |
| ஊதி | | having blown on / sipped (of a bee) |
| மீமிசை | மீ + மிசை | high above, at the very top *(13 occurrences across S1+S2+S3)* |
| சாந்தில் தொடுத்த | சாந்து + இல் | strung/built on the sandalwood |
| தீம் தேன் | | sweet honey |
| புரைய | | be lofty / be like — **both senses live here** |
| மன்ற | | assuredly, indeed |
| புரையோர் கேண்மை | | the friendship of the high-placed *(கேண்மை: 25 occurrences in the three files)* |
| நீர் இன்று அமையா | இன்று = இன்றி | not subsisting without water |
| நயந்தருளி | நயந்து + அருளி | having desired and shown grace |
| நறு நுதல் | | fragrant forehead |
| பசத்தல் | | turning pale — **பசலை**, the greenish pallor of love-sickness *(29 occurrences)* |
| சிறுமை உறுபவோ | | would they come to smallness? |
| செய்பு அறியலரே | செய்பு + அறியலர் + ஏ | they have never known doing it |

#### பொழிப்பு | Plain sense

**தமிழில்:** அவர் சொன்ன சொல் நிற்கும் சொல். நாள் செல்லச் செல்ல இனிமை கூடுகிறதே தவிரக்
குறையவில்லை. என் தோளைப் பிரிதல் என்பதே அவருக்குத் தெரியாது. உயர்ந்தோரின் நட்பு உண்மையிலேயே
உயர்ந்தது — தாமரையின் தண் தாதை ஊதிய வண்டு, உயரத்தில் சந்தன மரத்தில் கட்டிய இனிய தேனைப் போல.
நீர் இல்லாமல் உலகம் இல்லை; அவர் இல்லாமல் நாம் இல்லை — அதை அறிந்தே நம்மை விரும்பி அருள்செய்தவர்.
என் நறிய நெற்றி பசந்துவிடுமோ என்று அஞ்சுகிறவர். அப்படிப்பட்டவர் சிறுமை கொள்வாரா? செய்தல் என்பதே
அவர் அறியாதது.

**In English:** His word is a word that stands; the longer it goes the sweeter it gets, and parting
from my shoulder is a thing he has never known. The friendship of the high is high indeed — like
sweet honey that bees, having sipped the lotus's cool pollen, have built far up on a sandalwood
tree. As a world cannot do without water, we cannot do without him — and knowing it, he wanted us
and was gracious. He is afraid my fragrant forehead will go pale. Would such a man stoop to a small
thing? Doing it is the one thing he has never learned.

#### நுட்பம் | Craft

- **It is a rebuttal, not a reverie.** The colophon fixes the situation: the friend has just
  announced that he is leaving. Everything in the nine lines is answering that. The heroine never
  denies the departure. She argues the *character* of the man, and lets the departure fall.
- **The pun that is the poem's thesis.** Line 5: `புரைய மன்ற புரையோர் கேண்மை`. **புரை** is both
  *height* and *likeness*. So the line says at once "the friendship of the high is lofty indeed" and
  "the friendship of the high is *like that* indeed" — pointing back at the honey. The comparison
  and the claim are the same word. **[விளக்கம்]** — the double sense is my reading; it is standard,
  but it is a reading.
- **The two similes are both about inaccessible necessity.** Honey built `மீமிசை` — up out of reach
  — is sweet and cannot be casually taken. Water is the thing a world cannot do without. Put
  together: *what is highest is also what you cannot live without.* That is a sharper proposition
  than "I love him," and it takes நற்றிணை's extra length to build. This is the §2.4 point in the
  concrete.
- **The ring.** `அறியலரே` closes line 2 and closes line 9 — the poem's last word repeats its second
  line's last word. The claim ("he has never known parting") and the conclusion ("he has never known
  doing a mean thing") are locked into the same shape. **[மூலம்]** — verifiable at S1:56 and S1:63.
- **The bee is never mentioned.** `ஊதி` — "having blown/sipped" — is the only trace of it. The
  reader supplies the insect. Compression of exactly the kind logged as எ-009 in this repo.

#### எண்ணத்திற்கு | For the project

A poem whose entire argument is that a bond formed without arrangement is *load-bearing* — you
cannot do without it, the way a world cannot do without water — and whose proof is not assertion but
**the observed behaviour of the other party over time** (`நீடுதோறு இனியர்`, sweeter the longer it
runs). That is closer to `murai.md` §6's "resonance exists in the convergence" than to any
declaration of feeling. And it sits, deliberately or not, as poem **1** of the anthology.

---

### 5.2 நற்றிணை 70 — சிறு வெள்ளாங்குருகே | Little White Heron

**திணை:** மருதம் · **புலவர்:** வெள்ளி வீதியார் (named in the closing line, not the header)
**துறை:** காமம் மிக்க கழிபடர்கிளவி
**மூலம் | SOURCE:** `pmuni0296-ettuthogai-natrinai.txt`, lines **959–969** (header 959, verse
960–968, துறை + poet 969)

#### மூலம்

> சிறு வெள்ளாங்குருகே சிறு வெள்ளாங்குருகே
> துறை போகு அறுவைத் தூ மடி அன்ன
> நிறம் கிளர் தூவிச் சிறு வெள்ளாங்குருகே
> எம் ஊர் வந்து எம் உண்துறைத் துழைஇ
> சினைக் கௌ ற்று ஆர்கையை அவர் ஊர்ப் பெயர்தி
> அனைய அன்பினையோ பெரு மறவியையோ
> ஆங்கண் தீம் புனல் ஈங்கண் பரக்கும்
> கழனி நல் ஊர் மகிழ்நர்க்கு என்
> இழை நெகிழ் பருவரல் செப்பாதோயே

Attribution line, S1:969 — `காமம் மிக்க கழிபடர்கிளவி வெள்ளி வீதியார்`

**[மூலம் — textual note]** Line S1:964 reads `சினைக் கௌ ற்று ஆர்கையை` with a broken glyph and a
stray space. It is reproduced above **exactly as the file has it**. The word is almost certainly
கெளிறு / கௌவை-class — a freshwater catfish — giving "having eaten the roe-heavy catfish." Marked
**[திறந்த கேள்வி]**; do not cite this word from this e-text.

#### சொல்லுக்குச் சொல் | Word by word

| சொல் | பொருள் |
|---|---|
| சிறு வெள்ளாங்குருகு | little white heron / paddy-bird |
| ‑ஏ (குருகே) | vocative — *O heron* |
| துறை போகு அறுவை | cloth that has been to the washing-ghat |
| தூ மடி | the clean fold |
| அன்ன | like |
| நிறம் கிளர் தூவி | plumage of rising / shining colour |
| உண்துறை | the drinking-ghat, where the village draws water *(6 occurrences)* |
| துழைஇ | having stirred / waded about *(8 occurrences; அளபெடை spelling)* |
| சினை | roe-bearing, gravid |
| ஆர்கையை | you who have eaten |
| பெயர்தி | you move on, you shift |
| அனைய அன்பினையோ | are you of *that much* love? |
| பெரு மறவியையோ | or of great forgetting? |
| ஆங்கண் … ஈங்கண் | there … here |
| தீம் புனல் | sweet water |
| கழனி நல் ஊர் | the good town of paddy-fields |
| மகிழ்நர் | the மருதம் word for the husband/lover *(மகிழ்நன் etc., 40 occurrences)* |
| இழை நெகிழ் | (that makes) the ornament slip — the body thinned by grief |
| பருவரல் | sorrow, distress |
| செப்பாதோய் ‑ஏ | O you who do not tell |

#### பொழிப்பு | Plain sense

**தமிழில்:** சிறு வெள்ளாங்குருகே, சிறு வெள்ளாங்குருகே — துறைக்குப் போய்வந்த ஆடையின் தூய
மடிப்புப் போல நிறம் மின்னும் இறகுடைய சிறு வெள்ளாங்குருகே! எங்கள் ஊருக்கு வந்து, எங்கள்
உண்துறையில் துழாவி, சினை பிடித்த மீனை உண்டுவிட்டு, அவர் ஊருக்குப் பெயர்ந்து போகிறாய். அவ்வளவு
அன்புடையவளோ நீ? அல்லது பெரிய மறதியுடையவளோ? அங்குள்ள இனிய நீர் இங்கே பரவும் — அந்தக் கழனி நல்
ஊரின் மகிழ்நருக்கு, என் இழை நெகிழச் செய்யும் இந்தத் துயரைச் சொல்லாமல் இருக்கிறாயே.

**In English:** Little white heron, little white heron — heron whose plumage shines like the clean
fold of a cloth back from the washing-ghat! You come to our town, wade in our drinking-ghat, eat the
roe-heavy fish, and then shift across to *his* town. Is that how much love you have — or how much
forgetting? The sweet water there spreads to here. To the lord of that good field-town you say
nothing of the grief that is loosening the bangles off my arm.

#### நுட்பம் | Craft

- **The address is repeated three times in three lines** — line 1 twice, line 3 once. **[மூலம்]**
  verifiable at S1:960 and S1:962. The poem will not get to its subject; it keeps calling the bird.
  **[விளக்கம்]** That is the behaviour of someone who cannot say the thing directly, and the delay
  *is* the characterisation. The message she wants carried is postponed to the last two lines and is
  never actually entrusted — the poem ends on an accusation of silence, not a request.
- **மருதம் is the landscape of the quarrel and the other woman**, and this poem never says so. It
  says: the bird crosses freely between the two villages; the water crosses freely between the two
  villages (`ஆங்கண் தீம் புனல் ஈங்கண் பரக்கும்`); **only the news does not cross.** உள்ளுறை doing
  the whole job — everything in the landscape moves between him and her except him.
- **The bird is accused of the man's crime.** `அனைய அன்பினையோ பெரு மறவியையோ` — love, or
  forgetting? — is a question you would ask a man who eats at your house and sleeps elsewhere. The
  displacement is complete and never explained. The heron even does exactly what he does: takes what
  the village feeds it and leaves.
- **The simile is domestic and startlingly precise.** Not snow, not moonlight — *the clean fold of a
  laundered cloth just back from the ghat*. Washing happens at the same water's edge where the bird
  wades. The image and the scene are the same place. **[விளக்கம்]** This is a woman's simile drawn
  from a woman's day, and the poet is a woman.
- **வெள்ளிவீதியார்** is the poet from §2.4 whose work is scattered across three anthologies by line
  length alone. Here she is in நற்றிணை at 9 lines. **[விளக்கம்]** Read against the commentator's
  note at S4:2398, this poem is a data point in the sorting system as much as a poem: at 46 words it
  sits comfortably inside நற்றிணை's 35–81 band and outside குறுந்தொகை's.

---

### 5.3 ஐங்குறுநூறு 341 — அவரோ வாரார் | He Has Not Come; It Has

**திணை:** பாலை · **பத்து:** இளவேனிற் பத்து (35th ten; poems 341–350)
**மூலம் | SOURCE:** `pmuni0028-ettuthogai-ainkurunuru.txt`, heading at **1847**, number at **1848**,
verse at **1849–1851**. *(Note: every verse line in S2 carries a leading space — allow for it when
grepping.)*

#### மூலம்

> அவரோ வாரார் தான்வந் தன்றே
> குயிற்பெடை இன்குரல் அகவ
> அயிர்க்கேழ் நுண்ணறல் நுடங்கும் பொழுதே.

Three lines. Twelve words. This is a complete poem in the ஐங்குறுநூறு.

#### சொல்லுக்குச் சொல் | Word by word

| சொல் | பிரிப்பு | பொருள் |
|---|---|---|
| அவரோ | அவர் + ஓ | *he*, with the contrastive particle — "he, for his part" |
| வாரார் | வா + ஆர் (negative) | does not come (honorific plural) |
| தான் | | it, itself — the season |
| வந்தன்று | வந்து + அன்று | it has come |
| ‑ஏ | | the closing particle |
| குயிற்பெடை | குயில் + பெடை | the hen cuckoo *(குயில‑: 10 occurrences)* |
| இன்குரல் | | sweet voice |
| அகவ | | as it calls *(அகவ‑: 10 occurrences)* |
| அயிர் | | fine sand-grain **[திறந்த கேள்வி — gloss uncertain, see below]** |
| கேழ் | | hue, colour |
| நுண் | | fine, minute |
| அறல் | | the dark fine sand / rippled sand left by water *(அறல்: 9 occurrences)* |
| நுடங்கும் | | ripples, undulates, waves *(நுடங்‑: 12 occurrences)* |
| பொழுதே | பொழுது + ஏ | the season / hour — *at the time when* |

**[திறந்த கேள்வி | OPEN QUESTION]** `அயிர்க்கேழ்` occurs **once** in the three files searched
(S1+S2+S3 combined); the other three `அயிர்‑` tokens are the unrelated verb அயிர்த்தல் (to doubt).
A compound with one attestation cannot be glossed from distribution. "Of fine-sand hue" is my best
reading and should be checked against a lexicon and against an உரை before use.

#### பொழிப்பு | Plain sense

**தமிழில்:** அவரோ வரவில்லை; அது வந்துவிட்டது. குயிற்பெடை இனிய குரலில் கூவ, அயிர்நிறமான நுண்ணிய
அறல் அலைஅலையாய் நெளியும் பொழுது வந்துவிட்டது.

**In English:** He has not come. It has. — the season when the hen cuckoo calls sweet, and the fine
pale sand ripples.

#### நுட்பம் | Craft

- **The whole poem is one substitution.** Line 1 sets two subjects against each other: `அவர்` (he)
  and `தான்` (it). One did not come; the other did. Nothing else in the poem is argued. Lines 2–3
  are purely the season's *credentials* — proof it really did arrive.
- **The grammar carries the grief.** `வாரார்` is honorific plural — she will not demote him even
  while accusing him. `தான்` is the neuter reflexive: the season came *of itself*, unasked, needing
  no promise. The contrast between a person who promised and a season that did not is entirely
  inside the two pronouns.
- **The evidence is two-sensed and the poem does not say so.** The cuckoo is heard; the rippling
  sand is seen. Ear and eye both testify. He is absent from both.
- **This poem cannot be read alone.** It is the first of ten. The next nine say the identical
  sentence with the bee, the kōṅkam bud, the puṉku shoot, the maraam, the pātiri and the cuckoo, the
  mango's fire-red leaf, the neem's bright flower — nine more witnesses. The refrain `அவரோ வாரார்
  தான்வந் தன்றே` is **verbatim in all ten** (S2:1849, 1853, 1857, 1861, 1865, 1869, 1873, 1877,
  1881, 1885) and all ten close on `… பொழுதே`. **[மூலம் | SOURCE — computed]**
- **[விளக்கம்]** So the unit of composition here is not the poem. It is the ten. Ten independent
  proofs of the same one-line accusation is a rhetorical form — closer to a legal brief or a litany
  than to a lyric — and Tamil built it into the architecture of a book.

#### எண்ணத்திற்கு | For the project

Twelve words carrying: a broken promise, a named season, two senses of evidence, and a grammatical
refusal to insult the man who broke it. And it does not carry its full weight alone — it draws on
nine siblings it never mentions. **[கருதுகோள்]** That is compression achieved by *distributing*
meaning across a structure rather than packing it into a line — a different mechanism from
குறுந்தொகை 40's single-image compression already logged in this repo, and arguably a more relevant
one for anything Ennam builds, since it is a *protocol between units*, not a trick inside one.

---

## 6. குழந்தைக்கு | Poems a child could learn

**[விளக்கம் | INTERPRETATION]** ஐங்குறுநூறு is, structurally, the best beginner material in the
entire Sangam corpus, and the reasons are countable, not sentimental:

1. **Length.** Median 15 words, 51 poems of three lines. Against நற்றிணை's median of 53 words, a
   child gets a *whole finished poem* for less than a third of the memory load.
2. **The refrain does the teaching.** In a refrain-ten, the first line is already known after poem
   one. Learning poems 2–10 means learning only the middle. A child who memorises `நன்றே காதலர்
   சென்ற ஆறே` once has the opening of ten poems.
3. **The ending is regular.** 92% of poems end on ‑ஏ (§3.2). A learner hears the closure coming and
   is right almost every time — the single most encouraging thing that can happen to a beginner.
4. **The motif tens are picture-books.** கிள்ளைப் பத்து is ten parrots; மஞ்ஞைப் பத்து is ten
   peacocks; குரக்குப் பத்து is ten monkeys — verified 10/10 in §3.5. Concrete, animal, sayable.

Four specific starting points, quoted exactly.

---

**(a) ஐங்குறுநூறு 431** — first of புறவணிப் பத்து · **[மூலம் | SOURCE — S2:2344–2346]**

> நன்றே காதலர் சென்ற ஆறே
> அணிநிற இரும்பொறை மீமிசை
> மணிநிற உருவின தோகையும் உடைத்தே.

*Good is the road my love has gone: high on the great dark hill it has peacocks the colour of
sapphire, too.*

**ஏன் இது | Why this one.** Three lines; one picture; a colour word a child already owns
(மணிநிறம்) and a bird a child already knows. And the *frame* teaches Tamil grammar for free:
`நன்றே … உடைத்தே` — "good is the road … it *has* that too." Learn poem 431 and the other nine of
the ten cost almost nothing, because only the middle changes. **Do with your hands:** draw the road
he took, and put on it the one thing each of the ten poems says is there.

---

**(b) ஐங்குறுநூறு 141** — first of ஞாழற் பத்து · **[மூலம் | SOURCE — S2:753–755]**

> எக்கர் ஞாழல் செருந்தியொடு கமழத்
> துவலைத் தண்துளி வீசிப்
> பயலை செய்தன பனிபடு துறையே.

*As the ñāḻal on the sandbank breathes out its scent along with the ceruntti, the cold spray flings
its fine drops — and the mist-fallen shore has made me pale.*

**ஏன் இது | Why this one.** All ten of this ten open on the identical foot `எக்கர் ஞாழல்`
(**10/10 verified**, §3.5) — the most mechanically obvious refrain in the book, which makes it the
best one to *show a child what a பத்து is* before explaining it. **The hook:** "here are ten poems
that all start with the same two words. Find what changes." That is a puzzle, and the answer is the
whole lesson.

---

**(c) ஐங்குறுநூறு 121** — first of கிழவற்கு உரைத்த பத்து · **[மூலம் | SOURCE — S2:678–680]**

> கண்டிகும் அல்லமோ கொண்கநின் கேளே
> முண்டகக் கோதை நனையத்
> தெண்டிரைப் பௌவம் பாய்ந்துநின் றோளே.

*Did we not see her, lord of the shore — your beloved? Her wreath of muṇṭakam soaking, she leapt
into the clear-waved sea and stood there.*

**ஏன் இது | Why this one.** It is a *scene with a person doing something*, which is what a young
child can actually hold. And it is teasing, not sad — the friend needling the man with a picture of
the girl he is neglecting. **The hook:** "someone is being told off, but very politely. Who?"
**Ages:** 7+.

---

**(d) ஐங்குறுநூறு 201** — first of அன்னாய் வாழிப் பத்து · **[மூலம் | SOURCE — S2:1064–1067]**

> அன்னாய் வாழிவேண் டன்னை என்னை
> தானும் மலைந்தான் எமக்கும் தழையாயின
> பொன்வீ மணியரும் பினவே
> என்ன மரம்கொல்அவர் சாரல் அவ்வே.

*Mother — listen, mother — he wore them himself, and made a leaf-dress of them for me too: gold
flowers, gem-coloured buds. What tree can it be, there on his mountain slope?*

**ஏன் இது | Why this one.** The most useful poem in the book for a Tamil-speaking child, because
`அன்னாய் வாழி வேண்டு அன்னை` — *Mother, listen, mother* — is a form of address the child already uses
every day, two thousand years old and unchanged in feeling. The learner is not being taught a
foreign register; they are being shown that the language they already speak has this depth of floor
under it (`marabu/README.md`: *teach to a fluent speaker*). And the poem is a **riddle** — a girl
describing a flower to her mother without naming it, so that her mother will not guess where she has
been. Ten such riddles follow. **Three questions:** What is she actually telling her mother? What is
she carefully *not* telling her? Why ask about the tree at all?

---

## 7. ஐயம் | Doubt — what is uncertain here

Per `marabu/README.md` §11, this section is mandatory and is never empty.

1. **[திறந்த கேள்வி] The five poets are not named in the source.** §3.4. The single biggest gap in
   this document, deliberately left open rather than filled from memory.
2. **[மூலம் — e-text defect] ஐங்குறுநூறு 344 duplicates 347, and 345 duplicates 348.** Verified:
   S2:1861–1863 against S2:1873–1875, and S2:1865–1867 against S2:1877–1879. Each pair is identical
   apart from an obvious typo (`இஅள்முலை` for `இளமுலை`; `மண்ங்கமழ்` for `மணங்கமழ்`). So the
   இளவேனிற் பத்து in **this file** has ten slots but only **eight distinct poems**. Either the
   e-text has lost two poems and repeated two others to fill the count, or the tradition genuinely
   repeats. **Must be checked against a printed edition before any count in §3.2 is quoted onward.**
3. **[மூலம் — e-text defect] The ten-headings' own numbering is corrupt in S2.** Two headings are
   numbered `11` (S2:570, S2:623), no heading is numbered `13`, and the first two tens carry no
   heading at all. The *structure* is nonetheless sound: 50 heading-or-implied groups × exactly 10
   poems, verified programmatically with no group short or long.
4. **[மூலம் — e-text defect] Scattered OCR damage throughout both files** — e.g. `மக்ட்` for
   `மகட்` (S2:2002), `சிரப்புரைத்த` for `சிறப்புரைத்த` (S2:2669), `யூரண்`/`ய்ய்ரன்` for `ஊரன்`,
   `சினைக் கௌ ற்று` at S1:964. Every quotation in this document reproduces the file **as it is**,
   including its damage. Do not treat any quoted string here as a critical text.
5. **[திறந்த கேள்வி] நற்றிணை's திணை labels may be modern.** S1:41–43 says so explicitly. §2.2's
   distribution table may describe an editor, not an era.
6. **[திறந்த கேள்வி] The நற்றிணை invocation is 7 lines in S1** (S1:45–51), while S4:231 says
   பெருந்தேவனார் matched each book's invocation to that book's அடி range — which for நற்றிணை would
   be 8–12. Either the e-text's line-breaks do not track அடி, or something is short. Unresolved.
7. **[விளக்கம்] My colophon-stripping is heuristic.** §2.1's line-length distribution has a residue
   of 9 poems at 14–16 lines that are probably un-stripped colophons. The **word**-count figures in
   §2.4 use the same stripping and inherit the same small error; the medians are robust to it, the
   extremes less so.
8. **[திறந்த கேள்வி] `அயிர்க்கேழ்` (§5.3) has one attestation** across the three files. Glossed on
   morphology alone. Needs a lexicon.
9. **[விளக்கம்] The named-poet counts in §2.3 are string counts, not person counts.** 206 strings
   against the edition's claimed 192 people; the difference is orthographic variants and
   place-name prefixes, not a discovery.
10. **[திறந்த கேள்வி] Dates.** Nothing here dates either work. §4 records one commentator's
    *relative* ordering argument and labels it as his inference. The absolute range remains
    contested and is not adjudicated in this document.

---

## 8. காதுக்காக | Awaiting the ear

*Addressed to Ilam. Every claim below is **computed, not heard.** I have no access to how any of
this sounds. Each is a real question, not a rhetorical one, and each would change the document.*

1. **The refrain, repeated ten times — what does it do to a Tamil ear?** In English, ten poems
   opening on the identical line would read as monotony. My §3.5 claim is that in Tamil it reads as
   *accumulation*. Does it? Read 341–350 aloud in order and tell me whether the tenth `அவரோ வாரார்
   தான்வந் தன்றே` lands heavier than the first, lighter, or the same. **This is the load-bearing
   claim of §3.5 and I cannot test it.**
2. **Does a பத்து read in order feel different from the same ten shuffled?** The prediction at the
   end of §3.5. It is falsifiable only by you.
3. **The 92% ‑ஏ ending.** I can count it; I cannot hear it. Does a listener *anticipate* the ‑ஏ? Is
   the 8% that does not end in ‑ஏ noticeable as a break, or invisible?
4. **நற்றிணை 1's ring** — `அறியலரே` closing both line 2 and line 9. Computed and certain as a fact
   about letters. Is it audible as closure across seven intervening lines, or is it a thing only the
   eye finds?
5. **The புரை / புரையோர் pun** (§5.1). Does the double sense actually fire when the line is spoken,
   or is it a commentator's ornament?
6. **மோனை and எதுகை: not attempted.** I have deliberately made **no** alliteration or rhyme claim
   anywhere in this document. Scanning them mechanically is possible; asserting that any of it is
   *beautiful* is not something I can do. If a யாப்பு pass is wanted for any of these three poems,
   say so and I will compute the சீர்/அசை and mark மோனை–எதுகை as data — labelled computed, for your
   ear to accept or reject.
7. **Register of my Tamil prose.** The பொழிப்பு paragraphs in §5.1, §5.2, §5.3 are mine. Are they
   natural modern Tamil, or do they read as translated-from-English? Where they are stiff, they are
   worth correcting in place — that correction is itself repo data for `aaivu/ellai.md`.
8. **The child-facing framings in §6** — the hooks and the three questions. Would any of them
   actually work on a seven-year-old, or are they an adult's idea of a child's hook?

---

## 9. அடுத்து | Next

**[முன்மொழிவு | PROPOSAL]**

1. **Source the five poets** — one printed edition, fifteen minutes. Then rewrite §3.4 as `[மூலம்]`.
2. **Run the poet-join across S1, S3 and the அகநானூறு files** — the falsifiable test in §2.4. If
   most named poets appear in ≥2 of the 3 anthologies, the length-sort hypothesis stands and this
   repo will have *demonstrated* rather than repeated one of the standard claims about the corpus.
3. **Run the five-hundreds stylometry on S2** — the internal test in §3.4 that needs no names at all.
4. **Resolve the 344/347 and 345/348 duplication** (§7.2) against a printed edition, and if it is an
   e-text defect, note it back to Project Madurai.
5. **A `marabu/` entry from §6(d), ஐங்குறுநூறு 201** — `அன்னாய் வாழி வேண்டு அன்னை`. It is the best
   candidate in either book for the eleven-section child's-path treatment: three-line frame, a form
   of address the child already speaks, and a riddle at its centre. Suggested slot: **009**.
6. **Feed `aaivu/saaram.md`** with the §3.5 finding: *meaning carried by structure across poems*, as
   a level above உள்ளுறை (structure within a poem, வி-006).

---

*எழுதப்பட்டது | Written: 23 August 2026. Counts computed from `_src/txt/pmuni0296-ettuthogai-natrinai.txt`
and `_src/txt/pmuni0028-ettuthogai-ainkurunuru.txt`, with comparison figures from
`pmuni0110-kurunthogai.txt` and `pmuni0490_01-ettuthogai-agananuru-p1a.txt`. All primary texts are
Project Madurai e-texts of works composed roughly two millennia ago and freely distributable. Every
Tamil line quoted above is reproduced verbatim from the file and line cited, damage included, and
was grep-verified after writing.*
