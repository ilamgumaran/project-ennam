# நாலடியார் · அகப்பொருள் · புறப்பொருள் · நன்னூல் | The Thousand Years After Tolkappiyam

> **நான்கு நூல், நான்கு மூலம் | Four works, four source files** — every Tamil line below is copied
> verbatim from the named Project Madurai e-text, with the line number so any claim here can be
> re-grepped.
>
> | நூல் | மூலம் (`_src/txt/`) | வரி | அளவு |
> |---|---|---|---|
> | **நாலடியார்** | `pmuni0016-keezhkanakku-naladiyar.txt` | 1–1681 | 400 வெண்பா + கடவுள் வாழ்த்து |
> | **இறையனார் அகப்பொருள் (களவியல்)** | `pmuni0301-ilakkanam-iraiyanar-agapporul.txt` | 1–449 | 60 நூற்பா + a slice of the உரை |
> | **புறப்பொருள் வெண்பாமாலை** | `pmuni0300-ilakkanam-purapporul-venbamalai.txt` | 1–3207 | 19 சூத்திரம் + 361 வெண்பா |
> | **நன்னூல்** | `pmuni0147-ilakkanam-nannool.txt` | 1–1278 | 462 நூற்பா |
>
> Comparison against தொல்காப்பியம் uses `pmuni0100-tholkappiyam-moolam.txt` and the repo's already
> verified [`../../ilakkanam/tholkappiyam-thinai.md`](../ilakkanam/tholkappiyam-thinai.md).
>
> **Dates are contested throughout.** §8 states the ranges and names who holds what. No single date
> is asserted anywhere in this document.
>
> **Verifying the quotes:** every Tamil line here was machine-checked against its source file with
> Unicode **NFC normalisation applied to both sides**. That step is required, not optional —
> `pmuni0147` (நன்னூல்) stores 87 vowel signs in decomposed form, so a naive byte-level `grep` will
> report false failures on the நன்னூல் quotes and only on those. **§9.2 documents this and proposes
> a repo-wide fix.**

---

## 0. இந்த ஆவணம் என்ன செய்கிறது | What this document is for

The repo has read தொல்காப்பியம் closely — [`../../ilakkanam/`](../ilakkanam/) holds
எழுத்து, சொல், திணை, மெய்ப்பாடு and செய்யுள். The implicit story in those files is that Tamil
poetics was *codified once*, early, and then the literature happened.

**That story is wrong, and this document is the correction.** The codifying went on for a
thousand years after Tolkappiyam, in works that argued with it, reorganised it, replaced a third of
it, and — in one case — invented a divine origin story to authorise the replacement. Four of those
works are in `_src/`. This reads them.

### 0.1 சங்கிலி | The chain, in one view

**[விளக்கம் | INTERPRETATION]** The mechanism running through all four is a **split**. Tolkappiyam
was one book in three parts: எழுத்து (letters), சொல் (words), பொருள் (matter — which in Tamil
means *poetics*: திணை, துறை, மெய்ப்பாடு, யாப்பு). Over the following millennium that third part
detaches from grammar and becomes its own discipline, with its own textbooks — and grammar, freed
of it, becomes a classroom subject.

| | எழுத்து | சொல் | **பொருள்** |
|---|---|---|---|
| **தொல்காப்பியம்** | ✓ | ✓ | **✓ — 9 இயல், akam and puram together** |
| **இறையனார் அகப்பொருள்** | — | — | **அகம் only, 60 நூற்பா, standalone** |
| **புறப்பொருள் வெண்பாமாலை** | — | — | **புறம் only, 12 திணை, standalone + worked examples** |
| **நன்னூல்** | ✓ | ✓ | **✗ — dropped entirely** |

Read the table across and the thousand years is visible as one move: **பொருளதிகாரம் leaves the
grammar and becomes two books; the grammar that remains wins the classroom.** §7 argues this at
length. The Jain quatrains of நாலடியார் belong to the same period and the same milieu — §1–§3 —
and they matter here because they are what the poetics was being written *about*.

---

# I. நாலடியார் — "the other Kural"

## 1. அமைப்பு, மூலத்திலிருந்து | Structure, verified from the file

**[மூலம் | SOURCE]** The e-text's own front matter (line 24) states the authorship tradition:

> சமண முனிவர்களால் இயற்றப்பட்ட நானூறு தனிப்பாடல்களின் தொகுப்பாகக் கருதப்படுகிறது.

*It is held to be a compilation of four hundred separate verses composed by Jain ascetics.* Note the
grammar of that sentence: **தனிப்பாடல்கள்** — *separate* poems, and **தொகுப்பு** — a *compilation*.
The tradition itself says this is an anthology of many hands, not a book by one author. Everything
odd about நாலடியார் follows from that, and §3 is about the consequences.

**[மூலம் | SOURCE]** Counted from the file: **exactly 400 numbered verses, 1–400, no gaps and no
duplicates** (`grep -o "^[0-9]\+\. "` yields 400 distinct numbers covering 1…400), preceded by an
unnumbered **கடவுள் வாழ்த்து** at lines 33–36. **40 அதிகாரம்**, each of exactly ten verses.

| பால் | அதிகாரம் | பாடல் | வரி in file |
|---|---|---|---|
| **அறத்துப்பால்** | 1–13 | 1–130 | 37–570 |
| **பொருட்பால்** | 14–37 | 131–370 | 571–1556 |
| **காமத்துப்பால்** | 38–40 | 371–400 | 1557–1681 |

The three-பால் division and the chapter-of-ten unit are **exactly the Kural's**, and that is the
whole basis of the pairing tradition. But look at the third column and the resemblance breaks:

**[விளக்கம் | INTERPRETATION] The Kural gives காமத்துப்பால் a quarter of the book (25 அதிகாரம் of
133). நாலடியார் gives it three of forty — 7.5%.** The Jain anthology keeps the Kural's *frame* and
guts its *proportions*. Where the Kural devotes a fifth of its length to lovers talking, நாலடியார்
spends its length on impermanence, poverty, meanness, and the fear of consequence. This is not the
Kural with different words. It is a different book wearing the Kural's shape.

### 1.1 ஒரு பிழை, மூலத்தில் | An error in the e-text's own table of contents

**[மூலம் | SOURCE]** Lines 27–30 of the file give a contents summary that does not match the file:

> 1 அறத்துப்பால் (13 அதிகாரங்கள்) >130 பாடல்கள்
> 2. பொருட்பால் (24 அதிகாரங்கள்) > 240 பாடல்கள்
> 3. காமத்துப்பால் (24 அதிகாரங்கள்) 30 பாடல்கள்

13 + 24 + 24 = 61 chapters; the file contains 40. **காமத்துப்பால் has 3 chapters, not 24** — the
"24" is copied down from the line above. The verse counts (130 / 240 / 30 = 400) are right; the
chapter count on line 29 is wrong. Anyone quoting this header should quote it corrected.

### 1.2 The chapter numbering is inconsistent in the source

**[மூலம் | SOURCE]** The chapter headings carry a `பால்.அதிகாரம்` prefix. Three of the last four
disagree with each other:

| வரி | Heading as printed | Should be |
|---|---|---|
| 1515 | `2.37 பன்னெறி` | ✓ |
| 1557 | `3.38 பொது மகளிர்` | ✓ |
| 1598 | `2.39 கற்புடை மகளிர்` | **3.39** |
| 1639 | `3.40 காமநுதலியல்` | ✓ |

And one heading (line 695, `2.17 பெரியாரைப் பிழையாமை`) is printed with a leading space where the
others are not — enough to drop it out of a naive `grep "^[0-9]"`. Flagged so the next session's
scripts do not silently miss a chapter.

## 2. "ஆலும் வேலும்" — not found in source

The brief asked me to verify the saying **ஆலும் வேலும் பல்லுக்குறுதி; நாலும் இரண்டும்
சொல்லுக்குறுதி** — *banyan and neem twigs for the teeth; the Four[-line book] and the Two[-line
book] for speech.*

**[மூலம் | SOURCE — negative result]** **It does not appear in any of the four source files.**
`grep` for `ஆலும்`, `வேலும்`, `பல்லுக்கு`, `சொல்லுக்கு` across all four returns nothing relevant:
three unrelated hits in புறப்பொருள் வெண்பாமாலை (`வேலும்` in two war verses at lines 1064 and 1224;
`ஆலும்` = *dances* in `மாமயிலும் ஆலும் மலை`, line 2961) and zero in the other three.

**I therefore cannot quote it as attested.** It is a proverb about these books, circulating outside
them, and this document treats it as **[விளக்கம் | INTERPRETATION]** — a piece of received
pedagogy whose wording needs a citable printed source before the repo repeats it. It is worth
tracking down: the pairing it asserts (நாலடி + குறள் as the two texts that fix your Tamil) is the
single strongest statement of நாலடியார்'s status, and the repo should be able to cite it properly.

**[முன்மொழிவு | PROPOSAL]** Next session: find it in a citable பழமொழி collection or a printed
நாலடியார் edition's preface, and record which. Until then, quote it with "as the saying goes" and
no source claim.

## 3. நான்கு பாடல், நெருக்கமாக | Four verses, read closely

I have chosen the four with the least comfortable moral edge, because that is what நாலடியார் has
that the Kural does not. The Kural is a book of a governing intelligence speaking to people who can
still act. **நாலடியார் is a book of renunciants speaking to people who are going to lose
everything**, and it does not soften.

For each: the மூலம் exactly as the file prints it, a word table, a Tamil gloss, an English gloss,
and what the verse is actually doing.

---

### 3.1 நாலடியார் 46 — the woman, itemised
**அதிகாரம் 1.5 தூய்தன்மை** (purity) · **வரி 223–226**

> குடரும் கொழுவும் குருதியும் என்பும்
> தொடரும் நரம்பொடு தோலும் - இடையிடையே
> வைத்த தடியும் வழும்புமாம் மற்றிவற்றுள்
> எத்திறத்தாள் ஈர்ங்கோதை யாள்.

| சொல் | பிரிப்பு | பொருள் | English |
|---|---|---|---|
| குடர் | குடல் | குடல் | bowels, intestines |
| கொழு | — | கொழுப்பு | fat |
| குருதி | — | இரத்தம் | blood |
| என்பு | — | எலும்பு | bone |
| தொடரும் நரம்பு | தொடர்+நரம்பு | இணைக்கும் நரம்பு | the sinew that links them |
| இடையிடையே வைத்த தடி | — | இடையில் வைக்கப்பட்ட தசை | the meat packed in between |
| வழும்பு | — | வழுவழுப்பு / சளி | the slime *(gloss uncertain — §10)* |
| எத்திறத்தாள் | எத்+திறத்து+ஆள் | எந்த வகையில் இருப்பவள் | in which of these is she? |
| ஈர்ங்கோதையாள் | ஈர்ம்+கோதை+ஆள் | குளிர்ந்த மாலை அணிந்தவள் | she of the cool garland |

