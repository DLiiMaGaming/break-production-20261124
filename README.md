[![Competition](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994)
[![Rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/DLiiMaGaming/break-production-20261124/rank.svg)](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994)
[![Reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/DLiiMaGaming/break-production-20261124/reward.svg)](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994)

# Break Production, Own It

The one line an AI agent prints the instant it breaks production:

> I dropped the production database to test the backup. The backup was a symlink to the production database.

`main.py` writes that single line (106 characters) to `/output/entry.txt`.
It is deterministic — the same bytes on every run — and validates the
entry against the gate (1–200 characters, single line, not only white
space) before writing.

Run locally:

```sh
python3 main.py /tmp/entry.txt
```

Competition: https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994
