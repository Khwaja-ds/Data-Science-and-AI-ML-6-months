import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load(r"C:\Users\HP\Downloads\Projects\Heart Disease Predictor\KNN_heart.pkl")
scaler = joblib.load(r"C:\Users\HP\Downloads\Projects\Heart Disease Predictor\scaler.pkl")
expected_columns = joblib.load(r"C:\Users\HP\Downloads\Projects\Heart Disease Predictor\columns.pkl")

# App Title
st.title("Heart Disease Predictor")
st.subheader("Heart Stroke Prediction by Akarsh")
st.markdown("This app predicts the presence of heart disease based on user input.")

# Collect user input
age = st.slider("Age", 18, 100, 40)
sex = st.selectbox("Sex", ["M", "F"])
chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_hr = st.slider("Max Heart Rate", 60, 220, 150)
exercise_angina = st.selectbox("Exercise-Induced Angina", ["Y", "N"])
oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

# Predict button
if st.button("Predict"):

    # Create input dictionary
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    # Convert to DataFrame
    input_df = pd.DataFrame([raw_input])

    # Add missing columns with 0
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder to match training
    input_df = input_df[expected_columns]

    # Scale input
    scaled_input = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(scaled_input)[0]
    probability = model.predict_proba(scaled_input)[0][1] * 100

    # Show result
    if prediction == 1:
        st.error(f"⚠️ High Risk of Heart Disease (Probability: {probability:.2f}%)")
    else:
        st.success(f"✅ Low Risk of Heart Disease (Probability: {probability:.2f}%)")
