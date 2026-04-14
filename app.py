import streamlit as st

# Import project modules
from config import MODEL_PATH, IMAGE_SIZE
from model_loader import load_trained_model
from utils import preprocess_image, predict
from ui import load_css, navbar, hero, upload_card, show_result, footer, auth_ui
from auth import login, signup


# ================================
# PAGE CONFIG
# ================================
st.set_page_config(page_title="Rupee Vision", layout="wide")


# ================================
# SESSION STATE INIT
# ================================
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False


# ================================
# LOAD PREMIUM UI
# ================================
load_css()


# ================================
# AUTH SECTION (LOGIN / SIGNUP)
# ================================
if not st.session_state["logged_in"]:

    auth_ui()

    st.markdown("### Access Your Account")

    option = st.radio("", ["Login", "Sign Up"], horizontal=True)

    if option == "Login":
        login()
    else:
        signup()


# ================================
# MAIN APP (AFTER LOGIN)
# ================================
else:

    # Navbar + Hero
    navbar()
    hero()

    # Sidebar
    st.sidebar.title("Rupee Vision Dashboard")
    st.sidebar.success(f"Logged in as: {st.session_state['user']}")

    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.rerun()

    # Load model
    model = load_trained_model(MODEL_PATH)

    # Layout (Dashboard Style)
    col1, col2 = st.columns([1, 1])

    with col1:
        uploaded_file = upload_card()

    with col2:
        if uploaded_file:
            with st.spinner("Analyzing currency image..."):
                image, display_img = preprocess_image(uploaded_file, IMAGE_SIZE)

            st.image(display_img, caption="Uploaded Image", use_column_width=True)

            score = predict(model, image)
            show_result(score)

    # Footer
    footer()
