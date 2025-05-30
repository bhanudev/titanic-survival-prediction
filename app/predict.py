import pandas as pd
import joblib
import os

MODEL_PATH = os.path.join("model", "model.pkl")
model = joblib.load(MODEL_PATH)

def predict_survival(pclass, sex, age, sibsp, fare):
    sex = 1 if sex == "male" else 0
    input_data = pd.DataFrame({
        "Pclass": [pclass],
        "Sex": [sex],
        "Age": [age],
        "SibSp": [sibsp],
        "Fare": [fare]
    })
    prediction = model.predict(input_data)[0]
    return prediction
