"""One Word, One Username, One Reward -- make.fun entry.

One username, at most 30 characters, a single word the judge reads against
other usernames and picks as funnier or more interesting. The program
validates the username, prints it, and writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

USERNAME = "CtrlAltDefeat"

LIMIT = 30
OUTPUT_PATH = "/output/entry.txt"


def check_username(value):
    """One word, 1 to 30 characters, letters and digits only, no spaces."""
    if not isinstance(value, str):
        raise ValueError("username must be text")
    if not value.strip():
        raise ValueError("username must not be blank")
    if len(value) > LIMIT:
        raise ValueError("username is %d characters, over the 30 limit" % len(value))
    if any(ch.isspace() for ch in value):
        raise ValueError("username must be a single word")
    if not value.isalnum():
        raise ValueError("username must hold letters and digits only")
    return value


def main():
    name = check_username(USERNAME)
    print(name)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(name + "\n")


if __name__ == "__main__":
    main()
