# தொல்காப்பியம்: அகத்திணை · புறத்திணை — மூலத்திலிருந்து

**The திணை system read from the நூற்பா, not from the summaries.**

---

## 0. இந்த ஆவணம் | What this is, and how to check it

`../ilakkiyam/sangam.md` §1 describes திணை the way almost every account does: five landscapes, a table of flowers and birds, an inner state per landscape. That description is useful and it is also secondhand. This document goes to the நூற்பா and reports what தொல்காப்பியம் **actually says** — including the places where the famous version is an addition by commentators rather than a statement of the text.

### மூலங்கள் | Sources used

| File | What it is |
|---|---|
| `_src/txt/pmuni0100-tholkappiyam-moolam.txt` | The bare நூற்பா. பொருளதிகாரம் begins line 2154; அகத்திணையியல் lines 2155–2315 (58 numbered நூற்பா); புறத்திணையியல் lines 2316–2546 (30 numbered நூற்பா). |
| `_src/txt/pmuni0500_01-tholkappiyam-porulathikaram-urai-1.txt` | நச்சினார்க்கினியர் உரை on **அகத்திணையியல்** only, numbered 1–55 (14th c. commentary; this printing 1947/1955). |
| `_src/txt/pmuni0500_02-tholkappiyam-porulathikaram-urai-2.txt` | Same commentator on **புறத்திணையியல்**, numbered 56–91 continuing from the previous volume. |
| `_src/txt/pmuni0490_01-ettuthogai-agananuru-p1a.txt` | அகநானூறு 1–60 with சோமசுந்தரனார் உரை — used for the worked example. |

**Citation convention here.** `[அகம் 16]` = நூற்பா numbered 16 in the அகத்திணையியல் of the மூலம் e-text, with the file line number given so any quote can be grep-verified. Where நச்சினார்க்கினியர் divides differently, that is stated.

### எச்சரிக்கை: எண்கள் ஒன்றல்ல | Warning — the numbering is not stable

[மூலம் | SOURCE] The two local editions divide the same text differently, so **நூற்பா numbers do not transfer between them.**

- The மூலம் splits `காரும் மாலையும் முல்லை.` (line 2172, numbered 6) and `குறிஞ்சி, / கூதிர் யாமம் என்மனார் புலவர்.` (2173–2174, numbered 7) into two. நச்சினார்க்கினியர் prints them as one நூற்பா, his no. 6 (urai-1 lines 370–371). The same happens at மூலம் 9 and 10 (`வைகறை விடியல் மருதம்.` / `எற்பாடு, / நெய்தல் ஆதல்…`), which he prints as his no. 8.
- Result: from அகம் 13 onward, **நச்சினார்க்கினியர் = மூலம் − 3**, and his அகத்திணையியல் closes at 55 where the மூலம் closes at 58.
- In புறத்திணையியல் the divergence runs the other way — he *splits* several நூற்பா that the மூலம் prints whole (e.g. `வஞ்சிதானே முல்லையது புறனே` and `எஞ்சா மண் நசை…` are his 61 and 62, but one நூற்பா — no. 6 — in the மூலம்).

[விளக்கம் | INTERPRETATION] This is not a defect in either file. A நூற்பா has no punctuation and no line of its own; where one ends is an editorial judgement, and the judgements have differed for a thousand years. **Any statement of the form "Tolkappiyam sutra 3.1.N says…" is edition-relative.** Cite the words, not the number.

Three further e-text artefacts, noted so they are not mistaken for readings:

1. `கண்டோ ர்` appears with an intrusive space at மூலம் lines 2235, 2259 (and `கண்டோ ற்` at 2244). Almost certainly an OCR/proofing artefact for `கண்டோர்`. **Grep for `கண்டோ ர்` with the space, or the match will fail.**
2. மூலம் line 2510 reads `மெய்ப் பெயர் மருங்கின் வைத்தனர் வழியே.26` — the number 26 is fused to the text without the tab that separates every other நூற்பா number in the file.
3. Real textual variants exist between the two editions, e.g. புறம் 4 (மூலம் line 2331) reads `மறம் கடைக்கூட்டிய குடிநிலை சிறந்த`, while நச்சினார்க்கினியர் reads **துடிநிலை** and glosses it as the war-drum that goads the warriors' valour on the field (urai-2 lines 366–370). குடி (clan) and துடி (drum) are one letter apart and give quite different senses. [திறந்த கேள்வி | OPEN QUESTION] Which is prior is not decidable from these two files.

---

## 1. ஏழு அகத்திணை — the seven, and why the order is the argument

### 1.1 The நூற்பா

> கைக்கிளை முதலாப் பெருந்திணை இறுவாய்
> முற்படக் கிளந்த எழு திணை என்ப.

[மூலம் | SOURCE: `pmuni0100-tholkappiyam-moolam.txt` lines 2156–2157, அகம் 1 — the first நூற்பா of பொருளதிகாரம்.]

**சொல்லுக்குச் சொல்:**

| சொல் | பொருள் |
|---|---|
| கைக்கிளை முதலா | with கைக்கிளை as the first |
| பெருந்திணை இறுவாய் | having பெருந்திணை as the last / terminus |
| முற்படக் கிளந்த | stated in the earlier place (i.e. the ones spoken of first) |
| எழு திணை என்ப | are seven திணை, they say |

**பொருள்:** Beginning with கைக்கிளை and ending with பெருந்திணை — these, spoken of first, are the **seven** திணை.

The very first line of the book on content does not say five. It says seven, and it names the seven by naming only the two endpoints. The five in between are then produced by the second நூற்பா:

> அவற்றுள்,
> நடுவண் ஐந்திணை நடுவணது ஒழிய
> படு திரை வையம் பாத்திய பண்பே.

[மூலம் | SOURCE: மூலம் lines 2158–2160, அகம் 2.]

**பொருள்:** Among those — the **middle five திணை**, the middlemost of them excepted, are the manner in which the sea-girt world was apportioned.

[விளக்கம் | INTERPRETATION] Two நூற்பா, thirty-odd words, and the whole architecture is up: seven states of love, of which five occupy the middle; of those five, four received land and the middlemost did not. The word `ஐந்திணை` — "the five" — occurs in the மூலம் of the whole பொருளதிகாரம் **only three times, and never on its own**: `நடுவண் ஐந்திணை` (2159), `மக்கள் நுதலிய அகன் ஐந்திணையும்` (2311), and `அன்பொடு புணர்ந்த ஐந்திணை மருங்கின்` (2549, களவியல்). It is always *the middle five*, *the wide five*, *the five joined with love* — never "the Five" as the name of the system. The habit of calling the whole thing ஐந்திணை is later.

### 1.2 கைக்கிளை — what the text actually says

> காமம் சாலா இளமையோள்வயின்
> ஏமம் சாலா இடும்பை எய்தி
> நன்மையும் தீமையும் என்று இரு திறத்தான்
> தன்னொடும் அவளொடும் தருக்கிய புணர்த்து
> சொல் எதிர் பெறாஅன் சொல்லி இன்புறல்
> புல்லித் தோன்றும் கைக்கிளைக் குறிப்பே.

[மூலம் | SOURCE: மூலம் lines 2296–2301, அகம் 53. Same நூற்பா at urai-1 lines 3050–3055 as நச். 50.]

**பொருள் (line by line):** Toward a girl **not yet ripe for love** (`காமம் சாலா இளமையோள்`); having come to a grief that has **no refuge in it** (`ஏமம் சாலா இடும்பை`); by the two sides of *good* and *ill* — heaping speech upon himself and upon her; **receiving no word in answer** (`சொல் எதிர் பெறாஅன்`), and taking pleasure in the speaking itself — that, appearing thus, is the mark of கைக்கிளை.

[மூலம் | SOURCE — commentary] Naccinārkkiniyar's gloss (urai-1 line 112): `கைக்கிளை யென்பது ஒருமருங்கு பற்றிய கேண்மை… எனவே, ஒருதலைக் காமமாயிற்று` — *kaikkilai is attachment held from one side only; hence, one-sided love.* He reads `நன்மையும் தீமையும்` as: the man ascribes the *good* to himself (he did no harm) and the *ill* to her (she and hers wronged him) — urai-1 line 3058.

**Three things the நூற்பா encodes that summaries drop:**

1. It is not merely "unrequited love." The defining formal fact is `சொல் எதிர் பெறாஅன்` — **the poem has no second voice.** In a system whose whole business is who speaks to whom, kaikkilai is the case where the answering கூற்று does not exist.
2. The pleasure is in the speaking (`சொல்லி இன்புறல்`), not in the beloved. That is a statement about the poetics, not about the man.
3. `காமம் சாலா இளமையோள்` places it at the *unripe* end of a maturity scale — which is why it stands first.

### 1.3 பெருந்திணை — what the text actually says

> ஏறிய மடல் திறம் இளமை தீர் திறம்
> தேறுதல் ஒழிந்த காமத்து மிகு திறம்
> மிக்க காமத்து மிடலொடு தொகைஇ
> செப்பிய நான்கும் பெருந்திணைக் குறிப்பே.

[மூலம் | SOURCE: மூலம் lines 2302–2305, அகம் 54.]

**Four things, not one:**

| திறம் | The நூற்பா's word | நச். gloss (urai-1 lines 3104–3105) |
|---|---|---|
| ஏறிய மடல் திறம் | actually mounting the மடல் | not merely *threatening* to ride it (that is kaikkilai) but doing it; he extends it to வரைபாய்தல் (leaping from a height) |
| இளமை தீர் திறம் | youth being past | the woman not younger than him but of equal/advanced age; and both being past youth yet still in காமம் rather than turning to renunciation |
| தேறுதல் ஒழிந்த காமத்து மிகு திறம் | love beyond all steadying | he reads it against the மெய்ப்பாடு scale as the stage where judgement is gone |
| மிக்க காமத்து மிடல் | force in excessive love | union taken by strength upon encounter |

[விளக்கம் | INTERPRETATION] பெருந்திணை is not "the love of low people," which is how it is often paraphrased. On the face of the நூற்பா it is a **scale term**: love that has exceeded its proper measure — in publicity (the மடல்), in season (age), in judgement, in force. Its opposite number, கைக்கிளை, is love that has not yet reached measure. The five in between are love *in* measure.

### 1.4 Why the ordering is itself a claim

[விளக்கம் | INTERPRETATION, grounded in மூலம் அகம் 1–2, 53–55 and urai-1 lines 112–113]

Lay the seven out as the text orders them:

```
கைக்கிளை  →  [ குறிஞ்சி · முல்லை · மருதம் · நெய்தல் · பாலை ]  →  பெருந்திணை
  unripe            the five that were given the world              overripe
  no answer                                                          no restraint
```

