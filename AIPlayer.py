import random
from tensorflow import keras
import tensorflow as tf
from randomboards import training_boards
from randomscores import training_scores
import numpy as np

model = keras.Sequential([
    keras.layers.Dense(24, activation=tf.nn.relu),
    keras.layers.Dense(168, activation=tf.nn.relu),
    #keras.layers.Dense(8, activation=tf.nn.relu),
    #keras.layers.SimpleRNN(units=2),
    keras.layers.Dense(91, activation=tf.nn.relu),

    #keras.layers.Dense(64, activation=tf.nn.relu),
    keras.layers.Dense(3, activation=tf.nn.softmax)
])


model.compile(optimizer=keras.optimizers.Adam(lr=0.001), 
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])

model.fit(training_boards, training_scores, epochs=0)  # pass callback to training)

model.load_weights('my_model.h5')

class Player:
    def __init__(self, XO): ## Player always sees itself as X. So if it's O, we multiply the board by -1
        self.piece = XO
    
    def play(self, game, piece):
        self.piece = piece
        #if self.piece == 'o':
        open = game.open_positions()
        next_positions = np.zeros((9, 9), dtype=np.int)

        for i in range(0,len(open)):
            # print('open[i]: ' + str(open[i]))
            next_positions[i] = game.return_move(piece, open[i])
            
        next_positions = next_positions[~np.all(next_positions == 0, axis=1)]
        #print('next positions: ' + next_positions)
        predictions = model.predict(next_positions)
        #print("predictions: " + predictions[0])
        move_to_return = open[0] # default move
        # print("default move_to_return: " + str(move_to_return))
        move_prob = 0
        move_prediction = 2
        if piece == 'o':
            print('')
        elif piece == 'x':
            for index, prediction in enumerate(predictions):
                if prediction[0] > move_prob:
                    move_to_return = open[index] # Index is the prediction index, which corresponds to move in next_positions
                    move_prob = prediction[0]
                    move_prediction = np.argmax(prediction)
        print('move_to_return: ' + str(move_to_return))
        # print('move\'s type: ' + type(move_to_return).__name__)
        return move_to_return

    
    def play_random(self, game):
        #print("game.board before play: " + ''.join(str(e) for e in game.board))
        #print("open positions:" + ''.join(str(e) for e in game.open_positions()))
        if len(game.open_positions()) == 0:
            print("OHNONONONO")
        return random.choice(game.open_positions())