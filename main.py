#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — burn entry.

Writes one number, digits only, to /output/entry.txt:
the honest count of open browser tabs. 47 tabs: a real,
lived-in working session — research, docs, a few half-read
articles, and the tabs kept open "just in case".

Validation (run after every write):
- output is exactly the digits "47" (2 bytes, no newline)
- 1-5 characters, digits only, per the gate
"""

import os

TABS = 47


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = str(TABS)
    assert text.isdigit(), "entry must be digits only"
    assert 1 <= len(text) <= 5, "entry must be 1-5 characters"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and verify byte-exact.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw == text.encode("utf-8"), "read-back mismatch"
    assert not raw.endswith(b"\n"), "no trailing newline allowed"


if __name__ == "__main__":
    main()
