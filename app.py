from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# load our saved model and column list from Colab.
model = joblib.load('house_price_model.pkl')
model_columns = joblib.load('model_columns.pkl')

@app.route('/') # homepage
def home():
    return "App is running!"

if __name__ == '__main__':
    app.run(debug=True)