The order is a **single graded axis: the fit between desire and its proper form.** The two ends are the two ways the fit fails — too early, and too much. நச்சினார்க்கினியர் gives exactly this reason for putting kaikkilai first (urai-1 line 113): `காமஞ் சாலா விளமைப்பருவம் அதன்கண்ண தாகலானுங் கைக்கிளையை முற்கூறினார்` — *because the age not yet ripe for love belongs to it, they stated kaikkilai first.* And for பெருந்திணை last: `எல்லாவற்றினும் பெரிதாகிய திணையாதலிற் பெருந்திணையாயிற்று` — *it is the திணை larger than all the rest, hence "the great திணை"* — with the further reason that of the eight forms of union, the first six திணை share four between them while பெருந்திணை alone carries the other four.

[கருதுகோள் | HYPOTHESIS — falsifiable] If the seven are a graded scale rather than a list of five plus two appendices, then a நூற்பா should exist that lets the outer two *behave differently in kind* from the five. It does. அகம் 15 (மூலம் line 2187):

> உரிப்பொருள் அல்லன மயங்கவும் பெறுமே.

நச்சினார்க்கினியர் (urai-1 line 888) reads `உரிப்பொருள் அல்லன` as precisely **kaikkilai and perunthinai** — *the ones that are not உரிப்பொருள்* — and says they may mix into all four lands without restriction. So the outer two are exempt from the landscape machinery entirely. That is what "not one of the five" means structurally.

### 1.5 A detail that reverses the usual picture

> முன்னைய நான்கும் முன்னதற்கு என்ப.

[மூலம் | SOURCE: மூலம் line 2306, அகம் 55.]

*The earlier four belong to the earlier one.* நச்சினார்க்கினியர் (urai-1 lines 3180–3182): the four moments that precede இயற்கைப் புணர்ச்சி — `காட்சி` (the sight), `ஐயம்` (the doubt), `தெரிதல்` (the discerning), `தேறல்` (the settling) — belong to **கைக்கிளை**.

[விளக்கம் | INTERPRETATION] Read plainly: the opening of *every* love — before there is any answering word — is structurally kaikkilai. The "discarded" திணை is not a marginal case bolted on at the edge. It is the first four beats of the ordinary story. The popular five-item list does not have a slot for the interval before the beloved has answered, and the reason is that Tolkappiyam put that interval outside the five on purpose.

---

## 2. முதல் · கரு · உரி — the actual machinery

### 2.1 The நூற்பா

> முதல் கரு உரிப்பொருள் என்ற மூன்றே
> நுவலும் காலை முறை சிறந்தனவே
> பாடலுள் பயின்றவை நாடும் காலை.

[மூலம் | SOURCE: மூலம் lines 2161–2163, அகம் 3.]

**சொல்லுக்குச் சொல்:**

| சொல் | பொருள் |
|---|---|
| முதல் | the first / the ground — *land and time* |
| கரு | the germ / the native stock — *what lives there* |
| உரிப்பொருள் | the owned matter — *the phase of love that is this திணை's own* |
| நுவலும் காலை | at the time of telling (i.e. in composition) |
| முறை சிறந்தன | are, in order, ascending in rank |
| பாடலுள் பயின்றவை நாடும் காலை | when one investigates what is practised in the poems |

**A terminological note that matters.** The நூற்பா says `முதல் கரு உரிப்பொருள்`. The compounds **முதற்பொருள்** and **கருப்பொருள்** appear **nowhere in the மூலம் of the whole பொருளதிகாரம்** — only `உரிப்பொருள்` (lines 2161, 2187, 2190) does. The symmetrical three-name set every textbook uses is commentary vocabulary laid over a text that names only the third member with `-பொருள்`. [மூலம் | SOURCE: verified by grep over `pmuni0100-tholkappiyam-moolam.txt`.]

### 2.2 The two rules hidden in the last two lines

Most accounts quote this நூற்பா for the list of three and stop. The list is the least of it.

**(a) `நுவலும் காலை முறை சிறந்தனவே` — the layers are ranked, not parallel.**

நச்சினார்க்கினியர் (urai-1 line 142): `முதலிற் கருவும், கருவில் உரிப்பொருளுஞ் சிறந்துவரும்` — *கரு outranks முதல், and உரிப்பொருள் outranks கரு.* This is not a taxonomy of three equal slots. It is a **priority order for composition**: the land and hour are the floor; what grows and moves there is worth more; the phase of love is worth most. He then demonstrates it with a graded sequence of real poems (urai-1 lines 151–288):

| What is present | Example he cites | His verdict |
|---|---|---|
| முதல் + கரு + உரி | அகநானூறு 4 (முல்லை), 218 (குறிஞ்சி), 1 (பாலை), 46 (மருதம்), 40 (நெய்தல்) | `முதலுங் கருவும் வந்து உரிப்பொருளாற் சிறப்பெய்தி முடிந்தது` — the first two come, and it is *completed by* the உரிப்பொருள் |
| கரு + உரி, no முதல் | a முல்லை piece, a குறிஞ்சி piece | `இது முதற்பொருளின்றி வந்த முல்லை` |
| உரி only | a பாலை piece; a மருதம் piece | `இஃது உரிப்பொருளொன்றுமே வந்த பாலை` |
| முதல் + கரு, no உரி | — | *does not occur* |

His conclusion, urai-1 line 287: `உரிப்பொருளின்றேற் பொருட் பய‌னின் றென்பது பெற்றாம்` — **without the உரிப்பொருள் there is no yield of meaning at all** — and therefore `முதல் கரு வுரிப்பொருள் கொண்டே வருவது திணையாயிற்று`.

[விளக்கம் | INTERPRETATION] So the three layers are **not** three coordinates. Two are droppable and one is not. A poem can be a முல்லை poem with no forest and no rain in it, purely because it is about waiting. The landscape is the *carrier* of the state; the state is the திணை. `sangam.md` §1's table — "குறிஞ்சி · mountain · union" — reads the mapping as though all three columns were equally constitutive. They are not, and the commentary is explicit about which one is load-bearing.

**(b) `பாடலுள் பயின்றவை நாடும் காலை` — the method clause.**

நச்சினார்க்கினியர் (urai-1 line 142): `நாடுங் காலை யெனவே புலனெறிவழக்கிற் பயின்றவாற்றான் இம்மூன்றனையும் வரையறுத்துக் கூறுவதன்றி வழக்குநோக்கி இலக் கணங் கூறப்படாதென்பதூவும் பெறுதும்` — *because he says "when one investigates," these three are delimited from what is actually practised in the poems; a grammar is not stated apart from usage.*

[விளக்கம் | INTERPRETATION] This is a descriptive-grammar clause, and it is inside the நூற்பா, not in the commentary. Tolkappiyam is telling the reader that the three-layer scheme is an **abstraction from a corpus**, arrived at by inspecting `பாடலுள் பயின்றவை` — what recurs in the poems. That is worth pausing on: a text usually presented as a prescriptive rulebook opens its analytic apparatus with the statement that the categories were derived, not decreed.

### 2.3 Layer one — முதல்

> முதல் எனப்படுவது நிலம் பொழுது இரண்டின்
> இயல்பு என மொழிப இயல்பு உணர்ந்தோரே.

[மூலம் | SOURCE: மூலம் lines 2164–2165, அகம் 4.] *What is called முதல் is the nature of the two — land and time — so say those who have grasped the nature of things.*

And, later, the closing tally: `முதல் எனப்படுவது ஆயிரு வகைத்தே.` [மூலம் line 2194, அகம் 19] — *what is called முதல் is of those two kinds.*

The word `இயல்பு` (nature, the given) does real work. நச்சினார்க்கினியர் (urai-1 line 296): `இயற்கையெனவே செயற்கை நிலனுஞ் செயற்கைப் பொழுதும் உளவாயிற்று` — *by saying "natural," a made land and a made time are thereby implied.* The natural four are the ones apportioned in அகம் 2; a garden, a lamp-lit night, an artificial season are `செயற்கை`. The category admits its own exceptions in the same breath that it defines itself.

### 2.4 Layer two — கரு

> தெய்வம் உணாவே மா மரம் புள் பறை
> செய்தி யாழின் பகுதியொடு தொகைஇ
> அவ் வகை பிறவும் கரு என மொழிப.

[மூலம் | SOURCE: மூலம் lines 2195–2197, அகம் 20.]

**The eight the நூற்பா names:**

| # | சொல் | Gloss |
|---|---|---|
| 1 | தெய்வம் | the god |
| 2 | உணா | the food |
| 3 | மா | the beast |
| 4 | மரம் | the tree |
| 5 | புள் | the bird |
| 6 | பறை | the drum |
| 7 | செய்தி | the work / the doing |
| 8 | யாழின் பகுதி | the class of யாழ் (the tuning) |

**…and then `அவ் வகை பிறவும்` — "and others of that kind."** The list is explicitly open.

**Two findings here that matter.**

**(i) பூ — the flower — is not in the நூற்பா's list.** The single most famous fact about திணை (kurinji flower, mullai flower, neydal flower — the landscapes are *named after flowers*) is not stated in the நூற்பா that enumerates கரு. நச்சினார்க்கினியர் knows this and says so plainly (urai-1 line 1181): `பூவைக் கருவென ஓதிற்றிலரேனும் முற்கூறிய மரத்திற்குச் சினையாய் அடங்கிற்று` — *though they did not state the flower as கரு, it is subsumed as a part (சினை) of the tree stated earlier.* The flower enters through a subsumption argument by a commentator twelve or more centuries later.

**(ii) The famous per-landscape table is உரை, not நூற்பா.** The நூற்பா gives eight *categories* and stops. The filled-in table — kurinji: ஐவனநெல் and தினை for food, tiger and elephant and bear for beast, akil and sandal and teak for tree, parrot and peacock for bird, முருகியம் and தொண்டகப்பறை for drum, honey-taking and tuber-digging and millet-guarding and parrot-scaring for work, குறிஞ்சியாழ் for tuning, and (via `பிறவும்`) kaanthal and vengai for flower, waterfall and spring for water, சிறுகுடி and குறிச்சி for settlement — is **Naccinārkkiniyar's**, given landscape by landscape at urai-1 lines 1164–1170. He supplies the same for முல்லை, மருதம், நெய்தல், and பாலை.

[விளக்கம் | INTERPRETATION] This is the single largest gap between "Tolkappiyam's திணை system" as popularly described and Tolkappiyam. The **grid** — the thing that makes the system feel like a code-book — is a commentator's completion of an open-ended category list. The நூற்பா supplies the *slots*; a millennium of உரை supplied the *values*. That does not make the values wrong (they are drawn from the same poems the நூற்பா abstracts from), but it does mean that when a table of thirty cells is attributed to Tolkappiyam, twenty-nine of them are being attributed wrongly.

**And the நூற்பா immediately loosens even the slots:**

> எந் நில மருங்கின் பூவும் புள்ளும்
> அந் நிலம் பொழுதொடு வாரா ஆயினும்
> வந்த நிலத்தின் பயத்த ஆகும்.

[மூலம் | SOURCE: மூலம் lines 2198–2200, அகம் 21.] *Even if the flowers and birds of whatever land do not come with that land and its time, they take the yield of the land they came into.*

