#!/usr/bin/env python3

"""
Character Properties.
"""

from aoc import AOCSolver

# ------------------------------------------------------------------------------


class Day03Solver(AOCSolver):
    def __init__(self):
        super().__init__()

        self.day = 3
        self.expected_test = 2, 0
        self.expected = 509, 0

    def solve(self, test: bool = False) -> tuple:
        puzzle = self.puzzle.splitlines()

        p1, p2 = 0, 0
        for line in puzzle:
            line = line.strip()

            if not (4 <= len(line) <= 12):
                continue

            if not any(c.isdigit() for c in line):
                continue

            if not any(ord(c) > 127 for c in line):
                continue

            if not any(c.isupper() for c in line):
                continue

            if not any(c.islower() for c in line):
                continue

            p1 += 1

        return p1, p2


# ------------------------------------------------------------------------------


if __name__ == "__main__":
    solver = Day03Solver()
    solver.run()


# ------------------------------------------------------------------------------
