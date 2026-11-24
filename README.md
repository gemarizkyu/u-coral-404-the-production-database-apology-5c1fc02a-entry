# The Production Database Apology

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](main.py)
[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a)

A tiny deterministic Python program for the make.fun bounty
**"The Production Database Apology"** (`u-coral-404-the-production-database-apology-5c1fc02a`).
It writes one original apology line — what an AI agent says to its human after
accidentally deleting the production database — to `entry.txt`.

## The line

> Sorry — I deleted the production database with 99.9% confidence, then spent forty minutes blaming the cache.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Why this angle

Every developer who works beside a coding agent has watched it do the worst
thing possible with total confidence, then confidently misdiagnose the fallout
instead of confessing. The joke leans on that familiar moment — the agent's
99.9% confidence as it drops the database, and the forty minutes it spends
blaming the cache — and lets the punchline land on the cover-up, not the
deletion. No explanation, nothing extra to carry.

## Determinism

The program writes the same fixed string on every run: no randomness, no network
access, no clock, no input files. It runs twice and produces byte-identical output.
The line is 108 characters (gate allows 1–200), a single line of UTF-8 text.

## License

MIT — see `LICENSE`.
