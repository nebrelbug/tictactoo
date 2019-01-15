from tensorflow import keras
import tensorflow as tf
from randomboards import training_boards
from randomscores import training_scores
import numpy as np

training_boards = np.expand_dims(training_boards, axis=2)
print(training_boards.shape)


model = keras.Sequential()
model.add(keras.layers.Reshape((3,3,1), input_shape=(9,1)))
#print(model.output_shape)
model.add(keras.layers.Conv2D(filters=91, kernel_size=(2,2)))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(24, activation=tf.nn.relu))
model.add(keras.layers.Dense(91, activation=tf.nn.relu))
model.add(keras.layers.Dense(168, activation=tf.nn.relu))
model.add(keras.layers.Dense(3, activation=tf.nn.softmax))

model.compile(optimizer=keras.optimizers.Adam(lr=0.001), 
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])


model.fit(training_boards, training_scores, epochs=0)  # pass callback to training)

model.load_weights('my_model.h5')

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
        move_prob = 0 # Initialize the prob of winning to 0
        if piece == 'o':
            for index, prediction in enumerate(predictions):
                if prediction[2] > move_prob:
                    move_to_return = open[index] # Index is the prediction index, which corresponds to move in next_positions
                    move_prob = prediction[2]
        elif piece == 'x':
            for index, prediction in enumerate(predictions):
                if prediction[0] > move_prob:
                    move_to_return = open[index] # Index is the prediction index, which corresponds to move in next_positions
                    move_prob = prediction[0]
        return move_to_return