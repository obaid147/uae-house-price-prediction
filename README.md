# UAE House Price Prediction

A machine learning web application that estimates property sale prices using property features such as bedrooms, bathrooms, size, area, and furnishing status.

**[Try the Live Demo](https://uae-house-price-prediction.onrender.com/)**

## Project Overview

I built this project to practise the end-to-end machine-learning workflow: cleaning property data, engineering features, training and comparing models, and deploying a prediction web app.

- Dataset: UAE Real Estate 2024 dataset from Kaggle
- Data size: 5,000+ property listings
- Model used in the app: Linear Regression & Random Forest
- Web framework: Python, Flask
- Front end: HTML, CSS
- Deployment: Render

## How It Works

1. **Data cleaning:** handled missing values and inconsistent entries, including studio apartments and values such as `7+`.
2. **Feature engineering:** extracted area names from addresses and grouped locations into the top 50 areas plus `Other`.
3. **Categorical encoding:** converted area and furnishing categories into numeric features using one-hot encoding.
4. **Target transformation:** applied a log transformation to property prices because the price distribution was strongly       right-skewed.
5. **Model comparison:** evaluated Linear Regression and Random Forest.
6. **Deployment:** served predictions through a Flask application hosted on Render.

## Model Results

| Model             | Mean Absolute Error (AED) | R² Score |
| Linear Regression | 1,895,504                 | 0.72     |
| Random Forest     | 1,582,773                 | 0.76     |

The Random Forest model performed better on these evaluation metrics. The MAE is still relatively high, so predictions should be treated as estimates rather than official valuations.

## Tech Stack

- Python
- Pandas and NumPy
- scikit-learn
- Flask
- Joblib
- HTML
- CSS
- Gunicorn
- Google Colab for model training
- Render for deployment
- GitHub for version control

## Run Locally

1. Clone this repository:

   ```bash
   git clone https://github.com/obaid147/uae-house-price-prediction.git
   cd uae-house-price-prediction
   ```

2. Create and activate a virtual environment (recommended).

   **Windows:**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the app:

   ```bash
   python app.py
   ```

5. Open the local URL shown in the terminal, usually `http://127.0.0.1:5000/`.

## Repository Structure

```text
├── app.py                         # Flask application and prediction logic
├── house_price_model.pkl          # Saved trained model
├── model_columns.pkl              # Expected model input columns
├── requirements.txt               # Python dependencies
├── Procfile                       # Gunicorn startup command for deployment
├── templates/
│   └── index.html                 # Web page template
├── static/                        # Static assets
└── uae_house_price_prediction.ipynb # Data preparation and model training notebook
```

## Limitations

- The model is only as reliable as the dataset and features used to train it.
- Property prices can change over time and vary substantially within the same area.
- The result is a machine-learning estimate, not a formal property valuation.

## Links

- **Live app:** https://uae-house-price-prediction.onrender.com/
- **GitHub repository:** https://github.com/obaid147/uae-house-price-prediction
