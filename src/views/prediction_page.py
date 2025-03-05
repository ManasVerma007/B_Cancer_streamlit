import streamlit as st
from models.prediction_model import Prediction_Model
import os


def prediction_page():
    # Load CSS from file
    css_file_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "static",
        "assets",
        "prediction_page.css",
    )
    with open(css_file_path, "r") as f:
        css = f.read()

    # Apply CSS
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

    # Your existing prediction page code here...
    st.markdown(
        '<h1 class="section-header">Breast Cancer Prediction</h1>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="input-section">', unsafe_allow_html=True)
    st.markdown(
        '<h3 class="input-header">Enter Tumor Measurements</h3>', unsafe_allow_html=True
    )

    st.write(
        "Enter the following features to make a prediction about the tumor status:"
    )

    # Using tabs for better organization of input features
    tab1, tab2, tab3 = st.tabs(["Mean Values", "Standard Error Values", "Worst Values"])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            radius_mean = st.number_input(
                "Radius Mean",
                min_value=0.0,
                value=14.0,
                help="Mean of distances from center to points on the perimeter",
            )
            perimeter_mean = st.number_input(
                "Perimeter Mean",
                min_value=0.0,
                value=90.0,
                help="Mean size of the core tumor",
            )
        with col2:
            texture_mean = st.number_input(
                "Texture Mean",
                min_value=0.0,
                value=19.0,
                help="Standard deviation of gray-scale values",
            )
            area_mean = st.number_input(
                "Area Mean", min_value=0.0, value=650.0, help="Mean area of the tumor"
            )

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            radius_se = st.number_input(
                "Radius SE",
                min_value=0.0,
                value=0.5,
                help="Standard error for the mean of distances from center to points",
            )
            perimeter_se = st.number_input(
                "Perimeter SE",
                min_value=0.0,
                value=4.0,
                help="Standard error for the mean size of the core tumor",
            )
        with col2:
            texture_se = st.number_input(
                "Texture SE",
                min_value=0.0,
                value=0.7,
                help="Standard error for the standard deviation of gray-scale values",
            )
            area_se = st.number_input(
                "Area SE",
                min_value=0.0,
                value=75.0,
                help="Standard error for the mean area of the tumor",
            )

    with tab3:
        col1, col2 = st.columns(2)
        with col1:
            radius_worst = st.number_input(
                "Radius Worst",
                min_value=0.0,
                value=20.0,
                help="Worst or largest mean value of distances from center",
            )
            perimeter_worst = st.number_input(
                "Perimeter Worst",
                min_value=0.0,
                value=120.0,
                help="Worst or largest mean size of the core tumor",
            )
        with col2:
            texture_worst = st.number_input(
                "Texture Worst",
                min_value=0.0,
                value=25.0,
                help="Worst or largest standard deviation of gray-scale values",
            )
            area_worst = st.number_input(
                "Area Worst",
                min_value=0.0,
                value=800.0,
                help="Worst or largest mean area of the tumor",
            )

    st.markdown("</div>", unsafe_allow_html=True)

    form_data = {
        "radius_mean": radius_mean,
        "texture_mean": texture_mean,
        "perimeter_mean": perimeter_mean,
        "area_mean": area_mean,
        "radius_se": radius_se,
        "texture_se": texture_se,
        "perimeter_se": perimeter_se,
        "area_se": area_se,
        "radius_worst": radius_worst,
        "texture_worst": texture_worst,
        "perimeter_worst": perimeter_worst,
        "area_worst": area_worst,
    }

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Generate Prediction", key="predict_button"):
            # Show a spinner while processing
            with st.spinner("Processing..."):
                model = Prediction_Model(form_data)
                result = "Malignant" if model.predict() == 1 else "Benign"
                st.session_state["result"] = result
                st.session_state["form_data"] = form_data
                st.session_state["page"] = "Result"
                st.rerun()

    st.markdown("---")
    st.markdown('<div class="note-box">', unsafe_allow_html=True)
    st.write(
        """
    **Note:** The prediction system uses a machine learning model trained on the Wisconsin Breast Cancer Dataset. 
    This model provides approximately 96-97% accuracy on test data. The results should be used as a supportive tool 
    for medical professionals and not as a definitive diagnosis.
    """
    )
    st.markdown("</div>", unsafe_allow_html=True)
