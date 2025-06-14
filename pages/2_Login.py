import streamlit as st
st.title("🔐 Login")
st.text_input("Email")
st.text_input("Password", type="password")
if st.button("Login"):
    st.success("Logged in successfully!")