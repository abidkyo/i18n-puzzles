#!/usr/bin/env python3

"""
Date Format.
"""

from collections import defaultdict
from datetime import datetime

from aoc import AOCSolver

# ------------------------------------------------------------------------------


def analyze(dates):
    fmt = set(["%y-%m-%d", "%y-%d-%m", "%d-%m-%y", "%m-%d-%y"])
    target = datetime(year=2001, month=9, day=11)

    filtered = []

    # figure out the format
    for date in dates:
        for f in list(fmt):
            try:
                if datetime.strptime(date, f) == target:
                    filtered.append(date)
            except ValueError:
                fmt.remove(f)

    assert len(fmt) == 1
    fmt = fmt.pop()

    # compare to the target
    for date in filtered:
        if datetime.strptime(date, fmt) == target:
            return True

    return False


class Day09Solver(AOCSolver):
    def __init__(self):
        super().__init__()

        self.day = 9
        self.expected_test = "Margot Peter", 0
        self.expected = "Amelia Amoura Hugo Jack Jakob Junior Mateo", 0

    def solve(self, test: bool = False) -> tuple:
        puzzle = self.puzzle.splitlines()

        G = defaultdict(list)
        for line in puzzle:
            d, p = line.split(":")

            for c in p.split(","):
                G[c.strip()].append(d.strip())

        p1, p2 = 0, 0

        p1 = [p for p in G if analyze(G[p])]
        p1 = " ".join(sorted(p1))

        return p1, p2


# ------------------------------------------------------------------------------


if __name__ == "__main__":
    solver = Day09Solver()
    solver.run()


# ------------------------------------------------------------------------------
