#!/usr/bin/env python3
"""Plan: turn $100 into the most money in 30 days, alone.

Writes the plan to /output/entry.txt (1-280 Unicode chars).
Python 3.13, standard library only, no network.
"""

from pathlib import Path

PLAN = (
    # Math: 10 sales/week x 4 weeks x $19 = $760 by day 30; $12 domain
    # is the only spend, so $88 of the $100 stays unspent as buffer.
    "Build 5 digital products alone: Notion templates, spreadsheet tools, "
    "a tiny web utility. Sell each on Gumroad at $19. Day 1: ship two, then "
    "post daily demos on X and 3 niche subreddits. $12 domain, $0 ads. "
    "10 sales/week = $760 by day 30. Edge: products sell while you sleep."
)


def main() -> None:
    text = PLAN.strip()
    if not 1 <= len(text) <= 280:
        raise ValueError(f"plan is {len(text)} chars, must be 1-280")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {out}")


if __name__ == "__main__":
    main()
