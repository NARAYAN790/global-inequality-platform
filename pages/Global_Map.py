import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Interactive Global Inequality Map")

df = pd.read_csv("data/inequality_data.csv")

fig = px.scatter_geo(
    df,
    lat="Latitude",
    lon="Longitude",
    size="Gini_Index",
    color="Gini_Index",
    hover_name="Country"
)

st.plotly_chart(fig)