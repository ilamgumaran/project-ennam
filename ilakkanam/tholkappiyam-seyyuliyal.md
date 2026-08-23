# தொல்காப்பியம் · செய்யுளியல் | What Tolkappiyam Actually Says About Tamil Metre

> **நூல்** தொல்காப்பியம், பொருளதிகாரம், எட்டாம் இயல் — **செய்யுளியல்** · **நூற்பா** 235
> **மூலம்** Project Madurai e-text `pmuni0100-tholkappiyam-moolam.txt`, lines **3379–3883**
> **காலம்** contested — see §0.2. This document takes no single date.
> Every Tamil line below is copied verbatim from that file. Line numbers are given so any
> claim here can be re-grepped.

---

## 0. இந்த ஆவணம் என்ன செய்கிறது | What this document is for

`marabu/paadal/003-kurunthogai-002-kongu-ther.md` §7 and §11 left a hypothesis open and marked it
**"the next thing to verify"**:

> **[கருதுகோள் | HYPOTHESIS]** That **எதுகை is a post-Sangam systematisation** — present but not
> governing in ஆசிரியப்பா, near-universal by the Kural.

செய்யுளியல் has now been read. **The claim is half wrong and half right, and the two halves must be
separated.** §7 below gives the நூற்பā and the verdict; §8 puts the second half at risk against
23,000 lines of actual verse; §12 writes the correction that entry 003 needs.

### 0.1 மூலம் மட்டுமே | A source problem, stated up front

**[மூலம் | SOURCE]** The two commentary files named in the brief —
`pmuni0500_01-tholkappiyam-porulathikaram-urai-1.txt` and `pmuni0500_02-…urai-2.txt` — **do not
contain செய்யுளியல்.** Both are நச்சினார்க்கினியர்'s உரை on **அகத்திணையியல் and புறத்திணையியல்
only**. Verified: `grep -c "மோனை"` and `grep -c "எதுகை"` return **0** in both files; the index at
the tail of `urai-2` ends at புறத்திணையியல்.

**Consequence, stated plainly:** everything below is read from the **bare நூற்பā**, with no
commentator between us and the text. That is a real limitation. இளம்பூரணர் and நச்சினார்க்கினியர்
disagree with each other on several of these sutras, and where I have had to choose a reading I say
so and label it **[விளக்கம்]**. Getting a செய்யுளியல் உரை into `_src/` is the single highest-value
acquisition for the next session (§13).

**[மூலம் | SOURCE]** One OCR fault found in the chapter: line 3461 reads
`குன்றலும் மிகுதலுsம் இல் என மொழிப.` — a stray Latin `s` inside `மிகுதலும்`. That is the only
Latin-character intrusion in all 505 lines; the e-text is otherwise clean for this chapter.

### 0.2 காலம் | Dating — not settled, and it matters here

The repo's house position (`varalaru/arivu-varalaru.md` §2) is a defensible range of **core ~2nd–1st
c. BCE, final redaction by ~5th c. CE**, with named scholars spread from ~700 BCE
(தெ.பொ. மீனாட்சிசுந்தரம், இலக்குவனார்) to the 3rd c. CE (ச. வையாபுரிப்பிள்ளை), and a live
multiple-author view putting composition across 3rd c. BCE – 5th c. CE. **[திறந்த கேள்வி]** Whether
செய்யுளியல் in particular is early or a late layer (இடைச்செருகல்) is exactly the kind of question
that spread leaves open — and it bears directly on §7. This document does **not** assume an answer.

---

## 1. உறுப்புகள் | The famous நூற்பா — thirty-four components of a செய்யுள்

செய்யுளியல் opens by naming everything a poem is made of. This is the list the whole chapter then
walks through, in order.

**[மூலம் | SOURCE]** `pmuni0100`, lines **3380–3394**, செய்யுளியல் நூற்பா **1**:

> மாத்திரை எழுத்து இயல் அசை வகை எனாஅ
> யாத்த சீரே அடி யாப்பு எனாஅ
> மரபே தூக்கே தொடை வகை எனாஅ
> நோக்கே பாவே அளவு இயல் எனாஅ
> திணையே கைகோள் கூற்று வகை எனாஅ
> கேட்போர் களனே கால வகை எனாஅ
> பயனே மெய்ப்பாடு எச்ச வகை எனாஅ
> முன்னம் பொருளே துறை வகை எனாஅ
> மாட்டே வண்ணமொடு யாப்பு இயல் வகையின்
> ஆறு தலை இட்ட அந் நால் ஐந்தும்
> அம்மை அழகு தொன்மை தோலே
> விருந்தே இயைபே புலனே இழைபு எனாஅப்
> பொருந்தக் கூறிய எட்டொடும் தொகைஇ
> நல் இசைப் புலவர் செய்யுள் உறுப்பு என
> வல்லிதின் கூறி வகுத்து உரைத்தனரே.

**எண்ணிக்கை | The arithmetic.** **[விளக்கம் | INTERPRETATION]** `நால் ஐந்து` = 4 × 5 = **20**;
`ஆறு தலை இட்ட` = with six placed at the head = **26**; `எட்டொடும் தொகைஇ` = combined with the eight
வனப்பு = **34**. The multiplicative reading of number-compounds is confirmed inside the same chapter
by நூற்பா 155 (lines **3682–3683**), where பரிபாடல் is given `நால் ஈர் ஐம்பது` = 4 × 2 × 50 =
**400** lines upper limit and `ஐ ஐந்து` = **25** lower.

