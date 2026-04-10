import streamlit as st
from config import MODEL_PATH, IMAGE_SIZE
from model_loader import load_trained_model
from utils import preprocess_image, predict
from ui import load_css, navbar, hero, features, show_result

st.set_page_config(page_title="Rupee Vision", layout="wide")

# UI sections
load_css()
navbar()
hero()
features()

# Sidebar
st.sidebar.title("Rupee Vision")
st.sidebar.info("AI-based fake currency detection system.")

# Model
model = load_trained_model(MODEL_PATH)

# Upload section
st.markdown("### Upload Currency Image")
uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

if uploaded_file:
    col1, col2 = st.columns(2)

    image, display_img = preprocess_image(uploaded_file, IMAGE_SIZE)

    with col1:
        st.image(display_img, caption="Uploaded Image", use_column_width=True)

    with col2:
        score = predict(model, image)
        show_result(score)
