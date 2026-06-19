# CBB — Design Spec

> NCAA Men's College Basketball. ~32-game regular season, conference
> tournaments, the NCAA Tournament (March Madness — 68-team bracket). The
> visual language **peaks in March** when bracketology takes over. Editorial
> register is **analytics-heavy but tournament-driven**.

---

## 1. Identity

- **League:** NCAA Division I MBB (362 teams, 32 conferences)
- **Season:** November → April (30-35 games)
- **Postseason:** Conference tournaments → NCAA Tournament (68 teams) → Final Four → National Championship
- **Editorial weight:** Highest in March, otherwise narrative-driven.

## 2. Color palette

```js
colors: {
  bg:        '#0a0a0d',
  surface:   '#131318',
  raised:    '#1b1b22',
  ink:       '#e9e9f0',
  hairline:  'rgba(255,255,255,0.08)',
  home:      '#7c3aed',  // tournament purple
  away:      '#0891b2',  // bracket teal
  accent:    '#f59e0b',  // March gold
  live:      '#dc2626',
  done:      '#525252',
  dim:       '#6b7280',
}
```

Anchors: **tournament purple + bracket teal**, accent: **March gold**.

## 3. Typography

- **Display:** `'Roboto Slab', 'Source Serif 4', Georgia, serif`
- **Body:** `'Inter', system-ui, sans-serif`
- **Mono:** `'JetBrains Mono', monospace`

## 4. Section order

### PREVIEW
1. Topline
2. Hero — matchup + ranking + tip-off
3. Stat strip
4. Tale of the Tape
5. Vegas
6. **Bracketology impact preview** (NET ranking, quadrant record)
7. Star player duel
8. Coaching matchup
9. Injury report
10. Fan Pulse
11. CTA

### LIVE
1. Mega-scoreboard
2. Live NET-style efficiency
3. Live stats
4. Run tracker
5. Play-by-play
6. CTA

### RECAP
1. Final score hero
2. AI Verdict
3. Box score
4. 3 turning moments
5. Bracket movement
6. Player grades
7. Fan Verdict
8. CTA

### HUB
1. Topline
2. Next game countdown
3. AP Top 25
4. Conference standings (top 6 conferences)
5. Bracketology (current 68-team projection)
6. Bubble watch
7. Coach of the Year race
8. Wooden Award watch
9. Social buzz (especially March)
10. CTA

## 5. Data modules

| Metric | Notes |
|---|---|
| NET | NCAA Evaluation Tool ranking |
| KenPom | Ken Pomeroy's efficiency rankings |
| BPI | ESPN's Basketball Power Index |
| Quad record | Quadrant wins (1-4) |
| SOS | Strength of schedule |
| AdjOE / AdjDE | Adjusted offensive/defensive efficiency |

## 6. Mock-data schema

```json
{
  "sport": "cbb",
  "season": "2025-26",
  "home": {
    "team":"Duke Blue Devils","abbr":"DUKE",
    "conference":"ACC",
    "rank_ap":4,"rank_net":3,"rank_kenpom":5,
    "record":"18-2","conf_record":"8-1",
    "quad_record":"6-2-0-0",
    "ppg":84.2,"oppg":68.4,
    "adj_oe":118.4,"adj_de":94.1,
    "sos_rank":12,
    "top_player":{"name":"Cooper Flagg","ppg":19.2,"rpg":8.1,"bpg":2.1}
  }
}
```

## 7. Vocabulary

- **"Bracketology"** — always lowercase, one word.
- **"Bubble watch"** — teams on the NCAA Tournament bubble.
- **"Quad 1 win"** — must be specified.
- **"Cinderella"**, **"First Four"**, **"Bracket buster"**.
- **"The Big Dance"** = NCAA Tournament.
- **"Selection Sunday"** — bracket reveal day.

## 8. Visual motifs

- **Bracket lines** — single horizontal/vertical lines used as dividers.
- **Seed number** — circled number used for tournament seeds.

## 9. Tone

- Editorial register: Tournament-obsessed in March, otherwise analytics-first.

## 10. Print variant

- Bracket fits on letter sheet (whole point)
- Bubble watch fits top 10
