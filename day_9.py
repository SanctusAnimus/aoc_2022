from pprint import pprint
from collections import deque

from util import quick_hash, sign

KNOT_COUNT = 10


DIRECTIONS = {
    "D": (0, -1),
    "U": (0, 1),
    "L": (-1, 0),
    "R": (1, 0),
}


def parse_input(raw_input: list[str]):
    return [[line[0], int(line.rstrip()[2:])] for line in raw_input]


def resolve(_input: tuple[tuple[str, int]]):
    knot_x = [0 for _ in range(KNOT_COUNT)]
    knot_y = [0 for _ in range(KNOT_COUNT)]

    p1_visited = deque()
    p2_visited = deque()

    for direction, step_count in _input:
        head_dx, head_dy = DIRECTIONS[direction]
        for i in range(step_count):
            knot_x[0] += head_dx
            knot_y[0] += head_dy

            for knot_index in range(1, KNOT_COUNT):
                delta_x = knot_x[knot_index - 1] - knot_x[knot_index]
                delta_y = knot_y[knot_index - 1] - knot_y[knot_index]

                if delta_x > 1 or delta_x < -1 or delta_y > 1 or delta_y < -1:
                    knot_x[knot_index] += sign(delta_x)
                    knot_y[knot_index] += sign(delta_y)

            p1_visited.append(quick_hash(knot_x[1], knot_y[1]))
            p2_visited.append(quick_hash(knot_x[KNOT_COUNT - 1], knot_y[KNOT_COUNT - 1]))

    return len(set(p1_visited)), len(set(p2_visited))


"""
---------------- DAY #9 ----------------
Solutions:
  Part 1: 6314
  Part 2: 2504

Timings (1000 runs), ms:
  Total Parse: 367.44620
  Total Resolve: 24232.17150
  Total Complete: 24599.61770
  Min: 22.47560
  Max: 32.74710
  Avg: 24.59962
    [Parse]   0.36745
    [Resolve] 24.23217
"""