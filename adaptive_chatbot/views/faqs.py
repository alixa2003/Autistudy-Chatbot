 import streamlit as st
import base64

def render():

    # -------- Load Images --------
    with open("assets/about_img1.png", "rb") as f:
        hero_img = base64.b64encode(f.read()).decode()

    with open("assets/faqs_img1.png", "rb") as f:
        bg_img = base64.b64encode(f.read()).decode()

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
    faqs = [
        ("1️⃣ What is this AI chatbot for?",
         "This AI chatbot is designed to help autistic students in Grades 4–7 understand school subjects more easily."),
        ("2️⃣ How does the chatbot answer questions?",
         "It uses Retrieval-Augmented Generation (RAG), searching approved textbooks before generating answers."),
        ("3️⃣ What subjects are supported?",
         "Mathematics, Science (Biology, Physics, Chemistry), and Computer Studies."),
        ("4️⃣ Is the chatbot safe for children?",
         "Yes. It filters harmful content and only uses trusted material."),
        ("5️⃣ Does it replace teachers?",
         "No. It supports learning but does not replace teachers or professionals."),
        ("6️⃣ How does personalization work?",
         "It remembers grade level, preferences, and progress."),
        ("7️⃣ Can parents monitor progress?",
         "Yes. Learning summaries and reports are available."),
        ("8️⃣ How are difficult topics handled?",
         "It breaks them into smaller steps and provides examples."),
        ("9️⃣ What technology powers it?",
         "AI, NLP, RAG, vector search, and text-to-speech."),
        ("🔟 Does it store personal data?",
         "Only necessary learning data is stored securely."),
        ("1️⃣1️⃣ Can it work on mobile?",
         "Yes. It runs on laptops, tablets, and phones."),
        ("1️⃣2️⃣ What if it doesn't understand?",
         "It asks the student to clarify or rephrase."),
        ("1️⃣3️⃣ Can it remember progress?",
         "Yes. It saves session memory."),
        ("1️⃣4️⃣ Does it require internet?",
         "Yes. Real-time AI requires internet connection."),
        ("1️⃣5️⃣ What if I face technical problems?",
         "Refresh or check your connection. Contact support if needed.")
    ]

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
