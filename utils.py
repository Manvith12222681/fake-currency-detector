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
# PREDICT (DUMMY VERSION)
# ================================
def predict(model, image):
    import random
    score = random.random()
    print("Prediction Score:", score)
    return score
