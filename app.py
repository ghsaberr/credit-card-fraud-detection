from fastapi import FastAPI
import pickle
import numpy as np
import pandas as pd

# Loading the trained model
with open("fraud_detection_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Initialize the FastAPI app
app = FastAPI()

# Define the main endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the Fraud Detection API! Use /predict/ to make predictions."}


# Define the prediction endpoint
@app.post("/predict/")
def predict(data: dict):
    features = np.array(data["features"])
    predictions = model.predict(features)
    return {"fraud_predictions": predictions.tolist()}
@app.get("/predict/")
def predict_info():
    return {"message": "Please send a POST request with transaction features to get a prediction. Use /docs/ Swagger UI"}

# Run the API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
