import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Decade Comparison")

df = pd.read_csv("data/inequality_data.csv")

df["Decade"] = (df["Year"]//10)*10

fig = px.bar(df, x="Decade", y="Gini_Index")

st.plotly_chart(fig)