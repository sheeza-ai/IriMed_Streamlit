import streamlit as st

st.set_page_config(page_title="IriMed Home", page_icon="🧿")

st.title("👁️ IriMed: Detect Diabetes Through Your Eyes")
st.subheader("AI-driven health diagnostics")

st.image(
    "https://cdn.pixabay.com/photo/2020/04/06/20/38/eye-5009871_1280.jpg",
    caption="AI-powered Iris Scan for Diabetes Detection",
    use_column_width=True
)

st.markdown("""
Welcome to **IriMed** – an AI-powered app to detect diabetes through your iris image.
Use the sidebar to navigate to:
- Login
- Iris Scan
- Blood Pressure
- Results
- Doctor
""")
