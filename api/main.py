from fastapi import FastAPI

from .prediction import predict

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Customer Churn API"
    }


@app.post("/predict")
def predict_customer(customer: dict):

    probability = predict(customer)

    return {
        "churn_probability": float(probability)
    }