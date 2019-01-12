import random
class Player:
    def __init__(self, XO): ## Player always sees itself as X. So if it's O, we multiply the board by -1
        self.piece = XO
    
    def play(self, board, model):
        #if self.piece == 'o':
        next_positions = []
        predictions = model.predict(next_positions)
    
    def play_random(self, game):
        #print("game.board before play: " + ''.join(str(e) for e in game.board))
        #print("open positions:" + ''.join(str(e) for e in game.open_positions()))
        if len(game.open_positions()) == 0:
            print("OHNONONONO")
        return random.choice(game.open_positions())