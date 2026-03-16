import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib

print("Loading dataset...")

# Load dataset
data = pd.read_csv("../dataset/cic_ids_2017_data.csv")

# Remove leading/trailing spaces from column names
data.columns = data.columns.str.strip()

print("Dataset loaded")
print("Columns cleaned")

# Select features useful for anomaly detection
features = [
    "Flow Duration",
    "Total Fwd Packets",
    "Total Backward Packets",
    "Total Length of Fwd Packets",
    "Total Length of Bwd Packets",
    "Flow Bytes/s",
    "Flow Packets/s"
]

print("Selecting features...")

X = data[features]

# Replace infinity values
X.replace([np.inf, -np.inf], np.nan, inplace=True)

# Replace NaN with 0
X.fillna(0, inplace=True)

print("Training Isolation Forest model...")

model = IsolationForest(
    n_estimators=100,
    contamination=0.02,
    random_state=42
)

model.fit(X)

print("Training completed")

# Save model
joblib.dump(model, "../models/brain.joblib")

print("Model saved to models/brain.joblib")