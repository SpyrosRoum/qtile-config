"""
A quick script to check if my config is okay.
Not sure if it's 100% correct, but it's faster than `qtile check` and so far hasn't failed me.
"""

import argparse
import sys
from pathlib import Path

from libqtile.confreader import Config


def main(filepath: Path) -> None:
    try:
        config = Config(filepath)
        config.load()
        config.validate()
    except Exception as e:
        print("========== Error ==========", file=sys.stderr)
        raise e
    else:
        is_ok = True
        if len(config.keys) == 0:
            is_ok = False
            print("Warning: `keys` is empty", file=sys.stderr)
        if len(config.groups) == 0:
            is_ok = False
            print("Warning: `groups` is empty", file=sys.stderr)

        if is_ok:
            print("Looks good")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check a Qtile config for errors.")
    parser.add_argument("filepath", type=Path, help="The file to check")
    args = parser.parse_args()
    main(args.filepath)
