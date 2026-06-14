# Electric Vehicle Range Prediction

## Project Overview

This project uses Machine Learning to predict the electric driving range of electric vehicles based on vehicle characteristics such as manufacturer, model, vehicle type, model year, and CAFV eligibility.

The project follows a complete Data Science workflow including:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training
- Model Comparison
- Feature Importance Analysis
- Model Validation
- Streamlit Deployment

---

## Dataset

Dataset: Electric Vehicle Population Data

The dataset contains information about electric vehicles, including:

- Make
- Model
- Model Year
- Electric Vehicle Type
- Electric Range
- CAFV Eligibility

---

## Data Cleaning

The following cleaning steps were performed:

- Handled missing values
- Removed duplicates
- Standardized column names
- Optimized data types
- Created a clean modeling dataset

---

## Exploratory Data Analysis (EDA)

EDA included:

- Dataset overview
- Summary statistics
- Distribution analysis
- Correlation analysis
- Outlier analysis

---

## Feature Engineering

Additional features were created, including:

- Vehicle Age
- Encoded categorical variables
- Model-ready feature matrix

---

## Machine Learning Models Tested

The following models were trained and evaluated:

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor
4. Gradient Boosting Regressor

---

## Best Model

Random Forest Regressor was selected as the final model because it achieved the best predictive performance.

Performance:

- MSE: 13.88
- R² Score: 0.9977

---

## Feature Importance

The most important features identified by the model were:

1. Vehicle Age
2. Model Year
3. Electric Vehicle Type (PHEV)
4. Vehicle Model
5. Manufacturer

These features contributed most strongly to electric range prediction.

---

## Model Validation

The saved model was reloaded and validated successfully.

Validation confirmed that predictions from the saved model matched the original model predictions.

---

## Streamlit Application

A Streamlit application was created to allow users to:

- Select vehicle characteristics
- Generate electric range predictions
- Use dynamic Make → Model dropdowns
- Interact with the trained machine learning model

---

## Project Files

- EV_Range_prediction_Workflow.ipynb
- app.py
- best_random_forest_ev_model_corrected.pkl
- categories.json
- feature_columns.json
- requirements.txt

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Joblib
- Streamlit

---

## Author

Martin Jamed