import streamlit as st
import os

def landing_page():
    css_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "assets", "landing_page.css")
    with open(css_file_path, "r") as f:
        css = f.read()
    
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    
    st.markdown('<h1 class="main-header">Welcome to the Breast Cancer Prediction App</h1>', unsafe_allow_html=True)
    
    st.markdown('<h2 class="sub-header">Project Overview</h2>', unsafe_allow_html=True)
    st.write("""
    This application helps medical professionals and researchers predict whether a breast cancer tumor 
    is malignant or benign based on various tumor characteristics. By analyzing key measurements from 
    breast mass tissue samples, our model provides quick and accurate predictions to support clinical decisions.
    """)
    
    st.markdown('<h2 class="sub-header">Key Features</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">📊 Input Parameters</div>
            <div class="feature-content">
                <ul>
                    <li>Radius measurements</li>
                    <li>Texture analysis</li>
                    <li>Perimeter calculations</li>
                    <li>Area measurements</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">🔍 Output</div>
            <div class="feature-content">
                <ul>
                    <li>Binary classification: Malignant or Benign</li>
                    <li>Downloadable PDF report</li>
                    <li>Visual result presentation</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<h2 class="sub-header">Technical Implementation</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="tech-container">
            <div class="feature-title">🧠 Machine Learning Model</div>
            <p>The prediction system uses a Random Forest Classifier trained on the Wisconsin Breast Cancer Dataset. This model was chosen for its:</p>
            <ul>
                <li>High accuracy (96% on test data)</li>
                <li>Robust performance with medical data</li>
                <li>Ability to handle non-linear relationships</li>
                <li>Resistance to overfitting</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="tech-container">
            <div class="feature-title">💻 Frontend Technology</div>
            <p>The application is built using:</p>
            <ul>
                <li>Streamlit for the interactive web interface</li>
                <li>Custom CSS for enhanced visual presentation</li>
                <li>FPDF for generating detailed PDF reports</li>
                <li>Responsive design for various screen sizes</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<h2 class="sub-header">How to Use</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="tech-container">
        <ol>
            <li>Navigate to the 'Prediction' page using the sidebar</li>
            <li>Input the tumor measurements</li>
            <li>Click the 'Predict' button</li>
            <li>View the results and download the PDF report</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
        
    st.markdown("""
    <div class="call-to-action">
        <h3 style='margin-bottom: 15px; font-size: 28px;'>Ready to make a prediction?</h3>
        <p style='font-size: 18px;'>Head over to the Prediction page to get started!</p>
    </div>
    """, unsafe_allow_html=True)