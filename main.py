#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message: one commit message for the bug
fix that made everything worse.

Deterministic: one fixed line, written to $MAKEFUN_OUTPUT_DIR/entry.txt,
read back and asserted byte-identical.
"""
import os

LINE = "fix: resolve crash by deleting the button users kept pressing"
MAX_CHARS = 100


def main():
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, limit {MAX_CHARS}"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        back = f.read()
    assert back == data, "read-back mismatch"
    text = back.decode("utf-8")
    assert text == LINE, "decoded text differs from the line"
    assert text == text.strip(), "line has leading or trailing whitespace"
    print(f"wrote {len(data)} bytes ({len(LINE)} chars) to {path}")


if __name__ == "__main__":
    main()
