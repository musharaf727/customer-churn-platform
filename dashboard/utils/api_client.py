import requests

API_URL = "http://localhost:8000"


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