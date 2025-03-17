#!/usr/bin/env python3

"""
Greek Letters.
"""

from aoc import AOCSolver

# ------------------------------------------------------------------------------


class Day11Solver(AOCSolver):
    def __init__(self):
        super().__init__()

        self.day = 11
        self.expected_test = 19, 0
        self.expected = 688, 0

    def solve(self, test: bool = False) -> tuple:
        puzzle = self.puzzle.splitlines()

        odys = ["Οδυσσευς", "Οδυσσεως", "Οδυσσει", "Οδυσσεα", "Οδυσσευ"]
        odys = [ody.upper() for ody in odys]

        p1, p2 = 0, 0
        for line in puzzle:
            line = line.upper()

            # normalize
            s = [ord(c) - 913 for c in line if 913 <= ord(c) <= 937]

            for i in range(1, 24):
                # rotate by 1
                s = [((c + 1) % 25) for c in s]
                # fix
                s = [18 if c == 17 else c for c in s]
                # convert
                res = "".join(chr(c + 913) for c in s)

                if any(ody in res for ody in odys):
                    p1 += i
                    break

        return p1, p2


# ------------------------------------------------------------------------------


if __name__ == "__main__":
    solver = Day11Solver()
    solver.run()


# ------------------------------------------------------------------------------
