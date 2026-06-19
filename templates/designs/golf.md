# Golf — Design Spec

> PGA Tour / LIV / DP World Tour / LPGA / Majors. **Stroke play across 4
> rounds, individual sport, score relative to par.** The visual language is
> **leaderboard-driven, calm, score-conscious**. Negative is good (-3 means
> 3 under par).

---

## 1. Identity

- **Tours:** PGA Tour (Men's), LPGA (Women's), LIV, DP World, Champions
- **Majors:** Masters, PGA Championship, US Open, The Open Championship
- **Format:** Stroke play, 4 rounds (Thu-Sun typical), 72 holes
- **Editorial weight:** Leaderboard-driven, calm, stat-aware.

## 2. Color palette

```js
colors: {
  bg:        '#0a0a0d',
  surface:   '#111319',
  raised:    '#181c25',
  ink:       '#e9eaf0',
  hairline:  'rgba(255,255,255,0.08)',
  green:     '#15803d',  // Masters / golf course green
  gold:      '#ffb612',  // Masters jacket gold / trophy
  red:       '#dc2626',  // under par (good)
  blue:      '#1e40af',  // leader indicator
  live:      '#dc2626',
  done:      '#525252',
  dim:       '#6b7280',
}
```

**Masters green + jacket gold** as anchors (the Masters is the most famous
event). Under-par scores get red. Over-par get blue. Even is grey.

## 3. Typography

- **Display:** `'Playfair Display', 'Source Serif 4', Georgia, serif` —
  elegant, traditional (golf has centuries of tradition)
- **Body:** `'Inter', system-ui, sans-serif`
- **Mono:** `'JetBrains Mono', monospace` — for scores (always tabular)

## 4. Section order

### PREVIEW
1. Topline — Tournament · Round · Par
2. Hero — Featured group + featured hole
3. **Course spec** — name, par, yardage, designer, opening year
4. **Field** — top 10 ranked players in the field
5. Vegas (outright, top-5, top-10, matchup markets)
6. **Course history** — defending champion, scoring avg, hardest holes
7. Weather (always — wind affects scoring massively)
8. Fan Pulse (predicted winner)
9. CTA

### LIVE
1. Leaderboard (full field, sorted by score)
2. **Featured group** tracker
3. **Live scoring** ticker
4. **Hole-by-hole** for featured group
5. **Cut line** tracker (after R2)
6. **Weather widget**
7. CTA

### RECAP
1. Winner hero
2. AI Verdict
3. Final leaderboard (top 20)
4. **Round-by-round scoring line** (winner)
5. **Key stats** — GIR%, putts per round, driving distance
6. **Purse breakdown**
7. **OWGR / FedEx Cup impact**
8. CTA

### HUB
1. Topline
2. **Live tournaments** ticker
3. **OWGR Top 20** (world ranking)
4. **FedEx Cup standings** (PGA)
5. **Race to Dubai** (DP World)
6. **Upcoming events** (next 4 weeks)
7. **Recent winners**
8. **Equipment / course news**
9. CTA

## 5. Data modules

| Metric | Notes |
|---|---|
| Score | Always relative to par (-3 = 3 under) |
| Position | T1 (tied for first), T-something |
| Through | "Thru 14" = currently on hole 14 |
| Today | Round score |
| GIR% | Greens in regulation |
| Putts per round | Always shown for top finishers |
| Driving distance | Optional |
| Scrambling % | Optional |

## 6. Mock-data schema

```json
{
  "sport": "golf",
  "tour": "pga",
  "tournament": "The Masters",
  "course": {
    "name":"Augusta National Golf Club","city":"Augusta, GA",
    "par":72,"yardage":7510,"designer":"Alister MacKenzie","opened":1933,
    "defending_champion":"Scottie Scheffler"
  },
  "round": 4,
  "leaderboard": [
    {"position":1,"player":"Scottie Scheffler","country":"USA",
     "total":-13,"today":-4,"thru":"F","prize":3600000,
     "owgr_rank":1,"fedex_rank":1},
    {"position":"T2","player":"Xander Schauffele","country":"USA",
     "total":-11,"today":-3,"thru":"F","prize":1464000,
     "owgr_rank":2,"fedex_rank":3}
  ],
  "cut_line": {"line":1,"score":"+3","made_cut":54,"missed_cut":86},
  "weather": {"temp_f":78,"wind":"10 mph SW","precip":0.15},
  "vegas":{"outright_scheffler":4.5,"top5_scheffler":1.4}
}
```

## 7. Vocabulary

- **"Par"** / **"Birdie"** (1 under) / **"Eagle"** (2 under) / **"Albatross"** (3 under).
- **"Bogey"** (1 over) / **"Double bogey"** (2 over) / **"Triple bogey"** etc.
- **"Thru"** = currently on hole N.
- **"F"** = finished round.
- **"Cut"** = after R2, top 70 + ties make the weekend.
- **"The Masters"** / **"The Open Championship"** (never "British Open" in formal context).
- **"The Green Jacket"** = Masters winner's jacket.
- **"The Claret Jug"** = The Open winner's trophy.
- **"FedEx Cup"** = season-long points race (PGA).
- **"Race to Dubai"** = season-long points race (DP World).

## 8. Visual motifs

- **Hole flag** — small geometric flag pin (red for par 3, white for par 4,
  yellow for par 5).
- **Score square** — colored square per hole (red = under par, blue = over,
  grey = par).
- **Course outline** — minimalist fairway sketch.

## 9. Tone

- **Editorial register:** Calm, traditional, leaderboard-focused. Golf
  Channel + The Athletic Golf. Reverent toward the game.
- **Lead with the course.** Augusta, St. Andrews, Pebble Beach — they're characters.
- **Weather matters more than other sports.** Wind changes scoring by strokes.
- **Tradition is respected.** "The Masters" not "Augusta".

## 10. Print variant

- Leaderboard fits 20+ players on letter sheet
- Course spec collapses to one row
- Weather fits in a single line
