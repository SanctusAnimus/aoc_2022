from collections import defaultdict, deque

from util import get_nested


def parse_input(raw_input: list[str]) -> dict:
    """
    Build nested directory structure
    :param raw_input: puzzle input
    :return:
    """
    structure = defaultdict(dict)
    structure["/"] = {}
    # maintain current dir as a deque of all directories we're in
    # i.e. [a, b, c] means we're in structure[a][b][c]
    current_dir = deque()

    for line in raw_input:
        stripped = line.rstrip()
        # reading command
        if stripped[0] == "$":
            command = stripped[2:4]

            if command == "cd":
                new_dir = stripped[5:]

                if new_dir == "..":
                    current_dir.pop()
                else:
                    current_dir.append(new_dir)

                # ls command doesn't matter - since anything that is not a command is an output of it
                # and can be attributed to current directory

            continue

        size_or_type, name = line.split()

        current = get_nested(structure, current_dir)

        current[name] = {} if size_or_type == "dir" else int(size_or_type)

    return structure


def get_size(content: dict, sizes_container: dict, parent_keys: list) -> (dict, int):
    """
    Recursively build sizes dictionary
    :return:
    """
    current_size = 0
    for name, value in content.items():
        if type(value) == int:
            current_size += value
        else:
            # maintain current parent keys as there can be multiple folders
            # and this is somehow faster than deque append/pop combo
            updated_keys = parent_keys + [name]
            _, child_size = get_size(value, sizes_container, updated_keys)
            sizes_container["/".join(updated_keys)] = child_size
            current_size += child_size

    return sizes_container, current_size


def resolve(_input: dict):
    sizes, total_size = get_size(_input, {}, [])

    p1 = sum(v for v in sizes.values() if v <= 100_000)

    expected_free_space = 30_000_000
    current_free_space = 70_000_000 - sizes["/"]

    space_to_free = expected_free_space - current_free_space

    # sort sizes and find first big enough to free enough spaces
    # dir/file names are irrelevant to the puzzle
    sorted_sizes = sorted(sizes.values())
    p2 = next(filter(lambda size: size >= space_to_free, sorted_sizes), -1)

    return p1, p2


"""
---------------- DAY #7 ----------------
Solutions:
  Part 1: 1432936
  Part 2: 272298

Timings (10000 runs), ms:
  Total Parse: 3444.80380
  Total Resolve: 995.36280
  Total Complete: 4440.16660
  Min: 0.42320
  Max: 0.97700
  Avg: 0.44402
    [Parse]   0.34448
    [Resolve] 0.09954
"""