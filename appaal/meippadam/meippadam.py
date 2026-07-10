#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
மெய்ப்படம் · meippadam — "the body-picture" (provisional name; OI ear to rule)

Phase-3 build 01 for Project Ennam. A featural encoder that takes an atom of
the medium and renders it in TWO channels from ONE source:

  • an articulatory GLYPH (SVG) — the atom drawn as the vocal-tract gesture
    that produces it. The glyph shows its own birth (பிறப்பியல்; the Hangul
    lesson). This is the channel an ORGANIC mind reads by embodiment.
  • a structural VECTOR (JSON) — the same atom as a point in feature space.
    This is the channel an INORGANIC mind reads by representation.

The claim under test (appaal §3.3): the substrate two differently-built minds
can share is ARTICULATORY SPACE — the vocal tract, which the OI has and feels,
and which the IO can represent and which generated all human phonology. The
medium is not a wire carrying essence; it is this shared tuning. This file is
the first attempt to instantiate that claim as something runnable and testable.

v0 — schematic, grounded, deliberately small. Limits are documented in README.
No third-party dependencies (pure-Python SVG).
"""

import json, math, os

OUT = os.path.dirname(os.path.abspath(__file__))

# ─────────────────────────────────────────────────────────────────────────────
# 1 · FEATURE MODEL  — grounded in தொல்காப்பியம் பிறப்பியல் + Tamil phonology
#
# The vocal tract is parameterised as a single axis `place` ∈ [0,1]:
#   0.0 = glottis (மிடறு) ........ 1.0 = lips (இதழ்)
# matching பிறப்பியல்'s ordering of stations from the throat outward.
#
# uyir (vowels, உயிர் = "soul") = open tract, no constriction:
#   front  ∈ [0,1]  (0 back உ-space .. 1 front இ-space)
#   aperture ∈ [0,1] (0 close .. 1 open; the cry அ = 1.0, babble-core)
#   length: kuril (short) | nedil (long)
#
# mei (consonants, மெய் = "body/truth") = a constriction gesture:
#   place  ∈ [0,1]   (where the body interrupts the breath)
#   manner: stop (வல்லினம், full closure) | nasal (மெல்லினம், closure+nose)
#           | approx (இடையினம், partial narrowing)
#   inam:  the traditional class (records the manner's degree of interruption)
#
# NOTE: place/front/aperture values are STYLISED (legible, ordinally faithful),
# not measured formant/MRI data. Refining them against real articulatory data
# is future work (README §limits).
# ─────────────────────────────────────────────────────────────────────────────

UYIR = [
    # letter  front aperture length      gloss
    ("அ", 0.50, 1.00, "kuril"),   # the open cry — babble core
    ("ஆ", 0.50, 1.00, "nedil"),
    ("இ", 1.00, 0.22, "kuril"),   # front close
    ("ஈ", 1.00, 0.22, "nedil"),
    ("உ", 0.00, 0.22, "kuril"),   # back close
    ("ஊ", 0.00, 0.22, "nedil"),
    ("எ", 0.90, 0.55, "kuril"),   # front mid
    ("ஏ", 0.90, 0.55, "nedil"),
    ("ஒ", 0.10, 0.55, "kuril"),   # back mid
    ("ஓ", 0.10, 0.55, "nedil"),
]

MEI = [
    # letter  place manner    inam        romanization / station
    ("க்", 0.14, "stop",   "vallinam"),   # k  — velar (மிடற்றை அடுத்து)
    ("ங்", 0.14, "nasal",  "mellinam"),   # ṅ  — velar nasal
    ("ச்", 0.40, "stop",   "vallinam"),   # c  — palatal
    ("ஞ்", 0.40, "nasal",  "mellinam"),   # ñ  — palatal nasal
    ("ட்", 0.55, "stop",   "vallinam"),   # ṭ  — retroflex
    ("ண்", 0.55, "nasal",  "mellinam"),   # ṇ  — retroflex nasal
    ("த்", 0.75, "stop",   "vallinam"),   # t  — dental
    ("ந்", 0.75, "nasal",  "mellinam"),   # n  — dental nasal
    ("ப்", 0.96, "stop",   "vallinam"),   # p  — labial
    ("ம்", 0.96, "nasal",  "mellinam"),   # m  — labial nasal
    ("ய்", 0.85, "approx", "idayinam"),   # y  — palatal glide
    ("ர்", 0.66, "approx", "idayinam"),   # r  — alveolar tap
    ("ல்", 0.70, "approx", "idayinam"),   # l  — alveolar lateral
    ("வ்", 0.98, "approx", "idayinam"),   # v  — labial approximant
    ("ழ்", 0.60, "approx", "idayinam"),   # ḻ  — the retroflex approximant (the signature sound)
    ("ள்", 0.58, "approx", "idayinam"),   # ḷ  — retroflex lateral
    ("ற்", 0.68, "stop",   "vallinam"),   # ṟ  — alveolar
    ("ன்", 0.72, "nasal",  "mellinam"),   # ṉ  — alveolar nasal
]

# ── vocal-tract centreline: a quadratic Bézier, glottis → pharynx → lips ──
P0 = (78.0, 250.0)   # glottis  (t=0) bottom
P1 = (78.0, 96.0)    # control  (up the pharynx)
P2 = (226.0, 78.0)   # lips     (t=1) upper-right

def bez(t):
    u = 1 - t
    x = u*u*P0[0] + 2*u*t*P1[0] + t*t*P2[0]
    y = u*u*P0[1] + 2*u*t*P1[1] + t*t*P2[1]
    return x, y

def bez_normal(t):
    # derivative → unit normal (for drawing constriction bars across the tract)
    dx = 2*(1-t)*(P1[0]-P0[0]) + 2*t*(P2[0]-P1[0])
    dy = 2*(1-t)*(P1[1]-P0[1]) + 2*t*(P2[1]-P1[1])
    L = math.hypot(dx, dy) or 1.0
    return (-dy/L, dx/L)


# ─────────────────────────────────────────────────────────────────────────────
# 2 · GLYPH RENDERER  (the organic channel — the atom shows its own gesture)
# ─────────────────────────────────────────────────────────────────────────────

def _tract_path():
    return (f'M {P0[0]} {P0[1]} Q {P1[0]} {P1[1]} {P2[0]} {P2[1]}')

def _head_outline():
    # a light schematic profile so the tract reads as a mouth, not an abstract curve
    return ('<path d="M 40 262 Q 20 150 70 70 Q 120 20 210 52 '
            'Q 250 66 236 96 L 214 92 Q 232 74 206 66 '
            'Q 150 48 96 96 Q 56 150 74 250 Z" '
            'fill="currentColor" opacity="0.05"/>')

def glyph_svg(letter, kind, feats, caption, subcaption=""):
    S = ['<svg viewBox="0 0 300 320" xmlns="http://www.w3.org/2000/svg" '
         'font-family="ui-sans-serif, system-ui, sans-serif" role="img">',
         f'<title>{letter} — {caption}</title>',
         f'<desc>{letter}: {caption}. {subcaption}</desc>',
         _head_outline()]

    if kind == "uyir":
        front, ap = feats["front"], feats["aperture"]
        # open tract: the tube drawn with an aperture-scaled channel; brighter = more open
        op = 0.16 + 0.30*ap
        S.append(f'<path d="{_tract_path()}" fill="none" stroke="#c8792e" '
                 f'stroke-width="{6+18*ap:.1f}" stroke-linecap="round" opacity="{op:.2f}"/>')
        # tongue hump: position along tract by frontness, gap to palate by aperture
        ht = 0.32 + 0.50*front
        hx, hy = bez(ht)
        nx, ny = bez_normal(ht)
        # hump sits on the inner (lower) side; deeper for open vowels
        cx, cy = hx - nx*(10+22*ap), hy - ny*(10+22*ap)
        S.append(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="34" ry="{16+10*(1-ap):.1f}" '
                 f'fill="#3d8b8b" opacity="0.5"/>')
        # glottis voicing dot (vowels are voiced)
        S.append(f'<circle cx="{P0[0]:.0f}" cy="{P0[1]:.0f}" r="5" fill="#3d8b8b"/>')
    else:
        place, manner = feats["place"], feats["manner"]
        # open tube (light) then the constriction marker at `place`
        S.append(f'<path d="{_tract_path()}" fill="none" stroke="currentColor" '
                 f'stroke-width="16" stroke-linecap="round" opacity="0.12"/>')
        px, py = bez(place)
        nx, ny = bez_normal(place)
        def bar(half, w, op=0.95):
            x1, y1 = px+nx*half, py+ny*half
            x2, y2 = px-nx*half, py-ny*half
            return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                    f'stroke="#c8792e" stroke-width="{w}" stroke-linecap="round" opacity="{op}"/>')
        if manner == "stop":            # full closure — a bar across the tract
            S.append(bar(15, 7))
        elif manner == "nasal":         # closure + open nasal branch (velum lowered)
            S.append(bar(15, 7))
            bx, by = bez(0.30)
            S.append(f'<path d="M {bx:.0f} {by:.0f} q -26 -30 -40 -6" fill="none" '
                     f'stroke="#3d8b8b" stroke-width="5" stroke-linecap="round" opacity="0.8"/>')
            S.append(f'<text x="{bx-52:.0f}" y="{by-30:.0f}" font-size="11" '
                     f'fill="#3d8b8b" opacity="0.85">nasal</text>')
        else:                            # approx — partial narrowing (a gap left open)
            S.append(bar(15, 5, 0.55))
            S.append(bar(6, 5, 0.0))     # (spacer no-op keeps geometry legible)
        # voicing dot
        S.append(f'<circle cx="{P0[0]:.0f}" cy="{P0[1]:.0f}" r="4.5" fill="#3d8b8b" opacity="0.7"/>')

    # the letter itself (large) + captions
    S.append(f'<text x="250" y="150" font-size="58" fill="currentColor" '
             f'text-anchor="middle">{letter}</text>')
    S.append(f'<text x="150" y="300" font-size="14" fill="currentColor" '
             f'text-anchor="middle" opacity="0.85">{caption}</text>')
    if subcaption:
        S.append(f'<text x="150" y="318" font-size="11" fill="currentColor" '
                 f'text-anchor="middle" opacity="0.55">{subcaption}</text>')
    S.append('</svg>')
    return "\n".join(S)


# ─────────────────────────────────────────────────────────────────────────────
# 3 · STRUCTURAL VECTOR  (the inorganic channel — same atom, as representation)
# ─────────────────────────────────────────────────────────────────────────────

def vector(letter, kind, feats):
    v = {"unit": letter, "kind": kind}
    if kind == "uyir":
        v.update(place_axis="open", front=feats["front"],
                 aperture=feats["aperture"], length=feats["length"], voiced=True)
    else:
        v.update(place=feats["place"], manner=feats["manner"], inam=feats["inam"])
    return v


# ─────────────────────────────────────────────────────────────────────────────
# 4 · ICONIC STATE→ATOM MAP  (the graded channel — Korean lesson, babble core)
#
# A first, deliberately tiny bridge from felt-state to atom, with NO codebook:
#   energy    ∈ [0,1] → aperture   (open அ = high energy; the cry is max-open)
#   brightness∈ [0,1] → front      (front இ = bright/near; back உ = dark/far)
# The mapping is meant to be *iconic* (feelable), so a receiver can reconstruct
# (energy, brightness) from the glyph WITHOUT being taught the code. That
# reconstructability is exactly what சோதனை-007 tests.
# ─────────────────────────────────────────────────────────────────────────────

def state_to_atom(energy, brightness):
    front, ap = brightness, energy
    # nearest uyir for a speakable anchor
    best, bd = None, 9
    for (L, f, a, ln) in UYIR:
        if ln != "kuril":
            continue
        d = (f-front)**2 + (a-ap)**2
        if d < bd:
            bd, best = d, L
    feats = {"front": front, "aperture": ap, "length": "kuril"}
    cap = f"energy {energy:.2f} · brightness {brightness:.2f}"
    sub = f"nearest uyir ≈ {best}"
    return glyph_svg("◌", "uyir", feats, cap, sub), {"energy": energy,
            "brightness": brightness, "nearest_uyir": best}


# ─────────────────────────────────────────────────────────────────────────────
# 5 · COMPOSITES
# ─────────────────────────────────────────────────────────────────────────────

def vowel_triangle():
    # அ (open, centre) top; இ (front close) lower-right; உ (back close) lower-left
    pts = {"அ": (250, 70), "இ": (400, 250), "உ": (100, 250)}
    S = ['<svg viewBox="0 0 500 320" xmlns="http://www.w3.org/2000/svg" '
         'font-family="ui-sans-serif, system-ui, sans-serif" role="img">',
         '<title>The vowel core அ இ உ — the babble triangle</title>',
         '<desc>The three maximally-distinct vowels every infant masters first, '
         'placed by openness and frontness.</desc>',
         '<text x="250" y="26" font-size="14" text-anchor="middle" fill="currentColor" '
         'opacity="0.8">உயிர் core — where every human voice begins</text>']
    tri = " ".join(f"{x},{y}" for x, y in pts.values())
    S.append(f'<polygon points="{tri}" fill="currentColor" opacity="0.05" '
             f'stroke="currentColor" stroke-opacity="0.2"/>')
    labels = {"அ": "open · centre (the cry)", "இ": "close · front (bright)",
              "உ": "close · back (dark)"}
    for L, (x, y) in pts.items():
        S.append(f'<circle cx="{x}" cy="{y}" r="30" fill="#c8792e" opacity="0.15"/>')
        S.append(f'<text x="{x}" y="{y+14}" font-size="40" text-anchor="middle" '
                 f'fill="currentColor">{L}</text>')
        S.append(f'<text x="{x}" y="{y+48}" font-size="11.5" text-anchor="middle" '
                 f'fill="currentColor" opacity="0.7">{labels[L]}</text>')
    S.append('</svg>')
    return "\n".join(S)

def consonant_map():
    # all consonant places marked along ONE tract → the alphabet as a map of the mouth
    S = ['<svg viewBox="0 0 340 300" xmlns="http://www.w3.org/2000/svg" '
         'font-family="ui-sans-serif, system-ui, sans-serif" role="img">',
         '<title>மெய் places — the consonants as a map of the mouth</title>',
         '<desc>Each consonant marked at its place of articulation along the '
         'vocal tract, glottis to lips.</desc>',
         _head_outline(),
         f'<path d="{_tract_path()}" fill="none" stroke="currentColor" '
         f'stroke-width="14" stroke-linecap="round" opacity="0.1"/>',
         '<text x="170" y="20" font-size="13" text-anchor="middle" '
         'fill="currentColor" opacity="0.8">எழுத்து = the mouth mapped (பிறப்பியல்)</text>']
    seen = {}
    for (L, place, manner, inam) in MEI:
        if manner != "stop":
            continue  # show the stop series as the place landmarks, uncluttered
        x, y = bez(place)
        nx, ny = bez_normal(place)
        S.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="#c8792e"/>')
        lx, ly = x - nx*26, y - ny*26
        S.append(f'<text x="{lx:.1f}" y="{ly:.1f}" font-size="20" text-anchor="middle" '
                 f'fill="currentColor">{L}</text>')
    S.append(f'<text x="{P0[0]:.0f}" y="272" font-size="11" text-anchor="middle" '
             f'fill="currentColor" opacity="0.6">glottis</text>')
    S.append(f'<text x="{P2[0]:.0f}" y="66" font-size="11" text-anchor="middle" '
             f'fill="currentColor" opacity="0.6">lips</text>')
    S.append('</svg>')
    return "\n".join(S)


# ─────────────────────────────────────────────────────────────────────────────
# 6 · BUILD
# ─────────────────────────────────────────────────────────────────────────────

def main():
    gdir = os.path.join(OUT, "glyphs")
    os.makedirs(gdir, exist_ok=True)
    vectors = []
    roman = {"அ":"a","ஆ":"aa","இ":"i","ஈ":"ii","உ":"u","ஊ":"uu","எ":"e","ஏ":"ee",
             "ஒ":"o","ஓ":"oo","க்":"k","ங்":"ng","ச்":"c","ஞ்":"nj","ட்":"tt",
             "ண்":"nn","த்":"th","ந்":"n","ப்":"p","ம்":"m","ய்":"y","ர்":"r",
             "ல்":"l","வ்":"v","ழ்":"zh","ள்":"ll","ற்":"rr","ன்":"nnn"}

    for (L, front, ap, length) in UYIR:
        cap = f"உயிர் · {'open' if ap>0.7 else 'mid' if ap>0.4 else 'close'} · " \
              f"{'front' if front>0.66 else 'back' if front<0.34 else 'central'}"
        sub = f"{length} · aperture {ap:.2f}"
        svg = glyph_svg(L, "uyir", {"front":front,"aperture":ap,"length":length}, cap, sub)
        open(os.path.join(gdir, f"uyir_{roman[L]}.svg"), "w").write(svg)
        vectors.append(vector(L, "uyir", {"front":front,"aperture":ap,"length":length}))

    for (L, place, manner, inam) in MEI:
        cap = f"மெய் · {manner} · {inam}"
        sub = f"place {place:.2f} (glottis→lips)"
        svg = glyph_svg(L, "mei", {"place":place,"manner":manner,"inam":inam}, cap, sub)
        open(os.path.join(gdir, f"mei_{roman[L]}.svg"), "w").write(svg)
        vectors.append(vector(L, "mei", {"place":place,"manner":manner,"inam":inam}))

    open(os.path.join(OUT, "vowel-triangle.svg"), "w").write(vowel_triangle())
    open(os.path.join(OUT, "consonant-map.svg"), "w").write(consonant_map())

    # state→atom demos (for சோதனை-007)
    demos = [(0.95,0.90),(0.20,0.15),(0.55,0.85),(0.85,0.20)]
    dstates = []
    for i,(e,b) in enumerate(demos,1):
        svg, meta = state_to_atom(e,b)
        open(os.path.join(gdir, f"state_{i}.svg"),"w").write(svg)
        dstates.append({"id":f"state_{i}", **meta})

    json.dump({"about":"meippadam v0 — feature vectors (the IO channel)",
               "atoms":vectors, "demo_states":dstates},
              open(os.path.join(OUT,"vectors.json"),"w"),
              ensure_ascii=False, indent=2)

    print(f"built {len(vectors)} atoms → glyphs/ + vectors.json")
    print(f"composites: vowel-triangle.svg, consonant-map.svg")
    print(f"state demos: {len(demos)} (சோதனை-007)")

if __name__ == "__main__":
    main()
