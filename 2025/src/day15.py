#!/usr/bin/env python3

"""
Coverage across Timezones.
"""

from datetime import datetime, timedelta
from itertools import product
from zoneinfo import ZoneInfo

from aoc import AOCSolver

# ------------------------------------------------------------------------------


def get_coverage(data, kind):
    _, tz, holidays = data.split("\t")

    holidays = [
        datetime.strptime(holiday, "%d %B %Y") for holiday in holidays.split(";")
    ]

    coverage = set()
    for y, m, d in list(product([2022], range(1, 13), range(1, 32))) + [[2021, 12, 31]]:
        try:
            date = datetime(y, m, d)
        except ValueError:
            continue

        # skip weekend and holidays
        if date.weekday() not in range(5) or date in holidays:
            continue

        if kind == "office":
            # set working time
            start = datetime(y, m, d, 8, 30, tzinfo=ZoneInfo(tz))
            end = datetime(y, m, d, 17, 00, tzinfo=ZoneInfo(tz))
        elif kind == "customer":
            # set active time
            start = datetime(y, m, d, 0, 0, tzinfo=ZoneInfo(tz))
            end = start + timedelta(hours=24)
        else:
            assert False

        # calc difference from utc
        start -= datetime(2022, 1, 1, tzinfo=ZoneInfo("UTC"))
        end -= datetime(2022, 1, 1, tzinfo=ZoneInfo("UTC"))

        # normalize in 30-minutes block
        start = int(start.total_seconds() // 60 // 30)
        end = int(end.total_seconds() // 60 // 30)

        coverage |= set(range(start, end))

    # filter time
    maxs = datetime(2023, 1, 1) - datetime(2022, 1, 1)
    maxs = int(maxs.total_seconds() // 60 // 30)
    coverage = set(filter(lambda x: x in range(maxs), coverage))

    return coverage


class Day15Solver(AOCSolver):
    def __init__(self):
        super().__init__()

        self.day = 15
        self.expected_test = 3030, 0
        self.expected = 37890, 0

    def solve(self, test: bool = False) -> tuple:
        offices, customers = self.puzzle.split("\n\n")

        cov_office = set.union(
            *(get_coverage(data, "office") for data in offices.splitlines())
        )
        overtimes = [
            len(get_coverage(data, "customer") - cov_office) * 30
            for data in customers.splitlines()
        ]

        p1, p2 = 0, 0
        p1 = max(overtimes) - min(overtimes)

        return p1, p2


# ------------------------------------------------------------------------------


if __name__ == "__main__":
    solver = Day15Solver()
    solver.run()


# ------------------------------------------------------------------------------
