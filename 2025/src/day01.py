#!/usr/bin/env python3

"""
Characters and Bytes.
"""

from aoc import AOCSolver

# ------------------------------------------------------------------------------


class Day01Solver(AOCSolver):
    def __init__(self):
        super().__init__()

        self.day = 1
        self.expected_test = 31, 0
        self.expected = 107989, 0

    def solve(self, test: bool = False) -> tuple:
        puzzle = self.puzzle.splitlines()

        p1, p2 = 0, 0
        for line in puzzle:
            line = line.strip()
            c, b = len(line), len(bytes(line, "utf-8"))

            cost = 0
            if c <= 140:
                cost += 7
            if b <= 160:
                cost += 11

            if cost == 18:
                cost = 13

            p1 += cost

        return p1, p2


# ------------------------------------------------------------------------------


if __name__ == "__main__":
    solver = Day01Solver()
    solver.run()


# ------------------------------------------------------------------------------
