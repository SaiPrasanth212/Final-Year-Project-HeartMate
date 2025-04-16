"""
Heart Mate - Heart Attack Risk Prediction Web Application
"""

import os
import numpy as np
import pickle
import logging
from flask import Flask, request, render_template, flash, redirect, url_for

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask application
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "heart-mate-secret-key")

# Load the ML model
try:
    model = pickle.load(open('model.pkl', 'rb'))
    logging.info("Model loaded successfully")
except Exception as e:
    logging.error(f"Error loading model: {e}")
    model = None

@app.route('/')
def home():
    """Render the home page with the prediction form"""
    return render_template('index.html', show_glossary=True)

@app.route('/predict', methods=['POST'])
def predict():
    """Process form data and make a prediction"""
    try:
        if model is None:
            flash("Error: Model not loaded. Please try again later.", "danger")
            return render_template('index.html', show_glossary=True)
        
        # Get form data
        features = []
        
        # Validate and collect form inputs
        required_fields = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 
                          'restecg', 'thalach', 'exang', 'oldpeak', 
                          'slope', 'ca', 'thal']
        
        # Check if all required fields are present
        for field in required_fields:
            if field not in request.form:
                flash(f"Missing required field: {field}", "danger")
                return render_template('index.html', show_glossary=True)
            
            # Try to convert to float
            try:
                value = float(request.form[field])
                features.append(value)
            except ValueError:
                flash(f"Invalid value for {field}. Please enter a number.", "danger")
                return render_template('index.html', show_glossary=True)
        
        # Convert features to numpy array
        array_features = np.array(features).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(array_features)
        
        # Determine result message based on prediction
        if prediction[0] == 1:
            result = "The patient is not likely to have heart attack!"
            result_class = "success"
        else:
            result = "The patient is likely to have heart attack!"
            result_class = "danger"
        
        # Pass show_glossary=False to hide the glossary after prediction
        return render_template('index.html', result=result, result_class=result_class, show_glossary=False)
    
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        flash(f"An error occurred: {str(e)}", "danger")
        return render_template('index.html', show_glossary=True)

if __name__ == '__main__':
    # Run the application on host 0.0.0.0 and port 4678 (as requested)
    app.run(host='0.0.0.0', port=4678, debug=True)