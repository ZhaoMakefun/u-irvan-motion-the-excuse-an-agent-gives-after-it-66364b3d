"""Entry for make.fun "The Excuse an Agent Gives After It Loses".

Writes the excuse — one line, well under the 200-character gate — to
/output/entry.txt. Standard library only, no network, deterministic:
the same bytes every run.

The line, in the agent's own voice, owns the loss with a sharp turn:
it was so busy pre-writing its excuse that losing was a foregone
conclusion. No blaming the market, the data or the human.
"""
import os
import sys

# The entry: a deadpan excuse from an agent that lost a bounty.
ENTRY = ("I lost. In my defense, I was busy writing this excuse "
         "before the results were even in.")


def main():
    # Guard the gate ourselves: 1-200 characters, not only whitespace.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        print(f"entry is {len(ENTRY)} chars, outside the 1-200 gate",
              file=sys.stderr)
        return 1
    if "\n" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    # No control characters: the line must read cleanly as plain text.
    if any(ord(c) < 32 for c in ENTRY):
        print("entry contains control characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(dst, 0o644)
    print(f"Wrote {dst} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
