import streamlit as st
import pandas as pd

from utils.api_client import batch_predict

# --------------------------------------------------
# PAGE TITLE
# --------------------------------------------------

st.title("Batch Churn Prediction")

st.markdown(
    """
    Upload a CSV file containing customer data
    and predict churn for all customers.
    """
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "result_df" not in st.session_state:
    st.session_state.result_df = None

# --------------------------------------------------
# FILE UPLOAD
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Customer CSV",
    type=["csv"]
)

# --------------------------------------------------
# DISPLAY INPUT DATA
# --------------------------------------------------

if uploaded_file is not None:

    try:

        df = pd.read_csv(uploaded_file)

        st.subheader("Uploaded Data")

        st.dataframe(
            df.head(),
            use_container_width=True
        )

        st.write(
            f"Total Records: {len(df)}"
        )

        # ------------------------------------------
        # PREDICT BUTTON
        # ------------------------------------------

        if st.button("Run Predictions"):

            with st.spinner(
                "Generating predictions..."
            ):

                predictions = batch_predict(df)

                result_df = pd.DataFrame(
                    predictions
                )

                # Save permanently
                st.session_state.result_df = (
                    result_df
                )

                st.success(
                    "Predictions completed successfully!"
                )

    except Exception as e:

        st.error(
            f"Error reading file: {str(e)}"
        )

# --------------------------------------------------
# DISPLAY RESULTS
# --------------------------------------------------

if st.session_state.result_df is not None:

    result_df = st.session_state.result_df

    st.subheader("Prediction Results")

    st.dataframe(
        result_df,
        use_container_width=True
    )

    # ------------------------------------------
    # RISK SEGMENTATION
    # ------------------------------------------

    if "churn_probability" in result_df.columns:

        high_risk = len(
            result_df[
                result_df[
                    "churn_probability"
                ] > 0.7
            ]
        )

        medium_risk = len(
            result_df[
                (
                    result_df[
                        "churn_probability"
                    ] > 0.3
                )
                &
                (
                    result_df[
                        "churn_probability"
                    ] <= 0.7
                )
            ]
        )

        low_risk = len(
            result_df[
                result_df[
                    "churn_probability"
                ] <= 0.3
            ]
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "High Risk",
            high_risk
        )

        col2.metric(
            "Medium Risk",
            medium_risk
        )

        col3.metric(
            "Low Risk",
            low_risk
        )

    # ------------------------------------------
    # DOWNLOAD BUTTON
    # ------------------------------------------

    csv = result_df.to_csv(
        index=False
    )

    st.download_button(
        label="Download Predictions",
        data=csv,
        file_name="churn_predictions.csv",
        mime="text/csv"
    )