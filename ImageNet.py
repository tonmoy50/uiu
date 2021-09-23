
import keras,os
from keras.preprocessing import image
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Conv2D, MaxPool2D, Dense, Flatten, Dropout, BatchNormalization
from keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from keras.utils import np_utils

#importing data
from keras.datasets import cifar10



(X_train, y_train), (X_test, y_test) = cifar10.load_data()

X_train = X_train.astype('float32')
y_train = y_train.astype('float32')

X_train = X_train/255.0
y_train = y_train/255.0


# one hot encode outputs
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
class_num = y_test.shape[1]

print(class_num)

input_shape=X_train.shape[1:]
print(input_shape)

#vgg16_19 model of Convolutional network
model = Sequential()

layer1 = 10
layer2 = 20
layer3 = 30
layer4 = 40
layer5 = 40

model.add( Conv2D( input_shape=X_train.shape[1:], filters=layer1, kernel_size=(3,3), padding="same", activation="relu" ) )
#model.add( Dropout(0.2) )
model.add( Conv2D( filters=layer1, kernel_size=(3,3), padding="same", activation="relu" ) )

model.add( MaxPool2D( strides=(2,2), pool_size=(2,2) ) )

model.add( Conv2D( filters=layer2, kernel_size=(3,3), padding="same", activation="relu" ) )
#model.add( Dropout(0.2) )
model.add( Conv2D( filters=layer2, kernel_size=(3,3), padding="same", activation="relu" ) )

model.add( MaxPool2D( strides=(2,2), pool_size=(2,2) ) )

model.add( Conv2D( filters=layer3, kernel_size=(3,3), padding="same", activation="relu" ) )
#model.add( Dropout(0.2) )
model.add( Conv2D( filters=layer3, kernel_size=(3,3), padding="same", activation="relu" ) )
#model.add( Dropout(0.2) )
model.add( Conv2D( filters=layer3, kernel_size=(3,3), padding="same", activation="relu" ) )
#model.add( Dropout(0.2) )
model.add( Conv2D( filters=layer3, kernel_size=(3,3), padding="same", activation="relu" ) )

model.add( MaxPool2D( strides=(2,2), pool_size=(2,2) ) )

model.add( Conv2D( filters=layer4, kernel_size=(3,3), padding="same", activation="relu" ) )
#model.add( Dropout(0.2) )
model.add( Conv2D( filters=layer4, kernel_size=(3,3), padding="same", activation="relu" ) )
#model.add( Dropout(0.2) )
model.add( Conv2D( filters=layer4, kernel_size=(3,3), padding="same", activation="relu" ) )
#model.add( Dropout(0.2) )
model.add( Conv2D( filters=layer4, kernel_size=(3,3), padding="same", activation="relu" ) )

model.add( MaxPool2D( strides=(2,2), pool_size=(2,2) ) )

model.add( Conv2D( filters=layer5, kernel_size=(3,3), padding="same", activation="relu" ) )
#model.add( Dropout(0.2) )
model.add( Conv2D( filters=layer5, kernel_size=(3,3), padding="same", activation="relu" ) )
#model.add( Dropout(0.2) )
model.add( Conv2D( filters=layer5, kernel_size=(3,3), padding="same", activation="relu" ) )
#model.add( Dropout(0.2) )
model.add( Conv2D( filters=layer5, kernel_size=(3,3), padding="same", activation="relu" ) )

model.add( MaxPool2D( strides=(2,2), pool_size=(2,2) ) )
model.add( BatchNormalization() )

model.add(Flatten())

model.add( Dense(200, activation="relu") )
#model.add( Dropout(0.2) )
model.add( Dense(200, activation="relu") )

model.add(Dense(100, activation="relu"))

model.add( Dense(class_num, activation="softmax") )

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
#model.compile(optimizer="adam", loss=keras.losses.categorical_crossentropy, metrics=['accuracy'])



seed = 21
#model.fit_generator(steps_per_epoch=100, generator=train_data, validation_data=test_data, validation_steps=10, epochs=10 )
np.random.seed(seed)
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=64)


scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))
