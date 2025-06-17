import re
import streamlit as st


def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def is_valid_phone(phone):
    phone_pattern = r"^\d{6,12}$"
    return re.match(phone_pattern, phone) is not None


def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Nombre")
        email = st.text_input("Correo")
        celular = st.text_input("Celular", max_chars = 9)
        message = st.text_area("Dejame un comentario")
        submit_button = st.form_submit_button("Enviar", use_container_width = True)

    if submit_button:

        if not name:
            st.error("Por favor completa el campo de nombre.", icon="🧑")
            st.stop()

        if not email:
            st.error("Por favor completa el campo de email.", icon="📨")
            st.stop()

        if not is_valid_email(email):
            st.error("Por favor escribe un email válido.", icon="📧")
            st.stop()

        if not celular:
            st.error("Por favor completa el campo de celular.", icon="📨")
            st.stop()

        if not is_valid_phone(celular):
            st.error("Por favor escribe un celular válido.", icon="📧")
            st.stop()

        if not message:
            st.error("Por favor completa el campo de comentario.", icon="💬")
            st.stop()

        data = {"email": email, "name": name, "message": message}