import streamlit as st
import base64
from pathlib import Path  # Added import

def render():

    # -------- Load Images with Correct Path --------
    # 1. Get the directory of THIS file (views/faqs.py)
    # 2. Go UP one level to the root, then into 'assets'
    base_path = Path(__file__).parent.parent / "assets"

    def get_encoded_img(img_name):
        img_path = base_path / img_name
        try:
            with open(img_path, "rb") as f:
                # Use 'base64' to match standard import
                return base64.b64encode(f.read()).decode()
        except FileNotFoundError:
            return "" # Fallback to prevent crash

    hero_img = get_encoded_img("about_img1.png")
    bg_img = get_encoded_img("faqs_img1.png")

    # -------- Detect Source Page --------
    src = st.query_params.get("from")

    if src == "login":
        back_text = "Back to Login"
        back_link = "/?page=login"
    elif src == "signup":
        back_text = "Back to Sign Up"
        back_link = "/?page=signup"
    else:
        back_text = "Back to Home"
        back_link = "/?page=landing"

    # -------- FAQ DATA --------
    faqs =

    # -------- Session Control --------
    if "faq_visible" not in st.session_state:
        st.session_state.faq_visible = 5

    visible_count = st.session_state.faq_visible

    # -------- Styling --------
    st.markdown("""
    <style>

    body {
        font-family: 'Nunito', sans-serif;
    }

    a {
        text-decoration:none !important;
    }

    /* HEADER */
    .page-header {
        display:flex;
        justify-content:space-between;
        align-items:center;
        background:rgba(235,243,255,0.85);
        padding:14px 24px;
        border-radius:22px;
        margin:20px auto;
        max-width:1000px;
    }

    .nav-btn {
        font-size:16px;
        font-weight:600;
        color:#5A78C8;
    }

    .page-links {
        display:flex;
        gap:14px;
        background:#EEF4FF;
        padding:8px 20px;
        border-radius:30px;
    }

    .small-btn {
        font-size:15px;
        font-weight:600;
        color:#5A78C8;
    }

    .separator {
        color:#B5C3EA;
    }

    /* HERO */
    .page-hero {
        max-width:1100px;
        margin:40px auto 0;
        display:flex;
        justify-content:space-between;
        align-items:center;
    }

    .page-title {
        font-size:48px;
        font-weight:800;
        color:#1F3C88;
    }

    .page-subtitle {
        margin-top:12px;
        font-size:18px;
        color:#3B4F7D;
        max-width:500px;
    }

    .page-image img {
        width:420px;
        max-width:100%;
    }

    /* FAQ SECTION */
    .faq-section {
        max-width:900px;
        margin:80px auto;
    }

    .faq-question {
        background:#DCE8FF;
        padding:14px 20px;
        border-radius:14px;
        margin-bottom:8px;
        font-weight:600;
        color:#1F3C88;
    }

    .faq-answer {
        background:white;
        padding:14px 20px;
        border-radius:14px;
        margin-bottom:22px;
        color:#3B4F7D;
        font-size:14px;
        line-height:1.6;
        box-shadow:0 4px 10px rgba(0,0,0,0.04);
    }

    /* Blue Button */
    div.stButton > button {
        background:#1F3C88;
        color:white;
        border-radius:25px;
        padding:10px 30px;
        font-weight:600;
        border:none;
    }

    div.stButton > button:hover {
        background:#16306E;
        color:white;
    }

    </style>
    """, unsafe_allow_html=True)

    # -------- HEADER --------
    st.markdown(f"""
    <div class="page-header">
        <a class="nav-btn" href="{back_link}" target="_self">← {back_text}</a>
        <div class="page-links">
            <a class="small-btn" href="/?page=about" target="_self">About</a>
            <span class="separator">|</span>
            <a class="small-btn" href="/?page=privacy" target="_self">Privacy Policy & Terms</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # -------- HERO --------
    st.markdown(f"""
    <div class="page-hero">
        <div>
            <div class="page-title">Frequently Asked Questions</div>
            <div class="page-subtitle">
            Answers to common questions about our adaptive AI chatbot.
            </div>
        </div>
        <div class="page-image">
            <img src="data:image/png;base64,{hero_img}">
        </div>
    </div>
    """, unsafe_allow_html=True)

    # -------- FAQ SECTION --------
    st.markdown('<div class="faq-section">', unsafe_allow_html=True)

    for i in range(min(visible_count, len(faqs))):
        question, answer = faqs[i]
        st.markdown(f'<div class="faq-question">{question}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="faq-answer">{answer}</div>', unsafe_allow_html=True)

    if visible_count < len(faqs):
        if st.button("View More FAQs"):
            if visible_count == 5:
                st.session_state.faq_visible = 10
            elif visible_count == 10:
                st.session_state.faq_visible = len(faqs)
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
