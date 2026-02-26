import streamlit as st
import importlib

def navigate(page):
    st.session_state.page = page

def load_page():
    if "page" not in st.session_state:
        st.session_state.page = "landing"

    page = st.session_state.page
    module = importlib.import_module(f"views.{page}")
    module.render()