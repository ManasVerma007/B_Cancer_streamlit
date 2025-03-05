# Breast Cancer Prediction Web App

An interactive web application for predicting breast cancer malignancy based on tumor characteristics using machine learning.

## Features

- **AI-Powered Predictions**: Uses a Random Forest Classifier trained on the Wisconsin Breast Cancer Dataset to detect malignant vs benign tumors with ~96% accuracy
- **Interactive UI**: User-friendly interface built with Streamlit for inputting tumor measurements
- **Visual Results**: Clear presentation of prediction results with probability indicators
- **Downloadable Reports**: Generate and download detailed PDF reports of predictions
- **Responsive Design**: Adapts to both light and dark themes

## Live Demo

Access the live application at: [http://13.48.43.30:8501/](http://13.48.43.30:8501/)

## Technology Stack

- **Frontend**: Streamlit
- **Machine Learning**: scikit-learn (Random Forest Classifier)
- **Data Processing**: pandas, numpy
- **Reporting**: FPDF
- **Deployment**: AWS EC2
 
## Requirements

For complete requirements, see `requirements.txt`.

## Usage

1. Navigate to the app URL
2. Input tumor measurements on the "Make Prediction" page
3. View the prediction results and download PDF reports