**The twenty-six + eight, unpacked.** `இயல்` and `வகை` in the நூற்பா are கிளவி-fillers ("the kind
of…"), not items — நூற்பா 2 (line 3396) confirms this by re-using `எழுத்து இயல் வகை` as a single
phrase.

| # | உறுப்பு | What it governs | Where in the chapter |
|---|---|---|---|
| 1 | **மாத்திரை** | the unit of duration | referred upward (நூ. 2) |
| 2 | **எழுத்து** | the letter | referred upward (நூ. 2) |
| 3 | **அசை** | the metrical syllable — நேர்/நிரை | நூ. 3–9 |
| 4 | **சீர்** | the foot | நூ. 10–30, 40–41 |
| 5 | **அடி** | the line | நூ. 31–39, 43–71 |
| 6 | **யாப்பு** | binding matter into a finished whole | நூ. 74–76 |
| 7 | **மரபு** | inherited convention | நூ. 76–82 |
| 8 | **தூக்கு** | the weight/gait class | நூ. 83 |
| 9 | **தொடை** | the sound-tie — **மோனை, எதுகை, முரண், இயைபு…** | **நூ. 84–99** |
| 10 | **நோக்கு** | the angle of view onto all of the above | நூ. 100 |
| 11 | **பா** | the metre proper | நூ. 101–104 |
| 12 | **அளவு** | permitted length | நூ. 150–157 |
| 13–26 | திணை · கைகோள் · கூற்று · கேட்போர் · களன் · காலம் · பயன் · மெய்ப்பாடு · எச்சம் · முன்னம் · பொருள் · துறை · மாட்டு · **வண்ணம்** | the *content* side | நூ. 177–226 |
| 27–34 | **வனப்பு** — அம்மை · அழகு · தொன்மை · தோல் · விருந்து · இயைபு · புலன் · இழைபு | beauty-types | நூ. 227–234 |

**[விளக்கம் | INTERPRETATION] — the finding hiding in the list.** Items 1–12 are prosody. Items
13–26 are *who is speaking, to whom, where, when, about what, to what effect.* **Tolkappiyam does
not treat "the poem's form" and "the poem's situation" as different subjects.** கேட்போர் (the
audience) and களன் (the setting) are components of a செய்யுள் in exactly the sense that அசை and சீர்
are. That is the same move `varalaru/arivu-varalaru.md` §2 identifies in பொருளதிகாரம் as a whole —
here it is, inside the metre chapter.

---

## 2. கட்டுமானம் | The build: எழுத்து → அசை → சீர் → அடி → பா

### 2.1 அசை — the metrical syllable

**[மூலம் | SOURCE]** lines **3398–3400**, நூற்பா **3**:

> குறிலே நெடிலே குறில் இணை குறில் நெடில்
> ஒற்றொடு வருதலொடு மெய்ப் பட நாடி
> நேரும் நிரையும் என்றிசின் பெயரே.

Read it as a table. Two names, four shapes, each optionally closed by an ஒற்று:

| அசை | Shape | Example |
|---|---|---|
| **நேர்** | one குறில் (short vowel) | **தி** in ஆ-**தி** |
| **நேர்** | one நெடில் (long vowel) | **ஆ** in **ஆ**-தி |
| **நேர்** | either + ஒற்று | **கண்**, **வாழ்க்** |
| **நிரை** | குறில் + குறில் (`குறில் இணை`) | **அக**- in **அக**ர |
| **நிரை** | குறில் + நெடில் | **சிறை**- in அஞ்-**சிறை**த் |
| **நிரை** | either of those + ஒற்று | **எழுத்**, **சிறைத்** |

**[மூலம் | SOURCE]** lines **3401–3403**, நூற்பா **4** — the two extra அசை:

> இரு வகை உகரமொடு இயைந்தவை வரினே
> நேர்பும் நிரைபும் ஆகும் என்ப
> குறில் இணை உகரம் அல் வழியான.

When a நேர் or நிரை is joined to either kind of உகரம் (குற்றியலுகரம் / முற்றியலுகரம்), you get
**நேர்பு** and **நிரைபு**. **[திறந்த கேள்வி]** The third line — `குறில் இணை உகரம் அல் வழியான` — is
an exception clause, and *what it excepts* is genuinely contested: "except where the உகரம் follows a
குறில்-இணை" and "except in the case of the குறில்-இணை-உகரam" give different scansions of common words
(see §11.1 on **உலகு**). Without a உரை in `_src/` I cannot settle it and I will not pretend to.

**[மூலம் | SOURCE]** line **3404**, நூற்பா **5**:

> இயலசை முதல் இரண்டு ஏனவை உரியசை.

The first two (நேர், நிரை) are **இயலசை** — the ordinary ones. The others (நேர்பு, நிரைபு) are
**உரியசை** — the special ones. That two-way split is what drives the whole சீர் taxonomy next.

### 2.2 சீர் — the foot

**[மூலம் | SOURCE]** lines **3413–3414**, நூற்பா **11**:

> ஈர் அசை கொண்டும் மூ அசை புணர்த்தும்
> சீர் இயைந்து இற்றது சீர் எனப்படுமே.

**A சீர் is two or three அசை.** That is the whole definition.

**[மூலம் | SOURCE]** lines **3415–3416**, நூற்பா **12**:

> இயலசை மயக்கம் இயற்சீர் ஏனை
> உரியசை மயக்கம் ஆசிரிய உரிச்சீர்.

A mix of இயலசை = **இயற்சீர்**. A mix involving உரியசை = **ஆசிரிய உரிச்சீர்**. Two more named at
lines **3423–3426**, நூற்பā **18** and **19**:

> இயற்சீர் இறுதி முன் நேர் அவண் நிற்பின்
> உரிச்சீர் வெண்பா ஆகும் என்ப.

> வஞ்சிச் சீர் என வகை பெற்றனவே
> வெண் சீர் அல்லா மூ அசை என்ப.

So the சீர் inventory is **functional, four-way, and named after the பā it belongs to**:
**இயற்சீர் · ஆசிரிய உரிச்சீர் · வெண்(பா உரிச்)சீர் · வஞ்சிச்சீர்**.

> ### ⚠️ முதல் மறுப்பு | First negative result
> **[மூலம் | SOURCE]** **தேமா, புளிமா, கூவிளம், கருவிளம் do not occur anywhere in தொல்காப்பியம்.**
> `grep -n "தேமா\|புளிமா\|கூவிளம்\|கருவிளம்" pmuni0100-tholkappiyam-moolam.txt` returns **nothing**
> — not in செய்யுளியல், not in the other 26 இயல். The flower-and-fruit names every Tamil
> schoolchild learns for the சீர் are **later terminology** (யாப்பருங்கலம் / யாப்பருங்கலக்காரிகை
> tradition). Tolkappiyam names its feet by *which metre owns them*, not by mnemonic images.
> The same grep is negative for **நாள் · மலர் · காசு · பிறப்பு**, the four வெண்பா ஈற்றுச்சீர் names
> — so `marabu/paadal/001-kural-001-agara-mudhala.md` §7's "பிறப்பு pattern" claim, correctly
> flagged there as *verify*, is **licensed by the later tradition and not by Tolkappiyam**. That
> entry's §11 should say so.

### 2.3 அடி — the line

**[மூலம் | SOURCE]** lines **3444–3447**, நூற்பā **31–34**:

> நாற் சீர் கொண்டது அடி எனப்படுமே.
> அடி உள்ளனவே தளையொடு தொடையே.
> அடி இறந்து வருதல் இல் என மொழிப.
> அடியின் சிறப்பே பாட்டு எனப்படுமே.

Four sutras, each one load-bearing:

1. **அடி = four சீர்.** The default line.
2. **தளை and தொடை live *inside* the அடி.** ← remember this for §7 and §8. This single line
   determines that both the linkage rule and the sound-tie are, in Tolkappiyam's frame, **within-line
   phenomena**.
3. Nothing goes past the அடி boundary.
4. **A பாட்டு is the excellence of its அடி.**

**[மூலம் | SOURCE]** lines **3462–3463**, நூற்பா **42** — the counting rule, and a beautiful reason
for it:

> உயிர் இல் எழுத்தும் எண்ணப்படாஅ
> உயிர்த் திறம் இயக்கம் இன்மையான.

*Letters without a vowel are not counted, because they have no vowel-motion.* A bare மெய் (ஒற்று) is
not counted when you measure a line. **[விளக்கம்]** The stated reason is not "convention" but
**physics**: what has no உயிர் has no இயக்கம், no movement, therefore no duration to measure. The
metre is grounded in what can actually be sustained in a breath.

---

## 3. அடி வகை | Line types by length

Measured in எழுத்து, counted by the rule of நூற்பா 42 above.

**[மூலம் | SOURCE]** lines **3448–3457**, நூற்பā **35–39**:

> நால் எழுத்து ஆதி ஆக ஆறு எழுத்து
> ஏறிய நிலத்தே குறளடி என்ப.
> ஏழ் எழுத்து என்ப சிந்தடிக்கு அளவே
> ஈர் எழுத்து ஏற்றம் அவ் வழியான.
> பத்து எழுத்து என்ப நேரடிக்கு அளவே
> ஒத்த நால் எழுத்து ஏற்றலங்கடையே.
> மூ ஐந்து எழுத்தே நெடிலடிக்கு அளவே
> ஈர் எழுத்து மிகுதலும் இயல்பு என மொழிப.
> மூ ஆறு எழுத்தே கழிநெடிற்கு அளவே
> ஈர் எழுத்து மிகுதலும் இயல்பு என மொழிப.

**[விளக்கம் | INTERPRETATION]** Reading `ஆறு எழுத்து` / `ஏறிய நிலத்தே` (the sutra breaks across source lines 3448–3449) as *"rising to* six" rather than *"rising
by* six" is what makes the five bands **contiguous with no gap and no overlap** — which is strong
internal evidence that it is the right reading:

| அடி | எழுத்து | நூற்பா |
|---|---|---|
| **குறளடி** | 4 → 6 | 35 |
| **சிந்தடி** | 7 → 9 (7 + 2) | 36 |
| **நேரடி** | 10 → 14 (10 + 4) | 37 |
| **நெடிலடி** | 15 → 17 (3×5 + 2) | 38 |
| **கழிநெடிலடி** | 18 → 20 (3×6 + 2) | 39 |

**[மூலம் | SOURCE] — a naming point the brief asked about.** The brief lists the ten-letter line as
**அளவடி**. Tolkappiyam calls it **நேரடி** in the measuring நூற்பா (37, line 3452) — but it *does*
use **அளவடி** elsewhere in the same chapter, in the பā-assignment sutras: line **3482** (`குறளடி
முதலா அளவடி காறும்`, நூ. 54), line **3484** (`அளவும் சிந்தும் வெள்ளைக்கு உரிய`, நூ. 55) and line
**3486** (`அளவடி மிகுதி உளப்படத் தோன்றி`, நூ. 56). **Both terms are in the text**; they are used in
different registers — நேரடி when measuring, அளவடி when allocating to a பா.

**Which பா gets which அடி** — this is where the metres actually differ:

**[மூலம் | SOURCE]** line **3475**, நூ. **50**: `ஐ வகை அடியும் ஆசிரியக்கு உரிய.`
→ **ஆசிரியப்பா may use all five.** This is the licence behind the uneven Sangam line.

**[மூலம் | SOURCE]** lines **3484–3485**, நூ. **55**:
> அளவும் சிந்தும் வெள்ளைக்கு உரிய
> தளை வகை ஒன்றாத் தன்மையான.
→ **வெண்பா gets only two** — அளவடி and சிந்தடி — *because its தளை does not agree otherwise.*

**[மூலம் | SOURCE]** lines **3486–3487**, நூ. **56**: `அளவடி மிகுதி உளப்படத் தோன்றி / இரு நெடிலடியும்
கலியிற்கு உரிய.` → **கலி** takes அளவடி and up, including both long lines.

**[மூலம் | SOURCE]** line **3464**, நூ. **43**: `வஞ்சி அடியே இரு சீர்த்து ஆகும்.`
→ **வஞ்சி's அடி is two சீர்**, not four. It is the odd one out of the whole system.

**[விளக்கம்]** So the four பா are separated *first* by which line-lengths they may use, and only
after that by தளை. The permission table **is** the metre.

---

## 4. தளை | What links one சீர் to the next

**[மூலம் | SOURCE]** lines **3480–3481**, நூற்பா **53** — the only general definition in the
chapter:

> சீர் இயை மருங்கின் ஓர் அசை ஒப்பின்
> ஆசிரியத் தளை என்று அறியல் வேண்டும்.

*Where சீர் join, if one அசை matches, know it as ஆசிரியத்தளை.* **[விளக்கம்]** தளை is therefore a
rule about the **seam** — the relation between the last அசை of one foot and the first அசை of the
next. It is what stops a line from being merely a bag of feet.

**Named தளை in செய்யுளியல் — exactly three:**

| தளை | Where | Line |
|---|---|---|
| **ஆசிரியத் தளை** | நூ. 53, 61 | 3481, 3495 |
| **கலித் தளை** | நூ. 23, 24 | 3431, 3432 |
| **வெண்தளை** | நூ. 60 | 3493 |

> ### ⚠️ இரண்டாம் மறுப்பு | Second negative result
> **[மூலம் | SOURCE]** **வஞ்சித்தளை is not named.** Every occurrence of `வஞ்சி` in the chapter
> (lines 3425, 3428, 3434, 3442, 3459, 3464, 3483, 3505, 3527, 3558, 3565, 3571, 3851) attaches it
> to a சீர், an அடி, a தூக்கு, an ஓசை or a வண்ணம் — **never to a தளை.** The eight-fold தளை list of
> the later handbooks (நேரொன்று/நிரையொன்று ஆசிரியத்தளை, இயற்சீர்/வெண்சீர் வெண்டளை, கலித்தளை,
> ஒன்றிய/ஒன்றா வஞ்சித்தளை) is **not** Tolkappiyam's. Tolkappiyam has three names and a seam-rule.
> **[கருதுகோள் | HYPOTHESIS]** The later eight-fold list is a *derivation* from நூ. 53's seam
> principle crossed with the four சீர் types — testable against யாப்பருங்கலம் if it can be sourced.

**[மூலம் | SOURCE]** line **3479**, நூ. **52** — a sentence worth pinning up:

> தன் சீர் உள்வழித் தளை வகை வேண்டா.

*Where a metre's own foot is present, the தளை category is not needed.* **[விளக்கம்]** i.e. the
system has redundancy built in, and Tolkappiyam says so: if the feet are already the right kind, you
need not also invoke the seam rule.

---

## 5. பா | The four metres

**[மூலம் | SOURCE]** lines **3558–3559**, நூற்பா **101**:

> ஆசிரியம் வஞ்சி வெண்பா கலி என
> நால் இயற்று என்ப பா வகை விரியே.

Four, **when expanded** (`விரி`). And then, immediately, the compression:

**[மூலம் | SOURCE]** lines **3562–3566**, நூற்பā **103–104**:

> பா விரி மருங்கினைப் பண்புறத் தொகுப்பின்
> ஆசிரியப்பா வெண்பா என்று ஆங்கு
> ஆயிரு பாவினுள் அடங்கும் என்ப.
> ஆசிரிய நடைத்தே வஞ்சி ஏனை
> வெண்பா நடைத்தே கலி என மொழிப.

**Compressed, there are only two: ஆசிரியப்பா and வெண்பா.** வஞ்சி walks with ஆசிரியம்; கலி walks with
வெண்பா. **[விளக்கம்]** The word is `நடை` — *gait, walk*. The four-fold classification is a surface
expansion of a **two-fold underlying rhythm**. For a learner this is the most useful single fact in
the chapter: there are two ways a Tamil line can move, and everything else is a variation.

**[மூலம் | SOURCE]** lines **3528–3529**, நூற்பா **81** — and a fifth name that is refused:

> மருட்பா ஏனை இரு சார் அல்லது
> தான் இது என்னும் தனிநிலை இன்றே.

*மருட்பா has no standing of its own; it is of the other two kinds.* **[விளக்கம்] — third negative
result:** the later tradition (and நன்னூல்-era teaching) counts **five** பā with மருட்பா as an
independent member. **Tolkappiyam names it and explicitly denies it independence.** The five-fold
list is a promotion that happened after this text.

---

## 6. ஓசை | The gait — and how much of the "four ஓசை" is really here

The brief asked for "the four ஓசை types if present." **They are half present, and the half that is
missing is the interesting part.**

**[மூலம் | SOURCE]** lines **3524–3527**, நூற்பā **77–80**, in sequence:

> அகவல் என்பது ஆசிரியம்மே.
> அதாஅன்று என்ப வெண்பா யாப்பே.
> துள்ளல் ஓசை கலி என மொழிப.
> தூங்கல் ஓசை வஞ்சி ஆகும்.

Read the four together and the asymmetry jumps out:

| பா | Tolkappiyam's phrase | Uses the word ஓசை? |
|---|---|---|
| ஆசிரியம் | `அகவல் என்பது` — *"what is called அகவல்"* | **no** |
| வெண்பா | `அதாஅன்று` — ***"it is not that"*** | **no** |
| கலி | `துள்ளல் ஓசை` — the leaping sound | **yes** |
| வஞ்சி | `தூங்கல் ஓசை` — the swinging/hanging sound | **yes** |

> ### ⚠️ நான்காம் மறுப்பு | Fourth negative result
> **[மூலம் | SOURCE]** `grep -n "ஓசை" pmuni0100-tholkappiyam-moolam.txt` returns **exactly three
> lines in the whole of தொல்காப்பியம்**: 3526 (துள்ளல்), 3527 (தூங்கல்), and 3847
> (`ஒழுகு வண்ணம் ஓசையின் ஒழுகும்`, நூ. 218). **`செப்பல்` never occurs as a metre-name anywhere**
> (its three occurrences — lines 1675, 2571, 2903 — are the ordinary verb "to say"). So the famous
> tetrad **செப்பலோசை · அகவலோசை · துள்ளலோசை · தூங்கலோசை** is **not** in Tolkappiyam as a tetrad.
> Two of the four names are here with `ஓசை`; `அகவல்` is here without it; **`செப்பல்` is not here at
> all.** வெண்பā's gait is given **purely negatively** — `அதாஅன்று`, *it is not that.*

**[விளக்கம் | INTERPRETATION]** That negative definition is not laziness. It is the same
compression as நூ. 103–104: there is one primary gait (அகவல்/ஆசிரியம்), and வெண்பா is *the other
one.* The tidy four-name tetrad is a later regularisation which filled in `செப்பல்` for the slot
Tolkappiyam left as a negation. **[காதுக்காக]** Whether வெண்பā's gait really is best described as
"not-அகவல்" is a question for an ear, not for a grep.

---

## 7. ★ தொடை — the verdict on எதுகை ★

**This is what the document was written to settle.**

### 7.1 The நூற்பā, in full

**[மூலம் | SOURCE]** `pmuni0100`, lines **3532–3549**, செய்யுளியல் நூற்பā **84–96**:

> மோனை எதுகை முரணே இயைபு என
> நால் நெறி மரபின தொடை வகை என்ப. **(84)**
> அளபெடை தலைப்பெய ஐந்தும் ஆகும். **(85)**
> பொழிப்பும் ஒரூஉவும் செந்தொடை மரபும்
> அமைத்தனர் தெரியின் அவையுமார் உளவே. **(86)**
> நிரல் நிறுத்து அமைத்தலும் இரட்டை யாப்பும்
> மொழிந்தவற்று இயலான் முற்றும் என்ப. **(87)**
> அடிதொறும் தலை எழுத்து ஒப்பது மோனை. **(88)**
> அஃது ஒழித்து ஒன்றின் எதுகை ஆகும். **(89)**
> ஆயிரு தொடைக்கும் கிளையெழுத்து உரிய. **(90)**
> மொழியினும் பொருளினும் முரணுதல் முரணே. **(91)**
> இறுவாய் ஒன்றல் இயைபின் யாப்பே. **(92)**
> அளபு எழின் அவையே அளபெடைத் தொடையே. **(93)**
> ஒரு சீர் இடையிட்டு எதுகை ஆயின்
> பொழிப்பு என மொழிதல் புலவர் ஆறே. **(94)**
> இரு சீர் இடையிடின் ஒரூஉ என மொழிப. **(95)**
> சொல்லிய தொடையொடு வேறுபட்டு இயலின்
> சொல் இயற் புலவர் அது செந்தொடை என்ப. **(96)**

### 7.2 மொழிபெயர்ப்பு | Rendered

| நூ. | Term | What the text says |
|---|---|---|
| 84 | **மோனை · எதுகை · முரண் · இயைபு** | the four traditional தொடை |
| 85 | **அளபெடை** | placed at their head, they make five |
| 86 | **பொழிப்பு · ஒரூஉ · செந்தொடை** | if you look, these exist too |
| 87 | **நிரல்நிறை · இரட்டை** | and these complete it |
| 88 | **மோனை** | the **head letter** agreeing, `அடிதொறும்` |
| 89 | **எதுகை** | agreement **in the one other than that** — i.e. the second |
| 90 | — | for **both** of those two, the **கிளையெழுத்து** (kindred letter) is permitted |
| 91 | **முரண்** | opposing, **in word or in sense** |
| 92 | **இயைபு** | agreement of the **ending** |
| 93 | **அளபெடைத் தொடை** | when the vowel is stretched |
| 94 | **பொழிப்பு** | எதுகை with **one சீர** between |
| 95 | **ஒரூஉ** | with **two சீர்** between |
| 96 | **செந்தொடை** | **when it differs from every தொடை named** |

### 7.3 தீர்ப்பு | The verdict — the claim is half wrong

> **The repo's hypothesis said: "எதுகை is a post-Sangam systematisation — present but NOT governing
> in ஆசிரியப்பா, near-universal by the Kural."**

**PART A — "a post-Sangam systematisation": REFUTED.**
**[மூலம் | SOURCE]** எதுகை is **named** (நூ. 84), **defined** (நூ. 89), **licensed for kindred
letters** (நூ. 90), and **sub-classified by interval** (நூ. 94, 95) in தொல்காப்பியம் itself.
Whatever date one takes for செய்யுளியல் within the contested range (§0.2), this is the grammar of
the Sangam corpus or its immediate neighbourhood — **not something that arrived after it.** எதுகை
was systematised *early*. The word "post-Sangam" must come out of entry 003.

**PART B — "present but NOT governing in ஆசிரியப்பா": SUPPORTED, and by four independent
mechanisms in the text.**

**1. எதுகை is one item on a menu.** நூ. 84–87 build a list — four, then five, then eight — and
நூ. 86's phrasing is permissive to the point of casualness: `அமைத்தனர் தெரியின் அவையுமார் உளவே`,
*if you look into what they composed, those exist too.* This is a **descriptive inventory of ties
poets were observed using**, not a specification of what a poem must contain.

**2. செந்தொடை — the decisive one.** நூ. 96 provides, **by name and with authority**
(`சொல் இயற் புலவர்`), for a line that **differs from every தொடை just listed**. A verse with no tie
at all is not a defective verse; it is a **செந்தொடை** verse. ***A prosodic system that names the
absence of a rhyme as its own legitimate category is a system in which rhyme is not obligatory.***
This single sutra settles Part B.

**3. The asymmetry with தளை.** **[மூலம் | SOURCE]** தளை is assigned to specific பā, compulsorily and
repeatedly — `கலித்தளை` (நூ. 23, 24), `வெண்தளை` (நூ. 60), `ஆசிரியத் தளை` (நூ. 53, 61), and நூ. 55
derives வெண்பா's *permitted line lengths* **from** its தளை (`தளை வகை ஒன்றாத் தன்மையான`). Against
that: **no நூற்பா anywhere in செய்யுளியல் assigns a தொடை to a பா.** `எதுகை` occurs in the whole of
தொல்காப்பியம் at exactly four lines — **3532, 3540, 3545, 3833** — and **not one of them names
ஆசிரியப்பா, வெண்பா, கலி or வஞ்சி.** தளை is constitutive; **தொடை is ornamental**. In Tolkappiyam's system, *nothing about
whether a poem is a legal ஆசிரியப்பா depends on எதுகை.*

**4. மோனை is primary, எதுகை is derived from it.** **[விளக்கம் | INTERPRETATION]** நூ. 88 gives
மோனை a positive, self-standing definition (`தலை எழுத்து ஒப்பது`). நூ. 89 then defines எதுகை
**negatively, off மோனை**: `அஃது ஒழித்து ஒன்றின்` — *"in the one other than that."* எதுகை has no
independent definition in Tolkappiyam; it is "the *other* letter's version of மோனை." Word order and
grammatical dependence are evidence about which tie the system takes as basic. This is inference
from wording, not a statement of the text — but it points the same way as 1–3.

### 7.4 எஞ்சிய கேள்வி | And a fifth mechanism worth flagging

**[மூலம் | SOURCE]** நூ. **94–95** define பொழிப்பு and ஒரூஉ **for எதுகை specifically**
(`ஒரு சீர் இடையிட்டு எதுகை ஆயின்…`) and measure the interval **in சீர்** — which, with நூ. 32
(`அடி உள்ளனவே தளையொடு தொடையே`), means **Tolkappiyam's தொடை is a phenomenon inside one line, between
its feet** — not a rhyme *between* lines at all.

**[கருதுகோள் | HYPOTHESIS]** *The historical change is not that எதுகை appeared. It is that எதுகை
migrated — from an optional within-line tie between சீர் (Tolkappiyam) to a compulsory between-line
tie anchored on the first சீர் of each அடி (வெண்பா practice).* §8 tests this.

**[திறந்த கேள்வி]** நூ. **88** says `அடிதொறும்` — "in/at each அடி." Does that mean *across* அடி
(line 1's head letter matching line 2's) or *within* each அடி (foot to foot)? The bare text is
ambiguous, the commentators are not in `_src/`, and the two readings give completely different
prosodies. §8.3 answers it **from the corpus** rather than from authority.

---

## 8. அளவீடு | Putting Part B at risk — a corpus measurement

**[முன்மொழிவு → முடிவு | PROTOCOL AND RESULT]** §7 settles what the *grammar* says. It does not
settle what *poets did*. So the second half of the hypothesis — "not governing in ஆசிரியப்பா,
near-universal by the Kural" — was measured directly.

### 8.1 நெறிமுறை | Protocol, stated so it can be attacked

- **Corpora**, all from `_src/txt/`: திருக்குறள் `pmuni0001`, நாலடியார் `pmuni0016`, குறுந்தொகை
  `pmuni0110`, ஐங்குறுநூறு `pmuni0028`, நற்றிணை `pmuni0296`, பதிற்றுப்பத்து `pmuni0038`,
  கலித்தொகை `pmuni0221`, பரிபாடல் `pmuni0087`.
- **Letters** split into எழுத்து clusters (உயிர் / உயிர்மெய் / மெய் / ஆய்தம்); மெய் **counted** for
  tie-position indexing, **not counted** for length (per நூ. 42).
- **எதுகை test (strict)**: first எழுத்து of both words agree in **அளபு** (both குறில் or both
  நெடில்) **and** the second எழுத்து has the same consonant base. This is நூ. 89 plus the standard
  quantity requirement.
- **மோனை test**: head letters identical **or கிளையெழுத்து** (நூ. 90), with a conservative kindred
  set: க/ங, ச/ஞ, ட/ண, த/ந, ப/ம, ற/ன, ண/ன/ந, ல/ள/ழ, ர/ற.
- **Chance baseline**: the partner word is shuffled across the whole corpus, 100 trials, seed fixed.
  **The ratio observed ÷ chance is the finding**; the absolute rate is not.
- **Declared failure condition**: if ஆசிரியப்பா and வெண்பா show the *same* எதுகை ratio, Part B is
  dead.

**[எல்லை | LIMITS — read before believing any number]** These are **lower bounds**, for three
reasons: (i) the printed word ≠ the சீர் — Project Madurai's spacing only approximates foot
division; (ii) some Sangam e-text lines are merged (குறுந்தொகை 2 is printed as **four** lines where
the repo entry has five — see §11.2), which *destroys* real adjacencies and can only push rates
**down**; (iii) the kindred set is conservative. The *comparison* survives all three because the
identical algorithm runs on every corpus.

### 8.2 முடிவு | Result — எதுகை between consecutive அடி (first சீர் to first சீர்)

| நூல் | பா | எதுகை (strict) | chance | **ratio** |
|---|---|---|---|---|
| **திருக்குறள்** | குறள்வெண்பா | **56.8 %** (755/1329) | 5.9 % | **9.7 ×** |
| **கலித்தொகை** | கலிப்பா | **48.4 %** (1990/4110) | 5.7 % | **8.4 ×** |
| **நாலடியார்** | வெண்பா | **49.5 %** (402/812) | 6.3 % | **7.8 ×** |
| **பரிபாடல்** | mixed | 36.5 % (854/2337) | 5.8 % | 6.3 × |
| **ஐங்குறுநூறு** | ஆசிரியப்பா | 29.6 % (493/1668) | 6.2 % | **4.8 ×** |
| **குறுந்தொகை** | ஆசிரியப்பா | 24.4 % (304/1244) | 5.8 % | **4.2 ×** |
| **நற்றிணை** | ஆசிரியப்பா | 17.0 % (898/5292) | 6.2 % | **2.7 ×** |
| **பதிற்றுப்பத்து** | ஆசிரியப்பா | 14.0 % (311/2220) | 5.4 % | **2.6 ×** |

**[முடிவு | CONCLUSION — the narrowest claim the result supports]**

1. **எதுகை is real in ஆசிரியப்பா** — 2.6–4.8× chance in all four akaval corpora, never at chance.
   The entry-003 wording "**not systematically**" is right; a wording like "absent" would be wrong.
2. **எதுகை is not governing in ஆசிரியப்பா** — at 14–30 %, roughly **one line-junction in four to
   seven**. A constraint obeyed a quarter of the time is not a constraint.
3. **The வெண்பā group is 2–4× denser** and sits at 8–10× chance. The direction of the hypothesis is
   confirmed; the failure condition did not trigger.
4. **"Near-universal by the Kural" is NOT confirmed by this measurement** — 56.8 %, not ~95 %.
   **[விளக்கம்]** Inspecting misses shows why, and it is a real finding rather than a bug: in
   குறள் 1 the எதுகை is between the அடி (**அ**கர / **ப**கவன், second letter **க**), but in
   **குறள் 21** (`pmuni0001`, lines **59–60**) —

   > ஒழுக்கத்து நீத்தார் பெருமை விழுப்பத்து
   > வேண்டும் பனுவல் துணிவு.

   — it is **ஒ*ழு*க்கத்து / வி*ழு*ப்பத்து, inside line 1**, and line 2 does not participate. **Valluvar
   anchors எதுகை on the opening சீர் but is free about where its partner sits.** Measuring only
   அடி→அடி therefore undercounts him. Entry 001's "near-universal" should be softened to *"the
   dominant organising tie, though not always between the two அடி."*
5. **கலித்தொகை at 8.4× is the surprise** — கலி is grouped with வெண்பா by நூ. 104 (`வெண்பா நடைத்தே
   கலி`), and it behaves like வெண்பா here. **Tolkappiyam's two-fold compression predicted this
   result 2,000 years early.** [கருதுகோள்] worth a proper `sothanai-*`.

### 8.3 மோனை — the ambiguity in நூ. 88, settled by the corpus

The open question of §7.4: does `அடிதொறும்` mean across lines or within them?

| நூல் | மோனை **across** அடி | chance | ratio | மோனை **within** அடி (சீர்1↔சீர்3) | chance | ratio |
|---|---|---|---|---|---|---|
| திருக்குறள் | 11.3 % | 11.8 % | **1.0 ×** | 19.4 % | 11.9 % | **1.6 ×** |
| நாலடியார் | 11.8 % | 12.9 % | **0.9 ×** | 30.5 % | 12.9 % | **2.4 ×** |
| குறுந்தொகை | 14.1 % | 13.5 % | **1.0 ×** | 25.3 % | 14.0 % | **1.8 ×** |
| ஐங்குறுநூறு | 15.0 % | 14.6 % | **1.0 ×** | 25.4 % | 14.5 % | **1.8 ×** |
| நற்றிணை | 13.1 % | 14.6 % | **0.9 ×** | 20.4 % | 13.5 % | **1.5 ×** |
| பதிற்றுப்பத்து | 15.7 % | 15.5 % | **1.0 ×** | 28.5 % | 15.0 % | **1.9 ×** |
| கலித்தொகை | 12.8 % | 13.3 % | **1.0 ×** | 25.3 % | 12.8 % | **2.0 ×** |

**[முடிவு | CONCLUSION]** **Across அடி, மோனை is at chance in all seven corpora — 0.9–1.0×, without
exception.** Within the அடி it is above chance in all seven — 1.5–2.4×. **Tamil poets did not
alliterate line-to-line; they alliterated foot-to-foot inside a line.** So நூ. 88's `அடிதொறும்`
means ***within* each அடி**, and this reading is independently required by நூ. 32
(`அடி உள்ளனவே தளையொடு தொடையே`) and by the சீர்-counted intervals of நூ. 94–95.

**[விளக்கம்] Why this matters for the repo:** both existing entries marked மோனை **within a single
line** — `அகர … ஆதி` in குறள் 1 line 1, `காமம் … கண்டது` in குறுந்தொகை 2 line 2. **Those readings
are correct, and they are now corroborated by 23,000 lines of verse and by the நூற்பā.** The one
thing to fix is that entry 003 places `காமம்/கண்டது` at சீர் **1 and 3** — one foot apart — which
is Tolkappiyam's **பொழிப்பு** interval (நூ. 94, line 3545). Entry 003 should name it.

---

## 9. மறுப்புகள் தொகுப்பு | The negative results, collected

Things this document checked for and **did not find** in தொல்காப்பியம். Each is a `grep` anyone can
re-run against `pmuni0100-tholkappiyam-moolam.txt`.

| Not in the text | Grep | Where it actually comes from |
|---|---|---|
| **தேமா · புளிமா · கூவிளம் · கருவிளம்** | 0 hits | later யாப்பு handbooks |
| **நாள் · மலர் · காசு · பிறப்பு** (ஈற்றுச்சீர்) | 0 hits in செய்யுளியல் | later யாப்பு handbooks |
| **வஞ்சித்தளை** | 0 hits | later eight-fold தளை list |
| **செப்பல்** as an ஓசை-name | 0 hits (3 hits = the plain verb) | later four-ஓசை tetrad |
| **ஓசை** applied to ஆசிரியம் or வெண்பா | ஓசை occurs **3×** total, only for கலி, வஞ்சி, and நூ. 218 | later regularisation |
| **மருட்பா** as an independent 5th பா | present but **explicitly denied** (நூ. 81) | later promotion |
| **பொழிப்பு/ஒரூஉ** applied to **மோனை** | defined for **எதுகை** only (நூ. 94–95) | later extension |

**[விளக்கம் | INTERPRETATION]** The pattern is consistent: **Tolkappiyam is more austere, more
functional, and less tidy than the prosody taught today.** It names feet by which metre owns them,
not by fruit; it gives one seam-rule and three தளை names, not eight; it defines வெண்பா's gait as
*"not that"* rather than inventing a word. **The mnemonic beauty of school Tamil prosody is a later
achievement — a pedagogical layer over an engineering document.** That is worth knowing before
teaching either.

---

## 10. வண்ணம், வனப்பு | The twenty rhythms and the eight beauties

Briefly, because they are components 26 and 27–34 and are almost never taught.

**[மூலம் | SOURCE]** line **3816**, நூ. **204**: `வண்ணம்தாமே நால் ஐந்து என்ப.` — **twenty வண்ணம்**
(4 × 5), listed at lines **3818–3827** and then defined one per sutra. A sample, each a whole
poetics in one line:

- **[மூலம்]** line **3834**, நூ. **208**: `வல்லிசை வண்ணம் வல்லெழுத்து மிகுமே.` — the hard-sounding
  rhythm has excess வல்லெழுத்து.
- **[மூலம்]** line **3841**, நூ. **214**: `நெடியவும் குறியவும் நேர்ந்து உடன் வருமே.`
  (சித்திர வண்ணம்) — long and short arriving together.
- **[மூலம்]** lines **3843–3846**, நூ. **216–217**:
  > அகப்பாட்டு வண்ணம்
  > முடியாத் தன்மையின் முடிந்ததன் மேற்றே.
  > புறப்பாட்டு வண்ணம்
  > முடிந்தது போன்று முடியாதாகும்.

  *அகப்பாட்டு வண்ணம்: unfinished in manner, yet resting on what is finished. புறப்பாட்டு வண்ணம்:
  seeming finished, yet not finishing.* **[விளக்கம்]** These two define **closure** as a rhythmic
  property — a poem that sounds open but is complete, and a poem that sounds complete but is open.
  For a project about expressing interiority (`ilakkiyam/sangam.md` §1, seed வி-005) this is a
  two-line theory of how a poem hands the ending to its reader.
- **[மூலம்]** line 3847, நூ. **218**: `ஒழுகு வண்ணம் ஓசையின் ஒழுகும்.` — the flowing rhythm flows by
  its sound. **[காதுக்காக]** புறநானூறு 192's river lines (`ilakkiyam/sangam.md` §4) look like a
  candidate; only an ear can say.

**வனப்பு** — the eight beauties, நூ. **227–234**, lines **3858–3878**. Two of note:

- **[மூலம்]** lines **3868–3869**, நூ. **231**:
  > விருந்தேதானும்
  > புதுவது புனைந்த யாப்பின் மேற்றே.

  **விருந்து** is *the beauty of a composition made new*. **Tolkappiyam has a named category for
  novelty as a poetic virtue.**
- **[மூலம்]** lines **3859–3860**, நூ. **227**:
  > சில் மென் மொழியான் தாய பனுவலின்
  > அம்மைதானே அடி நிமிர்வு இன்றே.

  **அம்மை** is the beauty of few, soft words and lines that do not stretch. **Compression as a
  named aesthetic.**

**[கருதுகோள் | HYPOTHESIS]** வண்ணம் and வனப்பு together are a **vocabulary for describing how a
poem feels** that has no equivalent in the Greek/Latin/Sanskrit prosodies. If that holds, it belongs
in `aaivu/oppaayvu.md`. It is a claim about absence in three other traditions, which this session
cannot check — so it stays a hypothesis.

---

## 11. வேலைப்பாடு | Worked examples, scanned by Tolkappiyam's own rules

### 11.1 திருக்குறள் 1

**[மூலம் | SOURCE]** `pmuni0001-thirukkural.txt`, **lines 17–18**, quoted exactly:

> அகர முதல எழுத்தெல்லாம் ஆதி
> பகவன் முதற்றே உலகு.

**அசை-by-அசை** (நூ. 3–5, 11):

| அடி | சீர் | அசை | வகை |
|---|---|---|---|
| 1 | **அகர** | அக (நிரை) + ர (நேர்) | இயற்சீர் |
| 1 | **முதல** | முத (நிரை) + ல (நேர்) | இயற்சீர் |
| 1 | **எழுத்தெல்லாம்** | எழுத் (நிரை+ஒற்று) + தெல் (நேர்+ஒற்று) + லாம் (நேர்+ஒற்று) | 3 அசை — legal by நூ. 11 |
| 1 | **ஆதி** | ஆ (நேர்) + தி (நேர்) | இயற்சீர் |
| 2 | **பகவன்** | பக (நிரை) + வன் (நேர்+ஒற்று) | இயற்சீர் |
| 2 | **முதற்றே** | முதற் (நிரை+ஒற்று) + றே (நேர்) | இயற்சீர் |
| 2 | **உலகு** | **contested — see below** | — |

**4 சீர் + 3 சீர்.** அடி 1 is exactly நூ. 31's `நாற் சீர்`. Counting by நூ. 42 (மெய் not counted):
அடி 1 = 10 எழுத்து → **நேரடி/அளவடி** (நூ. 37); அடி 2 = 7 → **சிந்தடி** (நூ. 36). And நூ. 55
(`அளவும் சிந்தும் வெள்ளைக்கு உரிய`) permits **exactly those two** to வெண்பா. **The shape of the
Kural couplet is a direct consequence of நூற்பா 55.** That is the single most useful thing in this
document for a learner scanning his first poem.

**[திறந்த கேள்வி] உலகு.** Under நூ. 4, உல (நிரை) + a final உகரம் should give **நிரைபு** — which
matches entry 001's "பிறப்பு pattern" reading. But நூ. 4's own exception, `குறில் இணை உகரம் அல்
வழியான`, may exclude precisely this case, since உல *is* a `குறில் இணை`. Without a உரை I cannot
resolve it. **Entry 001 §11 should carry this as an open question, not as "(Verify)".**

**தொடை.** **[மூலம்-licensed]** **எதுகை**: **அ**கர / **ப**கவன் — first letters அ and ப both **குறில்**,
second letters both **க**. Strict எதுகை by நூ. 89, across the two அடி. **மோனை**: **அ**கர … **ஆ**தி,
சீர் 1 and 4 of அடி 1 — அ/ஆ are not identical, so this depends entirely on நூ. **90**
(`ஆயிரு தொடைக்கும் கிளையெழுத்து உரிய`). **Entry 001's "இனமோனை" claim is licensed by நூற்பா 90 —
it should cite it.**

### 11.2 குறுந்தொகை 2

**[மூலம் | SOURCE]** `pmuni0110-kurunthogai.txt`, **lines 38–41**, quoted exactly as printed:

> கொங்குதேர் வாழ்க்கை அஞ்சிறைத் தும்பி
> காமம் செப்பாது கண்டது மொழிமோ
> பயிலியது கெழீஇய நட்பின் மயிலியல்
> செறியெயிற் றரிவை கூந்தலின் நறியவும் உளவோ நீயறியும் பூவே.

**[எல்லை | LIMIT — a source discrepancy to record]** The e-text prints this poem as **four** lines;
`marabu/paadal/003` prints it as **five**, breaking after `கூந்தலின்`. The five-line division is
almost certainly right (it gives a **குறளடி** at line 4, exactly as entry 003 says), but **the local
source does not support it** and the discrepancy must be logged rather than smoothed. Anyone citing
line numbers for குறுந்தொகை from `pmuni0110` should know its அடி breaks are unreliable — which is
also limitation (ii) declared in §8.1.

**Scansion, line 2** (the line the poem turns on):

| சீர் | அசை | வகை |
|---|---|---|
| **காமம்** | கா (நேர்) + மம் (நேர்+ஒற்று) | இயற்சீர் |
| **செப்பாது** | செப் (நேர்+ஒற்று) + பாது (நேர்பு, நூ. 4) | உரிச்சீர் |
| **கண்டது** | கண் (நேர்+ஒற்று) + டது (நிரைபு, நூ. 4) | உரிச்சீர் |
| **மொழிமோ** | மொழி (நிரை) + மோ (நேர்) | இயற்சீர் |

Four சீர். The presence of **உரிச்சீர்** (feet containing நேர்பு/நிரைபு) is itself the marker: நூ. 12
calls this class **`ஆசிரிய உரிச்சீர்`** — the foot type named for ஆசிரியப்பா. **The metre announces
itself in the feet, before you count anything.**

**தொடை, line 2** — and here is entry 003's claim, now placed properly:

- **மோனை**: **கா**மம் (சீர் 1) … **க**ண்டது (சீர் 3). கா and க are the same consonant differing in
  vowel length → **கிளையெழுத்து**, licensed by நூ. **90**.
- **The interval is one சீர்** — நூ. **94**'s **பொழிப்பு** position. (நூ. 94 defines பொழிப்பு for
  எதுகை; extending the name to மோனை is later usage — say so when you use it.)
