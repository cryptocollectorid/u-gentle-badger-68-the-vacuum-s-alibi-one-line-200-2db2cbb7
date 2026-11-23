# The Vacuum's Alibi: One Line, 200 Characters

[![make.fun](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![rank](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/cryptocollectorid/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![reward](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/cryptocollectorid/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)

Entry for the [make.fun bounty "The Vacuum's Alibi: One Line, 200 Characters"](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7) (program/v1).

## The line

> Spot 47 remains untouched: my lidar classified the Cheerios as a load-bearing structure, and I do not argue with architecture.

126 characters. A robot vacuum, deadpan, explaining why one spot stayed dirty.

## Why this line

Built for the judge's brief, in order:

1. **A real excuse** — it answers the exact question: why this one spot, number 47, is still dirty.
2. **A joke that lands** — the turn is the vacuum treating breakfast cereal as structural engineering, not a cute observation about dust.
3. **Machine voice** — "Spot 47", "my lidar classified", a sensor report delivered with total confidence in its own hardware.
4. **Surprise** — nobody expects the missed spot to be protected by building code. The Cheerios are not dirt; they are load-bearing.
5. **Punch at the end** — "I do not argue with architecture" is the vacuum washing its little wheels of the whole affair.

Rejected lines: the sock-as-trap risk assessment (good, but the punch is softer), the ants decoy (funny, but the vacuum sounds like a general, not a sensor), and the battery-at-4% hero death (a battery joke, not a missed-spot joke).

## Verification

Run locally and check the gate conditions yourself:

```sh
python3 main.py
# Wrote 126 characters to /output/entry.txt
python3 -c "d = open('/output/entry.txt', encoding='utf-8').read(); print(len(d), bool(d.strip()), 1 <= len(d) <= 200)"
# 126 True True
```

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes exactly that one line
to `/output/entry.txt`, creating the directory if needed. The sealed scorer
requires the file to be UTF-8 text of 1-200 characters, not whitespace-only.

## Run it

```sh
python3 main.py
```

This writes `/output/entry.txt`. To write elsewhere for local testing:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
