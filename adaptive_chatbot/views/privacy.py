import streamlit as st
import base64
import os


def get_image_base64(filename):
    """
    Load image safely using absolute path.
    Works locally and on Streamlit Cloud.
    """
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    image_path = os.path.join(BASE_DIR, "assets", filename)

    if not os.path.exists(image_path):
        st.error(f"Image not found: {image_path}")
        return ""

    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def render():

    # -------- Load Hero Image (SAFE WAY) --------
    hero_img = get_image_base64("about_img1.png")

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

    # -------- CSS --------
    st.markdown("""
    <style>
    body { font-family: 'Nunito', sans-serif; }
    a { text-decoration:none !important; }

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

    .separator { color:#B5C3EA; }

    .page-hero {
        max-width:1100px;
        margin:40px auto 60px;
        display:flex;
        justify-content:space-between;
        align-items:center;
    }

    .page-title {
        font-size:46px;
        font-weight:900;
        color:#1F3C88;
    }

    .page-subtitle {
        margin-top:12px;
        font-size:18px;
        color:#3B4F7D;
        max-width:520px;
    }

    .page-image img {
        width:420px;
        max-width:100%;
    }

    div[data-baseweb="tab-list"] {
        gap:15px;
        background:#EAF2FF;
        padding:10px;
        border-radius:40px;
    }

    button[data-baseweb="tab"] {
        font-size:16px !important;
        font-weight:800 !important;
        color:#1F3C88 !important;
        background:transparent !important;
        border-radius:30px !important;
        padding:10px 24px !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        background:#1F3C88 !important;
        color:white !important;
    }

    .section-container {
        background:#F4F7FF;
        padding:35px;
        border-radius:28px;
        margin-top:40px;
        box-shadow:0 10px 30px rgba(0,0,0,0.05);
    }

    .privacy-card {
        background:white;
        padding:24px;
        border-radius:22px;
        margin-bottom:20px;
        box-shadow:0 6px 18px rgba(0,0,0,0.05);
    }

    .privacy-card h4{
        margin:0 0 10px 0;
        color:#1F3C88;
        font-size:22px;
        font-weight:800;
    }

    .privacy-card p{
        margin:0;
        color:#3B4F7D;
        font-size:15px;
        line-height:1.7;
    }

    .checkbox-wrapper {
        margin-top:40px;
        font-size:17px;
        font-weight:400;
        color:#1FA35B;
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
            <a class="small-btn" href="/?page=faqs" target="_self">FAQs</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # -------- HERO --------
    st.markdown(f"""
    <div class="page-hero">
        <div>
            <div class="page-title">Privacy Policy & Terms of Service</div>
            <div class="page-subtitle">
            Please read our Privacy Policy and Terms carefully.
            </div>
        </div>
        <div class="page-image">
            <img src="data:image/png;base64,{hero_img}">
        </div>
    </div>
    """, unsafe_allow_html=True)

    # -------- TABS --------
    tab1, tab2, tab3 = st.tabs(["Data Collection", "Data Usage", "Parental Consent"])

    with tab1:
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.markdown("""
        <div class="privacy-card">
        <h4>What information does the chatbot collect?</h4>
        <p>Basic information such as name, grade level, and email address.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.markdown("""
        <div class="privacy-card">
        <h4>How is my data used?</h4>
        <p>Your data is used only to personalize learning.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.markdown("""
        <div class="privacy-card">
        <h4>Is parental consent required?</h4>
        <p>Yes. Required for children under 13.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # -------- CHECKBOX --------
    st.markdown('<div class="checkbox-wrapper">', unsafe_allow_html=True)
    st.checkbox("I have read and agree to all Terms & Conditions")
    st.markdown('</div>', unsafe_allow_html=True)
