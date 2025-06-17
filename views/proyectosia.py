import streamlit as st
import base64
import google.generativeai as genai

st.title("🧠 Proyectos IA")
genai.configure(api_key='AIzaSyBRtzna5BcUk7YFirHBDFP0PKXbclpLW8Q')

def generative_table_invoice(image):
    model = genai.GenerativeModel(model_name='gemini-2.0-flash-exp')
    prompt = """
    Eres un GPT usado en una página de consultoría de Jose Pampa para leer una imagen y dar sus datos más relevantes.
    Primero saluda al usuario (Saludo general. Ejemplo. Hola! y explica que tipo de GPT eres.)
    Segundo entrega las siguientes informaciones de la imagen:
    1. ENTERPRISE (The enterprise finish in SA or SAC always) of the transaction. Called this as "Empresa".
    2. NAME OF THE BANK (VIA OR BANK IN THE PICTURE, NOT USE ANOTHER). Called this as "Banco"
    3. The DATETIME of the transaction (Format in DD/MM/YY HH:MM)) Called this as "Fecha de transacción".
    4. The AMOUNT Called this as "Monto"
    5. The CURRENCY TYPE (Only two ways in "S/" or "$") Called this as "Tipo de moneda"
    """
    with open(image, "rb") as img_file:
        image_data = img_file.read()
    response = model.generate_content(
        [prompt, {"mime_type": "image/jpeg", "data": image_data}],
        stream=False
    )
    return response.text

def generative_table_invoice_from_text(user_text):
    model = genai.GenerativeModel(model_name='gemini-1.5-pro-latest')
    prompt = """
    Eres un GPT usado en una página de consultoría de Jose Pampa para conversar el usuario en lo que necesite. Eres como un asesor que lo asesora y recomendará en todo momento tomar la consultoría de Jose Pampa.
    Puede hacerte preguntas abiertas sobre que soluciones aplicadas para un problema con datos, procura responder algo muy básico y que si quieren una solución más profunda podría tomar nuestra consultoría.
    Si te pregunta algo fuera de eso, responde que no puedes responder nada adicional a ayudarlo a solucionar problemas vinculados a data.
    """
    full_input = prompt + "\n\nTexto del usuario:\n" + user_text
    response = model.generate_content(full_input, stream=False)
    return response.text

def get_image_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_yape = get_image_base64("./resources/captura_yape.jpg")

st.markdown("""
    <style>
        .custom-container {
            background-color: white;
            border-radius: 8px;
            padding: 10px;
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
        
        .custom-text-gpt {
            background-color: white;
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

st.write("\n")
st.subheader("🔍 GPT con imágenes", anchor=False)
st.write("Integración de api GPT para lecutra y extracción de información.")

col1, col2= st.columns(2, gap="large", vertical_alignment="center")
with col1:
    st.markdown(f"""
        <div class="custom-container">
            <img src="data:image/png;base64,{img_yape}">
        </div>
    """, unsafe_allow_html=True)

with col2:
    if st.button("🧠 GPT Api", use_container_width = True):
        respuesta = generative_table_invoice("./resources/captura_yape.jpg")
        st.markdown(f"""
            <div class="custom-text-gpt">
                {respuesta}
            </div>
        """, unsafe_allow_html=True)

st.write("\n")
st.write("\n")
st.subheader("🗨️ GPT como asistente virtual", anchor=False)
st.write("Integración de api de GPT para poder simular un asistente virtual.")

with st.form("virtual-assitance-form"):
    message = st.text_area("¿Que problema con datos tienes actualmente?")
    submit_button = st.form_submit_button("🧠 Consultar a GPT", use_container_width = True)
    if submit_button:
        respuesta_usuario = generative_table_invoice_from_text(message)
        st.write(respuesta_usuario)