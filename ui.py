# ==========================================
# UI COMPONENTS
# ==========================================
import streamlit as st

def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def header():
    st.markdown("""
        <div class="header">
            <h1>Currency Authenticity Detection</h1>
            <p>AI-powered system to detect fake vs real currency</p>
        </div>
    """, unsafe_allow_html=True)


def show_result(score):
    if score > 0.5:
        st.markdown(f"""
            <div class="fake-box">
                Fake Currency Detected<br>
                Confidence: {score:.2f}
            </div>
        """, unsafe_allow_html=True)
        st.progress(int(score * 100))
    else:
        st.markdown(f"""
            <div class="real-box">
                Real Currency Detected<br>
                Confidence: {1-score:.2f}
            </div>
        """, unsafe_allow_html=True)
        st.progress(int((1-score) * 100))