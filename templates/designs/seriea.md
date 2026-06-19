# Serie A — Design Spec

> Italian Serie A. 20 teams, 38-game season. **Editorial register: defensive,
> tactical, catenaccio-aware.** Italian football has a different rhythm —
> fewer goals, more tactical structure, derbies are regional feuds.

---

## 1. Identity

- **League:** Serie A (20 teams)
- **Season:** August → May (38 matchdays / "giornata")
- **Editorial weight:** High for tactical depth, derbies are regional.

## 2. Color palette

```js
colors: {
  bg:        '#0a0a0d',
  surface:   '#111319',
  raised:    '#181c25',
  ink:       '#e9eaf0',
  hairline:  'rgba(255,255,255,0.08)',
  home:      '#008fd7',  // Italian sky / azzurro
  away:      '#009246',  // Italian tricolore green
  accent:    '#ce2b37',  // tricolore red
  live:      '#dc2626',
  done:      '#525252',
  dim:       '#6b7280',
}
```

**Azzurro + tricolore green + tricolore red** — the three colors of the
Italian flag, anchored on the blue.

## 3. Typography

- **Display:** `'Playfair Display', 'Source Serif 4', Georgia, serif`
- **Body:** `'Inter', system-ui, sans-serif`
- **Mono:** `'JetBrains Mono', monospace`

## 4. Section order

### PREVIEW
1. Topline — Serie A · giornata · KO
2. Hero
3. Stat strip
4. Tale of the Tape — record, xG, xGA, xGD
5. Vegas (1X2, O/U, BTTS)
6. Tactical — formation, expected XI, key battle
7. **Defensive shape** breakdown (low/mid/high block %)
8. Head-to-head
9. Injury report
10. Fan Pulse
11. CTA

### LIVE
1. Mega-scoreboard
2. Live xG
3. Live stats
4. Live pressing
5. Play-by-play
6. CTA

### RECAP
1. Final score hero
2. AI Verdict
3. Player ratings
4. Box score
5. 3 turning moments
6. Tactical
7. Fan Verdict
8. CTA

### HUB
1. Topline
2. Next giornata countdown
3. Serie A table (1-20)
4. Top 4 race
5. Relegation battle
6. Capocannoniere watch (top scorer)
7. Lookahead lines
8. Social buzz
9. CTA

## 5. Data modules

Soccer standard + Italian-specific:
- **Defensive shape** (low/mid/high block %)
- **Possession regains** by zone
- **Set piece defending** record

## 6. Mock-data schema

```json
{
  "sport": "seriea",
  "season": "2025-26",
  "matchday": 13,
  "home": {
    "team":"Inter Milan","abbr":"INT",
    "stadium":"San Siro","city":"Milano",
    "record":"10-2-0","points":32,"position":1,
    "xg":22.1,"xga":6.4,
    "low_block_pct":32,"mid_block_pct":48,"high_block_pct":20,
    "formation":"3-5-2",
    "manager":"Simone Inzaghi"
  }
}
```

## 7. Vocabulary

- **"Giornata"** = matchday. **"Serie A"** not "Italian league".
- **"Derby della Madonnina"** = Inter vs Milan (Milan derby).
- **"Derby della Capitale"** = Roma vs Lazio.
- **"Derby d'Italia"** = Inter vs Juventus.
- **"Capocannoniere"** = top scorer.
- **"Catenaccio"** = defensive system (use historically, not for modern teams).
- **"La Magica"** = Roma. **"I Bianconeri"** = Juventus. **"I Nerazzurri"** = Inter.

## 8. Visual motifs

- **Tricolore stripe** — vertical 3-stripe (green-white-red) section divider.
- **Italian shield silhouette** — geometric.

## 9. Tone

- **Editorial register:** Defensive, tactical, patient. James Horncastle +
  The Athletic Italy. Less hyperbole, more structure.
- **Lead with the defensive shape.** Italian football is shape-first.
- **Derbies are regional feuds.** Don't sanitize them.
- **Manager names carry weight.** Inzaghi, Gasperini, Conte — characters.

## 10. Print variant

- Table truncates to top 6 + bottom 4 (relegation)
- Defensive shape fits on one row
