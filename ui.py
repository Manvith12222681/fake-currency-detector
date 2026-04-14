import streamlit as st

def load_css():
    st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(135deg, #020617, #0f172a);
        color: white;
        font-family: 'Inter', sans-serif;
        animation: fadeIn 1s ease-in;
    }

    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }

    .block-container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .auth-box {
        width: 420px;
        padding: 40px;
        border-radius: 20px;
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(20px);
        box-shadow: 0 0 40px rgba(0,229,255,0.2);
        text-align: center;
        margin-top: 80px;
        animation: slideUp 0.8s ease;
    }

    @keyframes slideUp {
        from {transform: translateY(40px); opacity: 0;}
        to {transform: translateY(0); opacity: 1;}
    }

    .title {
        font-size: 40px;
        font-weight: bold;
        background: linear-gradient(90deg, #00e5ff, #7c3aed);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subtitle {
        color: #cbd5f5;
        margin-top: 10px;
    }

    .navbar {
        display: flex;
        justify-content: space-between;
        padding: 15px 30px;
        background: rgba(255,255,255,0.08);
        border-radius: 12px;
        backdrop-filter: blur(10px);
        width: 90%;
    }

    .logo {
        font-size: 22px;
        font-weight: bold;
        color: #00e5ff;
    }

    .hero {
        text-align: center;
        margin-top: 30px;
    }

    .hero-title {
        font-size: 48px;
        font-weight: bold;
        background: linear-gradient(90deg, #00e5ff, #7c3aed);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .card {
        background: rgba(255,255,255,0.08);
        padding: 20px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        margin-top: 20px;
        width: 100%;
    }

    .real { color: #00ff9f; font-size: 22px; }
    .fake { color: #ff4b4b; font-size: 22px; }

    .stButton>button {
        background: linear-gradient(90deg, #00e5ff, #7c3aed);
        border-radius: 10px;
        padding: 10px;
        font-weight: bold;
        width: 100%;
    }

    </style>
    """, unsafe_allow_html=True)


def auth_ui():
    st.markdown("""
    <div class="auth-box">
        <div class="title">Rupee Vision</div>
        <div class="subtitle">Secure Login to Continue</div>
    </div>
    """, unsafe_allow_html=True)


def navbar():
    st.markdown("""
    <div class="navbar">
        <div class="logo">Rupee Vision</div>
        <div>AI Detection</div>
    </div>
    """, unsafe_allow_html=True)


def hero():
    st.markdown("""
    <div class="hero">
        <div class="hero-title">Detect Fake Currency Instantly</div>
    </div>
    """, unsafe_allow_html=True)


def upload_card():
    st.markdown('<div class="card">Upload Currency Image</div>', unsafe_allow_html=True)
    return st.file_uploader("", type=["jpg","png","jpeg"])


def show_result(score):
    st.markdown('<div class="card">', unsafe_allow_html=True)

    if score > 0.5:
        st.markdown('<div class="fake">Fake Currency</div>', unsafe_allow_html=True)
        confidence = score
    else:
        st.markdown('<div class="real">Real Currency</div>', unsafe_allow_html=True)
        confidence = 1 - score

    st.progress(int(confidence * 100))
    st.markdown('</div>', unsafe_allow_html=True)


def footer():
    st.markdown("<center>Rupee Vision © 2026</center>", unsafe_allow_html=True)
