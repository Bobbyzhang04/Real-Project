import keras
import cv2


our_model = keras.applications.VGG16(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=1000,
    classifier_activation="softmax",
)

list_of_images = []

image = cv2.imread('/Users/snoopbob/Downloads/dog.jpg',
                   cv2.IMREAD_UNCHANGED)
image = cv2.resize(image, (224, 224))

list_of_images.append(image)

#array_of_images = numpy.array(list_of_images)
#print(array_of_images.shape)

results = our_model.predict(list_of_images)

print(results)


