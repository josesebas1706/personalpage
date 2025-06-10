import streamlit as st

#st.set_page_config(page_title="Mi App", layout="wide")

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Lato&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Lato', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

about_page = st.Page(
    "views/personal.py",
    title="¿Quien soy?",
    icon="🧑",
    default=True,
)

project_1_page = st.Page(
    "views/funciones.py",
    title="IA",
    icon="📊",
)

pg = st.navigation(
    {
        "Personal": [about_page],
        "Proyectos": [project_1_page],
    }
)

pg.run()