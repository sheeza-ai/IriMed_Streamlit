import streamlit as st
import datetime

st.title("👨‍⚕️ Doctor Consultation")

# --- Doctor Static Info ---
st.subheader("Doctor Name")
st.write("Specialist in Iridology & Internal Medicine")
st.write("🗓️ Available: Monday to Friday")
st.write("📍 Location: IriMed Health Clinic")

# --- Live Video/Chat Link ---
with st.expander("💬 Live Chat / Video Consultation"):
    st.write("Join a live session with your doctor:")
    st.markdown("[Join Video Call](https://meet.jit.si/irimed-consultation-room)", unsafe_allow_html=True)

# --- Appointment Booking Form ---
st.markdown("---")
st.header("🗓️ Book an Appointment")
with st.form("appointment_form"):
    name = st.text_input("Your Name")
    date = st.date_input("Preferred Date", min_value=datetime.date.today())
    time = st.time_input("Preferred Time", value=datetime.time(10, 0))
    submitted = st.form_submit_button("Book Appointment")

    if submitted:
        st.success(f"Appointment booked for {name} on {date} at {time}.")

# --- Doctor Login Panel (Static Only) ---
st.markdown("---")
st.header("🔐 Doctor Login Panel")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
if st.button("Login"):
    if username == "admin" and password == "admin":  # Replace with real auth later
        st.success("Login successful! View upcoming appointments.")
        st.info("(Feature under development)")
    else:
        st.error("Invalid credentials")

# --- Doctor Review System ---
st.markdown("---")
st.header("⭐ Doctor Reviews")
st.write("Leave a review for your consultation experience:")
review = st.text_area("Your review")
rating = st.slider("Rating", 1, 5, 4)
if st.button("Submit Review"):
    st.success("Thank you! Your feedback has been submitted.")
