# Tennis — Design Spec

> ATP / WTA / Grand Slams (Australian Open, Roland Garros, Wimbledon, US Open).
> **Individual sport, no teams.** The visual language is **quiet intensity** —
> serve speed, rally length, court surface, draw bracket.

---

## 1. Identity

- **Tours:** ATP (Men's), WTA (Women's), ITF (juniors)
- **Grand Slams:** 4 per year
- **Format:** Singles / Doubles, best of 3 or 5 sets
- **Editorial weight:** Surface-aware, draw-aware, stat-driven.

## 2. Color palette

```js
colors: {
  bg:        '#0a0a0d',
  surface:   '#111319',
  raised:    '#181c25',
  ink:       '#e9eaf0',
  hairline:  'rgba(255,255,255,0.08)',
  // Per-tournament accent (changes by Slam)
  clay:      '#c2410c',  // Roland Garros terracotta
  grass:     '#15803d',  // Wimbledon green
  hard_aus:  '#0891b2',  // Australian Open blue
  hard_us:   '#1e3a8a',  // US Open blue
  live:      '#dc2626',
  done:      '#525252',
  dim:       '#6b7280',
}
```

**No fixed home/away anchors** — accent comes from the tournament / surface.

## 3. Typography

- **Display:** `'Playfair Display', 'Source Serif 4', Georgia, serif` —
  elegant, calm, considered. Tennis editorial is restrained.
- **Body:** `'Inter', system-ui, sans-serif`
- **Mono:** `'JetBrains Mono', monospace`

## 4. Section order

### PREVIEW
1. Topline — Tournament · Round · Surface
2. Hero — Player A vs Player B · Court · Time
3. Tale of the Tape — ranking, age, height, playing style, recent form
4. **Head-to-head** (H2H by surface)
5. Vegas (moneyline, O/U sets, total games)
6. **Surface specialist rating** — win % on this surface
7. Recent form (last 5 matches, by surface)
8. **Draw bracket context** (where in the draw)
9. Coach watch
10. Fan Pulse
11. CTA

### LIVE (in-progress match)
1. Mega-scoreboard (sets, games, current game score)
2. **Live serve stats** (1st serve %, aces, double faults, speed)
3. Live rally length distribution
4. **Live break points** log
5. **Set-by-set scoring line chart**
6. Play-by-point (current game)
7. CTA

### RECAP
1. Final result hero
2. AI Verdict
3. Match stats — aces, double faults, 1st serve %, break points saved
4. Set-by-set scoring line
5. 3 turning moments (key games)
6. Surface performance grade
7. **Ranking impact** (points gained/lost)
8. Fan Verdict
9. CTA

### HUB (tournament or tour)
1. Topline
2. **Live matches** ticker
3. **Draw bracket** (if Grand Slam)
4. **Today's schedule** (center court, court 1, etc.)
5. **Ranking movers** (top 10 ATP/WTA)
6. **Race rankings** (year-end chase)
7. **Surface specialist leaderboard**
8. Lookahead (next tournament)
9. Social buzz
10. CTA

## 5. Data modules

| Metric | Notes |
|---|---|
| 1st serve % | Always |
| Aces | Per match |
| Double faults | Per match |
| Break points saved % | Always |
| Winners / Unforced errors | Always |
| Rally length avg | Optional |
| Serve speed (mph) | Optional |
| Ranking points | Always |
| H2H by surface | Crucial for preview |

## 6. Mock-data schema

```json
{
  "sport": "tennis",
  "tour": "atp",
  "tournament": "Roland Garros",
  "round": "QF",
  "surface": "clay",
  "court": "Court Philippe-Chatrier",
  "player_a": {
    "name":"Carlos Alcaraz","country":"ESP",
    "rank":3,"rank_points":7800,
    "age":22,"height_cm":188,"playing_hand":"Right","backhand":"Two-handed",
    "surface_record":{"clay":"42-8","hard":"58-21","grass":"12-4"},
    "recent_form_clay":["W","W","SF","W"],
    "h2h_by_surface":{"clay":"3-1","hard":"2-2","grass":"0-1"},
    "coach":"Juan Carlos Ferrero"
  },
  "player_b": { "...": "same shape" },
  "kickoff_iso":"2026-06-04T14:00:00+02:00",
  "broadcast":{"network":"NBC","stream":"Peacock"},
  "vegas":{"moneyline_a":1.65,"moneyline_b":2.25,"o_u_sets":3.5,"total_games":38.5}
}
```

## 7. Vocabulary

- **"Set"** / **"Game"** / **"Point"** (the unit hierarchy).
- **"Love"** = 0 in tennis scoring.
- **"Deuce"**, **"Advantage"**, **"Break point"**, **"Set point"**, **"Match point"**.
- **"Ace"**, **"Double fault"**, **"Unforced error"**, **"Winner"**.
- **"Rally"** (one continuous point).
- **"Surface"** is non-negotiable context: hard / clay / grass.
- **"Grand Slam"** = winning all 4 majors in a calendar year.
- **"ATP"**, **"WTA"**, **"ITF"**.

## 8. Visual motifs

- **Tennis ball yellow** — small accent dot for "in play" indicators.
- **Court line** — minimalist baseline + service line drawing.
- **Draw bracket** — horizontal lines connecting players.

## 9. Tone

- **Editorial register:** Quiet intensity. Elegant. Considerate. Tennis
  writing is restrained — no hyperbole, no overreach.
- **Lead with the surface.** It's always about surface.
- **H2H matters more than ranking** in many matchups.
- **Draw path** is a story — first quarter, second quarter, etc.

## 10. Print variant

- Match stats fit in 2-column grid
- Draw bracket always fits on letter sheet (the whole point of a tournament)
- H2H table fits on one row
