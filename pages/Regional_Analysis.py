import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Regional Inequality Analysis")

df = pd.read_csv("data/inequality_data.csv")

# Country wise average inequality
country_data = df.groupby("Country")["Gini_Index"].mean().reset_index()

fig = px.pie(
    country_data,
    names="Country",
    values="Gini_Index",
    title="Inequality Distribution by Country"
)

st.plotly_chart(fig, use_container_width=True)