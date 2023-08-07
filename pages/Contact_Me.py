import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Typ hier je e-mail adres")
    raw_message = st.text_area("Typ hier boodschap")
    message = f"""\
Subject: Nieuwe mail van {user_email} via Portfolio site

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Versturen!")
    if button:
        send_email(message)
        st.info("Uw email werd succesvol verzonden!")
