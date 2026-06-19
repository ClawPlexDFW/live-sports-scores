# WNBA — Design Spec

> Women's National Basketball Association. 40-game regular season, the
> playoffs, the Commissioner's Cup. The visual language should **feel like the
> W** — bold colors, sharp typography, elevated star treatment. No
> diminutives. This is a major professional league.

---

## 1. Identity

- **League:** WNBA (13 teams, 2 conferences)
- **Season:** May → October (40 games)
- **Editorial weight:** Medium-high — star-driven narratives.

## 2. Color palette

```js
colors: {
  bg:        '#0d0a14',  // deep plum-black
  surface:   '#16121e',
  raised:    '#1f1a2a',
  ink:       '#efeaff',
  hairline:  'rgba(255,255,255,0.08)',
  home:      '#c026d3',  // magenta
  away:      '#0e7490',  // teal
  accent:    '#f59e0b',  // trophy gold
  live:      '#dc2626',
  done:      '#525252',
  dim:       '#6b7280',
}
```

**Magenta + teal** — drawn from the WNBA's brand palette.

## 3. Typography

- **Display:** `'Bricolage Grotesque', 'Bebas Neue', 'Inter', sans-serif`
- **Body:** `'Inter', system-ui, sans-serif`
- **Mono:** `'JetBrains Mono', monospace`

## 4. Section order

Follows NBA structure exactly, but with:
- **"Commissioner's Cup"** tier between preview and regular season
- **Star player treatment** is even more elevated
- **Stats are identical vocabulary** to NBA but always lead with player names

## 5. Data modules

Identical to NBA: pace, ORtg/DRtg, eFG%, TS%, plus/minus, four factors.

## 6. Mock-data schema

```json
{
  "sport": "wnba",
  "season": 2025,
  "home": {
    "team": "Las Vegas Aces","abbr":"LV",
    "record":"22-6","conference":"Western",
    "ppg":92.4,"oppg":81.7,
    "pace":96.4,"ortg":110.2,"drtg":102.4,
    "top_player":{"name":"A'ja Wilson","ppg":27.1,"rpg":11.4,"bpg":2.3}
  }
}
```

## 7. Vocabulary

- **Use player names.** A'ja Wilson. Caitlin Clark. Breanna Stewart.
- **"Commissioner's Cup"** = in-season tournament.
- **"Rookie of the Year"** race — always surface in preview.

## 8. Visual motifs

- **Star shape** (5-point) as a star-player marker.

## 9. Tone

- **Editorial register:** Confident, star-focused, modern. Treat every player
  as a star. Don't downplay, don't qualify, don't apologize.
- Lead with stars. Lead with records. Lead with the present.

## 10. Print variant

Standard NBA-equivalent print rules.
