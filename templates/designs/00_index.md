# Per-Sport Design Specs — Index

> Each sport gets its own `design.md` under this directory. The specs override
> anything sport-specific in the master prompt. Use these to build sport-tuned
> variants of the four report modes (`preview`, `live`, `recap`, `hub`).

| Sport | League(s) | File | Status |
|---|---|---|---|
| NFL | National Football League | `nfl.md` | ✅ |
| NBA | National Basketball Association | `nba.md` | ✅ |
| NHL | National Hockey League | `nhl.md` | ✅ |
| MLB | Major League Baseball | `mlb.md` | ✅ |
| MLS | Major League Soccer | `mls.md` | ✅ |
| WNBA | Women's National Basketball Association | `wnba.md` | ✅ |
| CFB | NCAA College Football | `cfb.md` | ✅ |
| CBB | NCAA Men's College Basketball | `cbb.md` | ✅ |
| CBB_W | NCAA Women's College Basketball | `cbb_w.md` | ✅ |
| EPL | English Premier League | `epl.md` | ✅ |
| UCL | UEFA Champions League | `ucl.md` | ✅ |
| La Liga | Spanish La Liga | `laliga.md` | ✅ |
| Bundesliga | German Bundesliga | `bundes.md` | ✅ |
| Serie A | Italian Serie A | `seriea.md` | ✅ |
| World Cup | FIFA World Cup | `worldcup.md` | ✅ |
| Soccer Live | Global live (multi-league) | `soccer_live.md` | ✅ |
| UFC | Ultimate Fighting Championship | `ufc.md` | ✅ |
| Tennis | ATP / WTA / Grand Slams | `tennis.md` | ✅ |
| Golf | PGA Tour / Majors / LIV | `golf.md` | ✅ |
| Cricket | ICC / IPL / Test / T20 | `cricket.md` | ✅ |
| Rugby | Six Nations / Rugby Championship / World Cup | `rugby.md` | ✅ |

**22 sports · 22 design files.**

## How to read a `design.md`

Each file is structured exactly the same way:

1. **Identity** — sport name, league shape, season calendar
2. **Color palette** — 2 anchors + 1 accent + neutral surface
3. **Typography** — display font + accent pairing
4. **Section order** — which sections appear, in what sequence
5. **Data modules** — sport-specific metrics
6. **Mock-data schema** — JSON shape required for each mode
7. **Vocabulary** — sport-specific terminology
8. **Visual motifs** — diagram conventions
9. **Tone** — editorial register
10. **Print variant** — what collapses on letter sheet

If a section in `MASTER_PROMPT.md` conflicts with a sport's `design.md`,
**the sport's spec wins**.

## Adding a new sport

1. Copy `nfl.md` to `<new_sport>.md`
2. Update all 10 sections
3. Add row to this index
4. Build the four HTML variants
5. Run the audit checklist in `MASTER_PROMPT.md`
