# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from randomboards import training_boards
from randomscores import training_scores

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

class_names = ['X', 'draw', 'O']

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(9)),
    keras.layers.Dense(18, activation=tf.nn.relu),
    keras.layers.Dense(3, activation=tf.nn.softmax)
])

model.compile(optimizer=tf.train.AdamOptimizer(), 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_boards, training_scores, epochs=5)

#test_loss, test_acc = model.evaluate(test_images, test_labels)

#print('Test accuracy:', test_acc)

#predictions = model.predict(test_images)
#print(predictions[0])