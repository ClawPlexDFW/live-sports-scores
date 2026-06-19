# Soccer Live — Design Spec

> Global live soccer, multi-league. Aggregates games from EPL / La Liga /
> Bundesliga / Serie A / UCL / World Cup / MLS / Liga MX / Brasileirão / etc.
> into a single global feed. **Editorial register: aggregator, ticker-style,
> never deep on any one game.**

---

## 1. Identity

- **League:** Global, multi-league
- **Editorial weight:** Low per game, high in volume — the goal is to scan
  hundreds of matches at once.

## 2. Color palette

```js
colors: {
  bg:        '#0a0a0d',
  surface:   '#111319',
  raised:    '#181c25',
  ink:       '#e9eaf0',
  hairline:  'rgba(255,255,255,0.08)',
  // Per-matchup dynamic — drawn from each game's teams
  live:      '#dc2626',  // pulsing red
  done:      '#525252',  // grey for FINAL
  upcoming:  '#0891b2',  // teal for SCHEDULED
  dim:       '#6b7280',
}
```

**No fixed anchors.** Every row of the live ticker takes its accent from the
two teams playing. Background stays consistent.

## 3. Typography

- **Display:** `'Source Serif 4', 'Playfair Display', Georgia, serif` — used
  only in headers
- **Body:** `'Inter', system-ui, sans-serif`
- **Mono:** `'JetBrains Mono', monospace` — for clock, minute, score

## 4. Section order

This is a **ticker mode**, not a preview. The page is a long, scannable feed.

### LIVE ticker
1. Topline — global soccer live · X games · Y leagues · Z countries
2. Filter chips — league / status / search
3. Live ticker — every game in a compact row:
   - League badge (EPL, La Liga, etc.)
   - Clock / minute
   - Team logos + names
   - Score (large)
   - Status pill (LIVE pulsing / FINAL / SCHEDULED)
   - Optional: goal events, red cards (highlighted)
4. CTA — load more

### LIVE detail (when a game is clicked)
1. Mega-scoreboard
2. Live xG + stats
3. Play-by-play
4. CTA

### HUB
1. Topline
2. League selector (chips)
3. Standings per league
4. Today's matches across leagues
5. CTA

## 5. Data modules

| Metric | Notes |
|---|---|
| Live minute | 1'–90+ |
| Score | Always shown |
| xG (when available) | Optional |
| Status | LIVE / HT / FT / SCHEDULED |
| League | Always shown |

## 6. Mock-data schema

```json
{
  "sport": "soccer_live",
  "home": {
    "team":"Arsenal","abbr":"ARS","league":"EPL",
    "country":"ENG","score":2,"color":"#ef0107"
  },
  "away": {
    "team":"Liverpool","abbr":"LIV","league":"EPL",
    "country":"ENG","score":1,"color":"#c8102e"
  },
  "status": "LIVE",
  "minute": 67,
  "events": [
    {"minute":12,"type":"goal","team":"home","player":"Saka"},
    {"minute":34,"type":"goal","team":"away","player":"Salah"},
    {"minute":58,"type":"goal","team":"home","player":"Ødegaard"}
  ]
}
```

## 7. Vocabulary

- **"Live ticker"**, **"global feed"**.
- **"Pulsing red"** = LIVE indicator.
- **"Pill"** = small status badge.
- **"League"** not "competition" (more universal).
- **"HT"** = halftime.

## 8. Visual motifs

- **League badge** — small geometric shape per league (EPL = lion, La Liga
  = trophy, etc.) or simple monogram.
- **Country flag stripe** — small horizontal tricolor beside country code.

## 9. Tone

- **Editorial register:** Aggregator, ticker-style, scan-friendly. No narrative
  on the index — clicking into a game gets the full preview/live treatment.
- **Density over depth.** Every pixel carries information.

## 10. Print variant

- Ticker becomes a static table
- League filter chips removed
- 30+ games fit on letter sheet
