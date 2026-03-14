import streamlit as st
import pandas as pd

# ---------------- LOGIN CHECK ---------------- #

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first")
    st.stop()

# ---------------- PAGE TITLE ---------------- #

st.title("AI Insights on Global Inequality")

# ---------------- LOAD DATA ---------------- #

df = pd.read_csv("data/inequality_data.csv")

df.columns = df.columns.str.strip().str.lower()

# ---------------- BASIC METRICS ---------------- #

avg_gini = round(df["gini_index"].mean(), 2)

highest = df.sort_values("gini_index", ascending=False).head(5)
lowest = df.sort_values("gini_index", ascending=True).head(5)

st.subheader("Global Inequality Overview")

col1, col2 = st.columns(2)

with col1:
    st.metric("Average Global Gini Index", avg_gini)

with col2:
    st.metric("Total Countries", df["country"].nunique())

st.divider()

# ---------------- TOP INEQUALITY ---------------- #

st.subheader("Countries With Highest Inequality")

st.dataframe(highest[["country","year","gini_index"]])

# ---------------- LOWEST INEQUALITY ---------------- #

st.subheader("Countries With Lowest Inequality")

st.dataframe(lowest[["country","year","gini_index"]])

# ---------------- AI STYLE INSIGHT ---------------- #

st.subheader("AI Insight")

st.info(
"""
Countries with a **higher Gini Index** tend to have a larger income gap between the rich and the poor.

Tracking inequality trends over time helps policymakers understand economic imbalance and design better policies for wealth distribution.
"""
)