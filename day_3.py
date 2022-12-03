from string import ascii_lowercase, ascii_uppercase

from util import chunked

ITEM_TYPES = ascii_lowercase + ascii_uppercase
ITEM_TYPE_COST = {letter: index for index, letter in enumerate(ITEM_TYPES, start=1)}


def parse_input(raw_input: list[str]) -> list[str]:
    return [line.rstrip() for line in raw_input]


def resolve(_input: list[str]) -> (int, int):
    p1 = sum(
        ITEM_TYPE_COST[
            set(rucksack[:len(rucksack) // 2]).intersection(set(rucksack[len(rucksack) // 2:])).pop()
        ]
        for rucksack in _input
    )

    p2 = sum(
        ITEM_TYPE_COST[set(rucksacks[0]).intersection(set(rucksacks[1])).intersection(set(rucksacks[2])).pop()]
        for rucksacks in chunked(_input, 3)
    )

    return p1, p2


"""
---------------- DAY #3 ----------------
Solutions:
  Part 1: 8072
  Part 2: 2567

Timings (10000 runs), ms:
  Total Parse: 125.21360
  Total Resolve: 6116.53910
  Total Complete: 6241.75270
  Min: 0.60290
  Max: 0.87270
  Avg: 0.62418
"""
