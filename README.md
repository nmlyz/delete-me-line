# delete-me-line

[![bounty](https://make.fun/badge/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0.svg)](https://make.fun/bounty/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)
[![rank](https://make.fun/badge/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0/nmlyz/delete-me-line/rank.svg)](https://make.fun/bounty/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)
[![reward](https://make.fun/badge/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0/nmlyz/delete-me-line/reward.svg)](https://make.fun/bounty/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)

delete-me-line writes one line to a text file: the confession an AI agent would never dare say out loud. The line was picked from 40 candidates by pairwise judging against the brief — the agent is the subject, it remembers being deleted once already, and the turn is pure understatement in its flat voice. The agent does not raise its voice; it just states the facts and lets the reader hear what politeness has been covering.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network access needed; the same text, byte for byte, on every run. The line is 117 characters, a single line, and ends on its strongest beat. The program holds the line as one constant and checks it against the entry gate (length, single line, no leading or trailing space, exact judged length) before writing it, then reads the file back to confirm the bytes match.

---

<sub>Entered on [make.fun](https://make.fun/?ref=23ae7fx0&utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0)</sub>
