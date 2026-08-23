# அகநானூறு | Akanāṉūṟu — The Long Akam Anthology

**நெடுந்தொகை** — "the long collection." Four hundred akam poems, thirteen to thirty-one lines each,
by roughly a hundred and forty-five poets, arranged by a rule so strict that you can name a poem's
landscape before you have read a word of it.

This document is built entirely from five local Project Madurai e-texts of the நாட்டார் /
சோமசுந்தரனார் editions. Every line of மூலம் quoted below was copied out of those files by script,
never from memory; each quotation carries its file and line number so a `grep` can check it. Where
a claim comes from the editors' prose rather than from the verse, it is marked. Where it comes from
counting the files, it says so and gives the count.

**மூலங்கள் | Sources used**

| Short name | File | Contents | Commentary |
|---|---|---|---|
| **A** | `pmuni0490_01-ettuthogai-agananuru-p1a.txt` | 1–60 | பொ.வே. சோமசுந்தரனார் |
| **B** | `pmuni0490_02-ettuthogai-agananuru-p1b.txt` | 61–120 | பொ.வே. சோமசுந்தரனார் |
| **C** | `pmuni0523_01-ettuthogai-agananuru-p2a.txt` | 121–210 | ந.மு. வேங்கடசாமி நாட்டார் & ரா. வேங்கடாசலம் பிள்ளை |
| **D** | `pmuni0523_02-ettuthogai-agananuru-p2b.txt` | 211–300 | ,, |
| **E** | `pmuni0534-ettuthogai-agananuru-p3.txt` | 301–400 | ,, |

All in `_src/txt/`. Note that A/B and C/D/E are **two different editorial traditions bound into one
corpus** — see §9. That is a feature for a learner, not a nuisance.

---

## 1. அமைப்பு | The shape of the book

[மூலம் | SOURCE — file E, l. 3389–3390, the old பாயிரம் colophon reproduced by the editors]
The traditional end-note to the anthology states four things at once: that the poems were composed
by **145 poets** (`இவை பாடின கவிகள் நூற்று நாற்பத்தைவர்`); that the shortest poem is **13 lines**
and the longest **31** (`கடியளவு சிறுமை பதின்மூன்று; பெருமை முப்பத்தொன்று`); that the compiler was
**உருத்திரசன்மன்**, son of மதுரை உப்பூரி குடிகிழார்; and that the compilation was commissioned by
**பாண்டியன் உக்கிரப்பெருவழுதி**.

I checked the last three of those against the files. All three hold.

[முடிவு | RESULT — computed over all five files]

| Fact | Traditional claim | What the files give |
|---|---|---|
| Number of poems | 400 | **400** parsed, none missing |
| Shortest poem | 13 lines | **13** (22 poems) |
| Longest poem | 31 lines | **31** (one poem: 86) |
| Poets | 145 | **183 distinct name-strings**, 3 poems unattributed — see §8 |
| Divisions | 3 | **3**, boundaries confirmed at 120/121 and 300/301 |

### The three divisions

[மூலம் | SOURCE — file A, l. 60; file C, l. 66–67; and the பாயிரம் in file E]
The 400 poems are bound as three books with three deliberately beautiful names:

| # | பெயர் | Poems | Count | Name means |
|---|---|---|---|---|
| 1 | **களிற்றியானை நிரை** | 1–120 | 120 | *a file of bull elephants* |
| 2 | **மணிமிடை பவளம்** | 121–300 | 180 | *coral set between sapphires* |
| 3 | **நித்திலக் கோவை** | 301–400 | 100 | *a string of pearls* |

The பாயிரம் identifies each division not by number but by the **first line of its first poem and of
its last poem** — a manuscript-era way of fixing a boundary that cannot drift. I checked all four
boundary lines against the files, and all four match:

| Boundary | Colophon cue | Actual line in the file |
|---|---|---|
| Division 1 opens | `வண்டுபடத் ததைந்த கண்ணி` | `வண்டுபடத் ததைந்த கண்ணி யொண்கழ` — A l. 306 |
| Division 1 closes | `நெடுவேண்மார்பின்` | `நெடுவேள் மார்பின் ஆரம் போலச்` — B l. 2454 |
| Division 2 opens | `நாநகை யுடைய நெஞ்சே` | `1நாம்நகை யுடையம் நெஞ்சே கடுந்தெறல்` — C l. 77 |
| Division 2 closes | `நாள்வலை முகந்த` | `நாள்வலை முகந்த கோள்வல் பரதவர்` — D l. 2969 |

(The e-text of poem 121 reads `நாம்நகை`; the பாயிரம் cue and a variant recorded in file C both
read `நாள்நகை`. A one-syllable manuscript variant, not a mismatch.)

[விளக்கம் | INTERPRETATION] The editors of file A (l. 138) give a practical reason for the split
that is worth keeping: 400 long poems make a palm-leaf bundle no student could hold. Three books of
120 / 180 / 100 are three carryable சுவடி. The gorgeous names came afterwards, and — the same
editor notes at l. 139 — were quarried out of phrases occurring *inside* the anthology itself, so
that the container is named from its own contents.

---

## 2. அடியளவு | Line length, counted

[முடிவு | RESULT — computed] I parsed all 400 verse blocks and reconstructed each poem's line count
using the print-edition line markers (the `5`, `10`, `15` … numerals the e-text preserves at line
ends), which survive even where the e-text has dropped a line.

| Lines | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Poems | 22 | 58 | 58 | 35 | 42 | 43 | 36 | 16 | 17 | 21 | 11 | 12 | 6 | 13 | 3 | 3 | 2 | 1 | 1 |

Mean **17.9**, median **17**. Nothing falls outside 13–31 — the traditional bound is not an
approximation, it is exact, and it was evidently a **selection criterion**, not a description.

By division: களிற்றியானைநிரை mean 18.5 (13–31), மணிமிடைபவளம் mean 17.5 (13–29), நித்திலக்கோவை
mean 17.8 (13–28). [கருதுகோள் | HYPOTHESIS] The first division running slightly longer and holding
both extremes is consistent with the three books being cut from an already-ordered 400 rather than
compiled separately — but 1.0 line of mean difference is thin evidence and I would not push it.

---

## 3. யாப்பு | The metre

[மூலம் | SOURCE — file A, l. 231; file C, l. 65] Both editorial traditions say the same thing: the
anthology is a collection of **ஆசிரியப்பா** (`ஆசிரியப்பாக்களின் தொகுதி`), also called **அகவல்**
(file C: `நானூறு அகவற் பாட்டுக்களால் ஆனது`). Not one poem in another metre.

[முடிவு | RESULT — computed] ஆசிரியப்பா's structural signature is that its lines run to four சீர்,
with the **ஈற்றயலடி — the second-to-last line — cut short to three**. I counted whitespace-separated
feet in the last two lines of every poem:

| | 3 feet | 4 feet | other |
|---|---|---|---|
| **Penultimate line** | **389** | 8 | 3 |
| **Final line** | 2 | **390** | 8 |
| All interior lines | 31 | **6,240** | ~230 |

So the ஈற்றயல் முச்சீரடி holds in **389 of 400 poems (97%)**, and the four-foot interior line in
about 96% of interior lines. The residue is almost entirely e-text damage (§9), not metrical
variation.

⚠️ **[விளக்கம் | INTERPRETATION — caveat]** Whitespace tokens are a *proxy* for சீர், not சீர் itself. In files A/B the e-text keeps the old joined-sandhi orthography, so a token boundary
sometimes falls where a சீர் boundary does not. The 97% figure should be read as "the shape is
overwhelmingly there", not as a scansion.

---

## 4. எண்முறை | The numbering rule

This is the structural fact worth the trip.

### The rule as the tradition states it

[மூலம் | SOURCE — file E, l. 3400–3403; the second of three traditional வெண்பா printed under the
heading `அகநானூற்றின் தொகுப்பு முறை`]

