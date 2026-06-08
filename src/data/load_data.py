import pandas as pd

def load_data():

    df = pd.read_excel(
        "data/raw/Telco_Churn.xlsx"
    )

    return df


if __name__ == "__main__":

    df = load_data()

    print(df.head())