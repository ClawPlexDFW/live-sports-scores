# UFC — Design Spec

> Ultimate Fighting Championship. MMA, not a team sport. **Editorial register:
> fighter-first, physical, stat-tracked.** UFC is individual — the page IS the
> fighter. No team, no coach, just two people and their camps.

---

## 1. Identity

- **Promotion:** UFC (Ultimate Fighting Championship)
- **Format:** Events with multiple fights per card; main event is the headliner
- **Editorial weight:** Fighter-driven, hype-aware, never dismissive.

## 2. Color palette

```js
colors: {
  bg:        '#08080a',
  surface:   '#111114',
  raised:    '#1a1a1f',
  ink:       '#ebebf0',
  hairline:  'rgba(255,255,255,0.08)',
  red:       '#d20a11',  // UFC octagon red
  gold:      '#ffb612',  // UFC championship gold
  blue:      '#0033a0',  // UFC brand blue
  live:      '#dc2626',
  done:      '#525252',
  dim:       '#6b7280',
}
```

Anchors: **UFC octagon red + championship gold**.

## 3. Typography

- **Display:** `'Bebas Neue', 'Oswald', 'Impact', sans-serif` — tall,
  condensed, poster-like, fighter names should *feel like a poster*
- **Body:** `'Inter', system-ui, sans-serif`
- **Mono:** `'JetBrains Mono', monospace` — for reach, slpm, td%

## 4. Section order

### PREVIEW (fight preview)
1. Topline — UFC 312 · Main Event · Light Heavyweight
2. Hero — fighter A vs fighter B, with weight class + belt indicator
3. Tale of the Tape (side-by-side, fighter-focused)
4. **Striking stats** — SLpM, Striking Accuracy, Striking Defense
5. **Grappling stats** — Td Avg, Td Accuracy, Td Defense, Sub Avg
6. **Physical** — age, height, reach, stance, weight
7. **Recent form** — last 5 fights (W/L + method)
8. **Path to this fight** — last 3 opponents
9. Vegas (moneyline, O/U rounds, method)
10. **Fight camp intel** — coaches, training partners, location
11. **Storylines** — rivalry, beef, redemption arc, etc.
12. Fan Pulse
13. CTA

### LIVE (event in progress)
1. Event header — UFC 312 · Live
2. Fight card progress (which fight is live, which are done)
3. Mega-scoreboard (round, time, judge scorecards if needed)
4. Live strike map
5. Live takedown log
6. Play-by-play (round-by-round recap)
7. CTA

### RECAP (post-fight)
1. Final result hero
2. AI Verdict
3. Method of victory (KO/TKO/Submission/Decision)
4. Round + time
5. 3 turning moments
6. **Performance bonuses** tracker
7. **What's next** — title shot implications
8. Fan Verdict
9. CTA

### HUB (event preview)
1. Topline — UFC 312 · Saturday · Etihad Arena
2. **Main card countdown**
3. Fight card (all fights with weight class)
4. **Title fights** highlighted
5. **Co-main** featured
6. **Title eliminator** marker
7. **Ranked contenders** indicator
8. **Lookahead** — next 3 events
9. Social buzz
10. CTA

## 5. Data modules

| Metric | Notes |
|---|---|
| Record | W-L-D |
| SLpM | Significant strikes landed per minute |
| Str. Acc. | Striking accuracy % |
| Str. Def. | Striking defense % |
| TD Avg | Takedowns per 15min |
| TD Acc | Takedown accuracy % |
| TD Def | Takedown defense % |
| Sub. Avg | Submission attempts per 15min |
| Reach | Inches (always shown) |
| Stance | Orthodox / Southpaw / Switch |

## 6. Mock-data schema

```json
{
  "sport": "ufc",
  "event": "UFC 312",
  "fight_number": 12,
  "is_main_event": true,
  "weight_class": "Light Heavyweight",
  "is_title_fight": true,
  "fighter_a": {
    "name":"Alex Pereira","nickname":"Poatan","country":"Brazil",
    "record":"11-2-0","age":37,"height_cm":193,"reach_cm":201,
    "stance":"Orthodox","weight_lb":205,
    "rank":"C","rank_position":1,
    "slpm":7.84,"str_acc":0.621,"str_def":0.561,
    "td_avg":0.0,"td_acc":0.0,"td_def":0.847,
    "sub_avg":0.0,
    "last_5":[{"result":"W","method":"KO","round":1,"opponent":"Hill"}],
    "camp":"Connecticut","coach":"Glover Teixeira"
  },
  "fighter_b": { "...": "same shape" },
  "venue":{"name":"Etihad Arena","city":"Abu Dhabi","capacity":18000},
  "broadcast":{"network":"ESPN+ PPV","price_usd":79.99},
  "vegas":{"moneyline_a":-180,"moneyline_b":+155,"o_u_rounds":2.5,"method":"KO/TKO +165"}
}
```

## 7. Vocabulary

- **"Main event"** / **"Co-main"** / **"Main card"** / **"Prelims"**.
- **"Title fight"** / **"Title eliminator"** / **"Non-title fight"**.
- **"Catchweight"** = non-standard weight class.
- **"Method of victory"** = KO, TKO, Submission, Decision (unanimous /
  split / majority).
- **"Performance of the Night"** / **"Knockout of the Night"** bonuses.
- **"Rank"** = C (champion), 1-15 (ranked contender), NR (unranked).
- **"Pound-for-pound"** (P4P) list.
- **"Five-round main event"** (championship fights are 5 rounds, others 3).

## 8. Visual motifs

- **Octagon shape** — 8-sided polygon as section marker.
- **Belt silhouette** — horizontal championship belt icon.
- **Reach bar** — horizontal bar comparing two fighters' reach.

## 9. Tone

- **Editorial register:** Fighter-first, physical, hype-aware but never
  dismissive. Ariel Helwani + The Athletic MMA.
- **Lead with the fighters.** Names, nicknames, records.
- **Path to the fight matters.** Last 3 opponents contextualize the booking.
- **No team.** Camps matter, but the fighter is the unit.

## 10. Print variant

- Tale of the Tape fits in two columns side-by-side
- Strike map simplifies to per-round totals
- Bonus tracker collapses to one row
