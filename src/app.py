import streamlit as st
from views.landing_page import landing_page
from views.prediction_page import prediction_page
from views.results_page import results_page

st.set_page_config(
    page_title="Cancer-Prediction",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("Navigation")
if 'page' not in st.session_state:
    st.session_state['page'] = 'Home'

page = st.sidebar.radio("Go to", ["Home", "Prediction", "Result"], 
                       index=["Home", "Prediction", "Result"].index(st.session_state['page']))

if page == "Home":
    landing_page()
elif page == "Prediction":
    prediction_page()
elif page == "Result":
    results_page()

if st.session_state['page'] != page:
    st.session_state['page'] = page
    st.rerun()