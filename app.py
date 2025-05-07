import pandas as pd
import streamlit as st
import plotly.express as px

st.header('Anuncios de vehículos en venta')

df = pd.read_csv('vehicules_env\\vehicles_us.csv')

#grafica 1
df['manufacturer'] = df['model'].str.split().str[0]
ads_count = df['manufacturer'].value_counts().reset_index()
ads_count.columns = ['manufacturer', 'ad_count']


st.title('Data Viewer - Vehículos')
show_small = st.checkbox('Mostrar solo fabricantes con menos de 1000 anuncios')

if show_small:
    filtered_data = ads_count[ads_count['ad_count'] < 1000]
else:
    filtered_data = ads_count

fig = px.bar(
    filtered_data.sort_values('ad_count', ascending=False),
    x='manufacturer',
    y='ad_count',
    title='Cantidad de anuncios por fabricante',
    labels={'manufacturer': 'Fabricante', 'ad_count': 'Cantidad de anuncios'},
    color='ad_count',
    color_continuous_scale='Blues'
)

st.plotly_chart(fig, use_container_width=True)

st.write(filtered_data)

#grafica 2
grouped = df.groupby(['manufacturer','type']).size().reset_index(name='count')

st.title('Tipos de vehículos por fabricante')

fig = px.bar(
    grouped,
    x='manufacturer',
    y='count',
    color='type',
    title='Tipos de vehículos por fabricante',
    barmode='overlay',
    labels={'count': 'Cantidad', 'manufacturer': 'Fabricante', 'type': 'Tipo de vehículo'},
    color_discrete_sequence=px.colors.qualitative.Plotly,
    )
st.write(fig)

#grafica 3
data_clean = df.dropna(subset=['price', 'manufacturer'])
data_clean = data_clean[data_clean['price'] < 100000] 

st.title('Comparación de precios por fabricante')

manufacturers = data_clean['manufacturer'].unique()
selected = st.multiselect(
    'Selecciona 2 fabricantes para comparar:',
    options=manufacturers,
    default=manufacturers[:2],
)

if len(selected) != 2:
    st.warning('Por favor selecciona exactamente 2 fabricantes.')
else:
    filtered_data = data_clean[data_clean['manufacturer'].isin(selected)]

fig = px.scatter(
    filtered_data,
    x='price',
    color='manufacturer',
    title='Comparación de precios entre fabricantes',
    labels={'price': 'Precio', 'manufacturer': 'Fabricante'},
    color_discrete_sequence=px.colors.qualitative.Set2
)

st.plotly_chart(fig)