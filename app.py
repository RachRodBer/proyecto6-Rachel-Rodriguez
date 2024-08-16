import streamlit as st
import pandas as pd
import plotly_express as px

        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.markdown("# Análisis de venta de autos en Estados Unidos 🚗")
st.markdown("### Una herramienta interactiva para explorar los datos 📊")


hist_button = st.button('Construir histograma') # crear un botón
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:  # al hacer clic en el botón
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("###### Elaborado por: Rachel Rodríguez")