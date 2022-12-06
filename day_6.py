def parse_input(raw_input: list[str]):
    return raw_input[0]


def resolve(_input: str):
    p1 = 0
    p2 = 0

    for index in range(len(_input)):
        if len(set(_input[index:index + 4])) == 4 and p1 == 0:
            p1 = index + 4
        if len(set(_input[index:index + 14])) == 14 and p2 == 0:
            p2 = index + 14

        if p1 != 0 and p2 != 0:
            break

    return p1, p2


"""
---------------- DAY #6 ----------------
Solutions:
  Part 1: 1287
  Part 2: 3716

Timings (10000 runs), ms:
  Total Parse: 1.34040
  Total Resolve: 22241.51960
  Total Complete: 22242.86000
  Min: 2.11290
  Max: 3.55860
  Avg: 2.22429 
    [Parse]   0.00013
    [Resolve] 2.22415

"""