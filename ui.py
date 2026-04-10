import streamlit as st

def load_css():
    st.markdown("""
    <style>

    /* GLOBAL */
    body {
        background: linear-gradient(135deg, #0f172a, #020617);
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }

    /* NAVBAR */
    .navbar {
        display: flex;
        justify-content: space-between;
        padding: 10px 30px;
        background: rgba(255,255,255,0.05);
        border-radius: 10px;
        margin-bottom: 20px;
    }

    .logo {
        font-size: 20px;
        font-weight: bold;
        color: #38bdf8;
    }

    /* HERO */
    .hero {
        text-align: center;
        padding: 40px 20px;
    }

    .hero-title {
        font-size: 50px;
        font-weight: bold;
        background: linear-gradient(to right, #38bdf8, #6366f1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        color: #cbd5f5;
        margin-top: 10px;
        font-size: 18px;
    }

    /* BUTTON */
    .cta {
        margin-top: 20px;
        padding: 10px 20px;
        background: #38bdf8;
        color: black;
        border-radius: 8px;
        font-weight: bold;
        display: inline-block;
    }

    /* CARD */
    .card {
        background: rgba(255,255,255,0.05);
        padding: 20px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.3);
        margin-top: 20px;
    }

    /* FEATURE GRID */
    .grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        margin-top: 30px;
    }

    /* RESULT */
    .real {
        color: #22c55e;
        font-size: 24px;
        font-weight: bold;
    }

    .fake {
        color: #ef4444;
        font-size: 24px;
        font-weight: bold;
    }

    /* UPLOAD */
    .upload {
        border: 2px dashed #38bdf8;
        padding: 30px;
        border-radius: 12px;
        text-align: center;
        margin-top: 20px;
    }

    </style>
    """, unsafe_allow_html=True)


def navbar():
    st.markdown("""
    <div class="navbar">
        <div class="logo">Rupee Vision</div>
        <div>AI Currency Detection</div>
    </div>
    """, unsafe_allow_html=True)


def hero():
    st.markdown("""
    <div class="hero">
        <div class="hero-title">Detect Fake Currency Instantly</div>
        <div class="hero-subtitle">
            Powered by Deep Learning for real-time verification
        </div>
        <div class="cta">Upload & Analyze</div>
    </div>
    """, unsafe_allow_html=True)


def features():
    st.markdown("""
    <div class="grid">
        <div class="card">
            <h4>⚡ Fast</h4>
            <p>Instant AI predictions</p>
        </div>
        <div class="card">
            <h4>🧠 Smart</h4>
            <p>CNN-based detection</p>
        </div>
        <div class="card">
            <h4>🌐 Simple</h4>
            <p>User-friendly interface</p>
        </div>
    </div>
    """, unsafe_allow_html=True)


def show_result(score):
    st.markdown('<div class="card">', unsafe_allow_html=True)

    if score > 0.5:
        st.markdown('<div class="fake">Fake Currency Detected</div>', unsafe_allow_html=True)
        confidence = score
    else:
        st.markdown('<div class="real">Real Currency Detected</div>', unsafe_allow_html=True)
        confidence = 1 - score

    st.progress(int(confidence * 100))
    st.write(f"Confidence: {confidence:.2f}")

    st.markdown('</div>', unsafe_allow_html=True)
