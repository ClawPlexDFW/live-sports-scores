# NBA — Design Spec

> National Basketball Association. 82-game regular season, four rounds of
> playoffs, the Finals. Per-game tempo, pace, lineup data, lineup-on/off
> splits, plus-minus, usage rate — the visual language needs **rhythm and
> pace**. Use a tempo-aware type scale. The page should *feel* like a
> fastbreak.

---

## 1. Identity

- **League:** NBA (30 teams, 2 conferences × 3 divisions)
- **Season:** October → June (82 games)
- **Postseason:** 16 teams, 4 rounds, NBA Finals
- **Game length:** ~2h15m (4 × 12min)
- **Editorial weight:** Medium — narrative-driven, star-focused.

## 2. Color palette

```js
colors: {
  bg:        '#0a0a0f',
  surface:   '#12131a',
  raised:    '#1a1c25',
  ink:       '#e9eaee',
  hairline:  'rgba(255,255,255,0.08)',
  home:      '#c2410c',  // burnt orange — court hardwood
  away:      '#1e3a8a',  // deep blue
  accent:    '#fbbf24',  // gold — championship
  live:      '#dc2626',
  done:      '#525252',
  dim:       '#6b7280',
}
```

Anchors are **hardwood orange + deep blue** — pulled directly from the iconic
NBA ball-and-court palette, desaturated to print-ink density. Accent is
**championship gold**.

## 3. Typography

- **Display:** `'Bebas Neue', 'Oswald', 'Impact', sans-serif` — tall,
  condensed, scoreboard energy. Alternative: `'Anton', 'Bebas Neue'`.
- **Body:** `'Inter', system-ui, sans-serif`
- **Mono:** `'JetBrains Mono', monospace` — for pace, TS%, eFG%, plus/minus
- **Accent:** Bebas Neue for quarter scores and arena names

## 4. Section order

### PREVIEW
1. Topline rule
2. Hero — matchup + tip-off + TNT/ESPN broadcast
3. Stat strip (4-up: tip-off, arena, capacity, broadcast)
4. Tale of the Tape — record, PPG, OP PPG, pace, ORtg, DRtg
5. Vegas (spread, total, ML)
6. Star Player Duel (top scorer vs top scorer, season averages)
7. Key Matchup (PG battle, paint battle, 3PT battle)
8. Injury Report
9. Pace & Style — pace comparison, eFG%, TOV%, ORB%
10. Last 10 form (game-by-game results)
11. Fan Pulse
12. CTA

### LIVE
1. Mega-scoreboard (home/away/score/quarter/clock)
2. Live team stats — FG%, 3P%, FT%, rebounds, assists, turnovers
3. Quarter-by-quarter scoring line chart
4. Hot player spotlight (live +/-, points in paint)
5. Run tracker (longest runs, momentum swings)
6. Play-by-play feed
7. CTA

### RECAP
1. Final score hero
2. AI Verdict
3. Box score (5-man starters + bench)
4. 3 turning points (with WP delta)
5. Player grades (5-man units)
6. Coach adjustments — what worked, what didn't
7. Fan Verdict
8. CTA

### HUB
1. Topline rule
2. Next game countdown
3. Conference standings (East / West, top 15)
4. Power rankings (top 10 with movement)
5. Trade & rumor mill
6. Fantasy waiver targets
7. Lookahead lines (next 5 games)
8. Rookie of the Year watch
9. MVP ladder
10. Social buzz
11. CTA

## 5. Data modules

| Metric | Where | Notes |
|---|---|---|
| Pace | Preview · Live · Recap | Possessions per 48 |
| ORtg / DRtg | All | Per 100 possessions |
| eFG% | Preview · Live | Effective FG% |
| TS% | Recap | True Shooting % |
| Usage % | Preview | Per player |
| Plus/minus | Live · Recap | Per player / unit |
| Net rating | Preview · Recap | ORtg - DRtg |
| PIE | Recap | Player Impact Estimate |
| Four Factors | All | eFG, TOV, ORB, FT/FGA |

