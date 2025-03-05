import streamlit as st
from utils.pdf_generator import create_pdf

def results_page():
    st.title("Prediction Result")
    if 'result' in st.session_state:
        result = st.session_state['result']
        form_data = st.session_state['form_data']
        
        # White heading and larger result text
        st.markdown("<h4 style='color: white;'>Diagnosis Result:</h4>", unsafe_allow_html=True)
        if result == "Malignant":
            st.markdown(
                f"""
                <div style='background-color: #FFA07A; padding: 8px; border-radius: 6px;
                text-align: left; border: 2px solid #8B0000; width: 25%; margin-left: 0;
                box-shadow: 2px 2px 5px rgba(0,0,0,0.1);'>
                    <h4 style='color: #8B0000; margin: 0; font-size: 25px;'>{result}</h4>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style='background-color: #90EE90; padding: 8px; border-radius: 6px;
                text-align: left; border: 2px solid #006400; width: 25%; margin-left: 0;
                box-shadow: 2px 2px 5px rgba(0,0,0,0.1);'>
                    <h4 style='color: #006400; margin: 0; font-size: 25px;'>{result}</h4>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("<h4 style='color: white;'>Input Features:</h4>", unsafe_allow_html=True)
        features_col1, features_col2, features_col3 = st.columns(3)
        
        mean_features = {k:v for k,v in form_data.items() if 'mean' in k}
        se_features = {k:v for k,v in form_data.items() if 'se' in k}
        worst_features = {k:v for k,v in form_data.items() if 'worst' in k}
        
        def display_feature_group(features, title, container):
            with container:
                st.markdown(f"<h5 style='color: white;'>{title}</h5>", unsafe_allow_html=True)
                for key, value in features.items():
                    st.markdown(
                        f"""
                        <div style='background-color: #f5f5f5; padding: 8px; border-radius: 4px; margin: 4px 0;
                        border: 1px solid #ddd;'>
                            <p style='color: #666666; margin: 0; font-size: 14px;'>
                                <strong>{key.replace('_mean', '').replace('_se', '').replace('_worst', '').title()}</strong>
                                <br>
                                <span style='color: #333333; font-size: 16px;'>{value:.2f}</span>
                            </p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
        
        display_feature_group(mean_features, "Mean Values", features_col1)
        display_feature_group(se_features, "SE Values", features_col2)
        display_feature_group(worst_features, "Worst Values", features_col3)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.download_button(
                label="📥 Download Report as PDF",
                data=create_pdf(result, form_data),
                file_name="breast_cancer_prediction_results.pdf",
                mime="application/pdf",
            )
    else:
        st.info("No prediction made yet. Please go to the 'Prediction' page to input features and get a prediction.")
