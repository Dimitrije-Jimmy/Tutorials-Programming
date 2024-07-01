# Handwritten Digit Recognition with Tensorflow

# essential libraries
import cv2 as cv   # open cv2 library, for importing our own images into it
import numpy as np
import matplotlib.pyplot as plt
import os
# to build the Neural Netwrok, get the data, test it, apply it
import tensorflow as tf     # jesus christ tale import upocasni kodo za ful, namest 3 sekunde da loada, rab 11

# MNIST - dataset of around 60k samples of human handwritten digits
mnist = tf.keras.datasets.mnist

"""
This is a dataset of 60,000 28x28 grayscale images of the 10 digits, 
 along with a test set of 10,000 images. 
The 'fashion_mnist' dataset can be used as a drop-in replacement for MNIST.

"""
# example use:
(x_train, y_train), (x_test, y_test) = mnist.load_data()
assert x_train.shape == (60000, 28, 28)
assert x_test.shape == (10000, 28, 28)
assert y_train.shape == (60000,)
assert y_test.shape == (10000,)


# splitting it into train and test data
#(x_train, y_train), (x_test, y_test) = mnist.load_data()  # 10-20% test split idk


# next step is to normalise the data, easier for computing, 0-255 -> 0-1
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)
# we don't scale down the Y data (the Y data represents the output a.k.a 0-9)

# defining the model
# you can adjust it however you like, we're choosing an input layer, 
#  2 dense layers and an output layer
# you can also use convolutional neural networks but we're keeping it simple
model = tf.keras.models.Sequential()

# now we add layers, this is going to be a 'flat layer' - a 1D layer
"""
What we actually have is a 28x28 pixels and it's a grid, and we flatten the layer
 into 784 neurons
 we specify the input shape of the initial grid that we're trying to flatten
"""
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
# all the pixels of each individual image of a handwritten image and we feed that into the Input Layer


"""
now we add the dense/hidden layers, Dense just means that all the neurons are 
 connected to the previous layer and the next layer
you also pick how many units/neurons you want in you mode, the more neurons 
 the more complicated/sophisticated the layer becomes, the more nuances you can have 
and we specify the activation function, we're picking the simple RELU - Rectified Linear Unit
"""
model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
# we want two hidden layers that are the same

# in the end we have our output layer
"""
the 'softmax' funciton is the activation function, that takes the activation
 of all the output neurons (in this case for each digit from 0-9)
 and scales down all the values so that they add up to 1 (normalise) 
 so that we get the % probability of that number being the classification
""" 
model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))


# now we need to compile the layers and specify the optimizer, loss funciton
#  and metrics that we want to look at after
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# now we train/fit the model
# we can also specify the epochs - how many times is the model gonna see the data
#  / repeat the whole proccess of training
model.fit(x_train, y_train, epochs=3)


# evaluating the model
loss, accuracy = model.evaluate(x_test, y_test)
print(loss)         # 0.08919800072908401
print(accuracy)     # 0.972000002861023
# 97% accuracy


# we're saving the model so that we can use it to feed our own images into it
#  without having to train the model again
model.save('digits.model')

# to load the model again:
#model.tf.keras.load_model or something like that

# now we make digits in pain, resize the canvas to 28x28 px

script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)

# now we open them
for x in range(2, 10):
    img = cv.imread(f'{script_directory}\HandwrittenDigits\{x}_2.png')[:, :, 0] # get the first of the last one
    img = np.invert(np.array([img]))    # so that we get black on white

    prediction = model.predict(img)
    # the softmax result of all of the output, but we want only the output
    # index of the neuron is equal to the resulting digit
    print(np.argmax(prediction))   # index of highest value

    print(f'The result is probably: {np.argmax(prediction)}')

    plt.title(f'Image should be: {np.argmax(prediction)}')
    plt.imshow(img[0], cmap=plt.cm.binary)
    plt.show()