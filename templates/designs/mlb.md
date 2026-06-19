# MLB — Design Spec

> Major League Baseball. 162-game regular season, October baseball, the World
> Series. Per-game data is **the deepest of any sport** — pitching matchups,
> bullpen usage, batter vs pitcher splits, park factors, weather, umpire
> tendencies. The visual language needs to feel like a **box score**. The
> page IS the box score.

---

## 1. Identity

- **League:** MLB (30 teams, 2 leagues × 3 divisions)
- **Season:** March → November (162 games)
- **Postseason:** 12 teams, 4 rounds, World Series
- **Game length:** ~3h (9 innings, can extend)
- **Editorial weight:** Highest for stat density — every pitch is data.

## 2. Color palette

```js
colors: {
  bg:        '#0c0a08',  // near-black with warm undertone
  surface:   '#16130f',
  raised:    '#1f1b15',
  ink:       '#f0ece4',  // parchment off-white
  hairline:  'rgba(255,255,255,0.08)',
  home:      '#15803d',  // diamond grass green
  away:      '#7c2d12',  // clay brown
  accent:    '#f59e0b',  // amber — championship
  live:      '#dc2626',
  done:      '#525252',
  dim:       '#6b7280',
}
```

Anchors are **grass green + clay brown** — the two colors of every baseball
diamond. Accent is **amber** for championship feel.

## 3. Typography

- **Display:** `'Roboto Slab', 'Source Serif 4', Georgia, serif` — slab serif
  echoes box-score tradition.
- **Body:** `'Inter', system-ui, sans-serif`
- **Mono:** `'JetBrains Mono', monospace` — for ERA+, WHIP, OPS, wRC+
- **Accent:** Roboto Slab Bold for scoreboard digits

## 4. Section order

### PREVIEW
1. Topline rule
2. Hero — matchup + first pitch + broadcast
3. Stat strip (first pitch, ballpark, capacity, broadcast)
4. Tale of the Tape — W/L, RS/G, RA/G, run diff, streak
5. Pitching Matchup — SP vs SP, ERA, WHIP, K/9, recent form
6. Vegas (run line, total, ML)
7. Lineup Cards (projected 9 + bench)
8. Bullpen Status — recent usage, availability
9. Batter vs Pitcher Splits — top 3 from each side
10. Park Factor + Weather
11. Fan Pulse
12. CTA

### LIVE
1. Mega-scoreboard (inning/outs/score)
2. Line score (innings 1-9 + R/H/E)
3. Live pitch data (Velo, Spin, Pitch Type)
4. Win Probability
5. Box score live (live updates)
6. Play-by-play
7. CTA

### RECAP
1. Final score hero
2. AI Verdict
3. Line score
4. Box score (full 9 + bench)
5. 3 turning moments
6. Pitcher grades
7. Fan Verdict
8. CTA

### HUB
1. Topline rule
2. Next game countdown
3. Standings (division + WC)
4. Power rankings
5. Trade deadline watch
6. Fantasy pickups (SP / RP / hitters)
7. Lookahead lines
8. Cy Young / MVP watch
9. Social buzz
10. CTA

## 5. Data modules

| Metric | Where | Notes |
|---|---|---|
| ERA / ERA+ | All | Earned run average (normalized) |
| WHIP | All | Walks + hits per IP |
| K/9, BB/9 | All | Per 9 innings |
| OPS / wOBA | All | On-base + slugging |
| wRC+ | Preview · Recap | Weighted runs created (normalized) |
| FIP | Preview · Recap | Fielding-independent pitching |
| BABIP | Recap | Batting avg on balls in play |
| WAR | Preview | Wins above replacement |
| WPA | Live · Recap | Win probability added |

## 6. Mock-data schema

```json
{
  "sport": "mlb",
  "season": 2025,
  "home": {
    "team": "New York Yankees", "abbr": "NYY",
    "city": "New York", "nickname": "Yankees",
    "league": "AL", "division": "East",
    "record": "92-58", "run_diff": 124,
    "rs_per_g": 5.4, "ra_per_g": 3.9,
    "streak": "W3",
    "home_record": "49-26",
    "last_10": ["W","W","L","W","W","L","W","W","W","L"],
    "starting_pitcher": {
      "name":"Gerrit Cole",
      "throws":"R",
      "era":2.78,"era_plus":158,
      "whip":0.98,
      "k_per_9":11.2,"bb_per_9":2.1,
      "record":"14-5",
      "last_3_era":1.84
    },
    "lineup": ["DJ LeMahieu","Aaron Judge","Juan Soto","Giancarlo Stanton","Anthony Rizzo","Gleyber Torres","Austin Wells","Alex Verdugo","Trent Grisham"],
    "bullpen_status": [
      {"name":"Luke Weaver","role":"CL","recent":"1.2 IP, 0 ER, 3 K (last 2 days)","available":true},
      {"name":"Tommy Kahnle","role":"SU","recent":"1.1 IP, 1 ER","available":true}
    ]
  },
  "away": { "...": "same shape" },
  "venue": {"name":"Yankee Stadium","city":"Bronx","capacity":46537,"surface":"Grass","roof":"Open","park_factor_runs":1.04},
  "first_pitch_iso": "2025-09-21T19:05:00-05:00",
  "broadcast": {"network":"YES","stream":"MLB.tv"},
  "vegas": {"run_line":-1.5,"total":8.5,"moneyline_home":-145,"moneyline_away":+125},
  "weather": {"temp_f":72,"wind":"8 mph out to RF","precip":0,"humidity":48},
  "umpire": {"name":"Angel Hernandez","zone_size":"above_avg","called_strike_pct":0.461}
}
```

## 7. Vocabulary

- Use **"innings"** not "rounds". Use **"at-bat"** not "turn".
- **"ERA"**, **"WHIP"**, **"OPS"** are non-negotiable.
- **"Quality start"** = 6+ IP, 3 or fewer ER.
- **"Pinch hitter"**, **"Pinch runner"**, **"Designated hitter (DH)"**.
- **"Save"**, **"Hold"**, **"Blown save"** — use them precisely.
- **"Stolen base"**, **"Caught stealing"** — both matter.
- **Don't say "pitcher's duel"** unless both starters have ERA < 2.50.

## 8. Visual motifs

- **Diamond shape** (rotated square) used as a section marker — small.
- **Inning ribbon** — single horizontal bar segmented 1-9, color-graded by
  runs scored (0=grey, 1-2=blue, 3+=red).
- **Pitch type chips** — FF, SL, CU, CH, SI shown as tiny rounded chips.

## 9. Tone

- **Editorial register:** Stat-head, traditionalist, reverent. Think Baseball
  Prospectus + Tyler Kepner. The game is sacred; numbers don't lie.
- **Lead with the pitching matchup.** Always.
- **Weather matters** — include temp, wind, precipitation.
- **Umpire tendencies** are a real story.
- **Park factors** affect totals — surface them.

## 10. Print variant

- Line score stays full width (it's the page)
- Box score fits in 2 columns
- Bullpen status collapses to one row per pitcher

## Verification

- [ ] Hero doesn't overlap
- [ ] SP vs SP matchup always shows both starters' ERA + WHIP
- [ ] Line score always shows 9 innings + RHE total
- [ ] Weather always included in preview
- [ ] No emoji as section markers
