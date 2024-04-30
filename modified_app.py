import streamlit as st
from PIL import Image
import joblib
import json
import pandas as pd

# Sidebar Options:
SIDEBAR_OPTIONS = ["Introduction", "Predict your Credit Score"]
st.sidebar.subheader("Options:")
selected_option = st.sidebar.selectbox("Select an option:", SIDEBAR_OPTIONS)

def display_intro():
    # Introduction Section
    image = Image.open('Credit_Risk.jpg')
    st.image(image, use_column_width="always")
    st.title("Welcome to the Credit Risk Simulator")
    st.header("Predict Credit Eligibility with Confidence")
    st.subheader("Let's get started...")

def predict_credit_score():
    # Input Section
    st.header("Provide Your Details for Credit Assessment")

    data = {}
    columns = st.columns(2)
    data['person_age'] = columns[0].number_input("Age:", 18, 70)
    data['person_income'] = columns[1].number_input("Annual Income ($):", 1000, 100000)
    data['person_emp_length'] = st.number_input("Employment Length (years):", 1, 50)
    data['loan_amnt'] = st.number_input("Loan Amount ($):", 100, 50000)
    data['loan_percent_income'] = st.number_input("Loan Percent Income (%):", 0, 100)
    data['cb_person_cred_hist_length'] = st.slider("Credit History Length (years):", 0, 50)
    data['person_home_ownership'] = st.selectbox("Home Ownership:", ["RENT", "OWN", "MORTGAGE", "OTHER"])
    data['loan_intent'] = st.selectbox("Loan Intent:", ['EDUCATION', 'MEDICAL', 'VENTURE', 'PERSONAL', 'DEBT CONSOLIDATION', 'HOME IMPROVEMENT'])
    data['loan_grade'] = st.selectbox("Loan Grade:", ['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    data['cb_person_default_on_file'] = st.selectbox("Previous Defaults:", ["No", "Yes"])

    # Display Data
    if st.button("Display Data"):
        data_json = json.dumps(data, indent=4)
        st.write("Input Data (JSON Format):")
        st.code(data_json)
        st.write("Input Data (Tabular Format):")
        st.write(pd.DataFrame(data, index=[0]))

    # Predict Credit Score
    if st.button("Predict Credit Score"):
        input_data = pd.DataFrame([data])
        pipeline = joblib.load('best_pipeline.pkl')
        prediction = pipeline.predict(input_data)
        result = "Risk Assessment: Risky" if prediction[0] else "Risk Assessment: Not Risky"
        st.write("Prediction Result:", result)

# Main
if selected_option == SIDEBAR_OPTIONS[0]:
    display_intro()
elif selected_option == SIDEBAR_OPTIONS[1]:
    predict_credit_score()
