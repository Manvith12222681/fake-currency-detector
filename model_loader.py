# model_loader.py

from tensorflow.keras.models import load_model

def load_trained_model(path):
    try:
        model = load_model(path, compile=False)
        print(" Model loaded successfully")
        return model
    except Exception as e:
        print(" Error loading model:", e)
        return None
