import joblib
import json

class DropoutPredictor:
    def __init__(self):
        self.model = joblib.load('dropout_prediction_model.pkl')
        with open('model_config.json', 'r') as f:
            self.config = json.load(f)
    
    def predict(self, input_data):
        # Prepare input in the same order as training features
        features = []
        for feature_name in self.config['feature_names']:
            if feature_name in self.config['categorical_mappings']:
                # Convert categorical input to numerical
                value = str(input_data.get(feature_name, 0))
                features.append(self.config['categorical_mappings'][feature_name].get(value, 0))
            else:
                # Numerical features
                features.append(float(input_data.get(feature_name, 0)))
        
        # Make prediction
        prediction = self.model.predict([features])[0]
        return bool(prediction)
