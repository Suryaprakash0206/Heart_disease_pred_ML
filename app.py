import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("heart_disease_svm.pkl", "rb") as file:
    model = pickle.load(file)


# Page configuration
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️"
)

st.title("❤️ Heart Disease Prediction")
st.write("Enter the patient's information below.")


# Input fields

# =========================
# PATIENT INPUTS
# =========================

# Age
age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=50
)


# Sex
sex = st.selectbox(
    "Sex",
    [0, 1],
    format_func=lambda x: {
        0: "Female",
        1: "Male"
    }[x]
)


# Chest Pain Type
cp = st.selectbox(
    "Chest Pain Type",
    [1, 2, 3, 4],
    format_func=lambda x: {
        1: "Typical Angina",
        2: "Atypical Angina",
        3: "Non-anginal Pain",
        4: "Asymptomatic"
    }[x]
)


# Resting Blood Pressure
trestbps = st.number_input(
    "Resting Blood Pressure (mm Hg)",
    min_value=50,
    max_value=250,
    value=120
)


# Cholesterol
chol = st.number_input(
    "Cholesterol (mg/dl)",
    min_value=50,
    max_value=600,
    value=200
)


# Fasting Blood Sugar
fbs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dl",
    [0, 1],
    format_func=lambda x: {
        0: "No",
        1: "Yes"
    }[x]
)


# Resting ECG
restecg = st.selectbox(
    "Resting ECG",
    [0, 1, 2],
    format_func=lambda x: {
        0: "Normal",
        1: "ST-T Wave Abnormality",
        2: "Left Ventricular Hypertrophy"
    }[x]
)


# Maximum Heart Rate
thalach = st.number_input(
    "Maximum Heart Rate Achieved",
    min_value=50,
    max_value=250,
    value=150
)


# Exercise Induced Angina
exang = st.selectbox(
    "Exercise Induced Angina",
    [0, 1],
    format_func=lambda x: {
        0: "No",
        1: "Yes"
    }[x]
)


# Oldpeak
oldpeak = st.number_input(
    "ST Depression (Oldpeak)",
    min_value=0.0,
    max_value=10.0,
    value=1.0,
    step=0.1
)


# Slope
slope = st.selectbox(
    "Slope of Peak Exercise ST Segment",
    [1, 2, 3],
    format_func=lambda x: {
        1: "Upsloping",
        2: "Flat",
        3: "Downsloping"
    }[x]
)


# Number of Major Vessels
ca = st.selectbox(
    "Number of Major Vessels (CA)",
    [0, 1, 2, 3]
)


# Thal
thal = st.selectbox(
    "Thal",
    [3, 6, 7],
    format_func=lambda x: {
        3: "Normal",
        6: "Fixed Defect",
        7: "Reversible Defect"
    }[x]
)

# Prediction button

if st.button("Predict"):

    # Create input array in the SAME order as training columns
    patient_data = np.array([[
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]])

    # Make prediction
    prediction = model.predict(patient_data)

    if prediction[0] == 1:
        st.error("⚠️ Heart Disease Detected")
    else:
        st.success("✅ No Heart Disease Detected")