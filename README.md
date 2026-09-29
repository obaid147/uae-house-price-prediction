🔴 Live Demo

Try it here :- https://uae-house-price-prediction.onrender.com/

Project Overview

Predicts Dubai property sale prices using a Random Forest model trained on 5,000+ real listings (bedrooms, bathrooms, size, location, furnishing). Deployed as a Flask web app so anyone can get an instant estimate.

Approach
Data Cleaning — handled missing values, fixed inconsistent text entries (e.g. "7+", "studio"), cleaned size field
Feature Engineering — extracted neighborhood/area from address text, grouped into top 50 areas + "Other", one-hot encoded categoricals
Log-Transformed Target — price data was heavily right-skewed (luxury listings up to 199M AED); log-transforming the target significantly improved model accuracy
Models Trained & Compared:
Model	MAE (AED)	R²
Linear Regression	1,895,504	0.72
Random Forest	1,582,773	0.76
Deployment — Flask app with server + client-side input validation, deployed on Render
Tech Stack
Python, Pandas, NumPy, scikit-learn
Flask, gunicorn
Google Colab (training), Render (deployment)
Dataset

UAE Real Estate 2024 Dataset (Kaggle)

(Note: hosted on Render's free tier — the app may take ~30-60 seconds to wake up if it hasn't been visited recently.)