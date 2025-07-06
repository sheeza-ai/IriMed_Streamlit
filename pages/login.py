import streamlit as st
import requests

st.set_page_config(page_title="🔐 Login", page_icon="🔑")

st.title("🔐 Login")

# --- Session State to store token ---
if "access_token" not in st.session_state:
    st.session_state.access_token = None

# --- Login Form ---
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")

    if submitted:
        if not username or not password:
            st.warning("Please fill in both username and password.")
        else:
            # send to FastAPI /auth/token
            try:
                response = requests.post(
                    "http://127.0.0.1:8001/auth/token",
                    data={"username": username, "password": password}
                )
                if response.status_code == 200:
                    data = response.json()
                    st.session_state.access_token = data["access_token"]
                    st.success("✅ Login successful!")
                    st.experimental_rerun()
                else:
                    st.error("❌ Invalid username or password.")
            except Exception as e:
                st.error(f"Error connecting to backend: {e}")

# --
