import streamlit as st
from models.prediction_model import Prediction_Model

def prediction_page():
    st.title("Breast Cancer Prediction")
    st.write("Enter the following features:")

    col1, col2, col3 = st.columns(3)

    with col1:
        radius_mean = st.number_input("Radius Mean", help="Mean of distances from center to points on the perimeter")
        radius_se = st.number_input("Radius SE", help="Standard error for the mean of distances from center to points on the perimeter")
        radius_worst = st.number_input("Radius Worst", help="Worst or largest mean value of distances from center to points on the perimeter")
        area_mean = st.number_input("Area Mean", help="Mean area of the tumor")

    with col2:
        texture_mean = st.number_input("Texture Mean", help="Standard deviation of gray-scale values")
        texture_se = st.number_input("Texture SE", help="Standard error for the standard deviation of gray-scale values")
        texture_worst = st.number_input("Texture Worst", help="Worst or largest standard deviation of gray-scale values")
        area_se = st.number_input("Area SE", help="Standard error for the mean area of the tumor")

    with col3:
        perimeter_mean = st.number_input("Perimeter Mean", help="Mean size of the core tumor")
        perimeter_se = st.number_input("Perimeter SE", help="Standard error for the mean size of the core tumor")
        perimeter_worst = st.number_input("Perimeter Worst", help="Worst or largest mean size of the core tumor")
        area_worst = st.number_input("Area Worst", help="Worst or largest mean area of the tumor")

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
        "area_worst": area_worst
    }

    if st.button("Predict"):
        model = Prediction_Model(form_data)
        result = "Malignant" if model.predict() == 1 else "Benign"
        st.session_state['result'] = result
        st.session_state['form_data'] = form_data
        st.session_state['page'] = 'Result'
        st.rerun()

    st.markdown("---")
    st.write("""
    **Note:** The prediction system uses a Random Forest Classifier trained on the Wisconsin Breast Cancer Dataset. 
    This model averages around 97% accuracy.
    """)