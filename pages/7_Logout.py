import streamlit as st

st.title("🚪 Logout")

st.write("Are you sure you want to logout?")

if st.button("✅ Confirm Logout"):
    st.success("You have been logged out.")
    st.info("Please close the browser tab or restart the app to login again.")

