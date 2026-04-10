import streamlit as st

def load_css():
    st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
    }

    .main-title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        background: -webkit-linear-gradient(#00c6ff, #0072ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #cccccc;
        margin-bottom: 30px;
    }

    .card {
        background-color: rgba(255,255,255,0.05);
        padding: 20px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        margin-top: 20px;
    }

    .real {
        color: #00ff9f;
        font-size: 22px;
        font-weight: bold;
    }

    .fake {
        color: #ff4b4b;
        font-size: 22px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)


def header():
    st.markdown('<div class="main-title">Fake Currency Detector</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">AI-powered currency authenticity verification system</div>', unsafe_allow_html=True)


def info_section():
    st.markdown("""
    <div class="card">
    <h4>How it works</h4>
    <ul>
        <li>Upload a currency image</li>
        <li>Image is processed using AI</li>
        <li>Model predicts real or fake</li>
        <li>Confidence score is displayed</li>
    </ul>
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
