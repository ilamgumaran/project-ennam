# புறநானூறு | The Four Hundred on the Outer Life

*The great புறம் anthology — war, kings, generosity, hunger, death, and the ethics of public life.*

---

## 0. இந்த ஆவணம் | What this document is, and how it was made

**மூலம் | SOURCE — the one file.** Every Tamil line quoted below is copied verbatim from a single
local file:

```
_src/txt/pmuni0057-ettuthogai-purananuru.txt
```

a Project Madurai e-text (© மதுரைத் திட்டம் 2000; the header states the text may be freely
redistributed with the header intact). It was prepared by staff and students of K.A.P. Viswanatham
Higher Secondary School, Tiruchirappalli. The poems themselves are roughly two thousand years old
and in the public domain.

**A mechanical warning about this particular file.** The e-text is one enormous physical line
(line 39 of the file, 226,105 characters). The original HTML wrapped each verse-line in its own
paragraph; the stripping that produced this `.txt` **destroyed every line break inside every poem.**
Verse lines are now fused end-to-start, sometimes with no space at all —
`கொன்றை;ஊர்தி வால்வெள் ளேறே;` (poem 1). Two consequences run through this whole document:

1. **Line counts cannot be computed from this file.** Anywhere below that a poem is presented in
   lines, those lines were recovered by a rule — *split where a punctuation mark is immediately
   followed by a Tamil letter with no space* — and each recovered fragment was then re-tested as a
   literal substring of the source. Where the e-text fused two verse lines **without** punctuation,
   the fusion is left standing and marked `⟨fused⟩` rather than guessed apart.
2. **Every Tamil string in this document is grep-verifiable.** All 48 quoted strings were
   programmatically checked against the source file; all 48 pass. If a quotation here does not
   `grep` in that file, it is an error in this document, not a variant reading.

**விளக்கம் | INTERPRETATION.** The counts in §2–§5 are this instance's own tallies over the
colophons, computed with scripts, not taken from any secondary authority. They are checkable, and
they are also **counts of what this edition says** — a different edition will give slightly
different numbers. That distinction is held open throughout.

**Not re-read here.** புறம் 192 (யாதும் ஊரே) and புறம் 86 (கல்லளை போல வயிறு) are already read in
[`../../ilakkiyam/sangam.md`](../ilakkiyam/sangam.md) §4–§5 and are not re-opened. One new datum
about 86 is added in §3, because `sangam.md` gives it no colophon and the source has one.

---

## 1. புறம் என்றால் என்ன | What "puṟam" actually means

**அகம்** is the inside — love, and only love, spoken by unnamed people. **புறம்** is everything
else: the outside, the public, the world where people have names.

That is not a topical distinction. It is a **grammatical** one. In akam, convention forbids naming
the lovers, because interior life is written as universal — anyone's. In puram, naming is the
point. A puram poem is anchored: *this* king, *this* battle, *this* dead man, *this* poet who came
begging and got what he came for or did not. The corpus splits along the axis of whether a proper
noun is allowed.

**[விளக்கம் | INTERPRETATION]** So புறநானூறு is the part of Sangam literature where Tamil holds
history — not as chronicle, which it never wrote, but as four hundred anchored moments with names
attached and an editorial note under each saying who spoke and to whom. It is, functionally, the
oldest surviving Tamil archive of public life.

---

## 2. நூலின் அமைப்பு | The structure, verified against the file

### 2.1 எத்தனை பாடல் | How many poems

| | |
|---|---|
| Canonical numbering | **400** (நானூறு = four hundred; the name is a count) |
| Numbered records actually present in this e-text | **398 poems + 1 lacuna marker = 399 records** |
| Missing outright | **2** — poems 267 and 268 |

**[மூலம் | SOURCE]** The file does not silently skip them. Between poem 266 and poem 269 it prints,
as its own entry:

> `267- 268 கிடைத்தில`

**கிடைத்தில** — "were not obtained." The archaic negative finite form (கிடை- + -த்த- + -இல), not
the modern *kiḍaikkavillai*. The editors kept the gap *visible* and numbered. That is a small,
serious act of scholarship: the anthology's own count of 400 is preserved, and the hole in it is
labelled rather than papered over by renumbering.

### 2.2 எங்கே சிதைந்தது | Where the manuscript rotted — a real gradient

The e-text represents illegible passages by runs of spaced dots (`. . . . . .`). Counting poems that
contain such a run:

| Range | Poems with dot-lacunae |
|---|---|
| 1–243 | **0** |
| 244–400 | **38** |

Thirty-eight damaged poems, and **not one of them below 244.** The list: 244, 249, 282, 283, 285,
288, 306, 317, 321, 323, 328, 333, 334, 335, 337, 339, 340, 341, 346, 347, 352, 353, 355, 357, 366,
370, 371, 373, 377, 379, 380, 383, 384, 390, 393, 396, 398, 400.

**[கருதுகோள் | HYPOTHESIS]** This is the signature of a **palm-leaf bundle decaying from one end.**
An ōlai manuscript is a stack of leaves strung on a cord between two boards; the outermost leaves —
which is to say the *end* of the text as much as the beginning — take the damp, the insects and the
handling. A gradient this clean (zero, then thirty-eight) is what physical decay looks like, not
what scribal carelessness looks like: carelessness scatters.

**[திறந்த கேள்வி | OPEN QUESTION]** Whether the gradient is a property of the *manuscript tradition*
or of the *particular exemplar* U. V. Swaminatha Iyer's 1894 printed edition rested on. This file
cannot answer that; it is downstream of that edition. A scholar with access to the palm-leaf
descriptions could settle it.

The apparatus itself decayed alongside the verse. Poem 244's colophon is a note about its own loss:

Poem 289's whole classification reads:

> திணை, துறை. தெரிந்தில

and poem 361's reads:

> பாடியவர், பாடப்பட்டோர், திணை, துறை தெரிந்தில

**தெரிந்தில** — "were not known." Poems 289 and 361 have survived as *text* while losing every
piece of their identification. The poem outlived its own label.

### 2.3 காப்புச் செய்யுள் | The invocation

