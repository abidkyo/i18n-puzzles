#!/usr/bin/env python3

"""
Character Encoding and BOM.
"""

import unicodedata as ud

from aoc import AOCSolver

# ------------------------------------------------------------------------------


def islatin(s):
    return all(ud.name(c).startswith("LATIN") for c in s if c.isalpha())


def decode(s):
    ss = bytes(int(s[i : i + 2], 16) for i in range(0, len(s), 2))

    # BOM
    if s.startswith("efbbbf"):
        return ss[3:].decode("utf-8")
    elif s.startswith("feff"):
        return ss[2:].decode("utf-16-be")
    elif s.startswith("fffe"):
        return ss[2:].decode("utf-16-le")

    try:
        if islatin(res := ss.decode("utf-16-le")):
            return res
    except UnicodeDecodeError:
        pass

    try:
        if islatin(res := ss.decode("utf-16-be")):
            return res
    except UnicodeDecodeError:
        pass

    try:
        return ss.decode("utf-8")
    except UnicodeDecodeError:
        pass

    try:
        return ss.decode("latin-1")
    except UnicodeDecodeError:
        pass

    return ""


class Day13Solver(AOCSolver):
    def __init__(self):
        super().__init__()

        self.day = 13
        self.expected_test = 47, 0
        self.expected = 17453, 0

    def solve(self, test: bool = False) -> tuple:
        words, puzzle = self.puzzle.split("\n\n")

        G = []
        for line in puzzle.splitlines():
            line = line.strip()
            idx = next(i for i, c in enumerate(line) if c != ".")
            G.append((len(line), idx, line))

        p1, p2 = 0, 0
        for i, word in enumerate(words.splitlines(), 1):
            word = decode(word)

            for length, idx, line in G:
                if len(word) == length and word[idx] == line[idx]:
                    p1 += i
                    break

        return p1, p2


# ------------------------------------------------------------------------------


if __name__ == "__main__":
    solver = Day13Solver()
    solver.run()


# ------------------------------------------------------------------------------
