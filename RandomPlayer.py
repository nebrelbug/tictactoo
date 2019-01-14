import random

def Random(game):
    if len(game.open_positions()) == 0:
        print("OHNONONONO")
    return random.choice(game.open_positions())