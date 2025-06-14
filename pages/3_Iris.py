import streamlit as st
import requests

st.title("👁️ Iris Scan")
uploaded_file = st.file_uploader("Upload an iris image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    if st.button("Predict"):
        files = {
            "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
        }
        try:
            response = requests.post("http://127.0.0.1:8001/iris/scan", files=files)
            prediction = response.json().get("prediction")
            if prediction:
                st.success(f"Prediction: {prediction}")
            else:
                st.warning("No prediction returned from backend.")
        except Exception as e:
            st.error(f"Failed to get prediction: {e}")
