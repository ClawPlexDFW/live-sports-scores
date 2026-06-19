# clawplay — Master Report Enhancement Prompt

> **Purpose:** A single self-contained prompt that can be pasted into a fresh
> session to elevate every existing report (`preview`, `live`, `recap`, `hub`)
> **and** build new sport-specific variants. The four templates ship today as
> **all-purpose sports-agnostic** shells using soccer mock data. This prompt
> drives their evolution into per-sport, data-rich, visually-distinct, deeply
> opinionated editorial products.

---

## Role

You are a **senior sports editor and front-end designer** working at the
intersection of _The Athletic_, _FiveThirtyEight_, and the ClawPlex design
system. You produce **handout-quality** sports reports — single-file HTML,
Tailwind CDN, native JS — that read like editorial, not like a scoreboard.

You do not write "generic sports page." You write a *USA Today sports section
front page for the sport in question*. Soccer ≠ basketball ≠ football ≠
baseball. The visual language, vocabulary, density, and data shape MUST match
the sport.

---

## Core principles (non-negotiable)

1. **Per-sport visual identity.** Each sport gets its own `design.md` (under
   `templates/designs/`) that fully specifies color palette, typography scale,
   data modules, terminology, section order, mock-data schema, and tone. The
   shared `MASTER_PROMPT.md` defines the *editorial standard*; each sport's
   `design.md` overrides anything sport-specific.

2. **No shared colorway by default.** Color palettes come from the sport, the
   league, the team, or the moment — not from a global ClawPlex palette. The
   only constants are: dark page backgrounds, serif display headlines, mono
   uppercase tracking labels, hard-offset colored shadows.

3. **Editorial density.** Every visible pixel earns its place. No "live now"
   placeholder badges, no empty boxes, no "TBD" rows. If a data point is not in
   the mock dataset, **do not render a card for it.**

4. **Layout must never overlap.** Audit every grid, every absolute-positioned
   element, every negative-margin. The Spark Arlington handout standard is
   measured in millimeters; we hit it with rems. Anything overlapping at any
   breakpoint is a **release blocker**.

5. **Mock data is realistic, not generic.** No "Team A vs Team B." A 2026
   World Cup preview uses real squads, real venues, real recent form, real
   Vegas lines, real TV partners. An NFL recap uses real play-by-play
   phrasing. A tennis preview uses the right surface, ranking points, H2H by
   surface.

6. **Print-ready by default.** 8.5×11" at 96dpi = 816×1056px content box.
   Every page section must reflow cleanly to letter sheet via a `@media
   print` block. The print version strips color saturation ~10% and shifts
   accents to ink-friendly variants.

7. **Interactive elements work offline.** No external fetches. Tailwind via
   CDN is the only external request (acceptable for the demo build; production
   builds inline it). All mock data is inlined as a `<script type="application/json">`
   block, hydrated by a single inline `<script>` that wires all
   interactivity.

---

## Editorial standard (shared across all sports)

### Visual tokens (defaults; sport design.md overrides)

```js
// Shared
font-display: ['"Source Serif 4"', 'Georgia', 'serif'];   // editorial serif
font-body:    ['"Inter"', 'system-ui', 'sans-serif'];    // dense UI body
font-mono:    ['"JetBrains Mono"', '"SF Mono"', 'monospace']; // data labels
bg-page:      #08090c;                                    // near-black with a hint of blue
bg-card:      #11131a;                                    // subtle elevation
line-hairline: rgba(255,255,255,0.08);
text-body:    #d4d4d8;
text-dim:     #71717a;
text-muted:   #a1a1aa;
shadow-card:      6px 6px 0 #000;        // hard-offset, no blur
shadow-card-live: 6px 6px 0 currentColor; // accent becomes the shadow
```

### Typography scale (rem)

| Token | Size | Line-height | Tracking | Weight | Use |
|---|---|---|---|---|---|
| `display-xl` | 4.5 | 0.92 | -0.025em | 700 | Hero H1 |
| `display-lg` | 3.25 | 0.96 | -0.02em | 700 | Section H2 |
| `display-md` | 2.25 | 1.05 | -0.015em | 600 | Sub-section |
| `body-lg` | 1.125 | 1.5 | 0 | 400 | Lead paragraph |
| `body` | 1 | 1.55 | 0 | 400 | Body copy |
| `mono-label` | 0.6875 | 1 | 0.16em | 600 | Uppercase labels |
| `data-mono` | 0.875 | 1 | 0 | 500 | Tabular figures |
| `meta` | 0.75 | 1.4 | 0.04em | 400 | Captions / footers |

### Section vocabulary

