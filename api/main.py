from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
import os

app = FastAPI(title="Unemployment Analysis API")

# Setup CORS to allow the frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model pipeline
# We assume the backend is run from the project root or the model is placed correctly
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.joblib")
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    model = None

class PredictionRequest(BaseModel):
    Region: str
    Frequency: str = " Monthly"
    Employed: float
    Labour_participation: float
    Area: str
    Month: int = 6
    Year: int = 2020

class PredictionResponse(BaseModel):
    Unemployment_rate: float

@app.get("/api")
@app.get("/")
def read_root():
    return {"message": "Unemployment Analysis API is running.", "status": "ok"}

@app.get("/api/health")
@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": model is not None}

@app.post("/api/predict", response_model=PredictionResponse)
@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    if model is None:
        return {"Unemployment_rate": 0.0, "error": "Model not loaded."}
    
    # Convert input to DataFrame
    input_data = pd.DataFrame([{
        "Region": request.Region,
        "Frequency": request.Frequency,
        "Employed": request.Employed,
        "Labour_participation": request.Labour_participation,
        "Area": request.Area,
        "Month": request.Month,
        "Year": request.Year
    }])
    
    prediction = model.predict(input_data)
    
    return {"Unemployment_rate": float(prediction[0])}
