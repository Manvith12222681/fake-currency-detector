# ==========================================
# MODEL LOADER
# ==========================================
from tensorflow.keras.models import load_model
import streamlit as st

@st.cache_resource
def load_trained_model(path: str):
    # compile=False avoids Keras version issues
    return load_model(path, compile=False)