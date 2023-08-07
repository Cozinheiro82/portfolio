import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Danny Veugelen")
    content = """Hallo, Ik ben Danny! Geboren in Leuven op 17 December 1982. 
    Na 17 jaar als chauffeur werk ik nu als instructeur bij de Lijn.
    Ik ben gehuwd en heb 2 kinderen.
    In mijn vrije tijd hou ik me bezig met cursussen programmeren.
    """
    st.info(content)

content2 = """
Hieronder vind je enkele Apps die ik reeds heb gemaakt met Python-code. 
Voel je vrij mij te contacteren!"""
st.write(content2)