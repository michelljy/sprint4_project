import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header('Car Sales Dashboard')

show_histogram = st.checkbox('Show Histogram')

if show_histogram:
    fig_hist = px.histogram(df, x='model_year', title='Distribution of Car Model Years')
st.plotly_chart(fig_hist)
   

fig_scatter = px.scatter(df, x='price', y='odometer', title='Price vs. Odometer')
st.plotly_chart(fig_scatter)
