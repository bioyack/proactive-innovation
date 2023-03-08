import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

def obtener_respuesta(pregunta):
    opciones = ["Totalmente en desacuerdo", "En desacuerdo", "Ni de acuerdo ni en desacuerdo", "De acuerdo", "Totalmente de acuerdo"]
    
    
    # --- DISPLAY IMAGE & DATAFRAME
    col1, col2 = st.columns([35, 400])
    image = Image.open('images/Escala.jpg')
    col1.image(image)
    opcion_seleccionada = col2.radio(pregunta, opciones)
        
    #opcion_seleccionada = st.radio(pregunta, opciones)

    opciones_numeradas = {"Totalmente en desacuerdo": 1, "En desacuerdo": 2, "Ni de acuerdo ni en desacuerdo": 3, "De acuerdo": 4, "Totalmente de acuerdo": 5}
    numero_seleccionado = opciones_numeradas[opcion_seleccionada]

    return numero_seleccionado


def main():
    st.set_page_config(page_title="PROACTIVE", page_icon=":rocket:")
    header = st.container()
    with header:
        st.image("images/HeaderPROACTIVE.jpg", use_column_width=True)
        #st.subheader("A tool to converting caffeine into innovation")
    # Creamos el menú
    menu = ["Priorities", "Relevant challenges", "Order blocks", "Alliances", "Culture", "Trends", "Inventions", "Verify progress", "Experience"]
    choice = st.sidebar.radio("Una herramienta para convertir la cafeína en innovación :-).", menu)
    
    if choice == "Priorities":
        st.title("Priorities")
#-----------------------
        st.subheader("Diagnóstico")
        tabs = ["Instrucciones", "Diagnóstico", "Reporte"]
        selected_tab = st.selectbox("Selecciona una pestaña", tabs)
        if selected_tab == "Instrucciones":
            st.subheader("Instrucciones para Diagnóstico")
            st.write("Por favor, sigue los siguientes pasos:")
            st.write("1. Primero, crea una copia de este documento con el nombre: Modulo_2_Nombre del Alumno")
            st.write("2. Luego, elije una organización a evaluar")
            st.write("3. Después, Aplique el cuestionario de la pestaña Evaluación (consulte a quienes considere necesario para responder las preguntas a conciencia), ELIJA ENTRE: TOTALMENTE EN DESACUERDO,	EN DESACUERDO,NI DE ACUERDO NI EN DESACUERDO,DE ACUERDO,TOTALMENTE DE ACUERDO CLICKEANDO EN EL RADIOBUTTON CORRESPONDIENTE.")
            st.write("4. Continúa en la Pestaña Reporte, agregando todas las observaciones que entienda pertinentes para cada elemento del método PROACTIVE.")
            st.write("5. Finalmente, completar el campo: Nombre de la Institución, guardar.")
        elif selected_tab == "Diagnóstico":
#---------------------
            respuesta_seleccionada1 = obtener_respuesta("¿Están establecidas las herramientas para identificar las necesidades actuales y futuras de los clientes y las actividades de la competencia para mejorar o crear nuevos productos o servicios? *Hay un sistema de identificción de las necesidades actuales y futuras de los clientes y las actividades de la competencia para crear nuevos productos y servicios, o hacer mejores los existentes.")
            st.write(f"Respuesta seleccionada: {respuesta_seleccionada1}")
#---------------------
            respuesta_seleccionada2 = obtener_respuesta("¿El sistema de gestión de la innovación está conectado a las fuentes de datos clave y sistemas empresariales? *Hay un sistema de recompensas y reconocimientos diseñado para motivar y reconocer a quienes contribuyen con innovaciones alineadas con las necesidades de la organización.")
            st.write(f"Respuesta seleccionada: {respuesta_seleccionada2}")
#---------------------



        else:
            st.write("Contenido de la pestaña 3 del grupo 1")
#-----------------------
    elif choice == "Relevant challenges":
        st.title("Relevant challenges")
    
    elif choice == "Order blocks":
        st.title("Order blocks")

    elif choice == "Alliances":
        st.title("Alliances")

    elif choice == "Culture":
        st.title("Culture")

    elif choice == "Trends":
        st.title("Trends")

    elif choice == "Inventions":
        st.title("Inventions")

    elif choice == "Verify progress":
        st.title("Verify progress")

    elif choice == "Experience":
        st.title("Experience")
   

if __name__ == "__main__":
    main()
