# doctor.py

import streamlit as st
import requests

st.set_page_config(page_title="👨‍⚕️ Doctor")

st.title("👨‍⚕️ Doctor Consultation")

if "access_token" not in st.session_state or st.session_state.access_token is None:
    st.error("Please login first from the Login page.")
    st.stop()

with st.expander("💬 Video Consultation"):
    st.markdown(
        "[Join Video Call](https://meet.jit.si/irimed-consultation-room)",
        unsafe_allow_html=True
    )

with st.form("appointment"):
    name = st.text_input("Name")
    date = st.date_input("Preferred Date")
    time = st.time_input("Preferred Time")
    submit = st.form_submit_button("Book")
    if submit:
        st.success(f"Appointment booked for {name} on {date} at {time}.")

# --- Doctor data view below ---

st.subheader("📊 Patient Results History")

try:
    headers = {"Authorization": f"Bearer {st.session_state.access_token}"}
    response = requests.get(
        "http://127.0.0.1:8001/results/",
        headers=headers
    )
    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])

        if not results:
            st.info("No patient data found yet.")
        else:
            for patient in results:
                st.markdown(f"### 👤 **{patient['patient']}** ({patient.get('email', '')})")

                st.write("👁️ **Iris Scan Results**")
                if patient.get("iris_results"):
                    for iris in patient["iris_results"]:
                        st.write(f"- Class ID: {iris['class_id']} ({iris['confidence']}) at {iris['date']}")
                else:
                    st.write("No iris records.")

                st.write("💉 **Blood Pressure Results**")
                if patient.get("bp_results"):
                    for bp in patient["bp_results"]:
                        st.write(f"- {bp['systolic']}/{bp['diastolic']} at {bp['date']}")
                else:
                    st.write("No BP records.")
                st.markdown("---")
    else:
        st.error("Failed to fetch data from backend.")
except Exception as e:
    st.error(f"Error: {e}")
