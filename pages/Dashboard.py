import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Income Inequality Dashboard")

df = pd.read_csv("data/inequality_data.csv")

fig = px.bar(df, x="Country", y="Gini_Index", title="Income Inequality by Country")

st.plotly_chart(fig, use_container_width=True)

fig2 = px.line(df, x="Year", y="Gini_Index", color="Country")

st.plotly_chart(fig2, use_container_width=True)