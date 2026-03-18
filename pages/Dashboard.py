import streamlit as st
import pandas as pd
import plotly.express as px

# LOGIN CHECK
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first")
    st.stop()

st.title("📊 Income Inequality Dashboard")

# LOAD DATA
df = pd.read_csv("data/inequality_data.csv")

# ----------- METRICS -----------

col1, col2, col3 = st.columns(3)

col1.metric("Countries Tracked", df["Country"].nunique())
col2.metric("Average Gini Index", round(df["Gini_Index"].mean(),2))
col3.metric("Latest Year", df["Year"].max())

st.divider()

# ----------- BAR CHART -----------

st.subheader("Income Inequality by Country")

fig = px.bar(
    df,
    x="Country",
    y="Gini_Index",
    title="Income Inequality by Country"
)

st.plotly_chart(fig, use_container_width=True)

# ----------- TREND CHART -----------

st.subheader("Inequality Trend Over Time")

fig2 = px.line(
    df,
    x="Year",
    y="Gini_Index",
    color="Country"
)

st.plotly_chart(fig2, use_container_width=True)

# ----------- DATA TABLE -----------

st.subheader("Dataset Preview")

st.dataframe(df)
