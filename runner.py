from importlib import import_module
from argparse import ArgumentParser
from time import perf_counter


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

    print(f"""
---------------- DAY #{args.day} ----------------
Solutions:
\tPart 1: {p1}
\tPart 2: {p2}

Timings ({args.run_count} runs):
\tTotal Parse: {parse_total_time * 1000:.05f}ms
\tTotal Resolve: {resolve_total_time * 1000:.05f}ms
\tTotal Complete: {parse_total_time + resolve_total_time * 1000:.05f}ms
\tMin: {min_time * 1000:.05f}ms
\tMax: {max_time * 1000:.05f}ms
\tAvg: {(parse_total_time + resolve_total_time) / args.run_count * 1000:.05f}ms
    """)


main()
