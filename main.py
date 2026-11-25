#!/usr/bin/env python3
"""make.fun news-image-20261124 entry: copy the bundled entry.png to the
output directory as entry.png. Python 3.13 standard library only."""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(here, "entry.png"),
                    os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
