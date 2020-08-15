import os
from os import listdir
from os.path import isfile, join

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from tensorflow.keras.applications import imagenet_utils
from tensorflow.keras.models import load_model

fruit_model = load_model('models/fruit_v1.h5')
test_path = 'input'

test_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.mobilenet.preprocess_input).flow_from_directory(
    directory=test_path, target_size=(224,224), batch_size=1, shuffle=False)

test_labels = test_batches.classes

predictions = fruit_model.predict(x=test_batches, verbose=0)

rounded_predictions = []

for i in range(len(predictions)):
    rounded_predictions.append(np.argmax(predictions[i], axis=-1))

fruits = ['apple','banana','blackberry','blueberry','cherry','kiwi','orange','raspberry','strawberry','watermelon']

mypath = test_path + '/images'
test_images = [f for f in listdir(mypath) if isfile(join(mypath, f))]
test_images.sort()

for i in range(len(rounded_predictions)):
    print(f"'{test_images[i]}' is a {fruits[rounded_predictions[i]]}")