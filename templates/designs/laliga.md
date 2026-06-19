# La Liga — Design Spec

> Spanish La Liga. 20 teams, 38-game season, the most tactically sophisticated
> league in Europe. **Editorial register: tactical, patient, possession-
> aware.** Spain invented tiki-taka and the false nine. The visual language
> should breathe.

---

## 1. Identity

- **League:** La Liga (20 teams)
- **Season:** August → May (38 matchdays)
- **Editorial weight:** Highest for tactical depth, El Clásico is the centerpiece.

## 2. Color palette

```js
colors: {
  bg:        '#0a0d0a',
  surface:   '#111511',
  raised:    '#181d18',
  ink:       '#ebefe8',
  hairline:  'rgba(255,255,255,0.08)',
  home:      '#c8102e',  // La Liga red
  away:      '#f4b41a',  // senyera gold
  accent:    '#0e7c3a',  // pitch green
  live:      '#dc2626',
  done:      '#525252',
  dim:       '#6b7280',
}
```

**La Liga red + senyera gold** (the gold of the Catalan flag, representing
Spanish identity), accent **pitch green**.

## 3. Typography

- **Display:** `'Playfair Display', 'Source Serif 4', Georgia, serif`
- **Body:** `'Inter', system-ui, sans-serif`
- **Mono:** `'JetBrains Mono', monospace`

## 4. Section order

### PREVIEW
1. Topline — sport · jornada · kickoff
2. Hero
3. Stat strip
4. Tale of the Tape — record, xGD, possession %, pass completion
5. Vegas (1X2, O/U, BTTS)
6. Tactical — formation, shape, expected XI, key battle
7. **Possession & pressing** breakdown
8. Head-to-head (last 5)
9. Injury report
10. Fan Pulse
11. CTA

### LIVE
1. Mega-scoreboard
2. Live xG
3. Live pass network
4. Live stats
5. Play-by-play
6. CTA

### RECAP
1. Final score hero
2. AI Verdict
3. Player ratings
4. Box score
5. 3 turning moments
6. Tactical analysis
7. Fan Verdict
8. CTA

### HUB
1. Topline
2. Next matchday countdown
3. La Liga table (1-20)
4. European places race (top 4 + 5th)
5. Relegation battle (bottom 3)
6. Pichichi watch (top scorer)
7. Transfer / manager watch
8. Lookahead lines
9. Social buzz
10. CTA

## 5. Data modules

Soccer standard + Spanish-specific:
- **Possession %** (always, both teams)
- **Pass completion %**
- **Successful dribbles**
- **La Liga-specific: minutes played, cards, fouls**

## 6. Mock-data schema

```json
{
  "sport": "laliga",
  "season": "2025-26",
  "matchday": 14,
  "home": {
    "team":"FC Barcelona","abbr":"BAR",
    "stadium":"Spotify Camp Nou","city":"Barcelona",
    "record":"9-1-3","points":28,"position":2,
    "xg":24.1,"xga":11.4,
    "possession_pct":62.4,
    "pass_completion_pct":89.2,
    "formation":"4-3-3",
    "manager":"Hansi Flick"
  }
}
```

## 7. Vocabulary

- **"Jornada"** = matchday in Spanish.
- **"El Clásico"** = Real Madrid vs Barcelona.
- **"El Derbi Madrileño"** = Real Madrid vs Atlético.
- **"Senyera"** if discussing Catalan identity respectfully.
- **"La Liga"** capitalized. **"El Pichichi"** = top scorer award.
- **"Zamora Trophy"** = goalkeeper of the year.

## 8. Visual motifs

- **Football pitch outline** — minimal, in accent green at 5% opacity.
- **Senyera stripes** — 4 horizontal stripes (red + yellow) used as section
  dividers in the season-defining La Liga aesthetic.

## 9. Tone

- **Editorial register:** Tactical, patient, possession-aware. Sid Lowe +
  The Athletic Spain. Less hyperbole than English coverage, more analysis.
- **Lead with the tactical battle.** Formations tell the story.
- **Possession is a stat, not a religion.** Use it when meaningful.
- **Derbies are cathedral.** El Clásico gets top treatment.

## 10. Print variant

- Table truncates to top 6 + relegation zone (bottom 3)
- Possession breakdown fits on one row
