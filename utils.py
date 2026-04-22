# utils.py

import numpy as np
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
# PREDICT (SAFE VERSION)
# ================================
def predict(model, image):
    import random

    # If model is None (cloud case)
    if model is None:
        score = random.random()
        print("Demo Prediction:", score)
        return score

    # If real model exists (local case)
    prediction = model.predict(image)[0][0]
    return prediction
