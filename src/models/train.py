import mlflow
import pandas as pd
import joblib

from pathlib import Path
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

BASE_DIR = Path(__file__).resolve().parents[2]

data_path = BASE_DIR / "data" / "processed" / "train.csv"

print("Loading:", data_path)

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

excel_path = BASE_DIR / "data" / "raw" / "Telco_Churn.xlsx"

print(f"Loading: {excel_path}")

df = pd.read_excel(excel_path)

X = df.drop("Churn Value", axis=1)
y = df["Churn Value"]

X = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = XGBClassifier(
    n_estimators=300,
    max_depth=5,
    learning_rate=0.05,
    random_state=42
)

with mlflow.start_run():

    model.fit(X_train, y_train)

    pred = model.predict_proba(X_test)[:, 1]

    auc = roc_auc_score(y_test, pred)

    mlflow.log_param("n_estimators", 300)
    mlflow.log_param("max_depth", 5)
    mlflow.log_param("learning_rate", 0.05)

    mlflow.log_metric("roc_auc", auc)

    print(f"ROC-AUC Score: {auc:.4f}")

Path("artifacts").mkdir(exist_ok=True)

joblib.dump(model, "artifacts/model.pkl")
joblib.dump(X.columns.tolist(), "artifacts/features.pkl")

print("Model saved successfully.")