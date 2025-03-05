import streamlit as st
from views.landing_page import landing_page
from views.prediction_page import prediction_page
from views.results_page import results_page

# Rest of the navigation code remains the same


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


# import streamlit as st
# import numpy as np
# from models.prediction_model import Prediction_Model
# from fpdf import FPDF


# # Define the pages
# def landing_page():
#     st.title("Welcome to the Breast Cancer Prediction App")
#     st.write("""
#     This application helps in predicting whether a breast cancer tumor is malignant or benign based on various features.
#     Please navigate to the 'Prediction' page to input the features and get the prediction result.
#     """)

# def prediction_page():
#     st.title("Breast Cancer Prediction")

#     st.write("Enter the following features:")

#     form_data = {
#         "radius_mean": st.number_input("Radius Mean", help="Mean of distances from center to points on the perimeter"),
#         "texture_mean": st.number_input("Texture Mean", help="Standard deviation of gray-scale values"),
#         "perimeter_mean": st.number_input("Perimeter Mean", help="Mean size of the core tumor"),
#         "area_mean": st.number_input("Area Mean", help="Mean area of the tumor"),
#         "radius_se": st.number_input("Radius SE", help="Standard error for the mean of distances from center to points on the perimeter"),
#         "texture_se": st.number_input("Texture SE", help="Standard error for the standard deviation of gray-scale values"),
#         "perimeter_se": st.number_input("Perimeter SE", help="Standard error for the mean size of the core tumor"),
#         "area_se": st.number_input("Area SE", help="Standard error for the mean area of the tumor"),
#         "radius_worst": st.number_input("Radius Worst", help="Worst or largest mean value of distances from center to points on the perimeter"),
#         "texture_worst": st.number_input("Texture Worst", help="Worst or largest standard deviation of gray-scale values"),
#         "perimeter_worst": st.number_input("Perimeter Worst", help="Worst or largest mean size of the core tumor"),
#         "area_worst": st.number_input("Area Worst", help="Worst or largest mean area of the tumor")
#     }

#     if st.button("Predict"):
#         model = Prediction_Model(form_data)
#         result = "Malignant" if model.predict() == 1 else "Benign"
#         st.session_state['result'] = result
#         st.session_state['form_data'] = form_data
#         st.session_state['page'] = 'Result'
#         st.rerun()


# def results_page():
#     st.title("Prediction Result")
#     if 'result' in st.session_state:
#         result = st.session_state['result']
#         form_data = st.session_state['form_data']
        
#         # Create two columns for better layout
#         col1, col2 = st.columns([1, 2])
        
#         # Display prediction result with custom styling
#         with col1:
#             st.markdown("### Diagnosis")
#             if result == "Malignant":
#                 st.markdown(
#                     f"""
#                     <div style='background-color: #FFA07A; padding: 20px; border-radius: 10px; text-align: center'>
#                         <h2 style='color: #8B0000;'>{result}</h2>
#                     </div>
#                     """, 
#                     unsafe_allow_html=True
#                 )
#             else:
#                 st.markdown(
#                     f"""
#                     <div style='background-color: #90EE90; padding: 20px; border-radius: 10px; text-align: center'>
#                         <h2 style='color: #006400;'>{result}</h2>
#                     </div>
#                     """, 
#                     unsafe_allow_html=True
#                 )

#         # Display feature values in an organized way
#         with col2:
#             st.markdown("### Input Features")
#             # Create three columns for feature display
#             features_col1, features_col2, features_col3 = st.columns(3)
            
#             # Organize features by type
#             mean_features = {k:v for k,v in form_data.items() if 'mean' in k}
#             se_features = {k:v for k,v in form_data.items() if 'se' in k}
#             worst_features = {k:v for k,v in form_data.items() if 'worst' in k}
            
#             with features_col1:
#                 st.markdown("**Mean Values**")
#                 for key, value in mean_features.items():
#                     st.metric(label=key.replace('_mean', '').title(), value=f"{value:.2f}")
                    
#             with features_col2:
#                 st.markdown("**SE Values**")
#                 for key, value in se_features.items():
#                     st.metric(label=key.replace('_se', '').title(), value=f"{value:.2f}")
                    
#             with features_col3:
#                 st.markdown("**Worst Values**")
#                 for key, value in worst_features.items():
#                     st.metric(label=key.replace('_worst', '').title(), value=f"{value:.2f}")
        
#         # Add some space before the download button
#         st.markdown("---")
        
#         # Center-align the download button
#         col1, col2, col3 = st.columns([1, 2, 1])
#         with col2:
#             # Create PDF download button (keeping your existing PDF generation code)
#             def create_pdf():
#                 pdf = FPDF()
#                 pdf.add_page()
#                 pdf.set_font("Arial", size=12)
#                 pdf.cell(200, 10, txt="Breast Cancer Prediction Results", ln=1, align='C')
#                 pdf.ln(10)
#                 pdf.cell(200, 10, txt=f"Prediction Result: {result}", ln=1, align='L')
#                 pdf.ln(5)
#                 pdf.cell(200, 10, txt="Input Features:", ln=1, align='L')
#                 for key, value in form_data.items():
#                     pdf.cell(200, 10, txt=f"{key}: {value}", ln=1, align='L')
#                 return pdf.output(dest='S').encode('latin-1')
            
#             st.download_button(
#                 label="📥 Download Report as PDF",
#                 data=create_pdf(),
#                 file_name="breast_cancer_prediction_results.pdf",
#                 mime="application/pdf"
#             )
#     else:
#         st.info("No prediction made yet. Please go to the 'Prediction' page to input features and get a prediction.")


# # Define the navigation
# st.sidebar.title("Navigation")
# if 'page' not in st.session_state:
#     st.session_state['page'] = 'Home'

# page = st.sidebar.radio("Go to", ["Home", "Prediction", "Result"], index=["Home", "Prediction", "Result"].index(st.session_state['page']))

# if page == "Home":
#     landing_page()
# elif page == "Prediction":
#     prediction_page()
# elif page == "Result":
#     results_page()

# if st.session_state['page'] != page:
#     st.session_state['page'] = page
#     st.rerun()  # Changed from st.experimental_rerun()

