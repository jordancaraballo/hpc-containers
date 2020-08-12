#--------------------------------------------------------------
# Simple test to verify packages compatibility and calling
# libraries. Simple NN to load.
# Author: Jordan A Caraballo-Vega
#--------------------------------------------------------------
# Loading libraries
import tensorflow as tf
from tensorflow import keras
import sunpy as sp
import dask_image as di
import astropy as asp
import jax
import aiapy as aip
import pyflux as pf
import pyspedas as ps
import dask
import numpy as np

print("Libraries have been loaded")

# Tensorflow list CPU and GPU devices
physical_devices = tf.config.list_physical_devices()
print("Devices: ", physical_devices)

# ------------ Build simple example with fashion_mnist ---------

# Download the data
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Normalization
train_images = train_images / 255.0
test_images = test_images / 255.0

# Build small model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10)
])

# Tensorflow distributed strategy
mirrored_strategy = tf.distribute.MirroredStrategy() # using distributed parallelization
with mirrored_strategy.scope():
    
    # Build small model
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(10)
    ])

    # Compile model
    model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\nTest accuracy:', test_acc)

