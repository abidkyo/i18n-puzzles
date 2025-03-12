#!/usr/bin/env python3

"""
Grid with UTF-16 characters.

but Python dont have this issue :)
"""

from aoc import AOCSolver

# ------------------------------------------------------------------------------


class Day05Solver(AOCSolver):
    def __init__(self):
        super().__init__()

        self.day = 5
        self.expected_test = 2, 0
        self.expected = 74, 0

    def solve(self, test: bool = False) -> tuple:
        puzzle = self.puzzle.splitlines()

        G = {}
        for y, r in enumerate(puzzle):
            for x, c in enumerate(r):
                G[(x, y)] = c

        R, C = y + 1, x + 1

        p1, p2 = 0, 0
        x, y = 0, 0
        while True:
            if G[(x, y)] == "💩":
                p1 += 1

            nx, ny = (x + 2) % C, (y + 1)

            if ny >= R:
                break

            x, y = nx, ny

        return p1, p2


# ------------------------------------------------------------------------------


if __name__ == "__main__":
    solver = Day05Solver()
    solver.run()


# ------------------------------------------------------------------------------
