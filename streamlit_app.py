import streamlit as st

#st.set_page_config(page_title="Mi App", layout="wide")


st.markdown("""
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #ffffff; /* Blanco puro para combinar con Streamlit */
            color: #6c757d; /* Gris elegante */
            text-align: center;
            padding: 10px 10px;
            font-size: 13px;
            box-shadow: 0 -2px 10px rgba(0,0,0,0.1); /* Sombra suave */
            z-index: 999999 !important;
        }

        section[data-testid="stSidebar"] {
            z-index: 999998 !important;
        }

        .footer {
            animation: slideUp 0.5s ease-out;
        }

        @keyframes slideUp {
            from { transform: translateY(100%); }
            to { transform: translateY(0); }
        }
    </style>

    <div class="footer">
        © 2025 Jose Pampa - Todos los derechos reservados
    </div>
""", unsafe_allow_html=True)

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
    "views/soluciones.py",
    title="Soluciones Cloud",
    icon="☁️",
)

project_2_page = st.Page(
    "views/proyectosia.py",
    title="IA",
    icon="🧠",
)

pg = st.navigation(
    {
        "Personal": [about_page],
        "Proyectos": [project_1_page, project_2_page],
    }
)

pg.run()