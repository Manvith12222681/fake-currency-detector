st.sidebar.title("About")
st.sidebar.info("This system detects fake currency using AI.")
import streamlit as st
from config import MODEL_PATH, IMAGE_SIZE
from model_loader import load_trained_model
from utils import preprocess_image, predict
from ui import load_css, header, show_result, info_section

# Page config
st.set_page_config(page_title="Currency Detector", layout="centered")

# Load UI
load_css()
header()

# Info section
info_section()

# Load model
model = load_trained_model(MODEL_PATH)

# Upload section
st.markdown("### Upload Currency Image")
uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

if uploaded_file:
    with st.spinner("Analyzing image..."):
        image, display_img = preprocess_image(uploaded_file, IMAGE_SIZE)

    st.image(display_img, caption="Uploaded Image", use_column_width=True)

    score = predict(model, image)

    show_result(score)
