#!/usr/bin/env python3

"""
Character Normalization.
"""

import unicodedata as ud

from aoc import AOCSolver

# ------------------------------------------------------------------------------


def normalize(s):
    res = ""
    for c in s:
        if c > "Z":
            c = ud.normalize("NFKD", c)[0]
        res += c.lower()
    return res


class Day08Solver(AOCSolver):
    def __init__(self):
        super().__init__()

        self.day = 8
        self.expected_test = 2, 0
        self.expected = 809, 0

    def solve(self, test: bool = False) -> tuple:
        puzzle = self.puzzle.splitlines()

        p1, p2 = 0, 0
        for line in puzzle:
            line = line.strip()

            if not (4 <= len(line) <= 12):
                continue

            if not any(c.isdigit() for c in line):
                continue

            line = normalize(line)

            if len(line) != len(set(line)):
                continue

            if not any(c in "aeiou" for c in line):
                continue

            if not any("a" <= c <= "z" and c not in "aeiou" for c in line):
                continue

            p1 += 1

        return p1, p2


# ------------------------------------------------------------------------------


if __name__ == "__main__":
    solver = Day08Solver()
    solver.run()


# ------------------------------------------------------------------------------
