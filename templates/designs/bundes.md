# Bundesliga — Design Spec

> German Bundesliga. 18 teams, 34-game season. **Editorial register: organized,
> analytical, less hype.** German football culture emphasizes fan ownership
> (50+1 rule), standing sections, and tactical discipline. Matchdays are
> sacred — Friday night, Saturday afternoon, Sunday afternoon.

---

## 1. Identity

- **League:** Bundesliga (18 teams)
- **Season:** August → May (34 matchdays, also known as "Spieltag")
- **Editorial weight:** High — tactical depth + fan culture.

## 2. Color palette

```js
colors: {
  bg:        '#0a0c0d',
  surface:   '#111518',
  raised:    '#181c20',
  ink:       '#e6e9ec',
  hairline:  'rgba(255,255,255,0.08)',
  home:      '#d20515',  // Bundesliga red
  away:      '#f5d90a',  // Bundesliga gold
  accent:    '#00a651',  // pitch green / DFB green
  live:      '#dc2626',
  done:      '#525252',
  dim:       '#6b7280',
}
```

**Bundesliga red + Bundesliga gold** + **DFB green** for the pitch.

## 3. Typography

- **Display:** `'Source Serif 4', 'Playfair Display', Georgia, serif`
- **Body:** `'Inter', system-ui, sans-serif`
- **Mono:** `'JetBrains Mono', monospace`

## 4. Section order

### PREVIEW
1. Topline — Bundesliga · Spieltag · KO
2. Hero
3. Stat strip
4. Tale of the Tape — record, xG, xGA, xGD
5. Vegas (1X2, O/U, BTTS)
6. Tactical — formation, expected XI, key battle
7. Head-to-head
8. Injury report
9. Fan Pulse
10. CTA

### LIVE
1. Mega-scoreboard
2. Live xG
3. Live stats
4. Live pressing intensity
5. Play-by-play
6. CTA

### RECAP
1. Final score hero
2. AI Verdict
3. Player ratings ("Bundesliga Noten" — out of 1.0 in 0.5 increments)
4. Box score
5. 3 turning moments
6. Tactical
7. Fan Verdict
8. CTA

### HUB
1. Topline
2. Next Spieltag countdown
3. Bundesliga table (1-18)
4. Top 4 / Champions League race
5. Relegation play-off watch (16-17)
6. Torjägerkanone watch (top scorer)
7. **50+1 watch** (fan ownership updates)
8. Lookahead lines
9. Social buzz
10. CTA

## 5. Data modules

Soccer standard + German-specific:
- **Bundesliga Noten** (player ratings 1.0-6.0 in 0.5 increments)
- **Pressing intensity** (PPDA + recoveries)
- **Yellow/Red cards** (more prominent than in other leagues)

## 6. Mock-data schema

```json
{
  "sport": "bundes",
  "season": "2025-26",
  "matchday": 11,
  "home": {
    "team":"Bayern München","abbr":"FCB",
    "stadium":"Allianz Arena","city":"München",
    "record":"9-1-0","points":28,"position":1,
    "xg":28.4,"xga":7.8,
    "formation":"4-2-3-1",
    "manager":"Vincent Kompany",
    "fan_ownership":"75% — Club members"
  }
}
```

## 7. Vocabulary

- **"Spieltag"** = matchday. **"Bundesliga"** capitalized.
- **"Der Klassiker"** = Bayern vs Dortmund.
- **"50+1"** = fan ownership rule.
- **"Südtribüne"** = the famous standing terrace at Dortmund.
- **"Torjägerkanone"** = top scorer cannon award.
- **"Meisterschale"** = championship plate (trophy).
- **"Fußball"** not "Fussball" in modern usage.

## 8. Visual motifs

- **Soccer ball hex pattern** — subtle hexagonal background pattern in
  accent green, 3% opacity.
- **Standing-section stripes** — vertical lines used as section dividers.

## 9. Tone

- **Editorial register:** Organized, analytical, less hype. Raphael
  Honigstein + The Athletic Germany. Tactical depth without the theater.
- **Lead with tactics.** German coverage is formational.
- **Respect fan culture.** 50+1, standing sections — these matter.
- **Der Klassiker is the centerpiece.**

## 10. Print variant

- Table fits comfortably (only 18 teams)
- Player ratings use Bundesliga Noten scale (1.0-6.0)