```
ஒன்றுமூன் றைந்தோழொன பான்பாலை; ஒதாது
நின்றவற்றின் நான்கு நெறிமுல்லை ;-அன்றியே
ஆறாம் மருதம்; அணிநெய்தல் ஐயிரண்டு;
கூறா தவைகுறிஞ்சிக் கூற்று. 2
```

And the third, saying the same thing from the other end:

```
பாலை வியமெல்லாம்; பத்தாம் பனிநெய்தல்;
நாலு நளிமுல்லை நாடுங்கால்;-மேலையோர்
தேறும் இரண்டெட் டிவைகுறிஞ்சி; செந்தமிழின்
ஆறு மருதம் அகம். 3
```

The file even supplies the kennings' glosses (E l. 3408):

> வியம் - ஒற்றையெண்கள். வெண்டே ரியக்கம் - பாலை. தாமரை - மருதம். குட்டத்து இவர் திரை - நெய்தல். தோலாச் செவியான் - கேள்வியுணர்வு மிக்கவன்.

*(வியம் = the odd numbers. வெண்டேரியக்கம் = mirage-motion = பாலை. தாமரை = lotus = மருதம். குட்டத்து
இவர் திரை = the rising wave of the deep = நெய்தல்.)*

**The rule, stated plainly:**

| Poem number ends in | திணை | Poems |
|---|---|---|
| **odd** (1, 3, 5, 7, 9 …) | **பாலை** — the wasteland, hard separation | 200 |
| **2 or 8** | **குறிஞ்சி** — the mountain, union | 80 |
| **4** | **முல்லை** — the forest, patient waiting | 40 |
| **6** | **மருதம்** — the farmland, quarrel and infidelity | 40 |
| **0** | **நெய்தல்** — the shore, anxious separation | 40 |

Every block of ten poems is therefore a fixed chord: **பா கு பா மு பா ம பா கு பா நெ**.

### The rule as the poems actually testify

> **[திருத்தம் | CORRECTED 2026-08-23 on verification.]** This section originally reported extracting
> the திணை colophon "of every poem in all five files — 399 of 400" and matching **398 of 400**.
> **That aggregate is not supportable from these sources and has been replaced.** The e-texts do not
> carry திணை colophons for the whole anthology: `pmuni0534` (poems 301–400) contains the string
> திணை **zero times**, and `pmuni0523_01/02` contain it only in commentary prose. Labelled colophons
> exist for **poems 1–120 only**, in the two `pmuni0490` files. The re-run below is what the files
> actually support. The rule itself, and the poem-44 anomaly, both survive — see below.

[முடிவு | RESULT — recomputed, method stated] Colophons of the form `செய்யுள் N` followed by
`திணை: X` were extracted from all five files. **117 recovered, all in the range 1–120.** Compared
against the rule, after normalising a zero-width-joiner artefact in the e-text (`ம‌ருத‌ம்` for
மருதம், four poems) and re-attributing one label that belongs to the கடவுள் வாழ்த்து invocation at
`pmuni0490_01` l. 213 (`திணை: பாடாண்`) rather than to செய்யுள் 1 — which is itself correctly
labelled `திணை: பாலை` at l. 302:

| | |
|---|---|
| colophons recovered | **117** (poems 1–120) |
| match the numbering rule | **116** |
| genuine exception | **1** — செய்யுள் 44 |
| rate | **99.1 %** over the range the sources cover |

**[எல்லை | LIMIT]** This tests the first 120 poems, not 400. For poems 121–400 the rule is attested
here **only** by the traditional வெண்பா quoted above, which is a statement of intent by the
anthologists, not independent evidence that the poems obey it. Confirming the remaining 280 needs an
edition that prints their colophons — நாட்டார்'s printed volumes do, but the Project Madurai
e-texts of them do not. **Until then, "398 of 400" is a claim nobody in this repo has checked.**

### The two anomalies

**செய்யுள் 44 — the one poem labelled against its number.** [மூலம் | SOURCE — A l. 2300] Poem 44
ends in 4, so the rule demands முல்லை; the colophon in this edition reads `திணை: பாலை`. Its துறை
(A l. 2301) is `வினை முற்றி மீளுந் தலைமகன் தேர்ப்பாகற்குச் சொல்லியது` — the hero, his task
finished, speaking to his charioteer on the way home. That subject is the முல்லை situation almost
by definition; poem 114, which carries exactly the same துறை wording, *is* labelled முல்லை (B
l. 2192).
[திறந்த கேள்வி | OPEN QUESTION] Is `பாலை` at poem 44 a slip of this edition (or of the e-text), or
a genuine dissent by a commentator who read the poem's முதற்பொருள் as arid? **I cannot settle this
from the files I have** — it needs a second edition to collate. Flagged, not resolved.

**செய்யுள் 39 — the poem that had to be argued into place.** [மூலம் | SOURCE — A l. 2081] Poem 39
carries no `திணை:` line at all in this e-text. Instead the துறை note ends with an explicit defence:
the poem `உரிப் பொருளால் முல்லைத் திணையாயினும் முத‌ற் பொருள் ப‌ற்றிப் பாலைத்திணை ஆயிற்று` — *by its
inner subject it is முல்லை, but on account of its setting it has become பாலை*.

[விளக்கம் | INTERPRETATION] That sentence is the numbering rule caught in the act. The poem's felt
content is one திணை; the slot it occupies demands another; and the commentator reconciles them by
appealing to the two-tier structure திணை already has (முதற்பொருள், the land-and-time; உரிப்பொருள்,
the inner state). The constraint is not decorative. It has teeth, and where a poem strains against
it, the tradition argues rather than reshelves.

### ஏன் இப்படி? | Why build a book this way

[மூலம் | SOURCE — file A, l. 150–152] The editor of file A gives the reason without hedging: the
arrangement is `ஒரு காப்பமைந்துளது` — a *guard*, a protection — so that the poems `நின்றநிலை பிறழாது
நிற்றற்கு`, stand without their positions slipping; and so that from a poem's number alone
`அஃது இன்ன திணைச் செய்யுள் என்று எளிதில் உணரலாம்`.

[விளக்கம் | INTERPRETATION] Stated in modern terms: **அகநானூறு carries a checksum.** In a corpus
transmitted by memory and by palm-leaf copying, the two commonest failure modes are transposition
(two poems swap) and loss (a poem drops and the rest shift up). Both corrupt the numbering
silently — *unless* the number itself predicts a visible property of the poem. Here it does. Any
transposition that moves a poem across a திணை boundary is detectable by one glance at the
landscape; any deletion shifts all following poems into the wrong landscape class and rings like an
alarm all the way to poem 400. The redundancy costs the anthologist a real freedom (he must have
had spare பாலை poems and a shortage of others, and the 200/80/40/40/40 split is what that
constraint looks like from outside), and it buys the text a self-verifying spine.

[கருதுகோள் | HYPOTHESIS] The 200 : 80 : 40 : 40 : 40 ratio is a *consequence* of the odd/even
mechanism, not an independent statement about how much பாலை the Sangam corpus had. Half the slots
are odd, so half the book is பாலை whatever the poets wrote. **Prediction that would put this at
risk:** if the பாலை share in குறுந்தொகை and நற்றிணை — which have no such rule — is far below 50%,
the ratio here is an artefact of the grid; if it is near 50%, the grid may have been fitted to a
real distribution. Testable against the local குறுந்தொகை e-text; not done here.

---

## 5. குறுந்தொகை · நற்றிணை · அகநானூறு | What length buys

[மூலம் | SOURCE — file A, l. 137] The editor states the relation directly: the three akam
anthologies are `செய்யுளானும் பொருளானும் ஒரே தன்மை யுடையன` — one in metre and one in subject —
separated **only** by `அடிகளின் சிறுமை பெருமைகளை` — the smallness and largeness of their lines. Three
books, one poetics, three sizes.

| | அளவு | Poems | What that size affords |
|---|---|---|---|
| **குறுந்தொகை** | short | 400 | One image, one turn. The whole poem *is* the figure. |
| **நற்றிணை** | middle | 400 | Image plus a situation around it. |
| **அகநானூறு** | 13–31 lines | 400 | Image, situation, **and a second world entirely** |

