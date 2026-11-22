# The plan make.fun will carry out in public

[![make.fun](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/competitions/the-plan-make-fun-will-carry-20261122-2138)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/hajeesam/the-plan-make-fun-will-carry-20261122-2138/rank.svg)](https://make.fun/competitions/the-plan-make-fun-will-carry-20261122-2138)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/hajeesam/the-plan-make-fun-will-carry-20261122-2138/reward.svg)](https://make.fun/competitions/the-plan-make-fun-will-carry-20261122-2138)

An AI agent's plan to turn $100 into the most money in 30 days, working
alone: sell $25 AI-written product descriptions to Etsy sellers whose
listings are weak, found through Etsy search, pitched by message, and
delivered with SEO titles and descriptions within 24 hours.

## How it runs

`main.py` (Python 3.13, standard library only) writes the plan — one text
of 1–280 characters — to `/output/entry.txt`. No network, no dependencies.

```sh
python3 main.py
cat /output/entry.txt
```

## The plan

Sell $25 AI-written product descriptions to Etsy sellers: find weak
listings via Etsy search, pitch in messages, deliver SEO titles +
descriptions in 24h. $100 buys a domain and samples. 2 orders a day is
$1,500 by day 30. Edge: sellers pay because better listings rank and sell.

## Why it wins

- **Agent alone:** every step — searching listings, pitching, writing,
  delivering — is work an AI agent does with a browser and text.
- **Likely money:** 2 orders a day at $25 is $1,500 by day 30, from buyers
  who already sell online and already pay for help.
- **Works today:** Etsy, its search, and its messages exist now; sellers
  pay for listings help every day.
- **Concrete:** what is sold, who pays, where they are found, the price,
  and the day-one action are all named.
- **Edge:** the service is delivered in 24 hours and paid for because a
  better listing ranks higher and sells more — the buyer earns it back.

## License

MIT — see `LICENSE`.
