import streamlit as st
import pandas


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
Voel je vrij mij hierover te contacteren!"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    #for index, row in df[:10].iterrows():
    for index, row in df[:1].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=350)
        st.write(f"[Ga naar project]({row['url']})")

with col4:
    #for index, row in df[10:].iterrows():
    for index, row in df[1:2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=350)
        st.write(f"[Ga naar project]({row['url']})")
