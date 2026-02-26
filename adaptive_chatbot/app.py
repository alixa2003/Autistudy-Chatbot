from pathlib import Path
import streamlit as st
import base64

from views.landing import render as landing_page
from views.about import render as about_page
from views.faqs import render as faq_page
from views.privacy import render as privacy_page
from views.emergency import render as emergency_page
from views.signup import render as signup_page
from views.login import render as login_page


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AutiStudy",
    layout="wide"
)

st.set_option("client.showErrorDetails", False)


# --------------------------------------------------
# HIDE STREAMLIT CHROME
# --------------------------------------------------
st.markdown("""
<style>
header {visibility: hidden;}
footer {visibility: hidden;}

.block-container {
    padding-top: 0rem;
}
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# BACKGROUND
# --------------------------------------------------
def set_background(image_path):
    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# Get the absolute path to the directory containing this script
script_directory = Path(__file__).parent

# Join it with the assets folder and the image name
image_path = script_directory / "assets" / "Chatbot_background.png"

# Call the function with the corrected path
set_background(image_path)



# --------------------------------------------------
# SESSION INIT
# --------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "landing"


# --------------------------------------------------
# READ URL PARAM (SAFE)
# --------------------------------------------------
page = st.query_params.get("page")

if page and page != st.session_state.page:
    st.session_state.page = page


# --------------------------------------------------
# ROUTER
# --------------------------------------------------
if st.session_state.page == "about":
    about_page()

elif st.session_state.page == "faqs":
    faq_page()

elif st.session_state.page == "privacy":
    privacy_page()

elif st.session_state.page == "emergency":
    emergency_page()

elif st.session_state.page == "signup":
    signup_page()

elif st.session_state.page == "login":
    login_page()

else:

    landing_page()
