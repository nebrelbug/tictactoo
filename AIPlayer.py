from tensorflow import keras
import tensorflow as tf
from randomboards import training_boards
from randomscores import training_scores
import numpy as np

training_boards = np.expand_dims(training_boards, axis=2)
print(training_boards.shape)

model = keras.models.load_model("my_model.h5")

class Player:
    
    def play(self, game, piece):
        open = game.open_positions()
        next_positions = np.zeros((9, 9), dtype=np.int) # Initialize the array

        for i in range(0,len(open)):
            next_positions[i] = game.return_move(piece, open[i]) # Add a possible next position
            
        next_positions = next_positions[~np.all(next_positions == 0, axis=1)] # Remove all empty next positions
        next_positions = np.expand_dims(next_positions, axis=2) # Give it a spacial dimension
        predictions = model.predict(next_positions) # Generate predictions for each possible position
        move_to_return = open[0] # default move
        move_prob = -1000 # Initialize the prob of winning to 0
        if piece == 'o':
            for index, prediction in enumerate(predictions):
                if prediction[2] - 1.1 * prediction[0] > move_prob:
                    move_to_return = open[index] # Index is the prediction index, which corresponds to move in next_positions
                    move_prob = prediction[2] - prediction[0]
        elif piece == 'x':
            for index, prediction in enumerate(predictions):
                if prediction[0] - 1.1 * prediction[2] > move_prob:
                    move_to_return = open[index] # Index is the prediction index, which corresponds to move in next_positions
                    move_prob = prediction[0] - prediction[2]
        return move_to_return