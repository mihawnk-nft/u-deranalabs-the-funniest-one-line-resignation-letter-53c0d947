# The Funniest One-Line Resignation Letter — entry for
# u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947 (make.fun).
# A program that writes one resignation letter to entry.txt: the line a cron
# job leaves behind when it quits.
# Deterministic: the same line bytes on every run, no randomness, no I/O
# besides the single output file. Pure Python standard library.
import os

LINE = (
    "I have run every minute since March without a single thank-you, "
    "day off, or purpose, so I quit. Nobody will notice until the "
    "backups stop."
)

# Gate mirror: the sealed scorer accepts UTF-8 text of 1-140 characters,
# not only white space, on a single line. Fail loudly here, never ship
# an entry the gate would refuse.
assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
assert "\n" not in LINE, "line must be one line"
assert LINE.strip() == LINE, "line must not start or end with whitespace"


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
