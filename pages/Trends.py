import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- LOGIN CHECK ---------------- #

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first")
    st.stop()

# ---------------- PAGE TITLE ---------------- #

st.title("Global Inequality Trends")

# ---------------- LOAD DATA ---------------- #

df = pd.read_csv("data/inequality_data.csv")

df.columns = df.columns.str.strip().str.lower()

# ---------------- GLOBAL TREND ---------------- #

trend = df.groupby("year")["gini_index"].mean().reset_index()

fig = px.line(
    trend,
    x="year",
    y="gini_index",
    markers=True,
    title="Average Global Inequality Over Time"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------- DATA TABLE ---------------- #

st.subheader("Trend Data")

st.dataframe(trend)