[விளக்கம் | INTERPRETATION — the mechanism] The extra ten to twenty lines in அகநானூறு do not go on
saying more about the lovers. They go almost entirely into **the simile's own world**, which is
allowed to grow until it is a landscape you could walk in. குறுந்தொகை 40 compares mingling hearts
to red earth and rain in *four words*. அகநானூறு 251 (§7) spends fifteen lines on a war, a siege, a
mountain cut open, an elephant, and a tiger — in order to say *he has gone away*.

Three consequences follow, and they are what makes this anthology different in kind:

1. **உள்ளுறை gets room to be an argument.** In a four-line poem the implied comparison must be a
   flash. Here it can be staged, and the reader's completion of it becomes structural. See the
   worked example at §7.3 — including a recorded disagreement between two commentators about what
   *kind* of implication it even is.
2. **History gets in.** A long simile needs particulars, and particulars in this corpus are real
   kings, real ports, real invasions. §8 is only possible because of the line length.
3. **The frame becomes visible.** Almost every அகநானூறு poem has a two-part build: the *near* frame
   (a woman speaking to her friend, sixteen words of it) and the *far* frame (twenty lines of
   elsewhere). The poem's force lives in the join.

---

## 6. மூன்று பாடல் | Three poems, read closely

I chose 1, 4 and 10 deliberately: they are the first பாலை, the first முல்லை and the first நெய்தல்
in the book, so **the three of them together demonstrate the numbering rule of §4 as a by-product of
being read.** All three sit in file A, where the e-text preserves the old joined orthography — good
practice for the eye.

---

### 6.1 · அகநானூறு 1 — *the whetstone set in lac*

**திணை:** பாலை · **துறை:** பிரிவிடை ஆற்றாளாய தலைமகள் தோழிக்குச் சொல்லியது — *she, unable to bear
the separation, speaking to her friend* · **புலவர்:** **மாமூலனார்** · **19 lines**
[மூலம் | SOURCE — file A, l. 302–325]

#### மூலம்

```
வண்டுபடத் ததைந்த கண்ணி யொண்கழ
லுருவக் குதிரை மழவ ரோட்டிய
முருக னற்போர் நெடுவே ளாவி
யறுகோட்டி யானைப் பொதினி யாங்கட்
சிறுகா ரோடன் பயினொடு சேர்த்திய 5
கற்போற் பிரியல மென்ற சொற்றா
மறந்தனர் கொல்லோ தோழி சிறந்த
வேய்மருள் பணைத்தோ ணெகிழச் சேய்நாட்டுப்
பொலங்கல வெறுக்கை தருமார் நிலம்பக
வழல்போல் வெங்கதி்ர் பைதறத் தெறுதலி 10
னிழறேய்ந் துலறிய மரத்த வறைகாய்
பறுநீர்ப் பைஞ்சுனை யாமறப் புலர்தலி
னுகுநெற் பொரியும் வெம்மைய யாவரும்
வழங்குந ரின்மையின் வௌவுநர் மடியச்
சுரம்புல் லென்ற வாற்ற வலங்குசினை 15
நாரின் முருங்கை நவிரல் வான்பூச்
சூரலங் கடுவளி யெடுப்ப வாருற்
றுடைதிரைப் பிதிர்விற் பொங்கிமுன்
கடல்போற் றோன்றல காடிறந் தோரே.
                              --மாமூலனார்.
```
*(file A, lines 306–325)*

#### சொல்லுக்குச் சொல் | Word by word

| சொல் | பிரிப்பு | பொருள் | English |
|---|---|---|---|
| வண்டுபடத் ததைந்த கண்ணி | வண்டு பட ததைந்த கண்ணி | வண்டு மொய்க்கும்படி செறிந்த மலர்மாலை | a head-garland so thick with flowers that bees swarm it |
| ஒண்கழல் | ஒள் + கழல் | ஒளிரும் வீரக்கழல் | the bright warrior's anklet |
| மழவர் | — | மழநாட்டு மறவர் | the fighting men of Maḻa-nāḍu |
| ஓட்டிய | — | போரில் வென்று ஓடச்செய்த | who drove them routed from the field |
| நெடுவேள் ஆவி | — | வேளிர் குலத் தலைவன் ஆவி | Āvi, chieftain of the Vēḷir |
| பொதினி | — | பழனி | Podiṉi — today's Palani |
| சிறு காரோடன் | — | தோல் உறை தைக்கும் தொழிலாளன் | the leather-worker who stitches scabbards |
| பயின் | — | அரக்கு | lac, the resin cement |
| சேர்த்திய கல் | — | அரக்கால் பொருத்தி வைத்த சாணைக்கல் | the whetstone bedded into its block with lac |
| பிரியலம் என்ற சொல் | — | "பிரியமாட்டோம்" என்ற சொல் | the words *we will not part* |
| வேய்மருள் பணைத்தோள் | — | மூங்கில் என மயங்கும் பருத்த தோள் | round arms one could mistake for bamboo |
| பொலங்கல வெறுக்கை | — | பொன் அணிகலச் செல்வம் | wealth in worked gold |
| பைது அற | — | பசுமை அற்றுப்போக | until the green is gone out of it |
| உகுநெல் பொரியும் வெம்மைய | — | உதிர்ந்த மூங்கில் நெல் பொரியும் வெப்பம் | heat that pops the fallen bamboo grain where it lies |
| வௌவுநர் மடிய | — | ஆறலைப்போரும் தொழிலின்றிச் சோம்ப | the highway robbers idle, out of work |
| நார் இல் முருங்கை | — | நார் இல்லாத முருங்கை | the sapless drumstick tree |
| சூரல் அம் கடுவளி | — | சுழன்றடிக்கும் கடுங்காற்று | the whirling, violent wind |
| உடைதிரைப் பிதிர்வு | — | உடையும் அலையின் நுரைச் சிதறல் | the spray flung off a breaking wave |
| காடு இறந்தோர் | — | காட்டைக் கடந்து சென்றவர் | he who has crossed the forest and gone |

