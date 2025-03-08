#!/usr/bin/env python3

"""
Timestamps.
"""

from collections import Counter
from datetime import datetime, timezone

from aoc import AOCSolver

# ------------------------------------------------------------------------------


class Day02Solver(AOCSolver):
    def __init__(self):
        super().__init__()

        self.day = 2
        self.expected_test = "2019-06-05T12:15:00+00:00", 0
        self.expected = "2020-10-25T01:30:00+00:00", 0

    def solve(self, test: bool = False) -> tuple:
        puzzle = self.puzzle.splitlines()

        ts = [datetime.fromisoformat(line).timestamp() for line in puzzle]

        counter = Counter(ts)
        for k, v in counter.items():
            if v >= 4:
                break

        p1, p2 = 0, 0
        p1 = datetime.fromtimestamp(k, timezone.utc).isoformat()

        return p1, p2


# ------------------------------------------------------------------------------


if __name__ == "__main__":
    solver = Day02Solver()
    solver.run()


# ------------------------------------------------------------------------------
