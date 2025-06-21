from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import pickle

api = FastAPI()

# Load the trained model
with open("Linear_regression_housing_case_study.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Define the expected input structure
class ModelInput(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    stories: int
    mainroad: int         # 1 if yes, 0 if no
    guestroom: int        # 1 if yes, 0 if no
    hotwaterheating: int  # 1 if yes, 0 if no
    airconditioning: int  # 1 if yes, 0 if no
    parking: int
    prefarea: int         # 1 if yes, 0 if no

@api.post("/predict")
def predict(input_data: ModelInput):
    try:
        # Convert input to a NumPy array and reshape for prediction
        features = np.array([[
            input_data.area,
            input_data.bedrooms,
            input_data.bathrooms,
            input_data.stories,
            input_data.mainroad,
            input_data.guestroom,
            input_data.hotwaterheating,
            input_data.airconditioning,
            input_data.parking,
            input_data.prefarea
        ]])

        # Make prediction
        prediction = model.predict(features)
        return {"predicted_price": int(prediction[0])}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {e}")
