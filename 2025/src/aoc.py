#!/usr/bin/env python3

"""
AOC Utilities.
"""

from collections.abc import Iterable
from copy import deepcopy
from itertools import chain, islice, pairwise, product, repeat
from math import floor, gcd, log10, sqrt
from re import findall
from timeit import default_timer as timer

# CONSTANTS --------------------------------------------------------------------

INFINITY = float("inf")
EN_DIGITS = dict(
    zip(
        "zero, one, two, three, four, five, six, seven, eight, nine".split(", "),
        range(0, 10),
    )
)

# x,y point
DIR = {
    "u": (0, -1),
    "r": (1, 0),
    "d": (0, 1),
    "l": (-1, 0),
    "ur": (1, -1),
    "ul": (-1, -1),
    "dr": (1, 1),
    "dl": (-1, 1),
}

DIRC = {
    "u": -1j,
    "r": 1,
    "d": 1j,
    "l": -1,
    "ur": 1 - 1j,
    "dr": 1 + 1j,
    "dl": -1 + 1j,
    "ul": -1 - 1j,
}

# CLASS ------------------------------------------------------------------------


class AOCSolver:
    def __init__(self):
        self.year = 2015
        self.day = 0
        self.expected_test = 0, 0
        self.expected = 0, 0

    def run(self) -> None:
        print(f"AOC {self.year} Day {self.day:02}")

        self.puzzle = self.read_input(test=True)

        start = timer()
        p1, p2 = self.solve(test=True)
        t = (timer() - start) * 1000
        print(f"Test: {p1 = }, {p2 = }, {t = :.3f} ms")
        assert (p1, p2) == self.expected_test, self.expected_test

        self.puzzle = self.read_input(test=False)

        start = timer()
        p1, p2 = self.solve(test=False)
        t = (timer() - start) * 1000
        print(f"Real: {p1 = }, {p2 = }, {t = :.3f} ms")
        assert (p1, p2) == self.expected, self.expected

    def solve(self, test: bool = False) -> tuple:
        p1, p2 = 0, 0

        return p1, p2

    def read_input(self, test: bool) -> str:
        # filename == "input/day01.txt" or "input/day01_test.txt"

        filename = f"input/day{self.day:02d}"
        filename += "_test" if test else ""
        filename += ".txt"

        with open(filename, "r") as f:
            return f.read()


# FUNCTIONS --------------------------------------------------------------------


def cat(iterable):
    return "".join(iterable)


def printn(obj):
    print(*obj, sep="\n")


def print2d(grid: list):
    for row in grid:
        print(cat(row))


def map_tuple(f, iterable):
    return tuple(map(f, iterable))


def map_list(f, iterable):
    return list(map(f, iterable))


def sign(num: int):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0


def lcm(nums: Iterable) -> int:
    assert type(list(nums)[0]) is int

    res = 1
    for n in nums:
        res = res * n // gcd(res, n)
    return res


def concat_int(x: int, y: int) -> int:
    assert y >= 0, "positive y-values only"

    if y > 0:
        a = floor(log10(y))
    else:
        a = -1

    return x * 10 ** (a + 1) + y


def identity_matrix(n: int, val: int = 1):
    mat = []
    for i in range(n):
        mat.append([])
        for j in range(n):
            if i == j:
                mat[i].append(val)
            else:
                mat[i].append(0)

    return mat


def get_neighbour(x, y, direction=4):
    assert direction in {3, 4, 8, 9}

    for dx, dy in product([-1, 0, 1], repeat=2):
        if (
            (direction == 3 and abs(dx) == abs(dy) and not dx == dy == 0)  # diagonal
            or (direction == 4 and abs(dx) != abs(dy))  # cardinal
            or (direction == 8 and not dx == dy == 0)  # compass
            or (direction == 9)
        ):
            yield (x + dx, y + dy)


def en_digit(string: str) -> int:
    """Parse digit 0 - 9 in english spelling."""

    for key, value in EN_DIGITS.items():
        if string.startswith(key):
            return value
    return -1


def quad_root(a, b, c) -> tuple:
    dis = b**2 - 4 * a * c
    r1 = (b - sqrt(dis)) / 2 * a
    r2 = (b + sqrt(dis)) / 2 * a
    return r1, r2


def digits(string: str) -> list:
    return map_list(int, string)


def integers(string: str) -> tuple:
    return map_tuple(int, findall(r"-?\d+", string))


def manhattan_distance(x: tuple, y: tuple) -> int:
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def euclidean_distance(x: tuple, y: tuple) -> int:
    return sqrt(abs(x[0] - y[0]) ** 2 + abs(x[1] - y[1]) ** 2 + abs(x[2] - y[2]) ** 2)


def tuple_sum(a: tuple, b: tuple) -> tuple:
    return tuple(sum([x, y]) for x, y in zip(a, b))


def shoelace(points: list[tuple[int, int]]) -> int:
    """
    Shoelace algorithm: Calculate area of polygon
    A = 1/2(x0.y1 - x1.y0 + ... + x(n-1).yn - xn.y(n-1) + xn.y0 - x0.yn)
    """
    x0, y0 = points[0]
    xn, yn = points[-1]

    area = sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in pairwise(points))

    # add last term
    area += xn * y0 - x0 * yn

    area = abs(area) // 2
    return area


def iter_take(iterable, n: int) -> list:
    # return list of n-items from iterable or until iterable exhausted
    return list(islice(iterable, n))


def iter_ncycles(iterable, n: int):
    return chain.from_iterable(repeat(iterable, n))


def list_flatten(iterable):
    return chain.from_iterable(iterable)


def list_transpose(src: list) -> list:
    # length of every list should be the same
    assert all(len(a) == len(src[0]) for a in src)
    return map_list(list, zip(*src))


def list_copy(src: list) -> list:
    # every other method of copy does not actually copy the list
    return deepcopy(src)


def list_remove_value(val, src: list) -> list:
    return list(filter(lambda x: x != val, src))


def list_remove_index(idx: int, src: list) -> list:
    return src[:idx] + src[idx + 1 :]


def bfs(graph, start):
    """
    BFS for shortest-path problem.
    """
    queue = [start]
    visited = set()

    while queue:
        vertex = queue.pop(0)

        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)

    return visited


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]

    while queue:
        (vertex, path) = queue.pop(0)

        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)

    return visited


def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])


# ------------------------------------------------------------------------------
