import streamlit as st

st.set_page_config(page_title="🚪 Logout")

st.title("🚪 Logout")

if st.button("Confirm Logout"):
    st.session_state.access_token = None
    st.success("You have been logged out.")

