import random
from tensorflow import keras
import numpy as np

# import os
# checkpoint_path = "training_1/cp.ckpt"
# checkpoint_dir = os.path.dirname(checkpoint_path)
model = keras.models.load_model(
    'savedmodel',
    custom_objects=None,
    compile=True
)

class Player:
    def __init__(self, XO): ## Player always sees itself as X. So if it's O, we multiply the board by -1
        self.piece = XO
    
    def play(self, game, piece):
        self.piece = piece
        #if self.piece == 'o':
        open = game.open_positions()
        next_positions = np.zeros((9, 9), dtype=np.int)

        for i in range(0,len(open)):
            print('open[i]: ' + str(open[i]))
            next_positions[i] = game.return_move(piece, open[i])
            
        next_positions = next_positions[~np.all(next_positions == 0, axis=1)]
        #print('next positions: ' + next_positions)
        predictions = model.predict(next_positions)
        #print("predictions: " + predictions[0])
        move_to_return = open[0] # default move
        print("default move_to_return: " + str(move_to_return))
        move_prob = 0
        move_prediction = 2
        if piece == 'o':
            print('')
        elif piece == 'x':
            for index, prediction in enumerate(predictions):
                if np.argmax(prediction) <= move_prediction and prediction[np.argmax(prediction)] > move_prob: # if winner is better than the last moves 
                                                                                           # winner and prob > last prob
                    move_to_return = index
                    move_prob = prediction[0]
                    move_prediction = np.argmax(prediction)
        print('move_to_return: ' + str(move_to_return))
        print('move\'s type: ' + type(move_to_return).__name__)
        return move_to_return

    
    def play_random(self, game):
        #print("game.board before play: " + ''.join(str(e) for e in game.board))
        #print("open positions:" + ''.join(str(e) for e in game.open_positions()))
        if len(game.open_positions()) == 0:
            print("OHNONONONO")
        return random.choice(game.open_positions())