FIGURES = {
    "A": 1,  # rock,
    "B": 2,  # paper,
    "C": 3,  # scissors,
    "X": 1,  # rock,
    "Y": 2,  # paper,
    "Z": 3,  # scissors,
}

P2_OUTCOMES = {
    1: 0,
    2: 3,
    3: 6,
}


def parse_input(raw_input: list[str]):
    return [
        [FIGURES[letter] for letter in line.strip().split(" ")]
        for line in raw_input
    ]


def get_winner(a, b):
    if a == b:
        return 3

    # rock wins scissors
    elif abs(a - b) == 2:
        return 0 if a == 1 else 6

    # scissors win paper, paper wins rock
    if b > a:
        return 6

    return 0


def get_figure_cost_for_outcome(a, b):
    expected_outcome = P2_OUTCOMES[b]

    # draw - return same cost as A
    if expected_outcome == 3:
        return expected_outcome + a

    winning_figure_cost = a + 1
    losing_figure_cost = a - 1

    # if we have to lose, return losing figure, underflowing into scissors
    if expected_outcome == 0:
        return expected_outcome + (losing_figure_cost if losing_figure_cost > 0 else 3)

    # if we have to win, return winning figure, overflowing into rock
    if expected_outcome == 6:
        return expected_outcome + (winning_figure_cost if winning_figure_cost <= 3 else 1)

    print("FAILED TO FIND OUTCOME: ", a, b, expected_outcome)


def resolve(_input: list[list[str]]):
    p1 = sum([b + get_winner(a, b) for a, b in _input])
    p2 = sum([get_figure_cost_for_outcome(a, b) for a, b in _input])

    return p1, p2


"""
12679


A X
A Y
A Z
B X
B Y
B Z
C X
C Y
C Z
"""