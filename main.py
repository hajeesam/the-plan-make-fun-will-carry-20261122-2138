#!/usr/bin/env python3
"""Plan entry: turn $100 into recurring revenue in 30 days.

Writes the plan text (1-280 Unicode chars) to /output/entry.txt.
Stdlib only, no network.
"""
import os

PLAN = (
    "Find Shopify stores with no blog via BuiltWith. "
    "Offer one free 800-word post, then $49/mo for 4 posts. "
    "10 clients = $490/mo by day 30. "
    "Spend $20 domain/hosting, $80 API credits for prospecting. "
    "Edge: direct outreach, not waiting in Fiverr queue."
)
# 245 chars: under the 280-char limit, full $100 budget accounted for
# ($20 hosting + $80 prospecting credits), recurring revenue from day 30.


def main():
    assert 1 <= len(PLAN) <= 280, f"plan length {len(PLAN)} out of range"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN)
    print(f"wrote {len(PLAN)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
