Rock = 1
Paper = 2
Scissors = 3

Lose = 0
Draw = 3
Win = 6

Lose_encoded = 1
Draw_encoded = 2
Win_encoded = 3

FIGURES = {
    "A": Rock,
    "B": Paper,
    "C": Scissors,
    "X": Rock,
    "Y": Paper,
    "Z": Scissors,
}

P1_OUTCOMES = {
    Rock: {
        Rock: Rock + Draw,
        Paper: Paper + Win,
        Scissors: Scissors + Lose,
    },
    Paper: {
        Rock: Rock + Lose,
        Paper: Paper + Draw,
        Scissors: Scissors + Win,
    },
    Scissors: {
        Rock: Rock + Win,
        Paper: Paper + Lose,
        Scissors: Scissors + Draw,
    },
}

P2_OUTCOMES = {
    Lose_encoded: {
        Rock: Lose + Scissors,
        Paper: Lose + Rock,
        Scissors: Lose + Paper,
    },
    Draw_encoded: {
        Rock: Draw + Rock,
        Paper: Draw + Paper,
        Scissors: Draw + Scissors,
    },
    Win_encoded: {
        Rock: Win + Paper,
        Paper: Win + Scissors,
        Scissors: Win + Rock,
    },
}


def parse_input(raw_input: list[str]):
    return [
        [FIGURES[letter] for letter in line.rstrip().split(" ")]
        for line in raw_input
    ]


def resolve(_input: list[list[str]]):
    p1 = sum(P1_OUTCOMES[a][b] for a, b in _input)
    p2 = sum(P2_OUTCOMES[b][a] for a, b in _input)

    return p1, p2


"""
Solutions:
        Part 1: 12679
        Part 2: 14470

Timings (10000 runs):
        Total Parse: 6903.25750ms
        Total Resolve: 2634.15610ms
        Total Complete: 9537.41360ms
        Min: 0.87040ms
        Max: 1.88490ms
        Avg: 0.95374ms
"""
