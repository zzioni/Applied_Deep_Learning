from keras import models
from keras import layers
from tensorflow.keras.utils import to_categorical
import tensorflow
import numpy as np
import matplotlib.pyplot as plt

import os
from PIL import Image
import cv2
import random

targetDir = './data'
files = os.listdir(targetDir)
random.shuffle(files)
random.shuffle(files)
random.shuffle(files)

image_list = []
label_list = []


for name in files:
    image_dir = './data/' + name
    img = cv2.imread(image_dir)
    image_list.append(img.astype('float32')/255)
    if 'cheetah' in name:
        label_list.append(0)
    elif 'leopard' in name:
        label_list.append(1)
    elif 'jaguar' in name:
        label_list.append(2)

images = np.array(image_list)
labels = np.array(label_list)
labels = to_categorical(labels)

train_images = images[:9545]
train_labels = labels[:9545]
test_images = images[9545:]
test_labels = labels[9545:]

conv_model = models.Sequential()
conv_model.add(layers.Conv2D(32, (3, 3), activation='relu', padding='valid' , input_shape=(255, 255, 3)))
conv_model.add(layers.MaxPooling2D((2, 2)))
conv_model.add(layers.Conv2D(64, (3, 3),  padding='valid', activation='relu')) 
conv_model.add(layers.MaxPooling2D((2, 2)))
conv_model.add(layers.Conv2D(64, (3, 3), activation='relu'))
conv_model.add(layers.Flatten())
conv_model.add(layers.Dense(64, activation='relu'))
conv_model.add(layers.Dropout(0.5))
conv_model.add(layers.Dense(2, activation='softmax'))


sgd = tensorflow.keras.optimizers.SGD(learning_rate=0.2,  momentum=0.9)

conv_model.compile(optimizer='rmsprop',
                      loss='categorical_crossentropy',
                                    metrics=['accuracy'])
history = conv_model.fit(train_images, train_labels, epochs=10, batch_size=64, validation_split=0.1)

plt.plot(history.history['loss'], label='train loss')
plt.plot(history.history['val_loss'], label='val loss')
plt.legend()
plt.savefig('2D_loss.jpg')

plt.clf()
plt.plot(history.history['accuracy'], label='train acc')
plt.plot(history.history['val_accuracy'], label='val acc')
plt.legend()
plt.savefig('2D_acc.jpg')

