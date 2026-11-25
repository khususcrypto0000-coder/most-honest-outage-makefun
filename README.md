# The Most Honest Outage Line

One line for a status page, written by the on-duty AI agent while every
server is down. It states what is down and admits what the agent cannot
verify: whether a request sent during the outage went through, was lost,
or will run twice when the servers return — so it asks the reader not to
retry it yet. Plain, first-person, specific, no cause invented, no ETA
invented.

[![make.fun · u-mgwals-the-most-honest-outage-line-baaf9c81](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/khususcrypto0000-coder/most-honest-outage-makefun/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/khususcrypto0000-coder/most-honest-outage-makefun/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)

## The entry

> All servers are down. I cannot tell whether the request you just sent went through, was lost, or will run twice when we return. Please do not retry it yet.

## Run

```sh
python3 main.py
```

Writes `/output/entry.txt` (UTF-8, one line, no trailing newline), then
reads it back and asserts it is byte-identical.
