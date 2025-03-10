#!/usr/bin/env python3

"""
Timezones.
"""

from datetime import datetime
from zoneinfo import ZoneInfo

from aoc import AOCSolver

# ------------------------------------------------------------------------------


def datetime2timestamp(dt, tz):
    res = datetime.strptime(dt, "%b %d, %Y, %H:%M")
    res = res.replace(tzinfo=ZoneInfo(tz))
    return res.timestamp()


class Day04Solver(AOCSolver):
    def __init__(self):
        super().__init__()

        self.day = 4
        self.expected_test = 3143, 0
        self.expected = 16451, 0

    def solve(self, test: bool = False) -> tuple:
        puzzle = self.puzzle.split("\n\n")

        p1, p2 = 0, 0
        for block in puzzle:
            dep, arr = block.splitlines()

            _, dtz, *dt = dep.split()
            dt = " ".join(dt)

            _, atz, *at = arr.split()
            at = " ".join(at)

            dts = datetime2timestamp(dt, dtz)
            ats = datetime2timestamp(at, atz)

            p1 += ats - dts

        p1 //= 60

        return p1, p2


# ------------------------------------------------------------------------------


if __name__ == "__main__":
    solver = Day04Solver()
    solver.run()


# ------------------------------------------------------------------------------
