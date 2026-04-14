import streamlit as st


# ================================
# PREMIUM GLOBAL CSS
# ================================
def load_css():
    st.markdown("""
    <style>

    /* FULL APP BACKGROUND */
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }

    /* REMOVE DEFAULT SPACE */
    .block-container {
        padding-top: 1rem;
    }

    /* NAVBAR */
    .navbar {
        display: flex;
        justify-content: space-between;
        padding: 15px 30px;
        background: rgba(255,255,255,0.08);
        border-radius: 12px;
        backdrop-filter: blur(12px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }

    .logo {
        font-size: 24px;
        font-weight: bold;
        color: #00e5ff;
    }

    /* HERO */
    .hero {
        text-align: center;
        margin-top: 40px;
    }

    .hero-title {
        font-size: 52px;
        font-weight: bold;
        background: linear-gradient(90deg, #00e5ff, #7c3aed);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-sub {
        color: #cbd5f5;
        margin-top: 10px;
        font-size: 18px;
    }

    /* AUTH BOX */
    .auth-box {
        max-width: 400px;
        margin: auto;
        margin-top: 100px;
        padding: 30px;
        border-radius: 20px;
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(15px);
        box-shadow: 0 10px 40px rgba(0,0,0,0.5);
        text-align: center;
    }

    /* CARD */
    .card {
        background: rgba(255,255,255,0.08);
        padding: 25px;
        border-radius: 20px;
        backdrop-filter: blur(15px);
        box-shadow: 0 10px 40px rgba(0,0,0,0.4);
        margin-top: 20px;
        transition: 0.3s;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 50px rgba(0,0,0,0.6);
    }

    /* RESULT TEXT */
    .real {
        color: #00ff9f;
        font-size: 26px;
        font-weight: bold;
    }

    .fake {
        color: #ff4b4b;
        font-size: 26px;
        font-weight: bold;
    }

    /* BUTTON */
    .stButton>button {
        background: linear-gradient(90deg, #00e5ff, #7c3aed);
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
        transition: 0.3s;
    }

    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 15px #00e5ff;
    }

    /* FILE UPLOADER */
    section[data-testid="stFileUploader"] {
        border: 2px dashed #00e5ff;
        padding: 20px;
        border-radius: 15px;
        background: rgba(255,255,255,0.05);
    }

    /* FOOTER */
    .footer {
        text-align: center;
        margin-top: 50px;
        color: #94a3b8;
    }

    </style>
    """, unsafe_allow_html=True)


# ================================
# NAVBAR
# ================================
def navbar():
    st.markdown("""
    <div class="navbar">
        <div class="logo">Rupee Vision</div>
        <div>AI Currency Detection Platform</div>
    </div>
    """, unsafe_allow_html=True)


# ================================
# HERO SECTION
# ================================
def hero():
    st.markdown("""
    <div class="hero">
        <div class="hero-title">Rupee Vision</div>
        <div class="hero-sub">Detect Fake Currency with AI Precision</div>
    </div>
    """, unsafe_allow_html=True)


# ================================
# AUTH UI
# ================================
def auth_ui():
    st.markdown("""
    <div class="auth-box">
        <h2 style='color:#00e5ff;'>Rupee Vision</h2>
        <p style='color:#cbd5f5;'>Login to access dashboard</p>
    </div>
    """, unsafe_allow_html=True)


# ================================
# UPLOAD CARD
# ================================
def upload_card():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Upload Currency Image")
    file = st.file_uploader("", type=["jpg", "jpeg", "png"])
    st.markdown('</div>', unsafe_allow_html=True)
    return file


# ================================
# RESULT DISPLAY
# ================================
def show_result(score):
    st.markdown('<div class="card">', unsafe_allow_html=True)

    if score > 0.5:
        st.markdown('<div class="fake">Fake Currency Detected</div>', unsafe_allow_html=True)
        confidence = score
    else:
        st.markdown('<div class="real">Real Currency Detected</div>', unsafe_allow_html=True)
        confidence = 1 - score

    st.progress(int(confidence * 100))
    st.metric("Confidence Score", f"{confidence:.2f}")

    st.markdown('</div>', unsafe_allow_html=True)


# ================================
# FOOTER
# ================================
def footer():
    st.markdown("""
    <div class="footer">
        Built with AI • Rupee Vision © 2026
    </div>
    """, unsafe_allow_html=True)
