import streamlit as st
import pandas as pd
import joblib
import json

# Load model
model = joblib.load("best_random_forest_ev_model_corrected.pkl")

# Load dropdown categories
with open("categories.json", "r") as f:
    categories = json.load(f)

# Load feature columns
with open("feature_columns.json", "r") as f:
    feature_columns = json.load(f)

st.title("Electric Vehicle Range Prediction App")
st.write("This app predicts electric vehicle range using the trained Random Forest model.")

# User inputs
make = st.selectbox("Vehicle Make", categories["make"])
available_models = categories["make_model_map"].get(make, [])

model_name = st.selectbox(
    "Vehicle Model",
    available_models
)
ev_type = st.selectbox("Electric Vehicle Type", categories["electric_vehicle_type"])
cafv = st.selectbox("CAFV Eligibility", categories["cafv_eligibility"])

model_year = st.number_input("Model Year", min_value=1999, max_value=2027, value=2024)
vehicle_age = 2026 - model_year

st.write(f"Calculated Vehicle Age: **{vehicle_age} years**")

# Create empty input row
input_data = pd.DataFrame(0, index=[0], columns=feature_columns)

# Fill numerical features
if "model_year" in input_data.columns:
    input_data["model_year"] = model_year

if "vehicle_age" in input_data.columns:
    input_data["vehicle_age"] = vehicle_age

# Fill encoded categorical features
encoded_values = [
    f"make_{make}",
    f"model_{model_name}",
    f"electric_vehicle_type_{ev_type}",
    f"clean_alternative_fuel_vehicle_(cafv)_eligibility_{cafv}"
]

for col in encoded_values:
    if col in input_data.columns:
        input_data[col] = 1

# Predict
if st.button("Predict Electric Range"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Electric Range: {prediction:.2f} miles")