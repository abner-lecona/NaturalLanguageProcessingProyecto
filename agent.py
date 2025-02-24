from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
import streamlit as st
import os

# Configuración inicial
os.environ['LANCHAIN_API_KEY'] = "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"
os.environ['LANGCHAIN_TRACING_V2'] = "false"
os.environ['LANGCHAIN_PROJECT'] = "proyecto_chatbot_medico"

# Carga y preparación de documentos contextuales
loader = TextLoader("medical_context.txt")  # Archivos con enfermedades/medicamentos
text_documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
doc_txt = text_splitter.split_documents(text_documents)

# Creación de la base de datos vectorial con FAISS
embeddings = OllamaEmbeddings(model="llama3.2")
db = FAISS.from_documents(doc_txt, embeddings)

# Configuración del LLM
llm = OllamaLLM(model="llama3.2")

# Prompt para estructurar respuestas en JSON
prompt = ChatPromptTemplate.from_template("""
Tu tarea es analizar el texto ingresado y extraer información clave de forma precisa y detallada. El resultado debe presentarse en formato JSON para facilitar su uso. Los campos que necesitas identificar y estructurar son los siguientes: 

- **nombre_paciente**: Nombre completo del paciente.
- **fecha_nacimiento**: Fecha de nacimiento del paciente, en formato DD/MM/AAAA.
- **fecha_consulta**: Fecha de la consulta médica, en formato DD/MM/AAAA.
- **diagnostico**: Diagnóstico principal del paciente, indicado en el texto.
- **medicamento**: Medicamentos recetados, si los hay.
- **dosis**: Dosis de cada medicamento especificado.
- **frecuencia**: Frecuencia con la que se debe administrar cada medicamento.

Debes seguir estos pasos cuidadosamente:
1. Lee el texto proporcionado y entiende el contexto general.
2. Identifica y extrae las entidades mencionadas, asignándolas a los campos requeridos.
3. Verifica que las fechas estén en el formato correcto y corrige inconsistencias si es necesario.
4. Si encuentras múltiples diagnósticos o medicamentos, enuméralos adecuadamente en listas dentro del JSON.
5. Utiliza únicamente el contexto proporcionado en el texto o en la base de datos para inferir detalles adicionales. No asumas información que no está explícitamente indicada.
6. Si falta algún dato en el texto, indícalo en el JSON como `"campo": "No especificado"`.

El formato JSON debe cumplir con el siguiente esquema:

```json

  "nombre_paciente": "string",
  "fecha_nacimiento": "DD/MM/AAAA",
  "fecha_consulta": "DD/MM/AAAA",
  "diagnostico": "string",
  "medicamento": ["string", "string"],
  "dosis": ["string", "string"],
  "frecuencia": ["string", "string"]


<context>
    {context}
</context>
Input: {input}
""")

# Crear las cadenas de procesamiento
document_chain = create_stuff_documents_chain(llm, prompt)
retriever = db.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

# Interfaz en Streamlit
st.title("Asistente Médico - Resúmenes Estructurados")

# Inicializar historial
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Mostrar historial
for message in st.session_state.messages:
    st.write(f"**{message['role'].capitalize()}:** {message['content']}")

# Entrada del usuario
user_input = st.text_input("Ingresa un resumen médico aquí:")

if user_input:
    st.session_state.messages.append({'role': 'user', 'content': user_input})

    try:
        # Procesar con la cadena de recuperación
        response = retrieval_chain.invoke({"input": user_input})

        # Agregar respuesta del asistente al historial
        structured_response = response.get('answer', "No se pudo estructurar la información.")
        st.session_state.messages.append({'role': 'assistant', 'content': structured_response})

        # Mostrar respuesta estructurada
        st.write(f"**Respuesta:** {structured_response}")

    except Exception as e:
        st.error(f"Error: {str(e)}")

# Botón para reiniciar la conversación
if st.button("Reiniciar conversación"):
    st.session_state.messages = [prompt]
