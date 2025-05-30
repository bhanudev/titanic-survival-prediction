import streamlit as st
import pandas as pd
from predict import predict_survival

st.title("Titanic Survival Prediction")

# Input fields
pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.slider("Age", 0, 100, 25)
sibsp = st.number_input("Number of Siblings/Spouses Aboard", 0, 10, 0)
fare = st.number_input("Fare Paid", 0.0, 600.0, 50.0)

# Predict button
if st.button("Predict Survival"):
    result = predict_survival(pclass, sex, age, sibsp, fare)
    if result == 1:
        st.success("🎉 Likely to survive")
    else:
        st.error("💀 Not likely to survive")
