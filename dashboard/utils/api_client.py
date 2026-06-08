import requests

API_URL = "https://churn-api-ghze.onrender.com"


def predict_customer(customer):

    response = requests.post(
        f"{API_URL}/predict",
        json=customer
    )

    return response.json()


def batch_predict(df):

    response = requests.post(
        f"{API_URL}/batch_predict",
        json=df.to_dict(
            orient="records"
        )
    )

    return response.json()