import numpy as np


def jenga():
    round = 1
    turn = 1
    stand_probability = 100

    game_intro()

    while stand_probability > 0:
        if turn % 2 == 1:
            round_info(round, stand_probability)
            stand_probability -= computer_turn(stand_probability)
        else:
            stand_probability -= player_turn()
            round += 1

        turn += 1

    if turn % 2 == 1:
        print("OH NO! Your move caused the tower to fall! YOU LOSE!")
    else:
        print("YAY! The computer knocked down the tower! YOU WON!")


def computer_turn(stand_probability):
    print("Computer's turn...")

    level = ""

    if stand_probability > 74:
        level = "H"
    elif stand_probability > 24:
        level = "M"
    else:
        level = "L"

    risk = risk_selection(level)
    print("This move was {percent} risky!\n".format(percent=risk / 10 * 100))

    return risk


def player_turn():
    risk = risk_selection(input("Your turn. Enter L, M, or H: "))
    print("This move was {percent} risky!\n".format(percent=risk / 10 * 100))
    return risk


def risk_selection(level):
    risk = 0

    if level == "L":
        risk = randomize_risk(0, 3)
    elif level == "M":
        risk = randomize_risk(4, 7)
    elif level == "H":
        risk = randomize_risk(8, 10)
    else:
        risk = randomize_risk(0, 10)

    return risk


def randomize_risk(l, h):
    return np.random.randint(low=l, high=h + 1)


def round_info(round, stand_probability):
    print(
        """
----------
ROUND {}: PROB OF TOWER STANDING: {}%
----------
""".format(
            round, stand_probability
        )
    )


def game_intro():
    print("\nLet's play JENGA")


jenga()
