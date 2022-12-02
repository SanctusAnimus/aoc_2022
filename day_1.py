def parse_input(raw_input: list[str]) -> list[int]:
    elfs = []
    current_value = 0
    for line in raw_input:
        if line == "\n":
            elfs.append(current_value)
            current_value = 0
            continue
        current_value += int(line.rstrip())

    return elfs


def resolve(_input: list[int]) -> (int, int):
    return max(*_input), sum(sorted(_input)[-3:])
