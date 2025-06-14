
import streamlit as st
import requests

st.set_page_config(page_title="IriMed - Iris Health Scanner", layout="centered")

st.title("👁️ IriMed - Iris Health Scanner")
st.markdown("Upload an iris image to detect diabetic retinopathy.")

# Image upload
uploaded_file = st.file_uploader("Choose an iris image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    if st.button("Analyze"):
        with st.spinner("Sending to backend..."):
            files = {"file": uploaded_file.getvalue()}
            try:
                # Replace this URL with your NGROK public URL
                response = requests.post("http://127.0.0.1:8001/iris/scan", files=files)
                result = response.json()
                st.success(f"Prediction: **{result.get('prediction', 'No result')}**")
            except Exception as e:
                st.error(f"Error: {str(e)}")

# Blood pressure form
st.markdown("---")
st.header("💉 Blood Pressure Check")

with st.form("bp_form"):
    systolic = st.number_input("Systolic", min_value=80, max_value=200, value=120)
    diastolic = st.number_input("Diastolic", min_value=60, max_value=140, value=80)
    submitted = st.form_submit_button("Submit")
    if submitted:
        try:
            response = requests.post("http://127.0.0.1:8001/bp/submit", json={
                "systolic": systolic,
                "diastolic": diastolic
            })
            result = response.json()
            st.success(f"BP Status: **{result.get('status', 'No result')}**")
        except Exception as e:
            st.error(f"Error: {str(e)}")
