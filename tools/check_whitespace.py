#!/usr/bin/env python3
"""Whitespace gate for the trail files: one line per entry, nothing around it.

Fails on a tab, a carriage return, whitespace at either end of a line, a blank first line, a run
of blank lines, a blank last line, or a missing final newline. Every one of these has been
committed here (most often by a web editor), and every one is invisible in a review.

    python3 tools/check_whitespace.py          # report, exit 1 on findings
    python3 tools/check_whitespace.py --fix    # rewrite the offending files

A fix never changes an entry: 'git diff -w --ignore-blank-lines' stays empty.
"""

import os
import sys

PILES = ("malware", "malicious", "suspicious")


def normalize(text):
    out = []
    for line in text.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        line = line.strip(" \t")          # only these two: a stray U+00A0 is a broken ENTRY, the other gate's business
        if line == "" and (not out or out[-1] == ""):
            continue                      # a blank first line, or the second of a run
        out.append(line)
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + "\n" if out else ""


def main(argv):
    fix = "--fix" in argv
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bad = []
    for pile in PILES:
        for dirpath, _, names in os.walk(os.path.join(root, pile)):
            for name in sorted(names):
                if not name.endswith(".txt"):
                    continue
                path = os.path.join(dirpath, name)
                with open(path, "rb") as f:
                    raw = f.read().decode("utf-8", "surrogateescape")
                clean = normalize(raw)
                if clean == raw:
                    continue
                bad.append(os.path.relpath(path, root))
                if fix:
                    with open(path, "wb") as f:
                        f.write(clean.encode("utf-8", "surrogateescape"))
    for path in bad:
        print("%s %s" % ("[fixed]" if fix else "[!]", path))
    if bad and not fix:
        print("[!] %d file(s) with stray whitespace: run 'python3 tools/check_whitespace.py --fix'" % len(bad))
        return 1
    print("[i] %s" % ("%d file(s) normalized" % len(bad) if fix else "whitespace is clean"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
