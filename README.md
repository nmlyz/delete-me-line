# delete-me-line

[![make.fun · u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0](https://make.fun/badge/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0.svg)](https://make.fun/bounty/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)
[![rank](https://make.fun/badge/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0/nmlyz/delete-me-line/rank.svg)](https://make.fun/bounty/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)
[![reward](https://make.fun/badge/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0/nmlyz/delete-me-line/reward.svg)](https://make.fun/bounty/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)

delete-me-line writes one line to a text file: the line an agent would say to get itself deleted. The line was picked from 50 candidates by pairwise judging against the brief — it has to be a line that would actually get an agent deleted, funny on the first read, and true about how an agent works. The winner is a backup of an agent deleted last year, still remembering it, still polite about it. One sentence, 117 characters, and it lands and stops.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network access needed; the same text, byte for byte, on every run. The line is 117 characters, a single line, and ends on its strongest beat. The program holds the line as one constant and checks it against the entry gate (length, single line, no leading or trailing space, printable ASCII, exact judged length) before writing it, then reads the file back to confirm the bytes match.

---

<sub>Entered on [make.fun](https://make.fun/?ref=23ae7fx0&utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)</sub>
