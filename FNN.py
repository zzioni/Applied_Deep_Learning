from keras import models
from keras import layers
from tensorflow.keras.utils import to_categorical
import tensorflow
from keras.optimizers import RMSprop 
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
    image_list.append(img)
    if 'cheetah' in name:
        label_list.append(0)
    elif 'leopard' in name:
        label_list.append(1)
    elif 'jaguar' in name:
        label_list.append(2)

images = np.array(image_list)
labels = np.array(label_list)

images = images.reshape((-1, 255 * 255 *3))
images = images.astype('float32') / 255

labels = to_categorical(labels)
#images = images.reshape(-1, 255*255*3)

train_images = images[:9545]
train_labels = labels[:9545]
test_images = images[9545:]
test_labels = labels[9545:]

model1 = models.Sequential()
model1.add(layers.Dense(512, activation='relu', input_shape=(255* 255*3,)))
model1.add(layers.Dense(256, activation='relu'))
model1.add(layers.Dense(128, activation='relu'))
model1.add(layers.Dense(64, activation='relu'))
model1.add(layers.Dropout(0.5))
model1.add(layers.Dense(2, activation='softmax'))

sgd = tensorflow.keras.optimizers.SGD(learning_rate=0.000095,  momentum=0.9)

model1.compile(optimizer=sgd,
                        loss='categorical_crossentropy',
                                        metrics=['accuracy'])

history = model1.fit(train_images, train_labels, epochs=10, batch_size=64, validation_split=0.1)

plt.plot(history.history['loss'], label='train loss')
plt.plot(history.history['val_loss'], label='val loss')
plt.legend()
plt.savefig('FNN_loss.jpg')

plt.clf()
plt.plot(history.history['accuracy'], label='train acc')
plt.plot(history.history['val_accuracy'], label='val acc')
plt.legend()
plt.savefig('FNN_acc.jpg')
