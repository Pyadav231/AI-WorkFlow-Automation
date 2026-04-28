import streamlit as st
import requests

st.title("AI Email Automation System")

email = st.text_area("Enter your email:")

if st.button("Process"):
    if email.strip():
        response = requests.post(
            "http://127.0.0.1:8000/process-email",
            json={"email": email}
        )
        result = response.json()

        st.write("### Result:")
        st.json(result)
    else:
        st.warning("Please enter email text")