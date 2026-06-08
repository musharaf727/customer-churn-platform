import shap
import joblib

from models.train import X_test

model = joblib.load(
    "artifacts/model.pkl"
)

explainer = shap.TreeExplainer(
    model
)

shap_values = explainer.shap_values(
    X_test
)

shap.summary_plot(
    shap_values,
    X_test
)