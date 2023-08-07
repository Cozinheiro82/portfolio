import streamlit as st

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Typ hier je e-mail adres")
    message = st.text_area("Typ hier boodschap")
    button = st.form_submit_button("Versturen!")
    if button:
        print("Pressed")