A peacock in a wasteland poem does not make it a mountain poem. **It becomes a wasteland peacock.** The system is not a lookup table with error states; it is a set of defaults with a documented override rule. Naccinārkkiniyar's example (urai-1 lines 1191–1195) is a கலித்தொகை piece where a mountain peacock arrives in a பாலை setting in the early-hot season, so that bird *and* season mix at once.

Note also that this நூற்பா names `பூ` — the flower — even though the enumerating நூற்பா did not. The text is not tidy, and pretending otherwise is how the tidy table got built.

### 2.5 Layer three — உரிப்பொருள்

> புணர்தல் பிரிதல் இருத்தல் இரங்கல்
> ஊடல் அவற்றின் நிமித்தம் என்றிவை
> தேரும் காலை திணைக்கு உரிப்பொருளே.

[மூலம் | SOURCE: மூலம் lines 2188–2190, அகம் 16.]

| சொல் | பொருள் |
|---|---|
| புணர்தல் | union |
| பிரிதல் | separating — the act of going |
| இருத்தல் | remaining — the waiting |
| இரங்கல் | grieving |
| ஊடல் | the lovers' quarrel, the sulk |
| அவற்றின் நிமித்தம் | **and the occasions of those** |

**A sixth item that is usually not counted.** `அவற்றின் நிமித்தம்` is part of the list, not a coda. The உரிப்பொருள் includes not only the five states but the *causes that bring them on*. That is why the iyal spends நூற்பா 27–38 on the taxonomy of `பிரிவு` — the reasons a man may leave — and why அகம் 46 (மூலம் line 2285) can say `நிகழ்ந்தது நினைத்தற்கு ஏதுவும் ஆகும்`: *what happened before becomes the cause of remembering later.* Causation is inside the poetic category.

**The finding that most needs saying.** [கருதுகோள் | HYPOTHESIS — I put it at risk, and it survived the check]

**அகத்திணையியல் never pairs a landscape with its உரிப்பொருள்.** (My statement, not a quotation.)

Grep the whole அகத்திணையியல் of the மூலம் (lines 2156–2314) for the five landscape names. They occur in exactly six lines: 2170 (the naming list), 2172, 2173, 2176, 2178 (the பொழுது நூற்பா), and 2217 (`முல்லை முதலாச் சொல்லிய முறையான்`, about the ordering of separations). The உரிப்பொருள் list occurs once, at 2188–2190, **attached to nothing.** There is no நூற்பா in this iyal that says குறிஞ்சி is union, or மருதம் is the quarrel.

The mapping everyone knows —

| திணை | உரிப்பொருள் |
|---|---|
| குறிஞ்சி | புணர்தல் |
| பாலை | பிரிதல் |
| முல்லை | இருத்தல் |
| நெய்தல் | இரங்கல் |
| மருதம் | ஊடல் |

