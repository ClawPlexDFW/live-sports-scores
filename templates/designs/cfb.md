# CFB — Design Spec

> NCAA College Football. 12-game regular season, conference championships, the
> College Football Playoff (12-team as of 2024-25). Per-game intensity is high,
> rivalries are religion. **132 teams across FBS** = visual chaos — the design
> has to handle wild team-color palettes gracefully. Editorial register is
> **part analytics, part pageantry**.

---

## 1. Identity

- **League:** NCAA Division I FBS (132 teams, 10 conferences)
- **Season:** August → January (12-14 games)
- **Postseason:** Conference championships → 12-team CFP → National Championship
- **Editorial weight:** Very high — pageantry + rivalries + rankings drama.

## 2. Color palette

**Dynamic per matchup.** Use the two schools' primary colors as anchors, with
neutral surface tones from the master prompt. When teams clash (red vs blue
works), accept it. When both teams are red, desaturate one side.

```js
// Per-game dynamic palette
homePrimary: fromTeamData,
awayPrimary: fromTeamData,
surface: '#0c0e12',  // always
raised: '#15181f',
accent: '#facc15',  // always championship gold
```

## 3. Typography

- **Display:** `'Source Serif 4', 'Playfair Display', Georgia, serif`
- **Body:** `'Inter', system-ui, sans-serif`
- **Mono:** `'JetBrains Mono', monospace`

## 4. Section order

### PREVIEW
1. Topline
2. Hero — matchup + ranking (if ranked) + kickoff
3. Stat strip
4. Tale of the Tape — record, PPG, OP PPG, SOS, FPI/SP+
5. Vegas
6. Recruiting comparison (avg stars, top recruits)
7. Coaching matchup (HC vs HC all-time)
8. Injury report
9. Rivalry context (all-time series, last meeting, streak)
10. **Poll impact preview** (CFP implications)
11. Fan Pulse
12. CTA

### LIVE
1. Mega-scoreboard (quarter/clock/score)
2. Live SP+ win probability
3. Drive chart
4. Live team stats
5. Play-by-play
6. CFP bracket implications
7. CTA

### RECAP
1. Final score hero
2. AI Verdict
3. Box score
4. 3 turning moments
5. Player grades
6. CFP bracket movement
7. Fan Verdict
8. CTA

### HUB
1. Topline
2. Next game countdown
3. AP Top 25 + CFP Top 25
4. Conference standings (10)
5. Heisman watch
6. Bowl projections
7. Transfer portal watch
8. Coach hot seat
9. Social buzz
10. CTA

## 5. Data modules

| Metric | Notes |
|---|---|
| SP+ | Always shown (Bill Connelly) |
| FPI | ESPN's predictive index |
| SOS | Strength of schedule |
| Recruiting rank | 247 / On3 / Rivals composite |
| CFP ranking | Weekly |
| Drive efficiency | Yards per play |

## 6. Mock-data schema

```json
{
  "sport": "cfb",
  "season": 2025,
  "week": 7,
  "home": {
    "team":"Texas Longhorns","abbr":"TEX",
    "conference":"SEC","division":"",
    "rank_ap":7,"rank_cfp":6,
    "record":"5-1","conf_record":"3-1",
    "ppg":42.4,"oppg":18.7,
    "sp_plus":31.4,"fpi":24.1,
    "sos_rank":18,
    "recruiting_rank_avg":5,
    "top_recruits":[{"name":"Arch Manning","pos":"QB","stars":5,"rank":7}],
    "head_coach":"Steve Sarkisian",
    "hc_record":"38-15"
  }
}
```

## 7. Vocabulary

- **"Ranked matchup"** — always note when both teams are ranked.
- **"Conference championship game"** — different from regular season.
- **"Rivalry week"** — week 13/14, full of rivalry games.
- **"The Game"** (Michigan vs Ohio State), **"The Iron Bowl"** (Alabama vs
  Auburn), **"The Red River Showdown"** (Texas vs Oklahoma).
- **"Walk-on"**, **"scholarship"**, **"transfer portal"** — all real terms.
- **"CFP"** = College Football Playoff (12-team since 2024).

## 8. Visual motifs

- **Waving pennant flag** — small geometric pennant for rank/seed.
- **Mascot silhouette** (text only, no images).

## 9. Tone

- **Editorial register:** Pageantry-driven, tradition-respecting, but with
  modern analytics. The NY Times CFB coverage is the model.
- **Rivalries are sacred.** Always include series record + last meeting.
- **Recruiting is a story.** Top recruits change games.
- **Coach names matter.** Always include HC and all-time HC vs HC record.

## 10. Print variant

- SP+ tables collapse to top 25
- Recruiting comparison fits on one row
- CFP bracket projection fits on one page