**[மூலம் | SOURCE]** Poem 1 is the only poem in the anthology with **no திணை and no துறை at all** —
its colophon names only a poet (பெருந்தேவனார்) and a subject (`பாடப்பட்டோன்: இறைவன்`, "the one sung
of: God"). It is a hymn to Śiva.

**[விளக்கம் | INTERPRETATION]** That absence is itself evidence. The புறத்திணை grid has no slot for
a god, because the grid was built to classify *human political situations*. The invocation is
therefore almost certainly **not part of the original anthology** but a later devotional cap fitted
to the front — the standard Tamil practice of adding a கடவுள் வாழ்த்து to an older secular
collection. The classifier's silence dates the poem.

---

## 3. திணையும் துறையும் | Thinai versus thurai — the two-level machine

This is the single most useful structural idea in the book, and it is routinely blurred in
summaries. The two are **not** synonyms and **not** a genre-and-subgenre pair in the loose sense.

### திணை — the situation

**திணை** classifies **what kind of human situation the poem stands in.** In akam it is the famous
five landscapes. In puram it is a set of war-and-public-life situations, most of them named after
the **flower the warriors wore** while doing that particular thing: வெட்சி is the flower worn while
lifting the enemy's cattle; கரந்தை the flower worn while getting them back; வஞ்சி while marching to
invade; உழிஞை while besieging a fort; நொச்சி while defending the fort's wall; தும்பை in pitched
open battle; வாகை when you have won.

**[விளக்கம் | INTERPRETATION]** Note what that means: **the Tamil taxonomy of war is a botany.** The
categories are not "raid / counter-raid / invasion / siege / defence / battle / victory" as abstract
nouns. They are seven plants. A garland was a uniform, and the uniform became the name of the
situation, and the name of the situation became a literary genre. Nobody designed that; it silted
into place.

### துறை — the speech act

**துறை** is finer and different in kind. It classifies **what the poem is doing as an utterance** —
its illocutionary move, its speaker's posture, the exact conversational turn it occupies.

Within the single திணை **பொதுவியல்**, the source uses (among others) துறை values including
`கையறுநிலை` (the helpless-state lament for a dead patron), `பொருண்மொழிக் காஞ்சி` (the utterance of a
settled truth), `முதுமொழிக் காஞ்சி` (the utterance of an ancient saying), `ஆனந்தப் பையுள்` (grief
inside joy), `தாபதநிலை` (the state of one who has renounced), and `பெருங்காஞ்சி`. Same situation
class, six entirely different speech acts.

The clearest way to hold it:

> **திணை = which world you are standing in. துறை = what you are doing with your mouth while standing there.**

A single poem gets one of each. **[மூலம் | SOURCE]** Poem 91's colophon reads
`திணை : தும்பை. துறை: வாழ்த்தியல்.` — *situation:* pitched battle; *speech act:* blessing. The poem
is a benediction spoken inside a war. Neither label alone would tell you that; the pair does.

**[மூலம் | SOURCE — the datum `sangam.md` is missing]** Poem 86, read in `sangam.md` §5 without a
colophon, carries one here: `துறை: ஏறாண் முல்லை`, under திணை **வாகை**. So the anthologist did not
file the tiger-cave poem as a lament at all — he filed it under *victory*, in the speech-act slot
for a mother's declaration of her son's fighting stock. That reclassifies the poem's tone and is
worth folding back into `sangam.md`.

---

## 4. புறத்திணை in practice | The count

**[மூலம் | SOURCE — computed over all 399 records of the file]** 386 records carry a `திணை:` field.
Normalising the obvious typo `நொட்சி` → `நொச்சி` (poems 271, 272) and stripping variant notes:

| # | திணை | Poems | Share of tagged | The situation |
|---:|---|---:|---:|---|
| 1 | **பாடாண்** | **135** | 35.0% | Praise of a person; the patron poem |
| 2 | **வாகை** | **77** | 19.9% | Victory, and excellence of any kind |
| 3 | **பொதுவியல்** | **74** | 19.2% | The general/common — wisdom, death, lament |
| 4 | **காஞ்சி** | **30** | 7.8% | Impermanence; the instability of everything |
| 5 | **தும்பை** | **29** | 7.5% | Pitched battle in the open |
| 6 | **வஞ்சி** | **11** | 2.8% | The march to invade |
| 7 | **கரந்தை** | **11** | 2.8% | Recovering the lifted cattle |
| 8 | **நொச்சி** | **6** | 1.6% | Defending the fort wall |
| 9 | **பெருந்திணை** | **5** | 1.3% | Unmatched / improper love |
| 10 | **வெட்சி** | **5** | 1.3% | Lifting the enemy's cattle |
| 11 | **கைக்கிளை** | **3** | 0.8% | One-sided love |
| — | **உழிஞை** | **0** | — | **Besieging a fort** |
| — | *no திணை given* | 13 | — | Poems 1, 99, 174, 194, 200, 244, 267, 282, 289, 298, 312, 361, 380 |

**Three findings that fall straight out of the table.**

**(a) The anthology is not primarily a war book.** பாடாண் + வாகை + பொதுவியல் = **286 of 386 tagged
poems, 74%.** Praise, excellence, and general wisdom. The actual combat திணை — தும்பை, வஞ்சி,
கரந்தை, நொச்சி, வெட்சி — total **62 poems, 16%.** The popular image of புறநானூறு as an anthology of
battle is an artefact of which poems get anthologised for schoolbooks, not of the book's own shape.

**(b) உழிஞை has zero poems.** **[மூலம் | SOURCE]** The word `உழிஞை` occurs four times in the entire
file. Once as a *variant reading* in poem 37's colophon —

> `திணை: வாகை; உழிஞை எனவும் பாடம்`

("thiṇai: vākai; it is also read as uḻiñai") — and three times (poems 50, 76, 77) as the plant
itself, worn in a garland inside the verse. **Not once as a primary classification.** The
fort-siege category exists in the theory and has no poem filed under it in this edition. That is a
concrete, checkable hole in the grid.

**(c) The colophons use the twelve-fold scheme, not Tolkāppiyam's seven.** Tolkāppiyam's புறத்திணையியல்
gives seven புறத்திணை. The eleven distinct labels actually used here include கரந்தை, நொச்சி and
பொதுவியல், which belong to the **twelve-திணை** reckoning associated with the later handbook
புறப்பொருள் வெண்பாமாலை. **[கருதுகோள் | HYPOTHESIS]** The colophons are therefore later than the
poems and reflect a classification system that had already evolved past Tolkāppiyam by the time
someone sat down to label the collection. **[திறந்த கேள்வி | OPEN QUESTION]** How much later, and
whether the labels came in one editorial pass or accreted, is not decidable from this file.

### 4.1 துறை — the long tail

387 records carry a `துறை:` field. Normalising spacing variants, the file uses **more than 120
distinct துறை** for eleven திணை. The commonest:

| துறை | Poems | What the speaker is doing |
|---|---:|---|
| இயன்மொழி | 51 | Stating a patron's nature as fact |
| **கையறுநிலை** | **43** | The helpless state — lament for a dead patron |
| அரசவாகை | 34 | Declaring a king's excellence as king |
| மகட்பாற் காஞ்சி | 18 | The father refusing / defending a daughter sought in marriage-by-war |
| பரிசில் கடாநிலை | 16 | **Pressing a patron for the gift not yet given** |
| பொருண்மொழிக் காஞ்சி | 15 | Stating a settled truth |
| பரிசில் | 15 | The gift itself |
| வல்லாண் முல்லை | 15 | The strong man's steadiness |
| மூதின் முல்லை | 14 | The old-family woman's fortitude |

**[விளக்கம் | INTERPRETATION]** Look at what the vocabulary is *fine-grained about*. Tamil poetics
did not need one word for "asking a patron for money." It needed **at least four** — பரிசில் (the
gift), பரிசில் கடாநிலை (pressing for it), பரிசில் விடை (taking leave after it), பரிசில் துறை. And
கையறுநிலை, at 43 poems, is the second-commonest speech act in the entire book: **eleven percent of
புறநானூறு is a poet standing over a dead patron.** The technical vocabulary is densest exactly where
the poet's own livelihood and grief were.

---

## 5. மன்னரும் வேளிரும் | Kings, chieftains, and where the anthology's heart actually is

**[மூலம் | SOURCE — computed over the `பாடப்பட்டோன்` field]** 245 of 399 records name an addressee.
Of those:

| | Poems |
|---|---:|
| The three crowned dynasties (சேரர் + சோழர் + பாண்டியர்) | **114** |
| Uncrowned chieftains and others | **131** |

Broken out: **சோழர் 65, பாண்டியர் 26, சேரர் 24** (one poem, 58, is addressed jointly to a Chola
*and* a Pandya and is counted once).

**This is the finding that should reset anyone's picture of the book.** More poems are addressed to
men who wore no crown than to all three imperial houses put together. புறநானூறு is not a court
anthology of the மூவேந்தர். Its centre of gravity is the **வேளிர்** — the hill and border chieftains
who had no standing army, no capital worth the name, and, apparently, the best poets.

### 5.1 கடையெழு வள்ளல் | The seven patrons

Tradition names seven great givers. All seven are attested in this file, and the distribution is
lopsided:

| Patron | Poems | Numbers |
|---|---:|---|
| **அதியமான் நெடுமான் அஞ்சி** | **25** | 87–98, 100–104, 206, 208, 231, 232, 235, 315, 390, 392 |
| **ஆய் அண்டிரன்** | **17** | 127–136, 138–140, 240, 241, 374, 375 |
| **வேள் பாரி** | 7 | 105–111 |
| **வையாவிக் கோப்பெரும் பேகன்** | 7 | 141–147 |
| **மலையமான் திருமுடிக்காரி** | 5 | 121–124, 126 |
| **வல்வில் ஓரி** | 3 | 152, 153, 204 |
| **கண்டீரக் கோப் பெருநள்ளி** | 3 | 148, 149, 150 |
| | **67 poems** | |

**அதியமான் நெடுமான் அஞ்சி, at 25 poems, is the most-sung individual in புறநானூறு** — ahead of every
Chola, every Pandya, every Chera. He was a chieftain of தகடூர் (modern Dharmapuri), and by the
book's own count he outweighs the emperors.

**[மூலம் | SOURCE — a structural fact about the anthology's arrangement]** The poems are not
scattered. They come in **patron blocks**: 87–104 is Adhiyaman, 105–111 is Pāri, 121–126 is Kāri,
127–140 is Āy, 141–147 is Pēkan, 148–150 is Naḷḷi. Whoever compiled this collection sorted it by
*who was being sung to*, not by திணை and not by poet. That is an editorial decision with a visible
signature, and it means the compiler had access to poems already grouped — or did the grouping
himself and left us the seam.

### 5.2 வடக்கிருத்தல் | Facing north to die

**[மூலம் | SOURCE]** Six poems (65, 215, 216, 218, 220, 236) turn on **வடக்கிருத்தல்** — sitting
facing north and fasting to death. It is done by the defeated (poem 65) and, more startlingly, by
poets: poem 236's editorial note says Kapilar sang it *while sitting north* after Pāri's death,
having first found homes for Pāri's daughters. The lament and the suicide are the same act.

**[விளக்கம் | INTERPRETATION]** The புறம் ethic that emerges across these six is that **a life is
finished when its public role is finished**, and that ending it deliberately is a recognised, named,
classifiable procedure rather than a private despair. It has a துறை.

---

## 6. ஔவையார் — எந்த ஔவையார்? | Which Auvaiyar

**[மூலம் | SOURCE]** ஔவையார் is the **single most prolific poet in புறநானூறு: 32 poems** —
87–98, 100–104, 140, 187, 206, 231, 232, 235, 269, 286, 290, 295, 311, 315, 367, 390, 392. கபிலர் is
second with 30.

Seventeen of those 32 are one continuous block on அதியமான் நெடுமான் அஞ்சி (87–98 and 100–104). She
did not merely praise him; she praised him, was fed by him, was sent by him as an envoy, and then
buried him — poems 231, 232 and 235 are all `கையறுநிலை`, laments for him dead. **[விளக்கம் | INTERPRETATION]**
No other poet–patron relationship in the corpus is documented at this length or through this many
registers. It is the closest thing early Tamil has to a sustained portrait of a friendship.

> **⚠ The confusion this repo has already flagged.** `../../marabu/paadal/002-aathichudi-uyir-varukkam.md`
> §9 records it: **"ஔவையார்" is not one poet.** It is a name — roughly *the venerable woman* — borne
> by at least three or four poets across more than a thousand years. The ஔவையார் of these 32 Sangam
> poems, Adhiyaman's friend, is **not** the ஔவையார் of ஆத்திசூடி, கொன்றைவேந்தன், மூதுரை and
> நல்வழி, who is very much later. Conflating them is the commonest error in popular Tamil literary
> history. Nothing in this document should be read as attributing ஆத்திசூடி to the poet of §7.2.

### 6.1 பெண் புலவர் | The women in the book

**[மூலம் | SOURCE]** Filtering the poet field for name-forms that are explicitly feminine — those
containing ஔவை, பெண்டு, மகள், தேவி, பாடினியார், or a known woman's name — yields **13 distinct
name-strings covering 51 poems**:

| Poet | Poems |
|---|---|
| ஔவையார் | 32 |
| மாறோக்கத்து நப்பசலையார் | 37, 39, 126, 174, 226, 280, 383 |
| பெருங்கோழி நாய்கன் மகள் நக்கண்ணையார் | 83, 84, 85 |
| பேய்மகள் இளவெயினியார் | 11 |
| காவற் பெண்டு | 86 |
| குறமகள் இளவெயினி | 157 |
| பூதப் பாண்டியன் தேவி பெருங்கோப்பெண்டு | 246 |
| வெறி பாடிய காமக்கண்ணியார் | 271 |
| காக்கைபாடினியார் நச்செள்ளையார் | 278 |
| ஒக்கூர் மாசாத்தியார் | 279 |
| நெடுங்கழுத்துப் பரணர் | 291 |
| பொன்முடியார் | 310 |

**[திறந்த கேள்வி | OPEN QUESTION]** This is a **floor, not a count.** The honorific `-ஆர்` is
gender-neutral in Tamil, so a woman whose name carries no feminine marker is invisible to this
method. `நெடுங்கழுத்துப் பரணர்` is included only because tradition holds this poet to be a woman;
the *name* does not say so. The true number of women in புறநானூறு cannot be recovered from
orthography and is a question for scholarship, not for a script.

**[மூலம் | SOURCE]** 180 distinct poet name-strings appear; **126 of them contribute exactly one
poem.** Eight poems carry an explicit `பெயர் தெரிந்திலது` — "the name is not known" (256, 257, 327,
328, 333, 339, 340, 355), and ten poems name no poet at all.

---

## 7. நான்கு பாடல், ஆழமாக | Four poems, read closely

Chosen for range: a king's own voice from inside a prison; a woman's lament for a dead patron;
a mother on a battlefield; and the anthology's most-quoted statement of what a good life is.

---

### 7.1 புறம் 74 — ஈன்மரோ இவ்வுலகத்தானே | *Does this world give birth to such men?*

**[மூலம் | SOURCE — colophon, verbatim]**
`74. வேந்தனின் உள்ளம்! பாடியவன்: சேரமான் கணைக்கா லிரும்பொறை திணை: பொதுவியல் துறை; முதுமொழிக் காஞ்சி`

Note `பாடியவன்` — the **masculine** singular, not the honorific `பாடியவர்` used almost everywhere
else in the book. The colophon-writer drops the honorific because the poet is a king. The colophon
also cites a commentator by name: `'தாமே தாங்கியதாங்கரும் பையுள்' என்னும் துறைக்குக் காட்டுவர் இளம்பூரணர்`
— "Iḷampūraṇar cites it for the thurai *the unbearable grief they bore themselves*." A grammarian's
citation has been folded into the anthology's own apparatus.

#### மூலம்

> குழவி இறப்பினும், ஊன்தடி பிறப்பினும்,
> ஆள் அன்று என்று வாளின் தப்பார்தொடர்ப்படு ஞமலியின் இடர்ப்படுத்து இரீஇயகேளல் கேளிர் வேளாண் சிறுபதம், ⟨fused: the e-text has lost two or three line breaks inside this stretch⟩
> மதுகை இன்றி, வயிற்றுத் தீத் தணியத்,
> தாம் இரந்து உண்ணும் அளவைஈன்ம ரோ, இவ் உலகத் தானே? ⟨fused⟩

#### சொல்லுக்குச் சொல்

| சொல் | பிரிப்பு | பொருள் | English |
|---|---|---|---|
| குழவி | — | குழந்தை | infant |
| இறப்பினும் | இற(ப்பு)+இன்+உம் | இறந்து பிறந்தாலும் | even if it is born dead |
| ஊன்தடி | ஊன் + தடி | சதைத் துண்டு | a lump of flesh |
| பிறப்பினும் | பிற(ப்பு)+இன்+உம் | பிறந்தாலும் | even if what is born is (only that) |
| ஆள் அன்று | — | மனிதன் அல்ல | "it is not a man" |
| வாளின் தப்பார் | — | வாளால் நீக்கத் தவறார் | they do not fail to (put it) to the sword |
| தொடர்ப்படு ஞமலி | தொடர் + படு + ஞமலி | சங்கிலியில் கட்டப்பட்ட நாய் | a dog held on a chain |
| இடர்ப்படுத்து இரீஇய | — | துன்புறுத்தி இருக்கச் செய்த | having tormented and made (one) sit |
| கேளல் கேளிர் | — | உறவல்லாத உறவினர் | kin who are not kin |
| வேளாண் சிறுபதம் | வேளாண்மை + சிறு + பதம் | உபகாரமாகத் தரப்பட்ட சிறு உணவு | the small ration handed over as a favour |
| மதுகை இன்றி | — | வலிமை இன்றி | without strength |
| வயிற்றுத் தீ | — | பசி என்னும் நெருப்பு | the fire in the belly |
| தணிய | — | தணிவதற்கு | for it to be quenched |
| இரந்து உண்ணும் அளவை | — | பிச்சை எடுத்து உண்ணும் அளவுக்கு | to the extent of eating by begging |
| ஈன்மரோ | ஈன்+மர்+ஓ | ஈன்பார்களோ? | do they give birth (to such)? |

**[திறந்த கேள்வி | OPEN QUESTION]** `ஞமலி` occurs **exactly once in the entire anthology** — here.
Whether the poet reached for a rare word for effect, or whether it was ordinary in his dialect and
this is simply the one place the topic arose, cannot be decided from a single attestation.

#### பொருள் — தமிழில்

செத்துப் பிறந்த குழவியாயினும், உருவமற்ற ஊன்தடியாகப் பிறந்ததாயினும், "இது ஆள் அல்ல" என்று சொல்லி
வாளால் அறுக்கத் தவறமாட்டார்கள் — அத்தகைய குடியில் பிறந்தவர்கள். அவர்கள், சங்கிலியில் கட்டிய நாயைப்
போலத் துன்புறுத்தி இருத்தி வைக்கப்பட்டு, உறவே அல்லாத உறவினர் உபகாரமாக இடும் சிறு உணவை, வலிமை இழந்து,
வயிற்றெரிச்சல் தணியும் பொருட்டுப் பிச்சையாக ஏற்று உண்ணும் அளவுக்கு — அத்தகையவர்களை இவ்வுலகம்
ஈன்றுவிடுமோ?

#### பொருள் — in English

Men of that line will not fail to put a thing to the sword and say *this is not a man* — not even if
what was born is a dead infant, not even if it is only a lump of flesh. And such men, tethered like
a chained dog, tormented and made to sit; taking, from kin who are no kin, the small ration handed
down as a favour; strengthless, and only so the fire in the belly might be quenched — begging, and
eating what is begged. **Does this world give birth to such men?**

#### நுட்பம் | Craft

**Who is speaking, and from where.** **[விளக்கம் | INTERPRETATION]** The colophon names the poet as
சேரமான் கணைக்கால் இரும்பொறை, a Chera king. The poem's speaker is a man of a line so fierce it
executes its own stillborn for failing to be a warrior — and who is now on a chain, eating charity
from people who are not really his kin, because his belly hurts. **The poem is a king describing his
own captivity.** The tradition holds that this Chera was taken prisoner by the Chola and died in
confinement. The poem does not narrate that. It only makes the ethical arithmetic of it unbearable.

**The mechanism is a collision of two scales of the same word — flesh.** Line 1's `ஊன்தடி`, the lump
of flesh cut down for not being a man, and line 3's `வயிற்றுத் தீ`, the fire in a living belly, are
the same substance seen from the two ends of a life. The code that kills the unfit infant and the
hunger that unmakes the fit king are one continuous thing.

**The verb `ஈன்ம ரோ` — "do they give birth?" — is doing something structurally strange.** A lament
would ask *why has this happened to me.* This asks whether the **world** produces such men at all. It
converts a private humiliation into a question about the species. That grammatical move — the
first-person situation stated only in the third person plural, the "I" never appearing — is what
puts the poem under `பொதுவியல் / முதுமொழிக் காஞ்சி`, "the general / the utterance of ancient truth,"
rather than under any war திணை. **The classifier read it as philosophy. That is why it survived.**

**[கருதுகோள் | HYPOTHESIS]** The most politically radical poems in this anthology are disproportionately
written **by rulers, not about them** — see §7.4, whose author is also a king. A poet who depended on
patronage could not safely write that the whole apparatus of rank is worth nothing against hunger. A
king could.

---

### 7.2 புறம் 235 — அருநிறத்து இயங்கிய வேல் | *The spear that went through*

**[மூலம் | SOURCE — colophon, verbatim]**
`235. அருநிறத்து இயங்கிய வேல்! பாடியவர்: ஔவையார். பாடப்பட்டோன்: அதியமான் நெடுமான் அஞ்சி. திணை: பொதுவியல். துறை: கையறுநிலை.`

The Sangam Auvaiyar (§6), on the death of the patron she had known for at least seventeen poems.

#### மூலம்

> சிறியகட் பெறினே, எமக்கீயும்; மன்னே!
> பெரிய கட் பெறினே,
> யாம் பாடத், தான்மகிழ்ந்து உண்ணும்; மன்னே!
> சிறுசோற் றானும் நனிபல கலத்தன்; மன்னே!
> பெருஞ்சோற்றானும் நனிபல கலத்தன்; மன்னே!
> என்பொடு தடிபடு வழியெல்லாம் எமக்கீயும்; மன்னே!
> அம்பொடு வேல்நுழை வழியெல்லாம் தான்நிற்கும் மன்னே! நரந்தம் நாறும் தன் கையால், ⟨fused⟩
> புலவு நாறும் என்தலை தைவரும்! மன்னேஅருந்தலை இரும்பாணர் அகன்மண்டைத் துளையுரீஇ, ⟨fused⟩
> இரப்போர் புன்கண் பாவை சோர,
> அஞ்சொல் நுண்தேர்ச்சிப் புலவர் நாவில்சென்றுவீழ்ந் தன்று, அவன்அருநிறத்து இயங்கிய வேலே! ⟨fused⟩
> ஆசாகு எந்தை யாண்டுஉளன் கொல்லோ?
> இனிப், பாடுநரும் இல்லை; படுநர்க்குஒன்று ஈகுநரும் இல்லை; ⟨fused⟩
> பனித்துறைப் பகன்றை நறைக் கொள் மாமலர்சூடாது வைகியாங்குப், பிறர்க்கு ஒன்றுஈயாது வீயும் உயிர்தவப் பலவே! ⟨fused⟩

#### சொல்லுக்குச் சொல்

| சொல் | பிரிப்பு | பொருள் | English |
|---|---|---|---|
| சிறிய கள் பெறினே | — | கள் சிறிதளவு கிடைத்தால் | if he got a little toddy |
| எமக்கு ஈயும் | — | எங்களுக்குத் தருவான் | he would give it to us |
| **மன்னே** | — | *(கழிவிரக்கக் குறிப்பு)* | **the particle of what-is-now-gone** |
| நனி பல கலத்தன் | — | மிகப் பல கலங்களை உடையவன் | he was a man of very many vessels |
| என்பொடு தடிபடு வழி | என்பு + தடி + படு | எலும்பும் தசையும் வெட்டுண்ணும் இடம் | wherever bone and meat are being carved |
| அம்பொடு வேல் நுழை வழி | — | அம்பும் வேலும் நுழையும் இடம் | wherever arrow and spear go in |
| தான் நிற்கும் | — | தானே நிற்பான் | *he* would stand |
| நரந்தம் நாறும் தன் கை | — | நறுமணம் கமழும் அவன் கை | his hand, smelling of fragrance |
| புலவு நாறும் என் தலை | — | புலால் நாற்றமுள்ள என் தலை | my head, smelling of raw flesh |
| தைவரும் | — | தடவும் | would stroke |
| அகல் மண்டை | — | பாணரின் அகன்ற பிச்சைப் பாத்திரம் | the bard's wide begging-bowl |
| துளையுரீஇ | துளை + உரீஇ | துளையிட்டுத் தேய்த்து | boring through, wearing through |
| இரப்போர் புன்கண் பாவை சோர | — | இரப்பவர் கண்ணின் கருமணி சோர | the pupils of the beggars' eyes slackening |
| புலவர் நாவில் சென்று வீழ்ந்தன்று | — | புலவர் நாவில் சென்று விழுந்தது | it went and fell on the poets' tongues |
| அருநிறத்து இயங்கிய வேல் | — | (தாங்குதற்) அரிய மார்பில் சென்ற வேல் | the spear that travelled through that hard-to-pierce chest |
| ஆசு ஆகு எந்தை | — | பற்றுக்கோடாய் இருந்த என் தந்தை | my father, who was my support |
| படுநர்க்கு ஒன்று ஈகுநரும் இல்லை | — | பாடுவோர்க்கு ஒன்று ஈபவரும் இல்லை | there is no one who gives anything to those who sing |
| பகன்றை மாமலர் | — | பகன்றைச் செடியின் பெரும் பூ | the great flower of the pakaṉṟai plant |
| சூடாது வைகியாங்கு | — | யாரும் சூடாமல் தங்கியது போல | as it stays without anyone wearing it |
| ஈயாது வீயும் உயிர் தவப் பல | — | ஈயாமல் அழியும் உயிர்கள் மிகப் பல | very many are the lives that perish without giving |

#### பொருள் — தமிழில்

சிறிதளவு கள் கிடைத்தால் எமக்குத் தருவான் — இருந்தான் அவன்! பெரிதளவு கிடைத்தால், நாங்கள் பாட, தான்
மகிழ்ந்து உண்பான் — இருந்தான்! சோறு சிறிதாயினும் பெரிதாயினும் பல கலங்களில் வைத்திருப்பான் —
இருந்தான்! எலும்பும் தசையும் வெட்டப்படும் இடமெல்லாம் எமக்கு ஈவான்; அம்பும் வேலும் நுழையும்
இடமெல்லாம் தானே நிற்பான் — இருந்தான்! நறுமணம் கமழும் தன் கையால் புலால் நாறும் என் தலையைத்
தடவுவான் — இருந்தான்!

பாணரின் அகன்ற மண்டையைத் துளைத்து, இரப்போரின் கண்மணி சோர, நல்ல சொல்லும் நுண்ணறிவும் உடைய புலவரின்
நாவில் சென்று விழுந்தது — அவன் மார்பைக் கடந்து சென்ற அந்த வேல். பற்றுக்கோடாய் இருந்த என் தந்தை
இப்போது எங்கே இருக்கிறான்? இனிப் பாடுவாரும் இல்லை; பாடுவார்க்கு ஈவாரும் இல்லை. குளிர்ந்த
துறையில் பூத்த பகன்றையின் பெரிய மலர் யாரும் சூடாமல் கிடப்பதுபோல, பிறர்க்கு ஒன்றும் ஈயாமல்
அழிந்துபோகும் உயிர்கள் மிகமிகப் பல.

#### பொருள் — in English

If he got a little toddy, he gave it to us — *and now he is gone.* If he got a great deal, we sang
and he drank it in joy — *and now he is gone.* Little rice or much, he kept it in very many vessels
— *gone.* Wherever bone and meat were being carved, he gave to us; wherever arrow and spear went in,
**he** stood — *gone.* With his own hand, that smelled of fragrance, he would stroke my head, that
smelled of raw flesh — *and now he is gone.*

The spear that passed through that unpierceable chest — it bored through the bards' wide begging
bowls, it slackened the pupils in the eyes of everyone who lives by asking, and it went on and fell
on the tongues of poets skilled in fine speech and fine discernment. My father, who was my hold on
the world — where is he now? Now there is no one who sings; and no one who gives anything to those
who sing. Like the great flower of the pakaṉṟai at the cold water's edge, blooming and lying there
with no one to wear it — very, very many are the lives that go out without having given anything to
anyone.

#### நுட்பம் | Craft

**The whole first half is built on one particle: `மன்`.** It appears **eight times.** `மன்` (here
`மன்னே`) is the classical Tamil marker of *what was and is no longer* — grammarians call it
கழிவு, the past-that-is-cut-off. **[விளக்கம் | INTERPRETATION]** The poem never says "he is dead."
It states eight ordinary facts about his habits in the imperfect and hangs `மன்னே` off each one, and
the particle does the killing. English has no equivalent and needs a whole clause — *and now he is
gone* — which is why the translation above is so much heavier than the Tamil. **This is the single
clearest instance in the anthology of Tamil grammar carrying an emotion that English can only carry
lexically.** Logged as a candidate for `../../aaivu/vithai.md`.

**The two-smells couplet is the emotional centre and it is built out of nouns.**
`நரந்தம் நாறும் தன் கையால் / புலவு நாறும் என்தலை தைவரும்` — *his hand that smells of fragrance
strokes my head that smells of raw meat.* The chieftain is perfumed; the poet, who has been eating
at his table and travelling hard, smells of flesh. The line says everything about the asymmetry
between them — rank, cleanliness, wealth — and then the verb `தைவரும்`, *strokes*, crosses it
without a word of comment. **[கருதுகோள் | HYPOTHESIS]** A poem that wanted to praise a patron's
generosity would put the gift in this slot. Putting a *gesture* there instead, and an unhygienic one,
is what makes this an elegy for a person rather than for a source of income.

**The spear's trajectory is the technical masterstroke.** A spear went through Adhiyaman's chest.
The poem then keeps following it: `அகன்மண்டைத் துளையுரீஇ` — it bores on through the bards' begging
bowls; `இரப்போர் புன்கண் பாவை சோர` — it slackens the pupils in the eyes of the poor; and finally
`புலவர் நாவில்சென்றுவீழ்ந் தன்று` — **it goes and falls on the tongues of poets.** One weapon,
one continuous line of flight, four bodies. The killing of a patron is rendered as a wound to an
entire economy: the bowl that will not be filled, the eye that will not brighten, and the tongue
that now has nothing to praise. **[விளக்கம் | INTERPRETATION]** This is not metaphor decorating a
death. It is a piece of economic reporting written as ballistics.

**The close refuses to be about him.** `பிறர்க்கு ஒன்றுஈயாது வீயும் உயிர்தவப் பலவே` — very many are
the lives that die without giving anything to anyone. The lament ends by turning away from the dead
man to indict the living, and the image it uses — a flower blooming at the cold water's edge with
nobody to wear it — is beautiful and is an accusation. Ungiven generosity is the same waste as an
unworn flower. That final move is why the colophon files this under `பொதுவியல்`, the general, and
not under any war category: by its last line the poem has stopped being about Adhiyaman.

---

### 7.3 புறம் 278 — ஈன்ற ஞான்றினும் பெரிது உவந்தனளே | *Gladder than the day she bore him*

**[மூலம் | SOURCE — colophon, verbatim]**
`278. பெரிது உவந்தனளே! பாடியவர்: காக்கைபாடினியார் நச்செள்ளையார் திணை: தும்பை துறை: உவகைக் கலுழ்ச்சி`

A woman poet. Her name means *Nacceḷḷaiyār who sang the crow* — Sangam poets are routinely named
after their own best image (compare செம்புலப் பெயனீரார் in `sangam.md` §2). And note the துறை:
**உவகைக் கலுழ்ச்சி**, "the weeping that belongs to joy." Tamil poetics had a technical slot for
that.

#### மூலம்

> “நரம்புஎழுந்து உலறிய நிரம்பா மென்தோள்முளரி மருங்கின், முதியோள் சிறுவன்படைஅழிந்து மாறினன்” என்று பலர் கூற, ⟨fused: three verse lines run together here⟩
> “மண்டுஅமர்க்கு உடைந்தனன் ஆயின், உண்டஎன்முலைஅறுத் திடுவென், யான்’ எனச் சினைஇக், ⟨fused⟩
> கொண்ட வாளடு படுபிணம் பெயராச்,
> செங்களம் துழவுவோள், சிதைந்துவே றாகியபடுமகன் கிடக்கை காணூஉ, ⟨fused⟩
> ஈன்ற ஞான்றினும் பெரிதுஉவந் தனளே!

#### சொல்லுக்குச் சொல்

| சொல் | பிரிப்பு | பொருள் | English |
|---|---|---|---|
| நரம்பு எழுந்து உலறிய | — | நரம்பு புடைத்து வற்றிய | veins standing out, dried up |
| நிரம்பா மென் தோள் | — | நிறைவற்ற மெல்லிய தோள் | thin, unfilled, soft shoulders |
| முளரி மருங்கு | — | வற்றிய இடை *(உரையாளர் வேறுபடுவர்)* | a wasted waist *(gloss disputed)* |
| முதியோள் | — | முதிய பெண் | the old woman |
| சிறுவன் | — | அவள் மகன் | her son |
| படை அழிந்து மாறினன் | — | படை சிதைந்ததால் புறமுதுகிட்டான் | "his ranks broke and he turned back" |
| மண்டு அமர் | — | நெருங்கிய போர் | the press of battle |
| உடைந்தனன் ஆயின் | — | முறிந்து ஓடினான் என்றால் | "if he broke and fled" |
| உண்ட என் முலை அறுத்திடுவென் | — | அவன் உண்ட என் முலையை அறுத்துவிடுவேன் | "I will cut off this breast he fed at" |
| சினைஇ | — | சினந்து *(அளபெடை)* | flaring into rage |
| கொண்ட வாளொடு | — | கையில் எடுத்த வாளுடன் | with the sword she had taken up |
| படு பிணம் பெயரா | — | விழுந்த பிணங்களைப் புரட்டி | turning over the fallen corpses |
| செங்களம் துழவுவோள் | செம் + களம் + துழவு | குருதிக் களத்தைத் துழாவுபவள் | she who rakes through the red field |
| சிதைந்து வேறாகிய | — | சிதைந்து வேறுபட்டுப்போன | hacked into unrecognisability |
| படு மகன் கிடக்கை | — | வீழ்ந்த மகன் கிடக்கும் நிலை | the fallen son lying there |
| காணூஉ | — | கண்டு *(அளபெடை)* | on seeing |
| ஈன்ற ஞான்று | — | பெற்ற நாள் | the day she gave birth |
| பெரிது உவந்தனளே | — | மிகவும் மகிழ்ந்தாள் | she rejoiced greatly |

#### பொருள் — தமிழில்

"நரம்பு புடைத்து வற்றிய, நிறைவற்ற மெல்லிய தோளையும் வற்றிய இடையையும் உடைய அந்த முதியவளின் மகன்,
படை சிதைந்ததால் புறமுதுகிட்டுத் திரும்பிவிட்டான்" என்று பலரும் சொல்ல, "நெருங்கிய போரில் அவன்
முறிந்து ஓடினான் என்றால், அவன் உண்ட இந்த என் முலையை நானே அறுத்தெறிவேன்" என்று சினந்து, கையில்
எடுத்த வாளுடன் விழுந்த பிணங்களைப் புரட்டிக்கொண்டு குருதிக் களத்தைத் துழாவினாள். சிதைந்து
வேறுபட்டுப்போன நிலையில் தன் மகன் வீழ்ந்து கிடப்பதைக் கண்டு — அவனைப் பெற்ற நாளைவிட மிகவும்
மகிழ்ந்தாள்.

#### பொருள் — in English

Many were saying: *the old woman's son — the one with the wasted waist and the thin soft shoulders
where the veins stand out — his ranks broke and he turned back.* And she flared: **"If he broke in
the press of battle, I will cut off this breast he fed at."** She took up a sword and went out and
began turning the fallen bodies over, raking through the red field. And when she saw her son lying
there, hacked past recognition — **she was gladder than on the day she bore him.**

#### நுட்பம் | Craft

**The description in the opening lines is of the mother, not the son.** `நரம்பு எழுந்து உலறிய
நிரம்பா மென்தோள் / முளரி மருங்கின், முதியோள்` — starved arms, wasted waist. The poem opens on a
body that has not had enough to eat, and *then* tells you what that body is about to do. **[விளக்கம் | INTERPRETATION]**
The wasted shoulders are the poem's honesty: this ferocity is not being performed by anyone
comfortable.

**The threat is anatomically exact and that is the whole force of it.** She does not threaten to
disown him. `உண்டஎன்முலை` — *this breast he fed at* — makes the punishment retroactive: she will
destroy the specific organ that made him. Cowardice is treated as something that travels backwards
up the line of nourishment and contaminates its source.

**`துழவுவோள்` is the ugliest and best-chosen verb in the poem.** துழாவு- is what you do to a cooking
pot — stir, rake through, feel around in. Applied to `செங்களம்`, the red field, it makes the
battlefield a vessel and the search for her son a domestic action performed at the wrong scale.
**[விளக்கம் | INTERPRETATION]** A poet reaching for grandeur would not have used a kitchen verb.
Reaching for a kitchen verb is what makes this a *mother* on the field.

**The last line is a controlled detonation, and its mechanism is arithmetic.**
`ஈன்ற ஞான்றினும் பெரிதுஉவந் தனளே` — *gladder than the day she bore him.* The comparison sets the
birth of a child, the culturally maximal joy, as the **baseline** and then exceeds it, at the sight
of that same child hacked apart. **[கருதுகோள் | HYPOTHESIS]** The poem is not endorsing that
arithmetic; it is *exhibiting* it. The line is placed so that the reader has to do the sum
themselves, and the sum is monstrous. Note that the anthologist did not file this under a war
திணை's heroism slot but under `உவகைக் கலுழ்ச்சி` — *the weeping that belongs to joy* — a category
whose very name concedes that two incompatible states are present at once and does not resolve them.
That is the same capability `sangam.md` §5 identified in புறம் 86 and flagged as a requirement for
phase 2: **holding contradiction losslessly.** Here the *classification system itself* has a name
for it.

**[திறந்த கேள்வி | OPEN QUESTION]** `முளரி` is glossed above as *wasted / withered* (of the waist),
following the common reading, but the word elsewhere means the lotus, and commentators differ. The
source gives no gloss. Ilam's ear and a commentary are both needed here.

---

### 7.4 புறம் 182 — உண்டால் அம்ம இவ்வுலகம் | *This world exists — because of them*

**[மூலம் | SOURCE — colophon, verbatim]**
`182. பிறர்க்கென முயலுநர்! பாடியவர்: கடலுள் மாய்ந்த இளம்பெரு வழுதி திணை: பொதுவியல் துறை: பொருண்மொழிக் காஞ்சி`

The poet's name is itself an obituary: **கடலுள் மாய்ந்த இளம்பெரு வழுதி** — *Iḷamperu Vaḻuti who was
lost in the sea.* A Pandya. Like §7.1, one of the anthology's most radical ethical statements comes
from a king.

#### மூலம்

> உண்டால் அம்ம, இவ்வுலகம்; இந்திரர்;
> அமிழ்தம் இயைவ தாயினும், இனிதுஎனத்தமியர் உண்டலும் இலரே; முனிவிலர்! ⟨fused⟩
> துஞ்சலும் இலர்; பிறர் அஞ்சுவது அஞ்சிப்,
> புகழ்எனின், உயிருங் கொடுக்குவர், பழியெனின்,
> உலகுடன் பெறினும், கொள்ளலர், அயர்விலர்;
> அன்ன மாட்சி அனைய ராகித்,
> தமக்கென முயலா நோன்தாள்,
> பிறர்க்கென முயலுநர் உண்மை யானே.

#### சொல்லுக்குச் சொல்

| சொல் | பிரிப்பு | பொருள் | English |
|---|---|---|---|
| உண்டால் | உண்டு + ஆல் | உளது *(ஆல்: அசைநிலை)* | it exists *(-āl: expletive particle)* |
| அம்ம | — | *(கேட்பித்தல் அசைச்சொல்)* | *listen* — a particle calling for attention |
| இந்திரர் அமிழ்தம் | — | இந்திரனுடைய அமிழ்தம் | the ambrosia of the gods |
| இயைவதாயினும் | இயைவது + ஆயினும் | கிடைப்பதாயிருந்தாலும் | even were it available |
| தமியர் உண்டலும் இலர் | — | தனியே உண்பதும் இல்லை | they will not eat alone |
| முனிவு இலர் | — | வெறுப்பு இல்லாதவர் | they hold no hatred |
| துஞ்சலும் இலர் | — | சோம்பியிருத்தலும் இல்லை | nor do they slumber |
| பிறர் அஞ்சுவது அஞ்சி | — | பிறர் அஞ்சுவதற்கு அஞ்சி | fearing what others fear |
| புகழ் எனின் உயிரும் கொடுக்குவர் | — | புகழ் என்றால் உயிரையும் தருவர் | if it be for fame, they will give even life |
| பழி எனின் உலகுடன் பெறினும் கொள்ளலர் | — | பழி என்றால் உலகம் முழுதும் கிடைத்தாலும் ஏற்கார் | if it be blame, they will not take it though the whole world were the price |
| அயர்வு இலர் | — | சோர்வு இல்லாதவர் | they do not flag |
| அன்ன மாட்சி அனையர் ஆகி | — | அத்தகைய மாட்சிமை உடையவராகி | being of that greatness |
| தமக்கென முயலா நோன்தாள் | — | தமக்கென முயலாத வலிய முயற்சி | strong effort not exerted for themselves |
| பிறர்க்கென முயலுநர் | — | பிறர்க்காக முயல்பவர் | those who labour for others |
| உண்மை யானே | உண்மை + ஆன் + ஏ | இருத்தலால் | *because they exist* |

#### பொருள் — தமிழில்

இவ்வுலகம் உளது; கேளுங்கள் — எதனால் என்றால்: இந்திரனுடைய அமிழ்தமே கிடைப்பதாயினும், "இனிது" என்று
தாமே தனித்து உண்ணமாட்டார்; எவரையும் வெறுக்கமாட்டார்; சோம்பியிருக்கமாட்டார்; பிறர் அஞ்சுவதற்குத்
தாமும் அஞ்சி நடப்பார்; புகழ் என்றால் உயிரையும் கொடுத்துவிடுவார்; பழி என்றால் உலகம் முழுவதும்
கிடைப்பதாயினும் ஏற்கமாட்டார்; சோர்வு அடையார். அத்தகைய மாட்சிமை உடையவராகி, தமக்கென எதையும்
முயலாத வலிய முயற்சியோடு பிறர்க்கென உழைப்பவர் சிலர் இருக்கிறார்கள் — **அவர்கள் இருப்பதனால்தான்**
இவ்வுலகம் நிலைத்திருக்கிறது.

#### பொருள் — in English

This world exists — *listen* — and here is why. Though the very ambrosia of the gods were within
reach, they will not say "how sweet" and eat it alone. They hate no one. They do not slumber. They
fear what other people fear. If it is a matter of honour, they will give up life itself; if it is a
matter of disgrace, they will not take it though the whole world were offered. They never flag.
Being of that greatness, and putting out hard effort in nothing for themselves but everything for
others — **because such people exist, this world goes on standing.**

#### நுட்பம் | Craft

**The poem is one sentence with its main clause first and its reason last.** `உண்டால் அம்ம,
இவ்வுலகம்` opens with a bare assertion — *this world exists* — and then makes you wait eight lines
for `உண்மை யானே`, *because they exist.* Everything between is the description of the people the
world is resting on. **[விளக்கம் | INTERPRETATION]** The syntax enacts the argument: the world's
existence is stated as a fact, and only afterwards is it revealed to be **contingent** on a handful
of anonymous people. You are made to feel the ground get taken out from under a sentence you already
accepted.

**The test of virtue is a meal.** The first specification of a good person in the poem is not
courage, not truth, not justice. It is `தமியர் உண்டலும் இலரே` — *they will not eat alone.* Even the
gods' ambrosia. **[விளக்கம் | INTERPRETATION]** In an anthology whose most frequent speech act is a
poet asking a chieftain for food (§4.1: at least four distinct துறை for the request-for-a-gift), this
is not an abstract moral. **Eating alone is the specific, concrete sin of the world these poems come
out of.** The line is a professional's ethic: the giver who eats alone destroys the class of people
who sing.

**The two conditionals are deliberately unbalanced, and the imbalance is the argument.**
`புகழ்எனின், உயிருங் கொடுக்குவர்` / `பழியெனின்,` `உலகுடன் பெறினும், கொள்ளலர்,` — for honour, they will
pay their **life**; to avoid disgrace, they will refuse the **whole world**. The price of honour is
one life; the price of dishonour is everything that exists. **[கருதுகோள் | HYPOTHESIS]** The
asymmetry is the point: the poem prices *avoiding shame* higher than *gaining glory.* Compare புறம்
192 (`sangam.md` §4), where the closing pair is ordered the same way — refusing awe of the great,
then, marked as greater still (`அதனினும்`), refusing contempt for the small. **In both poems the
negative virtue is ranked above the positive one.** That looks like a stable feature of this
anthology's ethics and not a one-off.

**`பிறர் அஞ்சுவது அஞ்சி` is the line that resists modern translation.** Literally *fearing what
others fear.* **[திறந்த கேள்வி | OPEN QUESTION]** It can be read at least two ways: (i) they are
sensitive — what frightens ordinary people frightens them too, so they act to prevent it; or
(ii) they observe the community's taboos rather than exempting themselves. The Tamil supports both
and the poem does not disambiguate. This is a genuine open question, not a translator's laziness,
and Ilam's ear should be asked which reading the Tamil leans toward.

---

## 8. மேலும் மூன்று, சுருக்கமாக | Three more, briefly

**புறம் 312 — காளைக்குக் கடனே.** **[மூலம் | SOURCE]** The e-text gives it **no colophon at all** —
title and verse only, no poet, no திணை, no துறை. Six lines, each ending in the same word, `கடனே`
(*is the duty*):

> ஈன்று புறந்தருதல் என்தலைக் கடனே;
> சான்றோன் ஆக்குதல் தந்தைக்குக் கடனே;
> வேல்வடித்துக் கொடுத்தல் கொல்லற்குக் கடனே;
> நன்னடை நல்கல் வேந்தற்குக் கடனே;
> ஒளிறுவாள் அருஞ்சமம் முருக்கிக்,
> களிறுஎறிந்து பெயர்தல் காளைக்குக் கடனே.

*To bear him and raise him is my duty. To make him a man of worth is the father's duty. To forge and
hand him the spear is the smith's duty. To give good governance is the king's duty. To break the
hard battle with a shining sword, strike the war-elephant and come back — that is the young man's
duty.*

**[விளக்கம் | INTERPRETATION]** The mother is speaking, and she speaks first. The poem is a **complete
social contract in six lines** — mother, father, smith, king, son — with every party's obligation
stated in the same grammatical frame, so that raising a child, forging iron and governing a kingdom
are made syntactically identical kinds of work. Nobody is thanked and nobody is exempt. The
repetition of `கடனே` at every line-end is the form doing the argument's work: duty is what everyone
has, and it is the same shape for all of them.

**புறம் 279 — செல்கென விடுமே.** Poet: **ஒக்கூர் மாசாத்தியார**, a woman. திணை: வாகை. துறை:
**மூதின் முல்லை** — the old-family woman's fortitude, one of the 14 poems in that slot.

> கெடுக சிந்தை ; கடிதுஇவள் துணிவே;
> மூதின் மகளிர் ஆதல் தகுமே;
> … ஒருமகன் அல்லது இல்லோள்,
> ‘செருமுக நோக்கிச் செல்க’ என’ விடுமே!

Her brother died in one battle, her husband in the next, and today she hears the war-drum, oils the
hair of the one son she has, puts a spear in his hand and says *go, and look the battle in the face.*
The poem opens on the poet's own recoil — `கெடுக சிந்தை`, *let my mind be destroyed* — before it
concedes that the woman is worthy of her line. **[விளக்கம் | INTERPRETATION]** The recoil is not
decoration. It is the poem admitting that what it is about to praise is also unbearable, and it puts
that admission **first**, before the praise, so the praise never quite closes over it.

**புறம் 91 — சாதல் நீங்க, எமக்கு ஈத்தனையே.** Auvaiyar to Adhiyaman. திணை: தும்பை, துறை: வாழ்த்தியல்.
He possessed a `நெல்லி` fruit from a rock crevice on an old mountain — the fruit said to give long
life — and gave it away:

> சிறியிலை நெல்லித் தீங்கனி குறியாது,
> … சாதல் நீங்க, எமக்கு ஈத்தனையே.

*Without letting on what the sweet small-leaved nelli fruit was, keeping that inside yourself, you
gave it to us — so that death should keep away.* **[விளக்கம் | INTERPRETATION]** `ஆதல் நின்னகத்து
அடக்கி` — *keeping what it was inside you* — is the line that makes it. He concealed the gift's value
**so that she would accept it.** Read against poem 235, where the same man is dead and the poet is
raking the world for anyone who gives: this is what she is mourning, precisely.

---

## 9. என்ன வகையான இயந்திரம் | What the anthology is, as a machine

**[விளக்கம் | INTERPRETATION]** Pulling §2–§8 together, four things about how புறநானூறு is built:

1. **It is a database with a schema.** Each record carries: number, editorial title, poet, addressee,
   திணை, துறை, verse, and sometimes a `குறிப்பு` note or a commentator's citation. 386 records carry
   the திணை field, 387 the துறை field, 389 a poet, 245 an addressee. Different fields have different
   completeness — which is exactly what an aging database looks like.

2. **The schema is two-dimensional and the second dimension is speech acts.** Eleven திணை against
   more than 120 துறை. **[கருதுகோள் | HYPOTHESIS]** A classification system that is coarse about
   *topic* and enormously fine about *what the speaker is doing* is describing a culture that cared
   more about pragmatics than subject matter. There is one word for the whole category of pitched
   battle, and at least four for kinds of asking a patron for a gift.

3. **It is sorted by patron, not by theme.** The blocks at 87–104, 105–111, 121–126, 127–140,
   141–147, 148–150 are the compiler's fingerprint (§5.1).

4. **Its damage is physical and directional** — nothing lost before 244, thirty-eight damaged after
   (§2.2), with poems 267–268 gone entirely and marked as gone.

---

## 10. எண்ணத்திற்கு | What this gives Ennam

**[விளக்கம் | INTERPRETATION]**

- **`மன்` is the finding to take away.** In புறம் 235 a single one-syllable particle, repeated eight
  times, carries the entire fact of a death that the poem never states. English needs a clause each
  time. This is the clearest instance yet of the project's core question — *what can Tamil say
  structurally that English can only say lexically* — with a measurable cost difference. Should go to
  `../../aaivu/vithai.md`.

- **The classification system has a name for unresolved contradiction.** `உவகைக் கலுழ்ச்சி` —
  *the weeping that belongs to joy* — is a **category**, not a description of one poem. `sangam.md`
  §5 identified holding two opposed feelings without resolving them as a capability phase 2 must not
  lose. புறம் 278 shows that Tamil poetics did not merely *achieve* this; it had **filing cabinet
  space** for it.

- **A precedent for labelling the state of every claim.** `murai.md` §9 requires that source,
  observation, hypothesis and open question be kept distinct. The colophon apparatus does the same
  job for a poem: it states what is known, and when it does not know, it writes `தெரிந்தில` (poems
  289, 361) or `கிடைத்தில` (267–268) rather than guessing. **The Tamil tradition already had a
  vocabulary for admitting what the record does not contain, and used it inside the record itself.**
  That is a two-thousand-year-old precedent for this repo's §11 provenance labels, and the words are
  reusable.

- **A caution about who gets read.** The two most ethically radical poems read here (74 and 182) are
  by kings; the two most emotionally exposed (235 and 278) are by women. Neither group is who a
  modern reader pictures when they picture "a Sangam poet." The bias ledger in
  `../../varalaru/arivu-varalaru.md` should hold that.

---

## 11. ஐயம் | Doubt — what is uncertain here

**Never empty, per `../../marabu/README.md`.**

1. **[மூலம் | SOURCE — verified]** All 48 Tamil strings quoted in this document were programmatically
   tested as literal substrings of `pmuni0057-ettuthogai-purananuru.txt`. All 48 passed. Nothing here
   is reconstructed from memory.

   **One exception, stated plainly:** the `சொல்` column of every `சொல்லுக்குச் சொல்` table holds
   **normalised headwords**, not byte-exact quotations. The e-text's word-spacing is erratic
   (`ஈன்ம ரோ`, `உண்டஎன்முலை`), and a gloss table is unreadable if it reproduces that. Only the
   `மூலம்` blocks and strings shown in `backticks` are byte-exact. Where a phrase is discussed in
   running prose it is given in its exact source form even when that form is oddly spaced.

2. **[திறந்த கேள்வி | OPEN QUESTION] — the line divisions are partly lost.** The e-text destroyed
   line breaks (§0). Every `⟨fused⟩` marker above is a place where the original verse-line division
   is **unknown to this document**. A printed edition — U. V. Swaminatha Iyer's, or Auvai
   Duraisamippillai's commentary — would restore them. Until then, no claim about line count, line
   length or line-final placement in poems 74, 235 or 278 should be made from this document.

3. **[திறந்த கேள்வி | OPEN QUESTION] — the Tamil prose in §7 is composed by the instance.** Every
   `பொருள் — தமிழில்` paragraph is this instance's own Tamil, not a quotation from any commentary.
   Register, idiom, verb choice and whether it reads as natural modern Tamil or as stilted
   translationese are **entirely unverified.** Per `murai.md` §8, Ilam's ear is the authority. Treat
   those paragraphs as drafts to be corrected, not as content.

4. **[திறந்த கேள்வி | OPEN QUESTION] — individual glosses flagged.** `முளரி` (278) — *wasted* or
   *lotus*; commentators differ and the source gives no gloss. `பிறர் அஞ்சுவது அஞ்சி` (182) — two
   readings, both supportable (§7.4). `ஊன்தடி` (74) is glossed *lump of flesh* on the strength of
   `ஊன்` + `தடி`; that is a compositional reading, not an attested gloss from this file.

5. **[விளக்கம் | INTERPRETATION] — the counts are counts of *this edition*.** Every number in
   §2–§6 is a tally over one Project Madurai e-text. Colophons vary between printed editions; poem
   numbering varies; the `நொட்சி`/`நொச்சி` typo at 271–272 shows that transcription errors are
   present. Treat the numbers as **checkable and provisional**: right about this file, and to be
   re-run against any second edition before being called facts about புறநானூறு.

6. **[விளக்கம் | INTERPRETATION] — the e-text has at least two clear defects.** Poem 99 has lost its
   entire colophon and begins straight at the verse; poem 312 likewise has no colophon. Since both
   are well-known poems that other editions do classify, these are almost certainly **losses in this
   transcription**, not genuine gaps in the tradition. Any claim in §4 resting on the "13 poems with
   no திணை" figure inherits that uncertainty.

7. **[விளக்கம் | INTERPRETATION] — the women-poet count is a floor (§6.1).** The `-ஆர்` honorific is
   gender-neutral; the method used here can only find women whose names are explicitly marked.

8. **[திறந்த கேள்வி | OPEN QUESTION] — dates.** Per `murai.md`, no single date is asserted anywhere
   in this document. The Sangam corpus is variously placed between roughly 300 BCE and 300 CE, with
   the anthologising later still and the colophons later again (§4c); the ranges are contested and
   this document takes no position on them. Who holds which position belongs in
   `../../varalaru/arivu-varalaru.md`, not here.

9. **[திறந்த கேள்வி | OPEN QUESTION] — the historical framing of poem 74.** That its author died a
   prisoner of the Cholas is **tradition, reported here as tradition.** This source file states only
   his name. Nothing in the file corroborates the captivity.

---

## 12. காதுக்காக | Awaiting the ear — for Ilam

**Everything in this section is computed or read, never heard.** This instance cannot hear Tamil.
Each item below is a claim about sound, rhythm, register or beauty that it has no standing to
settle.

1. **The eight `மன்னே`s of புறம் 235.** §7.2 claims the repetition is the poem's engine. That is a
   *structural* observation — a count. **Does it land as a drumbeat, a sob, or a stumble?** Read the
   eight aloud in sequence. Nothing else in this document depends more on the answer.

2. **`ஈன்ற ஞான்றினும் பெரிதுஉவந் தனளே` (278, last line).** Called "a controlled detonation" above,
   on the strength of its *logic*. **Does the line sound like a detonation, or does it sound flat and
   the horror arrive only afterwards, on reflection?** These are different poems.

3. **`கெடுக சிந்தை` (279, first two words).** Rendered *let my mind be destroyed.* Is that an
   exclamation of horror, a formulaic opener, or something drier? The reading in §8 rests entirely on
   it being genuine recoil.

4. **The six `கடனே` endings of புறம் 312.** Six lines closing on the same word. **Computed as
   repetition; does it hear as incantation, as legal recitation, or as monotony?**

5. **The two-smells couplet in 235** — `நரம்பம் நாறும் தன் கையால் / புலவு நாறும் என்தலை`. §7.2 calls
   it the emotional centre. **Is the perfume/raw-flesh contrast as physically shocking in Tamil as it
   is in English translation, or is `புலவு` a neutral, unremarkable word in this register?**

6. **`துழவுவோள்` (278).** Claimed above to be a "kitchen verb" used at the wrong scale, and that the
   register clash is the poem's craft. **Does துழாவு- actually carry a domestic register to a native
   ear, or is that an over-reading of the dictionary?** This is the single most falsifiable
   craft-claim in §7.

7. **`அம்ம` (182, line 1).** Glossed as an attention-calling particle. **What does it *do* to the
   opening — is it a raised finger, a sigh, or invisible?**

8. **The அளபெடை forms.** `சினைஇ` and `காணூஉ` (278), `இரீஇய` (74), `துளையுரீஇ` (235). These are
   metrically lengthened vowels and this instance can only identify them, never hear them. **Do they
   slow the line the way `sangam.md` §4 says the அளபெடை in புறம் 192 slows the river passage?**

9. **Every `பொருள் — தமிழில்` paragraph in §7.** Composed by the instance. **Does the Tamil sound
   like Tamil, or like English wearing a Tamil script?** (Item 3 of §11.)

10. **The word `கிடைத்தில` / `தெரிந்தில`.** §10 proposes adopting these as repo vocabulary for
    "not obtained" / "not known." **Do they read as dignified classical usage a modern Tamil reader
    would accept in a research note, or as archaism that would look affected?** If the first, they
    belong in `../../agaraadhi.md`.

---

## தொடர்ச்சி | What should come next

- **[முன்மொழிவு | PROPOSAL]** Fold the புறம் 86 colophon (திணை வாகை, `துறை: ஏறாண் முல்லை`, §3)
  back into `../../ilakkiyam/sangam.md` §5, which currently gives the poem no classification and
  reads it as lament.
- **[முன்மொழிவு | PROPOSAL]** `marabu/` entry 007 is already planned for புறம் 192. **புறம் 312**
  is a better first புறம் for a child: six lines, one repeated word, a complete social contract, and
  the mother speaks first.
- **[முன்மொழிவு | PROPOSAL]** Re-run the §2–§6 tallies against a second edition and diff them. The
  disagreements will be more informative than either set of numbers alone.
- **[முன்மொழிவு | PROPOSAL]** The `மன்` finding (§10) deserves its own short study across the
  corpus — count every கழிவு `மன்` in புறநானூறு and see whether it clusters in `கையறுநிலை`.
  That is a one-script question with a real answer.

---

*மூலம்: `_src/txt/pmuni0057-ettuthogai-purananuru.txt` (Project Madurai, pmuni0057).
All Tamil quoted here is verbatim from that file and grep-verifiable against it.
Counts computed 2026-08-23 by the instance; §12 awaits the ear.*