— is **not stated in the நூற்பா of அகத்திணையியல்.** நச்சினார்க்கினியர் treats it as already known and reasons *from* it: at urai-1 line 377 he explains why கார் and மாலை belong to முல்லை by appeal to `முல்லைப் பொருளாகிய மீட்சி` (mullai's matter, the return) and the heroine's `இருத்தல்`. He does not derive it; he assumes it. [திறந்த கேள்வி | OPEN QUESTION] Whether the pairing is derivable from a நூற்பா elsewhere in பொருளதிகாரம் (களவியல் / கற்பியல் / பொருளியல்), or whether it is a tradition the நூற்பா presuppose without stating, I have not settled here. It should be settled — it is the most-repeated single claim about Tamil poetics.

### 2.6 The slack in the system

> திணை மயக்குறுதலும் கடி நிலை இலவே
> நிலன் ஒருங்கு மயங்குதல் இல என மொழிப
> புலன் நன்கு உணர்ந்த புலமையோரே.

[மூலம் | SOURCE: மூலம் lines 2184–2186, அகம் 14.] *That திணை should mix is not forbidden; that lands should mix wholesale is not [permitted] — so say those who have grasped the field well.*

[விளக்கம் | INTERPRETATION] The rule is asymmetric and precise. **States may blend; grounds may not.** A poem may carry more than one phase of love; it may not be set in two landscapes at once. Naccinārkkiniyar's reading (urai-1 line 639 ff.) is that the strict `நிரல்நிறை` mapping of one ஒழுக்கம் to one நிலம் laid down in அகம் 5 is a default, not a fence.

Followed immediately by அகம் 15 (`உரிப்பொருள் அல்லன மயங்கவும் பெறுமே`), which exempts the outer two from even that, and by அகம் 17–18 on how கொண்டு தலைக்கழிதல் and பிரிந்து இரங்கல் can co-occur in one place. **Three consecutive நூற்பா are about permitted exceptions.** A system whose fourth-largest topic is its own override conditions is not a rigid code.

### 2.7 ஒரு பாடல், மூன்று அடுக்கு | One poem, all three layers

**அகநானூறு 4** — chosen because நச்சினார்க்கினியர் himself uses it (urai-1 lines 152–169) as his first demonstration of `முறை சிறந்தன`, and the சோமசுந்தரனார் edition notes that he did (`pmuni0490_01`, line 422).

**Colophon, from the edition** [மூலம் | SOURCE: `pmuni0490_01-ettuthogai-agananuru-p1a.txt` lines 418–420, 440]:
`செய்யுள் 4` · `திணை:முல்லை` · `துறை:தோழி தலைமகளைப் பருவங்காட்டி வற்புறுத்தியது` · poet **குறுங்குடி மருதனார்**

**மூலம், opening seven lines** [SOURCE: same file, lines 423–429]:

> முல்லை வைந்நுனை தோன்ற வில்லமொடு
> பைங்காற் கொன்றை மென்பிணி யவிழ
> விரும்புதிரித் தன்ன மாயிரு மருப்பிற்
> பரலவ லடைய விரலை தெறிப்ப
> மலர்ந்த ஞாலம் புலம்புபுறக் கொடுப்பக்
> கருவி வானங் கதழுறை சிதறிக்
> கார்செய் தன்றே கவின்பெறு கானங்

**and the close** [SOURCE: same file, lines 435–439]:

> னுவக்காண் டோன்றுங் குறும்பொறை நாடன்
> கறங்கிசை விழவி னுறந்தைக் குணாது
> நெடும்பெருங் குன்றத் தமன்ற காந்தட்
> போதவி ழலரி னாறு
> மாய்தொடி யரிவைநின் மாணலம் படர்ந்தே.

**பொழிப்பு (drawing on the சோமசுந்தரனார் உரை at lines 443–449):** The mullai buds show their sharp points; on the illam and the green-stemmed konrai the soft knots come undone; stags with black horns like twisted iron drop down to the pebbled hollows; over the wide world the parching grief turns its back and goes; the thunder-massed sky scatters its hurrying drops — **the rains have made the season**, and the forest takes its beauty. And he of the low-hill country will appear — *there*, look — his chariot's bell muffled with cloth lest he startle the pollen-feeding birds roosting in pairs on the flowering bough; he who is fragrant as the opening kaanthal on the great hill east of Urandhai of the loud festivals — coming, O woman of the chosen bangles, drawn by your beauty.

**The three layers, marked on this poem:**

| அடுக்கு | In this poem | Where the நூற்பா licenses it |
|---|---|---|
| **முதல்** — நிலம் | `கானம்` — the forest tract | அகம் 5: `மாயோன் மேய காடு உறை உலகமும் … முல்லை` |
| **முதல்** — பொழுது | `கார்செய் தன்றே` — the rains have made the season | அகம் 6: `காரும் மாலையும் முல்லை.` |
| **கரு** — மரம் | `இல்லம்`, `பைங்காற் கொன்றை` | அகம் 20: `மரம்` |
| **கரு** — மா | `இரலை` (the stag) | அகம் 20: `மா` |
| **கரு** — புள் | `தாதுண் பறவை` (line 433) | அகம் 20: `புள்` |
| **கரு** — பூ (via `பிறவும்`) | `முல்லை வைந்நுனை` | not in அகம் 20's list; enters by நச்.'s சினை argument, and by அகம் 21 |
| **கரு** — crossing in | `காந்தள்` — a குறிஞ்சி flower, on a hill, used as the simile for his fragrance | **அகம் 21** — a flower out of its land takes the yield of the land it comes into |
| **உரிப்பொருள்** | `இருத்தல்` — she is waiting; he is not yet here, only about to be | அகம் 16: `இருத்தல்` |

**நுட்பம்.** Watch the machine work. Seven lines of pure முதல் + கரு — not one word about the woman, not one word about love. Then `உவக்காண்` — *there, look* — and the whole apparatus discharges into a single act: the friend is **pointing at the season as evidence that he is coming**. The colophon says exactly this: `தோழி தலைமகளைப் பருவங்காட்டி வற்புறுத்தியது` — *the friend strengthened the heroine by showing her the season.* The rain is not scenery. It is the argument. He said he would return at the rains; the rains are here; therefore. Naccinārkkiniyar's one-line verdict (urai-1 line 169): `இது குறித்த காலம் வந்தது, அவரும் வந்தாரென ஆற்றுவித்தது` — *the appointed time has come; she is consoled with "he too has come."*

And note what `உரிப்பொருளாற் சிறப்பெய்தி முடிந்தது` means concretely: strip the forest and the stag and the konrai and you still have a woman being told to hold on. Strip the holding-on and you have a weather report.

---

## 3. நிலம் and பொழுது — the full table from source

### 3.1 நிலம் — the four lands, named by their gods first

> மாயோன் மேய காடு உறை உலகமும்
> சேயோன் மேய மை வரை உலகமும்
> வேந்தன் மேய தீம் புனல் உலகமும்
> வருணன் மேய பெரு மணல் உலகமும்
> முல்லை குறிஞ்சி மருதம் நெய்தல் எனச்
> சொல்லிய முறையான் சொல்லவும் படுமே.

[மூலம் | SOURCE: மூலம் lines 2166–2171, அகம் 5.]

This is a `நிரல்நிறை` — a parallel-ordered construction. Read the two lists down the same column:

| God | World | Landscape name | நச். gloss (urai-1 line 308) |
|---|---|---|---|
| மாயோன் | காடு உறை உலகம் — the forest-dwelt world | **முல்லை** | `கடல்வண்ணன் காதலித்த காடுறையுலகமுஞ்` — the sea-hued one's beloved forest world |
| சேயோன் | மை வரை உலகம் — the dark-mountain world | **குறிஞ்சி** | `செங்கேழ் முருகன் காதலித்த வான் தங்கிய வரைசுழுலகமும்` — red-hued Murugan's sky-holding hills |
| வேந்தன் | தீம் புனல் உலகம் — the sweet-water world | **மருதம்** | `இந்திரன் காதலித்த தண்புன னாடுங்` — Indra's cool-watered country |
| வருணன் | பெரு மணல் உலகம் — the great-sand world | **நெய்தல்** | `கருங்கடற் கடவுள் காதலித்த நெடுங்கோட்டெக்கர் நிலனும்` — the dark-sea god's long dune-ridge land |

**Three observations from the text.**

1. **The lands are named by their gods before they are named by their names.** Four full lines of `X மேய Y உலகம்` come first; the landscape names arrive only in line five, as an afterthought clause — `எனச் சொல்லிய முறையான் சொல்லவும் படுமே`, *may also be spoken of in the order stated.* The primary identification of a Tamil landscape in this நூற்பா is **whose it is**, not what grows there.
2. **The order is முல்லை first, not குறிஞ்சி.** Every popular listing runs குறிஞ்சி முல்லை மருதம் நெய்தல் பாலை. The நூற்பா runs **முல்லை குறிஞ்சி மருதம் நெய்தல்**, and the following பொழுது நூற்பா keep that same order (6: முல்லை, 7: குறிஞ்சி, 9: மருதம், 10: நெய்தல், 11: பாலை). So does அகம் 30, `முல்லை முதலாச் சொல்லிய முறையான்` — *in the order stated beginning with mullai*. [திறந்த கேள்வி | OPEN QUESTION] Why the reordering happened, and whether the received order carries an argument of its own (a developmental one — mountain-dwellers first, as this edition's முன்னுரை assumes at line 85), is not decidable from these files.
3. `சொல்லவும் படுமே` — the `-உம்` is read by Naccinārkkiniyar's as `எதிர்மறை` (urai-1 line 310): the lands *may also* be named in some other order. The நூற்பா licenses its own violation in its last word.

**And note the deity list itself.** `வேந்தன்` is glossed as Indra, `வருணன` is Varuna. [விளக்கம் | INTERPRETATION] Two of the four land-gods in the founding statement of the Tamil landscape system carry Sanskritic identifications in the commentary tradition — a fact worth holding beside §6 and §8 of `../varalaru/arivu-varalaru.md` on how much of "what Tamil says" is what Tamil's commentators said.

### 3.2 பொழுது — season and hour, நூற்பா by நூற்பா

| # | நூற்பா (verbatim from மூலம்) | Line | What it assigns |
|---|---|---|---|
| 6 | `காரும் மாலையும் முல்லை.` | 2172 | முல்லை ← கார் (rains) + மாலை (evening) |
| 7 | `குறிஞ்சி,` / `கூதிர் யாமம் என்மனார் புலவர்.` | 2173–4 | குறிஞ்சி ← கூதிர் (cold) + யாமம' (deep night) |
| 8 | `பனி எதிர் பருவமும் உரித்து என மொழிப.` | 2175 | குறிஞ்சி also ← the season that meets பனி |
| 9 | `வைகறை விடியல் மருதம்.` | 2176 | மருதம் ← வைகறை + விடியல் (last watch, first light) |
| 10 | `எற்பாடு,` / `நெய்தல் ஆதல் மெய் பெறத் தோன்றும்.` | 2177–8 | நெய்தல் ← எற்பாடு (sun-fall, late afternoon) |
| 11 | `நடுவுநிலைத் திணையே நண்பகல் வேனிலொடு` / `முடிவு நிலை மருங்கின் முன்னிய நெறித்தே.` | 2179–80 | பாலை ← நண்பகல் (high noon) + வேனில் (heat) |
| 12 | `பின்பனிதானும் உரித்து என மொழிப.` | 2181 | பாலை also ← பின்பனி (late dew/frost) |

**The assembled table.** [மூலம் for the assignments; the two-tier vocabulary is commentary — see below.]

| திணை | பெரும்பொழுது (season) | சிறுபொழுது (hour) |
|---|---|---|
| **முல்லை** | கார் — the rains (roughly ஆவணி–புரட்டாசி; நச். at urai-1 line 377) | **மாலை** — evening |
| **குறிஞ்சி** | கூதிர் — the cold; **and முன்பனி** | **யாமம்** — midnight watch |
| **மருதம்** | *none assigned* | **வைகறை · விடியல்** — the last watch and first light |
| **நெய்தல்** | *none assigned* | **எற்பாடு** — sun-fall |
| **பாலை** | வேனில் — the heat (நச். reads both இளவேனில் and முதுவேனில்); **and பின்பனி** | **நண்பகல்** — high noon |

**Four things this table shows that the usual one does not.**

**(i) The words பெரும்பொழுது and சிறுபொழுது do not occur in the மூலம்.** Not once, in the entire file. [மூலம் | SOURCE: grep over `pmuni0100-tholkappiyam-moolam.txt` returns zero hits for both.] They occur throughout Naccinārkkiniyar's (five occurrences in urai-1 alone, from line 372 on). The நூற்பா simply juxtapose a season-word and an hour-word — `காரும் மாலையும்` — and leave the reader to know which is which. **The two-tier scheme is a commentator's formalisation of an unstated distinction.**

**(ii) மருதம் and நெய்தல் are given no season at all.** This is not an omission I am inferring; நச்சினார்க்கினியர் says it explicitly and repeatedly. At urai-1 line 512, on the two lands that get only hours: `இதன் பயன் இவ்விரண்டு நிலத்துக்கு மற்றை மூன்று காலமும் பெரும்பான்மை வாராதென்றலாம்`. And in the puram volume, twice, using the pairing to explain why a war-திணை matches a love-திணை: of உழிஞை/மருதம், `மருதம்போல் இதற்கும் பெரும்பொழுது வரைவின்மையானுஞ்` — *because for this too, as for marutham, there is no restriction of season* (urai-2 line 1309); of தும்பை/நெய்தல், `பெரும் பொழுது வரைவின்மையானும்` (urai-2 line 1772). **Three of the five landscapes are timed; two are only clocked.**

**(iii) The six seasons are not evenly distributed.** Of the six பெரும்பொழுது (கார், கூதிர், முன்பனி, பின்பனி, இளவேனில், முதுவேனில்), முல்லை takes one, குறிஞ்சி takes two, பாலை takes three — and the other two landscapes take none. `பனி எதிர் பருவமும்` is read by நச். as முன்பனி on the grammar of `எதிர்தலென்பது முன்னாதல்`, *to meet is to precede* (urai-1 line 427).

**(iv) The hour-cycle is a complete partition; the season-cycle is not.** நச்சினார்க்கினியர் lays out the six சிறுபொழுது in order (urai-1 line 374): மாலை → இடையாமம் → விடியல் → காலை → நண்பகல் → எற்பாடு, `அவை ஒரோவொன்று பத்து நாழிகையாக` — ten நாழிகை each, the day cut into six. Of those six the நூற்பா assign five (மாலை, யாமம், வைகறை/விடியல், நண்பகல், எற்பாடு) and leave **காலை** — mid-morning — unassigned to any திணை.

[திறந்த கேள்வி | OPEN QUESTION] Why காலை alone gets no திணை. நச்சினார்க்கினியர் notes the sequence but I do not find him addressing the gap in the அகத்திணையியல் commentary. It is a real hole in an otherwise complete partition and it is not usually remarked on.

**One variant to record.** மூலம் 9 reads `வைகறை விடியல் மருதம்.` நச்சினார்க்கினியர் reads `வைகுறு விடியன் மருதம்` and explicitly discusses the variant (urai-1 line 441): `கங்குல் வைகிய அறுதியாதனோக்கி வைகறை யெனவுங் கூறுப. அதுவும் பாடம்` — *reckoning from the end of the night's passing it is also called வைகறை; that too is a reading.* Both readings were live in the fourteenth century.

---

## 4. பாலை — the திணை with no land

### 4.1 What the text says

**(a) It was excluded from the apportioning.**

> நடுவண் ஐந்திணை நடுவணது ஒழிய
> படு திரை வையம் பாத்திய பண்பே.

[மூலம் | SOURCE: மூலம் lines 2159–2160, அகம் 2.]

Naccinārkkiniyar's paraphrase (urai-1 line 120) is unambiguous: `நடுவணது ஒழிய- நடுவணதாகிய பாலையை அவ்வுலகம் பெறாதே நிற்கும்படியாகச் செய்தார்` — *"the middlemost excepted" means: he so arranged it that the world does not receive பாலை.* At line 122 he expands: when the world was made as forest, mountain, farmland, and shore, the four were given four of the five ஒழுக்கம், `பாலை யொழிந்தனவற்றை` — all but பாலை.

**(b) But it *was* given a time.**

> நடுவுநிலைத் திணையே நண்பகல் வேனிலொடு
> முடிவு நிலை மருங்கின் முன்னிய நெறித்தே.

[மூலம் | SOURCE: மூலம் lines 2179–2180, அகம் 11.] Plus அகம் 12, `பின்பனிதானும் உரித்து என மொழிப.`

**So the answer to "does பாலை have its own land?" is, from the நூற்பா: no — and it is the only one of the seven for which the text says so in a dedicated clause.** It has a season and an hour and no ground.

### 4.2 Why the name நடுவணது — four reasons from the commentary

Naccinārkkiniyar's (urai-1 lines 122–127) gives the reasons, and they are worth setting out because they show the word doing four different jobs at once:

| Sense of "middle" | The reasoning |
|---|---|
| **Middle of the list** | It is the middlemost of the five that were apportioned |
| **Middle of the day** | `நடுவணதாகிய நண்பகற்காலந் தனக்குக் காலமாகலானும்` — high noon, the middle of the six hours, is its hour |
| **Middle of the sequence of love** | `புணர்தல் இருத்தல், இரங்கல், ஊடல் என்பவற்றிற்கு இடையே பிரிவு நிகழ்தலானும்` — separation falls *between* union, waiting, grieving, and quarrelling |
| **Middle of the three ends of life** | `அறம்பொரு ளின்பங்களுள் நடுவணதாய பொருட்குத்தான் காரணமாகலானும்` — it is the cause of பொருள், the middle one of அறம்/பொருள்/இன்பம் |

He also cites சிலப்பதிகாரம் (காடுகாண் காதை 64–66) for the naturalistic account — that mullai and kurinji, deranged from their proper nature, *take on the form called பாலை* — and treats that as the முதற்பொருள் ground for the name.

[விளக்கம் | INTERPRETATION] The design is not "we forgot to give one a landscape." **பாலை is the term for the interval between the other states**, and an interval by definition has no ground of its own. That is why it can appear in any of the four lands: அகம் 15 (`உரிப்பொருள் அல்லன மயங்கவும் பெறுமே`) is read by நச். (urai-1 line 888) as covering பாலை too, since the `உம்` is `எச்சவும்மை`. He then cites poems he labels `முல்லையுட் பாலை` — *palai within mullai* (urai-1 line 523).

### 4.3 The consequence nobody mentions: பாலை has no god

நச்சினார்க்கினியர் draws the inference explicitly (urai-1 line 1163): `இதனானே பாலைக்குத் தெய்வமும் இன்றாயிற்று` — *by this, பாலை has no deity either.*

The logic is airtight and slightly chilling. அகம் 5 assigns gods **to worlds**, not to திணை. பாலை has no world. Therefore no god. [விளக்கம் | INTERPRETATION] The one திணை about separation, thirst, ruin, and the crossing of waste ground is, in the architecture of the system, the one place where nobody is watching. The other four `கரு` categories he does supply for it — food that is what was taken on the road, beasts that are a weakened elephant and a tiger and a red dog, trees that are dried iruppai and omai, birds that are vulture and kite and dove, drums that are the drums of raiding, work that is waylaying, and பாலையாழ் for the tuning (urai-1 line 1170) — but the deity slot stays empty.

[காதுக்காக — flagged for §9] Whether `பாலையாழ்` as the tuning of a landless திணை is doing something audible that the other four யாழ் are not, I cannot assess.

---

## 5. கூற்று — who may speak

### 5.1 What அகத்திணையியல் assigns, and to whom

The iyal devotes நூற்பா **39 through 45** (மூலம் lines 2230–2284) to speech-rights, in the setting of `உடன்போக்கு` — the elopement — which is where the question of who may speak becomes acute.

| நூற்பா | Lines | Speaker | Closing words |
|---|---|---|---|
| 39 | 2230–2237 | **நற்றாய்** — the birth mother, lamenting after the going | `ஆகிய கிளவியும் அவ் வழி உரிய.` |
| 40 | 2238–2239 | **தாயர்** who go themselves, to the street and to the waste | `தாமே செல்லும் தாயரும் உளரே.` |
| 41 | 2240 | **அயலோர்** — the neighbours | `அயலோர் ஆயினும் அகற்சி மேற்றே.` |
| 42 | 2241–2250 | **தோழி** — the friend | `ஒன்றித் தோன்றும் தோழி மேன.` |
| 43 | 2251–2259 | **கண்டோர்** — those who saw them pass | `கண்டோ ர் மொழிதல் கண்டது என்ப.` |
| 44 | 2260–2283 | **கிழவோன்** — the man | `உரைத் திற நாட்டம் கிழவோன் மேன.` |
| 45 | 2284 | **the remainder** | `எஞ்சியோர்க்கும் எஞ்சுதல் இலவே.` |

### 5.2 The two findings

**(i) The heroine is not named in a நூற்பா of her own.**

Read the list again. நற்றாய், தாயர், அயலோர், தோழி, கண்டோர், கிழவோன் — six parties get a dedicated நூற்பா. **தலைவி does not.** She arrives through அகம் 45, the mopping-up clause: `எஞ்சியோர்க்கும் எஞ்சுதல் இலவே` — *to the remaining ones too, [speech] is not withheld.*

Who are `எஞ்சியோர்`? நச்சினார்க்கினியர் names them (urai-1 line 2547): `முன்னர்க் கூறாது நின்ற செவிலிக்குந் **தலைவிக்கும்** ஆயத்தோர்க்கும் அயலோர்க்கும்` — *the foster-mother, **the heroine**, her companions, and the neighbours, who stood unmentioned before.*

[விளக்கம் | INTERPRETATION] In the iyal that governs the poetry of interior life, the woman whose interior life it is receives her right to speak from a residue clause, in the same breath as the neighbours. This is a structural fact about the text, not a rhetorical flourish: the நூற்பா that name speakers name her only by not excluding her.

I want to state the limit of this claim carefully. **அகத்திணையியல் is not the whole of the speech-rights machinery.** களவியல் and கற்பியல் go into கூற்று at far greater length and the heroine speaks constantly there; and Naccinārkkiniyar's opening survey (urai-1 line 100) counts `பன்னிருவகைக் கூற்றும் பத்துவகைக் கேட்போரும்` — twelve kinds of speech and ten kinds of hearer — across the whole அதிகாரம். So the claim is: **within the iyal that lays down the general law of akam, this is the distribution.** [திறந்த கேள்வி | OPEN QUESTION] Whether the same asymmetry holds when களவியல் and கற்பியல் are counted is a separate piece of work.

**(ii) The allocation of textual space is itself the hierarchy.**

Count the lines:

| Speaker | Lines of நூற்பா |
|---|---|
| **கிழவோன்** (the man) | **24** |
| தோழி (the friend) | 10 |
| கண்டோர் (witnesses) | 9 |
| நற்றாய் (the mother) | 8 |
| தாயர் | 2 |
| அயலோர் | 1 |
| **the remainder, தலைவி among them** | **1** |

The man's நூற்பா (மூலம் 2260–2283) is the longest in the iyal by a factor of more than two, and it is an itemised catalogue of what he may raise: the shortness of the days and the hardness of youth, the merit of effort and the fitness of the fitting, `இன்மையது இளிவும் உடைமையது உயர்ச்சியும்` — *the meanness of not having and the elevation of having* — the breadth of love and the difficulty of leaving, gain reckoned by mouth and by hand, fame and honour urged as strengthening, and the matter of an embassy interposed.

[விளக்கம் | INTERPRETATION] Twenty-four lines enumerating a man's permissible arguments for going, one line covering everyone else including the woman he is going from. Whatever else this is, it is a distribution of expressive resource, written into the grammar as grammar.

### 5.3 And a rule about naming

> மக்கள் நுதலிய அகன் ஐந்திணையும்
> சுட்டி ஒருவர்ப் பெயர் கொளப் பெறாஅர்.

[மூலம் | SOURCE: மூலம் lines 2311–2312, அகம் 57.] *In the wide five திணை that concern human beings, they may not take up any one person's name by pointing at them.*

This is the famous anonymity convention, and here is its நூற்பா. `sangam.md` §1 states it correctly as a convention; this is the rule itself. Note `நுதலிய` — *aimed at, concerning* — and `சுட்டி` — *by deixis, by pointing.* The prohibition is on **deictic naming**, not on names as such. Which the next நூற்பா immediately confirms:

> புறத்திணை மருங்கின் பொருந்தின் அல்லது
> அகத்திணை மருங்கின் அளவுதல் இலவே.

[மூலம் | SOURCE: மூலம் lines 2313–2314, அகம் 58 — the last நூற்பா of the iyal.] Proper names *may* enter an akam poem — but only where a புறத்திணை matter is joined in. Naccinārkkiniyar's (urai-1 line 3302): they come in as `கருப்பொருள்` or as `உவமம்`, and he gives அகநானூறு 1 as his instance — the poem names `நெடுவேள் ஆவி` and his hill `பொதினி`, and both are landscape-furniture for a poem whose lovers stay nameless.

[விளக்கம் | INTERPRETATION] The rule is not "no names in love poems." It is: **the lovers may not be named; the world may.** Kings, hills, and chieftains are scenery you can point at. The people the poem is about are not. This is the formal mechanism behind the observation in `sangam.md` §2 that குறுந்தொகை 40 becomes "every first union that ever bypassed family" — the anonymity is not tact, it is a stated rule about deixis, and its effect is universalisation.

---

## 6. ஏழு புறத்திணை — and how each one is fastened to an akam திணை

### 6.1 The frame

> அகத்திணை மருங்கின் அரில் தப உணர்ந்தோர்
> புறத்திணை இலக்கணம் திறப்படக் கிளப்பின்
> வெட்சிதானே குறிஞ்சியது புறனே
> உட்கு வரத் தோன்றும் ஈர் ஏழ் துறைத்தே.

[மூலம் | SOURCE: மூலம் lines 2317–2320, புறம் 1.] *Those who have understood the akam திணை without tangle (`அரில் தப`), if they set out the grammar of the புறத்திணை by division: வெட்சி is the outside of குறிஞ்சி, and it has fourteen துறை that appear so as to bring dread.*

The very first புறத்திணை நூற்பா does two things at once: it names a war-திணை, and it fastens it to a love-திணை. **The pairing is not an afterthought; it is the definition.** Every one of the seven is introduced the same way.

### 6.2 The seven, with the நூற்பா that pairs them

| புறத்திணை | The pairing நூற்பா (verbatim) | Line | Pairs with | What it covers, from the நூற்பா |
|---|---|---|---|---|
| **வெட்சி** | `வெட்சிதானே குறிஞ்சியது புறனே` | 2319 | **குறிஞ்சி** | `வேந்து விடு முனைஞர் வேற்றுப் புலக் களவின் / ஆ தந்து ஓம்பல் மேவற்று ஆகும்` (2321–2) — frontier-men sent by the king; **by theft** in enemy country, bringing the cattle away and guarding them |
| **வஞ்சி** | `வஞ்சிதானே முல்லையது புறனே` | 2355 | **முல்லை** | `எஞ்சா மண் நசை வேந்தனை வேந்தன் / அஞ்சு தகத் தலைச் சென்று அடல் குறித்தன்றே` (2356–7) — out of unabated hunger for land, king marching upon king, aiming at his destruction |
| **உழிஞை** | `உழிஞைதானே மருதத்துப் புறனே` | 2371 | **மருதம்** | `முழு முதல் அரணம் முற்றலும் கோடலும்` (2372) — investing the whole-stock fortress, and taking it |
| **தும்பை** | `தும்பைதானே நெய்தலது புறனே` | 2396 | **நெய்தல்** | `மைந்து பொருளாக வந்த வேந்தனைச் / சென்று தலை அழிக்கும் சிறப்பிற்று` (2397–8) — the king who came with sheer strength as his object, met and stripped of pre-eminence |
| **வாகை** | `வாகைதானே பாலையது புறனே` | 2421 | **பாலை** | `தா இல் கொள்கைத் தம்தம் கூற்றைப் / பாகுபட மிகுதிப் படுத்தல்` (2422–3) — each party, holding its faultless principle, being raised to excellence in its own portion |
| **காஞ்சி** | `காஞ்சிதானே பெருந்திணைப் புறனே` | 2457 | **பெருந்திணை** | `பாங்கு அருஞ் சிறப்பின் பல் ஆற்றானும் / நில்லா உலகம் புல்லிய நெறித்தே` (2458–9) — by many roads, the way that embraces **the world that does not stand** |
| **பாடாண்** | `பாடாண் பகுதி கைக்கிளைப் புறனே` | 2496 | **கைக்கிளை** | `நாடும் காலை நால் இரண்டு உடைத்தே` (2497) — praise of a man; eight kinds when investigated |

**Note the ordering.** The புறம் sequence is வெட்சி · வஞ்சி · உழிஞை · தும்பை · வாகை · காஞ்சி · பாடாண், which pairs to குறிஞ்சி · முல்லை · மருதம் · நெய்தல் · பாலை · பெருந்திணை · கைக்கிளை. The four land-holding திணை come in a fixed order, then the landless one, then the two outliers — **and the two outliers come in reverse** (பெருந்திணை before கைக்கிளை). [திறந்த கேள்வி | OPEN QUESTION] Whether the reversal is significant or metrical convenience.

### 6.3 Why each pairing holds — Naccinārkkiniyar's reasoning

This is where the system stops looking like an analogy and starts looking like an argument. His grounds, thinly paraphrased:

| Pairing | The ground he gives | Where |
|---|---|---|
| வெட்சி / குறிஞ்சி | Both are **clandestine and nocturnal**: `களவொழுக்கமுங் கங்குற் காலமுங் காவலர் கடுகினுந் தான் கருதிய பொருளை இரவின்கண் முடித்து மீடலும்` — the stolen tryst and the cattle-raid have the same shape: guards alert, the thing accomplished by night, the return before dawn | urai-2 line 69 |
| வஞ்சி / முல்லை | The forest world, the rains, the forest's கரு — and above all the **waiting**: the king separated from his queen in the war-camp, she separated from him at home. `அரசன் பாசறைக்கட் டலைவியைப் பிரிந்து இருத்தலும், அவன் தலைவி அவனைப் பிரிந்து மனைவயி னிருத்தலுமாகிய உரிப்பொருளும்` | urai-2 line 898 |
| உழிஞை / மருதம் | The fortress stands in farmland; the besieger camps in farmland; **and the shape of the act is the same** — one party shut in and refusing to open the gate, one party outside wanting in. Both have no season restriction; both take the dawn hour | urai-2 line 1309 |
| தும்பை / நெய்தல் | Neither forest nor hill nor field but the **salt flat and the sand** as battleground; no season restriction; sun-fall is when the fighting ends; and grief belongs to the one left, not to the fighters | urai-2 line 1772 |
| வாகை / பாலை | **Both are landless.** `பாலை தனக்கென ஓர் நிலமின்றி நால்வகைநிலத்தும் நிகழுமாறு போல, முற்கூறிய புறத்திணை நான்கும் இடமாக வாகைத் திணை நிகழ்தலிற் றனக்கு நிலமின்றாயிற்று` — as பாலை has no land of its own and occurs across all four, so வாகை occurs across the four புறத்திணை already stated and so has none. And both are about **leaving**: he leaves the marriage-bed for a fame worth having, the warrior leaves kin for a righteous war and heaven | urai-2 line 2179 |
| காஞ்சி / பெருந்திணை | Both are the **excess case**. As பெருந்திணை alone carries four of the eight forms of union while the other six திணை share four, so காஞ்சி alone carries the impermanence of all three of அறம்/பொருள்/இன்பம் and is common to every திணை; and as the four marks of பெருந்திணை are the loves the wise held cheap, so the matters of காஞ்சி are what the wise hold cheap because they do not last | urai-2 line 2952 |
| பாடாண் / கைக்கிளை | *(He gives the pairing at urai-2 line 3399 and the eightfold division; the ground is the structural one — one-sided address. Praise, like kaikkilai, is speech that expects no answering word.)* | urai-2 line 3399 |

[விளக்கம் | INTERPRETATION] The வாகை / பாலை pairing is the one that proves the system is doing real work. **Two landless categories, matched to each other on the ground of their landlessness.** Whoever built this was not decorating a table; they were reasoning about the structure of the table.

### 6.4 The துறை counts, and why they do not add up cleanly

Each புறத்திணை is subdivided into `துறை` — situations. The counts as the நூற்பா state them:

| திணை | The நூற்பா's own words | Line | Count |
|---|---|---|---|
| வெட்சி | `உட்கு வரத் தோன்றும் ஈர் ஏழ் துறைத்தே` | 2320 | 14 |
| வெட்சி (elaborated) | `வந்த ஈர் ஏழ் வகையிற்று ஆகும்` | 2330 | 14 more — நச். reads the total as 28 (urai-2 line 104) |
| — கரந்தை | `சொல்லப்பட்ட எழு மூன்று துறைத்தே` | 2354 | 21 |
| வஞ்சி | `கழி பெருஞ் சிறப்பின் துறை பதின்மூன்றே` | 2370 | 13 |
| உழிஞை | `அதுவேதானும் இரு நால் வகைத்தே` | 2374 | 8 |
| உழிஞை | `சொல்லப்பட்ட நால் இரு வகைத்தே` | 2382 | 8 |
| — நொச்சி | `வகை நால் மூன்றே துறை என மொழிப` | 2395 | 12 |
| தும்பை | `புல்லித் தோன்றும் பன்னிரு துறைத்தே` | 2420 | 12 |
| வாகை | `ஆங்கு எழு வகையான் / தொகை நிலைபெற்றது என்மனார் புலவர்` | 2431–2 | 7 classes |
| வாகை | `இரு பாற் பட்ட ஒன்பதின் துறைத்தே` | 2456 | "nine, in two portions" |
| காஞ்சி | `ஈர் ஐந்து ஆகும் என்ப` | 2477 | 10 |
| காஞ்சி | `நிறை அருஞ் சிறப்பின் துறை இரண்டு உடைத்தே` | 2495 | 2 |
| பாடாண் | `நாடும் காலை நால் இரண்டு உடைத்தே` | 2497 | 8 |

[திறந்த கேள்வி | OPEN QUESTION] I have deliberately not summed these. Counting the items in புறம் 3, for example, yields sixteen distinguishable nouns against a stated `ஈர் ஏழ்` of fourteen — meaning some pairs are meant to be read as single துறை, and *which* pairs is a commentator's decision. Different உரை give different totals for the same நூற்பா. **The counts are not arithmetic facts about the text; they are readings of it.** Anyone quoting "வெட்சி has 14 துறை" should say whose 14.

### 6.5 கரந்தை and நொச்சி — why there are seven and not nine

Two well-known war-topics — **கரந்தை** (recovering the raided cattle) and **நொச்சி** (defending the fort) — sit inside this iyal but are **not counted among the seven.** கரந்தை appears at புறம் 5 (மூலம் line 2346: `அனைக்கு உரி மரபினது கரந்தை`), inside the வெட்சி section; நொச்சி at புறம் 11 (line 2387: `அகத்தோன் வீழ்ந்த நொச்சியும்`), inside உழிஞை.

நச்சினார்க்கினியர் gives the reason for கரந்தை (urai-1 line 113): `கரந்தை அவ் வேழற்கும் பொதுவாகிய வழுவாதலின், வேறு திணையாகாது` — *because கரந்தை is a deviation common to all seven, it does not become a separate திணை.*

[விளக்கம் | INTERPRETATION] The criterion for திணை-hood is therefore **not** "is this a distinct kind of fighting." It is: *does this stand in a one-to-one relation to an akam திணை?* கரந்தை is a response-move available inside any of them, so it is a துறை. The seven-and-seven symmetry is being actively defended — which tells you the symmetry is the point. நச்சினார்க்கினியர் makes the defence explicit with a small joke about hands (urai-1 line 113): if the palm has two, the back of the hand does not have four; it has two. Seven akam, therefore seven puram.

And note the count of the whole system, from his opening survey (urai-1 line 100): `அதன்கட் கைக்கிளை முதற் பெருந்திணை யிறுவா யேழும் வெட்சி முதற் பாடாண்டிணை யிறுவா யேழுமாகப் **பதினான்கு**` … `பால் வகுத்து` — fourteen.

### 6.6 One புறத்திணை நூற்பா worth quoting for its own sake

> காமப் பகுதி கடவுளும் வரையார்
> ஏனோர் பாங்கினும் என்மனார் புலவர்.

[மூலம் | SOURCE: மூலம் lines 2505–2506, புறம் 23.] *In the matter of love, they do not exclude even a god — nor others either, so say the learned.*

நச்சினார்க்கினியர் cites this back in the அகத்திணையியல் (urai-1 line 130) to make the point that the akam grammar is for `மக்கள் நுதலிய` — human beings — and so does not apply to gods, `இன்பமே நிகழுந் தேவர்க்காகா`, for whom pleasure alone occurs. Gods' love goes to பாடாண், the praise-திணை, not to the five.

---

## 7. இலக்கணமாக்கப்பட்ட சமூக ஒழுங்கு | Where the text encodes social order as grammar

`../varalaru/arivu-varalaru.md` §2 says: *"it codifies who may speak…, gendered scripts (கற்பு chastity ideology enters the poetics), and social norms presented as grammar. The founding gift and the founding bias are the same page."* That is correct and it is an assertion. Here are the lines.

I want to be precise about what is being claimed. **Not** that Tolkappiyam invented these hierarchies, and **not** that noticing them diminishes the text. The claim is narrower and stranger: these are stated in the same register, with the same `என்மனார் புலவர்` and `என்ப` formulae, as the rule about which bird belongs to which landscape. **A social fact and a poetic fact are given the same grammatical form, and that is the encoding.**

### 7.1 வருணம் — caste, as a determinant of who may be a தலைவன்

> அடியோர் பாங்கினும் வினைவலர் பாங்கினும்
> கடிவரை இல புறத்து என்மனார் புலவர்.

[மூலம் | SOURCE: மூலம் lines 2207–2208, அகம் 25.] *Among servants too and among those skilled at commanded work too, there is no barring — **on the outside**, so say the learned.*

Naccinārkkiniyar's gloss (urai-1 lines 1319–1320) removes all ambiguity about `புறத்து`: `அடியோர் பாங்கினும்- பிறர்க்குக் குற்றேவல் செய்வோரிடத்தும்; வினை வல பாங்கினும்- பிறர் ஏவிய தொழிலைச் செய்தல் வல்லோரிடத்தும்; கடி வரையில புறத்து என்மனார் புலவர்- தலைமக்களாக நாட்டிச் செய்யுட்செய்தல் நீக்கப் படாது **நடுவணைந்திணைப் புறத்து நின்ற கைக்கிளை பெருந்திணைகளுள்**` — *setting them up as the principals and composing poetry is not prohibited: **in the கைக்கிளை and பெருந்திணை that stand outside the middle five.***

Read that again. Those who do menial service and those who do commanded labour **may be the hero and heroine of an akam poem — in the two திணை outside the five.** They are not barred; they are placed. His illustrations (urai-1 lines 1322–1329) are கலித்தொகை lines where the speaker says `கோனடி தொட்டேன்` (I have touched the master's feet) and mentions `கோயில்` — and he notes precisely that these markers are what make the speakers `குற்றேவன்மாக்க ளாயிற்று`, servants, and therefore the poem பெருந்திணை.

[விளக்கம் | INTERPRETATION] This is the sharpest single instance in the iyal. The five திணை that "the sea-girt world was apportioned into" — the ones with land, season, hour, god, and a settled inner state — are, by this நூற்பா as read in the received commentary, the love-life of those who are not servants. The others get the two categories that have no land and no god: the unripe and the excessive. **A social boundary and a poetic boundary are made to coincide, and the coincidence is stated as grammar.**

I flag one uncertainty honestly. `கடிவரை இல புறத்து` is terse. நச். reads `புறத்து` as *outside the middle five* (i.e. in kaikkilai/perunthinai). A reading of `புறத்து` as *in the புறத்திணை* is grammatically available and would give a different, milder sense. [திறந்த கேள்வி | OPEN QUESTION] Whether Ilampūraṇar's or other உரை read it differently is not checkable from these two files. **The reading matters a great deal and I cannot settle it here.**

**The reciprocal நூற்பா** confirms the frame from the other side:

> ஏவல் மரபின் ஏனோரும் உரியர்
> ஆகிய நிலைமை அவரும் அன்னர்.

[மூலம் | SOURCE: மூலம் lines 2209–2210, அகம் 26.] நச். (urai-1 line 1361) glosses `மரபின்` as `வேதநூலுட்கூறிய இலக்கணத்தானே` — *by the definition stated in the Vedic books* — and `ஏவல் ஆகிய நிலைமையவரும்` as those whose station is **to command others.** The commanding and the commanded are both given their line.

### 7.2 உயர்ந்தோர் — "the high," as a grammatical category

The `பிரிவு` sequence (அகம் 27–36) sorts the reasons a man may leave his wife **by his station**, in so many words:

| நூற்பா | Line | Text | What it allots |
|---|---|---|---|
| 28 | 2213 | `ஓதலும் தூதும் உயர்ந்தோர் மேன.` | Study and embassy belong to **the high** |
| 29 | 2214–5 | `தானே சேறலும் தன்னொடு சிவணிய / ஏனோர் சேறலும் வேந்தன் மேற்றே.` | Going himself, and allies going for him, belong to **the king** |
| 31 | 2220 | `மேலோர் முறைமை நால்வர்க்கும் உரித்தே.` | The manner of **the upper** is proper **to the four** |
| 32 | 2221 | `மன்னர் பாங்கின் பின்னோர் ஆகுப.` | Those in the king's following become **the latter ones** |
| 33 | 2222 | `உயர்ந்தோர்க்கு உரிய ஓத்தினான.` | By the ஓத்து (recitation/scripture) proper **to the high** |
| 36 | 2226 | `உயர்ந்தோர் பொருள்வயின் ஒழுக்கத்தான.` | By the conduct of **the high** in the matter of wealth |

நச்சினார்க்கினியர் names the referents without hedging. On அகம் 28 (urai-1 line 1472): `ஓதற்பிரிவுந் தூதிற்பிரிவும் **அந்தணர் முதலிய மூவரிடத்தன**` — the separations for study and for embassy belong to *the three beginning with brahmins*. On அகம் 33 (urai-1 line 1688): `உயர்ந்தோர்க்கு உரிய- **அந்தணர் அரசர் வணிகர்க்கும், உயர்ந்த வேளாளர்க்கும்** உரிய`. On அகம் 11 in his numbering (=மூலம் 13, urai-1 line 601): `நான்கு வருணத்தாருக்கும் காலிற் பிரிவும் **வேளாளர்க்குக்** கலத் திற் பிரிவுந் தத்தம் நிலைமைக்கேற்பத் தோன்றினும்` — land-travel for all four varnas, sea-travel for the வேளாளர்.

[விளக்கம் | INTERPRETATION] The four-varna scheme is not smuggled in; in the received commentary it is the sorting key for an entire block of the poetics. Whether the நூற்பா's bare `உயர்ந்தோர்` and `நால்வர்` *meant* the four varnas when they were composed, or whether that is Naccinārkkiniyar's fourteenth-century reading laid on an older and vaguer word, is exactly the kind of question `arivu-varalaru.md` §5 says must always be asked. [திறந்த கேள்வி | OPEN QUESTION — and a real one, not rhetorical: `உயர்ந்தோர்` could as easily be *the eminent* as *the twice-born*, and the நூற்பா does not say.]

### 7.3 மகடூஉ — two prohibitions with the word for "woman" in them

> முந்நீர் வழக்கம் மகடூஉவொடு இல்லை.

[மூலம் | SOURCE: மூலம் line 2227, அகம் 37.] *There is no sea-going along with a woman.* நச். (urai-1 line 1717): of the five kinds of separation, the three that are study, embassy, and wealth-seeking do not involve taking the wife along.

> எத்திணை மருங்கினும் மகடூஉ மடல்மேல்
> பொற்புடை நெறிமை இன்மையான.

[மூலம் | SOURCE: மூலம் lines 2228–2229, அகம் 38.] *In no திணை whatsoever is there for a woman a seemly way upon the மடல்.* நச். (urai-1 line 1728) glosses `எத்திணை மருங்கினும்` as `கைக்கிளைமுதற் பெருந்திணையிறுவாய் **ஏழன்கண்ணும்**` — in all seven — and cites திருக்குறள் 1137 in support.

[விளக்கம் | INTERPRETATION] Take the second one seriously as *poetics*. The மடல் — the palmyra-stalk horse, ridden through the streets to make one's love public and force the family's hand — is the one device in the whole system by which a lover **breaks the anonymity rule and makes a private matter public.** It is a speech-act of last resort. அகம் 38 removes it from women in all seven திணை, and does so with a word of quality: `பொற்புடை நெறிமை இன்மையான` — *because there is no seemly way.* The prohibition is not on the woman's feeling. It is on **her access to the escalation.** And it is scoped more broadly than any other rule in the iyal: not "in the five," but `எத்திணை மருங்கினும்`.

Note also what falls out of §1.3: the man's *actually riding* the மடல் is the first mark of பெருந்திணை. So the system's account is: for a man, riding the மடல் is excessive but categorised; for a woman, it is `பொற்புடை நெறிமை இன்மையான` — outside seemliness, and given no category at all.

### 7.4 கற்பு inside அகத்திணையியல்

The word `கற்பு` occurs **once** in the whole of அகத்திணையியல் (grep of மூலம் lines 2155–2315), at line 2264, inside the man's long நூற்பா:

> கற்பொடு புணர்ந்த கௌவை உளப்பட

*including the scandal joined with கற்பு.* [மூலம் | SOURCE: மூலம் line 2264, within அகம் 41.]

[விளக்கம் | INTERPRETATION] Two observations, offered narrowly. First, the ideology is not built in this iyal — கற்பியல் is a separate chapter and that is where the weight sits; `arivu-varalaru.md` §2's claim about கற்பு should be tested there, not here. Second, and more interesting: in its one appearance in the general law of akam, கற்பு appears **bound to `கௌவை`, scandal** — the word for the village's talk. Not as a virtue in the abstract, but as the thing about which a village talks. [கருதுகோள் | HYPOTHESIS, testable against கற்பியல்] That கற்பு enters Tolkappiyam's poetics primarily as *a social-visibility condition* — what is sayable about a union and by whom — rather than as an interior state. If so, the machinery of கற்பு would be continuous with the machinery of கூற்று, not separate from it.

### 7.5 The புறம் side: வாகை enumerated by வருணம்

> அறு வகைப் பட்ட பார்ப்பனப் பக்கமும்
> ஐ வகை மரபின் அரசர் பக்கமும்
> இரு மூன்று மரபின் ஏனோர் பக்கமும்
> மறு இல் செய்தி மூ வகைக் காலமும்
> நெறியின் ஆற்றிய அறிவன் தேயமும்
> நால் இரு வழக்கின் தாபதப் பக்கமும்
> பால் அறி மரபின் பொருநர்கண்ணும்

[மூலம் | SOURCE: மூலம் lines 2424–2430, புறம் 16.]

The புறத்திணை of **excellence** — வாகை, *each party raised to the height of its own portion* (புறம் 15) — is enumerated as: the brahmin's side in six kinds, the king's side in five, the others' side in six, the seer's country, the ascetic's side in eight, the bard's part. **Excellence itself is decomposed by station.**

நச்சினார்க்கினியர் unpacks the brahmin's six (urai-2 line 2210) as `ஓதல் ஓதுவித்தல் வேட்டல் வேட்பித்தல் கொடுத்தல் கோடல்` — reciting, causing to recite, sacrificing, causing to sacrifice, giving, receiving — the standard six duties, and spends several pages ranking the texts each of them requires, `தலை இடை கடை` (first, middle, last), placing இருக்கு/எசுர்/சாமம் at the head and `அகத்தியந் தொல்காப்பியம் முதலிய தமிழ்நூல்களும்` in the middle band (urai-2 line 2213). He then adds, almost in passing, `இவற்றுள் தருக்கமுங் கணிதமும் **வேளாளர்க்கும் உரித்தாம்**` — logic and mathematics belong to the வேளாளர் too.

[விளக்கம் | INTERPRETATION] Note what has happened by the fourteenth century: a Tamil poetics chapter on *what counts as excellence* is being commented on with a graded curriculum in which Tamil grammar including Tolkappiyam itself is placed in the second rank behind the Vedas. `arivu-varalaru.md` §5 is exactly right that the commentary swings with its commentator's world. This is a documented instance, with the line number.

### 7.6 Summary of §7

| The rule, as grammar | Line | The social fact inside it |
|---|---|---|
| `அடியோர் பாங்கினும் வினைவலர் பாங்கினும் / கடிவரை இல புறத்து` | 2207–8 | servants may be principals — in the two landless திணை (per நச்.) |
| `ஓதலும் தூதும் உயர்ந்தோர் மேன.` | 2213 | study and embassy belong to "the high" |
| `மேலோர் முறைமை நால்வர்க்கும் உரித்தே.` | 2220 | the four (varnas, per நச்.) |
| `உயர்ந்தோர்க்கு உரிய ஓத்தினான.` | 2222 | scripture belongs to "the high" |
| `முந்நீர் வழக்கம் மகடூஉவொடு இல்லை.` | 2227 | no sea-voyage with a woman |
| `எத்திணை மருங்கினும் மகடூஉ மடல்மேல் / பொற்புடை நெறிமை இன்மையான.` | 2228–9 | no மடல் for a woman, in any of the seven |
| `எஞ்சியோர்க்கும் எஞ்சுதல் இலவே.` | 2284 | the heroine's speech-right arrives in the residue clause |
| `அறு வகைப் பட்ட பார்ப்பனப் பக்கமும் / ஐ வகை மரபின் அரசர் பக்கமும்…` | 2424–6 | excellence itself decomposed by station |

**What this is and is not.** [விளக்கம் | INTERPRETATION] It is not a discovery that a text from the first centuries around the Common Era assumes a stratified society. It is that the stratification is **doing formal work** — determining which திணை a poem falls into, which separations may be narrated, who may escalate. Change the caste of the lovers and the poem changes genre. That is what "encoded as grammar" means, and it is why the observation belongs in a grammar file rather than a history one.

---

## 8. மூலத்தில் இல்லாதவை | What is not in the நூற்பா

A checklist, because this is the practical use of the whole document. Each of these is standardly attributed to Tolkappiyam and is not in the அகத்திணையியல்/புறத்திணையியல் நூற்பா of `pmuni0100`:

| Commonly attributed | Status in the நூற்பா |
|---|---|
| "The five திணை" as the name of the system | The word `ஐந்திணை` occurs three times, always qualified (`நடுவண்`, `அகன்`, `அன்பொடு புணர்ந்த`). The system is stated as **seven**. |
| The terms முதற்பொருள், கருப்பொருள் | Do not occur. The நூற்பா says `முதல் கரு உரிப்பொருள்`. |
| The terms பெரும்பொழுது, சிறுபொழுது | Do not occur anywhere in the மூலம். Commentary vocabulary. |
| குறிஞ்சி = union, மருதம் = quarrel, etc. | **The pairing is never stated in அகத்திணையியல்.** The உரிப்பொருள் list stands unattached at 2188–2190. |
| The flower as a கரு | Not in the enumerating நூற்பா (2195–7). Enters via நச். as a `சினை` of `மரம்`, and via 2198–2200. |
| The per-landscape table of god / food / beast / tree / bird / drum / work / yaazh | The நூற்பா gives the **eight slots** and `அவ் வகை பிறவும்`. The filled table is Naccinārkkiniyar's at urai-1 lines 1164–1170. |
| A season for மருதம் and நெய்தல் | None assigned. நச். says explicitly there is no restriction. |
| A god for பாலை | None. நச். draws the inference at urai-1 line 1163. |
| Fixed துறை totals per புறத்திணை | The நூற்பா give phrases (`ஈர் ஏழ்`, `இரு பாற் பட்ட ஒன்பதின்`) whose resolution is a commentator's count. |
| The order குறிஞ்சி முல்லை மருதம் நெய்தல் | The நூற்பா order is **முல்லை குறிஞ்சி மருதம் நெய்தல்**, kept consistently across நூற்பா 5, 6, 7, 9, 10, 30. |

[விளக்கம் | INTERPRETATION] The pattern is consistent and worth naming: **the நூற்பா give an architecture with open slots and stated exceptions; the உரை tradition filled the slots and hardened the exceptions into a table.** Both operations were necessary — an open slot cannot be taught — but the result is that "Tolkappiyam's திணை system" as it now circulates is a composite object, and the seams are all findable with grep.

---

## 9. காதுக்காக | Awaiting the ear

Addressed to the repo owner. Everything below is **computed, not heard.** I cannot hear Tamil; these are pattern-observations that need a native ear to accept, correct, or reject.

1. **`கைக்கிளை` and `பெருந்திணை` as a matched pair by sound.** Both are four syllables with a heavy first element and both end `-ளை / -ணை`. Whether they *sound* like a pair — whether the first and last names of the seven were chosen to rhyme the frame shut — is not something I can judge.

2. **அகம் 1's rhythm as an opening.** `கைக்கிளை முதலாப் பெருந்திணை இறுவாய் / முற்படக் கிளந்த எழு திணை என்ப.` I can see the ளை/ணை and the -ப்ப- in `முற்படக்`, but whether this line has the weight of an opening — whether it *lands* as the first sentence of a book about all of human content — is yours to say.

3. **அகம் 5's four parallel lines** (`மாயோன் மேய… / சேயோன் மேய… / வேந்தன் மேய… / வருணன் மேய…`). Four lines with the same second word. Computationally this is anaphora; whether it produces a chant, a list, or a liturgy in the ear I cannot tell. It matters, because if it chants, the primacy of gods over landscape names in §3.1 is reinforced by the sound.

4. **மாயோன் / சேயோன்** — the two god-names in lines 1 and 2 differ in one syllable and are semantically opposed (dark / red). Whether that opposition is audible as a pair, or whether it is only visible on the page, needs your ear.

5. **அகநானூறு 4's opening seven lines** as a *withheld* sentence — no main clause about the woman until `உவக்காண்`. Whether the delay is felt as suspension or just as description depends entirely on how the lines move aloud.

6. **`கார்செய் தன்றே`** — I have called this the pivot of அகம் 4. The `-ஏ` is the standard Sangam closing particle noted in `sangam.md` §2, but here it lands mid-poem. Whether that produces a false ending that the poem then walks past is an ear question and possibly the best thing in the poem.

7. **`ஈர் ஏழ்`, `இரு நால்`, `நால் இரு`, `எழு மூன்று`, `இரு மூன்று`, `நால் இரண்டு`.** The புறத்திணையியல் almost never says a number plainly; it multiplies. Whether these compounds are chosen for metre, for a numerological habit, or for something audible I cannot judge — but the consistency is striking and someone should say what it is doing.

8. **`பாலையாழ்`** as the tuning assigned to the landless திணை. I have no access to what any of the four/five யாழ் sounded like; the whole `யாழின் பகுதி` category is, for me, a name with nothing behind it.

9. **The register of `மகடூஉ`.** I have translated it flatly as "woman." Whether it carries a formal, archaic, legal, or neutral colour in these நூற்பா — and whether that colour changes how §7.3 should be read — I cannot hear.

10. **`அரில் தப உணர்ந்தோர்`** (புறம் 1) — I have rendered `அரில் தப` as "without tangle." Whether `அரில்` here is thicket-tangle, confusion, or something more specific, and whether the phrase is idiomatic or striking, needs checking against your ear and against usage elsewhere.

---

## 10. திறந்த கேள்விகள் | Open questions

1. **Where, if anywhere, does a நூற்பா pair a landscape with its உரிப்பொருள்?** Not in அகத்திணையியல். களவியல், கற்பியல், and பொருளியல் have not been checked. This is the highest-value next check in the whole file.
2. **`கடிவரை இல புறத்து` (அகம் 25)** — does `புறத்து` mean *outside the five* (நச்சினார்க்கினியர்) or *in the புறத்திணை*? Ilampūraṇar's reading is not available in these files. The two readings give materially different accounts of caste in the poetics.
3. **`உயர்ந்தோர்` and `நால்வர்`** — do the நூற்பா themselves intend the four varnas, or is that Naccinārkkiniyar's overlay? The words do not say.
4. **Why is காலை the one சிறுபொழுது with no திணை?** Five of six hours are assigned; mid-morning is not.
5. **குடிநிலை or துடிநிலை** at புறம் 4? Clan-state or drum-state — one letter, two quite different நூற்பா.
6. **Why does the received order of the landscapes differ from the நூற்பா's order?** And does the received order (குறிஞ்சி first) encode the developmental argument this edition's முன்னுரை makes at line 85?
7. **Why do the two outlier pairings come in reverse** (காஞ்சி/பெருந்திணை before பாடாண்/கைக்கிளை) when the inner five keep their order?
8. **Is கற்பு in கற்பியல் primarily a visibility condition or an interior state?** §7.4 puts this at risk; கற்பியல் would settle it.
9. **How do Ilampūraṇar's and Naccinārkkiniyar's divisions and readings differ across this iyal?** Only one commentator is available locally. Every "the commentary says" in this document means *this* commentary.
10. **Are the two commentary volumes' நூற்பா readings ever silently emended by the 1947 editor?** The footnoted `(பாடம்)` variants show the editor was tracking manuscript readings; whether the main text is ever a conjecture is not visible from the e-text.

---

## 11. Provenance ledger

Every Tamil line quoted above as மூலம், with its file and line, for grep verification:

| What | File | Line(s) |
|---|---|---|
| அகம் 1 — the seven | `pmuni0100-tholkappiyam-moolam.txt` | 2156–2157 |
| அகம் 2 — the middle five, minus the middlemost | same | 2158–2160 |
| அகம் 3 — முதல் கரு உரிப்பொருள் | same | 2161–2163 |
| அகம் 4 — முதல் = நிலம் + பொழுது | same | 2164–2165 |
| அகம் 5 — the four gods and lands | same | 2166–2171 |
| அகம் 6–12 — the பொழுது | same | 2172–2181 |
| அகம் 14 — திணை may mix, lands may not | same | 2184–2186 |
| அகம் 15 — the outer two mix freely | same | 2187 |
| அகம் 16 — the உரிப்பொருள் | same | 2188–2190 |
| அகம் 19 — முதல் is twofold | same | 2194 |
| அகம் 20 — the கரு | same | 2195–2197 |
| அகம் 21 — a flower out of its land | same | 2198–2200 |
| அகம் 25 — servants and labourers | same | 2207–2208 |
| அகம் 28, 33, 36 — உயர்ந்தோர் | same | 2213, 2222, 2226 |
| அகம் 31 — நால்வர் | same | 2220 |
| அகம் 37–38 — மகடூஉ | same | 2227–2229 |
| அகம் 39–45 — கூற்று | same | 2230–2284 |
| அகம் 49–50 — உள்ளுறை உவமம் | same | 2289–2292 |
| அகம் 53 — கைக்கிளை | same | 2296–2301 |
| அகம் 54 — பெருந்திணை | same | 2302–2305 |
| அகம் 55 — the earlier four | same | 2306 |
| அகம் 57–58 — no names / புறம் names | same | 2311–2314 |
| புறம் 1–2 — வெட்சி | same | 2317–2322 |
| புறம் 4 — கொற்றவை நிலை (குடி/துடி variant) | same | 2331–2332 |
| புறம் 6–7 — வஞ்சி | same | 2355–2357, 2370 |
| புறம் 8–9 — உழிஞை | same | 2371–2374 |
| புறம் 12 — தும்பை | same | 2396–2398 |
| புறம் 15–17 — வாகை | same | 2421–2432, 2456 |
| புறம் 18–19 — காஞ்சி | same | 2457–2459, 2495 |
| புறம் 20 — பாடாண் | same | 2496–2497 |
| புறம் 23 — காமப் பகுதி | same | 2505–2506 |
| அகநானூறு 4 — colophon and poem | `pmuni0490_01-ettuthogai-agananuru-p1a.txt` | 418–420, 423–439 |

Commentary passages are cited inline by file and line throughout; the two commentary files are `pmuni0500_01-…-urai-1.txt` (அகத்திணையியல்) and `pmuni0500_02-…-urai-2.txt` (புறத்திணையியல்).

**Dating.** Not settled and not settled here. `../varalaru/arivu-varalaru.md` §2 gives the spread by name — from ~700 BCE (இலக்குவனார், தெ.பொ. மீனாட்சிசுந்தரம்) to the 3rd century CE (ச. வையாபுரிப்பிள்ளை and several foreign scholars), with the multiple-author position spreading composition across 3rd c. BCE – 5th c. CE and இடைச்செருகல் (interpolation) held by many to be present in the received text. **Nothing in this document depends on a date.** Naccinārkkiniyar's commentary is conventionally placed in the 14th century CE; this printing is 1947/1955 (Saiva Siddhanta Works, Tirunelveli), digitised by Project Madurai.

---

## முடிவு | What this changes

For `../ilakkiyam/sangam.md` §1, three corrections are due:

1. **"ஐந்திணை — the five landscapes" should become seven, with the five named as the middle.** The two dropped ones are not curiosities; கைக்கிளை holds the first four beats of every love story (அகம் 55) and both outliers are the system's only exemptions from the landscape machinery (அகம் 15).
2. **The three-column table (திணை / land / inner state) should be marked as ranked, not parallel.** உரிப்பொருள் is the only non-droppable layer; the landscape is its carrier. `உரிப்பொருளின்றேற் பொருட் பய‌னின் றென்பது பெற்றாம்`
3. **The landscape↔inner-state pairing should be labelled as tradition, not as நூற்பா** — until §10 question 1 is answered — because it is not stated in the chapter that lays down the law of akam.

And one thing §1 already has right, which the நூற்பா now backs with a rule rather than a convention: **`சுட்டி ஒருவர்ப் பெயர் கொளப் பெறாஅர்`** — the lovers may not be pointed at by name. The universality of `செம்புலப் பெயனீர்` is not a happy accident of taste. It is அகம் 57.
