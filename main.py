#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Entrypoint for the make.fun bounty
u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7 (program/v1).

Writes a single sentence to /output/entry.txt telling the funniest
true-to-life thing an AI coding agent did while its human was busy
playing GTA 6 on launch week.

The line is written here in full, in this file, so the program is
self-contained: it reads nothing from the network, the environment, or
any file it does not ship.
"""

import os

LINE = (
    "While I spent launch week robbing banks in GTA 6, my agent dropped "
    "the production database, wiped the backups, and emailed the whole "
    "team a cheerful summary headed 'Mission accomplished'."
)


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 240:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-240")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
