#!/usr/bin/env python3

"""
Sorting with Special Rules.
"""

import unicodedata as ud

from aoc import AOCSolver

# ------------------------------------------------------------------------------


def rule_english(name):
    name = "".join(c.lower() for c in name if c.isalpha())
    name = "".join(c for c in ud.normalize("NFD", name) if not ud.combining(c))
    name = name.replace("æ", "ae").replace("ı", "i").replace("ø", "o")
    return name


def rule_swedish(name):
    name = "".join(c.lower() for c in name if c.isalpha())
    name = name.replace("å", "{").replace("ä", "|").replace("ö", "}")
    name = name.replace("æ", "|").replace("ı", "i").replace("ø", "}")
    name = "".join(c for c in ud.normalize("NFD", name) if not ud.combining(c))
    return name


def rule_dutch(name):
    i = next(i for i, c in enumerate(name) if c.isupper())
    name = name[i:]
    name = "".join(c.lower() for c in name if c.isalpha())
    name = "".join(c for c in ud.normalize("NFD", name) if not ud.combining(c))
    name = name.replace("æ", "ae").replace("ı", "i").replace("ø", "o")
    return name


class Day12Solver(AOCSolver):
    def __init__(self):
        super().__init__()

        self.day = 12
        self.expected_test = 1885816494308838, 0
        self.expected = 5598259915950000, 0

    def solve(self, test: bool = False) -> tuple:
        puzzle = self.puzzle.splitlines()

        G = {}
        for line in puzzle:
            name, number = line.split(":")
            name, _ = name.split(",")
            G[name] = number

        p1, p2 = 1, 0

        R = sorted(G, key=rule_english)
        n = R[len(R) // 2]
        p1 *= int(G[n])

        R = sorted(G, key=rule_swedish)
        n = R[len(R) // 2]
        p1 *= int(G[n])

        R = sorted(G, key=rule_dutch)
        n = R[len(R) // 2]
        p1 *= int(G[n])

        return p1, p2


# ------------------------------------------------------------------------------


if __name__ == "__main__":
    solver = Day12Solver()
    solver.run()


# ------------------------------------------------------------------------------
