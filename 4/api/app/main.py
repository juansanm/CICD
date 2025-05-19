# Niveles/4/api/app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

model = joblib.load("app/model.pkl")
app = FastAPI()

REQUEST_COUNT = Counter("predict_requests_total", "Total prediction requests")

class InputData(BaseModel):
    data: list

@app.post("/predict")
def predict(input: InputData):
    REQUEST_COUNT.inc()
    prediction = model.predict([input.data])
    return {"prediction": prediction.tolist()}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
