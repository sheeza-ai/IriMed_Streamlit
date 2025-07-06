import streamlit as st
import requests

st.set_page_config(page_title="📊 Results History")

st.title("📊 Results History")

if "access_token" not in st.session_state or st.session_state.access_token is None:
    st.error("Please login first from the Login page.")
    st.stop()

try:
    headers = {"Authorization": f"Bearer {st.session_state.access_token}"}
    response = requests.get(
        "http://127.0.0.1:8001/results/history",
        headers=headers
    )
    results = response.json().get("results", [])
    if not results:
        st.info("No results yet.")
    else:
        for r in results:
            st.write(f"**{r['type']}**: {r['value']} at {r['date']}")
except Exception as e:
    st.error(f"Error: {e}")

