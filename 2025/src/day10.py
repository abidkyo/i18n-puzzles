#!/usr/bin/env python3

"""
Bcrypt with Character Normalization.
"""

import unicodedata as ud
from functools import cache

from aoc import AOCSolver
from bcrypt import checkpw

# ------------------------------------------------------------------------------


def dp(s, i=0, r=""):
    if i == len(s):
        yield r
    else:
        c = s[i]
        n = ud.normalize("NFD", c)
        if n != c:
            yield from dp(s, i + 1, r + n)
        yield from dp(s, i + 1, r + c)


@cache
def check(secret, hash):
    for secret in dp(secret):
        secret = secret.encode("utf-8")
        if checkpw(secret, hash):
            return True
    return False


class Day10Solver(AOCSolver):
    def __init__(self):
        super().__init__()

        self.day = 10
        self.expected_test = 4, 0
        self.expected = 2513, 0

    def solve(self, test: bool = False) -> tuple:
        database, attempts = self.puzzle.split("\n\n")

        D = {}
        for line in database.splitlines():
            name, hash = line.split()
            D[name] = hash.encode("utf-8")

        p1, p2 = 0, 0
        for line in attempts.splitlines():
            name, secret = line.split()

            hash = D[name]
            secret = ud.normalize("NFC", secret)
            p1 += check(secret, hash)

        return p1, p2


# ------------------------------------------------------------------------------


if __name__ == "__main__":
    solver = Day10Solver()
    solver.run()


# ------------------------------------------------------------------------------
