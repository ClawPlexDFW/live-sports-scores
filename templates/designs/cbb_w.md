# CBB_W — Design Spec

> NCAA Women's College Basketball. The game is at peak attention — Caitlin
> Clark era, Angel Reese vs Caitlin narratives, Final Four ratings records.
> The visual language should **celebrate the stars** and **modernize the
> presentation**.

---

## 1. Identity

- **League:** NCAA Division I WBB (362 teams, 32 conferences)
- **Season:** November → April
- **Postseason:** 68-team NCAA Tournament → Final Four → National Championship
- **Editorial weight:** Star-driven, rising fast.

## 2. Color palette

```js
colors: {
  bg:        '#0a0a0e',
  surface:   '#13131c',
  raised:    '#1b1b25',
  ink:       '#ecedf2',
  hairline:  'rgba(255,255,255,0.08)',
  home:      '#be185d',  // modern rose
  away:      '#0e7490',  // deep teal
  accent:    '#facc15',  // championship gold
  live:      '#dc2626',
  done:      '#525252',
  dim:       '#6b7280',
}
```

Anchors: **modern rose + deep teal**, accent: **championship gold**.

## 3. Typography

- **Display:** `'Bricolage Grotesque', 'Inter Display', sans-serif` — modern
  geometric, less traditional than CBB
- **Body:** `'Inter', system-ui, sans-serif`
- **Mono:** `'JetBrains Mono', monospace`

## 4. Section order

Follows CBB structure but with:
- **Player names elevated** above team names in hero treatment
- **Triple-double** watch (more common in women's game)
- **Naismith Award** watch instead of Wooden

## 5. Data modules

Same metrics as CBB: NET, KenPom, BPI, Quad record, SOS, AdjOE/AdjDE.

## 6. Mock-data schema

```json
{
  "sport": "cbb_w",
  "home": {
    "team":"Iowa Hawkeyes","abbr":"IOWA",
    "rank_ap":2,"rank_net":1,
    "record":"22-1","top_player":{"name":"Caitlin Clark","ppg":32.1,"apg":8.4}
  }
}
```

## 7. Vocabulary

- Same as CBB but **"Naismith Trophy"** not Wooden.
- **"Triple-double"** more frequent (Clark, Plum, etc.).
- **"Transfer portal"** changed women's game significantly.

## 8-10. Standard

Same visual structure as CBB but with the modern colorway.
