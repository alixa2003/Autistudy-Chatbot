import streamlit as st
import base64

def render():

    # -------- Load About Image --------
    with open("assets/about_img1.png", "rb") as f:
        about_img = base64.b64encode(f.read()).decode()

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

    html = f"""
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">

<style>

body {{
    font-family: 'Nunito', sans-serif;
}}

a {{
    text-decoration:none;
}}

/* ================= HEADER ================= */

.about-header {{
    display:flex;
    justify-content:space-between;
    align-items:center;
    background:rgba(235,243,255,0.85);
    padding:14px 24px;
    border-radius:22px;
    margin:20px auto;
    max-width:1000px;
}}

.nav-btn {{
    font-size:16px;
    font-weight:600;
    color:#5A78C8;
}}

.nav-btn:hover {{
    color:#1F3C88;
}}

.about-links {{
    display:flex;
    gap:14px;
    background:#EEF4FF;
    padding:8px 20px;
    border-radius:30px;
}}

.small-btn {{
    font-size:15px;
    font-weight:600;
    color:#5A78C8;
}}

.small-btn:hover {{
    color:#1F3C88;
}}

.separator {{
    color:#B5C3EA;
}}

/* ================= HERO ================= */

.about-hero {{
    max-width:1100px;
    margin:40px auto 0;
    display:flex;
    justify-content:space-between;
    align-items:center;
}}

.about-title {{
    font-size:60px;
    font-weight:800;
    color:#1F3C88;
}}

.about-image img {{
    width:480px;
    max-width:100%;
}}

/* ================= ACCORDION ================= */

.accordion-wrapper {{
    max-width:900px;
    margin:60px auto 80px;
    display:flex;
    flex-direction:column;
    gap:18px;
}}

details {{
    background:linear-gradient(135deg,#EEF3FF,#F7F9FF);
    border-radius:18px;
    padding:18px 22px;
    box-shadow:0 4px 12px rgba(0,0,0,0.04);
}}

summary {{
    list-style:none;
    font-size:18px;
    font-weight:700;
    color:#1F3C88;
    display:flex;
    justify-content:space-between;
    align-items:center;
    cursor:pointer;
}}

summary::-webkit-details-marker {{
    display:none;
}}

summary::after {{
    content:"⌄";
    font-size:22px;
    transition:transform .3s ease;
}}

details[open] summary::after {{
    transform:rotate(180deg);
}}

details p {{
    margin-top:14px;
    color:#3B4F7D;
    line-height:1.7;
    font-size:15px;
}}
a,
a:hover,
a:focus,
a:active {{
    text-decoration: none !important;
}}
</style>

<!-- HEADER -->
<div class="about-header">

<a class="nav-btn" href="{back_link}" target="_self">
← {back_text}
</a>

<div class="about-links">
<a class="small-btn" href="/?page=faqs" target="_self">FAQs</a>
<span class="separator">|</span>
<a class="small-btn" href="/?page=privacy" target="_self">Privacy Policy & Terms</a>
</div>

</div>

<!-- HERO -->
<div class="about-hero">

<div class="about-title">About</div>

<div class="about-image">
<img src="data:image/png;base64,{about_img}">
</div>

</div>

<!-- ACCORDION -->

<div class="accordion-wrapper">

<details open>
<summary>About the System</summary>
<p>
This chatbot is a smart learning helper made especially for autistic students.
It helps students from Grade 4 to Grade 7.
It can explain Math, Science, and Computer subjects.
It gives answers in simple and clear language.
It can show text, pictures, and even speak out loud.
It remembers your learning preferences.
It adjusts explanations based on how you learn best.
It is designed to make learning calm, safe, and comfortable.
</p>
</details>

<details>
<summary>How It Works</summary>
<p>
You type or speak your question to the chatbot.
The system understands what you are asking.
It searches your grade textbooks for correct information.
It chooses the best way to explain — text, image, or voice.
If you like pictures more, it shows images.
If you prefer listening, it gives voice answers.
It remembers where you stopped learning.
You can continue anytime from the same place.
</p>
</details>

<details>
<summary>Safety & Ethics</summary>
<p>
The chatbot gives answers only from trusted textbooks.
It does not guess or make up information.
It avoids harmful or unsafe content.
It protects your personal information.
Your data is stored safely and securely.
It does not replace doctors or therapists.
Parents and teachers can monitor progress.
The system is built to support and protect students.
</p>
</details>

<details>
<summary>Coverage</summary>
<p>
The chatbot supports Grade 4 to Grade 7 students.
It covers Math, Science, and Computer subjects.
It explains topics step by step.
It supports text, pictures, and voice learning.
It remembers your learning progress.
It helps with homework and practice questions.
It provides simple study feedback.
It works online anytime you need help.
</p>
</details>

</div>
"""

    st.markdown(html, unsafe_allow_html=True)