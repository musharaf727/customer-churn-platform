import pandas as pd
from pathlib import Path

from evidently import Report
from evidently.presets import DataDriftPreset

BASE_DIR = Path(__file__).resolve().parents[2]

train_df = pd.read_csv(
    BASE_DIR / "data" / "processed" / "train.csv"
)

new_df = pd.read_csv(
    BASE_DIR / "data" / "processed" / "new_data.csv"
)

report = Report(
    metrics=[
        DataDriftPreset()
    ]
)

report.run(
    reference_data=train_df,
    current_data=new_df
)

report.save_html(
    BASE_DIR / "reports" / "drift.html"
)