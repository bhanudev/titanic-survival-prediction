# Titanic Survival Prediction

This is a machine learning web app that predicts whether a passenger survived the Titanic disaster based on some input features like sex, age, number of siblings/spouses aboard, and fare paid.

The app is built with **Streamlit** for the frontend and **Python** for the prediction logic.

---

## Features

- Input passenger details via a user-friendly web interface
- Real-time prediction of survival probability
- Simple, clean UI with Streamlit

---

## Tech Stack

- Python 3.x
- Streamlit
- Pandas
- Scikit-learn (for the prediction model)
- [Add any other libraries you used]

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/bhanudev/titanic-survival-prediction.git
   cd titanic-survival-prediction


python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt

streamlit run app/streamlit_app.py

Project Structure

titanic-survival-prediction/

│
├── app/
│   ├── streamlit_app.py       
│   └── predict.py             
│
├── model/                     
├── data/                      
├── notebooks/                 
├── requirements.txt           
└── README.md
