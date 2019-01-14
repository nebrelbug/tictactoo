# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from randomboards import training_boards
from randomscores import training_scores
import os
checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

class_names = ['X', 'draw', 'O']

# Returns a short sequential model
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


# Create checkpoint callback
#cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path, save_weights_only=True, verbose=1, period=5)

model.fit(training_boards, training_scores, epochs=5)  # pass callback to training)
keras.models.save_model(
    model,
    'savedmodel',
)
#test_loss, test_acc = model.evaluate(test_images, test_labels)

#print('Test accuracy:', test_acc)

predictions = model.predict(np.array([[0,0,0,0,-1,0,0,0,0],[-1,-1,-1,0,1,1,0,0,0]]))
print(predictions[0])
print(predictions[1])