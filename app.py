"""import of libraries."""
import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us_new.csv')  # leer los datos
st.markdown("<h1 style='text-align:center;'> vehicle graphics</h1>",
            unsafe_allow_html=True)

data_button = st.button('visualize data frame', use_container_width=True)
if data_button:

    st.dataframe(car_data)
st.markdown("---")
st.markdown("<h3 style='text-align:center;'> Histogram plot</h3>",
            unsafe_allow_html=True)
#########
col1, col2, col3 = st.columns(3)

if col1.button('types of cars'):
    # escribir un mensaje
    st.write(
        'Creación de un histograma donde se muestra los tipos de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="type")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
elif col2.button('number of cylinders'):
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig2 = px.histogram(car_data, x="model_year",
                        color='condition')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=False)
st.markdown("---")
st.markdown("<h3 style='text-align:center;'> Bar Graphic</h3>",
            unsafe_allow_html=True)
fig3 = px.bar(car_data, x="cylinders", color="type",
              title="type of vehicle cylinder capacity")
st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")
st.markdown("<h3 style='text-align:center;'> scartter plot</h3>",
            unsafe_allow_html=True)
fig4 = px.scatter(car_data, x="model_year", y="price",
                  color='condition')  # crear un gráfico de dispersión
st.plotly_chart(fig4, use_container_width=True)
