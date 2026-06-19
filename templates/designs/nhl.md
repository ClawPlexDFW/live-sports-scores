# NHL — Design Spec

> National Hockey League. 82-game regular season, four playoff rounds, the
> Stanley Cup. Per-game data is **event-driven** — goals are rare, every shot
> matters, goaltending is half the story. The visual language needs **cold
> precision**. Use ice-blue + arena-red as anchors, and remember: this is the
> only sport where 1-0 is a *thrilling* final score.

---

## 1. Identity

- **League:** NHL (32 teams, 2 conferences × 4 divisions)
- **Season:** October → June (82 games)
- **Postseason:** 16 teams, 4 rounds, Stanley Cup Final
- **Game length:** ~2h30m (3 × 20min)
- **Editorial weight:** Medium — goalies + special teams + rivalries drive the story.

## 2. Color palette

```js
colors: {
  bg:        '#06090f',
  surface:   '#0e131c',
  raised:    '#161c28',
  ink:       '#e6ecf2',
  hairline:  'rgba(255,255,255,0.08)',
  home:      '#1e40af',  // ice blue
  away:      '#b91c1c',  // arena red
  accent:    '#fbbf24',  // Stanley gold
  live:      '#dc2626',
  done:      '#525252',
  dim:       '#6b7280',
}
```

Anchors are **ice-blue + arena-red** — the two colors that dominate every NHL
arena scoreboard. Background goes near-black with a slight blue cast — like
looking through arena glass at ice.

## 3. Typography

- **Display:** `'Oswald', 'Bebas Neue', 'Impact', sans-serif` — tall,
  condensed, scoreboard energy
- **Body:** `'Inter', system-ui, sans-serif`
- **Mono:** `'JetBrains Mono', monospace` — for shot attempts, save %, xG
- **Accent:** Oswald Medium for period labels (1ST, 2ND, 3RD, OT)

## 4. Section order

### PREVIEW
1. Topline rule
2. Hero — matchup + puck drop + broadcast
3. Stat strip (puck drop, arena, capacity, broadcast)
4. Tale of the Tape — record, GF/G, GA/G, PP%, PK%, FO%
5. Vegas
6. Goaltending Duel — GAA, SV%, quality starts, recent form
7. Special Teams — PP vs PK breakdown
8. Injury Report
9. Head-to-head + last 5 meetings
10. Fan Pulse
11. CTA

### LIVE
1. Mega-scoreboard (period/clock/score/shots)
2. Shot chart (live)
3. Corsi / Fenwick live
4. Power-play tracker
5. Goalie heat map
6. Play-by-play (last 10 events)
7. CTA

### RECAP
1. Final score hero
2. AI Verdict
3. Box score (skaters + goalies + special teams)
4. 3 turning points
5. Three stars
6. Goalie grades
7. Fan Verdict
8. CTA

### HUB
1. Topline rule
2. Next game countdown
3. Division standings (4 divisions)
4. Power rankings
5. Trade & rumor mill
6. Fantasy pickups (goalies + skaters)
7. Lookahead lines
8. Stanley Cup odds
9. Social buzz
10. CTA

## 5. Data modules

| Metric | Where | Notes |
|---|---|---|
| SV% | All | Save percentage |
| GAA | All | Goals against average |
| xG | Preview · Live · Recap | Expected goals |
| Corsi / Fenwick | Live · Recap | Shot attempt differential |
| PP% / PK% | All | Power play / penalty kill |
| FO% | All | Faceoff win percentage |
| PDO | Recap | Luck metric (sum of SV% + SH%) |
| QoC | Preview | Quality of competition |

## 6. Mock-data schema

```json
{
  "sport": "nhl",
  "season": "2025-26",
  "home": {
    "team": "Boston Bruins", "abbr": "BOS",
    "city": "Boston", "nickname": "Bruins",
    "conference": "Eastern", "division": "Atlantic",
    "record": "14-5-2", "points": 30,
    "gf_per_g": 3.4, "ga_per_g": 2.3,
    "pp_pct": 0.248, "pk_pct": 0.842,
    "fo_pct": 0.524,
    "top_scorer": {"name":"David Pastrnak","goals":18,"assists":22,"points":40},
    "goalie": {"name":"Linus Ullmark","gaa":2.18,"sv_pct":0.924,"record":"11-4-1"},
    "last_5": ["W","W","L","W","W"],
    "injuries": []
  },
  "away": { "...": "same shape" },
  "venue": {"name":"TD Garden","city":"Boston","capacity":17850},
  "puck_drop_iso": "2025-11-21T19:00:00-05:00",
  "broadcast": {"network":"TNT","stream":"Max"},
  "vegas": {"puck_line":-1.5,"total":6.0,"moneyline_home":-145,"moneyline_away":+125},
  "goalie_duel": {
    "home":{"name":"Ullmark","sv_pct":0.924,"gaa":2.18,"quality_starts":11},
    "away":{"name":"Shesterkin","sv_pct":0.918,"gaa":2.41,"quality_starts":9}
  },
  "special_teams_edge": {"pp":"home","pk":"away"}
}
```

## 7. Vocabulary

- Use **"goals"** not "scores". Use **"assists"**, not "passes that led to goals".
- **"Power play"** and **"penalty kill"** are the bread-and-butter stats.
- **"Five-on-five"** is the default state.
- **"Even strength"** / **"special teams"** / **"empty net"** — use them.
- **"Plus/minus"** — single stat, often misleading, use sparingly.
- **Don't say "shots on goal"** when you mean "shot attempts" — be specific.

## 8. Visual motifs

- **Goal light** — bright red dot animation when a goal is scored (recap only).
- **Ice surface lines** — 4 horizontal hairlines (blue line + red line) used
  as section dividers in preview/recap.
- **Puck** — small black circle used as a CTA bullet.

## 9. Tone

- **Editorial register:** Cold, precise, stat-driven. Think Elliotte Friedman
  + Dom Luszczyszyn. Goals are events, not just scores.
- **Lead with the goalie.** Half the game is the netminder.
- **Special teams decide playoff series.** Always have a special teams
  breakdown in preview/recap.
- **Rivalries are holy** — Original Six games get extra weight.

## 10. Print variant

- Period chart collapses to a single bar
- Shot chart simplifies to per-period counts
- Three stars fits in a 3-column row

## Verification

- [ ] Hero doesn't overlap (ice lines below H1)
- [ ] Goalie duel always shows GAA + SV%
- [ ] PP% / PK% always visible on preview hero strip
- [ ] Corsi / Fenwick labeled correctly (not "shot differential")
- [ ] No emoji as section markers
