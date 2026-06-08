from pathlib import Path
import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]

MODEL_PATH = BASE_DIR / "artifacts" / "model.pkl"
FEATURES_PATH = BASE_DIR / "artifacts" / "features.pkl"

model = joblib.load(MODEL_PATH)
features = joblib.load(FEATURES_PATH)


def predict(data: dict):

    df = pd.DataFrame([data])

    df = pd.get_dummies(df)

    df = df.reindex(
        columns=features,
        fill_value=0
    )

    probability = model.predict_proba(df)[0][1]

    return probability