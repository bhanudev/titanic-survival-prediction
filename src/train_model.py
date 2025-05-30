import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load data
df = pd.read_csv("data/train.csv",delimiter='\t')
df = df[["Pclass", "Sex", "Age", "SibSp", "Fare", "Survived"]].dropna()
df["Sex"] = df["Sex"].map({"male": 1, "female": 0})

# Features and target
X = df.drop("Survived", axis=1)
y = df["Survived"]

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(model, os.path.join("model", "model.pkl"))
