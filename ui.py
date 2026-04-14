import streamlit as st

def load_css():
    st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(270deg, #020617, #0f172a, #1e293b);
        background-size: 600% 600%;
        animation: gradientBG 10s ease infinite;
        color: white;
        font-family: 'Inter', sans-serif;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .hero-title {
        font-size: 52px;
        font-weight: bold;
        background: linear-gradient(90deg, #00e5ff, #7c3aed);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        animation: glow 2s infinite alternate;
    }

    @keyframes glow {
        from { text-shadow: 0 0 10px #00e5ff; }
        to { text-shadow: 0 0 25px #7c3aed; }
    }

    .navbar {
        display: flex;
        justify-content: space-between;
        padding: 15px 30px;
        background: rgba(255,255,255,0.08);
        border-radius: 15px;
        backdrop-filter: blur(12px);
        margin-bottom: 30px;
    }

    .logo {
        font-size: 24px;
        font-weight: bold;
        color: #00e5ff;
    }

    .card {
        background: rgba(255,255,255,0.08);
        padding: 25px;
        border-radius: 20px;
        backdrop-filter: blur(20px);
        box-shadow: 0 10px 40px rgba(0,0,0,0.4);
        margin-top: 20px;
        transition: 0.3s;
    }

    .card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 15px 60px rgba(0,229,255,0.3);
    }

    section[data-testid="stFileUploader"] {
        border: 2px dashed #00e5ff;
        padding: 30px;
        border-radius: 20px;
        background: rgba(255,255,255,0.05);
        transition: 0.3s;
    }

    section[data-testid="stFileUploader"]:hover {
        border-color: #7c3aed;
        box-shadow: 0 0 20px #7c3aed;
    }

    .stButton>button {
        background: linear-gradient(90deg, #00e5ff, #7c3aed);
        border-radius: 12px;
        padding: 12px;
        font-weight: bold;
        transition: 0.3s;
    }

    .stButton>button:hover {
        transform: scale(1.08);
        box-shadow: 0 0 25px #00e5ff;
    }

    .real { color: #00ff9f; font-size: 22px; }
    .fake { color: #ff4b4b; font-size: 22px; }

    .footer {
        text-align: center;
        margin-top: 50px;
        color: #94a3b8;
    }

    </style>
    """, unsafe_allow_html=True)


def auth_ui():
    st.markdown("""
    <div style="text-align:center; margin-top:80px;">
        <h1 class="hero-title">Rupee Vision</h1>
        <p style="color:#cbd5f5;">Secure Login to Continue</p>
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
    <div class="hero-title">Detect Fake Currency Instantly</div>
    """, unsafe_allow_html=True)


def upload_card():
    st.markdown('<div class="card">Upload Currency Image</div>', unsafe_allow_html=True)
    return st.file_uploader("", type=["jpg","png","jpeg"])


def show_result(score):
    st.markdown('<div class="card">', unsafe_allow_html=True)

    if score > 0.5:
        st.markdown('<div class="fake">Fake Currency Detected</div>', unsafe_allow_html=True)
        confidence = score
    else:
        st.markdown('<div class="real">Real Currency Detected</div>', unsafe_allow_html=True)
        confidence = 1 - score

    st.progress(int(confidence * 100))
    st.markdown('</div>', unsafe_allow_html=True)


def footer():
    st.markdown("<div class='footer'>Rupee Vision © 2026</div>", unsafe_allow_html=True)
