from importlib import import_module
from argparse import ArgumentParser
from time import perf_counter


class COLOR:
    HEADER = "\033[38;4;95;4;1m"
    SOLUTION = "\033[38;5;148;4;1m"
    OKGREEN = "\033[38;4;92;1m"
    ENDC = "\033[0m"
    TIME_PART = "\033[38;5;100;1m"
    TIME_COMPLETE = "\033[38;5;76;4;1m"


def main():
    parser = ArgumentParser()
    parser.add_argument("day", help="Which day to run", type=int, choices=range(1, 26))
    parser.add_argument("run_count", help="How many times to re-run for results aggregation", type=int)
    args = parser.parse_args()

    day_module = import_module(f"day_{args.day}")

    parse_total_time = 0
    resolve_total_time = 0

    min_time = 99999
    max_time = 0

    p1, p2 = None, None

    with open(f"inputs/day_{args.day}.txt") as src:
        raw_input = src.readlines()

    for _ in range(args.run_count):
        iter_start = perf_counter()
        _input = day_module.parse_input(raw_input)
        iter_parsed = perf_counter()
        p1, p2 = day_module.resolve(_input)
        iter_complete = perf_counter()

        time_taken_parsed = iter_parsed - iter_start
        parse_total_time += time_taken_parsed

        time_taken_resolve = iter_complete - iter_parsed
        resolve_total_time += time_taken_resolve

        time_taken_total = time_taken_resolve + time_taken_parsed

        if time_taken_total < min_time:
            min_time = time_taken_total
        if time_taken_total > max_time:
            max_time = time_taken_total

    print(f"""---------------- DAY {COLOR.HEADER}#{args.day}{COLOR.ENDC} ----------------
Solutions:
  Part 1: {COLOR.SOLUTION}{p1}{COLOR.ENDC}
  Part 2: {COLOR.SOLUTION}{p2}{COLOR.ENDC}

Timings ({COLOR.HEADER}{args.run_count}{COLOR.ENDC} runs), ms:
  Total Parse: {COLOR.TIME_PART}{parse_total_time * 1000:.05f}{COLOR.ENDC}
  Total Resolve: {COLOR.TIME_PART}{resolve_total_time * 1000:.05f}{COLOR.ENDC}
  Total Complete: {COLOR.TIME_COMPLETE}{(parse_total_time + resolve_total_time) * 1000:.05f}{COLOR.ENDC}
  Min: {COLOR.TIME_PART}{min_time * 1000:.05f}{COLOR.ENDC}
  Max: {COLOR.TIME_PART}{max_time * 1000:.05f}{COLOR.ENDC}
  Avg: {COLOR.TIME_COMPLETE}{(parse_total_time + resolve_total_time) / args.run_count * 1000:.05f}{COLOR.ENDC}
    """)


main()
