import streamlit as st
import base64

st.title("☁️ Soluciones Cloud")
st.write("\n")

def get_image_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_google = get_image_base64("./resources/Google-cloud.png")
img_aws = get_image_base64("./resources/aws-color.png")
img_azure = get_image_base64("./resources/azure_logo_794_new.png")

st.markdown("""
    <style>
        .custom-container {
            background-color: white;
            border-radius: 8px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .custom-container img {
            border-radius: 8px;
            width: 100%;
            height: auto;
        }
        .custom-container:hover {
            transform: scale(1.05);
            transition: transform 0.3s ease;
        }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown(f"""
        <div class="custom-container">
            <img src="data:image/png;base64,{img_google}">
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="custom-container">
            <img src="data:image/png;base64,{img_aws}">
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="custom-container">
            <img src="data:image/png;base64,{img_azure}">
        </div>
    """, unsafe_allow_html=True)

st.write("\n")
st.write("\n")
st.subheader("⚙️ Automatización", anchor=False)
st.write("Integración de servicios gratuitos y low cost para seguimiento de indicadores.")
st.write("\n")

st.image(image = "./resources/Untitled-2025-06-11-1117.png")

st.write("\n")
st.subheader("⚡ Optimización", anchor=False)
st.write("Optimización de carga y estructura tablas en Athena en AWS para simplificar pesos de archivos y redudancia de datos.")
st.write("\n")

st.image(image = "./resources/diagrama_optimizacion.png")

st.write("\n")
st.subheader("🗂️ Proyectos", anchor=False)
st.write("Gestión de proyectos en migración de base de datos onpremise a Azure Studio, utilizando servicios de integración, storage y visualización.")
st.write("\n")

st.image(image = "/workspaces/personalpage/resources/diagrama-proyectos.png")