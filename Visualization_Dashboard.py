import streamlit as st
import requests
import pandas as pd

# Define the FastAPI endpoint
API_URL = "http://127.0.0.1:8000/predict"  # Replace with actual URL if deployed

# App title
st.title("🏠 Housing Price Prediction Dashboard")

st.markdown("Enter housing features below to get a predicted price:")

# Input fields for all features
area = st.number_input("Area (sq ft)", value=3000)
bedrooms = st.number_input("Number of Bedrooms", min_value=0, value=3)
bathrooms = st.number_input("Number of Bathrooms", min_value=0, value=2)
stories = st.number_input("Number of Stories", min_value=1, value=2)
mainroad = st.selectbox("Main Road Access", ["Yes", "No"])
guestroom = st.selectbox("Guest Room", ["Yes", "No"])
hotwaterheating = st.selectbox("Hot Water Heating", ["Yes", "No"])
airconditioning = st.selectbox("Air Conditioning", ["Yes", "No"])
parking = st.number_input("Number of Parking Spots", min_value=0, value=1)
prefarea = st.selectbox("Preferred Area", ["Yes", "No"])

# Convert categorical inputs to binary
mainroad_val = 1 if mainroad == "Yes" else 0
guestroom_val = 1 if guestroom == "Yes" else 0
hotwater_val = 1 if hotwaterheating == "Yes" else 0
aircon_val = 1 if airconditioning == "Yes" else 0
prefarea_val = 1 if prefarea == "Yes" else 0

# Input data dictionary
input_data = {
    "area": area,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "stories": stories,
    "mainroad": mainroad_val,
    "guestroom": guestroom_val,
    "hotwaterheating": hotwater_val,
    "airconditioning": aircon_val,
    "parking": parking,
    "prefarea": prefarea_val
}

# Show input summary as a table
st.subheader("🔎 Feature Summary")
st.dataframe(pd.DataFrame([input_data]))

# Button to make prediction
if st.button("Predict Price 💰"):
    try:
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"🏷️ Predicted House Price: ₹{result['predicted_price']:,}")
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Connection error: {e}")
