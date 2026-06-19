# Rugby — Design Spec

> Rugby Union (15s), Rugby League (13s), Sevens. **Editorial register: brutal,
> physical, set-piece-aware.** Rugby has its own stat universe — scrums,
> lineouts, rucks, mauls, tackles, turnovers.

---

## 1. Identity

- **Codes:** Rugby Union (15-a-side), Rugby League (13-a-side), Sevens (7-a-side)
- **Major events:** Six Nations, Rugby Championship (SANZAR), World Cup,
  Premiership (England), Top 14 (France), URC (Ireland/Scotland/Wales/Italy/SA),
  Super Rugby (Southern Hemisphere)
- **Editorial weight:** Set-piece + breakdown + physical.

## 2. Color palette

```js
colors: {
  bg:        '#0a0a0d',
  surface:   '#111319',
  raised:    '#181c25',
  ink:       '#e9eaf0',
  hairline:  'rgba(255,255,255,0.08)',
  red:       '#c8102e',  // British & Irish Lion red
  green:     '#0e7c3a',  // pitch green
  gold:      '#ffb612',  // trophy gold
  black:     '#000000',  // All Blacks
  live:      '#dc2626',
  done:      '#525252',
  dim:       '#6b7280',
}
```

**No fixed anchors.** Use the two teams' national colors (red rose for
England, blue for France, green for Ireland, black for New Zealand, etc.).

## 3. Typography

- **Display:** `'Source Serif 4', 'Playfair Display', Georgia, serif`
- **Body:** `'Inter', system-ui, sans-serif`
- **Mono:** `'JetBrains Mono', monospace` — for tries, conversions, penalty

## 4. Section order

### PREVIEW
1. Topline — Tournament · Matchday
2. Hero — Nation A vs Nation B · Kickoff
3. Tale of the Tape — W/L, PF, PA, BP, table position
4. Vegas
5. **Team news** — XV selected, captain, position changes
6. **Head-to-head** (last 5)
7. **Recent form**
8. **Key battles** (props, halfbacks, centers)
9. **Set-piece edge**
10. Weather
11. Fan Pulse
12. CTA

### LIVE
1. Mega-scoreboard (score / clock / sin bin)
2. Live stats (tries, conversions, penalty kicks, drop goals)
3. **Territory / possession** map
4. **Set-piece success rate** (scrums, lineouts)
5. **Tackle completion %**
6. Play-by-play (last 10)
7. CTA

### RECAP
1. Final score hero
2. AI Verdict
3. **Try timeline** (visual)
4. **Man of the Match** stats
5. 3 turning moments
6. Player ratings (1-10)
7. Table movement
8. Fan Verdict
9. CTA

### HUB
1. Topline
2. **Tournament table** (with bonus points)
3. Upcoming fixtures (next matchday)
4. World rankings (top 15)
5. Player watch (form guide)
6. Transfer / injury news
7. Lookahead
8. CTA

## 5. Data modules

| Metric | Notes |
|---|---|
| Tries | 5 points each |
| Conversions | 2 points each |
| Penalty kicks | 3 points each |
| Drop goals | 3 points each |
| Scrum success % | Per team |
| Lineout success % | Per team |
| Tackle completion % | Per team |
| Possession % | Per team |
| Territory % | Per team |
| Bonus points | Standings |

## 6. Mock-data schema

```json
{
  "sport": "rugby",
  "code": "union",
  "tournament": "Six Nations 2026",
  "matchday": 3,
  "home": {
    "team":"Ireland","abbr":"IRE","flag_color_primary":"#0e7c3a",
    "record":"2-0-0","points":10,"table_position":1,
    "pf":62,"pa":21,
    "scrum_success_pct":0.94,"lineout_success_pct":0.88,
    "tackle_completion_pct":0.91,
    "captain":"Peter O'Mahony","coach":"Andy Farrell"
  },
  "away": { "...": "same shape" },
  "venue":{"name":"Aviva Stadium","city":"Dublin","capacity":51800},
  "kickoff_iso":"2026-02-22T17:00:00+00:00",
  "broadcast":{"network":"BBC","stream":"iPlayer"},
  "vegas":{"ireland_win":1.45,"draw":25.0,"france_win":2.75,"handicap":-7.5}
}
```

## 7. Vocabulary

- **"Try"** = 5 points (touchdown equivalent).
- **"Conversion"** = 2 points (kick after try).
- **"Penalty kick"** = 3 points.
- **"Drop goal"** = 3 points.
- **"Scrum"** / **"Lineout"** / **"Ruck"** / **"Maul"** / **"Breakdown"**.
- **"Sin bin"** = 10-minute suspension.
- **"Yellow card"** / **"Red card"**.
- **"Bonus point"** = scoring 4+ tries OR losing by 7 or fewer.
- **"Fly-half"** = #10. **"Scrum-half"** = #9.
- **"Tighthead prop"** / **"Loosehead prop"** = the two props.
- **"Number 8"** = back of the scrum.

## 8. Visual motifs

- **Try line** — horizontal stripe at section breaks.
- **Pillars** — two vertical lines as section dividers (suggesting goal posts).
- **Ball** — small oval shape (prolate spheroid — rugby's distinctive ball).

## 9. Tone

- **Editorial register:** Brutal, physical, set-piece-aware. RugbyPass +
  The Rugby Paper. Less hyperbole than football, more respect for physicality.
- **Lead with the set-piece.** Scrums and lineouts decide matches.
- **Captain + coach names matter.** Andy Farrell, Ronan O'Gara — characters.
- **Bonus points are non-negotiable** in standings.

## 10. Print variant

- Scorecard fits on letter sheet
- Try timeline collapses to one row per try
- Set-piece stats fit in 2-column grid
