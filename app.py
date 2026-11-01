import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Customer Churn Predictor")
st.title("Customer Churn Prediction")
st.write("Enter customer details to predict whether they will leave.")

@st.cache_resource
def load_files():
    model = joblib.load("churn_best_model.joblib")
    columns = joblib.load("churn_columns.joblib")
    return model, columns

model, columns = load_files()

senior = st.selectbox("Senior citizen", ["No", "Yes"])
tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, value=12)
monthly = st.number_input("Monthly charges", min_value=0.0, value=70.0)
total = st.number_input("Total charges", min_value=0.0, value=840.0)
gender = st.selectbox("Gender", ["Female", "Male"])
partner = st.selectbox("Partner", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["No", "Yes"])
phone = st.selectbox("Phone service", ["No", "Yes"])
internet = st.selectbox("Internet service", ["DSL", "Fiber optic", "No"])
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])

def set_flag(row, name):
    if name in row:
        row[name] = 1

if st.button("Predict"):
    row = {col: 0 for col in columns}
    row["SeniorCitizen"] = 1 if senior == "Yes" else 0
    row["tenure"] = tenure
    row["MonthlyCharges"] = monthly
    row["TotalCharges"] = total
    if gender == "Male":
        set_flag(row, "gender_Male")
    if partner == "Yes":
        set_flag(row, "Partner_Yes")
    if dependents == "Yes":
        set_flag(row, "Dependents_Yes")
    if phone == "Yes":
        set_flag(row, "PhoneService_Yes")
    if internet == "Fiber optic":
        set_flag(row, "InternetService_Fiber optic")
    if internet == "No":
        set_flag(row, "InternetService_No")
    if contract == "One year":
        set_flag(row, "Contract_One year")
    if contract == "Two year":
        set_flag(row, "Contract_Two year")
    input_df = pd.DataFrame([row])[columns]
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]
    if prediction == 1:
        st.error(f"Likely to churn ({probability:.0%} probability).")
    else:
        st.success(f"Likely to stay ({probability:.0%} churn probability).")