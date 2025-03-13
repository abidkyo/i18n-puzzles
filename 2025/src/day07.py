#!/usr/bin/env python3

"""
DST Time.
"""

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from aoc import AOCSolver

# ------------------------------------------------------------------------------


class Day07Solver(AOCSolver):
    def __init__(self):
        super().__init__()

        self.day = 7
        self.expected_test = 866, 0
        self.expected = 32152346, 0

    def solve(self, test: bool = False) -> tuple:
        puzzle = self.puzzle.splitlines()

        p1, p2 = 0, 0
        for i, line in enumerate(puzzle, 1):
            dt, correct, incorrect = line.split()
            correct = int(correct)
            incorrect = int(incorrect)

            dt = datetime.fromisoformat(dt)

            for tz in ["America/Halifax", "America/Santiago"]:
                loc = dt.astimezone(ZoneInfo(tz))
                if dt.isoformat() == loc.isoformat():
                    break
            else:
                assert False

            ndt = dt + timedelta(minutes=correct - incorrect)
            ndt = ndt.astimezone(ZoneInfo(tz))

            p1 += ndt.hour * i

        return p1, p2


# ------------------------------------------------------------------------------


if __name__ == "__main__":
    solver = Day07Solver()
    solver.run()


# ------------------------------------------------------------------------------
