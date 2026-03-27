# ==========================================
# MAIN APPLICATION
# ==========================================
import streamlit as st
from config import MODEL_PATH, IMAGE_SIZE
from model_loader import load_trained_model
from utils import preprocess_image, predict
from ui import load_css, header, show_result

# Page config
st.set_page_config(page_title="Currency Detection", layout="centered")

# Load custom CSS
load_css()

# Header UI
header()

# Load model
model = load_trained_model(MODEL_PATH)

# File uploader
uploaded_file = st.file_uploader("Upload Currency Image", type=["jpg", "jpeg", "png"])

# Main logic
if uploaded_file:
    image, display_img = preprocess_image(uploaded_file, IMAGE_SIZE)

    st.image(display_img, caption="Uploaded Image", use_column_width=True)

    score = predict(model, image)

    show_result(score)