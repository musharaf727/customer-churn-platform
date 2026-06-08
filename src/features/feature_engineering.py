def create_features(df):
    
    df = df.copy()

    df["Charge_Per_Month"] = (
        df["Total Charges"]
        /
        (df["Tenure Months"] + 1)
    )

    df["CLTV_Per_Month"] = (
        df["CLTV"]
        /
        (df["Tenure Months"] + 1)
    )

    return df