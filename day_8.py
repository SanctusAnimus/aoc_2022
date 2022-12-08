def parse_input(raw_input: list[str]):
    return [tuple(map(int, line.rstrip())) for line in raw_input]


def resolve(_input: list[tuple[int]]):
    width = len(_input[0])
    height = len(_input)

    p1 = width * 2 + (height - 2) * 2

    p2 = 0

    # direct brute-force implementation of grid scanning
    for l_i, line in enumerate(_input[1:-1], start=1):
        for i, value in enumerate(line[1:-1], start=1):
            # print(f"checking {value} at {i}:{l_i}")
            offset = 1

            left_obscured, right_obscured, top_obscured, bottom_obscured = False, False, False, False
            p1_tracking = [False, False, False, False]
            # view distance for p2
            p2_left, p2_right, p2_top, p2_bottom = 0, 0, 0, 0

            while True:
                if i - offset < 0 and not left_obscured:
                    left_obscured = True
                    if not any(p1_tracking):
                        p1 += 1
                        p1_tracking[0] = True
                    # print("\tvisible from left")
                    # breaks don't work for p2 unfortunately
                    # break

                if i + offset >= width and not right_obscured:
                    right_obscured = True
                    if not any(p1_tracking):
                        p1 += 1
                        p1_tracking[1] = True
                    # print("\tvisible from right")
                    # break

                if l_i - offset < 0 and not top_obscured:
                    top_obscured = True
                    if not any(p1_tracking):
                        p1 += 1
                        p1_tracking[2] = True
                    # print("\tvisible from top")
                    # break

                if l_i + offset >= height and not bottom_obscured:
                    bottom_obscured = True
                    if not any(p1_tracking):
                        p1 += 1
                        p1_tracking[3] = True
                    # print("\tvisible from bottom")
                    # break

                if not left_obscured:
                    # print(f"\tchecking left {_input[l_i][i - offset]}")
                    if _input[l_i][i - offset] >= value:
                        # print("\tobscured from left")
                        left_obscured = True
                    p2_left += 1
                if not right_obscured:
                    # print(f"\tchecking right {_input[l_i][i + offset]}")
                    if _input[l_i][i + offset] >= value:
                        # print("\tobscured from right")
                        right_obscured = True
                    p2_right += 1
                if not top_obscured:
                    # print(f"\tchecking top {_input[l_i - offset][i]}")
                    if _input[l_i - offset][i] >= value:
                        # print("\tobscured from top")
                        top_obscured = True
                    p2_top += 1
                if not bottom_obscured:
                    # print(f"\tchecking bottom {_input[l_i + offset][i]}")
                    if _input[l_i + offset][i] >= value:
                        # print("\tobscured from bottom")
                        bottom_obscured = True
                    p2_bottom += 1

                # tree is not visible from all sides
                if left_obscured and right_obscured and top_obscured and bottom_obscured:
                    break

                offset += 1
            # print(f"p2 {value} at {i}:{l_i}: {p2_left} {p2_right} {p2_top} { p2_bottom}")
            view_distance = p2_left * p2_right * p2_top * p2_bottom
            if view_distance > p2:
                p2 = view_distance

    return p1, p2


"""
---------------- DAY #8 ----------------
Solutions:
  Part 1: 1763
  Part 2: 671160

Timings (1 runs), ms:
  Total Parse: 0.55050
  Total Resolve: 8.70100
  Total Complete: 9.25150
  Min: 9.25150
  Max: 9.25150
  Avg: 9.25150
    [Parse]   0.55050
    [Resolve] 8.70100
"""
