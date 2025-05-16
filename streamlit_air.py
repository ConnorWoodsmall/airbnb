import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Import or load your data
from data_loader import load_airbnb_data

df = load_airbnb_data()

if 'price' in df.columns:
    df['price'] = df['price'].replace({'\$': '', ',': ''}, regex=True).astype(float)

df = df[['price', 'bedrooms', 'bathrooms', 'accommodates']]

st.title("Interactive Data Visualization")

# Let user select a column
column = st.selectbox("Select a column to visualize:", df.columns)

# Let user select an aggregation
agg_func = st.selectbox("Select aggregation:", ["count"])

# Perform aggregation
if agg_func == "count":
    data = df[column].value_counts()
else:
    data = df.groupby(column).agg(agg_func).iloc[:, 0]

# Plot
st.bar_chart(data)
st.line_chart(data)