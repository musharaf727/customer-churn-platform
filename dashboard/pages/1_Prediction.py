import streamlit as st

from utils.api_client import predict_customer

st.title(
    "Customer Churn Prediction"
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

tenure = st.number_input(
    "Tenure Months",
    min_value=0,
    max_value=100,
    value=12
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    max_value=1000.0,
    value=50.0
)

contract = st.selectbox(
    "Contract",
    [
        "Month-to-month",
        "One year",
        "Two year"
    ]
)

if st.button("Predict"):

    customer = {
        "Gender": gender,
        "Tenure Months": tenure,
        "Monthly Charges": monthly_charges,
        "Contract": contract
    }

    result = predict_customer(
        customer
    )

    prob = result[
        "churn_probability"
    ]

    st.metric(
        "Churn Probability",
        f"{prob:.2%}"
    )

    if prob > 0.7:

        st.error(
            "🔴 High Risk Customer"
        )

    elif prob > 0.3:

        st.warning(
            "🟠 Medium Risk Customer"
        )

    else:

        st.success(
            "🟢 Low Risk Customer"
        )