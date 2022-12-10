from util import chunked

RUNNER_DISABLE_RESULT_HIGHLIGHT = True

CYCLE_COSTS = {
    "noop": 1,
    "addx": 2,
}

P1_INTERESTING_CYCLES = {20: True, 60: True, 100: True, 140: True, 180: True, 220: True}


def parse_input(raw_input: list[str]):
    return [line.rstrip().split() for line in raw_input]


def resolve(_input):
    register_x = 1
    current_cycle = 0

    p1 = 0
    # prepare p2 display beforehand - 240 symbols
    p2_display = ["."] * 240

    for command_line in _input:
        command = command_line[0]

        cycle_cost = CYCLE_COSTS[command]

        for i in range(cycle_cost):
            # if current cycle overlaps sprite (centered at register X value) - draw `#`
            if register_x + 1 >= current_cycle % 40 >= register_x - 1:
                p2_display[current_cycle] = "#"

            current_cycle += 1

            if P1_INTERESTING_CYCLES.get(current_cycle, None):
                p1 += (current_cycle * register_x)

        if command == "noop":
            continue

        register_x += int(command_line[1])

    # starting \n is for runner output - to start ascii art from new line properly
    # split combined string of display into sub-strings of 40 length, and rejoin them with new lines
    p2 = "\n" + "\n".join(chunked("".join(p2_display), 40))

    return p1, p2
