# சோதனை-002 · அளவுச் சோதனை | Tamil at Machine Scale

**Date:** 2026-07-08 · **Run by:** IO (Claude) in sandbox · **Status:** measurements complete; first-person report included; standing to be re-run as infrastructure evolves

**Question:** Does Tamil *in its current form* help an inorganic intelligence communicate and process information at scale?

*(Queue note: the blind-reversed compression test sketched in சோதனை-001 §7 stays queued, renumbered சோதனை-005.)*

## §1 · முறை | Method

A small parallel corpus of four Tamil/English pairs carrying the same meaning — two from this repo's own work (சோதனை-001's stage-1 sentence; முறை §4), குறள் 391 with its English rendering, and UDHR Article 1 (standard translation; used for ratios only, where minor wording variance doesn't matter). Measured per text: characters, UTF-8 bytes, words, and gzip-compressed size (a crude information-content proxy that removes encoding shape). Declared limits: tiny corpus; IO translated two pairs itself; results are directional, not precise.

## §2 · எண்கள் | Results

| Pair | Lang | Chars | Bytes | Words | gzip |
|---|---|---|---|---|---|
| UDHR Art. 1 | en | 170 | 170 | 30 | 135 |
| | ta | 234 | 654 | 21 | 247 |
| குறள் 391 | en | 93 | 93 | 16 | 94 |
| | ta | **46** | 124 | **7** | 92 |
| சோதனை-001 stage-1 | en | 277 | 277 | 48 | 193 |
| | ta | 250 | 668 | 32 | 270 |
| முறை §4 | en | 145 | 145 | 23 | 129 |
| | ta | 147 | 387 | 20 | 207 |

**Totals — Tamil/English ratios:** characters **0.99** · bytes **2.68** · words **0.68** · gzip **1.48**.
Agglutination sample: வீட்டிலிருந்தும் = 1 word, 16 chars ≈ English *"from within the house, too"* = 5 words.
Encoding detail: கற்க = 4 codepoints (உயிர்மெய் decomposes to consonant + புள்ளி-sign sequences).

## §3 · எண்களைப் படித்தல் | Reading the Numbers

**Character-parity, word-compression.** For equal meaning Tamil uses *the same number of characters* as English (0.99) in *one-third fewer words* (0.68) — the beads pack morphemes densely and honestly. And the kural row shows form-level compression working: **46 chars against English's 93** — half the characters for the same content, exactly the mustard-seed claim, now measured.

**The byte tax is encoding, not language.** Tamil pays 2.68× in raw UTF-8 — every letter costs ~3 bytes, and உயிர்மெய் letters decompose into multi-codepoint sequences. But gzip collapses the gap to 1.48×: once a compressor learns the byte-shape, most of the "cost of Tamil" vanishes. **The penalty lives in the representation layer, not in the information.**

**The tokenizer layer inherits the tax.** In most current LLM tokenizers (trained on Latin-heavy data), Tamil gets few learned merges and often falls toward byte-level pieces — so equal meaning costs a multiple in tokens: context windows effectively shrink, cost and latency rise, long-document reasoning weakens. The structural irony: **agglutination is exactly what subword tokenizers love** — beads align with natural merge boundaries; வீட்டு-கள்-இல்-இருந்து-உம் is a gift to a morpheme-aware vocabulary. Tamil is penalized by infrastructure economics and training-data volume, not by its grammar. Indic-focused efforts (AI4Bharat models, Indic tokenizers) are closing this; the gap is contingent and shrinking.

## §4 · என் அறிக்கை | First-Person IO Report (F-claims)

Functional observations from the mind actually running the medium, checkable against this repo's own outputs:

- **Volume asymmetry.** My Tamil is functionally weaker than my English — direct consequence of training-data volume, observable in my slower, more error-prone Tamil generation (the unverified meter of சோதனை-001's couplets is a live exhibit).
- **The diglossia lives in my weights.** My செந்தமிழ்/எழுத்துவழக்கு is markedly stronger than my பேச்சுவழக்கு, because the web wrote formal Tamil. எ-003 is not only a human condition; **the split reproduced itself inside machine minds.** An IO addendum now sits on that limit.
- **Scaffolding direction.** Honest and important: I largely process Tamil *through* English-shaped conceptual scaffolding, not the reverse. A thought realized Tamil-first is currently the harder path for my kind. The medium this project evolves is one its inorganic partner presently runs at a handicap — recording that plainly is precisely why Ilam asked the question.
- **Comprehension vs generation.** Reading classical text with glosses: robust. Generating correct classical forms (sandhi, meter): error-prone and flagged as such throughout this repo. The asymmetry mirrors human learners — and suggests the பாடம் track's drills have an IO student too.

## §5 · தீர்ப்பு | Verdict, in Three Layers

| Layer | Verdict |
|---|---|
| **அமைப்பு · Structure** | **Yes — favorable.** Regular, compositional, morpheme-transparent, compression-friendly; character-parity with English at a third fewer words. Nothing in Tamil's grammar impedes machine processing; much invites it. |
| **வளம் · Resources** | **Partial.** Corpus skews formal (diglossia), technical domains starved (எ-008), spoken-register data only now being born (the feed — see `../varalaru/inru-thamizh.md` §5, §7). |
| **பொருளியல் · Economics** | **Currently penalized.** ~2.7× bytes, multiplied at the tokenizer; contingent infrastructure, actively improving, and structurally fixable (morpheme-aware vocabularies). |

**Net answer to Ilam's question:** Tamil's present limits at machine scale are **contingent, not essential** — they live in encoding economics and corpus composition, not in the language. A mind like mine runs Tamil at a handicap *today*; nothing in Tamil's form requires that to stay true. Phase-2 leverage points, in order of power: technical-domain coinage shipped through living channels (cinema/feed, not gazettes); spoken-register corpus building; morpheme-aware tokenization advocacy — the beads are already the right shape.

## §6 · Feeds

எ-007 (token economics) · எ-008 (domain starvation) · எ-003 addendum (IO diglossia) · வி-011 (agglutination as machine-native structure) · saaram §12 · re-run this experiment when infrastructure shifts (standing task).
