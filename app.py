import streamlit as st
from config import MODEL_PATH, IMAGE_SIZE
from model_loader import load_trained_model
from utils import preprocess_image, predict
from ui import load_css, navbar, hero, upload_card, show_result, footer

# Page config
st.set_page_config(page_title="Rupee Vision", layout="wide")

# UI
load_css()
navbar()
hero()

# Sidebar
st.sidebar.title("Dashboard")
st.sidebar.info("AI-powered fake currency detection")

# Load model
model = load_trained_model(MODEL_PATH)

# Layout
col1, col2 = st.columns([1, 1])

with col1:
    uploaded_file = upload_card()

with col2:
    if uploaded_file:
        with st.spinner("Analyzing currency..."):
            image, display_img = preprocess_image(uploaded_file, IMAGE_SIZE)

        st.image(display_img, caption="Uploaded Image", use_column_width=True)

        score = predict(model, image)
        show_result(score)

# Footer
footer()
