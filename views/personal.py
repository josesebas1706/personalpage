import streamlit as st
from forms.contact import contact_form
import streamlit.components.v1 as components
import base64
from math import ceil

@st.dialog("Contacto directo")
def show_contact_form():
    contact_form()

st.title("💻 AutomatizAndo Ando")
st.write("\n")
st.write("\n")

col1, col2 = st.columns(2, gap="large", vertical_alignment="center")
with col1:
    st.image("./resources/profile_image.jpg", use_container_width = True)

with col2:
    st.title("Jose Pampa", anchor=False)
    st.write(
        "Especialista en datos, ayudando a empresas a transformar información en decisiones inteligentes a través de soluciones tecnológicas e innovadoras."
    )
    if st.button("✉️ Contacto", use_container_width = True):
        show_contact_form()
    st.write("\n")

st.write("\n")
st.subheader("Experiencia", anchor=False)
st.write(
    """
    - **+4 años de experiencia** trabajando en áreas de tecnología, innovación y comercial.  
    - Experiencia en el sector de **seguros**, **banca**, **salud**, **marketing** y **educación**.
    - Ingeniero Industrial Titulado por la Universidad Ricardo Palma con especialización en datos.
    - Maestreando el "Magíster en tecnologías de información y gestión" en la Pontificia Universidad Católica de Chile.
    - **+4 años de experiencia** trabajando en área de tecnología, innovación y comercial.  
    - Experiencia en el sector de **seguros**, **banca**, **salud**, **marketing** y **educación**.
    """
)

st.write("\n")
st.subheader("Manager Skills", anchor=False)
st.write(
    """
    - Sólida experiencia práctica con dominio de códigos de programación como Python, R, etc.
    - Buen entendimiento de principios estadísticos y su aplicación en contextos reales.
    - Excelente capacidad para lider proyectos de alto impacto.
    - Excelente capacidad para trabajar en equipo y destacada proactividad en la ejecución de tareas.
    """
)

st.write("\n")
st.subheader("Code Skills", anchor=False)
st.subheader("Skills programación", anchor=False)

st.write(
    """
    - 🚀 **Analytics**: SAS Enterprise Guide. SAS Miner. STATA. SPSS. CANCEIS. MATLAB. Octave. WEKA. Knime. Python. R. Spark. Jupyter. JavaScript. Machine Learning Studio, Cloudera, Google Analytics, Julia, PHP, html, CSS, app script.
    - 💾 **BBDD**: AWS, Azure, Oracle. SQL Server. My SQL. Teradata. SAP HANA, PostgreSQL, Mongo DB, SQLite, Big Query, Snowflake.
    - 📊 **Data Viz**: Reportlab. Power BI. Tableau. Shiny. Plotly. Qlik Sense, SAS Graph, SAS Visual Analytics. Sisense, D3, Superset, Data Studio, Looker, Superset.
    - ⚙️ **Softwares**: Hubspot API, Facebook API, Instagram API, Salesforce API, TikTok API, Vtiger, Zoho CRM, Microsoft Dynamics 365, Monday.com, Pipedrive, Freshsales, Zendesk Sell, Oracle CRM.
    - 💻 **Skills IA**: TensorFlow, PyTorch, Keras. SpaCy, NLTK, Transformers. OpenCV, YOLO, TensorFlow Object Detection. OpenAI Gym, Stable Baselines. GANs, VAEs. Facebook Prophet, ARIMA, LSTMs, XGBoost. H2O.ai, DataRobot, Auto-sklearn. MLflow, TensorFlow Serving, Docker, Kubernetes, Streamlit, Flask, FastAPI. Genetic Algorithms.
    """
)

st.write("\n")

st.subheader("Empresas e Instituciones", anchor=False)

st.subheader("Empresas", anchor=False)

st.write("\n")

def img_to_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

image_paths = [
    "resources/aunaperu_logo.jpg",
    "resources/352355201_110830012023987_4777561299793745994_n.png",
    "resources/channels4_profile.jpg",
    "resources/images.png",
    "resources/393362626_714691694028294_5300743196677862365_n.jpg",
    "resources/352355201_110830012023987_4777561299793745994_n.png",
    "resources/channels4_profile.jpg"
]

image_base64_list = [img_to_base64(path) for path in image_paths]

from math import ceil

# Agrupar las imágenes en grupos de 3

group_size = 3
num_slides = ceil(len(image_base64_list) / group_size)

carousel_items_html = ""

for i in range(num_slides):

    group_imgs = image_base64_list[i*group_size:(i+1)*group_size]
    
    # Cada slide tendrá hasta 3 imágenes
    group_imgs = image_base64_list[i*group_size:(i+1)*group_size]
    
    # Construimos el div del slide con las 3 imágenes
    
    images_html = "".join(
        f'<div class="col-4"><img src="data:image/jpeg;base64,{img_b64}" class="d-block w-100" alt="Imagen {i*group_size + idx + 1}"></div>'
        for idx, img_b64 in enumerate(group_imgs)
    )
    
    carousel_items_html += f'''
    <div class="carousel-item{' active' if i == 0 else ''}">
      <div class="row">
        {images_html}
      </div>
    </div>
    '''

carousel_html = f"""
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
<style>
  .carousel-item {{
    background-color: #F4F6F9;
    overflow: hidden;
    transition: transform 4s ease;
    border-radius: 8px;
    overflow: hidden;
    transition: transform 2s ease;
  }}
  .carousel-item img {{
    height: 200px;
    object-fit: contain;
    border-radius: 8px;
    width: auto!important;
    overflow: hidden;
    box-shadow: 0 4px 4px rgba(0, 0, 0, 0.1);
  }}
</style>
<div id="carouselExample" class="carousel slide" data-bs-ride="carousel" data-bs-interval="3000" data-bs-wrap="true">
  }}
</style>
<div id="carouselExample" class="carousel slide" data-bs-ride="carousel" data-bs-interval="2500" data-bs-wrap="true">
  <div class="carousel-inner">
    {carousel_items_html}
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
"""

components.html(carousel_html, height=200)