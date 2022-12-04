def parse_input(raw_input: list[str]):
    return [
        [[int(val) for val in part.split("-")] for part in line.rstrip().split(",")]
        for line in raw_input
    ]


def resolve(_input):
    p1 = sum(
        (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1])
        or (pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1])
        for pair in _input
    )

    # pairs don't overlap only if end of first pair is less than start of second
    # or start of first pair higher than end of second
    # i.e.          or
    # 123...        ...456
    # ...456        123...
    p2 = sum(
        not ((pair[0][1] < pair[1][0]) or (pair[0][0] > pair[1][1]))
        for pair in _input
    )

    return p1, p2


"""
---------------- DAY #4 ----------------
Solutions:                              
  Part 1: 511                           
  Part 2: 821                           
                                        
Timings (10000 runs), ms:               
  Total Parse: 9454.31340               
  Total Resolve: 2416.78650             
  Total Complete: 11871.09990           
  Min: 1.07120                          
  Max: 3.47690                          
  Avg: 1.18711
"""
