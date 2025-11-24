import streamlit as st

st.set_page_config(page_title="Formulario Interactivo", page_icon="📝", layout="centered")
st.title("Selecciona tu tipo de Dataset")

# Opciones del selector
opcion = st.radio(
    "Elige un tipo de Dataset:",
    ("Datasets con más contexto", "Datasets de campo especializado", "Datasets mixtos / adaptativos")
)

# Dependiendo de la opción, mostrar secciones diferentes
if opcion == "Datasets con más contexto":
    st.subheader("Sección para Datasets con más contexto")
    st.text("Aquí puedes agregar inputs, sliders o cualquier otro elemento.")
    st.text_input("Nombre del dataset")
    st.slider("Nivel de complejidad", 0, 10)

elif opcion == "Datasets de campo especializado":
    st.subheader("Sección para Datasets de campo especializado")
    st.text("Aquí puedes agregar otros inputs específicos.")
    st.text_input("Área de especialización")
    st.selectbox("Tipo de análisis", ["Análisis A", "Análisis B", "Análisis C"])

elif opcion == "Datasets mixtos / adaptativos":
    st.subheader("Sección para Datasets mixtos / adaptativos")
    st.text("Aquí puedes agregar formularios personalizados.")
    st.text_input("Descripción del dataset")
    st.checkbox("Incluye datos de campo y contexto")

# Mensaje opcional al final
st.markdown("---")
st.success("Formulario interactivo listo para usar!")