*(Glosses follow சோமசுந்தரனார்'s பதவுரை at file A, l. 328–338, condensed into my own English.)*

#### பொருள் — தமிழ்

தோழி! வண்டு மொய்க்கும் மலர்க்கண்ணியும் ஒளிரும் கழலும் உடைய, பகைவர் அஞ்சும் குதிரைப் படையுடைய
மழவரை வென்றோட்டிய, நல்ல போர்த்திறம் வாய்ந்த வேளிர் தலைவன் ஆவியின் பொதினி — முருகன் உறையும் அம்
மலைச்சாரல். அங்கே உறைகாரன் அரக்கால் பொருத்தி வைத்த சாணைக்கல் ஒருபோதும் விலகாதது போல, "நின்னைப்
பிரியேம்" என்று சொன்னாரே — அச்சொல்லை மறந்துவிட்டனரோ? மூங்கில் போன்ற என் தோள் மெலிய, தொலைநாட்டுப்
பொன் தேடுவதற்காக, நிலம் பிளக்கும் தீக்கதிரால் நிழல் தேய்ந்து மரம் உலர, சுனை வற்ற, உதிர்ந்த நெல்
தானே பொரியும் வெம்மையுடைய, ஆறு செல்வார் யாருமின்மையால் ஆறலைப்போரும் சோம்பிக் கிடக்கும், நார் அற்ற
முருங்கையின் வெண்பூவைச் சூறைக்காற்று வாரி எடுக்க — அவை உடையும் அலையின் நுரைப் பிதிர்வு போலத் தோன்றும்
— அக்காட்டைக் கடந்து போனாரே.

#### The meaning — English

Friend: in Podiṉi, the hill of Āvi — chieftain of the Vēḷir, good at war, who broke and scattered
the horsemen of Maḻa-nāḍu with their bee-thick garlands and bright anklets — a poor leather-worker
beds his whetstone into its seat with lac, and it never comes loose. *Like that stone, we shall not
part*, he said. Has he forgotten saying it? To fetch gold from a far country, and my bamboo-round
arms going slack for it, he has crossed a forest where the sun splits the ground and burns the
green out of it; where the shade has thinned and the trees dried and the pools gone hard, and the
fallen bamboo-grain pops in the heat where it lies; where nobody travels, so even the highwaymen
have nothing to do and lie idle; where the whirling wind rips the white flowers off the sapless
drumstick trees — and they scatter through the air exactly like the spray thrown off a breaking
wave.

#### நுட்பம் | Craft

**The vow is a piece of hardware.** Sangam poems do not usually swear on gods. This one swears on a
tradesman's whetstone — a cheap stone made permanent by cheap resin, in the hands of the lowest
craftsman named in the poem. The oath's guarantee is the *adhesion of lac*, and the poem's grief is
that a man's word turned out weaker than a cobbler's glue. Note that the anthology's very first
image is an image of **joining**, and its first line of complaint is that the join failed.

**The desert is proved, not described.** Look at how the heat is established: not by an adjective
but by three pieces of evidence. Shade has thinned (the trees are drying from the top). Pools have
gone hard. And fallen bamboo grain *pops by itself on the rock* — a detail so specific it functions
as a thermometer. Then the strangest proof of all: `வழங்குந ரின்மையின் வௌவுநர் மடியச்` — nobody
travels, **so the robbers are unemployed**. Emptiness measured by the idleness of the people who
prey on it. That is one line doing what a paragraph of landscape could not.

**The last image reverses the whole poem.** Twenty lines of absolute drought, and the closing simile
is *the sea*: white drumstick flowers torn loose by the wind look like the spray off a breaking
wave. Water arrives only as a resemblance, only at the end, and only in a place that has none. The
woman speaking has been thinking of water for nineteen lines without saying so.

**The frame.** Of nineteen lines, **three** are about the lovers (`பிரியலம் என்ற சொல் தாம் மறந்தனர்
கொல்லோ தோழி`). Sixteen are elsewhere. This is the அகநானூறு proportion.

---

### 6.2 · அகநானூறு 4 — *he tied the bell so the bees would not wake*

**திணை:** முல்லை · **துறை:** வினை முற்றி மீளும் தலைமகன் … (the friend consoling her as the rains
break) · **புலவர்:** **குறுங்குடி மருதனார்** · **17 lines**
[மூலம் | SOURCE — file A, l. 419–440]

#### மூலம்

```
முல்லை வைந்நுனை தோன்ற வில்லமொடு
பைங்காற் கொன்றை மென்பிணி யவிழ
விரும்புதிரித் தன்ன மாயிரு மருப்பிற்
பரலவ லடைய விரலை தெறிப்ப
மலர்ந்த ஞாலம் புலம்புபுறக் கொடுப்பக் 5
கருவி வானங் கதழுறை சிதறிக்
கார்செய் தன்றே கவின்பெறு கானங்
குரங்குளைப் பொலிந்த கொய்சுவற் புரவி
நரம்பார்த் தன்ன வாங்குவள் பரியப்
பூத்த பொங்கர்த் துணையொடு வதிந்த 10
தாதுண் பறவை பேதுற லஞ்சி
மணிநா வார்த்த மாண்வினைத் தேர
னுவக்காண் டோன்றுங் குறும்பொறை நாடன்
கறங்கிசை விழவி னுறந்தைக் குணாது
நெடும்பெருங் குன்றத் தமன்ற காந்தட் 15
போதவி ழலரி னாறு
மாய்தொடி யரிவைநின் மாணலம் படர்ந்தே.
                              --குறுங்குடி மருதனார்.
```
*(file A, lines 423–440)*

#### சொல்லுக்குச் சொல் | Word by word

| சொல் | பொருள் | English |
|---|---|---|
| வைந்நுனை | கூர்த்த நுனியையுடைய அரும்பு | the sharp-tipped bud |
| இல்லம் | தேற்றா மரம் (இங்கு அதன் மலர்) | the clearing-nut tree — here, its flower |
| பைங்கால் கொன்றை | பசிய அடியையுடைய கொன்றை | green-stemmed koṉṟai, the golden laburnum |
| மென்பிணி அவிழ | மெல்லிய கட்டு அவிழ | the soft binding loosens — the buds open |
| இரும்பு திரித்தன்ன | இரும்பைக் காய்ச்சி முறுக்கியது போன்ற | as if iron had been heated and twisted |
| மா இரு மருப்பு | கரிய பெரிய கொம்பு | great black antlers |
| இரலை | ஆண் மான் | the stag |
| பரல் அவல் | பரற்கல் நிறைந்த பள்ளம் | the pebbled hollow |
| தெறிப்ப | துள்ள | to leap, to spring |
| ஞாலம் | உலகு → உயிர்கள் | the world → its living creatures |
| புலம்பு புறக்கொடுப்ப | வருத்தம் புறங்கொடுத்து அகல | the misery turns its back and goes |
| கருவி வானம் | மின்னல் இடி முதலியவற்றுடன் வரும் முகில் | the cloud with its whole apparatus — lightning, thunder |
| கதழ் உறை | விரைந்து வீழும் துளி | fast-driving drops |
| கார் செய்தன்று | கார்ப்பருவத்தைத் தோற்றுவித்தது | it has *made* the rains |
| குரங்கு உளை | வளைந்த தலையாட்டம் (குரங்குதல் = வளைதல்) | the curved crest-plume |
| கொய்சுவல் புரவி | கத்தரித்த பிடரிமயிர் கொண்ட குதிரை | horses with clipped manes |
| நரம்பு ஆர்த்தன்ன வாங்குவள் | யாழ் நரம்பு ஒலித்தது போன்ற இழுத்த வார் | reins pulled taut, singing like yāḻ strings |
| பொங்கர் | பூத்த சோலை | the flowering bower |
| தாதுண் பறவை | மகரந்தம் உண்ணும் சிற்றுயிர் — வண்டு | the pollen-eating creature — the bee |
| பேதுறல் அஞ்சி | கலங்கிவிடும் என்று அஞ்சி | fearing it would be startled |
| மணிநா ஆர்த்த | மணியின் நாக்கைக் கட்டிய | having bound the tongue of the bell |
| மாண்வினைத் தேரன் | சிறந்த வேலைப்பாடமைந்த தேரையுடையவன் | he of the finely made chariot |
| உவக்காண் | உவ்விடத்தே! — காண் | *look — right over there!* |
| உறந்தை | உறையூர் | Uṟaiyūr, the Chola capital |
| குணாது | கிழக்கின்கண் | to the east of |
| ஆய்தொடி அரிவை | அழகிய வளையலுடைய இளம்பெண் | young woman of the fine bangles |

*(Glosses follow சோமசுந்தரனார், file A l. 443–453.)*

#### பொருள் — தமிழ்

முல்லைக் கொடியில் கூர்த்த அரும்பு தோன்ற, தேற்றாவும் பசுங்காற் கொன்றையும் மெல்லிய கட்டவிழ்ந்து மலர,
இரும்பை முறுக்கியது போன்ற கரிய பெரும் கொம்புடைய இரலைமான்கள் பரற்பள்ளத்தை அடைந்து — நீருண்ட
மகிழ்ச்சியால் — துள்ள, உலகின் உயிர்கள் உற்ற வறட்சித் துயரம் புறங்கொடுத்து அகல, மின்னலும் இடியுமாய
முகில் விரைந்த துளிகளைச் சிதறி — **கார் செய்துவிட்டது**; காடு அழகுபெற்றது. வளைந்த தலையாட்டத்தால்
பொலிந்த, கொய்த பிடரிமயிருடைய குதிரைகள், யாழ் நரம்பு ஒலிப்பது போல வார் இறுகப் பாய்ந்தோட —
பூத்த சோலையில் துணையோடு தங்கியிருக்கும் தாதுண்ணும் சிற்றுயிர்கள் கலங்கிவிடுமே என்று அஞ்சி,
**மணியின் நாவைக் கட்டிய** சிறந்த வேலைப்பாடுடைய தேரினனாய் — உவ்வதோ, அங்கே தோன்றுகிறான் குறும்பொறை
நாடன்! ஆய்தொடி அரிவையே, இசை முழங்கும் விழாக்களையுடைய உறையூருக்குக் கிழக்கே உள்ள நெடிய பெரிய
மலையில் செறிந்த காந்தளின் நாளரும்பு விரிந்த மலர் போன்ற நின் மாண்புடைய நலத்தை நினைந்தே.

#### The meaning — English

The jasmine has put out its sharp buds. The clearing-nut and the green-stemmed laburnum have
loosened their soft bindings and opened. Stags with great black antlers — twisted, as if someone
had heated iron and turned it — have come down to the pebbled hollows, and are leaping there for
the joy of the water. The world's long thirst-misery has turned its back and left. The cloud, with
its lightning and its thunder about it, has flung its fast drops down: **the rains are made**, and
the forest has gone beautiful.

And his horses — plumed with the curved crest, their manes clipped — come on so hard that the taut
reins sing like the strings of a yāḻ; and because there are bees asleep with their mates in the
flowering bower along his road, and he is afraid of startling them, **he has bound the tongue of
his chariot's bell.**

There — look — right there, he is coming: the man of the low-hill country.

O woman of the fine bangles: it is your beauty he has been thinking of — your beauty like the
just-opened flower of the glory lily on the great tall hill east of Uṟaiyūr, where the festivals go
loud with music.

#### நுட்பம் | Craft

**The tense of the season.** `கார்செய் தன்றே` — literally *it has made the kār*. Not "the rains
came." The cloud is the agent of a completed act, and the poem's first seven lines are a list of
that act's effects: buds sharpen, bindings loosen, stags leap, misery walks away. The rains are
established by their consequences before they are named — the same evidential method as poem 1's
desert, run in reverse.

**The bell.** `மணிநா வார்த்த` — *the tongue of the bell, bound*. The whole poem exists for this
half-line. A man racing home to a woman he has been away from, reins screaming — and he stops to
silence his own bell, for bees. Speed and tenderness in the same vehicle, and the tenderness costs
him nothing he was willing to keep.

**A recorded disagreement about that bell.** [மூலம் | SOURCE — file A, l. 453–462] Bees cannot
hear. Naccinārkkiṉiyar, citing this poem in his commentary on சீவகசிந்தாமணி, took that as the poet
mistaking the fact — writing as though `வண்டிற்குச் செவியறி வுண்டென`. சோமசுந்தரனார் rejects this
outright and reads it instead as **அன்புமடம்** — the *innocence of love*, an excess of tenderness
deliberately depicted — and compares it to **கொடைமடம்**, the giving-innocence of the chieftain who
covered a peacock with his cloak knowing perfectly well the bird could neither wear it nor be cold.
[விளக்கம் | INTERPRETATION] This is the better reading and it is also the more interesting one: the
mistake *is* the characterisation. He is not a man who believes bees can hear. He is a man too full
of care to do the arithmetic. And the friend telling this to the heroine is using it as an argument
— *a man like that will not have forgotten you.*

**Structure.** File A, l. 464 records that **Pēraciriyar** cited this very poem in his commentary on
Tolkāppiyam's செய்யுளியல் (sūtra 104) as an instance of **நோக்கு**. The poem is, in other words, a
classroom text about how a poem points.

**`உவக்காண்`.** One deictic particle — *look, over there* — and the whole poem changes register from
description to real time. Everything before it was seasonal; everything after it is happening now.
And it lands exactly on line 13 of 17, so the poem's turn and its metrical last stretch coincide.

---

### 6.3 · அகநானூறு 10 — *buds like stars, and a town called Toṇḍi*

**திணை:** நெய்தல் · **துறை:** தோழி தலைமகனை வரைவு கடாயது — *the friend pressing the hero to marry
her properly* · **புலவர்:** **அம்மூவனார்** · **13 lines** — one of the 22 shortest poems in the book
[மூலம் | SOURCE — file A, l. 730–747]

#### மூலம்

```
வான்கடற் பரப்பில் தூவற்கு கெதிரிய
மீன்கண் டன்ன மெல்லரும் பூழ்த்த
முடவுமுதிர் புன்னைத் தடவுநிலை மாச்சினைப்
புள்ளிறை கூரும் மெல்லம் புலம்ப
நெய்த லுண்கண் பைதல கலுழப் 5
பிரித லெண்ணினை யாயி னன்று
ம‌ரிதுதுற் றனையாற் பெரும வுரிதினிற்
கொண்டாங்குப் பெயர்தல் வேண்டுங் கொண்டலொடு
குரூஉத் திரைப் புணரி யுடைதரு மெக்கர்ப்
பழந்திமில் கொன்ற புதுவலைப் பரதவர் 10
மோட்டுமண ல‌டைகரைக் கோட்டுமீன் கொண்டி
மணங்கமழ் பாக்கத்துப் பகுக்கும்
வளங்கெழு தொண்டி ய‌ன்னவிவ ண‌லனே.
                              -அம்மூவ‌னார்
```
*(file A, lines 734–747)*

#### சொல்லுக்குச் சொல் | Word by word

| சொல் | பொருள் | English |
|---|---|---|
| வான்கடல் பரப்பு | பெரிய கடற்பரப்பு | the great sea's spread |
| தூவற்கு எதிரிய | துளிகளை ஏற்றுக்கொண்ட | meeting / taking the spray |
| மீன் கண்டன்ன | (சோமசுந்தரனார்) விண்மீனைக் கண்டாற்போல | like stars seen — *see the note below* |
| ஊழ்த்த | அரும்பு தோற்றுவித்த | having put forth |
| முடவு முதிர் புன்னை | முடம்பட்ட முதிர்ந்த புன்னை | the old crooked punnai (Alexandrian laurel) |
| தடவு நிலை மாச்சினை | வளைந்த நிலையையுடைய பெரிய கிளை | the great branch in its bent stance |
| புள் இறை கூரும் | பறவைகள் மிகுதியாகத் தங்கும் | where the birds roost thick |
| மெல்லம் புலம்ப | மென்புலமாகிய நெய்தல் நிலத் தலைவனே | O lord of the soft shore |
| நெய்தல் உண்கண் | நெய்தற் பூப்போன்ற மையுண்ட கண் | kohled eyes like the blue waterlily |
| பைதல கலுழ | துன்பமுற்று அழ | to grow wretched and weep |
| அரிது துற்றனை | நுகர்தற்கரியதை நுகர்ந்தாய் | you have swallowed something hard to swallow |
| உரிதினின் கொண்டு | உரிமையோடு ஏற்று | taking her by right |
| கொண்டல் | கீழ்க்காற்று | the east wind |
| எக்கர் | மணல் திட்டு | the dune |
| பழந்திமில் | பழைய படகு | the old boat |
| கோட்டுமீன் | சுறா | the horned fish — shark |
| கொண்டி | பிடிபட்ட பொருள் | the take, the catch |
| பகுக்கும் | கூறுவைத்து வழங்கும் | they portion out and share |
| பாக்கம் | நெய்தல் நிலச் சிற்றூர் | the fishing hamlet |
| தொண்டி | சேரர் துறைமுகம் | Toṇḍi, a Chera port |

*(Glosses follow சோமசுந்தரனார், file A l. 750–762.)*

#### பொருள் — தமிழ்

பெருங்கடற் பரப்பில் எழும் திவலைகளை ஏற்றுக்கொண்டு, மீன் கண்டாற்போன்ற மெல்லிய அரும்புகளைத்
தோற்றுவித்த, முடமாய் முதிர்ந்த புன்னையின் வளைந்த பெருங்கிளையில் பறவைகள் நிறையத் தங்கும் மென்புலத்
தலைவனே! எம் தலைவியின் நெய்தற்பூப் போன்ற மையுண்ட கண்கள் துயருற்று அழும்படி பிரியக் கருதினையாயின்,
நுகர்தற்கரியதொன்றை நீ நுகர்ந்தாய் ஆவாய். பெருமானே — கீழ்க்காற்றோடு நிறமிக்க பேரலைகள் மோதி
உடைக்கும் மணல்திட்டு அவர்தம் பழைய திமிலை அழித்தமையால், புதிய வலைகள் இருந்தும் வேட்டைக்குச்
செல்லாத பரதவர், உயர்ந்த மணற்கரையில் தாமே வந்தேறிய சுறாவைப் பிடித்து, மணங்கமழும் பாக்கத்தில்
எல்லார்க்கும் கூறுவைத்து வழங்குகின்ற — வளம் பொருந்திய தொண்டிப் பட்டினம் போன்ற — இவளுடைய நலத்தை,
உரிமையோடு ஏற்று அழைத்துச் செல்லுதலே நீ செய்யத் தக்கது.

#### The meaning — English

Lord of the soft shore — where the old crooked punnai takes the spray off the wide sea and has put
out soft buds on its bent great branch, and the birds crowd there to roost:

if you are thinking of leaving, and letting her waterlily eyes go dark with weeping, then you have
swallowed something no one can swallow.

Sir: the east wind drives the coloured breakers in, and the dune they have broken has crushed the
fishermen's old boat, so that although their nets are new they do not put out to sea — they take
the shark that comes aground of itself on the high sand, and they carry it up into the
sweet-smelling hamlet and cut it into shares for everyone. Her beauty is like that town — rich
Toṇḍi. **Take her by right, and go.**

#### நுட்பம் | Craft

**The உள்ளுறை, unpacked — and a disagreement about what to call it.** [மூலம் | SOURCE — file A,
l. 764–765] Why the boat, the nets, the beached shark? The old commentator (பழையவுரையாசிரியர்)
spells it out: the fishermen, having lost their boat, do not do their proper work; they take what
came without seeking, and divide it publicly so that everybody knows. *Just so* — he says — the
hero, instead of walking the honourable road, keeps to the clandestine way, and spreads it until
the town is talking. The praise is a rebuke. "Her beauty is like rich Toṇḍi" arrives sounding like
a compliment and turns out to be the sharp end.

And then the two commentators disagree about the machinery itself: the old commentator files this
as **இறைச்சிப் பொருள்**; சோமசுந்தரனார் replies that since the passage is expounded as comparison
and thing-compared, it is properly **உள்ளுறை உவமை**. [விளக்கம் | INTERPRETATION] Worth keeping the
argument rather than picking a winner — the two categories mark the difference between *meaning
that leaks out of a scene* and *meaning deliberately built into it as a figure*, and this poem sits
on the seam.

**The ending.** `வளங்கெழு தொண்டி ய‌ன்னவிவ ண‌லனே.` — the poem's last word is her worth, and the last
proper noun is a **port town**. Not a flower, not a star: a place where wealth arrives and is
divided fairly. In a poem urging marriage over concealment, the final image of value is a
functioning public economy.

**⚠️ [திறந்த கேள்வி | OPEN QUESTION] — `மீன்கண் டன்ன`.** The e-text line reads `மீன்கண் டன்ன`,
which the eye naturally splits as **மீன் கண் அன்ன** — *like fish-eyes*, a famous and physically
exact description of small pale punnai buds. But சோமசுந்தரனார்s own gloss at A l. 750 splits it
`மீன் கண்ட அன்ன` and explains it `விண்மீனைக் க‌ண்டாற் போன்று` — *like stars, seen*. Two readings,
same letters, both beautiful, and the choice changes whether the tree is being compared to the sea
or to the sky. **I have no basis for choosing and am not going to pretend to one.** This is a
question for Ilam's ear and for a second edition.

---

## 7. வரலாறு உள்ளே | The history inside the similes

[விளக்கம் | INTERPRETATION] அகம் poems are, by convention, *anonymous in their persons* — no lover
is ever named. But the **similes** are under no such rule, and this is the crack through which real
history enters the most private genre in Tamil. When a poet needs an image for a long journey or a
great hoard or an unstoppable force, he reaches for the news. அகநானூறு, being the long anthology,
has more room for such images than any other akam book — which is why historians read it.

[முடிவு | RESULT — computed over the parsed verse text of all 400 poems] Proper names in the verse
text, by poem:

| Name | Poems | What it is |
|---|---|---|
| **மோரியர்** | **69, 251, 281** | the Mauryas |
| **நந்தர் / நந்தன்** | **251, 265** | the Nandas of Magadha |
| **யவனர்** | **149** | the Yavanas — Greeks/Romans/Levantines |
| **முசிறி** | 57, 149 | Muciṟi / Muziris, the Chera pepper port |
| **தொண்டி** | 10, 60 | Toṇḍi, Chera port |
| **கோசர்** | 15, 90, 113, 196, 205, 216, 251, 262 | the Kōsar confederacy |
| **வடுகர்** | 107, 213, 253, 281, 295, 375, 381 | northerners / Telugu-country people |
| **நன்னன்** | 11 poems | the chieftain Naṉṉaṉ |
| **கரிகால்** | 55, 125, 141, 246, 376 | Karikāl the Chola |
| **இமயம் · கங்கை · பாடலி** | 265 | Himālaya, Ganges, Pāṭaliputra |

### 7.1 The best-dated reference: the Nandas' sunken treasure — அகநானூறு 265

**திணை:** பாலை · **புலவர்:** **மாமூலனார்** · [மூலம் | SOURCE — file D, l. 1818–1826]

```
புகையிற் பொங்கி வியல்விசும்பு உகந்து
பனியூர் அழற்கொடி கடுப்பத் தோன்றும்
இமயச் செவ்வரை மானுங் கொல்லோ
பல்புகழ் நிறைந்த வெல்போர் நந்தர்
சீர்மிகு பாடலிக் குழீஇக் கங்கை 5
நீர்முதற் கரந்த நிதியங் கொல்லோ
எவன்கொல் வாழி தோழி வயங்கொளி
```
*(file D, lines 1820–1826; poet named at l. 1843 — மாமூலனார்)*

**பொருள்:** *Is it like the red Himalayan peak, that rises smoking into the wide sky and shows like
a flame-creeper wearing frost? Or is it like the treasure the Nandas of many victories massed at
great Pāṭali and hid under the water of the Ganges? What is it, friend —* … the poem then turns and
names the thing being measured: **the wealth my lord went away to get**, which he weighed heavier
than me (`நம்மினும் வலிதாத் தூக்கிய பொருளே`, D l. 1842).

[விளக்கம் | INTERPRETATION] The poem is a woman asking her friend how big a thing must be, to
outweigh her. The two units of measure she reaches for are **the Himalaya** and **the treasury of
the Nanda dynasty sunk in the Ganges at Pāṭaliputra.** For a poet on the far southern tip of the
subcontinent to use the Nandas' hoard as a household unit of "unimaginably much" tells us the
Magadhan empire was *news that had travelled* — not learned reference but common currency, the way
a modern speaker says *Fort Knox*.

**Dating.** [கருதுகோள் — and contested] The Nandas held Magadha in roughly the **late 4th century
BCE**, and were displaced by Chandragupta Maurya around **321 BCE** — a range, not a date, and the
absolute chronology of the Nandas is itself disputed. What this poem licenses is narrower than it
looks. It gives a **terminus post quem for the memory, not for the poem**: மாமூலனார் can only be
writing *after* the Nandas were famous, but "after" could be a generation or five. Scholars have
used the Maurya and Nanda references to argue that மாமூலனார் belongs to an early stratum of the
corpus; others treat such references as inherited poetic furniture that says nothing about a
particular poet's date. **Both positions are live. This document does not adjudicate between them,**
and any single date offered for அகநானூறு — or for the Sangam corpus at large, conventionally placed
somewhere in the wide band c. 300 BCE – 300 CE — should be treated as one position among several.

### 7.2 The Mauryas cutting the mountain — 69, 251, 281

Three poems, all பாலை, share a single startling image: the Mauryas **cut a rock passage open so
their chariot wheels could roll through.**

அகநானூறு 69 (புலவர்: உமட்டூர்கிழார் மகனார் பரங்கொற்றனார்) [மூலம் | SOURCE — file B, l. 419–421]:

```
விண்பொரு நெடுவரை இயல்தேர் மோரியர் 10
பொன்புனை திகிரி திரிதரக் குறைத்த
அறையிறந் தகன்றனர் ஆயினும் எனையதூஉம்
```

அகநானூறு 281 (புலவர்: மாமூலனார்) [மூலம் | SOURCE — file D, l. 2350–2354]:

```
வான்போழ் வல்வில் சுற்றி நோன்சிலை 5
அவ்வார் விளிம்பிற்கு அமைந்த நொவ்வியல்
கனைகுர லிசைக்கும் விரைசெலற் கடுங்கணை
முரண்மிகு வடுகர் முன்னுற மோரியர்
தென்றிசை மாதிரம் முன்னிய வரவிற்கு
```

**பொருள் (281):** *…with the Vaḍukar of great enmity going before them, the Mauryas, in their advance
towards the southern quarter, cut through the rock on the high cold mountain that touches the sky,
so that the bright-rayed wheel could roll* — and it is **that** pass her lord crossed and went.

[விளக்கம் | INTERPRETATION] Notice what the image is *for*. In all three poems it is a measure of
**distance and irreversibility**: the road he took is the road an empire had to carve. The Mauryan
army is not the subject of any of these poems. It is the yardstick.

[திறந்த கேள்வி | OPEN QUESTION] Whether these lines record an actual Mauryan military push into the
far south is a genuinely open historical question — the northern sources do not describe a Mauryan
conquest of the Tamil country, and Ashoka's own edicts name the Cholas, Pandyas and Keralaputras as
*neighbours outside* his realm. The poems record that southern poets knew of Mauryan chariots
coming south and of rock being cut for them. What exactly they knew, and how accurately, is not
settled. [கருதுகோள்] File B, l. 451 preserves a striking alternative: the old commentary on
புறநானூறு 175, quoted there, glosses மோரியர் not as a historical dynasty at all but as legendary
universal emperors — evidence that by the commentators' own period the reference had already gone
soft.

### 7.3 The gold-for-pepper trade at Muziris — அகநானூறு 149

**திணை:** பாலை · **புலவர்:** **எருக்காட்டூர்த் தாயங்கண்ணனார்** · [மூலம் | SOURCE — file C,
l. 1044–1064]

```
வாரேன் வாழியென் நெஞ்சே சேரலர்
சுள்ளியம் பேரியாற்று வெண்நுரை கலங்க
யவனர் தந்த வினைமாண் நன்கலம்
பொன்னொடு வந்து கறியொடு பெயரும் 10
வளங்கெழு முசிறி ஆர்ப்பெழ வளைஇ
```
*(file C, lines 1052–1056)*

**பொருள்:** *I will not go, my heart — live long. Where the white foam of the Cheras' great Cuḷḷi
river is churned, the well-wrought ships the Yavanas brought **come with gold and leave with
pepper**, at Muciṟi of abundance…* — and the poem goes on to the Pandya Ceḻiyaṉ who besieged that
same Muciṟi till it roared, won a hard battle and carried off an image, and to Kūḍal of the
banner-fluttering streets.

[விளக்கம் | INTERPRETATION] `பொன்னொடு வந்து கறியொடு பெயரும்` — *comes with gold, leaves with
pepper* — is one of the most-cited half-lines in Tamil, and it is a **balance-of-trade statement**
in seven words: bullion in, spice out. The direction matters. It is the Tamil coast that receives
the gold. The commentator in file C, l. 1073, glosses யவனர் plainly as `எகித்து, கிரேக்கம்
முதலிய புறநாட்டினர்` — foreigners of Egypt, Greece and so on.

**Dating.** [கருதுகோள் — contested] The Muziris pepper trade with the Roman world is independently
attested from the Mediterranean side (the *Periplus*, Pliny's complaint about bullion draining east,
the Muziris papyrus) and is generally placed in the **first two centuries CE**, with its heaviest
phase in the 1st century CE. That gives this poem an external anchor that the Nanda and Maurya
poems do not have — but again it anchors the *reference*, not necessarily the composition, and the
Muziris trade itself has both earlier and later phases. What is safe to say: **அகநானூறு 149
describes a working international bullion-for-spice trade at a named west-coast port, and an
independent Mediterranean documentary record describes the same trade at the same port.** That
convergence is the strongest historical datum in the anthology.

### 7.4 A war in fifteen lines, to say *he left* — அகநானூறு 251

**திணை:** பாலை · **புலவர்:** **மாமூலனார்** · [மூலம் | SOURCE — file D, l. 1337–1360]

```
1நந்தன் வெறுக்கை யெய்தினும் மற்றவண் 5
தங்கலர் வாழி தோழி வெல்கொடித்
துனைகா லன்ன புனைதேர்க் கோசர்
தொன்மூ தாலத் தரும்பணைப் பொதியில்
இன்னிசை முரசங் கடிப்பிகுத் திரங்கத்
தெம்முனை சிதைத்த ஞான்றை மோகூர் 10
பணியா மையிற் பகைதலை வந்த
மாகெழு தானை வம்ப மோரியர்
புனைதேர் நேமி யுருளிய குறைத்த
இலங்குவெள் ளருவிய 2அறைவா யும்பர்
```
*(file D, lines 1344–1353)*

**பொருள்:** *Even if he were to gain the hoarded wealth of Nandaṉ himself, he will not stay there.
… When the Kōsar of victorious banners and chariots swift as the wind sounded their sweet-voiced
war-drum under the ancient banyan of the great assembly-ground, and broke the enemy's front — that
day, because **Mōkūr would not bow**, the upstart Mauryas came against it with their great army,
and cut the rock so the wheels of their fine chariots could roll: **above that cut face**, with its
gleaming white waterfall…* — and only then does the poem arrive at the tiger, the elephant, the
long road, and the man who loosened the bangles from her arm and went.

[விளக்கம் | INTERPRETATION] This is the anthology's method at full extension, and worth walking
through as craft. Twenty lines. **Two** of them concern the lovers (`அரம்போழ் அவ்வளை நிலைநெகிழ்த்
தோரே` — *he who loosened the file-cut bangle from its place*). Eighteen build a world: a dynasty's
treasury in the north, a drum under a banyan, a town that refused to submit, an invasion provoked by
that refusal, an engineering work in the mountains, a waterfall over the cut, a tiger that escaped
an elephant's jaws and killed the ground with a blow, a teak forest where nothing is guarded.

The word `வம்ப` in `வம்ப மோரியர்` is doing quiet, savage work: **newcomers, upstarts, parvenus.**
A southern poet calling the Mauryan empire *the new lot*.

And the syntax is the point. All of that — Nandas, Kōsar, Mōkūr, Mauryas, the cut rock — is
**subordinate**. The main clause is *he has gone, and my bangles are loose.* The empire is a
prepositional phrase attached to a woman's wrist.

---

## 8. புலவர் | The poets

[முடிவு | RESULT — computed from the colophon line of every poem]

- **183 distinct author-name strings** after normalising whitespace — against the tradition's **145**
  (file E, l. 3389). The gap is orthographic, not substantive: the e-text carries variants such as
  நக்கீரர் / நக்கீரனார், மதுரை மருதனிள நாகனார் / மதுரை மருதன் இளநாகனார், பாலைபாடிய பெருங்கடுங்கோ /
  பாலை பாடிய பெருங்கடுங்கோ, which a careful collation would merge. **145 is the better number; 183
  is what an uncollated machine count returns.** [திறந்த கேள்வி] Reconciling the two exactly — which
  variants merge and which are genuinely different poets — is real work not done here.
- **Three poems carry no poet's name: 114, 117, 123.** This is not e-text damage. File A, l. 137
  states it independently — of the 145 poets, `மூவர் பெயர் காணப்படவில்லை`, three names are not
  found — and the commentary at B l. 2213 says of poem 114 in so many words that its author's name
  is not extant. The count I computed and the count the editors state agree exactly at three.

**The most-represented poets:**

| Poet | Poems |
|---|---|
| **பரணர்** | 34 |
| **மாமூலனார்** | 26 |
| **மதுரை மருதனிள நாகனார்** (all spellings) | 18 |
| **கபிலர்** | 17 |
| **நக்கீரர் / நக்கீரனார்** | 14 |
| **கயமனார்** | 12 |
| **பாலைபாடிய பெருங்கடுங்கோ** | 11 |
| குடவாயிற் கீரத்தனார் | 9 |
| கல்லாடனார் · உலோச்சனார் | 7 each |

[விளக்கம் | INTERPRETATION] Two observations worth keeping. First, **மாமூலனார்** is the historians'
poet: he wrote 26 of the 400, and three of the five poems carrying the Maurya/Nanda material (251,
265, 281) are his. If any single voice in the anthology is preoccupied with the north, it is his.
Second, **பாலைபாடிய பெருங்கடுங்கோ** — "the great Kaḍuṅkō who sang pālai" — is a poet named *for the
landscape he specialised in*, a naming habit the corpus uses more than once (compare
செம்புலப் பெயனீரார், read in `../../ilakkiyam/sangam.md` §2). The person dissolves; the signature
image survives.

---

## 9. மூலத்தின் நிலை | The state of this e-text — read this before quoting

[முடிவு | RESULT — observed while parsing] These files are excellent and they are not perfect. Four
things a future session must know:

**1. Two editorial traditions, two orthographies.** Files A/B (சோமசுந்தரனார், 1970) print the verse
in the old **joined-sandhi** form, where a word runs across the line-break —
`கண்ணி யொண்கழ` at the end of one line and `லுருவக் குதிரை` at the head of the next. Files C/D/E (நாட்டார், 1965) print it **word-split** (`பதம் பிரித்து`).
Same poems, two conventions. For a learner this is a gift: the same corpus lets you practise reading
both, and A/B's joined form is closer to what a manuscript actually looks like.

**2. Occasional dropped lines.** At least two poems are short by one line in the e-text: **165**
(file C, l. 1565ff — the print marker `5` sits on the 4th surviving line) and **341** (file E,
l. 1413ff). The embedded print line-markers make such losses detectable, which is how I found them.
**Any line count taken by counting e-text lines rather than reconstructing from markers will be
wrong for ~50 poems.**

**3. Character-level defects.** Poem 10's first line in the e-text reads `தூவற்கு கெதிரிய`; the
same editor's own gloss at A l. 750 reads `தூவற்கு எதிரிய`. A stray `க`. Similarly A l. 315 carries
a spurious puḷḷi in `வெங்கதி்ர்`, and zero-width joiners are scattered through file A. **Quote
verbatim, then flag** — which is what this document does.

**3b. Two kinds of stray digit inside the verse.** A numeral at the **end** of a line is a
print-edition line marker (`5`, `10`, `15` …) and is trustworthy — §2 depends on it. A numeral
**glued to the front of a word** (`1நந்தன்`, `2அறைவா`) is a footnote key pointing at the
`(பாடம்)` variant-readings list a few lines below. Both are preserved verbatim in the quotations
above, because stripping them would make the quotations un-greppable. Strip them in your head, not
in the file.

**4. Poem 39 has no `திணை:` line** (file A, l. 2080ff), and poem 44's is anomalous (§4). Anyone
scripting over these files should special-case both.

---

## 10. காதுக்காக | Awaiting the ear

*Addressed to Ilam. Everything in this section is **computed, not heard.** I have no access to how
any of it sounds, and per `../../murai.md` §8 your ear is the authority.*

1. **The முச்சீர் penultimate line (§3).** I can show that 389 of 400 poems have a short
   second-to-last line. I cannot hear what that does. Does அகவல் actually *land* differently because
   the line before the last one is clipped — a drawing-in of breath before the close? Read
   அகநானூறு 4 aloud: `போதவி ழலரி னாறு` / `மாய்தொடி யரிவைநின் மாணலம் படர்ந்தே.` Is that a real
   effect or a page fact?

2. **மோனை in poems 1, 4, 10.** My token-level computation finds initial-letter agreement in about
   half the lines of each — e.g. poem 4's `கருவி வானங் கதழுறை சிதறிக்` and `கார்செய் தன்றே கவின்பெறு
   கானங்` both carry a க-run. But because files A/B use joined sandhi, my "feet" are not சீர், so
   **these counts may be artefacts.** Please check by ear whether the க-chain across those two lines
   is audible, or whether I am hearing my own tokeniser.

3. **`கார்செய் தன்றே`.** Does the -ஏ here land as the closing particle we found in குறுந்தொகை 40
   (`தாம் கலந்தனவே`, quoted in `../../ilakkiyam/sangam.md` §2) — audible finality — or as something else mid-poem?

4. **`உவக்காண்` (poem 4, l. 13).** In spoken Tamil, is there a living descendant of this — a
   one-word "look, right there" with that same pointing force? If so it belongs in `../../agaraadhi.md`.

5. **`மீன்கண் டன்ன` (poem 10, §6.3).** *Fish-eyes* or *stars-seen*? சோமசுந்தரனார் says stars; the
   letters permit both. **This is the single most useful thing your ear could settle in this
   document.** Which one does the line want?

6. **`வம்ப மோரியர்` (poem 251).** I have rendered வம்ப as *upstart / newcomer / parvenu*. Is that
   register right, or is it neutral ("newly-arrived") and I have put contempt into it that is not
   there?

7. **Register of my Tamil prose in §6.** The பொருள் paragraphs are my own composition, not quoted.
   They are the most likely place in this document for wrong Tamil. Please mark them up freely —
   per `../../murai.md` §3, wrong Tamil is data.

---

## 11. திறந்த கேள்விகள் | Open questions, collected

1. **Poem 44** — edition error or genuine commentarial dissent? Needs a second edition to collate.
2. **145 vs 183 poets** — which name-variants merge? A proper collation would settle it.
3. **The பாலை ratio** — is 200/400 an artefact of the odd/even grid, or was the grid fitted to a
   real corpus distribution? Testable against the local குறுந்தொகை and நற்றிணை e-texts.
4. **The three division-names** — file A, l. 139 claims each was quarried from a phrase occurring
   inside the anthology. I could locate `மணிமிடை பவளம்` only in editorial prose in these files, not
   inside any of the 400 poems. Either the phrase sits in a poem in a form my search missed, or the
   claim is a later rationalisation. **Unresolved.**
5. **The Mauryan southern campaign** — what, if anything, in 69 / 251 / 281 is testimony rather than
   inherited image?
6. **Ordering within a திணை class** — the rule fixes *which* landscape occupies a slot. Is there any
   further order *within* the 200 பாலை poems (by துறை? by poet? by length?), or is the sequence free
   once the landscape constraint is met? I did not test this and it is a clean, checkable question.

---

## 12. அடுத்து | Where this goes

- **`marabu/`** — அகநானூறு 4 is the strongest candidate in this document for a child-facing entry.
  The hook writes itself: *a man ties up his bell so he won't wake the bees.* Age 7+, one image, no
  grammar required, and the whole ஐந்திணை system can be introduced from it later.
- **`paadam/`** — §4's numbering rule is a complete lesson on its own: a text with an error-detecting
  code built into its table of contents, 1,500 years before the phrase existed.
- **`aaivu/karuthu/`** — two live disagreements are preserved above and belong on that shelf in full
  arc: Naccinārkkiṉiyar vs. சோமசுந்தரனார் on the bees (§6.2), and the old commentator vs.
  சோமசுந்தரனார் on இறைச்சி vs. உள்ளுறை (§6.3).
- **`aaivu/saaram.md`** — the pattern this anthology contributes: *meaning carried in the
  arrangement, not only in the poems*. The numbering rule is a claim made by the **shape of the
  book**, which no individual poem states and every poem confirms.

---

*Written from `_src/txt/` only. Every மூலம் quotation above carries a file and line number and was
extracted by script. Nothing was reconstructed from memory. Provenance labels follow
`../../murai.md` §11.*

*தொடங்கியது — 23 August 2026.*
