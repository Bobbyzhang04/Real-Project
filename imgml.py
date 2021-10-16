import keras
import cv2
import numpy
import math

our_model = keras.applications.VGG16(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=(224, 224, 3),
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
)


images = ['/Users/snoopbob/Downloads/dog.jpeg']


class MySequence(keras.utils.Sequence):

    def __init__(self, x_set, y_set, batch_size=1):
        self.x, self.y = x_set, y_set
        self.batch_size = batch_size

    def __len__(self):
        return math.ceil(len(self.x) / self.batch_size)

    def __getitem__(self, idx):
        batch_x = self.x[idx * self.batch_size:(idx + 1) * self.batch_size]
        batch_y = self.y[idx * self.batch_size:(idx + 1) * self.batch_size]
        return numpy.array([cv2.resize(cv2.imread(file_name), (224, 224)) for file_name in batch_x]), numpy.array(batch_y)


results = our_model.predict(MySequence(images, ['dog']))