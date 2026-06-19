# MLS — Design Spec

> Major League Soccer. 34-game regular season (since 2023), MLS Cup, plus
> Leagues Cup, US Open Cup, CONCACAF Champions Cup. The visual language
> **echoes the rest of soccer** but with North American specifics — salary
> budget, designated players, single-entity structure. Editorial register is
> growing: more analytical than European press, less stat-head than baseball.

---

## 1. Identity

- **League:** MLS (30 teams, 2 conferences × 15)
- **Season:** February → December (34 games regular season)
- **Playoffs:** 18 teams → MLS Cup (8 advancing to R16)
- **Editorial weight:** Medium — narrative + emerging analytics.

## 2. Color palette

```js
colors: {
  bg:        '#0a0d0c',
  surface:   '#131715',
  raised:    '#1b1f1d',
  ink:       '#e9ebe9',
  hairline:  'rgba(255,255,255,0.08)',
  home:      '#0e7c3a',  // pitch green
  away:      '#1e3a8a',  // navy
  accent:    '#facc15',  // goal-net yellow
  live:      '#dc2626',
  done:      '#525252',
  dim:       '#6b7280',
}
```

Anchors are **pitch green + navy**, accent is **goal-net yellow**.

## 3. Typography

- **Display:** `'Source Serif 4', 'Playfair Display', Georgia, serif`
- **Body:** `'Inter', system-ui, sans-serif`
- **Mono:** `'JetBrains Mono', monospace` — for xG, possession %, shots

## 4. Section order

### PREVIEW
1. Topline
2. Hero
3. Stat strip
4. Tale of the Tape — record, PPG, xG, xGA
5. Vegas
6. Form guide (last 5 with W/L/D dots)
7. Head-to-head (last 5 meetings)
8. Injury report (callups matter — international duty)
9. Designated Player watch
10. Fan Pulse
11. CTA

### LIVE
1. Mega-scoreboard (clock/score)
2. Live xG chart
3. Live stats (shots, shots on target, possession, corners, fouls)
4. Live possession map
5. Play-by-play
6. CTA

### RECAP
1. Final score hero
2. AI Verdict
3. Box score (pass % + tackles)
4. 3 turning moments (with xG delta)
5. Player grades
6. Fan Verdict
7. CTA

### HUB
1. Topline
2. Next game countdown
3. Conference standings (East / West)
4. Supporters' Shield race
5. Trade & rumor mill (transfer window)
6. Fantasy waiver targets
7. Lookahead lines
8. Audi MLS Cup Playoffs bracket
9. Social buzz
10. CTA

## 5. Data modules

| Metric | Notes |
|---|---|
| xG / xGA | Always shown |
| Possession % | Yes |
| Pass completion % | Both teams |
| Pressures | Defensive intensity |
| PPDA | Passes per defensive action |
| Field tilt | Attacking third time % |

## 6. Mock-data schema

```json
{
  "sport": "mls",
  "season": 2025,
  "matchday": 28,
  "home": {
    "team": "LAFC", "abbr": "LAFC",
    "stadium":"BMO Stadium","city":"Los Angeles",
    "record":"14-8-6","points":50,"conference":"Western",
    "form":["W","L","W","W","D"],
    "xg":1.84,"xga":1.12,
    "ppda":9.4,
    "designated_players":[
      {"name":"Olivier Giroud","pos":"FW","goals":14},
      {"name":"Son Heung-min","pos":"FW","goals":16}
    ]
  }
}
```

## 7. Vocabulary

- **"Matchday"**, not "game week". **"Designated Player (DP)"**.
- **"Audi MLS Cup Playoffs"** (sponsor name matters).
- **"Supporters' Shield"** = best regular-season record.
- **"Decision Day"** = final regular-season matchday.
- **"El Tráfico"** = LAFC vs LA Galaxy.

## 8. Visual motifs

- **Pitch outline** — minimalist field sketch in accent color, used as a
  section background (5% opacity).

## 9. Tone

- Editorial register: Emerging, narrative-driven, growing stat sophistication.

## 10. Print variant

- Standings tables truncate to top 8
- xG chart goes grayscale
- DP watch collapses to one row
