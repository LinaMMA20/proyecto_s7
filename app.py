import pandas as pd
import streamlit as st
import plotly.express as px

vehicules = pd.read_csv('../vehicules_env/vehicles_us.csv')
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    fig = px.histogram(vehicules, x="odometer")
     
    st.plotly_chart(fig, use_container_width=True)