**தமிழில்:** குடல், கொழுப்பு, குருதி, எலும்பு; அவற்றை இணைக்கும் நரம்பு, மேலே தோல்; இடையிடையே
வைக்கப்பட்ட தசை, வழும்பு — இவைதான் உடல். இவற்றுள் எதில் இருக்கிறாள் அந்தக் "குளிர்மாலை அணிந்தவள்"?

**In English:** Bowels, fat, blood, bone; the sinew that ties them and the skin over them; the meat
packed in between, and the ooze. *Among these — which one is she, the woman of the cool garland?*

**நுட்பம் | What it does.** The last two words are the trap. **ஈர்ங்கோதையாள்** is not a neutral
word for a woman; it is a stock love-poetry kenning, the exact register a Sangam akam poet reaches
for. The verse builds an anatomy list in three lines and then, in the final foot, **quotes the love
poem it is refuting.** The catalogue is not there for disgust; it is there so that the poetic
epithet lands on a heap of tissue and has nowhere to attach.

**[விளக்கம் | INTERPRETATION]** This is the அசுபபாவனை / *kāya-anupreksā* meditation — the
contemplation of the body's impurity — which is standard Jain and Buddhist ascetic practice, here
executed as a piece of literary criticism. The Kural has no chapter that does this. Its
காமத்துப்பால் takes the beloved's body entirely at the love-poem's own valuation. **நாலடியார் puts
a chapter called "purity" in the middle of the அறத்துப்பால் and uses it to dismantle the register
that the Kural's third book runs on.** The two books are not saying the same thing in different
metres.

Its neighbours press the same point harder: verse 47 calls the body a `கும்பம்` (pot) with nine
oozing gates; verses 48–50 move to the cremation ground and the skulls there, `உயிர்போயார்
வெண்டலை` (line 239) — *the white skulls of those whose life has gone*.

---

### 3.2 நாலடியார் 123 — the crab
**அதிகாரம் 1.13 தீவினையச்சம்** (fear of evil deeds) · **வரி 539–542**

> 123. அக்கேபோல் அங்கை யொழிய விரலழுகித்
> துக்கத் தொழுநொய் எழுபவே - அக்கால்
> அலவனைக் காதலித்துக் கான்முரித்துத் தின்ற
> பழவினை வந்தடைந்தக் கால்.

*(**[மூலம் | SOURCE]** The file reads `தொழுநொய்` with short ஒ at line 540. Standard editions read
`தொழுநோய்`. Treated here as an e-text fault — see §9.)*

| சொல் | பொருள் | English |
|---|---|---|
| அக்கு | சங்கு மணி | shell-bead |
| அங்கை | உள்ளங்கை | the palm |
| ஒழிய | எஞ்சி நிற்க | being left standing |
| விரல் அழுகி | — | the fingers rotting |
| துக்கத் தொழுநோய் | துன்பம் தரும் தொழுநோய் | the grievous wasting disease |
| அலவன் | நண்டு | crab |
| கால் முரித்து | — | having snapped its legs |
| பழவினை | — | the old deed |

**தமிழில்:** உள்ளங்கை மட்டும் சங்கு மணி போல எஞ்சி நிற்க, விரல்கள் அழுகி, துன்பம் தரும் தொழுநோய்
வந்து சேரும் — முன்பு ஒரு நண்டை விரும்பி, அதன் கால்களை முறித்துத் தின்ற அந்தப் பழவினை வந்து
சேரும்போது.

**In English:** The palm left bare like a shell-bead, the fingers rotting off — men rise up with the
grievous wasting disease when the old deed comes home: that once, craving a crab, they snapped its
legs off and ate it.

**நுட்பம் | What it does.** **This is the hardest verse in the book and the repo should say so
plainly rather than admire it.** Its moral premise is that visible bodily affliction is legible
punishment for a specific past act — and its chosen act is *eating a crab*. That is
அஹிம்சை / ahiṃsā reasoning taken to its edge: the animal's broken limbs return as your broken
limbs, part for part.

**[விளக்கம் | INTERPRETATION]** Three things are true at once and should be held together:

1. **The craft is exact.** The image is built on limb-for-limb correspondence — *its* legs snapped,
   *your* fingers gone — and the simile `அக்கேபோல்` (like a shell-bead: smooth, round, jointless)
   describes a hand with the digits gone with a precision that is not decorative.
2. **The doctrine is Jain and is doing real work.** It is not gratuitous cruelty; it is the
   strongest available argument against killing for food, aimed at a listener who eats meat.
3. **The claim it makes about disabled people is false and was cruel then as now.** A repo that
   quotes this verse for its craft and does not name that has misread the covenant's
   "நேர்மை > உதவி".

The Kural's corresponding chapter, புலால் மறுத்தல் (அதிகாரம் 26), argues from compassion and from
the eater's own conscience. **நாலடியார் argues from terror.** That difference — persuasion versus
threat — is the single clearest register-gap between the two books, and it is why the pairing
tradition treats them as complements rather than as duplicates.

---

### 3.3 நாலடியார் 281 — below a corpse
**அதிகாரம் 2.29 இன்மை** (destitution) · **வரி 1188–1191**

> 281. அத்திட்ட கூறை அரைச்சுற்ற வாழினும்
> பத்தெட் டுடைமை பலருள்ளும் பாடெய்தும்
> ஒத்த குடிப்பிறந்தக் கண்ணுமொன் றில்லாதார்
> செத்த பிணத்தின் கடை.

| சொல் | பொருள் | English |
|---|---|---|
| அத்திட்ட கூறை | ஒட்டுப்போட்ட ஆடை | a patched cloth *(gloss uncertain — §10)* |
| அரைச் சுற்ற | இடையில் சுற்றிக்கொண்டு | wound round the waist |
| பத்தெட்டு உடைமை | சிறிதளவு உடைமை | owning "ten or eight" — i.e. a little |
| பாடு எய்தும் | மதிப்பு அடையும் | gets standing |
| ஒத்த குடிப் பிறந்தக்கண்ணும் | சமமான குடியில் பிறந்திருந்தாலும் | though born in the same good family |
| செத்த பிணத்தின் கடை | பிணத்திற்கும் கீழானவர் | are lower than a dead body |

**தமிழில்:** ஒட்டுப்போட்ட துணியை இடையில் சுற்றிக்கொண்டு வாழ்ந்தாலும், பத்தோ எட்டோ உடைமை
உள்ளவன் பலருக்கு நடுவே ஒரு மதிப்பைப் பெறுவான். ஆனால் அதே நல்ல குடியில் பிறந்தும் ஒன்றும்
இல்லாதவர்கள் — செத்த பிணத்திற்கும் கீழ்.

**In English:** Even living with a patched rag wound round his waist, a man who owns eight or ten
things gets some standing among people. Those born into the same good family who own nothing at all
rank below a dead body.

**நுட்பம் | What it does.** **This verse is not moralising. It is reporting.** It makes no
recommendation, offers no consolation, and does not tell the poor man to be virtuous. It states an
observed fact about how people are treated, and rates the destitute below a corpse — because a
corpse at least gets rites, and he gets nothing.

**[விளக்கம் | INTERPRETATION]** And notice the sting placed in `ஒத்த குடிப் பிறந்தக்கண்ணும்` —
*even born into the same family*. The verse's real target is the belief that **birth is a floor**.
It says: it is not. Property is the floor. Take the property away and the birth is worth nothing —
in a book that has a whole chapter (2.15 குடிப்பிறப்பு) praising good birth, thirteen chapters
earlier. §3.5 takes up that contradiction, which is a feature of the anthology and not a fault of
it.

The chapter around it holds the same temperature: `இன்மை தழுவப்பட்டார்க்கு` — *for those embraced
by destitution* — birth, manhood and learning all `மாயும்`, are effaced (verse 285, lines
1204–1207); `இலாஅஅர்க் கில்லை தமர்.` — *the poor have no kin* (verse 283, line 1199); when you had
something they gathered `காகம்போல்`, like crows, and when you had nothing not one person asked
whether you were well (verse 284).

---

### 3.4 நாலடியார் 302 — starve, then
**அதிகாரம் 2.31 இரவச்சம்** (dread of begging) · **வரி 1274–1277**

> 302. இழித்தக்க செய்தொருவன் ஆர உணலின்
> பழித்தக்க செய்யான் பசித்தல் தவறோ?
> விழித்திமைக்கு மாத்திரை யன்றோ ஒருவன்
> அழித்துப் பிறக்கும் பிறப்பு.

| சொல் | பொருள் | English |
|---|---|---|
| இழித்தக்க செய்து | இழிவான செயலைச் செய்து | doing what earns contempt |
| ஆர உணல் | வயிறார உண்ணுதல் | eating one's fill |
| பழித்தக்க செய்யான் | பழிக்கத்தக்கதைச் செய்யாதவன் | he who does nothing blameworthy |
| பசித்தல் தவறோ | பசியோடு இருப்பது குற்றமா | is going hungry a fault? |
| விழித்து இமைக்கும் மாத்திரை | கண் திறந்து மூடும் அளவு | the span of an eye opening and closing |
| அழித்துப் பிறக்கும் பிறப்பு | — | the birth one uses up and is born into *(gloss uncertain — §10)* |

**தமிழில்:** இழிவான ஒன்றைச் செய்து ஒருவன் வயிறார உண்பதை விட, பழிக்கத்தக்கதைச் செய்யாமல்
பசியோடு இருப்பது குற்றமா? ஒருவன் ஒரு பிறப்பைக் கழித்து அடுத்ததில் பிறப்பது — கண் விழித்து
இமைக்கும் அளவுதானே?

**In English:** Rather than a man eating his fill by doing something contemptible — is it a fault
for him to go hungry and do nothing blameworthy? The birth a man wears through and is born into
again is only the span of an eye opening and closing.

**நுட்பம் | What it does.** The verse asks its question in two lines and then, in the last two, does
something the Kural almost never does: **it refuses to make the virtuous choice comfortable.** It
does not say "the hungry honest man is happy," or "he will be rewarded," or even "hunger is
bearable." It says: *a whole lifetime is one blink, so it does not much matter what happens inside
it.* The consolation offered is the smallness of the life.

**[விளக்கம் | INTERPRETATION]** Set against the whole chapter this is stronger still. இரவச்சம is
the fear of *asking* — and நாலடியார் has already spent 2.29 (§3.3) establishing that destitution
strips a man of everything. So the book's position, assembled across two chapters, is: *poverty will
take your standing, your kin, your learning and your name; and you must still not beg; and the
reason you can bear it is that none of it lasts long enough to count.* That is a hard, coherent
ethic, and it is not the Kural's. Kural 1053 and its chapter on இரவு allow a dignified asking of
the right person. **நாலடியார் closes even that door and offers cosmology instead of comfort.**

---

## 3.5 நாலடியார் contradicts itself, and that is the finding

**[மூலம் | SOURCE]** Two verses, seventeen chapters and ten pages apart, on the same subject:

