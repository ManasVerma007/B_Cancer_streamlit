import streamlit as st
import os
from views.landing_page import landing_page
from views.prediction_page import prediction_page
from views.results_page import results_page

st.set_page_config(
    page_title="Breast Cancer Prediction",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

css_file_path = os.path.join(os.path.dirname(__file__), "static", "assets", "style.css")
with open(css_file_path, "r") as f:
    css = f.read()

st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

st.sidebar.markdown("""
<div class="sidebar-header" style='text-align: center; padding: 10px 0; margin-bottom: 20px; border-bottom: 1px solid #ddd;'>
    <h1>🩺 Breast Cancer Prediction</h1>
    <p style='margin-top: 5px;'>AI-Powered Diagnostic Tool</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("## Navigation")
if 'page' not in st.session_state:
    st.session_state['page'] = 'Home'

def nav_button(label, page_name):
    current = st.session_state['page'] == page_name
    button_style = "primary" if current else "secondary"
    if st.sidebar.button(label, type=button_style, use_container_width=True):
        st.session_state['page'] = page_name
        st.rerun()

nav_button("🏠 Home", "Home")
nav_button("🔬 Make Prediction", "Prediction")
nav_button("📊 View Results", "Result")

if st.session_state['page'] == "Home":
    landing_page()
elif st.session_state['page'] == "Prediction":
    prediction_page()
elif st.session_state['page'] == "Result":
    results_page()

st.sidebar.markdown("---")

# Add Social Links section
st.sidebar.markdown("<h2 style='text-align: center; margin-bottom: 15px;'>Connect With Me</h2>", unsafe_allow_html=True)
st.sidebar.markdown("""
<div class="social-links" style='display: flex; justify-content: center; margin-bottom: 20px;'>
    <a href="https://github.com/ManasVerma007/B_Cancer_streamlit" target="_blank" style='margin: 0 10px; color: #3498db; text-decoration: none;'>
        <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="32" height="32" style='display: block; margin: 0 auto;'>
        <span style='display: block; text-align: center; font-size: 0.8rem; margin-top: 5px;'>GitHub</span>
    </a>
    <a href="https://www.linkedin.com/in/manas-verma-0000ba227/" target="_blank" style='margin: 0 10px; color: #3498db; text-decoration: none;'>
        <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="32" height="32" style='display: block; margin: 0 auto;'>
        <span style='display: block; text-align: center; font-size: 0.8rem; margin-top: 5px;'>LinkedIn</span>
    </a>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

# Footer
st.sidebar.markdown("""
<div class="sidebar-footer" style='text-align: center; padding: 10px; opacity: 0.7;'>
    <p style='font-size: 0.8rem; margin-bottom: 5px;'>
        Developed with ❤️ for Healthcare
    </p>
    <p style='font-size: 0.7rem;'>
        © 2025 Breast Cancer Prediction App
    </p>
</div>
""", unsafe_allow_html=True)