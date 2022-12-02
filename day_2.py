ROCK = 1
PAPER = 2
SCISSORS = 3

LOSE = 0
DRAW = 3
WIN = 6

LOSE_ENCODED = 1
DRAW_ENCODED = 2
WIN_ENCODED = 3

FIGURES = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}

P1_OUTCOMES = {
    ROCK: {
        ROCK: ROCK + DRAW,
        PAPER: PAPER + WIN,
        SCISSORS: SCISSORS + LOSE,
    },
    PAPER: {
        ROCK: ROCK + LOSE,
        PAPER: PAPER + DRAW,
        SCISSORS: SCISSORS + WIN,
    },
    SCISSORS: {
        ROCK: ROCK + WIN,
        PAPER: PAPER + LOSE,
        SCISSORS: SCISSORS + DRAW,
    },
}

P2_OUTCOMES = {
    LOSE_ENCODED: {
        ROCK: LOSE + SCISSORS,
        PAPER: LOSE + ROCK,
        SCISSORS: LOSE + PAPER,
    },
    DRAW_ENCODED: {
        ROCK: DRAW + ROCK,
        PAPER: DRAW + PAPER,
        SCISSORS: DRAW + SCISSORS,
    },
    WIN_ENCODED: {
        ROCK: WIN + PAPER,
        PAPER: WIN + SCISSORS,
        SCISSORS: WIN + ROCK,
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
