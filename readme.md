# Breast Cancer Prediction Web App

An interactive web application for predicting breast cancer malignancy based on tumor characteristics using machine learning.

## Features

- **AI-Powered Predictions**: Uses a Logistic Regression trained on the Wisconsin Breast Cancer Dataset to detect malignant vs benign tumors with ~96% accuracy
- **Interactive UI**: User-friendly interface built with Streamlit for inputting tumor measurements
- **Visual Results**: Clear presentation of prediction results with probability indicators
- **Downloadable Reports**: Generate and download detailed PDF reports of predictions
- **Responsive Design**: Adapts to both light and dark themes

## Live Demo

Access the live application at: [https://cancer-prediction.duckdns.org/](https://cancer-prediction.duckdns.org/)

## Technology Stack

- **Frontend**: Streamlit
- **Machine Learning**: scikit-learn (Logistic Regression)
- **Data Processing**: pandas, numpy
- **Reporting**: FPDF
- **Deployment**: AWS EC2
- **HTTPS**:  Let's Encrypt certificates
- **Domain Management**: DuckDNS
 
## Requirements

For complete requirements, see `requirements.txt`.

## Usage

1. Navigate to the app URL
2. Input tumor measurements on the "Make Prediction" page
3. View the prediction results and download PDF reports
