# World Cup — Design Spec

> FIFA World Cup. The biggest single-sport event on Earth. 2026 edition: 48
> teams, 12 groups, 104 matches, hosted across USA / Canada / Mexico. **The
> editorial register is monument.** This isn't a league — it's a quadrennial
> global moment.

---

## 1. Identity

- **Tournament:** FIFA World Cup (2026: 48 teams, 12 groups of 4)
- **Cycle:** Every 4 years (Men's)
- **Format:** Group stage (3 matchdays per group) → R32 → R16 → QF → SF → Final
- **Editorial weight:** Maximum. The biggest sporting event on the planet.

## 2. Color palette

**Dynamic per matchup.** Use the two nations' primary flag colors as anchors.
The page should *feel* like a flag exchange.

```js
homePrimary: fromTeamData,  // national flag primary
awayPrimary: fromTeamData,  // national flag primary
bg:        '#0a0a0d',
surface:   '#111319',
raised:    '#181c25',
accent:    '#d4af37',  // World Cup gold (trophy)
live:      '#dc2626',
```

## 3. Typography

- **Display:** `'Cinzel', 'Source Serif 4', Georgia, serif` — wide-spaced
  capital letters for nation names
- **Body:** `'Inter', system-ui, sans-serif`
- **Mono:** `'JetBrains Mono', monospace`

## 4. Section order

### PREVIEW
1. Topline — FIFA World Cup 2026 · Group C · Matchday 2
2. Hero — nation matchup + kickoff + stadium + city
3. Stat strip
4. **Tale of the Tape** — FIFA ranking, recent form, all-time H2H
5. **Road to 2026** — qualifying path + group stage so far
6. Vegas (1X2, O/U, BTTS)
7. **Squad watch** — key player, captain, formation
8. Injury report (international)
9. **Stadium & atmosphere** — capacity, weather, host city vibe
10. **Broadcast** — global TV partners
11. Fan Pulse (predicted score, % picking each team)
12. CTA

### LIVE
1. Mega-scoreboard (clock/score/minute)
2. Live xG
3. Live stats
4. Live shot map
5. Play-by-play
6. CTA

### RECAP
1. Final score hero
2. AI Verdict (tournament-context aware: "advances to R16 as Group C winner")
3. Player ratings
4. Box score
5. 3 turning moments
6. Tactical analysis
7. **Knockout bracket projection**
8. Fan Verdict
9. CTA

### HUB
1. Topline
2. Next matchday countdown
3. **All 12 groups** (A-L) with standings
4. Top scorers (Golden Boot race)
5. **Bracket projection** (top 24 advancing)
6. **Host cities & stadiums** (16 across 3 countries)
7. Manager watch
8. Lookahead lines
9. Social buzz
10. CTA

## 5. Data modules

Soccer standard + World Cup-specific:
- **FIFA ranking** (always shown)
- **Road to 2026** (qualifying path)
- **Group stage position** (1-4)
- **Goals in tournament** (Golden Boot)
- **All-time World Cup record**

## 6. Mock-data schema

```json
{
  "sport": "worldcup",
  "edition": 2026,
  "host": "USA / Canada / Mexico",
  "group": "C",
  "matchday": 2,
  "home": {
    "country":"United States","abbr":"USA",
    "confederation":"CONCACAF",
    "fifa_rank":11,
    "qualifying":"1st · CONCACAF",
    "record_wc":"2W-1D-0L · 7 GF · 2 GA",
    "form":["W","W","D"],
    "manager":"Mauricio Pochettino",
    "top_player":{"name":"Christian Pulisic","club":"AC Milan","pos":"FW","goals":7},
    "formation":"4-3-3"
  },
  "away": { "...": "same shape" },
  "venue": {"name":"SoFi Stadium","city":"Inglewood","capacity":70240,"host":"USA"},
  "kickoff_iso":"2026-06-21T20:00:00-05:00",
  "broadcast":{"usa":"FOX/Mundo","uk":"BBC","global":"FIFA+"},
  "weather":{"temp_f":72,"wind":"6 mph","precip":0}
}
```

## 7. Vocabulary

- **"Matchday"** (in group), **"Round of 32"** (since 2026), **"R16"** etc.
- **"Group of Death"** = the group with multiple top-20 ranked teams.
- **"Bracketology"** doesn't apply the same way — use **"bracket
  projection"**.
- **"Knockout rounds"** / **"knockout stage"** — use interchangeably.
- **"Golden Boot"** = top scorer. **"Golden Glove"** = best GK. **"Golden
  Ball"** = best player.
- **"World Cup holders"** = defending champion.
- **"Eternal glory"** — earned, never thrown around.
- **"Host nation"**, **"co-hosts"** (2026 has 3).
- **"CONCACAF"**, **"UEFA"**, **"CONMEBOL"**, **"CAF"**, **"AFC"**, **"OFC"**.

## 8. Visual motifs

- **Trophy silhouette** — geometric World Cup trophy as a section marker.
- **Flag stripes** — extracted from matchup nations, used as accents.
- **Group letter** — bold geometric letter (A, B, C...) as section marker.

## 9. Tone

- **Editorial register:** Monumental. Reverent. The biggest stage.
- **Lead with the stage.** SoFi Stadium, MetLife, Estadio Azteca — names matter.
- **FIFA ranking always visible.** This is the international standard.
- **Host cities are characters.** LA, NY, Dallas, Mexico City, Toronto, Vancouver.
- **No excuses.** When Argentina loses to Saudi Arabia, you write about it.

## 10. Print variant

- All 12 groups fit on letter sheet (compact view)
- Bracket projection fits on letter sheet (the entire point)
- Stadium map fits on letter sheet