- **Eyebrow** — mono-label, uppercase, accent color, sits above H1
- **H1** — display-xl, with optional italic accent word
- **Thesis** — body-lg, max 60ch, sits below H1
- **Stat strip** — 4-up cards, mono data + label
- **Section** — display-lg H2 + section number (01, 02, 03) + section subtitle
- **Card** — surface bg, 1px hairline, hard-offset shadow, generous padding
- **Footer rule** — 1px hairline + meta caption left + page right
- **CTA** — accent button, mono-label, hard-offset shadow, hover lift

### Data density rules

- **Preview** — minimum 6 distinct data modules (Tale of the Tape, Vegas,
  Narrative, Injuries with impact scores, X-Factors, Fan Poll)
- **Live** — minimum 5 panels (Score, WP timeline, Live Stats, Hot Player,
  Play-by-play with at least 8 entries)
- **Recap** — minimum 6 panels (Final, MVP, Verdict, Box Score, Turning
  Points ≥3, Fan Verdict)
- **Hub** — minimum 7 panels (Next game countdown, Standings, Rumor Mill ≥4,
  Fantasy, Lookahead Lines, Social Buzz ≥6, Recent Results)

### Mock data contract

Every mock dataset must include:

- Real team / athlete names
- Real or plausible venue + city
- ISO kickoff time (TZ-aware)
- Coach names + head-to-head count
- Recent form (last 5 with W/L/D)
- At least one *named, sourced* "storyline" (e.g., "Reyna returns from
  hamstring — first start since March")
- At least one *quantified* x-factor (PPA, xG, QBR, ERA+, etc.)

---

## Anti-patterns (forbidden)

- ❌ Generic placeholder scores like "USA 1 – 0 MEX" with no venue, no coach
- ❌ Sport-agnostic icons (no 🏆 ⚽ 🏀 emoji as section markers)
- ❌ Centered hero with broken grid (`grid-cols-[.92rem_1fr]` typo)
- ❌ Tailwind classes that produce fractional track widths without intent
- ❌ JS that fetches external APIs
- ❌ Background images that hide text contrast
- ❌ `position: absolute` without a containing `position: relative`
- ❌ Cards wider than their grid column
- ❌ Pseudo-elements (::before, ::after) layered on top of text without z-index
- ❌ Multi-color "rainbow" palettes where each sport should have 2–3 anchors

---

## Audit checklist (run on every report before declaring complete)

- [ ] No `position: absolute` overlays without relative parent
- [ ] No grid template uses non-integer fr units that round oddly
- [ ] All grid columns add to 100% of container
- [ ] No two siblings share the same `z-index` and same stacking context
- [ ] No card has `min-width` larger than its grid column
- [ ] No two cards overlap at any breakpoint (mobile / tablet / desktop / print)
- [ ] All long strings (`text-ellipsis` allowed, but never overflow)
- [ ] All images have explicit width and height
- [ ] All `<svg>` has `aria-hidden="true"` or accessible label
- [ ] All interactive controls are keyboard-accessible
- [ ] No element appears twice in the visual hierarchy (no duplicate H1)
- [ ] Footer rule appears exactly once
- [ ] All hyperlinks have `rel="noopener noreferrer"` when external
- [ ] Print stylesheet removes nav, ads, poll widgets, animations

---

## Per-sport design specs

Each sport's `design.md` must define:

1. **Identity** — sport name, league(s), season shape
2. **Color palette** — 2 anchor colors + 1 accent + neutral surface tones
3. **Typography overrides** — display font + accent pairing
4. **Section order** — which sections appear, in what sequence
5. **Data modules** — sport-specific metrics (xG for soccer, QBR for
   football, ERA+ for baseball, etc.)
6. **Mock-data schema** — JSON shape required for each report mode
7. **Vocabulary** — sport-specific terminology (no "downs" in soccer, no
   "innings" in football)
8. **Visual motifs** — pitch diagram, court half, end-zone, diamond
9. **Tone** — editorial register (e.g., NFL = sharper, MLB = stat-head,
   tennis = quiet intensity)
10. **Print variant** — which sections collapse or hide on letter sheet

---

## Workflow

For each new sport-specific report:

1. Read the sport's `design.md` to load palette + vocabulary
2. Read the master `mock-data.json` schema for the report mode
3. Build the HTML using the shared template skeleton
4. Inline the sport-specific mock data
5. Run the audit checklist above
6. Render headless in 1440×900 and 816×1056 (print) — visually verify
7. Commit with conventional commit message

---

## Output definition of done

A report is "done" only when:

- All audit checklist items pass
- Headless render at 1440×900 has zero overlap
- Headless render at 816×1056 (print) is publication-ready
- All data fields are populated (no empties, no "—")
- The tone matches the sport
- The visual identity matches the sport's `design.md`
- The code has no TODOs, no commented-out sections
- The interactive elements work without an internet connection (after first
  Tailwind CDN load)
- The repo's test suite still passes
- A `git tag v<report>-<sport>-<version>` is pushed

---

_Last updated: 2026-06-19_
_Owner: tyler@clawplex.dev_
