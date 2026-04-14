import streamlit as st
from config import MODEL_PATH, IMAGE_SIZE
from model_loader import load_trained_model
from utils import preprocess_image, predict
from ui import load_css, navbar, hero, upload_card, show_result, footer, auth_ui
from auth import login, signup

st.set_page_config(page_title="Rupee Vision", layout="wide")

# Initialize session
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# Load styles
load_css()

# ================= LOGIN PAGE =================
if not st.session_state["logged_in"]:

    auth_ui()

    menu = st.radio("Select Option", ["Login", "Sign Up"])

    if menu == "Login":
        login()
    else:
        signup()

# ================= MAIN APP =================
else:

    navbar()
    hero()

    st.sidebar.success(f"Logged in as {st.session_state['user']}")

    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False

    model = load_trained_model(MODEL_PATH)

    col1, col2 = st.columns(2)

    with col1:
        uploaded_file = upload_card()

    with col2:
        if uploaded_file:
            with st.spinner("Analyzing..."):
                image, display_img = preprocess_image(uploaded_file, IMAGE_SIZE)

            st.image(display_img, caption="Uploaded Image", use_column_width=True)

            score = predict(model, image)
            show_result(score)

    footer()