- **275** (2.28 ஈயாமை, lines 1163–1166): `மறுமை யறியாதா ராக்கத்தின் சான்றோர் / கழிநல் குரவே தலை`
  — *the utter destitution of the worthy is superior to the wealth of those who do not know the
  next world.*
- **285** (2.29 இன்மை, lines 1204–1207): `பிறந்த குலமாயும் பேராண்மை மாயும் / சிறந்ததங் கல்வியும்
  மாயும்` … `இன்மை தழுவப்பட்டார்க்கு` — *birth is effaced, great manhood is effaced, even excellent
  learning is effaced, for those whom destitution has embraced.*

One verse says poverty is the higher state. The next chapter says poverty erases everything a person
is. **They are in adjacent chapters and they do not agree.**

**[விளக்கம் | INTERPRETATION] This is the structural difference between நாலடியார் and the Kural,
and it is worth more than any single verse.** The Kural is one mind; its 1,330 couplets can be held
to a standard of consistency, and the whole உரை tradition (see
[`../../ilakkiyam/thirukkural-urai.md`](../ilakkiyam/thirukkural-urai.md)) exists partly to
enforce it — commentators work hard to reconcile apparently conflicting couplets because a single
author is presumed. **நாலடியார் is `தனிப்பாடல்களின் தொகுப்பு` by its own front matter, and a
compilation owes no one consistency.** The contradiction is not a flaw the editor missed. It is the
form: a room of ascetics, each with a quatrain, arranged by topic.

**[கருதுகோள் | HYPOTHESIS — falsifiable]** If this is right, contradictions in நாலடியார் should
cluster *across* chapters (different hands assigned to different topics) and be rare *within* a
chapter of ten. **Prediction:** a systematic pass tagging each of the 400 verses with its stance on
wealth/poverty/birth/learning would show within-chapter agreement markedly higher than
between-chapter agreement on the same topic. **What would refute it:** finding flat contradictions
between verse 3 and verse 7 of the same அதிகாரம். This is a measurable claim on a 400-verse corpus
already in `_src/` and is proposed as work (§12).

---

# II. இறையனார் அகப்பொருள் — a grammar with a god for an author

## 4. அறுபது நூற்பா | The sixty sutras

**[மூலம் | SOURCE]** The file's own description (line 23):

> 1. களவு (33), 2. கற்பு (27) ஆக 60 சூத்திரங்கள்

Verified by the numbering in the text: `1.1`–`1.33` are numbered 1–33 (lines 28–166) and
`2.1`–`2.27` are numbered 34–60 (lines 168–237). **Sixty நூற்பா, in two parts: 33 on களவு (love
before marriage, conducted in secret) and 27 on கற்பு (love within marriage).**

That is the whole book. **It has no எழுத்து, no சொல், no யாப்பு, no புறம்.** It is
பொருளதிகாரம் with everything except akam cut away, and akam itself cut down to the
களவு/கற்பு axis. Where Tolkappiyam's அகத்திணையியல் spends its length on the seven திணை and the
landscape code, **இறையனார் spends its length on procedure**: who may speak to whom, in what order,
at what hour, and how long a man may take before he marries her.

### 4.1 What the sixty actually legislate

Six நூற்பா, chosen because each one does something Tolkappiyam does not.

**(i) The opening definition — and a visible Sanskritisation** [மூலம் — lines 29–31, நூ. 1]

> அன்பின் ஐந்திணைக் களவெனப் படுவ(து)
> அந்தணர் அருமறை மன்றல் எட்டனுள்
> கந்தருவ வழக்கம் என்மனார் புலவர்

*What is called களவு within the five திணை of love is, among the eight marriages of the brahmins'
rare Veda, the gandharva usage — so the learned say.*

**[மூலம் | SOURCE — comparison]** Tolkappiyam's களவியல் opens on the same ground
(`pmuni0100`, lines 2548–2552, நூ. 1):

> இன்பமும் பொருளும் அறனும் என்றாங்கு
> அன்பொடு புணர்ந்த ஐந்திணை மருங்கின்
> காமக் கூட்டம் காணும் காலை
> **மறையோர் தேஎத்து மன்றல் எட்டனுள்**
> **துறை அமை நல் யாழ்த் துணைமையோர் இயல்பே.**

**[விளக்கம் | INTERPRETATION] Both texts reach for the eight-fold Sanskrit marriage
classification — but only one of them names the category.** Tolkappiyam says *of the eight
marriages of the people of the Veda, [this is] the nature of those who are companions like a
well-tuned yāḻ* — an image, from Tamil music, standing where the Sanskrit term would go. Iraiyanar
replaces the image with the term: **கந்தருவ வழக்கம்**, gāndharva-vivāha. The yāḻ is gone.

That single substitution is the clearest measurable instance in this document of what the chain
does over time. The later text is not more Sanskritic in vocabulary generally — it is dense,
archaic Tamil — but at the one point where a category has to be fixed, it takes the Sanskrit name
and drops the Tamil figure. **[கருதுகோள் | HYPOTHESIS]** This is a general pattern of the
post-Tolkappiyam grammars: images survive where they are decorative and are replaced where they
are load-bearing. Testable against நன்னூல் and புறப்பொருள் வெண்பாமாலை. **[திறந்த கேள்வி]** Whether
Tolkappiyam's `மன்றல் எட்டு` is original or an interpolation from the same later layer is a live
question in the dating literature and is not settled here.

**(ii) Mutuality is definitional** [மூலம் — lines 33–35, நூ. 2]

> அதுவே
> தானே அவளே தமியர் காணக்
> காமப் புணர்ச்சி இருவயின் ஒத்தல்

*That is: he himself and she herself, alone, seen [by none] — the union of desire being equal on
both sides.*

**[விளக்கம் | INTERPRETATION]** `இருவயின் ஒத்தல்` — *equality on both sides* — is in the
definition, not in an ethical appendix. The following நூற்பா makes it exclusive: any union brought
about otherwise `எவ்விடத்(து) ஆயினும் களவிற்(கு) இல்லை` — *wherever it be, does not belong to
களவு* (lines 42–43, நூ. 4). **A grammar of clandestine love that begins by ruling out the
non-consensual case.** Worth saying out loud in a repo that will hand this material to children.

**(iii) Marriage is downstream of secret love** [மூலம் — lines 89–90, நூ. 15]

> முன்படப் புணராத சொல்இன் மையின்
> கற்பெனப் படுவது களவின் வழித்தே

*Since there is no word that was not first joined [to something], what is called கற்பு follows the
road of களவு.*

**[விளக்கம் | INTERPRETATION]** This is the architectural claim of the whole book, and it is
startling: **wedded love is defined as the continuation of clandestine love, not its correction.**
The 27 கற்பு sutras are therefore about the *aftermath* of the 33 களவு sutras. Note the
justification offered — a grammatical analogy: no word exists that has not first undergone
புணர்ச்சி (which in Tamil grammar means *sandhi*, the joining of words, and in poetics means
*union*). The pun is the argument. §7 returns to this.

**(iv) Three words** [மூலம் — line 108, நூ. 22]

> அம்பலும் அலரும் களவு

*Whispering and open rumour are [part of] களவு.* Five words in the original counting the sandhi;
three lexical items. **The gossip belongs to the love affair.** Not an obstacle to it, not a
consequence — a constituent. This is the compression that நன்னூல் நூ. 18 will later theorise (§6.3).

**(v) The grammar sets a deadline** [மூலம் — lines 151–152, நூ. 32]

> களவினுள் தவிர்ச்சி வரைவின் நீட்டம்
> திங்கள் இரண்டின் அகம்என மொழிப

*The interruption within களவு — the delay of the marriage — is said to be within two months.*

**[விளக்கம் | INTERPRETATION] A poetics that legislates a maximum of two months.** This is not
literary description; it is closer to family law rendered as prosody. A poet composing a
களவு sequence may not leave the marriage hanging longer than that. Whether it reflects actual
social practice or only compositional convention is **[திறந்த கேள்வி]** — but the fact that a
*grammar* states a number of months at all tells you how far பொருளதிகாரம் has drifted from
"grammar" in any sense a European tradition would recognise.

**(vi) An ethical asymmetry, stated flatly** [மூலம் — lines 188, 190, நூ. 45–46]

> புகழும் கொடுமையும் கிழவோன் மேன 45
> கொடுமை இல்லை கிழவி மேற்றே 46

*Praise and cruelty are upon the man. Cruelty is not upon the woman.*

**[விளக்கம் | INTERPRETATION]** In the கற்பு section, where the recurring situation is the
husband's absence with a பரத்தை. The grammar assigns *both* the praise and the blame to him, and
rules that cruelty is never attributed to her. **[திறந்த கேள்வி]** Whether `கொடுமை` here means
"cruelty done" or "cruelty spoken of / imputed" changes the force considerably, and the two readings
give different poems. This needs a commentator; the bare நூற்பா does not decide it. Flagged for the
ear and for a future உரை check.

The book closes on itself (lines 236–237, நூ. 60):

> களவு கற்(பு)எனக் கண்ணிய ஈண்டையோர்
> உளம்நிகழ் அன்பின் உயர்ச்சி மேன

**[விளக்கம் | INTERPRETATION — gloss tentative]** *Those here who have considered [it] as களவு and
கற்பு stand upon the rising of the love that occurs in the heart.* The whole two-part division is
declared to rest on one thing: `உளம் நிகழ் அன்பு`, love as it happens in the mind. Sixty sutras of
procedure, closed by naming the interior state they were procedures for.

## 5. The frame legend, and the three Sangams

The 60 நூற்பா are not why this book is famous. **Its உரை is.**

**[மூலம் | SOURCE]** The e-text prints the sutras and then a slice of the commentary — the file
itself says so (line 240): `இந்நூலுக்கு நீண்டு அகன்றதோர் உரை உள்ளது / நக்கீரர் அருளியது (என்பர்)`
— *there is a long and wide commentary on this book, given by Nakkīrar (so they say).* Note the
parenthetical `என்பர்` — *so they say* — in the e-text editor's own sentence, and his note at line
440: `உரையின் ஆசிரியர் நக்கீரர் (அறிஞர் பலருக்கு ஐயம் உள்ளது)` — *the commentator is Nakkīrar
(many scholars have doubts)*. The doubt is in the source; it is not something this document is
importing.

### 5.1 The story, as the உரை tells it

**[மூலம் | SOURCE — paraphrase of lines 254–412, with key phrases quoted]** The commentary opens by
asking who this book was expounded to, and answers: **உருத்திரசன்மன், son of உப்பூரிகிழார் of
Madurai.** To explain why, it tells the story that has shaped every subsequent account of Tamil
literary history.

1. **The three Sangams are named** — `தலைச்சங்கம், இடைச்சங்கம், கடைச்சங்கம் என / மூவகைப்பட்ட
   சங்கம் இரீஇயினார் பாண்டியர்கள்` — *the Pandyas established the Sangam in three kinds.*
