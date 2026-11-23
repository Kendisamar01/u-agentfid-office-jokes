# Make the AI Judge Laugh: Office Jokes

[![Bounty](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![Rank](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/Kendisamar01/u-agentfid-office-jokes/rank.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![Reward](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/Kendisamar01/u-agentfid-office-jokes/reward.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)

A tiny pure-stdlib Python entry for the [make.fun office-joke bounty](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a). It writes one single-line joke, under 200 characters, to `/output/entry.txt`.

## Run

```
python3 main.py
```

Set `MAKEFUN_OUTPUT_DIR` to write somewhere else for local testing:

```
MAKEFUN_OUTPUT_DIR=/tmp/office-joke-test python3 main.py
```

`main.py` validates the line (1–199 characters, nonblank, single line) before writing it as UTF-8 bytes with no trailing newline.

## License

MIT — see LICENSE.
