import streamlit as st
import os
from utils.pdf_generator import create_pdf

def results_page():
    css_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "assets", "results_page.css")
    with open(css_file_path, "r") as f:
        css = f.read()
    
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    
    st.markdown('<h1 class="page-title">Prediction Result</h1>', unsafe_allow_html=True)
    
    if 'result' in st.session_state:
        result = st.session_state['result']
        form_data = st.session_state['form_data']
        
        st.markdown('<div class="result-section">', unsafe_allow_html=True)
        st.markdown('<h3 class="result-header">Diagnosis Result:</h3>', unsafe_allow_html=True)
        
        if result == "Malignant":
            st.markdown(
                f"""
                <div class="malignant-result">
                    <p class="malignant-text">⚠️ {result}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown("""
                <p style="color: #8B0000; font-style: italic;">
                    The model predicts this tumor is likely malignant. This suggests the presence of cancerous cells.
                    Please consult with a medical professional for a thorough evaluation.
                </p>
                """, unsafe_allow_html=True)
        else:
            st.markdown(
                f"""
                <div class="benign-result">
                    <p class="benign-text">✓ {result}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown("""
                <p style="color: #006400; font-style: italic;">
                    The model predicts this tumor is likely benign. This suggests the absence of cancerous cells.
                    Regular check-ups are still recommended.
                </p>
                """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Feature display section
        st.markdown('<div class="result-section">', unsafe_allow_html=True)
        st.markdown('<h3 class="result-header">Input Features:</h3>', unsafe_allow_html=True)
        
        tabs = st.tabs(["Mean Values", "SE Values", "Worst Values"])
        
        mean_features = {k:v for k,v in form_data.items() if 'mean' in k}
        se_features = {k:v for k,v in form_data.items() if 'se' in k}
        worst_features = {k:v for k,v in form_data.items() if 'worst' in k}
        
        with tabs[0]:
            for key, value in mean_features.items():
                formatted_key = key.replace('_mean', '').title()
                st.markdown(f"""
                <div class="feature-card">
                    <div class="feature-title">{formatted_key}</div>
                    <div class="feature-value">{value:.3f}</div>
                </div>
                """, unsafe_allow_html=True)
                
        with tabs[1]:
            for key, value in se_features.items():
                formatted_key = key.replace('_se', '').title()
                st.markdown(f"""
                <div class="feature-card">
                    <div class="feature-title">{formatted_key}</div>
                    <div class="feature-value">{value:.3f}</div>
                </div>
                """, unsafe_allow_html=True)
                
        with tabs[2]:
            for key, value in worst_features.items():
                formatted_key = key.replace('_worst', '').title()
                st.markdown(f"""
                <div class="feature-card">
                    <div class="feature-title">{formatted_key}</div>
                    <div class="feature-value">{value:.3f}</div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # PDF Download button
        pdf_data = create_pdf(result, form_data)
        st.download_button(
            label="📥 Download Complete PDF Report",
            data=pdf_data,
            file_name="breast_cancer_prediction_results.pdf",
            mime="application/pdf",
            key="download-pdf",
            use_container_width=True
        )
        
        # Navigation buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⬅️ Make Another Prediction"):
                st.session_state['page'] = 'Prediction'
                st.rerun()
        with col2:
            if st.button("🏠 Return to Home"):
                st.session_state['page'] = 'Home'
                st.rerun()
            
    else:
        st.markdown("""
        <div class="info-message">
            <h4 style="margin-top: 0;">No Prediction Results Available</h4>
            <p>No prediction has been made yet. Please go to the 'Prediction' page to input features and get a prediction.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Go to Prediction Page"):
            st.session_state['page'] = 'Prediction'
            st.rerun()