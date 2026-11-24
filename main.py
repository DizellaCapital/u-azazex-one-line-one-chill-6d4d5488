"""One Line, One Chill entry program.

Writes a single sentence of horror — under 200 characters — to
MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only. The line is the whole entry:
no setup, no paragraph, no second chance.
"""

import os
import sys

LINE = "At 3:04 a.m., the library's return slot clinked, and the book I checked out in 1998 slid back across the desk \u2014 stamped DUE TODAY, in my dead father's handwriting."


def main():
    if not (1 <= len(LINE) <= 200):
        print(f"entry must be 1-200 characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not LINE.endswith("."):
        print("entry must be one complete sentence", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
