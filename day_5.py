from copy import deepcopy
from re import split, compile

from itertools import zip_longest

command_splitter = compile(f" from | to ")


def parse_input(raw_input: list[str]):
    blocks_complete = {}
    blocks_intermediate = []
    commands = []

    parsing_commands = False

    for line in raw_input:
        if line == "\n":
            # blocks definition ended - switch to parsing commands, and turn partial blocks definition into final
            # turn block lines into columns, last element of each is column number
            # rest is reversed and filtered for easier placement access later
            stacks = zip_longest(*reversed(blocks_intermediate), fillvalue=' ')
            for stack in stacks:
                blocks_complete[int(stack[0])] = list(block for block in stack[1:] if block != " ")
            parsing_commands = True
            continue

        stripped = line.rstrip()

        if parsing_commands:
            # remove known "move " from the start of the string
            # and parse command line into tuple of (count, from, to)
            commands.append(tuple(map(int, split(command_splitter, stripped[5:]))))
        else:
            # starting from second char, take every 4th
            # takes every block's letter or stack number
            blocks_intermediate.append(stripped[1::4])
    return blocks_complete, commands


def resolve(_input: tuple[dict[int, list[str]], list[tuple[int]]]) -> (int, int):
    stacks_p1, commands = _input

    stacks_p2 = deepcopy(stacks_p1)
    # stacks are ordered from bottom to top - the highest element is at the end of each stack list
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
Solutions:                              
  Part 1: JDTMRWCQJ                     
  Part 2: VHJDDCWRD                     
                                        
Timings (10000 runs), ms:               
  Total Parse: 6367.40550               
  Total Resolve: 3144.48880             
  Total Complete: 9511.89430            
  Min: 0.90350                          
  Max: 1.69030                          
  Avg: 0.95119                          
    [Parse]   0.63674                   
    [Resolve] 0.31445 
"""
