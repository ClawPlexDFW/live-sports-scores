# NFL — Design Spec

> National Football League. Sundays, Mondays, Thursdays, plus three days of
> playoffs. Per-game complexity is the highest of any sport we cover — drive
> charts, QBR splits, EPA per play, red-zone efficiency, third-down rates, two
> minute drill, clock management. The visual language has to be **sharp, dense,
> high-contrast**, and absolutely unambiguous about who's winning.

---

## 1. Identity

- **League:** National Football League (32 teams, 2 conferences × 4 divisions)
- **Season:** September → February (regular season 17 weeks, 18 games)
- **Postseason:** 14 teams, 4 rounds, Super Bowl
- **Game length:** ~3h15m
- **Editorial weight:** Highest of any sport — every yard matters, every flag
  is a story, every fourth down is a referendum.

## 2. Color palette

```js
colors: {
  bg:        '#0c0e12',  // near-black with steel undertone
  surface:   '#15181f',
  raised:    '#1c2029',
  ink:       '#e8e9ec',
  hairline:  'rgba(255,255,255,0.08)',
  home:      '#7f1d1d',  // oxblood / burgundy
  away:      '#1e3a8a',  // midnight navy
  accent:    '#facc15',  // caution-tape yellow
  live:      '#dc2626',  // live red (only when status=LIVE)
  done:      '#525252',  // grey for FINAL
  dim:       '#6b7280',
}
```

The two anchor colors are **oxblood and midnight navy** — drawn from the NFL
shield's red+blue, darkened to print-page ink densities. Accent is **caution
yellow** — the only thing that should pop on the page other than a live
scoreboard. No orange. No pastel.

## 3. Typography

- **Display:** `'Playfair Display', 'Source Serif 4', Georgia, serif` —
  magazine-weight, dense, opinionated.
- **Body:** `'Inter', system-ui, sans-serif` — clean, screen-first.
- **Mono:** `'JetBrains Mono', monospace` — for play-by-play timecodes,
  yard lines, EPA values, snap counts.
- **Accent:** Playfair Italic for the *vs* connector and rivalry phrasing.

## 4. Section order (per report mode)

### PREVIEW
1. Topline rule (sport · week · kickoff TZ)
2. Hero header — matchup + week + prime-time tag
3. Stat strip (4-up: kickoff, venue, capacity, broadcast)
4. **The Tale of the Tape** — record, PF, PA, turnover margin, third-down %
5. **Vegas** — spread, total, moneyline, implied score
6. **Offensive & Defensive Rankings** — PPG, yards/play, EPA, success rate
7. **Injury Report** — Out / Questionable / Probable with impact score 1-10
8. **X-Factor Matchups** — QB vs pass rush, WR vs CB, OT vs Edge
9. **Coaching Intel** — HC vs HC all-time, last-5 against the spread
10. **Fan Pulse** — predicted score, spread pick %, confidence %
11. CTA footer

### LIVE
1. Mega-scoreboard (home/away/large scores/clock/quarter/down-distance)
2. Win Probability bar with sparkline
3. Drive chart (last 5 drives per team)
4. Live team stats — TOP, total yards, pass yards, rush yards, 3rd down
5. Hot player spotlight (live EPA leader)
6. Play-by-play feed (last 10 with time, down, yard line, play, players)
7. CTA footer

### RECAP
1. Final score hero
2. AI Verdict (3-sentence summary)
3. Box score (offense + defense + special teams tabs)
4. Game-changing moments — 3 turning points with WP delta
5. Player grades (offense / defense / special teams)
6. Fan Verdict sliders
7. What's next
8. CTA footer

### HUB
1. Topline rule
2. Next game countdown
3. Standings — division (NFC/AFC East/West/North/South) with W/L/PF/PA
4. Power rankings — top 5 with movement arrows
5. Trade & rumor mill (VERIFIED / DEVELOPING / SPECULATION)
6. Fantasy waiver targets (RB / WR / TE / DEF)
7. Lookahead betting lines (next 4 weeks)
8. Coach hot seat (current pressure gauge)
9. Social buzz (X, Reddit, IG)
10. CTA footer

## 5. Data modules

| Metric | Where used | Source |
|---|---|---|
| EPA/play | Preview · Recap | nflfastR (mocked) |
| Success rate | Preview · Live · Recap | nflfastR (mocked) |
| DVOA | Preview | Football Outsiders (mocked) |
| QBR | Preview · Live | ESPN (mocked) |
| PFF grade | Recap | PFF (mocked) |
| Win Probability | Live · Recap | nflfastR (mocked) |
| Air Yards | Preview · Recap | nflfastR (mocked) |
| YAC | Recap | nflfastR (mocked) |
| Pressure % | Preview | PFF (mocked) |
| CPOE | Recap | RBSDM (mocked) |

