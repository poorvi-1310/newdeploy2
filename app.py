import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('home_price_model.pkl')

# App Title
st.set_page_config(page_title="Home Price Predictor", page_icon="🏠")
st.title("🏠 Home Price Prediction App")
st.write("Enter the details below to predict the house price:")

# Input fields
area = st.number_input("Area (in square feet)", min_value=500, max_value=10000, step=100)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, step=1)
age = st.number_input("Age of the Property (in years)", min_value=0, max_value=100, step=1)

# Predict Button
if st.button("Predict Price"):
    input_data = np.array([[area, bedrooms, age]])
    prediction = model.predict(input_data)
    st.success(f"Estimated Home Price: ₹ {prediction[0]:,.2f}")
