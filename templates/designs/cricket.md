# Cricket — Design Spec

> ICC (international — Tests, ODIs, T20Is), IPL (Indian Premier League), BBL
> (Big Bash), PSL (Pakistan Super League), The Hundred, county cricket.
> **Editorial register: stat-rich, format-aware, multi-day.**

---

## 1. Identity

- **Formats:** Test (5 days), ODI (50 overs), T20 (20 overs), T10, The Hundred (100 balls)
- **Major events:** ICC Cricket World Cup, T20 World Cup, Champions Trophy, IPL,
  Ashes (England vs Australia), Border-Gavaskar (India vs Australia)
- **Editorial weight:** Format-specific. Tests need patience, T20 needs energy.

## 2. Color palette

```js
colors: {
  bg:        '#0a0a0d',
  surface:   '#111319',
  raised:    '#181c25',
  ink:       '#e9eaf0',
  hairline:  'rgba(255,255,255,0.08)',
  red:       '#c8102e',  // ball red (Test cricket)
  blue:      '#0033a0',  // ODI blue
  gold:      '#ffb612',  // IPL gold
  green:     '#15803d',  // pitch green
  live:      '#dc2626',
  done:      '#525252',
  dim:       '#6b7280',
}
```

**No fixed anchors.** The accent comes from the format / series context.
Test cricket = red ball, ODIs = blue, IPL = gold.

## 3. Typography

- **Display:** `'Source Serif 4', 'Playfair Display', Georgia, serif`
- **Body:** `'Inter', system-ui, sans-serif`
- **Mono:** `'JetBrains Mono', monospace` — for runs, overs, wickets

## 4. Section order

### PREVIEW
1. Topline — Series · Format · Day/Match
2. Hero — Team A vs Team B · Toss · Format
3. Tale of the Tape
4. **Pitch report** + Weather
5. **Playing XI** with captain indicator
6. Vegas
7. Head-to-head (recent + all-time)
8. **Key matchups** (top-order batsmen vs strike bowler)
9. Recent form (last 5 in this format)
10. Fan Pulse
11. CTA

### LIVE
1. Mega-scoreboard (runs / wickets / overs / target)
2. **Live run rate** chart
3. **Wagon wheel** (where the runs are being scored)
4. **Manhattan** (runs per over)
5. **Live partnerships** (current + best)
6. **Fall of wickets**
7. Play-by-ball (last 12 balls)
8. CTA

### RECAP
1. Final result hero
2. AI Verdict
3. **Innings breakdown** (both teams, all innings if Test)
4. Top scorer + best bowler
5. 3 turning moments
6. **Player of the Match** stats
7. **Series impact**
8. Fan Verdict
9. CTA

### HUB
1. Topline
2. **Live matches** ticker
3. **ICC rankings** (Test / ODI / T20I — top 10 each)
4. **Series in progress**
5. **Upcoming fixtures** (next 2 weeks)
6. **IPL standings** (when active)
7. **Player watch** (form guide)
8. Lookahead
9. CTA

## 5. Data modules

| Metric | Notes |
|---|---|
| Runs | Always |
| Wickets | Always |
| Overs | In ODI/T20; days in Test |
| Run rate | Current |
| Required rate | When chasing |
| Strike rate | Per batsman |
| Economy | Per bowler |
| Average | Per player |
| Partnership runs | Current |

## 6. Mock-data schema

```json
{
  "sport": "cricket",
  "format": "odi",
  "match_type": "World Cup 2026",
  "venue":{"name":"Narendra Modi Stadium","city":"Ahmedabad","capacity":132000,"pitch":"Batting","avg_score":312},
  "toss":{"winner":"India","decision":"bat"},
  "playing_xi": {
    "home":["Rohit Sharma (c)","Shubman Gill","Virat Kohli","Shreyas Iyer","KL Rahul (wk)","Hardik Pandya","Ravindra Jadeja","Kuldeep Yadav","Jasprit Bumrah","Mohammed Siraj","Mohammed Shami"],
    "away":["Pat Cummins (c)","David Warner","Travis Head","Steve Smith","Marnus Labuschagne","Glenn Maxwell","Alex Carey (wk)","Mitchell Starc","Josh Hazlewood","Adam Zampa","Pat Cummins"]
  },
  "vegas":{"india_win":1.65,"australia_win":2.25},
  "pitch_report":"Flat batting surface, expect 320+"
}
```

## 7. Vocabulary

- **"Runs"** / **"Wickets"** / **"Overs"** / **"Maiden over"**.
- **"Innings"** (singular even for plural — "first innings" / "second innings").
- **"Duck"** = out for 0. **"Golden duck"** = out first ball.
- **"Century"** = 100 runs. **"Half-century"** = 50. **"Double century"** = 200.
- **"Five-wicket haul"** = 5 wickets by one bowler.
- **"Powerplay"** = first overs (mandatory fielding restrictions).
- **"Death overs"** = final overs (typically 16-20 in T20, 41-50 in ODI).
- **"Toss"** / **"Bat / Bowl first"**.
- **"Test"** / **"ODI"** / **"T20"** / **"T10"** / **"The Hundred"**.
- **"IPL"**, **"BBL"**, **"PSL"**, **"CPL"**, **"The Ashes"**.

## 8. Visual motifs

- **Stumps** — 3 vertical lines as section marker.
- **Ball** — small red circle for current over.
- **Wagon wheel** — radial diagram of scoring areas.

## 9. Tone

- **Editorial register:** Patient, stat-rich, format-aware. ESPN Cricinfo +
  The Cricket Monthly. Cricket writing is technically dense.
- **Lead with the format.** Test = patience, T20 = aggression.
- **Pitch report is sacred.** Always include pitch type + expected behavior.
- **Toss matters.** Always surface toss winner + decision.

## 10. Print variant

- Scorecard fits on letter sheet (the whole point)
- Wagon wheel simplifies to summary stats
- Play-by-ball fits last 12 balls in one row
