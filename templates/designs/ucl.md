# UCL — Design Spec

> UEFA Champions League. 36-team league phase (since 2024-25), top 8
> advance directly to R16, 9-24 enter knockout play-offs, the Final in May.
> **Editorial register: cathedral.** This is the highest-stakes club
> competition in the world. Treat it accordingly.

---

## 1. Identity

- **League:** UEFA Champions League (36 teams in league phase)
- **Season:** September → May
- **Format:** League phase (8 matchdays, no groups) → R16 → QF → SF → Final
- **Editorial weight:** Highest of any club competition.

## 2. Color palette

```js
colors: {
  bg:        '#0a0a0d',
  surface:   '#11141d',
  raised:    '#181c28',
  ink:       '#eaeaf2',
  hairline:  'rgba(255,255,255,0.08)',
  home:      '#0a1f5c',  // UCL midnight blue
  away:      '#fbe122',  // star-ball gold
  accent:    '#1e88ff',  // UEFA blue
  live:      '#dc2626',
  done:      '#525252',
  dim:       '#6b7280',
}
```

**Midnight blue + star-ball gold** — the two colors of the iconic Champions
League brand identity.

## 3. Typography

- **Display:** `'Cinzel', 'Source Serif 4', Georgia, serif` — wide-spaced
  capital letters for stadium, club, competition headers
- **Body:** `'Inter', system-ui, sans-serif`
- **Mono:** `'JetBrains Mono', monospace`

## 4. Section order

### PREVIEW
1. Topline — matchday · KO · broadcaster
2. Hero — matchup + KO + broadcaster
3. Stat strip
4. **Tale of the Tape** — record (UCL + domestic), xG, xGD
5. **The European Night** — UEFA coefficient rank, last 5 European campaigns
6. **Tactical** — formation, key battle, expected XI
7. Vegas
8. Injury report (international duty)
9. Head-to-head (all-time European)
10. Fan Pulse
11. CTA

### LIVE
1. Mega-scoreboard
2. Live xG chart
3. Live stats
4. Live shot map
5. Live pressure map
6. Play-by-play
7. CTA

### RECAP
1. Final score hero
2. AI Verdict
3. Player ratings
4. Box score
5. 3 turning moments
6. Tactical analysis
7. Knockout implications
8. Fan Verdict
9. CTA

### HUB
1. Topline
2. Next matchday countdown
3. League Phase table (top 24)
4. Knockout bracket projection
5. Top scorers (Golden Boot race)
6. Manager watch
7. Transfer / injury watch
8. Lookahead lines
9. Social buzz
10. CTA

## 5. Data modules

Same as EPL + UEFA-specific:
- **UEFA coefficient**
- **League Phase position** (1-36)
- **Goals scored in UCL**
- **Knockout history**

## 6. Mock-data schema

```json
{
  "sport": "ucl",
  "season": "2025-26",
  "matchday": 4,
  "phase": "league",
  "home": {
    "team":"Real Madrid","abbr":"RMA",
    "stadium":"Santiago Bernabéu","city":"Madrid",
    "uefa_coeff":127.0,"uefa_coeff_rank":1,
    "league_phase_record":"2-0-1","league_phase_xgd":4.2,
    "form":["W","W","D"],
    "manager":"Carlo Ancelotti"
  }
}
```

## 7. Vocabulary

- **"Matchday"** in league phase, **"Round of 16"** in knockouts.
- **"League Phase"** (new since 2024-25, replaced group stage).
- **"Knockout play-offs"** = 9-24 seeds play home-and-away for R16 spots.
- **"Quarter-final"**, **"Semi-final"**, **"Final"** (no abbreviations in titles).
- **"The European Cup"** = historical name for UCL.
- **"Champions League nights"** is a vibe word — use it.
- **"El Clásico"** = Real Madrid vs Barcelona.

## 8. Visual motifs

- **Star-ball** — geometric star pattern as a section marker (subtle).
- **Stadium arch** — single arc line as a hero accent.

## 9. Tone

- **Editorial register:** Cathedral-like. Reverent. This is the biggest stage.
- **Lead with history.** UCL teams have European heritage — surface it.
- **Manager pedigree matters.** Ancelotti, Ferguson, Guardiola — they're characters.
- **No excuses for big teams.** Tone is unforgiving for giants who lose.

## 10. Print variant

- League phase table truncates to top 18 (knockout zone) + bottom 6 (eliminated)
- Knockout bracket always fits on letter sheet