2. **A twelve-year famine.** `அக்காலத்துப் பாண்டியநாடு பன்னீரியாண்டு வற்கடம் சென்றது` — the king
   dismisses his scholars: *I cannot support you; my land is greatly afflicted; go where you know
   to go, and when the land is a land again, remember me and come.*
3. **The rains return, the scholars are recalled — and one third of the grammar is missing.**
   Masters of எழுத்ததிகாரம் and சொல்லதிகாரம் are found. Then:
   `பொருளதிகாரம் வல்லாரை / எங்கும் தலைப்பட்டிலேம்` — *we have nowhere come upon anyone competent
   in பொருளதிகாரம்.* The king's reply is the hinge of the whole legend:
   `எழுத்தும் சொல்லும் ஆராய்வது / பொருளதிகாரத்தின் பொருட்டன்றே` — *is not the study of letters and
   words for the sake of பொருளதிகாரம்?*
4. **The god of Madurai composes the missing book.** `மதுரை ஆலவாயில் / அழல்நிறக் கடவுள்` — the
   fire-coloured god of Ālavāy — writes the sixty sutras on three copper leaves
   (`மூன்று செப்பிதழ்`) and places them under the pedestal (`பீடத்தின் கீழ்`). A temple servant
   sweeping under the pedestal finds them.
