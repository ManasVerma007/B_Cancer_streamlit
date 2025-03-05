import streamlit as st

def landing_page():
    st.title("Welcome to the Breast Cancer Prediction App")
    
    # Project Overview
    st.header("Project Overview")
    st.write("""
    This application helps medical professionals and researchers predict whether a breast cancer tumor 
    is malignant or benign based on various tumor characteristics. By analyzing key measurements from 
    breast mass tissue samples, our model provides quick and accurate predictions to support clinical decisions.
    """)
    
    # Key Features
    st.header("Key Features")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### Input Parameters
        - Radius measurements
        - Texture analysis
        - Perimeter calculations
        - Area measurements
        """)
        
    with col2:
        st.markdown("""
        #### Output
        - Binary classification: Malignant or Benign
        - Downloadable PDF report
        - Visual result presentation
        """)
    
    # Technical Details
    st.header("Technical Implementation")
    
    # Model Information
    st.subheader("Machine Learning Model")
    st.write("""
    The prediction system uses a Random Forest Classifier trained on the Wisconsin Breast Cancer Dataset. 
    This model was chosen for its:
    - High accuracy (96% on test data)
    - Robust performance with medical data
    - Ability to handle non-linear relationships
    - Resistance to overfitting
    The model averages around 97% accuracy.
    """)
    
    # Frontend Information
    st.subheader("Frontend Technology")
    st.write("""
    The application is built using:
    - Streamlit for the interactive web interface
    - Custom CSS for enhanced visual presentation
    - FPDF for generating detailed PDF reports
    - Responsive design for various screen sizes
    """)
    
    # How to Use
    st.header("How to Use")
    st.write("""
    1. Navigate to the 'Prediction' page using the sidebar
    2. Input the tumor measurements
    3. Click the 'Predict' button
    4. View the results and download the PDF report
    """)
        
    # Call to Action
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; 
                padding: 30px; 
                background-color: #2c3e50; 
                border-radius: 10px;
                border: 2px solid #34495e;
                margin: 20px 0;'>
        <h3 style='color: #ffffff; 
                margin-bottom: 15px; 
                font-size: 24px;'>Ready to make a prediction?</h3>
        <p style='color: #ecf0f1; 
                font-size: 18px;'>Head over to the Prediction page to get started!</p>
    </div>
    """, unsafe_allow_html=True)