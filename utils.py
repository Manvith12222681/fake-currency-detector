# ==========================================
# UTILITY FUNCTIONS
# ==========================================
import numpy as np
import cv2

def preprocess_image(file, size):
    file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    display_img = image.copy()

    image = cv2.resize(image, size)
    image = image.astype("float32") / 255.0
    image = np.expand_dims(image, axis=0)

    return image, display_img


def predict(model, image):
    # Dummy prediction (for deployment demo)
    import random
    return random.random()