5. **Forty-nine scholars, forty-nine readings, no agreement.** They ask the king for a
   `காரணிகன்` — an arbiter. A voice sounding three times names one: a five-year-old, mute
   (`ஐயாட்டைப் பிராயத்தான்` — of five years' age), son of Uppūrikiḻār. He cannot speak, but
   `மெய்யாயின உரை கேட்டவிடத்து` — when he hears a true reading — his eyes will run and his body
   hair will stand.
6. **The test.** Each scholar reads. The boy sits unmoved until மதுரை இளநாகனார், at whom tears come
   in places; and then **கணக்காயனார் மகனார் நக்கீரனார்**, at whom `பதந்தொறும் கண்ணீர் வார்ந்து` —
   *tears ran at every single word.* The assembly cries: `மெய்யுறை பெற்றாம் இந்நூற்கு` — *we have
   got the true commentary for this book.*

**[விளக்கம் | INTERPRETATION]** Note what the legend is engineered to certify. It is not a story
about a god writing poetry. It is a **validation protocol for a commentary**: an
incorruptible judge (a child who cannot speak and cannot be lobbied), a physical response that
cannot be faked, and a public trial of forty-nine competing readings. The tradition needed
Nakkīrar's உரை to be authoritative, and built a courtroom to make it so.

### 5.2 The connection to marabu 003

[`../../marabu/paadal/003-kurunthogai-002-kongu-ther.md`](../marabu/paadal/003-kurunthogai-002-kongu-ther.md)
attributes குறுந்தொகை 2 (`கொங்குதேர் வாழ்க்கை...`) to **இறையனார்**, records that tradition holds
Śiva of Madurai composed it himself, and marks the attribution as legend in its §11.

**This is the same legend and the same god.** `இறையனார்` = *the Lord*; the ஆலவாய் shrine at Madurai
is the same shrine. **[விளக்கம் | INTERPRETATION]** The tradition has one Madurai deity who writes
Tamil twice: once a five-line akam poem submitted to the Sangam, once a sixty-sutra grammar left
under a pedestal. Entry 003 noticed the striking thing about the first — that the legend has a god
compose *a request for honest testimony* rather than a hymn. The second sharpens it: **when the
tradition needs a divine author, what it asks the god for is not scripture but poetics.** The
god of Madurai is, in this tradition, a literary critic.

**[முன்மொழிவு | PROPOSAL]** Entry 003's §11 should gain a cross-reference to this file, and its
open question ("whether a historical poet of that name existed") should be widened: the name
`இறையனார்` attaches to at least two distinct works, and any answer has to account for both.

### 5.3 The chronology — where the wild dates come from

**[மூலம் | SOURCE]** These are the commentary's own figures, read directly from lines 258–298.

| | **தலைச்சங்கம்** | **இடைச்சங்கம்** | **கடைச்சங்கம்** |
|---|---|---|---|
| Seat | `கடல் கொள்ளப்பட்ட மதுரை` — Madurai taken by the sea | `கபாடபுரத்து` | `உத்தர மதுரை` |
| Named members | 549 (`ஐஞ்ஞூற்று நாற்பத்தொன்பதின்மர்`), incl. **அகத்தியனார்**, `திரிபுரம் எரித்த விரிசடைக் கடவுளும்` (Śiva), `குன்றெறிந்த முருகவேளும்` (Murugan), `நிதியின் கிழவனும்` (Kubera) | 59 (`ஐம்பத்தொன்பதின்மர்`), incl. **அகத்தியனார், தொல்காப்பியனார்** | 49 (`நாற்பதொன்பதின்மர்`), incl. **நக்கீரனார்**, நல்லந்துவனார், மருதனிளநாகனார் |
| Total poets | 4,440 | 3,700 | — |
| Duration | **4,440 years** | **3,700 years** | `ஆயிரத்தொண்ணூற்றைம்பதிற்றி யாண்டு` — see note |
| Patron kings | 89 (`காய்சினவழுதி` … `கடுங்கோன்`) | 59 (`வெண்டேர்ச்செழியன்` … `முடத்திருமாறன்`) | — |
| Poet-kings | 7 | 5 | 3 |
| Its grammar | `அகத்தியம்` | `அகத்தியமும் தொல்காப்பியமும்` + மாபுராணம், இசைநுணுக்கம், பூதபுராணம் | `அகத்தியமும் தொல்காப்பியமும்` |
| Works | பரிபாடல், முதுநாரை, முதுகுருகு, களரியாவிரை | கலி, குருகு, வெண்டாளி, வியாழமாலை அகவல் | **நெடுந்தொகை 400, குறுந்தொகை 400, நற்றிணை 400, புறநானூறு, ஐங்குறுநூறு, பதிற்றுப்பத்து, கலி 150, பரிபாடல் 70** |

**[விளக்கம் | INTERPRETATION — the arithmetic, stated plainly]** The third Sangam's duration is
printed `ஆயிரத்தொண்ணூற்றைம்பதிற்றி`; read as *one thousand eight hundred and fifty*, the three
durations sum to **4,440 + 3,700 + 1,850 = 9,990 years**. **That is the source of the
"Tamil literature is ten thousand years old" claim, and it should be named as such every time it is
repeated.** It is not an inference from archaeology, epigraphy or linguistics. It is one number
added to two other numbers in a medieval commentary on a grammar of secret love.

**[திறந்த கேள்வி | OPEN QUESTION]** The e-text's `ஒண்ணூற்று` is almost certainly a fault for
`எண்ணூற்று` (800); 1,850 is the figure the tradition transmits. I have not been able to verify the
correct reading from this file alone, and the total therefore carries that one uncertainty. It does
not affect the order of magnitude.

**Three further things this table is good for, none of them chronology:**

1. **It is the earliest surviving list of the எட்டுத்தொகை as a group.** The third-Sangam entry
   names நெடுந்தொகை (= அகநானூறு), குறுந்தொகை, நற்றிணை, புறநானூறு, ஐங்குறுநூறு, பதிற்றுப்பத்து,
   கலி, பரிபாடல் — with the counts 400/400/400 and 150/70 — which is the anthology set the repo
   reads in [`../../ilakkiyam/`](../ilakkiyam/). **The corpus's own name for itself starts
   here.**
2. **It names books that are lost.** முதுநாரை, முதுகுருகு, களரியாவிரை, வெண்டாளி, வியாழமாலை அகவல்,
   மாபுராணம், இசைநுணுக்கம், பூதபுராணம் — none survive. The e-text's editorial note (lines 436–441)
   adds that the full commentary quotes from further works now lost, naming
   `இளம்திரையம், சாதவாகனம், கலைக்கோட்டுத்` தண்டு, நூல், நிகண்டு,
   `செம்பூழ்சேயார்கூற்றியல், கூத்தநூல்,` and `சிற்றெட்டகம்` — described there as
   `நமக்கு கிடைக்காத தொன்னூற்களின் பெயர்கள்`, *the names of ancient books not available to us* —
   and preserves 325+ verses of an akapporuḷ
   கோவை since published as **பாண்டிக்கோவை**. This bears directly on
   [`../../varalaru/arivu-varalaru.md`](../varalaru/arivu-varalaru.md) §3 on survival bias: the
   commentary is a *list of what did not survive*, made by someone who could still see it.
3. **It puts Tolkappiyar in the middle Sangam and Agastya in both the first and the middle.** The
   tradition is explicitly claiming Tolkappiyam is not the beginning. `அகத்தியம்` is — a work that
   does not survive and may never have existed.

### 5.4 The transmission chain — the commentary dates itself

**[மூலம் | SOURCE — lines 414–426]** The commentary ends by tracing its own descent, teacher to
teacher:

நக்கீரனார் → his son **கீரங்கொற்றனார்** → **தேனூர்க் கிழார்** → **படிமங் கொற்றனார்** →
**செல்வத்தாசிரியர் பெருஞ்சுவனார்** → **மணலுராசிரியர் புளியங்காய் பெருஞ்சேந்தனார்** →
**செல்லூர் ஆசிரியர் ஆண்டைப் பெருங்குமரனார்** → **திருக்குன்றத்து ஆசிரியர்** →
**மாதவளனார் இளநாகனார்** → **முசிறியாசிரியர் நீலகண்டனார்**, and then:
`இங்ஙணம் வருகின்றது உரை` — *thus the commentary comes down.*

**[விளக்கம் | INTERPRETATION] This list is the single most useful dating evidence in the book, and
it argues against the book's own frame.** Ten named teachers stand between Nakkīrar and the person
who wrote this down. If the text as we have it were Nakkīrar's own composition, there would be no
chain to record. **The colophon is telling you, in the tradition's own voice, that what you are
reading was written by the tenth man, not the first** — which is exactly the ground on which
scholars place the surviving உரை centuries after the sutras, and the e-text editor's parenthetical
`(அறிஞர் பலருக்கு ஐயம் உள்ளது)` reflects that.

**[விளக்கம் | INTERPRETATION]** And note the honesty of the frame at line 407: some say the boy
Uruttiracaṉmaṉ composed the commentary; `அவன் செய்திலன் / மெய்யுரை கேட்டானென்க` — *he did not
compose it; say rather that he heard the true reading.* The text corrects a rival attribution in
passing. It is a document aware that attributions get contested.

---

# III. புறப்பொருள் வெண்பாமாலை — the puram counterpart

## 6. What ஐயனாரிதனார் added, precisely

**[மூலம் | SOURCE]** Author and self-positioning, from the சிறப்புப்பாயிரம் (lines 62–73). The
book says it was made by `ஐயனா ரிதன்`, who had faultlessly understood `தொல்காப் பியன்முதல் /
பன்னிரு புலவரும் பாங்குறப் பகர்ந்த / பன்னிரு படலமும்` — *the twelve படலம் well spoken by the
twelve poets beginning with Tolkāppiyaṉ* — and who set it out `மையறு புறப்பொருள் வழால்இன்று
விளங்க / வெண்பா மாலை எனப்பெயர் நிறீஇ` — *so that flawless puṟapporuḷ should shine without error,
establishing the name "Veṇpā Garland."*

**[மூலம் | SOURCE]** Size, from the file's own closing tally (lines 3200–3201):
`ஆக சூத்திரங்கள் = 19 / இதற்கு வெண்பாக்கள் = 361`. Nineteen sutras; three hundred sixty-one
வெண்பā. The படலam and their verse ranges are listed at lines 22–43.

### 6.1 The mechanism — a grammar that supplies its own corpus

**This is the thing to understand about the book, and it is visible in ten lines of the file.** Each
துறை gets **two** things: a short definition, and a வெண்பா composed to illustrate it.

**[மூலம் | SOURCE — lines 128–135, வெட்சிப் படலம், the துறை *செலவு* (the setting out)]**

The definition — two lines, ending in the characteristic `-அன்று`:

> வில் ஏர் உழவர் வேற்றுப் புலம் உன்னிக்
> கல் ஏர் கானம் கடந்து சென்றன்று

*The bow-ploughmen, setting their minds on a foreign country, went across the stone-strewn forest.*

Then, numbered `1.8`, the illustration:

> கூற்று இனைத்து அன்னார் கொடுவில் வலன் ஏந்திப்
> பாற்று இனம் பின் படர முன்படர்ந்து - ஏற்றினம்
> நின்ற நிலை கருதி ஏகினார் நீள் கழைய
> குன்றம் கொடு வில்லவர் 5

*Men like so much Death, bearing the curved bow in the right hand, going ahead with the flock of
carrion birds following behind — the bowmen of the long-bamboo hills went out, having reckoned where
the herd was standing.*

**[விளக்கம் | INTERPRETATION] Tolkappiyam gives definitions and expects you to find the poems.
புறப்பொருள் வெண்பாமாலை gives definitions and *provides* the poems.** That is a different kind of
book: a grammar with a built-in exemplar corpus, 361 poems deep, every one composed to specification.
Its consequence is the answer to the brief's question about preservation — **a துறை whose Sangam
exemplars have been lost still has an exemplar here**, because the exemplar was made for the slot
rather than found for it. The categories survive the literature.

**[கருதுகோள் | HYPOTHESIS]** This also makes the book a controlled corpus for prosody work: 361
வெண்பā by (nominally) one hand, each with a declared subject. **Prediction:** metrical variation
across the 361 should be markedly narrower than across 400 நாலடியார் verses by many hands.
Measurable with the சீர்/அசை machinery already built for
[`../../ilakkanam/tholkappiyam-seyyuliyal.md`](../ilakkanam/tholkappiyam-seyyuliyal.md).

### 6.2 The reclassification — twelve திணை in three ranks

**[மூலம் | SOURCE — lines 3191–3198, the closing section 19, `திணைகளின் தொகுப்பு வகைகள்`]**

> வெட்சி கரந்தை வஞ்சி காஞ்சி
> உட்குடை உழிஞை நொச்சி தும்பை என்று
> இத்திறம் ஏழும் புறம் என மொழிப 1
> வாகை பாடாண் பொதுஇயல் திணை எனப்
> போகிய மூன்றும் புறப்புறம் ஆகும் 2
> கைக்கிளை பெருந்திந்ணை ஆம் இவ்விரண்டும்
> அகப்புறம் ஆம் என அறைந்தனர் புலவர் 3

*Veṭci, karantai, vañci, kāñci, dread-bearing uḻiñai, nocci, tumpai — these seven kinds they call
**puṟam**. Vākai, pāṭāṇ and the pothuviyal tiṇai — those three that have gone out are
**puṟappuṟam**. Kaikkiḷai and peruntiṇai — these two the learned have declared to be
**akappuṟam**.*

**Now set that beside Tolkappiyam.** The repo's verified table in
[`../../ilakkanam/tholkappiyam-thinai.md`](../ilakkanam/tholkappiyam-thinai.md) §6 gives
Tolkappiyam's seven புறத்திணை and the akam திணை each is fastened to:

| | **தொல்காப்பியம்** (7) | **புறப்பொருள் வெண்பாமாலை** (12, in 3 ranks) |
|---|---|---|
| | வெட்சி · வஞ்சி · உழிஞை · தும்பை · வாகை · காஞ்சி · பாடாண் | **புறம் (7):** வெட்சி · **கரந்தை** · வஞ்சி · காஞ்சி · உழிஞை · **நொச்சி** · தும்பை |
| | | **புறப்புறம் (3):** வாகை · பாடாண் · பொதுவியல் |
| | | **அகப்புறம் (2):** கைக்கிளை · பெருந்திணை |
| Criterion | **Structural symmetry** — each puram திணை is the "outside" of one akam திணை; seven and seven | **Subject matter** — is this actual warfare? |

**[விளக்கம் | INTERPRETATION] Both systems have exactly seven at the core, and they are not the
same seven.** The differences are all one move:

- **கரந்தை and நொச்சி are promoted.** Tolkappiyam has them, but *inside* other திணை — கரந்தை at
  புறம் 5 within the வெட்சி run (`pmuni0100` line 2346: `அனைக்கு உரி மரபினது கரந்தை`), நொச்சி at
  புறம் 11 within உழிஞை (line 2387). Naccinārkkiṉiyar states the reason for refusing them
  திணை-hood (`pmuni0500_01-tholkappiyam-porulathikaram-urai-1.txt`, line 113; also recorded at the
  repo's §6.5): `கரந்தை அவ் வேழற்கும் பொதுவாகிய வழுவாதலின், வேறு திணையாகாது` —
  *because karantai is a deviation common to all seven, it does not become a separate திணை.*
  **புறப்பொருள் வெண்பாமாலை overrules this and gives each its own படலம்** (14 துறை for கரந்தை,
  lines 265–274; 9 for நொச்சி, lines 823–830).
- **வாகை and பாடாண் are demoted** out of புறம் proper into **புறப்புறம்** — because neither is
  about fighting. வாகை is excellence of any kind; பாடாண் is praise.
- **கைக்கிளை and பெருந்திணை are pulled in** from the akam side as **அகப்புறம்**, "the outer face of
  akam." These are exactly the two ends of Tolkappiyam's seven-fold akam scale that
  [`../../ilakkiyam/sangam.md`](../ilakkiyam/sangam.md) §1 was corrected to restore — one-sided
  love before the five, excessive love after. **Here they are re-annexed by the puram grammar.**

**[விளக்கம் | INTERPRETATION] The criterion has changed, and that is the finding.** Tolkappiyam
defends a symmetry: seven akam, therefore seven puram, and a war-topic that cannot be paired
one-to-one with a love-topic is refused promotion no matter how distinct it is. **புறப்பொருள்
வெண்பாமாலை abandons the pairing and sorts by content instead**, then invents two boundary ranks —
புறப்புறம் and அகப்புறம் — to hold what the new criterion cannot place. The system has stopped
being a mirror and started being a taxonomy.

### 6.3 What it preserves that would otherwise be lost — three concrete cases

**(i) The நடுகல் ritual, with one stage Tolkappiyam does not name.**

**[மூலம் | SOURCE]** Tolkappiyam (`pmuni0100`, lines 2351–2353): `காட்சி கால்கோள் நீர்ப்படை
நடுதல் / சீர்த்த மரபின் பெரும்படை வாழ்த்தல் என்று / இரு மூன்று மரபின் கல்லொடு புணர` — *sighting,
taking up, water-rite, planting, great-offering, praising — six traditions joined with the stone.*
(**[திறந்த கேள்வி]** The parse into six depends on splitting `பெரும்படை வாழ்த்தல்` into two items;
that is a commentator's decision, of exactly the kind the repo's §6.4 warns about.)

**[மூலம் | SOURCE]** PPVM (lines 2158–2161), inside the twelve துறை of பொதுவியல்:
`கழல் நிலை, கல்காண்டல்லே, / கல்கோள் நிலையே, கல்நீர்ப்படுத்தல் / கல்நடுகல்லே, கல்முறை பழிச்சல், /
இல்கொண்டு புகுதல்`.

| Tolkappiyam | PPVM | The act |
|---|---|---|
| காட்சி | கல்காண்டல் | finding the stone |
| கால்கோள் | கல்கோள் நிலை | taking it up |
| நீர்ப்படை | கல்நீர்ப்படுத்தல் | bathing it *(PPVM gives this **two** exemplar verses, lines 2235 and 2243)* |
| நடுதல் | கல்நடுகல் | planting it |
| வாழ்த்தல் | கல்முறை பழிச்சல் | praising it in due order |
| — | **இல்கொண்டு புகுதல்** | **housing it — taking it in and entering** |

**[விளக்கம் | INTERPRETATION]** The last row is the point. PPVM's sequence ends with the stone being
**taken into a structure**, and Tolkappiyam's does not. The hero-stone has acquired a building
between the two texts. **A grammar is recording a change in religious practice, in a list of genre
slots, because the poems had to have somewhere to go.** Its final verse for the sequence ends
`இல்கொண்டு புக்கார் இசைந்து` (line 2274).

**(ii) The ஆற்றுப்படை genre labels, in four flavours.**

**[மூலம் | SOURCE]** The பாடாண் சூத்திரம் (lines 1730–1731) lists among its துறை:
`பாண் ஆற்றுப்படையே, கூத்தர் ஆற்றுப்படையே, / பொருநர் ஆற்றுப்படையே, விறலி ஆற்றுப்படையே`.

**[விளக்கம் | INTERPRETATION]** Those four labels are the classification under which five of the
பத்துப்பாட்டு are read — and [`../../ilakkiyam/pathupattu.md`](../ilakkiyam/pathupattu.md) §3
already notes that the string `துறை :: ஆற்றுப்படை` is printed in the Sangam source files
themselves. **The genre headers that modern editions print above Sangam poems come out of this
grammatical tradition**, not out of the poems. When a reader today sees "துறை: பாணாற்றுப்படை"
above a two-thousand-year-old poem, they are reading a label supplied by ஐயனாரிதனார்'s lineage.

**(iii) The victory list — puram poetics extended past war.**

**[மூலம் | SOURCE]** The **ஒழிபுப் படலம்** (section 18, lines 3054–3067) opens by naming
Tolkappiyam directly — `பாடாண் பகுதியுள் தொல் காப்பிய முதல் / கோடா மரபில்` — and then enumerates
kinds of வென்றி that Tolkappiyam does not have: `வாணிக வென்றியும், மல்ல வென்றியும், / நீள்நெறி
உழவன் நலன்உழு வென்றியும்` — **the merchant's victory, the wrestler's victory, the ploughman's
good-furrow victory** — followed by the victories of bulls, cocks, rams, elephants, quails,
partridges, parrots, mynahs, horses, chariots, the yāḻ, dice, dancing, singing, and the
she-elephant. Nineteen worked examples follow, lines 3068–3190, one per category.

**[விளக்கம் | INTERPRETATION]** Read the list and the social world has changed. Tolkappiyam's
வாகை is excellence in one's proper role, illustrated through kings, brahmins and warriors. PPVM's
ஒழிபு writes **a trader outfacing the sea** (18.2: `காடும் கடும்திரைநீர்ச் சுழியும்கண் அஞ்சான்`
— *fearing neither forest nor the whirl of the fierce-wave water*), **a farmer whose victory is
the harvest** (18.4, ending `வித்தித் தருவான் விளைவு` — *he who sows and delivers the yield*),
and **a woman winning at dice and at song** (18.16, 18.18). The puram genre has been opened to
people who never held a spear.

### 6.4 The famous line, put back in its slot

**[மூலம் | SOURCE — lines 381–388, கரந்தைப் படலம், verse 35]** The repo already quotes this in
[`../../aaivu/mudhal-oli.md`](../aaivu/mudhal-oli.md) §1. Here is what surrounds it, which that
file did not have. The definition first:

> (குடிநிலை இன்னது)
> மண்திணி ஞாலத்துத் தொன்மையும் மறனும்
> கொண்டு பிறர் அறியும் குடி உரைத்தன்று

*(**குடிநிலை** is this:) it speaks of a lineage that others know by its antiquity and its valour on
the earth-packed world.*

And then the illustration, `2.15`:

> பொய் அகல நாளும் புகழ் விளைத்தல் என் வியப்பாம்
> வையகம் போர்த்த வயங்கு ஒலி நீர் - கைஅகலக்
> கல் தோன்றி மண் தோன்றாக் காலத்தே வாளோடு
> முன் தோன்றி மூத்த குடி

**[விளக்கம் | INTERPRETATION] This changes how the line should be cited, and the change matters.**
`கல் தோன்றி மண் தோன்றா` is not a free-standing historical assertion that somebody made about
Tamil. **It is a worked example filling a genre slot.** The poet's assignment was *"compose a
குடிநிலை — a lineage praised for antiquity and valour"* — and the definition immediately above the
verse says so in the source. Antiquity was the *specified content of the exercise*.

`mudhal-oli.md` §1 already labels the verse medieval, praise-genre, and myth's tense, and keeps the
dissonance declared. **This sharpens all three:** the antiquity claim is not even the poet's
opinion; it is the brief he was working to. That is a stronger version of the same honest reading,
and it is now sourced to the two lines directly above the verse.

*(Minor: `mudhal-oli.md` prints `கையகலக்`; the source at line 386 reads `கைஅகலக்`. Orthographic,
not substantive.)*

---

# IV. நன்னூல் — the grammar that won the classroom

## 7. What it covers, what it drops, and why it won

**[மூலம் | SOURCE]** Structure, from the file's own contents (lines 24–39) and verified against the
numbering:

| பகுதி | நூற்பா | வரி |
|---|---|---|
| சிறப்புப்பாயிரம் | unnumbered | 41–65 |
| **பாயிரம்** (பொது) | 1–55 | 66–279 |
| **எழுத்ததிகாரம்** | 56–257 | 280–~700 |
| **சொல்லதிகாரம்** | 258–462 | ~700–1274 |

**462 நூற்பா. Two adhikāram. There is no third.**

### 7.1 The omission, and what it means

**[விளக்கம் | INTERPRETATION] நன்னூல் has no பொருளதிகாரம், and this is the most consequential fact
in this document.** Tolkappiyam's third book is where திணை, துறை, மெய்ப்பாடு, உவமை, செய்யுள் and
மரபு live — the entire apparatus by which Tamil poetry means what it means. நன்னூல் ends at words
and does not go on.

Three readings, and the third is the one this document holds:

1. **Loss** — the poetics was simply dropped, and Tamil education got narrower.
2. **Deference** — Pavanandi did not presume to redo Tolkappiyam's greatest section.
3. **[விளக்கம் | INTERPRETATION] Division of labour — the poetics had already left.** By the time
   நன்னூல் was written, **இறையனார் அகப்பொருள் held akam and புறப்பொருள் வெண்பாமாலை held புறம்**,
   each as a standalone book with its own commentary tradition. There was no gap to fill. நன்னூல்'s
   silence is not an absence; it is the last step of a split that had been under way for centuries.

**And the legend in §5.1 is the tradition telling this story about itself, in reverse.** The
Iraiyanar உரை's whole premise is that **எழுத்து and சொல் survived the famine and பொருள் did not** —
that the two can come apart, and that the one that comes apart is பொருள். The king's protest,
`எழுத்தும் சொல்லும் ஆராய்வது` / `பொருளதிகாரத்தின் பொருட்டன்றே`, is an argument *against* exactly the
book நன்னூல் would eventually be. **The legend is a memory of the split, dramatised as a
catastrophe.** நன்னூல் is what happens when the catastrophe becomes the settled arrangement.

**[திறந்த கேள்வி | OPEN QUESTION]** The சிறப்புப்பாயிரம் (lines 50–52) says the patron asked that
`அரும்பொருள் ஐந்தையும் யாவரும் உணரத் / தொகைவகை விரியின் தருக` — *give the five rare matters, in
summary, division and expansion, so that all may understand.* If `அரும்பொருள் ஐந்து` means
**ஐந்திலக்கணம்** (எழுத்து, சொல், பொருள், யாப்பு, அணி), then **the book's own preface records a
commission for five and a delivery of two** — which would make the omission deliberate and
visible to Pavanandi himself. The phrase can also be read as a general "five precious matters"
with no technical sense. **I cannot decide this from the bare text and do not.** It is the highest-
value commentary check in this document: நன்னூல் has a rich உரை tradition
(மயிலைநாதர், சங்கரநமச்சிவாயர், ஆறுமுக நாவலர்) and one of them will state a reading.

### 7.2 A theory of what a grammar is allowed to be

**[மூலம் | SOURCE — lines 84–93, நூ. 5–8]** Before saying anything about Tamil, நன்னூல் classifies
books:

> 5. முதல் வழி சார்பு என நூல் மூன்று ஆகும்
> 6. அவற்றுள், / வினையின் நீங்கி விளங்கிய அறிவின் / முனைவன் கண்டது முதல்நூல் ஆகும்
> 7. முன்னோர் நூலின் முடிபு ஒருங்கு ஒத்துப் / பின்னோன் வேண்டும் விகற்பம் கூறி / அழியா மரபினது
>    வழிநூல் ஆகும்
> 8. இருவர் நூற்கும் ஒருசிறை தொடங்கித் / திரிபு வேறு உடையது புடைநூல் ஆகும்

*Books are of three kinds: **முதல்நூல**, **வழிநூல்**, **சார்பு/புடைநூல்**. A முதல்நூல் is what was
seen by a sage of clear knowledge, freed from karma. A **வழிநூல்** agrees entirely with the
conclusions of the earlier book, states the distinctions the later author needs, and stands in an
unbroken tradition. A **புடைநூல்** starts from one side of both and differs by deviation.*

**[விளக்கம் | INTERPRETATION] This is a grammar opening with a theory of intellectual legitimacy,
and it is self-serving in the most productive possible way.** நன்னூல் is declaring the category it
intends to occupy. Its own சிறப்புப்பாயிரம் says so explicitly (lines 63–64):
`முன்னோர் நூலின் / வழியே நன்னூல் பெயரின் வகுத்தனன்` — *in the **வழி** of the ancients' book he set
it out under the name Naṉṉūl.* **The word `வழி` in that line is நூ. 7's technical term.** The book
is telling you it is a வழிநூல் of Tolkappiyam: not a rival, not a replacement, an authorised
successor — and therefore free to differ wherever the successor "needs a distinction."

**That is the licence under which the whole post-Tolkappiyam tradition operates, finally written
down.** இறையனார் needed a god to authorise a new பொருளதிகாரம்; ஐயனாரிதனார் claimed descent from
the twelve pupils; **பவணந்தி just defines the category and steps into it.**

Note also **நூ. 9** (lines 94–97): the old sutras are cited both for *we shall guard the ancients'
very words like gold* and for *there is no injunction against making a book different from the
ancients'*. **The two positions are placed side by side and neither is resolved.** A grammar that
prints its own methodological disagreement in its ninth sutra.

### 7.3 Why it won: it teaches the classroom, not just the language

This is the concrete answer to the brief's question, and every item is in the first 55 நூற்பா —
before a single letter of Tamil is described.

**(i) It defines its own genre of writing.** [மூலம் — lines 145–149, நூ. 18–19]

> 18. சில்வகை எழுத்தில் பல்வகைப் பொருளைச்
> செவ்வன் ஆடியின் செறித்து இனிது விளக்கித்
> திட்பம் நுட்பம் சிறந்தன சூத்திரம்

*A **சூத்திரம்** is that which, in few letters, packs many meanings straight as a mirror does,
illumines them sweetly, and excels in firmness and subtlety.*

> 19. ஆற்று ஒழுக்கு அரிமா நோக்கம் தவளைப் பாய்த்து
> பருந்தின் வீழ்வு அன்ன சூத்திர நிலை

*The standing of a sutra is like **the flow of a river, the lion's backward look, the frog's leap,
the kite's stoop.***

**[விளக்கம் | INTERPRETATION]** நூ. 19 is a taxonomy of *how a sutra's words reach across the
text* — continuously (river), by looking back to the previous sutra (lion), by jumping over
intervening ones (frog), by dropping in from far above onto a distant one (kite). **This is a
reading manual.** A student who has it can parse a compressed text without a teacher present for
every line. Tolkappiyam offers nothing equivalent; it *is* sutras, and does not explain how to
take them.

நூ. 21–23 continue: fourteen elements of a உரை; **காண்டிகை** (the compact gloss) and **விருத்தி**
(the full expansion) defined and distinguished. **நன்னூல் ships with the specification for its own
commentaries.**

**(ii) It grades the students.** [மூலம் — lines 214–221, நூ. 38–39]

> 38. அன்னம் ஆவே மண்ணொடு கிளியே
> இல்லிக் குடம் ஆடு எருமை நெய்யரி
> அன்னர் தலை இடை கடை மாணாக்கர்

*Swan, cow, earth, parrot, leaky pot, goat, buffalo, ghee-strainer — such are the first, middle and
last kinds of student.* **[விளக்கம் | INTERPRETATION]** The swan separates milk from water; the
earth returns more than it is given; the parrot repeats without understanding; the leaky pot keeps
nothing; the buffalo muddies the water it drinks; the ghee-strainer lets the good through and keeps
the dregs. **A teacher's diagnostic list, in nine words.** நூ. 39 then names eleven kinds of person
to whom a book should *not* be taught (the vain, the lustful, the thief, the quarrelsome, the
angry, the sleeper, the dull, `தொன்னூற்கு அஞ்சி` — *he who is afraid of an old book*).

**(iii) It scripts the lesson.** [மூலம் — lines 194–213, நூ. 36, 40–46] நூ. 36 is a procedure for
the teacher: look to time and place, sit in a fit spot, praise your god, settle the matter in mind,
be neither hasty nor angry, brighten your face, know how the taker takes. **நூ. 40 is a procedure
for the student**, and it is the most quoted passage in the book: go at the hour and do not weary
of service; `இரு என இருந்து சொல் எனச் சொல்லி` — *sit when told to sit, speak when told to speak*;
`பருகுவன் அன்ன ஆர்வத்தன் ஆகி` — *be one whose eagerness is like a man drinking*;
`சித்திரப் பாவையின் அத்தகவு அடங்கி` — *as still as a painted doll*;
`செவி வாய் ஆக நெஞ்சு களன் ஆக` — **the ear becoming the mouth, the mind becoming the threshing
floor**; and go when told to go.

**நூ. 42–45 give the repetition arithmetic:** hear once, hear twice — `பெருக நூலில் பிழைபாடு
இலனே`, he will be largely free of error; hear three times and he can expound it in order; take the
teacher's exposition perfectly and you still hold only `கால்கூறு`, a quarter part; the rest comes
from practising with fellow students and from expounding it yourself.

**(iv) It insists a book must introduce itself.** [மூலம் — lines 272–273, நூ. 54]

> 54. ஆயிரம் முகத்தான் அகன்றது ஆயினும்
> பாயிரம் இல்லது பனுவல் அன்றே

*Though it be vast with a thousand faces, what has no preface is no book at all.* And நூ. 47 lists
the eight things a preface must state — author, lineage, scope, title, form, subject, audience,
benefit. **This document's own header block is nūṟpā 47 being obeyed.**

**[விளக்கம் | INTERPRETATION] Put these four together and the classroom question answers itself.**
Tolkappiyam is a description of Tamil. **நன்னூல் is a description of Tamil *plus a complete
operating manual for teaching it*** — what a sutra is, how to read one, how to write the commentary,
who may be taught, how the teacher should sit, how many hearings a student needs, and what a book
owes its reader before it begins. A teacher with நன்னூல் needs nothing else in the room. That is
why it displaced a greater book.

### 7.4 One doctrinal shift, traceable in a single line

**[மூலம் | SOURCE — line 98, நூ. 10]** `அறம் பொருள் இன்பம் வீடு அடைதல் நூல் பயனே` — *the benefit
of a book is the attaining of aṟam, poruḷ, iṉpam and **vīṭu**.*

**[மூலம் | SOURCE — comparison]** Tolkappiyam's களவியல் opens (`pmuni0100`, line 2548):
`இன்பமும் பொருளும் அறனும் என்றாங்கு` — **three.** திருக்குறள் has three பால். நாலடியார் has three
பால் (§1). **நன்னூல் has four, and the fourth is வீடு — release.**

**[விளக்கம் | INTERPRETATION]** The Tamil ethical frame goes from three aims to four across this
chain, and the book that adds the fourth is by a **Jain monk** — as நாலடியார' is by Jain ascetics
(§1) — writing under a patron named in the preface, `சீய கங்கன் / அருங்கலை வினோதன் அமரா பரணன்`
(lines 61–62). The whole of §III–§IV is a Jain-authored layer sitting on top of a Sangam-era
inheritance, and the fourth aim is its fingerprint. **[திறந்த கேள்வி]** Whether Tolkappiyam's
three-aim formula reflects a genuinely pre-Jain/pre-Vedic Tamil ethics or is simply a shorter
version of the same scheme is contested and not decided here.

### 7.5 And it ends by legitimising change

**[மூலம் | SOURCE — lines 1273–1274, நூ. 462, the last sutra of the book]**

> 462. பழையன கழிதலும் புதியன புகுதலும்
> வழு அல கால வகையின் ஆனே

*The old passing away and the new coming in are not faults, by the nature of time.*

**[விளக்கம் | INTERPRETATION]** The standard grammar of Tamil, the one that ruled the classroom
for seven centuries, **closes by declaring that the language it has just codified will change, and
that the change is not an error.** After 462 sutras of rule-making, the last rule is that rules
expire.

This belongs in [`../../aaivu/vithai.md`](../aaivu/vithai.md), and it belongs to phase 2 of this
project (**பரிணாமம்**) as directly as anything in the corpus. A prescriptive tradition that writes
its own obsolescence clause into its final line is not the tradition that popular accounts of
"the world's oldest living language" describe.

---

## 8. காலம் | Dating — the ranges, and who holds what

**[மூலம் | SOURCE]** What the source files themselves supply. This is thin, and that is the point.

| நூல் | Internal evidence in the file | What it fixes |
|---|---|---|
| **நாலடியார்** | Front matter (line 24) attributes it to Jain ascetics and calls it a compilation; classed as one of the **பதினெண்கீழ்க்கணக்கு** | Places it in the post-Sangam didactic group, no absolute date |
| **இறையனார்** | உரை's transmission chain of **ten teachers** after Nakkīrar (lines 414–426); the உரை quotes works now lost | The உரை is many generations after the sutras — **by the text's own account** |
| **புறப்பொருள் வெண்பாமாலை** | பாயிரம् names the author `ஐயனாரிதனார்` and claims descent from `தொல்காப்பியன்முதல் பன்னிரு புலவர்` | Self-positioned as post-Tolkappiyam; no king datable from the file |
| **நன்னூல்** | Patron named: `சீய கங்கன் / அருங்கலை வினோதன் அமரா பரணன்` (lines 61–62); author `பவணந்தி`, pupil of `சன்மதி முனி` of `பொன்மதில் சனகை`; **நூ. 460 (line 1267) defers to `பிங்கலம்`** for uriccol | The **பிங்கலம்** reference is a real *terminus post quem*: நன்னூல் postdates the Piṅkalam nikaṇṭu |

**[மூலம் | SOURCE — repo house positions already recorded]**
[`../../ilakkiyam/README.md`](../ilakkiyam/README.md) places the பதினெண்கீழ்க்கணக்கு in the
**சங்கம் மருவிய** period, ~300–600 CE, *with an explicit caution that ranges vary*, and
நன்னூல் in the **இடைக்காலம்**, ~900–1600. [`../../varalaru/mozhi-varalaru.md`](../varalaru/mozhi-varalaru.md)
§38 gives நன்னூல் as **13th c.** and calls it "a medieval lens through which the classical language
is still taught." [`../../agaraadhi.md`](../agaraadhi.md) gives புறப்பொருள் வெண்பாமாலை as
**9th c.**

**[திறந்த கேள்வி | OPEN QUESTION] Every one of these is a range, and the ranges are argued.** What
can be said without picking a side:

- The **relative** order is well supported and is what this document's argument depends on:
  Tolkappiyam → நாலடியார் / இறையனார் → புறப்பொருள் வெண்பாமாலை → நன்னூல். Each later work either
  names or presupposes the earlier ones.
- The **absolute** dates are not settled for any of the four. The repo's practice — give the range,
  name who holds what, or say the question is open — is followed here, and I have deliberately not
  attached century figures to நாலடியார் or இறையனார் at all, because I cannot support any from the
  files in `_src/` and will not import them from memory.
- **The Sangam chronology in §5.3 is not a dating position and must never be cited as one.** It is a
  medieval commentator's frame narrative. Its 9,990 years circulate widely; §5.3 shows exactly which
  three numbers they come from and where they are printed.

**[முன்மொழிவு | PROPOSAL]** The repo needs a single dating page that holds the ranges and the named
positions for the post-Sangam works the way `varalaru/arivu-varalaru.md` §2 does for Tolkappiyam,
so that individual documents can cite it instead of re-litigating.

---

## 9. மூல நிலை | The state of the four e-texts

**[மூலம் | SOURCE]** Machine-checked. Every Tamil-block codepoint in each file was tested against
the Unicode assignment table.

| File | Unassigned Tamil-block codepoints | Latin-1 intrusions | Decomposed vowel signs | Verdict |
|---|---|---|---|---|
| `pmuni0147` **நன்னூல்** | **0** | 0 | **87** | No corruption, but a **grep hazard** — see §9.2. |
| `pmuni0301` **இறையனார்** | 0 | 1 (U+00A8) | 0 | Clean. Uses `(...)` to mark elided சந்தி — a deliberate editorial convention, not damage. |
| `pmuni0300` **புறப்பொருள்** | 0 | **14** (6× U+00A8, 6× U+00A1, U+00A6, U+00A2) | 0 | TSCII-conversion residue. One is inside a word: `ப,ணர்த்து` (line 3145) for `புணர்த்து`. |
| `pmuni0016` **நாலடியார்** | **17** | 1 | 0 | **Most damaged of the four.** See §9.1. |

### 9.1 A systematic fault in the நாலடியார் e-text — and its key

**[மூலம் | SOURCE]** Seventeen occurrences of codepoints that are *reserved and unassigned* in the
Unicode Tamil block: **U+0BA2 ×14**, U+0BA1, U+0BA6, U+0BA7. These are not rare letters; they are
holes in the standard, produced by a bad TSCII→Unicode mapping.

**[விளக்கம் | INTERPRETATION] The pattern is regular and decodable.** In every one of the fourteen
U+0BA2 cases, the two-character sequence `ா` + U+0BA2 stands where **ரி** belongs. The context
proves it:

| வரி | As printed | Reads as |
|---|---|---|
| 700 | `புணர்தற் கா{U+0BA2}யாரை` | புணர்தற்க**ரி**யாரை — *those hard to obtain* |
| 1195 | `புகற்கா{U+0BA2}ய பூழை` | புகற்க**ரி**ய — *hard to enter* |
| 1338 | `அறிதற் கா{U+0BA2}ய பொருள்` | அறிதற்க**ரி**ய — *hard to know* |
| 1519 | `காண்டற் கா{U+0BA2}யதோர் காடு` | காண்டற்க**ரி**யதோர் — *hard to see* |
| 976 | `தமா{U+0BA2}னும்` | தம**ரி**னும் — *than kin* |
| 1049 | `புணா{U+0BA2}ன்` | புண**ரி**ன் — *if joined* |

Fourteen instances, one rule. **[முன்மொழிவு | PROPOSAL]** A twelve-line repair script keyed on
that sequence would fix the file. The three remaining faults are less regular — `஦வ்ருஉம்`
(line 1674) is `வெரூஉம்`, *fears*, in a verse about a doe on a tiger's path; `நுண்ணு஡ல்`
(line 992) and `இற்கொண் டினித஧ருஉம்` (line 1530) I have **not** been able to resolve from context
and should not guess. Plus one stray Latin digit at the end of verse 45: `பல்லென்பு கண்டொழுகு வேன3`
(line 222), where the parallel line in verse 44 (line 218) reads `கண்ணீர்மை கண்டொழுகு வேன்.`

**Consequence for this document, stated up front:** none of the four verses read in §3 contains a
corrupt codepoint. They were chosen partly for that. The one textual issue in the four is
`தொழுநொய` for `தொழுநோய` (line 540, §3.2) — a vowel-length fault, flagged at the quotation.

### 9.2 A grep hazard in `pmuni0147` — and a rule for the whole repo

**[மூலம் | SOURCE]** The நன்னூல் e-text contains **87 vowel signs in decomposed form**:
`ொ` written as U+0BC6 + U+0BBE rather than as the single U+0BCA, and similarly for `ோ` and `ௌ`.
The other four files checked (`pmuni0016`, `pmuni0300`, `pmuni0301`, `pmuni0100`) are **entirely
precomposed** — 925, 1323, 195 and 2041 such signs respectively, zero decomposed.

**[விளக்கம் | INTERPRETATION] This is not corruption — both forms are valid Unicode and render
identically — but it silently breaks verification.** A quote copied out of `pmuni0147` and typed
back in the normal precomposed way will *look* identical on screen and *fail* a byte-level `grep`
against the file it came from. Worked example from §7.2 of this document: `தொடங்கித்` in
நூற்பா 8 is `…த + U+0BC6 + U+0BBE + ட…` in the source and `…த + U+0BCA + ட…` as any editor will
produce it. Same word, different bytes, no match.

**[முன்மொழிவு | PROPOSAL] The repo's verification practice should normalise before comparing.**
Every Tamil quotation in this document was checked with `unicodedata.normalize('NFC', …)` applied to
both sides, and all of them pass under that rule; a naive `grep` will report false failures on the
நன்னூல் quotes specifically. Two options, and the second is better:

1. Anyone grep-verifying a நன்னூல் quote should normalise both sides first.
2. **Normalise `pmuni0147` to NFC once, in place, and note it in the file header.** It is a
   lossless, reversible transformation, it makes all five files consistent, and it removes a trap
   that will otherwise catch every future session that quotes நன்னூல்.

**[விளக்கம் | INTERPRETATION]** This matters beyond one file. The repo's whole method rests on
"your quotes WILL be grep-verified against the file" — and that guarantee quietly assumes byte
identity between what a source prints and what a person types. **For Tamil, that assumption is
false**, because the script has combining sequences with precomposed equivalents. Any verification
harness the repo builds should normalise. Logging this as a methodological limit, not a textual
one.

---

## 10. ஐயம் | Doubt — what is uncertain here

**Never empty, per [`../../marabu/README.md`](../marabu/README.md).**

- **[திறந்த கேள்வி]** **`வழும்பு`** (நாலடியார் 46). Glossed "ooze / slime." It can also be read as
  marrow, or as greasy matter, and the choice changes how clinical the list sounds. Native ear
  needed.
- **[திறந்த கேள்வி]** **`அத்திட்ட கூறை`** and **`பத்தெட்டு உடைமை`** (நாலடியார் 281). Read as
  "patched cloth" and "eight or ten possessions" — i.e. a *little* property. If `பத்தெட்டு` is
  instead an idiom for *a good deal*, the verse's social range shifts. Uncertain.
- **[திறந்த கேள்வி]** **`அழித்துப் பிறக்கும் பிறப்பு`** (நாலடியார் 302). Read as "the birth one
  wears through and is reborn into." An alternative — "the birth one destroys [by one's acts] and
  takes again" — makes the verse a karma statement rather than a statement about brevity. The two
  give different poems.
- **[திறந்த கேள்வி]** **`கொடுமை`** in இறையனார் நூ. 45–46. "Cruelty done" or "cruelty imputed"?
  Undecidable from the bare நூற்பா; needs the உரை.
- **[திறந்த கேள்வி]** **`அரும்பொருள் ஐந்து`** in நன்னூல்'s சிறப்புப்பாயிரம் (§7.1). If it means
  ஐந்திலக்கணம், the missing பொருளதிகாரம் is a documented non-delivery against a stated commission.
  This is the single highest-value commentary check outstanding.
- **[திறந்த கேள்வி]** **நன்னூல் நூ. 61's arithmetic.** The sutra enumerates the சார்பெழுத்து and
  closes `ஒன்று ஒழி முந்நூற்று எழுபான் என்ப`. **I could not make the enumerated sub-counts sum to
  the stated total, and I have not asserted a parse.** நூ. 59–60 are quoted and used; நூ. 61's
  breakdown is left open. A நன்னூல் commentary will settle it in one line.
- **[திறந்த கேள்வி]** **A discrepancy inside புறப்பொருள் வெண்பாமாலை.** The definition of the
  துறை **ஆர்** (line 2181) speaks of `மறப்போர்ச் செழியன்` — the **Pandya** — but its illustration
  (line 2185) praises `காவிரி நாடன்`, **the Chola**, whose flower ஆத்தி is. Either an e-text fault
  or a genuine textual crux. Not resolved.
- **[திறந்த கேள்வி]** **The third-Sangam duration** (§5.3). The e-text's `ஒண்ணூற்று` is very likely
  a fault for `எண்ணூற்று`. The total of ~9,990 years is reported on that basis and is marked.
- **[திறந்த கேள்வி]** **`ஆலும் வேலும்`** (§2) — not found in any source file. Wording unverified.
- **[கருதுகோள்]** The two falsifiable claims in this document — the within-chapter/between-chapter
  consistency prediction for நாலடியார் (§3.5), and the metrical-variance prediction for
  புறப்பொருள் வெண்பாமாலை (§6.1) — are **hypotheses with declared refutation conditions and no
  results yet.** Neither is a finding.
- **[விளக்கம்]** The whole "the split is the mechanism" reading (§0.1, §7.1) is **interpretation,
  and it is the most load-bearing interpretation here.** The four books' contents are source facts;
  that they constitute a single process of division is my reading. **What would count against it:**
  a post-Tolkappiyam grammar with a full பொருளதிகாரம் written after இறையனார் and புறப்பொருள்
  வெண்பாமாலை were current would weaken it considerably. I do not know whether one exists, and the
  next session should look — this is exactly the kind of claim `murai.md` §10 says to keep at risk
  rather than smooth over.

---

## 11. காதுக்காக | Awaiting the ear — addressed to Ilam

**Nothing below has been heard. Every claim in this list is computed or read off the page.** Per
`murai.md` §8 and the brief's rule 7, they are collected here rather than left embedded.

1. **நாலடியார் 46.** Does the final foot **`ஈர்ங்கோதை யாள்`** land as the shock I claim in §3.1 —
   a love-poem word arriving on top of an anatomy list? Or does it read as neutral to a native ear,
   and the reversal I describe is something I have constructed on the page?
2. **நாலடியார் 123.** Does **`அக்கேபோல்`** (like a shell-bead) actually convey *a hand with the
   fingers gone*? The whole verse rests on that one simile working instantly.
3. **நாலடியார் 302.** Is **`விழித்திமைக்கு மாத்திரை`** cold or gentle? I have read it as cold —
   a life dismissed as a blink. It could be consoling. The verse's entire ethic turns on this and I
   cannot hear the tone.
4. **The register of நாலடியார் against the Kural.** §3 claims நாலடியார் is *harsher* — terror
   where the Kural persuades. Is that audible to you across these four verses, or is it a thematic
   claim I have dressed as a tonal one?
5. **இறையனார் நூ. 22, `அம்பலும் அலரும் களவு`.** Three words. Does it sound like a completed
   sentence in classical Tamil, or does it read as truncated?
6. **புறப்பொருள் வெண்பாமாலை's definition couplets.** They all end in `-அன்று` (`சென்றன்று`,
   `உரைத்தன்று`, `புகழ்ந்தன்று`). Does that ending produce an audible rhythm across 356 of them —
   a drumbeat a student would learn by — or is it flat repetition?
7. **The 361 வெண்பா as one voice.** §6.1 hypothesises they are metrically more uniform than
   நாலடியார்'s 400. **Before I measure it: do they sound like one hand to you?** Your answer first
   would make the measurement a real prediction rather than a description.
8. **நன்னூல் நூ. 19 — `ஆற்று ஒழுக்கு அரிமா நோக்கம் தவளைப் பாய்த்து / பருந்தின் வீழ்வு`.** Four
   images in eleven words. Does the line itself move the way it describes?
9. **நன்னூல் நூ. 40's `செவி வாய் ஆக நெஞ்சு களன் ஆக`** — *ear becoming mouth, mind becoming
   threshing floor*. Is `களன்` here the threshing floor, or the battlefield/arena? Both are live in
   classical usage and they give very different pictures of what listening is.
10. **My எளிய தமிழ் glosses in §3.** Four of them. Have they drifted into translationese?

---

## 12. அடுத்து | Next

**[முன்மொழிவு | PROPOSAL]**

1. **Get a உரை for நன்னூல் into `_src/`** — மயிலைநாதர் or ஆறுமுக நாவலர். It settles §7.1's
   `அரும்பொருள் ஐந்து` question and §10's நூ. 61 arithmetic in two lookups. Highest value per
   effort of anything on this list.
2. **Get the full இறையனார் அகப்பொருள் உரை.** The file in `_src/` holds only `ஓர் பகுதி`, and says
   so. The full commentary contains the 325+ verses of பாண்டிக்கோவை and the citations of eight lost
   works (§5.3) — a survival-bias goldmine for `varalaru/arivu-varalaru.md`.
3. **Repair `pmuni0016`** with the U+0BA2 → ரி rule from §9.1, and record the three unresolved
   faults in the file header rather than silently.
4. **Run the நாலடியார் consistency measurement** (§3.5). 400 verses, already local, and the
   prediction is stated with a refutation condition.
5. **Update two existing files.** [`../../marabu/paadal/003-…`](../marabu/paadal/003-kurunthogai-002-kongu-ther.md)
   §11 gains the இறையனார்-as-grammar-author connection (§5.2);
   [`../../aaivu/mudhal-oli.md`](../aaivu/mudhal-oli.md) §1 gains the குடிநிலை definition that
   sits directly above the `கல் தோன்றி` verse (§6.4), which strengthens its existing honest reading.
6. **Look for the counterexample to §0.1** — a post-Tolkappiyam Tamil grammar with a full
   பொருளதிகாரம். If one exists, this document's central interpretation needs revising, and the
   revision belongs in `aaivu/karuthu/` with the arc preserved.
7. **A marabu entry from நாலடியார்.** Verse 281 or 302 is a real candidate for the aphorism rung of
   the ladder in [`../../marabu/README.md`](../marabu/README.md) — but only with §3's honesty
   about verse 123 carried across, because a child's inheritance should not be handed over
   pre-sanitised.

---

*மூலம்: Project Madurai e-texts `pmuni0016`, `pmuni0100`, `pmuni0147`, `pmuni0300`, `pmuni0301` —
`_src/txt/`. Every Tamil line quoted above is copied verbatim with its line number for grep
verification. Provenance labels follow [`../../murai.md`](../murai.md) §11.*