## 6. Mock-data schema

```json
{
  "sport": "nfl",
  "season": 2025,
  "week": 7,
  "season_type": "regular",
  "home": {
    "team": "Dallas Cowboys",
    "abbr": "DAL",
    "city": "Dallas",
    "nickname": "Cowboys",
    "conference": "NFC",
    "division": "East",
    "record": "4-2",
    "pf": 162, "pa": 134,
    "rank_ppg_off": 8, "rank_ppg_def": 14,
    "rank_yards_off": 11, "rank_yards_def": 19,
    "epa_off": 0.07, "epa_def": 0.03,
    "success_rate_off": 0.46, "success_rate_def": 0.42,
    "third_down_pct": 0.41, "red_zone_pct": 0.62,
    "turnover_margin": 0,
    "starting_qb": "Dak Prescott",
    "qb_record": "4-2",
    "head_coach": "Mike McCarthy",
    "home_record": "2-1",
    "last_5": ["W","L","W","W","L"],
    "injuries": [
      {"name":"DeMarcus Lawrence","pos":"DE","status":"OUT","impact":9,"reason":"Foot"},
      {"name":"Brandon Cooks","pos":"WR","status":"Q","impact":4,"reason":"Knee"}
    ]
  },
  "away": { "...": "same shape" },
  "venue": {"name":"AT&T Stadium","city":"Arlington","state":"TX","capacity":80000,"surface":"Turf","roof":"Retractable"},
  "kickoff_iso": "2025-10-19T19:20:00-05:00",
  "broadcast": {"network":"NBC","stream":"Peacock","announcers":"Al Michaels, Kirk Herbstreit"},
  "vegas": {
    "spread": -3.5, "spread_team": "DAL",
    "total": 47.5,
    "moneyline_home": -180, "moneyline_away": +155,
    "implied_home": 25.5, "implied_away": 22.0
  },
  "x_factor_matchups": [
    {"home":"Micah Parsons","pos":"LB","away":"Lane Johnson","pos":"OT","edge":"home","why":"Parsons 18 pressures last 3 games"}
  ],
  "storylines": [
    "Cowboys coming off bye — McCarthy 7-2 off bye as HC",
    "Eagles look to extend 3-game divisional win streak"
  ],
  "poll": {"predicted_dal":24, "predicted_phi":20, "spread_pick_dal":58, "confidence":71}
}
```

## 7. Vocabulary

- Use **yards**, not meters. Use **down & distance**, not possession.
- Say **"red zone"**, not "scoring area". Say **"two-minute drill"**, not
  "end-of-game situation".
- Quarterback → QB. Running back → RB. Wide receiver → WR.
- **Defense wins championships.** Don't shy from defensive metrics.
- "Stuff", "tackle for loss (TFL)", "sack", "INT", "fumble recovery", "red
  zone trip" — use precisely.
- **Don't use** "downs" in plural when meaning a single down (e.g., "third
  and long").

## 8. Visual motifs

- **Field marker** — yard-line stripe (5px tall) used as a section divider.
  Numbers 10, 20, 30, 40, 50 fade in alternating.
- **Down arrow** — for third-down and red-zone indicators.
- **Diamond** — for turnover indicators (W on green / L on red).
- **No football emoji** — geometric only.

## 9. Tone

- **Editorial register:** Sharp, declarative, stat-head. Think Peter King +
  Warren Sharp. Every paragraph ends with a fact or a take.
- **Lead with the spread.** Vegas sets the conversation.
- **Don't bury the QB matchup** — it's the headline.
- **Use coach names** liberally. Coaching intel is half the story.
- **Pull no punches** on injuries. If the LT is out, say it.

## 10. Print variant

On letter sheet (816×1056):
- Stats strip collapses from 4-up to 2-up
- Standings tables drop to 8 columns max
- Play-by-play collapses to single column (last 6 plays only)
- All animations off; live indicator becomes a static colored dot
- Fan pulse chart goes to grayscale
- CTA footer becomes a small meta caption

## Verification

Before declaring done:

- [ ] Hero header doesn't overlap (no `.92rem` track widths!)
- [ ] All yard-line numbers readable
- [ ] Spread / total always visible on hero
- [ ] Win probability always shown when game LIVE
- [ ] Injury report impact scores 1-10
- [ ] No emoji in section markers
- [ ] Print stylesheet removes all animations and poll widgets
