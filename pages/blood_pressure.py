import streamlit as st
import requests

st.set_page_config(page_title="💉 Blood Pressure")

st.title("💉 Blood Pressure")

if "access_token" not in st.session_state or st.session_state.access_token is None:
    st.error("Please login first from the Login page.")
    st.stop()

systolic = st.number_input("Systolic", min_value=80, max_value=200, value=120)
diastolic = st.number_input("Diastolic", min_value=60, max_value=140, value=80)

if st.button("Submit"):
    try:
        headers = {"Authorization": f"Bearer {st.session_state.access_token}"}
        response = requests.post(
            "http://127.0.0.1:8001/blood_pressure/submit",
            json={"systolic": systolic, "diastolic": diastolic},
            headers=headers
        )
        data = response.json()
        st.success(f"BP Status: {data.get('status')}")
    except Exception as e:
        st.error(f"Error: {e}")

