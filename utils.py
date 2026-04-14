# utils.py

import numpy as np
import cv2
from PIL import Image

# ================================
# PREPROCESS IMAGE
# ================================
def preprocess_image(uploaded_file, image_size):
    image = Image.open(uploaded_file).convert("RGB")
    display_img = image

    image = image.resize(image_size)
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    return image, display_img


# ================================
# PREDICT
# ================================
def predict(model, image):
    prediction = model.predict(image)

    score = float(prediction[0][0])

    print("Prediction Score:", score)  # 🔥 DEBUG

    return score
