import streamlit as st
import base64
from pathlib import Path

def render():
    # ================= LOAD IMAGES =================
    
    # 1. Get the directory where THIS file (landing.py) is located
    # 2. Go UP one level to reach the root, then into 'assets'
    # .parent gets 'views/', .parent.parent gets the root '/'
    base_path = Path(__file__).parent.parent / "assets"

    def get_base64_image(file_name):
        file_path = base_path / file_name
        with open(file_path, "rb") as f:
            # FIX: Changed base_64 to base64 to match the import above
            return base64.b64encode(f.read()).decode()

    # Load all images using the helper
    # Ensure these filenames match your GitHub files EXACTLY (case-sensitive)
    logo = get_base64_image("logo.png")
    img1 = get_base64_image("img1.png")
    lp_img2 = get_base64_image("lp_img2.png")
    lp_img3 = get_base64_image("lp_img3.png")
    lp_img4 = get_base64_image("lp_img4.png")
    lp_img5 = get_base64_image("lp_img5.png")

    # ================= HTML =================

    html = f"""
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;800&display=swap" rel="stylesheet">

<style>

/* ---------- PAGE WRAPPER ---------- */

.page-wrapper {{
    min-height:100vh;
    display:flex;
    flex-direction:column;
}}

.page-content {{
    flex:1;
}}

body {{
    font-family: 'Nunito', sans-serif;
}}

/* ---------- NAVBAR ---------- */

.container {{
    max-width: 880px;
    margin: 4px auto 0 auto;
    background: rgba(235,243,255,0.92);
    border-radius: 22px;
    padding: 14px 28px;
}}

.navbar {{
    display:flex;
    justify-content:space-between;
    align-items:center;
}}

.brand {{
    display:flex;
    gap:14px;
    align-items:center;
}}

.logo {{
    width:56px;
}}

.auti {{ color:#1F3C88; font-weight:800; }}
.study {{ color:#4C9BFF; font-weight:600; }}

.nav-buttons {{
    display:flex;
    gap:14px;
}}
.nava a{{
   text-decoration:none;
}}

.nav-btn {{
    background:#D6E6FF;
    border:none;
    padding:10px 22px;
    border-radius:22px;
    font-size:15px;
    font-weight:700;
    color:#1F3C88;
    cursor:pointer;
    animation:bounce 2s infinite;
    text-decoration:none;
}}

.nav-btn:hover {{
    background:#1F3C88;
    color:white;
}}

@keyframes bounce {{
    0%{{transform:translateY(0)}}
    50%{{transform:translateY(-4px)}}
    100%{{transform:translateY(0)}}
}}

/* ---------- HERO ---------- */

.hero {{
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:40px 6% 0;
}}

.hero-text {{ width:55%; }}

.hero-title {{
    font-size:42px;
    font-weight:800;
    color:#1F3C88;
}}

.hero-subtitle {{
    font-size:20px;
    margin-top:6px;
    color:#1F3C88;
}}

.hero-desc {{
    margin-top:16px;
    max-width:420px;
    color:#3B4F7D;
}}

.hero-image {{ width:45%; }}
.hero-image img {{
    width:100%;
    border-radius:14px;
}}

/* ---------- HIGHLIGHT ---------- */

.highlight-strip {{
    margin:40px auto 20px;
    background:#EDF4FF;
    padding:16px 28px;
    border-radius:28px;
    width:fit-content;
}}

.highlight-strip span {{
    font-size:18px;
    color:#1F3C88;
}}

.highlight-bold {{font-weight:800;}}
.highlight-light {{color:#4C6FBF;}}

/* ---------- SUB DESC ---------- */

.sub-desc {{
    text-align:center;
    max-width:520px;
    margin:0 auto 30px;
    color:#3B4F7D;
}}

/* ---------- FEATURES ---------- */

.features {{
    display:flex;
    justify-content:center;
    gap:22px;
    flex-wrap:wrap;
    margin-bottom:30px;
}}

.feature-card {{
    background:#F4F8FF;
    width:170px;
    padding:20px;
    border-radius:18px;
    text-align:center;
}}

.feature-card img {{
    width:52px;
    margin-bottom:10px;
}}

.feature-title {{
    font-weight:700;
    color:#1F3C88;
}}

/* ---------- CTA ---------- */

.cta-section {{
    display:flex;
    justify-content:center;
    gap:28px;
    margin-bottom:20px;
}}

.cta-btn {{
    padding:16px 44px;
    border:none;
    border-radius:40px;
    font-size:18px;
    font-weight:700;
    background:white;
    color:#1F3C88;
    animation:bounce 2s infinite;
}}

.signup-btn {{
    background:#1F3C88;
    color:white;
}}

.login-btn {{
    background:#1F3C88;
    color:white;
}}
.signup-btn, .login-btn{{
color:white !important;
}}

/* ---------- FOOTER ---------- */

.footer {{
    text-align:center;
    padding:6px 0;
    font-size:14px;
    color:#6B7BAA;
}}
a,
a:hover,
a:focus,
a:active {{
    text-decoration: none !important;
}}
</style>

<div class="page-wrapper">
<div class="page-content">

<!-- NAVBAR -->
<div class="container">
<div class="navbar">

<div class="brand">
<img class="logo" src="data:image/png;base64,{logo}">
<div>
<span class="auti">Auti</span><span class="study">Study</span>
</div>
</div>

<div class="nav-buttons">
<a class="nav-btn" href="/?page=about&from=landing" target="_self">About</a>
<a class="nav-btn" href="/?page=faqs&from=landing" target="_self">FAQs</a>
<a class="nav-btn" href="/?page=privacy&from=landing" target="_self">Privacy</a>
<a class="nav-btn" href="/?page=emergency&from=landing" target="_self">Emergency Support</a>
</div>

</div>
</div>

<!-- HERO -->
<div class="hero">

<div class="hero-text">
<div class="hero-title">Adaptive AI Chatbot<br>for Autistic Students</div>
<div class="hero-subtitle">(Grades 4–7)</div>
<div class="hero-desc">
A learning assistant that helps students understand Math, Science,
and Computer subjects using text, images and voice.
</div>
</div>

<div class="hero-image">
<img src="data:image/png;base64,{img1}">
</div>

</div>

<!-- HIGHLIGHT -->
<div class="highlight-strip">
<span class="highlight-bold">Personalized AI Learning Companion</span>
<span class="highlight-light"> built thoughtfully for </span>
<span class="highlight-bold">Autistic & Neurodiverse Students</span>
</div>

<!-- SUB DESC -->
<div class="sub-desc">
A supportive AI tutor that gently guides students through
Math, Science, and Computer concepts using visuals,
spoken explanations, and simple text.
</div>

<!-- FEATURES -->
<div class="features">

<div class="feature-card">
<img src="data:image/png;base64,{lp_img2}">
<div class="feature-title">Text Learning</div>
</div>

<div class="feature-card">
<img src="data:image/png;base64,{lp_img3}">
<div class="feature-title">Image Support</div>
</div>

<div class="feature-card">
<img src="data:image/png;base64,{lp_img4}">
<div class="feature-title">Voice Support</div>
</div>

<div class="feature-card">
<img src="data:image/png;base64,{lp_img5}">
<div class="feature-title">Safe & Controlled AI</div>
</div>

</div>

<!-- CTA -->
<div class="cta-section">
<a class="cta-btn signup-btn" href="/?page=signup" target="_self">Sign Up</a>
<a class="cta-btn login-btn" href="/?page=login" target="_self">Login</a>
</div>

</div>  <!-- page-content -->

<!-- FOOTER -->
<div class="footer">
© 2026 AutiStudy. All Rights Reserved.
</div>

</div> <!-- page-wrapper -->
"""

    st.markdown(html, unsafe_allow_html=True)
