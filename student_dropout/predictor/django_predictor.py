import json
import os

class DropoutPredictor:
    def __init__(self):
        self.thresholds = {
            'jee_main_score': 200,  # example threshold
            'attendance': 75,
            'cgpa': 6.0
        }
    
    def predict(self, input_data):
        try:
            # Simple rule-based prediction
            score = float(input_data.get('jee_main_score', 0))
            attendance = float(input_data.get('attendance', 0))
            cgpa = float(input_data.get('cgpa', 0))
            
            # Predict dropout if any condition is met
            if (score < self.thresholds['jee_main_score'] or 
                attendance < self.thresholds['attendance'] or 
                cgpa < self.thresholds['cgpa']):
                return True  # Likely to dropout
            return False  # Not likely to dropout
        except (ValueError, TypeError):
            return False