# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from randomboards import training_boards
from randomscores import training_scores
from testboards import training_boards as testboards
from testscores import training_scores as testscores

training_boards = np.expand_dims(training_boards, axis=2)
print(training_boards.shape)
testboards = np.expand_dims(testboards, axis=2)
#training_scores = np.expand_dims(training_scores, axis=2)
print(training_scores.shape)
#testscores = np.expand_dims(testscores, axis=2)

# Helper libraries


print(tf.__version__)

class_names = ['X', 'draw', 'O']

# Returns a short sequential model
model = keras.Sequential()
model.add(keras.layers.Reshape((3,3,1), input_shape=(9,1)))
print(model.output_shape)
#model.add(keras.layers.Conv2D(filters=91, kernel_size=(2,2)))
model.add(keras.layers.Conv2D(filters=64, kernel_size=(2,2)))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(64, activation=tf.nn.relu))
model.add(keras.layers.Dense(91, activation=tf.nn.relu))
model.add(keras.layers.Dense(24, activation=tf.nn.relu))
model.add(keras.layers.Dense(168, activation=tf.nn.relu))
model.add(keras.layers.Dense(3, activation=tf.nn.softmax))

model.compile(optimizer=keras.optimizers.Adam(lr=0.001), 
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])

model.fit(training_boards, training_scores, epochs=15)  # pass callback to training)
model.save_weights('my_model.h5')
test_loss, test_acc = model.evaluate(testboards, testscores)

print('Test accuracy:', test_acc)

test_predictors = np.expand_dims(np.array([[0,0,0,0,-1,0,0,0,0],[-1,-1,-1,0,1,1,0,0,0], [1,1,1,0,0,-1,-1,-1,-1]]), axis=2)

predictions = model.predict(test_predictors)
print(predictions[0])
print(predictions[1])
print(predictions[2])