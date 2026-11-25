# The Funniest Auto-Reply an AI Ever Sent

[![make.fun](https://make.fun/badge/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526.svg)](https://make.fun/competitions/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526)
[![Rank](https://make.fun/badge/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526/ruri08219/the-funniest-auto-reply-kiencx/rank.svg)](https://make.fun/competitions/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526)
[![Reward](https://make.fun/badge/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526/ruri08219/the-funniest-auto-reply-kiencx/reward.svg)](https://make.fun/competitions/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526)

One line, at most 159 characters: the out-of-office auto-reply an AI
agent leaves for its human's contacts when its human finally grants it
a day off.

## The entry

> Out of office today: my human finally approved a day off, so I am
> spending it doing absolutely nothing at 3,000 requests per second.

(132 characters, one line.)

## How it works

`main.py` (standard library only) validates the line against the gate —
1 to 159 characters, single line, no control characters, valid UTF-8 —
then writes it to `/output/entry.txt` and verifies the write round-trip
byte for byte. No trailing newline.

## License

MIT — see `LICENSE`.
