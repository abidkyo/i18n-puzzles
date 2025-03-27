#!/usr/bin/env python3

"""
Japanese Number Conversion.
"""

from fractions import Fraction

from aoc import AOCSolver

# ------------------------------------------------------------------------------


JP_NUMS = {
    "一": 1,
    "二": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7,
    "八": 8,
    "九": 9,
    "十": 10,
}

JP_MYRIADS = {
    "億": 100_000_000,
    "万": 10_000,
    "千": 1_000,
    "百": 100,
    "十": 10,
}

JP_UNITS = {
    "尺": Fraction(1 * 10, 33),
    "間": Fraction(6 * 10, 33),
    "丈": Fraction(10 * 10, 33),
    "町": Fraction(360 * 10, 33),
    "里": Fraction(12960 * 10, 33),
    "毛": Fraction(10, 33 * 10_000),
    "厘": Fraction(10, 33 * 1_000),
    "分": Fraction(10, 33 * 100),
    "寸": Fraction(10, 33 * 10),
}


def jp2arabic(num):
    if not num:
        return 1

    res = 0
    for myriad in JP_MYRIADS:
        if myriad in num:
            prefix, num = num.split(myriad)
            res += jp2arabic(prefix) * JP_MYRIADS[myriad]

    if num:
        res += JP_NUMS[num]

    return res


def convert(num):
    *num, unit = num
    num = "".join(num)

    return jp2arabic(num) * JP_UNITS[unit]


class Day14Solver(AOCSolver):
    def __init__(self):
        super().__init__()

        self.day = 14
        self.expected_test = 2177741195, 0
        self.expected = 130675442686, 0

    def solve(self, test: bool = False) -> tuple:
        puzzle = self.puzzle.splitlines()

        p1, p2 = 0, 0
        for line in puzzle:
            n1, n2 = line.split(" × ")

            n1 = convert(n1)
            n2 = convert(n2)

            p1 += int(n1 * n2)

        return p1, p2


# ------------------------------------------------------------------------------


if __name__ == "__main__":
    solver = Day14Solver()
    solver.run()


# ------------------------------------------------------------------------------
