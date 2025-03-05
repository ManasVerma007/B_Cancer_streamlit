import numpy as np
import os
import pickle

# Define the path to the pickle file
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../notebook/model.pkl')

class Prediction_Model:
    def __init__(self, data: dict) -> None:
        self.data = data
        self.model = pickle.load(open(model_path, "rb"))
    
    def predict(self) -> bool:
        raw_data = [float(val) for key, val in self.data.items()]
        features = np.array([raw_data])
        return self.model.predict(features)[0]