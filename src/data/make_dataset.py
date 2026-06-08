from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

raw_file = BASE_DIR / "data" / "raw" / "Telco_Churn.xlsx"

processed_dir = BASE_DIR / "data" / "processed"
processed_dir.mkdir(exist_ok=True)

df = pd.read_excel(raw_file)

print("Original Shape:", df.shape)

df.to_csv(
    processed_dir / "train.csv",
    index=False
)

print("Saved:")
print(processed_dir / "train.csv")