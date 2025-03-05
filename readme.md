# Breast Cancer Prediction Web App

This repository contains a web application for predicting breast cancer using machine learning models. The app is built using Python and Jupyter Notebook, and it is hosted on an AWS EC2 instance.

## Features

- **Breast Cancer Prediction**: The app takes input features from users and predicts the likelihood of breast cancer.
- **Machine Learning Model**: Utilizes a trained model built using `scikit-learn` for predictions.
- **Web Interface**: A user-friendly web interface built with `FastAPI` and `Jinja2`.
- **Hosted on EC2**: The application is deployed on an AWS EC2 instance for accessibility. (http://ec2-13-202-161-50.ap-south-1.compute.amazonaws.com:8080/)

 

## Requirements

The required Python packages are listed in `requirements.txt`:

```plaintext
pandas
numpy
scikit-learn
fastapi
uvicorn
jinja2

