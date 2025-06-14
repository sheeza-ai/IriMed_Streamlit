import streamlit as st
import requests

st.title("🩺 Blood Pressure Input")
systolic = st.number_input("Systolic", min_value=80, max_value=200, value=120)
diastolic = st.number_input("Diastolic", min_value=60, max_value=140, value=80)

if st.button("Submit"):
    try:
        response = requests.post("http://127.0.0.1:8001/blood_pressure/submit", json={
    "systolic": systolic,
    "diastolic": diastolic
})

        st.success("Blood pressure submitted successfully!")
    except Exception as e:
        st.error(f"Submission failed: {e}")