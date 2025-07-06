import streamlit as st
import requests

st.set_page_config(page_title="👁️ Iris Scan")

st.title("👁️ Iris Scan")

if "access_token" not in st.session_state or st.session_state.access_token is None:
    st.error("Please login first from the Login page.")
    st.stop()

uploaded_file = st.file_uploader("Upload an iris image", type=["jpg","png","jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded", use_column_width=True)
    if st.button("Analyze"):
        try:
            files = {"file": uploaded_file.getvalue()}
            headers = {"Authorization": f"Bearer {st.session_state.access_token}"}
            response = requests.post(
                "http://127.0.0.1:8001/iris/scan",
                files={"file": uploaded_file},
                headers=headers
            )
            data = response.json()
            st.success(f"Prediction: {data.get('prediction')}")
        except Exception as e:
            st.error(f"Error: {e}")
