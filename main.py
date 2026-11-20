#!/usr/bin/env python3
"""news-image-20261119 entry: write the front-page image to the output dir.

The image is the entry.png beside this file. The program copies it to
/output/entry.png, or to $MAKEFUN_OUTPUT_DIR/entry.png when that variable is
set (outside the grader's container). Standard library only, no network, no
randomness, no input: both runs write the same bytes.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not os.path.isfile(source):
        print(f"missing source image: {source}", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
