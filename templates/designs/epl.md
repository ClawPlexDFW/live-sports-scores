# EPL — Design Spec

> English Premier League. 20 teams, 38-game season, the most-watched league
> in the world. **Editorial register: the most established in our system.**
> Soccer vocabulary is native. xG culture is mature. Matchweek is the rhythm.
> The page should feel like **The Athletic's tactical preview**.

---

## 1. Identity

- **League:** Premier League (20 teams)
- **Season:** August → May (38 matchweeks)
- **Editorial weight:** Highest for soccer — every match preview is an event.

## 2. Color palette

```js
colors: {
  bg:        '#08090d',
  surface:   '#11131a',
  raised:    '#181b24',
  ink:       '#e8eaf0',
  hairline:  'rgba(255,255,255,0.08)',
  home:      '#38003c',  // Premier League purple
  away:      '#04f5ff',  // EPL sky cyan
  accent:    '#ff2882',  // PL pink
  live:      '#dc2626',
  done:      '#525252',
  dim:       '#6b7280',
}
```

**Premier League purple + sky cyan** with **PL pink** as the signature accent.
Background is the deepest near-black in the system — for tactical density.

## 3. Typography

- **Display:** `'Source Serif 4', 'Playfair Display', Georgia, serif` —
  weighty, opinionated
- **Body:** `'Inter', system-ui, sans-serif`
- **Mono:** `'JetBrains Mono', monospace`

## 4. Section order

### PREVIEW
1. Topline (sport · matchweek · kickoff)
2. Hero — matchup + kickoff + broadcaster
3. Stat strip (kickoff, ground, capacity, broadcaster)
4. **The Tale of the Tape** — record, xGD, xG, xGA, possession, PPDA
5. **Vegas** (1X2, O/U, BTTS, Asian Handicap)
6. **Tactical** — formation, shape, expected lineup, key battle
7. **Recent Form** — last 5 with W/D/L dots + result text
8. **Set Piece Threat** — goals from corners / free kicks
9. **Head-to-head** — last 5 meetings
10. **Injuries + Suspensions**
11. **Fan Pulse** (predicted score, BTTS %, O/U pick)
12. CTA

### LIVE
1. Mega-scoreboard (clock/score)
2. Live xG chart
3. Live stats (shots, SOT, possession, xG, big chances)
4. Live shot map (SVG)
5. Live player heat map
6. Play-by-play (last 10 events)
7. CTA

### RECAP
1. Final score hero
2. AI Verdict
3. Player ratings (1-10 each, both teams)
4. Box score (pass % + duels + tackles)
5. 3 turning moments
6. Tactical analysis
7. Fan Verdict
8. CTA

### HUB
1. Topline
2. Next gameweek countdown
3. Premier League table (1-20 with GD + last 5)
4. Top 4 race / relegation battle
5. **Manager Pressure Index**
6. Transfer watch
7. Fantasy FPL — captain picks, differentials
8. Lookahead lines
9. Social buzz
10. CTA

## 5. Data modules

| Metric | Notes |
|---|---|
| xG / xGA / xGD | Always shown |
| Possession % | Both teams |
| PPDA | Press intensity |
| Field tilt | Attacking third % |
| Pressures | Defensive intensity |
| Set piece goals | Corners + FK |
| Aerial duels won % | When relevant |

## 6. Mock-data schema

```json
{
  "sport": "epl",
  "season": "2025-26",
  "matchweek": 12,
  "home": {
    "team":"Arsenal","abbr":"ARS",
    "nickname":"Gunners","stadium":"Emirates Stadium","city":"London",
    "record":"8-2-1","points":26,"position":2,
    "xg":21.4,"xga":9.8,"xgd":11.6,
    "ppda":9.1,
    "form":["W","W","D","W","W"],
    "formation":"4-3-3",
    "manager":"Mikel Arteta",
    "set_piece_goals":7,
    "injuries":[]
  },
  "away": { "...": "same shape" },
  "venue":{"name":"Emirates Stadium","capacity":60704},
  "kickoff_iso":"2025-11-22T17:30:00-05:00",
  "broadcast":{"network":"Sky Sports","stream":"Sky Go"},
  "vegas":{"home_win":1.85,"draw":3.6,"away_win":4.2,"ou_25":1.91,"btts_yes":1.75}
}
```

## 7. Vocabulary

- **"Matchweek"** not "game week". **"Ground"** not "stadium" (UK tradition).
- **"xG"** without spelling out.
- **"Set piece"**, **"dead ball"**, **"open play"**.
- **"Promotion"** / **"relegation"** / **"play-off"**.
- **"The Big Six"** (Arsenal, Chelsea, Liverpool, Man City, Man United, Spurs).
- **"Merseyside Derby"** (Liverpool vs Everton), **"North London Derby"** (Arsenal vs Spurs).
- **"Goal-line clearance"** is real. **"Last-ditch tackle"** is real.

## 8. Visual motifs

- **Pitch outline** — minimalist field in the page background, 5% opacity.
- **Position dots** — small circles used for player ratings.
- **Set piece corner flag** — small geometric flag for set piece sections.

## 9. Tone

- **Editorial register:** Tactical, narrative-heavy, stat-confident. The
  Athletic + Tifo Football. Every preview has a tactical thesis.
- **Lead with the matchup.** Arsenal vs Spurs isn't a game — it's a thesis.
- **Form is recent and reverent.** Don't dismiss recent losses.
- **Manager names carry weight.** Always include.

## 10. Print variant

- Table truncates to top 10 + bottom 3 (relegation zone)
- Tactical diagrams go grayscale
- Player ratings collapse to single line per player
