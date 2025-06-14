import streamlit as st
import requests

st.title("📊 Results History")

try:
    # ✅ Corrected URL
    response = requests.get("http://127.0.0.1:8001/results/results/history")
    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])

        if not results:
            st.info("No diagnostic results available yet.")
        else:
            for result in results:
                result_type = result.get("type", "Unknown")
                value = result.get("value", "N/A")
                date = result.get("date", "Unknown Date")

                st.markdown(f"""
                ### 🔸 {result_type.capitalize()}
                - **Result:** {value}  
                - **Date:** {date}
                """)
    else:
        st.error("Failed to fetch results from backend.")
except Exception as e:
    st.error(f"Error: {e}")