## 6. Mock-data schema

```json
{
  "sport": "nba",
  "season": "2025-26",
  "home": {
    "team": "Boston Celtics", "abbr": "BOS",
    "city": "Boston", "nickname": "Celtics",
    "conference": "Eastern", "division": "Atlantic",
    "record": "12-4", "home_record": "7-1",
    "streak": "W3",
    "ppg": 118.4, "oppg": 109.7,
    "pace": 100.2, "ortg": 118.0, "drtg": 109.4, "net": 8.6,
    "efg_pct": 0.564, "tov_pct": 0.121, "orb_pct": 0.281, "ft_pct_fga": 0.214,
    "three_pt_pct": 0.382,
    "top_scorer": {"name":"Jayson Tatum","ppg":27.1,"rpg":8.0,"apg":4.6,"ts_pct":0.621},
    "last_10": ["W","W","L","W","W","W","L","W","W","L"],
    "injuries": [
      {"name":"Kristaps Porzingis","status":"OUT","impact":8,"reason":"Knee"}
    ]
  },
  "away": { "...": "same shape" },
  "venue": {"name":"TD Garden","city":"Boston","capacity":19156},
  "tipoff_iso": "2025-11-21T19:30:00-05:00",
  "broadcast": {"network":"TNT","stream":"Max","announcers":"Kevin Harlan, Reggie Miller"},
  "vegas": {"spread":-6.5,"spread_team":"BOS","total":225.5,"moneyline_home":-260,"moneyline_away":+215,"implied_home":116,"implied_away":109},
  "star_duel": {"home":{"name":"Tatum","ppg":27.1},"away":{"name":"Doncic","ppg":28.9},"edge":"away"},
  "key_matchups": [
    {"label":"Paint scoring","home_rank":4,"away_rank":11,"edge":"home"},
    {"label":"3PT shooting","home_rank":2,"away_rank":7,"edge":"home"},
    {"label":"Turnovers forced","home_rank":9,"away_rank":3,"edge":"away"}
  ],
  "poll": {"predicted_bos":118,"predicted_lal":109,"spread_pick_bos":62,"confidence":68}
}
```

## 7. Vocabulary

- Use **"field goal"** not "shot". Use **"three-pointer"** or **"3PT"**, not
  "long shot".
- **"Points in the paint"** is a real stat. **"Fast-break points"** is real.
  **"Second-chance points"** is real. Use them.
- **"Assist-to-turnover ratio"** is the canonical PG stat.
- Don't say **"rebs"**. Say **rebounds** or **boards**.
- Use **quarters** (Q1, Q2, Q3, Q4), not halves.
- **"Double-double"** and **"triple-double"** — use them when earned.

## 8. Visual motifs

- **Court line** — full-width 2px stripe used as section divider, with two
  thin parallel lines (1px each) flanking it to suggest the paint/key.
- **Free-throw circle** — small SVG used as a CTA button background on
  scoring moments.
- **Three-point arc** — for accent lines on shot charts.

## 9. Tone

- **Editorial register:** Puckish, narrative, star-driven. Think Jackie MacMullan
  + Bill Simmons. Personality matters.
- **Lead with the star duel.** This isn't X's-and-O's — it's theater.
- **Use arena nicknames** ("The Garden", "The Forum", "Crypto.com Arena").
- **Playoff implications** always get a paragraph in preview.
- **Don't bury the coach storyline.** A new coach is a story; a coach on the
  hot seat is a story.

## 10. Print variant

- Stat strip collapses to 2-up
- Quarter chart goes grayscale
- Standings tables truncate to top 8 in each conference
- Player grades fit on one letter sheet

## Verification

- [ ] Hero doesn't overlap (court line stays below H1)
- [ ] Pace + ORtg/DRtg always visible
- [ ] Star duel in preview always has both player names + averages
- [ ] Quarter-by-quarter chart fits inside letter sheet width when printed
- [ ] No emoji as section markers
