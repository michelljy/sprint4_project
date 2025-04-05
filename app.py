import streamlit as st
import pandas as pd
import plotly.express as px

# Load your dataset
df = pd.read_csv('vehicles_us.csv')

# Add a header
st.header('Car Sales Dashboard')

# Add a checkbox
show_histogram = st.checkbox('Show Histogram')

# Conditional display of the histogram
if show_histogram:
    fig_hist = px.histogram(df, x='model_year', title='Distribution of Car Model Years')
    st.plotly_chart(fig_hist)
    
# Scatterplot display
fig_scatter = px.scatter(df, x='price', y='odometer', title='Price vs. Odometer')
st.plotly_chart(fig_scatter)
