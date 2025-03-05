import numpy as np
import os
import pickle
import pandas as pd

model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../notebook/model.pkl')

class Prediction_Model:
    def __init__(self, data: dict) -> None:
        self.data = data
        self.model = pickle.load(open(model_path, "rb"))
    
    def predict(self) -> bool:
        # Create a pandas DataFrame with proper feature names
        # This helps avoid the feature name warnings
        ordered_features = [
            'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
            'radius_se', 'texture_se', 'perimeter_se', 'area_se',
            'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst'
        ]
        
        # Create feature data in the correct order
        feature_values = []
        for feature in ordered_features:
            if feature in self.data:
                feature_values.append(float(self.data[feature]))
            else:
                # Handle missing features with a default value (0.0)
                feature_values.append(0.0)
        
        # Create dataframe with named columns to avoid warnings
        features_df = pd.DataFrame([feature_values], columns=ordered_features)
        
        # Make prediction using the dataframe
        return self.model.predict(features_df)[0]