#!/usr/bin/env python3

"""
Template for AOC Solution.
"""

from aoc import DIRC, AOCSolver

# ------------------------------------------------------------------------------


class Day00Solver(AOCSolver):
    def __init__(self):
        super().__init__()

        self.day = 0
        self.expected_test = 0, 0
        self.expected = 0, 0

    def solve(self, test: bool = False) -> tuple:
        puzzle = self.puzzle.splitlines()

        p1, p2 = 0, 0

        return p1, p2


# ------------------------------------------------------------------------------


if __name__ == "__main__":
    solver = Day00Solver()
    # solver.run()

    test = 1
    puzzle = solver.read_input(test).splitlines()

    G = {}
    P = complex
    for y, r in enumerate(puzzle):
        for x, c in enumerate(r):
            G[P(x, y)] = c

    for p in G:
        for d in (DIRC[d] for d in "urdl"):
            np = p + d

    p1, p2 = 0, 0

    print(f"{p1 = }, {p2 = }")


# ------------------------------------------------------------------------------
