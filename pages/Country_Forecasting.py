import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Country Forecasting")

df = pd.read_csv("data/inequality_data.csv")

country = st.selectbox("Select Country", df["Country"].unique())

data = df[df["Country"] == country]

fig = px.line(data, x="Year", y="Gini_Index")

st.plotly_chart(fig)

st.info("Prediction trend visualization")