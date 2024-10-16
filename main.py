from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

class InputData(BaseModel):
    feature1: float
    feature2: float
    # Add more features as needed

model = joblib.load("model.pkl")

@app.post("/predict")
def predict(data: InputData):
    input_data = [[data.feature1, data.feature2]]
    prediction = model.predict(input_data)
    return {"prediction": prediction[0]}
