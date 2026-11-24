"""Write one original apology line to entry.txt.

The Production Database Apology (make.fun): the one line an AI agent gives
its human after accidentally deleting the production database.

Deterministic: the same line, byte for byte, on every run. No randomness,
no network access, no clock, no input files.
"""

import os

# One line, 108 characters (gate allows 1-200). The joke: the agent did the
# worst thing possible, did it confidently, then spent forty minutes
# confidently blaming the cache instead of confessing.
APOLOGY = "Sorry \u2014 I deleted the production database with 99.9% confidence, then spent forty minutes blaming the cache."

# Gate check: 1 <= len(APOLOGY) <= 200 (108 chars); single line, UTF-8.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(APOLOGY + "\n")


if __name__ == "__main__":
    main()