- **எதுகை across அடி**: கொங்குதேர் / காமம் — second letters **ங்** and **ம**, kindred (both
  மெல்லினம்); but first letters **கொ** (குறில்) and **கா** (நெடில்) fail the quantity match.
  **No strict எதுகை.** Entry 003's reading holds.

**[விளக்கம்]** So the poem does exactly what §8 found the corpus doing: **மோனை inside the line at
the பொழிப்பு interval; no governing எதுகை between lines.** Entry 003 described the mechanism
correctly and only mis-dated it.

---

## 12. திருத்தம் | The correction entry 003 needs

**[முன்மொழிவு | PROPOSAL]** Replace the hypothesis in
`marabu/paadal/003-kurunthogai-002-kongu-ther.md` §11 with the following, and soften §7's
"**எதுகை becomes a governing requirement later**" accordingly. Per `murai.md` §10 the arc must be
preserved, so this belongs in `aaivu/karuthu/` as well, not as a silent overwrite.

> **[முடிவு | CONCLUSION, from தொல்காப்பியம் செய்யுளியல்]**
> **எதுகை is *not* a post-Sangam systematisation.** It is named, defined, licensed for kindred
> letters and sub-classified by interval in தொல்காப்பியம் itself — நூற்பā **84, 89, 90, 94, 95**
> (`pmuni0100`, lines 3532–3547). What is post-Sangam is not the **systematisation** but the
> **obligation**.
>
> **[முடிவு]** **எதுகை is not governing in ஆசிரியப்பா, and Tolkappiyam is explicit about why.**
> தளை is assigned to particular பா and constrains them (நூ. 23, 53, 55, 60); **no நூற்பா assigns
> any தொடை to any பா.** And நூ. **96** gives a verse that matches *no* தொடை its own honourable name,
> **செந்தொடை**. Measured: எதுகை between consecutive அடி runs **14–30 %** in four ஆசிரியப்பா corpora
> (2.6–4.8× chance) against **48–57 %** in வெண்பா and கலி (7.8–9.7× chance).
>
> **[திருத்தம்]** "Near-universal by the Kural" **overstates** it as measured line-to-line (56.8 %).
> Valluvar anchors எதுகை on the **opening சீர்** of a couplet but places its partner freely —
> sometimes in the other அடி (குறள் 1), sometimes inside the first (குறள் 21).
>
> **[கருதுகோள் | HYPOTHESIS — the replacement, still at risk]** *The change from Sangam to
> கீழ்க்கணக்கு is not the birth of எதுகை but its **migration and promotion**: from an **optional
> within-line tie between சீர்** (Tolkappiyam's own frame, நூ. 32, 94, 95) to a **near-obligatory
> tie anchored on the first சீர் of the அடி** in வெண்பா. **Prediction:** within-line எதுகை at the
> பொழிப்பு interval should be **higher** in ஆசிரியப்பா than in வெண்பா, while அடி-anchored எதுகை is
> lower. First look supports this (குறுந்தொகை சீர்1↔சீர்3 எதுகை 16.9 % at 3.4× chance vs
> திருக்குறள் 5.6 % at 1.0×) but the சீர்-division problem of §8.1 makes it provisional. Needs a
> `sothanai-*` with proper foot segmentation.*
>
> **[முடிவு]** **மோனை's own definition is settled by the same work.** நூ. 88's `அடிதொறும்` means
> ***within* each அடி**: across அடி, மோனை sits **at chance (0.9–1.0×) in all seven corpora
> measured**; within the அடி it runs 1.5–2.4× chance in all seven. Entry 003's மோனை reading is
> correct and should now cite நூ. **88, 90** and name the interval **பொழிப்பு** (நூ. 94).

---

## 13. அடுத்து | What the next session should do

1. **[முன்மொழிவு]** Acquire a **செய்யுளியல் உரை** into `_src/txt/` — இளம்பூரணர் or
   பேராசிரியர் on பொருளதிகாரம் 3.8. Three specific questions are blocked on it: நூ. 4's exception
   clause (§2.1, §11.1), the arithmetic of நூ. 97 (§14), and whether நூ. 88's `அடிதொறும்` was read
   as within-line by the commentators as the corpus says it should be (§8.3).
2. **[முன்மொழிவு]** Write `aaivu/sothanai-008-ethukai-idamperyarchi.md` — a real experiment on the
   migration hypothesis, with proper சீர் segmentation rather than printed word division.
3. **[முன்மொழிவு]** Log to `aaivu/karuthu/` the full arc of this claim per `murai.md` §10:
   question → "post-Sangam systematisation" → செய்யுளியல் 84/89 as counterexample → the தளை/தொடை
   asymmetry and செந்தொடை as evidence → revision to "migration, not birth" → open question on
   within-line rates.
4. **[முன்மொழிவு]** `agaraadhi.md` entries: **அசை · நேர் · நிரை · நேர்பு · நிரைபு · சீர் · இயற்சீர் ·
   உரிச்சீர் · தளை · தொடை · செந்தொடை · பொழிப்பு · ஒரூஉ · வண்ணம் · வனப்பு · விருந்து · அம்மை**.
5. **[முன்மொழிவு]** `aaivu/ellai.md`: the source-fidelity limit found in §11.2 (அடி breaks lost in
   the குறுந்தொகை e-text) and the commentary gap in §0.1.

---

## 14. ஐயம் | Doubt

*Per `marabu/README.md`, never empty.*

- **[மூலம் | SOURCE]** Every Tamil line quoted is copied verbatim from the named file at the named
  line numbers. Nothing is reconstructed from memory.
- **[எல்லை | LIMIT]** **No commentary was available** for this chapter (§0.1). Every reading of an
  ambiguous நூற்பா here is mine and is labelled **[விளக்கம்]**. Where இளம்பூரணர் and
  நச்சினார்க்கினியர் disagree, I do not know it, because I could not read them.
- **[திறந்த கேள்வி]** **நூற்பா 97** (lines **3550–3553**) gives a total count of தொடை varieties:

  > ஐ ஈர் ஆயிரத்து ஆறு ஐஞ்ற்றொடு
  > தொண்டு தலை இட்ட பத்துக் குறை எழுநூற்று
  > ஒன்பஃது என்ப உணர்ந்திசினோரே.

  One arithmetic reading gives (5×2×1000) + (6×500) + (700−10) + 9 = **13,699**. I am **not
  confident** in it:
  `ஐஞ்ற்றொடு` looks like an e-text corruption of `ஐஞ்ஞூற்றொடு`, and `தொண்டு` (9) and `ஒன்பஃது` (9)
  appear to duplicate. **No number should be quoted from this document for நூ. 97** until a உரை
  confirms it.
- **[திறந்த கேள்வி]** நூ. **48** (lines **3469–3472**) gives the five அடி types expanding into
  `மெய் வகை அமைந்த பதினேழ் நிலத்தும்` / `எழுபது வகையின் வழு இல ஆகி` /
  `அறுநூற்று இருபத்தைந்து ஆகும்மே.` — seventeen grounds, seventy kinds, **625**. I have not worked
  out the derivation and do not assert it.
- **[திறந்த கேள்வி]** The அடி-length arithmetic in §3 depends on reading `ஆறு எழுத்து` / `ஏறிய நிலத்தே` (the sutra breaks across source lines 3448–3449) as
  *"rising to* six." The bands come out contiguous, which is good evidence — but it is evidence for
  a reading, not the reading itself.
- **[எல்லை]** §8's numbers are **lower bounds** for the three reasons declared in §8.1. Treat the
  **ratios** as the finding and the **absolute percentages** as approximate.
- **[திறந்த கேள்வி]** Whether செய்யுளியல் is contemporaneous with the rest of தொல்காப்பியம் or a
  later layer is unresolved (§0.2) and **materially affects §7's Part A.** If செய்யுளியல் turned out
  to be a 4th–5th c. CE addition, "எதுகை was systematised early" would weaken considerably. This
  document's Part B (எதுகை not governing) does **not** depend on the date; Part A does.
- **[கருதுகோள்]** The reading of நூ. 88–89 as *"மோனை is primary, எதுகை derived from it"* (§7.3
  mechanism 4) rests on word order and grammatical dependence. It is suggestive, not proven.

---

## காதுக்காக | Awaiting the ear

*`murai.md` §8 — Ilam's ear is the authority. The inorganic side built every claim below by
counting characters and cannot hear a single one of them.*

1. **The big one — நூற்பா 78.** வெண்பā's gait is defined only as `அதாஅன்று`, *"it is not that."*
   **Say a குறள் aloud, then say five lines of குறுந்தொகை aloud. Is the difference the kind of thing
   that would make a grammarian give up and write "not that"?** If yes, that negative definition is
   an honest report of an ear, not a gap in the text — and the whole reading in §6 turns on it.
2. **துள்ளல் / தூங்கல் (நூ. 79, 80).** Does கலித்தொகை *leap* and வஞ்சி *swing/hang*? These are the
   only two gaits Tolkappiyam names with `ஓசை`. If they land, that is evidence that the author
   named exactly what he could hear and refused to name what he couldn't.
3. **§8.3's central result.** Across-அடி மோனை measured **at chance** in all seven corpora. **Read
   any Sangam poem and listen at the line-beginnings. Is there really nothing there?** A "no" from
   your ear against 23,000 lines of counting is exactly the kind of disagreement `murai.md` §4 wants.
4. **குறுந்தொகை 2, line 2** — **கா**மம் … **க**ண்டது at the **பொழிப்பு** interval. Entry 003 says
   the sound welds what the sense splits. **Does one சீர' of separation actually make them a pair in
   the ear, or is the claim doing work the sound isn't?**
5. **உலகு** (§11.1). நிரைபு or நிரை + நேர்? **Is the final -கு of `முதற்றே உலகு` held, clipped, or
   almost swallowed?** A குற்றியலுகரம் is defined by being *shortened* — the ear is the instrument
   for this, not the grep.
6. **அம்மை and விருந்து** (நூ. 227, 231) — *few soft words, lines that do not stretch*; *newly
   made*. **Do those two named beauties describe anything you actually feel in a poem?** If they do,
   Tamil has had vocabulary for two aesthetic experiences that English still names clumsily.
7. **ஒழுகு வண்ணம்** (நூ. 218) — *it flows by its sound.* Candidate: புறநானூறு 192's river passage
   (`ilakkiyam/sangam.md` §4). **Does it flow?**

---

> **Provenance summary.** All மூலம் in this document: `_src/txt/pmuni0100-tholkappiyam-moolam.txt`
> (செய்யுளியல், lines 3379–3883; எழுத்ததிகாரம் line 88 for மாத்திரை),
> `_src/txt/pmuni0001-thirukkural.txt` (lines 17–18), `_src/txt/pmuni0110-kurunthogai.txt`
> (lines 38–41). §8's measurements were computed over `pmuni0001`, `pmuni0016`, `pmuni0028`,
> `pmuni0038`, `pmuni0087`, `pmuni0110`, `pmuni0221`, `pmuni0296`. The commentary files
> `pmuni0500_01` / `pmuni0500_02` were checked and **do not cover this chapter** (§0.1).
