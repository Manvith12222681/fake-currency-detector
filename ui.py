import streamlit as st

def load_css():
    st.markdown("""
    <style>

    body {
        background: linear-gradient(135deg, #020617, #0f172a);
        color: white;
        font-family: 'Inter', sans-serif;
    }

    /* NAVBAR */
    .navbar {
        display: flex;
        justify-content: space-between;
        padding: 15px 40px;
        background: rgba(255,255,255,0.05);
        border-radius: 12px;
        margin-bottom: 20px;
    }

    .logo {
        font-size: 22px;
        font-weight: bold;
        color: #38bdf8;
    }

    /* HERO */
    .hero {
        text-align: center;
        margin-top: 30px;
    }

    .hero-title {
        font-size: 48px;
        font-weight: bold;
        background: linear-gradient(to right, #38bdf8, #6366f1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-sub {
        color: #cbd5f5;
        margin-top: 10px;
    }

    /* CARD */
    .card {
        background: rgba(255,255,255,0.05);
        padding: 25px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        box-shadow: 0 10px 40px rgba(0,0,0,0.4);
        margin-top: 20px;
    }

    /* RESULT */
    .real {
        color: #22c55e;
        font-size: 26px;
        font-weight: bold;
    }

    .fake {
        color: #ef4444;
        font-size: 26px;
        font-weight: bold;
    }

    /* FOOTER */
    .footer {
        text-align: center;
        margin-top: 40px;
        color: #94a3b8;
    }

    </style>
    """, unsafe_allow_html=True)


def navbar():
    st.markdown("""
    <div class="navbar">
        <div class="logo">Rupee Vision</div>
        <div>AI Currency Detection Platform</div>
    </div>
    """, unsafe_allow_html=True)


def hero():
    st.markdown("""
    <div class="hero">
        <div class="hero-title">Rupee Vision</div>
        <div class="hero-sub">Detect Fake Currency with AI Precision</div>
    </div>
    """, unsafe_allow_html=True)


def upload_card():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Upload Currency Image")
    file = st.file_uploader("", type=["jpg", "jpeg", "png"])
    st.markdown('</div>', unsafe_allow_html=True)
    return file


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


def footer():
    st.markdown("""
    <div class="footer">
        Built with AI • Rupee Vision © 2026
    </div>
    """, unsafe_allow_html=True)
