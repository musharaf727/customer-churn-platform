import pandas as pd

DROP_COLUMNS = [

    "CustomerID",
    "Count",
    "Country",
    "State",
    "City",
    "Zip Code",
    "Lat Long",
    "Latitude",
    "Longitude",
    "Churn Label",
    "Churn Score",
    "Churn Reason"
]

def preprocess(df):

    df = df.copy()

    df.drop(
        columns=DROP_COLUMNS,
        inplace=True
    )

    return df