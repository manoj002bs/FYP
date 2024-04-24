import tensorflow as tf

import cv2

import numpy as np

# Load your trained model

model = tf.keras.models.load_model(‘path/to/model’)

# Read image using OpenCV

image = cv2.imread(‘path/to/image.png’, 0)

# Preprocess the image (convert to the right shape for the model)

image = cv2.resize(image, (width, height))

image = np.expand_dims(image, axis=-1)

image = np.expand_dims(image, axis=0)

# Use the model to predict

prediction = model.predict(image)

# Post-process the prediction to get readable text

# This will depend on how you’ve trained your model

readable_text = post_process(prediction)

print(“Predicted text:”, readable_text)