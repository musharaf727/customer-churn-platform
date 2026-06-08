import streamlit as st
import pandas as pd

from utils.api_client import batch_predict

st.title(
    "Batch Prediction"
)

uploaded = st.file_uploader(
    "Upload CSV"
)

if uploaded:

    df = pd.read_csv(
        uploaded
    )

    st.dataframe(df.head())

    if st.button(
        "Run Predictions"
    ):

        predictions = batch_predict(
            df
        )

        result_df = pd.DataFrame(
            predictions
        )

        st.dataframe(
            result_df
        )
        
csv = result_df.to_csv(
    index=False
)

st.download_button(
    "Download Results",
    csv,
    "predictions.csv"
)