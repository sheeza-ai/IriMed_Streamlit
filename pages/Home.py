import streamlit as st

st.set_page_config(page_title="IriMed Home", page_icon="🧿", layout="centered")

st.title("👁️ IriMed: Detect Diabetes Through Your Eyes")
st.subheader("Using Iris Image & Artificial Intelligence")

st.image(
    "https://cdn.pixabay.com/photo/2020/04/06/20/38/eye-5009871_1280.jpg",
    use_container_width=True,
    caption="AI-Powered Iris Scan for Diabetes Detection"
)

st.markdown("""
Welcome to **IriMed** – an AI-driven diagnostic platform that detects **diabetes** using a non-invasive iris scan.

### 🌟 Key Features:
- 📷 Upload iris images for real-time diabetes detection
- 🩺 Manually input blood pressure
- 📊 View health report history
- 👨‍⚕️ Consult with a doctor

---

🚀 **Use the left sidebar to start.**
""")
