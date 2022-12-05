from copy import deepcopy
from re import split, compile
from util import chunked

from itertools import zip_longest

command_splitter = compile(f" from | to ")


def parse_input(raw_input: list[str]):
    blocks_complete = {}
    blocks_intermediate = []
    commands = []

    parsing_commands = False

    for line in raw_input:
        if line == "\n":
            # turn block lines into columns, last element of each is column number
            # rest is reversed and filtered for easier placement access later
            stacks = zip_longest(*blocks_intermediate, fillvalue=' ')
            for stack in stacks:
                blocks_complete[int(stack[-1])] = list(filter(lambda s: s != ' ', reversed(stack[:-1])))
            parsing_commands = True
            continue

        stripped = line.rstrip()

        if parsing_commands:
            # parse command line into tuple of (count, from, to)
            commands.append(tuple(map(int, split(command_splitter, stripped[5:]))))
        else:
            # store blocks per-line, taking chunks of 4 ([N] plus space) and extracting N from it
            # works as well to extract stack number
            blocks_intermediate.append([block[1] for block in chunked(stripped, 4)])
    return blocks_complete, commands


def resolve(_input: tuple[dict[int, list[str]], list[tuple[int]]]) -> (int, int):
    stacks_p1, commands = _input

    stacks_p2 = deepcopy(stacks_p1)

    for count, _from, to in commands:
        # p1 moves 1 by 1 - reversing order for multiple blocks
        # p2 takes as-is
        blocks_p1 = reversed(stacks_p1[_from][-count:])
        blocks_p2 = stacks_p2[_from][-count:]

        stacks_p1[to].extend(blocks_p1)
        stacks_p1[_from] = stacks_p1[_from][:-count]

        stacks_p2[to].extend(blocks_p2)
        stacks_p2[_from] = stacks_p2[_from][:-count]

    p1 = "".join(row[-1] for row in stacks_p1.values())
    p2 = "".join(row[-1] for row in stacks_p2.values())

    return p1, p2


"""
---------------- DAY #5 ----------------
  Part 1: JDTMRWCQJ
  Part 2: VHJDDCWRD

Timings (10000 runs), ms:
  Total Parse: 6474.74840
  Total Resolve: 3214.25530
  Total Complete: 9689.00370
  Min: 0.92080
  Max: 1.71590
  Avg: 0.96890
    [Parse]   0.64747
    [Resolve] 0.32143
"""
