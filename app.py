from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the trained model and column structure
model = joblib.load('house_price_model.pkl')
model_columns = joblib.load('model_columns.pkl')

# Extract the list of area names from the column names (strip "Area_" prefix)
areas = sorted([col.replace('Area_', '') for col in model_columns if col.startswith('Area_')])

@app.route('/')
def home():
    return render_template('index.html', areas=areas, prediction=None, errors=None, form_data=None)

@app.route('/predict', methods=['POST'])
def predict():
    # Get form inputs
    bedrooms = float(request.form['bedrooms'])
    bathrooms = float(request.form['bathrooms'])
    size_min = float(request.form['sizeMin'])
    area = request.form['area']
    furnishing = request.form['furnishing']

    # Server-side validation — reject unrealistic or missing values
    errors = []
    if bedrooms < 0 or bedrooms > 15:
        errors.append("Bedrooms must be between 0 and 15.")
    if bathrooms <= 0 or bathrooms > 15:
        errors.append("Bathrooms must be between 1 and 15.")
    if size_min < 100 or size_min > 50000:
        errors.append("Size must be between 100 and 50,000 sqft.")

    if errors:
        return render_template('index.html', areas=areas, prediction=None, errors=errors, form_data=request.form)

    # Build a single row matching the model's expected columns, all zeros to start
    input_data = pd.DataFrame([[0] * len(model_columns)], columns=model_columns)

    # Fill in the numeric values
    input_data['bedrooms'] = bedrooms
    input_data['bathrooms'] = bathrooms
    input_data['sizeMin'] = size_min

    # Set the matching one-hot column to 1. One area name was dropped during training
    # as the baseline category — if the user picks that one, no column needs setting.
    area_col = f'Area_{area}'
    if area_col in input_data.columns:
        input_data[area_col] = 1

    if furnishing == 'PARTLY':
        input_data['furnishing_PARTLY'] = 1
    elif furnishing == 'YES':
        input_data['furnishing_YES'] = 1

    # Predict (model was trained on log price, so convert back)
    log_prediction = model.predict(input_data)[0]
    predicted_price = np.exp(log_prediction)

    formatted_price = f"AED {predicted_price:,.0f}"

    return render_template('index.html', areas=areas, prediction=formatted_price, errors=None, form_data=request.form)

if __name__ == '__main__':
    app.run(debug=True)