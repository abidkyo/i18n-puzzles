#!/usr/bin/env python3

"""
Character Encoding.
"""

from aoc import AOCSolver

# ------------------------------------------------------------------------------


class Day06Solver(AOCSolver):
    def __init__(self):
        super().__init__()

        self.day = 6
        self.expected_test = 50, 0
        self.expected = 11252, 0

    def solve(self, test: bool = False) -> tuple:
        dictionary, puzzle = self.puzzle.split("\n\n")

        dictionary = dictionary.splitlines()
        puzzle = [line.strip() for line in puzzle.splitlines()]

        for i, word in enumerate(dictionary, 1):
            if i % 3 == 0:
                word = word.encode("iso8859-1").decode("utf-8")
            if i % 5 == 0:
                word = word.encode("iso8859-1").decode("utf-8")
            dictionary[i - 1] = word

        p1, p2 = 0, 0

        for line in puzzle:
            idx = next(i for i, c in enumerate(line) if c != ".")
            idx = next(
                i
                for i, word in enumerate(dictionary, 1)
                if len(word) == len(line) and word[idx] == line[idx]
            )
            p1 += idx

        return p1, p2


# ------------------------------------------------------------------------------


if __name__ == "__main__":
    solver = Day06Solver()
    solver.run()


# ------------------------------------------------------------------------------
